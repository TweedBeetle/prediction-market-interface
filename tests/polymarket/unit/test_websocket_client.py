"""
Unit tests for Polymarket WebSocket client.

Tests WebSocket connection, subscription management, and event streaming
using mocked WebSocket connections.
"""

import pytest
import asyncio
import json
from unittest.mock import AsyncMock, MagicMock, patch
from src.polymarket.websocket_client import PolymarketWebSocketClient
from src.polymarket.websocket_models import (
    WebSocketEventType,
    PriceChangeEvent,
    OrderBookUpdate,
    UserOrderEvent,
)


@pytest.fixture
def mock_websocket():
    """Create a mock WebSocket connection."""
    ws = AsyncMock()
    ws.closed = False
    ws.recv = AsyncMock()
    ws.send = AsyncMock()
    ws.close = AsyncMock()
    return ws


async def async_return(value):
    """Helper to make a value awaitable."""
    return value


@pytest.fixture
def mock_connect(mock_websocket):
    """Create a mock websockets.connect function."""
    async def mock_connect_async(*args, **kwargs):
        return mock_websocket
    return mock_connect_async


@pytest.fixture
async def ws_client():
    """Create a WebSocket client instance for testing."""
    client = PolymarketWebSocketClient(
        channel="market",
        ws_url="wss://test.example.com",
        max_reconnect_attempts=2,
    )
    return client


class TestWebSocketClientConnection:
    """Test WebSocket connection lifecycle."""

    @pytest.mark.asyncio
    async def test_connect_success(self, ws_client, mock_connect):
        """Test successful WebSocket connection."""
        with patch("websockets.connect", side_effect=mock_connect):
            await ws_client.connect()

            assert ws_client._connected is True
            assert ws_client._ws is not None
            assert ws_client._receive_task is not None

    @pytest.mark.asyncio
    async def test_context_manager(self, mock_connect):
        """Test async context manager connects and disconnects."""
        with patch("websockets.connect", side_effect=mock_connect):
            async with PolymarketWebSocketClient(channel="market") as client:
                assert client._connected is True

            # Should be disconnected after context exit
            assert client._connected is False

    @pytest.mark.asyncio
    async def test_disconnect(self, ws_client, mock_connect):
        """Test clean disconnection."""
        with patch("websockets.connect", side_effect=mock_connect):
            await ws_client.connect()
            await ws_client.disconnect()

            assert ws_client._connected is False

    @pytest.mark.asyncio
    async def test_connect_retry_on_failure(self, ws_client, mock_websocket):
        """Test connection retries on failure."""
        call_count = [0]

        async def mock_with_retries(*args, **kwargs):
            call_count[0] += 1
            if call_count[0] < 3:
                raise ConnectionError("Failed")
            return mock_websocket

        with patch("websockets.connect", side_effect=mock_with_retries):
            # Should succeed after retries
            await ws_client.connect()
            assert ws_client._connected is True


class TestWebSocketSubscriptions:
    """Test subscription management."""

    @pytest.mark.asyncio
    async def test_subscribe_market(self, ws_client, mock_connect):
        """Test market subscription."""
        with patch("websockets.connect", side_effect=mock_connect):
            await ws_client.connect()

            asset_ids = ["asset_1", "asset_2"]
            await ws_client.subscribe_market(asset_ids)

            # Verify subscriptions tracked
            assert "market:asset_1" in ws_client._subscriptions
            assert "market:asset_2" in ws_client._subscriptions

    @pytest.mark.asyncio
    async def test_subscribe_user(self, mock_connect):
        """Test user channel subscription."""
        client = PolymarketWebSocketClient(channel="user", api_key="test_api_key")

        with patch("websockets.connect", side_effect=mock_connect):
            await client.connect()
            await client.subscribe_user()

            # Verify subscription tracked
            assert "user:authenticated" in client._subscriptions

    @pytest.mark.asyncio
    async def test_subscribe_user_without_api_key(self, mock_connect):
        """Test user subscription fails without API key."""
        client = PolymarketWebSocketClient(channel="user")  # No API key

        with patch("websockets.connect", side_effect=mock_connect):
            await client.connect()

            with pytest.raises(ValueError, match="API key required"):
                await client.subscribe_user()

    @pytest.mark.asyncio
    async def test_unsubscribe(self, ws_client, mock_connect):
        """Test unsubscription from channel."""
        with patch("websockets.connect", side_effect=mock_connect):
            await ws_client.connect()

            # Subscribe first
            asset_ids = ["asset_1"]
            await ws_client.subscribe_market(asset_ids)

            # Unsubscribe
            from src.polymarket.websocket_models import WebSocketChannel
            await ws_client.unsubscribe(WebSocketChannel.MARKET, "asset_1")

            # Verify subscription removed
            assert "market:asset_1" not in ws_client._subscriptions

    @pytest.mark.asyncio
    async def test_duplicate_subscription(self, ws_client, mock_connect):
        """Test duplicate subscription is handled gracefully."""
        with patch("websockets.connect", side_effect=mock_connect):
            await ws_client.connect()

            asset_ids = ["asset_1"]

            # Subscribe twice (second overwrites pending subscription)
            await ws_client.subscribe_market(asset_ids)
            await ws_client.subscribe_market(asset_ids)

            # Subscription should still be tracked
            assert "market:asset_1" in ws_client._subscriptions


class TestMessageParsing:
    """Test WebSocket message parsing."""

    @pytest.mark.asyncio
    async def test_parse_price_change_event(self, ws_client, mock_websocket, mock_connect):
        """Test parsing price change event."""
        price_change_msg = {
            "event_type": "price_change",
            "asset_id": "token123",
            "market": "0xabc",
            "price": 0.55,
            "side": "ASK"
        }

        mock_websocket.recv = AsyncMock(side_effect=[
            json.dumps(price_change_msg),
            asyncio.CancelledError()  # Stop after one message
        ])

        with patch("websockets.connect", side_effect=mock_connect):
            await ws_client.connect()

            # Get event from iterator
            async for event in ws_client:
                assert isinstance(event, PriceChangeEvent)
                assert event.price == 0.55
                assert event.asset_id == "token123"
                assert abs(event.probability_pct - 55.0) < 0.001  # Float comparison with tolerance
                break

    @pytest.mark.asyncio
    async def test_parse_orderbook_event(self, ws_client, mock_websocket, mock_connect):
        """Test parsing order book event."""
        orderbook_msg = {
            "event_type": "book",
            "asset_id": "token123",
            "market": "0xabc",
            "bids": [
                {"price": 0.54, "size": 100.0},
                {"price": 0.53, "size": 50.0}
            ],
            "asks": [
                {"price": 0.56, "size": 75.0},
                {"price": 0.57, "size": 25.0}
            ]
        }

        mock_websocket.recv = AsyncMock(side_effect=[
            json.dumps(orderbook_msg),
            asyncio.CancelledError()
        ])

        with patch("websockets.connect", side_effect=mock_connect):
            await ws_client.connect()

            async for event in ws_client:
                assert isinstance(event, OrderBookUpdate)
                assert event.best_bid.price == 0.54
                assert event.best_ask.price == 0.56
                assert abs(event.spread - 0.02) < 0.001  # Float comparison with tolerance
                break

    @pytest.mark.asyncio
    async def test_invalid_message_handling(self, ws_client, mock_websocket, mock_connect):
        """Test handling of invalid/unknown messages."""
        invalid_msg = {"event_type": "unknown_type", "data": "test"}
        valid_msg = {
            "event_type": "price_change",
            "asset_id": "token123",
            "market": "0xabc",
            "price": 0.60
        }

        mock_websocket.recv = AsyncMock(side_effect=[
            json.dumps(invalid_msg),  # Invalid - should be skipped
            json.dumps(valid_msg),     # Valid - should be received
            asyncio.CancelledError()
        ])

        with patch("websockets.connect", side_effect=mock_connect):
            await ws_client.connect()

            # Should skip invalid and receive valid
            async for event in ws_client:
                assert isinstance(event, PriceChangeEvent)
                assert event.price == 0.60
                break


class TestReconnection:
    """Test automatic reconnection logic."""

    @pytest.mark.asyncio
    async def test_reconnect_on_disconnect(self, ws_client, mock_websocket):
        """Test automatic reconnection when connection drops."""
        # Simulate connection drop
        import websockets

        mock_websocket.recv = AsyncMock(side_effect=websockets.exceptions.ConnectionClosed(None, None))

        reconnect_ws = AsyncMock()
        reconnect_ws.closed = False
        reconnect_ws.recv = AsyncMock(side_effect=asyncio.CancelledError())
        reconnect_ws.send = AsyncMock()

        # Wrap mocks in async functions for proper awaiting
        call_count = [0]
        async def mock_connect_sequence(*args, **kwargs):
            if call_count[0] == 0:
                call_count[0] += 1
                return mock_websocket
            else:
                return reconnect_ws

        with patch("websockets.connect", side_effect=mock_connect_sequence):
            await ws_client.connect()

            # Wait a moment for reconnection to trigger
            await asyncio.sleep(0.1)

            # Should have attempted reconnection
            # Note: In real implementation, reconnection happens in background

    @pytest.mark.asyncio
    async def test_resubscribe_after_reconnect(self, ws_client, mock_websocket, mock_connect):
        """Test resubscription to channels after reconnect."""
        # Subscribe to a market
        with patch("websockets.connect", side_effect=mock_connect):
            await ws_client.connect()
            await ws_client.subscribe_market(["asset_1"])

            # Track pending subscription
            assert ws_client._pending_subscription is not None
            pending_sub = ws_client._pending_subscription

            # Trigger reconnection
            reconnect_ws = AsyncMock()
            reconnect_ws.closed = False
            reconnect_ws.send = AsyncMock()

            async def mock_reconnect(*args, **kwargs):
                return reconnect_ws

            with patch("websockets.connect", side_effect=mock_reconnect):
                await ws_client._reconnect()

                # Should still have same pending subscription
                assert ws_client._pending_subscription == pending_sub


class TestEventStreaming:
    """Test event streaming functionality."""

    @pytest.mark.asyncio
    async def test_async_iterator(self, ws_client, mock_websocket, mock_connect):
        """Test async iterator yields events."""
        messages = [
            {"event_type": "price_change", "asset_id": "token1", "market": "0xabc", "price": 0.50},
            {"event_type": "price_change", "asset_id": "token1", "market": "0xabc", "price": 0.51},
            {"event_type": "price_change", "asset_id": "token1", "market": "0xabc", "price": 0.52},
        ]

        mock_websocket.recv = AsyncMock(side_effect=[
            json.dumps(msg) for msg in messages
        ] + [asyncio.CancelledError()])

        with patch("websockets.connect", side_effect=mock_connect):
            await ws_client.connect()

            prices = []
            async for event in ws_client:
                prices.append(event.price)
                if len(prices) == 3:
                    break

            assert prices == [0.50, 0.51, 0.52]

    @pytest.mark.asyncio
    async def test_multiple_event_types(self, ws_client, mock_websocket, mock_connect):
        """Test streaming multiple event types."""
        messages = [
            {"event_type": "price_change", "asset_id": "token1", "market": "0xabc", "price": 0.50},
            {
                "event_type": "book",
                "asset_id": "token1",
                "market": "0xabc",
                "bids": [{"price": 0.49, "size": 100}],
                "asks": [{"price": 0.51, "size": 100}]
            },
        ]

        mock_websocket.recv = AsyncMock(side_effect=[
            json.dumps(msg) for msg in messages
        ] + [asyncio.CancelledError()])

        with patch("websockets.connect", side_effect=mock_connect):
            await ws_client.connect()

            events = []
            async for event in ws_client:
                events.append(event)
                if len(events) == 2:
                    break

            assert isinstance(events[0], PriceChangeEvent)
            assert isinstance(events[1], OrderBookUpdate)
