"""
Polymarket WebSocket client for real-time market data streaming.

This module provides a Python client for Polymarket's WebSocket API, enabling
real-time price updates, order book changes, and user notifications.

Example usage:
    ```python
    from polymarket.websocket_client import PolymarketWebSocketClient

    async with PolymarketWebSocketClient() as ws:
        await ws.subscribe_market("0xabc123...")
        async for event in ws:
            print(f"Price update: {event.price}")
    ```
"""

import asyncio
import json
from typing import Optional, AsyncIterator, Set
from loguru import logger
import websockets
from websockets.client import WebSocketClientProtocol
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
)

from .websocket_models import (
    WebSocketEvent,
    WebSocketChannel,
    parse_websocket_message,
)


class PolymarketWebSocketClient:
    """
    Async WebSocket client for Polymarket real-time data.

    Provides:
    - Market data streaming (public)
    - User update streaming (authenticated)
    - Automatic reconnection
    - Message queuing during reconnects
    - Type-safe event parsing

    Usage:
        async with PolymarketWebSocketClient() as ws:
            await ws.subscribe_market(market_id)
            async for event in ws:
                # Process event
                pass
    """

    DEFAULT_WS_URL = "wss://ws-subscriptions-clob.polymarket.com"

    def __init__(
        self,
        channel: str = "market",
        ws_url: Optional[str] = None,
        api_key: Optional[str] = None,
        max_reconnect_attempts: int = 5,
    ):
        """
        Initialize WebSocket client.

        Args:
            channel: Channel type - "market" for public data or "user" for authenticated
            ws_url: Base WebSocket URL (defaults to Polymarket production)
            api_key: Optional API key for authenticated channels (required for "user" channel)
            max_reconnect_attempts: Maximum reconnection attempts
        """
        self.channel = channel
        base_url = ws_url or self.DEFAULT_WS_URL
        # Polymarket requires channel-specific URLs
        self.ws_url = f"{base_url}/ws/{channel}"
        self.api_key = api_key
        self.max_reconnect_attempts = max_reconnect_attempts

        # Connection state
        self._ws: Optional[WebSocketClientProtocol] = None
        self._connected = False
        self._subscriptions: Set[str] = set()
        self._message_queue: asyncio.Queue[WebSocketEvent] = asyncio.Queue()
        self._receive_task: Optional[asyncio.Task] = None
        self._ping_task: Optional[asyncio.Task] = None
        self._pending_subscription: Optional[dict] = None

    async def __aenter__(self) -> "PolymarketWebSocketClient":
        """Async context manager entry - connects to WebSocket."""
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit - disconnects from WebSocket."""
        await self.disconnect()

    async def connect(self):
        """
        Establish WebSocket connection.

        Raises:
            ConnectionError: If connection fails after retries
        """
        if self._connected:
            logger.warning("Already connected to WebSocket")
            return

        try:
            await self._connect_with_retry()
            self._connected = True

            # Start background task to receive messages
            self._receive_task = asyncio.create_task(self._receive_loop())

            # Start background task for manual PING (Polymarket requirement)
            self._ping_task = asyncio.create_task(self._ping_loop())

            logger.info(f"Connected to Polymarket WebSocket at {self.ws_url}")

        except Exception as e:
            logger.error(f"Failed to connect to WebSocket: {e}")
            raise ConnectionError(f"WebSocket connection failed: {e}")

    @retry(
        stop=stop_after_attempt(5),
        wait=wait_exponential(multiplier=1, min=1, max=10),
        retry=retry_if_exception_type((ConnectionError, TimeoutError)),
    )
    async def _connect_with_retry(self):
        """Connect with exponential backoff retry."""
        try:
            # Build connection headers
            headers = {}
            if self.api_key:
                headers["Authorization"] = f"Bearer {self.api_key}"

            # Connect to WebSocket (disable automatic ping - we handle manually)
            self._ws = await websockets.connect(
                self.ws_url,
                additional_headers=headers if headers else None,
                ping_interval=None,  # Disable automatic ping (Polymarket requires manual)
                ping_timeout=None,
            )

            logger.debug("WebSocket connection established")

            # Polymarket requires immediate subscription after connection
            if self._pending_subscription:
                await self._ws.send(json.dumps(self._pending_subscription))
                logger.debug(f"Sent immediate subscription: {self._pending_subscription}")

        except Exception as e:
            logger.error(f"Connection attempt failed: {e}")
            raise

    async def disconnect(self):
        """Close WebSocket connection and clean up resources."""
        if not self._connected:
            return

        logger.info("Disconnecting from WebSocket...")

        # Cancel receive task
        if self._receive_task and not self._receive_task.done():
            self._receive_task.cancel()
            try:
                await self._receive_task
            except asyncio.CancelledError:
                pass

        # Cancel ping task
        if self._ping_task and not self._ping_task.done():
            self._ping_task.cancel()
            try:
                await self._ping_task
            except asyncio.CancelledError:
                pass

        # Close WebSocket (websockets 15.x: check close_code instead of closed)
        if self._ws and self._ws.close_code is None:
            try:
                await self._ws.close()
            except RuntimeError as e:
                # Event loop errors during teardown - ignore
                logger.debug(f"Ignoring event loop error during close: {e}")

        self._connected = False
        self._ws = None
        logger.info("Disconnected from WebSocket")

    async def subscribe_market(self, asset_ids: list[str]):
        """
        Subscribe to real-time updates for specific market assets.

        Polymarket requires:
        - Connection to /ws/market channel
        - Subscription message sent immediately on connection
        - Asset IDs (token IDs), not market IDs

        Args:
            asset_ids: List of asset IDs (token IDs) to subscribe to

        Raises:
            ConnectionError: If not connected to WebSocket
            ValueError: If called on user channel
        """
        if self.channel != "market":
            raise ValueError("subscribe_market() requires channel='market'")

        # Build subscription message (Polymarket format)
        message = {
            "assets_ids": asset_ids,
            "type": "market",  # Lowercase per Polymarket docs
        }

        # Store subscription for reconnection
        self._pending_subscription = message
        for asset_id in asset_ids:
            subscription_key = f"market:{asset_id}"
            self._subscriptions.add(subscription_key)

        # If connected, send immediately; otherwise stored for connection
        if self._connected and self._ws and self._ws.close_code is None:
            await self._ws.send(json.dumps(message))
            logger.info(f"Subscribed to {len(asset_ids)} market assets")
        else:
            logger.info(f"Stored subscription for {len(asset_ids)} assets (will send on connect)")

    async def subscribe_user(self, markets: Optional[list[str]] = None):
        """
        Subscribe to authenticated user updates (orders, fills, balance).

        Polymarket requires:
        - Connection to /ws/user channel
        - API key for authentication
        - Optional market filter

        Args:
            markets: Optional list of market IDs to filter user events

        Raises:
            ValueError: If api_key not provided or wrong channel
            ConnectionError: If not connected to WebSocket
        """
        if not self.api_key:
            raise ValueError("API key required for user channel subscription")

        if self.channel != "user":
            raise ValueError("subscribe_user() requires channel='user'")

        # Build subscription message (Polymarket format)
        message = {
            "auth": {},  # Auth handled via headers
            "type": "user",  # Lowercase per Polymarket docs
        }
        if markets:
            message["markets"] = markets

        # Store subscription for reconnection
        self._pending_subscription = message
        subscription_key = "user:authenticated"
        self._subscriptions.add(subscription_key)

        # If connected, send immediately; otherwise stored for connection
        if self._connected and self._ws and self._ws.close_code is None:
            await self._ws.send(json.dumps(message))
            logger.info("Subscribed to user channel")
        else:
            logger.info("Stored user subscription (will send on connect)")

    async def unsubscribe(self, channel: WebSocketChannel, market_id: Optional[str] = None):
        """
        Unsubscribe from a channel.

        Args:
            channel: Channel to unsubscribe from
            market_id: Market ID (required for market channel)

        Raises:
            ConnectionError: If not connected to WebSocket
        """
        if not self._connected or not self._ws:
            raise ConnectionError("Not connected to WebSocket")

        # Build subscription key
        if channel == WebSocketChannel.MARKET and market_id:
            subscription_key = f"{channel.value}:{market_id}"
        else:
            subscription_key = f"{channel.value}:user"

        if subscription_key not in self._subscriptions:
            logger.warning(f"Not subscribed to {subscription_key}")
            return

        # Send unsubscribe message
        message = {
            "type": "unsubscribe",
            "channel": channel.value,
        }
        if market_id:
            message["market"] = market_id

        await self._ws.send(json.dumps(message))
        self._subscriptions.discard(subscription_key)

        logger.info(f"Unsubscribed from {subscription_key}")

    async def _receive_loop(self):
        """
        Background task to receive and queue messages.

        Continuously receives messages from WebSocket and adds them to the queue.
        Handles reconnection on disconnect.
        """
        while self._connected:
            try:
                if not self._ws or self._ws.close_code is not None:
                    logger.warning("WebSocket closed, attempting reconnection...")
                    await self._reconnect()
                    continue

                # Receive message
                message_str = await self._ws.recv()

                # Skip PONG responses (Polymarket sends these in response to PING)
                if message_str == "PONG":
                    logger.debug("Received PONG")
                    continue

                message_data = json.loads(message_str)

                # Parse into event model
                try:
                    event = parse_websocket_message(message_data)
                    await self._message_queue.put(event)

                except ValueError as e:
                    logger.warning(f"Failed to parse message: {e}")
                    logger.debug(f"Raw message: {message_data}")

            except websockets.exceptions.ConnectionClosed:
                logger.warning("WebSocket connection closed")
                if self._connected:
                    await self._reconnect()

            except asyncio.CancelledError:
                logger.debug("Receive loop cancelled")
                break

            except Exception as e:
                logger.error(f"Error in receive loop: {e}")
                await asyncio.sleep(1)  # Avoid tight error loop

    async def _ping_loop(self):
        """
        Background task to send manual PING messages.

        Polymarket requires sending "PING" string every 10 seconds to keep
        connection alive. Server responds with "PONG".
        """
        while self._connected:
            try:
                if self._ws and self._ws.close_code is None:
                    await self._ws.send("PING")
                    logger.debug("Sent PING")
                await asyncio.sleep(10)

            except websockets.exceptions.ConnectionClosed:
                logger.debug("Connection closed during PING")
                break

            except asyncio.CancelledError:
                logger.debug("PING loop cancelled")
                break

            except Exception as e:
                logger.error(f"Error in PING loop: {e}")
                await asyncio.sleep(10)

    async def _reconnect(self):
        """
        Reconnect to WebSocket and resubscribe to all channels.

        Uses exponential backoff for reconnection attempts.
        Subscription message stored in _pending_subscription will be sent
        automatically by _connect_with_retry().
        """
        logger.info("Reconnecting to WebSocket...")

        try:
            # Close existing connection
            if self._ws and self._ws.close_code is None:
                await self._ws.close()

            # Reconnect with retry (will send _pending_subscription automatically)
            await self._connect_with_retry()

            logger.info("Reconnection successful")

        except Exception as e:
            logger.error(f"Reconnection failed: {e}")
            raise

    async def __aiter__(self) -> AsyncIterator[WebSocketEvent]:
        """
        Async iterator for streaming WebSocket events.

        Yields:
            WebSocketEvent: Parsed event from WebSocket stream

        Example:
            async for event in ws_client:
                if event.event_type == "price_change":
                    print(f"New price: {event.price}")
        """
        while self._connected:
            try:
                # Get next event from queue (with timeout to allow graceful shutdown)
                event = await asyncio.wait_for(
                    self._message_queue.get(),
                    timeout=1.0
                )
                yield event

            except asyncio.TimeoutError:
                # Timeout - check if still connected and continue
                continue

            except asyncio.CancelledError:
                logger.debug("Iterator cancelled")
                break

            except Exception as e:
                logger.error(f"Error in event iterator: {e}")
                # Continue streaming despite errors
                await asyncio.sleep(0.1)


async def main():
    """Example usage of PolymarketWebSocketClient."""
    # Example: Monitor a market for price changes
    async with PolymarketWebSocketClient(channel="market") as ws:
        # Subscribe to market assets (token IDs, not market ID!)
        # Get these from market data: market["tokens"][0]["token_id"]
        asset_ids = ["your_asset_id_1", "your_asset_id_2"]
        await ws.subscribe_market(asset_ids)

        # Stream events
        async for event in ws:
            print(f"Event type: {event.event_type}")

            if hasattr(event, 'price'):
                print(f"  Price: {event.price}")

            # Exit after 10 events (for demo)
            # In practice, you'd run continuously or until a condition is met


if __name__ == "__main__":
    asyncio.run(main())
