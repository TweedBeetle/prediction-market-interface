"""Real-time WebSocket client for Kalshi prediction market API.

Provides persistent connections to Kalshi WebSocket endpoints with:
- Automatic reconnection with exponential backoff
- Message parsing and routing
- Channel subscription/unsubscription
- Connection pooling
- Graceful error recovery
"""

import asyncio
import json
import uuid
from typing import Optional, Callable, Dict, Any, Set, List
from datetime import datetime, timedelta
from enum import Enum

import websockets
from loguru import logger


class WebSocketChannel(str, Enum):
    """Available WebSocket channels."""
    TICKER = "ticker"  # Real-time market price updates
    ORDERBOOK_SNAPSHOT = "orderbook_snapshot"  # Full orderbook state
    ORDERBOOK_DELTA = "orderbook_delta"  # Incremental orderbook changes
    TRADES = "trades"  # Public trade execution feed
    USER_FILLS = "user_fills"  # Authenticated user order fills
    USER_POSITIONS = "user_positions"  # Authenticated user position updates
    COMMUNICATIONS = "communications"  # RFQ and quote notifications


class ConnectionState(str, Enum):
    """WebSocket connection states."""
    DISCONNECTED = "disconnected"
    CONNECTING = "connecting"
    CONNECTED = "connected"
    RECONNECTING = "reconnecting"
    CLOSED = "closed"


class KalshiWebSocketClient:
    """Real-time WebSocket client for Kalshi API.

    Manages persistent WebSocket connections with automatic reconnection,
    message routing, and subscription management.
    """

    BASE_URL = "wss://api.elections.kalshi.com/trade-api/v2/ws"
    MAX_RECONNECT_ATTEMPTS = 5
    INITIAL_RECONNECT_DELAY = 1.0  # seconds
    MAX_RECONNECT_DELAY = 60.0  # seconds

    def __init__(
        self,
        api_key_id: str,
        private_key_pem: str,
        timeout: float = 30.0,
    ):
        """Initialize WebSocket client.

        Args:
            api_key_id: API key ID for authentication
            private_key_pem: Private key PEM string for authentication
            timeout: Request timeout in seconds
        """
        self.api_key_id = api_key_id
        self.private_key_pem = private_key_pem
        self.timeout = timeout

        self.connection_id = str(uuid.uuid4())
        self.state = ConnectionState.DISCONNECTED
        self.websocket: Optional[Any] = None  # WebSocket connection (type varies by websockets version)

        # Subscription management
        self.subscribed_channels: Set[str] = set()
        self.subscribed_tickers: Set[str] = set()

        # Message callbacks (channel -> list of async callbacks)
        self.callbacks: Dict[str, List[Callable[[Dict[str, Any]], None]]] = {}

        # Reconnection management
        self.reconnect_task: Optional[asyncio.Task] = None
        self.reconnect_attempts = 0
        self.last_reconnect_time = datetime.now()

        # Message queue for processing
        self.message_queue: asyncio.Queue = asyncio.Queue()
        self.message_processor_task: Optional[asyncio.Task] = None

    async def connect(self) -> bool:
        """Establish WebSocket connection.

        Returns:
            True if connection successful, False otherwise
        """
        if self.state != ConnectionState.DISCONNECTED:
            logger.warning(f"Cannot connect: current state is {self.state}")
            return False

        self.state = ConnectionState.CONNECTING
        logger.info(f"Connecting WebSocket ({self.connection_id})")

        try:
            self.websocket = await asyncio.wait_for(
                websockets.connect(self.BASE_URL),
                timeout=self.timeout,
            )

            self.state = ConnectionState.CONNECTED
            self.reconnect_attempts = 0
            logger.info(f"WebSocket connected ({self.connection_id})")

            # Start message processor
            self.message_processor_task = asyncio.create_task(self._process_messages())

            # Start message listener
            asyncio.create_task(self._listen_for_messages())

            return True

        except asyncio.TimeoutError:
            logger.error(f"Connection timeout ({self.connection_id})")
            self.state = ConnectionState.DISCONNECTED
            return False
        except Exception as e:
            logger.error(f"Connection failed: {e} ({self.connection_id})")
            self.state = ConnectionState.DISCONNECTED
            return False

    async def disconnect(self) -> None:
        """Gracefully disconnect WebSocket.

        Cancels reconnection, closes message processor, and closes connection.
        """
        logger.info(f"Disconnecting WebSocket ({self.connection_id})")
        self.state = ConnectionState.CLOSED

        # Cancel reconnection task
        if self.reconnect_task:
            self.reconnect_task.cancel()
            try:
                await self.reconnect_task
            except asyncio.CancelledError:
                pass

        # Cancel message processor
        if self.message_processor_task:
            self.message_processor_task.cancel()
            try:
                await self.message_processor_task
            except asyncio.CancelledError:
                pass

        # Close WebSocket
        if self.websocket:
            try:
                await self.websocket.close()
            except Exception as e:
                logger.error(f"Error closing WebSocket: {e}")

        logger.info(f"WebSocket disconnected ({self.connection_id})")

    async def subscribe(
        self,
        channels: List[str],
        market_tickers: Optional[List[str]] = None,
    ) -> bool:
        """Subscribe to WebSocket channels.

        Args:
            channels: List of channels to subscribe to (from WebSocketChannel enum)
            market_tickers: List of market tickers (required for ticker/orderbook channels)

        Returns:
            True if subscription successful
        """
        if self.state != ConnectionState.CONNECTED:
            logger.error(f"Cannot subscribe: connection not connected ({self.state})")
            return False

        try:
            # Build subscription message
            subscription = {
                "type": "subscribe",
                "channels": channels,
            }

            if market_tickers:
                subscription["market_tickers"] = market_tickers

            # Send subscription
            message = json.dumps(subscription)
            await asyncio.wait_for(
                self.websocket.send(message),
                timeout=self.timeout,
            )

            # Track subscriptions
            self.subscribed_channels.update(channels)
            if market_tickers:
                self.subscribed_tickers.update(market_tickers)

            logger.info(f"Subscribed to {channels} for {market_tickers or 'all'} ({self.connection_id})")
            return True

        except Exception as e:
            logger.error(f"Subscription failed: {e}")
            return False

    async def unsubscribe(
        self,
        channels: List[str],
        market_tickers: Optional[List[str]] = None,
    ) -> bool:
        """Unsubscribe from WebSocket channels.

        Args:
            channels: List of channels to unsubscribe from
            market_tickers: List of market tickers

        Returns:
            True if unsubscription successful
        """
        if self.state != ConnectionState.CONNECTED:
            logger.error(f"Cannot unsubscribe: connection not connected ({self.state})")
            return False

        try:
            unsubscription = {
                "type": "unsubscribe",
                "channels": channels,
            }

            if market_tickers:
                unsubscription["market_tickers"] = market_tickers

            message = json.dumps(unsubscription)
            await asyncio.wait_for(
                self.websocket.send(message),
                timeout=self.timeout,
            )

            # Track unsubscriptions
            for channel in channels:
                self.subscribed_channels.discard(channel)
            if market_tickers:
                for ticker in market_tickers:
                    self.subscribed_tickers.discard(ticker)

            logger.info(f"Unsubscribed from {channels} ({self.connection_id})")
            return True

        except Exception as e:
            logger.error(f"Unsubscription failed: {e}")
            return False

    def register_callback(
        self,
        channel: str,
        callback: Callable[[Dict[str, Any]], None],
    ) -> None:
        """Register callback for channel messages.

        Args:
            channel: Channel name to listen for
            callback: Async callback function to invoke on messages
        """
        if channel not in self.callbacks:
            self.callbacks[channel] = []
        self.callbacks[channel].append(callback)
        logger.debug(f"Registered callback for {channel}")

    async def _listen_for_messages(self) -> None:
        """Listen for incoming WebSocket messages.

        Handles reconnection on unexpected disconnects.
        """
        try:
            while self.state == ConnectionState.CONNECTED:
                try:
                    message = await asyncio.wait_for(
                        self.websocket.recv(),
                        timeout=self.timeout + 10,  # Slightly longer than timeout
                    )
                    await self.message_queue.put(message)

                except asyncio.TimeoutError:
                    logger.warning(f"Message receive timeout ({self.connection_id})")
                    break

        except websockets.exceptions.ConnectionClosed:
            logger.info(f"WebSocket connection closed ({self.connection_id})")
            self.state = ConnectionState.DISCONNECTED
            await self._handle_reconnection()

        except Exception as e:
            logger.error(f"Error in message listener: {e} ({self.connection_id})")
            self.state = ConnectionState.DISCONNECTED
            await self._handle_reconnection()

    async def _process_messages(self) -> None:
        """Process messages from queue and invoke callbacks."""
        try:
            while self.state != ConnectionState.CLOSED:
                try:
                    # Get message from queue (with timeout to allow state checks)
                    message = await asyncio.wait_for(
                        self.message_queue.get(),
                        timeout=1.0,
                    )

                    try:
                        data = json.loads(message)
                        channel = data.get("channel")

                        if channel and channel in self.callbacks:
                            # Invoke all callbacks for this channel
                            for callback in self.callbacks[channel]:
                                try:
                                    if asyncio.iscoroutinefunction(callback):
                                        await callback(data)
                                    else:
                                        callback(data)
                                except Exception as e:
                                    logger.error(f"Callback error: {e}")

                    except json.JSONDecodeError:
                        logger.warning(f"Invalid JSON message: {message}")

                except asyncio.TimeoutError:
                    continue

        except asyncio.CancelledError:
            logger.debug(f"Message processor cancelled ({self.connection_id})")
        except Exception as e:
            logger.error(f"Error in message processor: {e}")

    async def _handle_reconnection(self) -> None:
        """Handle reconnection with exponential backoff."""
        if self.state == ConnectionState.CLOSED:
            return

        self.state = ConnectionState.RECONNECTING
        self.reconnect_attempts += 1

        if self.reconnect_attempts > self.MAX_RECONNECT_ATTEMPTS:
            logger.error(f"Max reconnection attempts exceeded ({self.connection_id})")
            self.state = ConnectionState.CLOSED
            return

        # Exponential backoff
        delay = min(
            self.INITIAL_RECONNECT_DELAY * (2 ** (self.reconnect_attempts - 1)),
            self.MAX_RECONNECT_DELAY,
        )

        logger.info(
            f"Reconnecting in {delay}s (attempt {self.reconnect_attempts}/{self.MAX_RECONNECT_ATTEMPTS})"
            f" ({self.connection_id})"
        )

        await asyncio.sleep(delay)

        # Attempt reconnection
        if await self.connect():
            # Resubscribe to previous channels
            if self.subscribed_channels:
                await self.subscribe(
                    list(self.subscribed_channels),
                    list(self.subscribed_tickers) if self.subscribed_tickers else None,
                )
        else:
            # Schedule another reconnection attempt
            self.reconnect_task = asyncio.create_task(self._handle_reconnection())

    def is_connected(self) -> bool:
        """Check if WebSocket is connected."""
        return self.state == ConnectionState.CONNECTED

    def get_status(self) -> Dict[str, Any]:
        """Get WebSocket connection status."""
        return {
            "connection_id": self.connection_id,
            "state": self.state.value,
            "is_connected": self.is_connected(),
            "subscribed_channels": list(self.subscribed_channels),
            "subscribed_tickers": list(self.subscribed_tickers),
            "reconnect_attempts": self.reconnect_attempts,
        }
