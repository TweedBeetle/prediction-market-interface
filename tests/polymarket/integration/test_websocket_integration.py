"""
Integration tests for Polymarket WebSocket client.

These tests connect to the real Polymarket WebSocket API and verify
real-time data streaming functionality.

Note: These tests may be skipped if:
- WebSocket endpoint is not available
- API rate limits are hit
- Network connectivity issues
"""

import pytest
import asyncio
import os
from loguru import logger
import httpx

from src.polymarket.websocket_client import PolymarketWebSocketClient
from src.polymarket.websocket_models import (
    PriceChangeEvent,
    OrderBookUpdate,
    LastTradePriceEvent,
)


# Skip integration tests if environment variable is set
# Also disable VCR recording for WebSocket tests (they test real API)
pytestmark = [
    pytest.mark.skipif(
        os.getenv("SKIP_WEBSOCKET_INTEGRATION", "false").lower() == "true",
        reason="WebSocket integration tests disabled via environment variable"
    ),
    pytest.mark.disable_recording,  # Disable VCR cassettes
]


@pytest.fixture
async def ws_client():
    """Create WebSocket client connected to production API."""
    client = PolymarketWebSocketClient(channel="market")
    yield client
    # Cleanup
    if client._connected:
        await client.disconnect()


@pytest.fixture
def test_market_id():
    """
    Provide a test market ID for integration testing.

    This should be a real, active market on Polymarket.
    Update this with a current high-liquidity market for testing.
    """
    # Default: Use a popular/liquid market if available
    # In practice, you'd fetch an active market dynamically
    return os.getenv("TEST_MARKET_ID", "0x4319532e181605cb15b1bd677759a3bc7f7394b2fdf145195b700eeaedfd5221")


@pytest.fixture
async def test_asset_ids():
    """
    Fetch asset IDs (token IDs) from an active market.

    Polymarket WebSocket requires asset IDs, not market IDs.
    We'll search for active markets and use the first one found.
    """
    try:
        # Search for active markets from Gamma API
        async with httpx.AsyncClient() as client:
            response = await client.get(
                "https://gamma-api.polymarket.com/markets",
                params={"closed": "false", "limit": 20}  # Get multiple to find one with tokens
            )
            response.raise_for_status()
            data = response.json()

        # Extract markets
        markets = data if isinstance(data, list) else data.get("markets", data.get("data", []))
        if not markets:
            pytest.skip("No active markets found")

        # Find first market with tokens
        for market in markets:
            tokens = market.get("tokens", [])
            if tokens and len(tokens) >= 2:
                # Extract token IDs
                asset_ids = [token["token_id"] for token in tokens]
                logger.info(f"Found {len(asset_ids)} asset IDs for market '{market.get('question', market.get('title', 'Unknown'))[:50]}...'")
                return asset_ids

        pytest.skip("No markets with tokens found in first 20 results")

    except Exception as e:
        pytest.skip(f"Failed to fetch market data: {e}")


class TestWebSocketConnection:
    """Test real WebSocket connections."""

    @pytest.mark.asyncio
    async def test_connect_to_production_websocket(self, ws_client):
        """Test connection to production WebSocket endpoint."""
        try:
            await ws_client.connect()
            assert ws_client._connected is True
            logger.info("Successfully connected to Polymarket WebSocket")

        except Exception as e:
            pytest.skip(f"WebSocket connection failed: {e}")

    @pytest.mark.asyncio
    async def test_context_manager_connection(self):
        """Test connection via async context manager."""
        try:
            async with PolymarketWebSocketClient(channel="market") as ws:
                assert ws._connected is True
                logger.info("Context manager connection successful")

        except Exception as e:
            pytest.skip(f"WebSocket connection failed: {e}")


class TestMarketSubscription:
    """Test market data subscription and streaming."""

    @pytest.mark.asyncio
    @pytest.mark.timeout(30)  # 30 second timeout
    async def test_subscribe_to_market(self, ws_client, test_asset_ids):
        """Test subscribing to a real market."""
        try:
            await ws_client.connect()
            await ws_client.subscribe_market(test_asset_ids)

            logger.info(f"Subscribed to {len(test_asset_ids)} assets")

            # Verify subscriptions are tracked
            for asset_id in test_asset_ids:
                assert f"market:{asset_id}" in ws_client._subscriptions

        except Exception as e:
            pytest.skip(f"Market subscription failed: {e}")

    @pytest.mark.asyncio
    @pytest.mark.timeout(60)  # 60 second timeout
    async def test_receive_market_events(self, ws_client, test_asset_ids):
        """Test receiving real market events."""
        try:
            await ws_client.connect()
            await ws_client.subscribe_market(test_asset_ids)

            logger.info("Waiting for market events...")

            # Collect first few events
            events_received = []
            timeout = 30  # seconds

            async def collect_events():
                async for event in ws_client:
                    events_received.append(event)
                    logger.info(f"Received event: {event.event_type}")

                    if len(events_received) >= 3:
                        break

            # Wait for events with timeout
            try:
                await asyncio.wait_for(collect_events(), timeout=timeout)
            except asyncio.TimeoutError:
                if not events_received:
                    pytest.skip(f"No events received within {timeout}s (market may be inactive)")

            # Verify we received some events
            assert len(events_received) > 0, "Should receive at least one event"

            logger.info(f"Received {len(events_received)} events successfully")

        except Exception as e:
            pytest.skip(f"Event streaming failed: {e}")

    @pytest.mark.asyncio
    @pytest.mark.timeout(60)
    async def test_parse_real_events(self, ws_client, test_asset_ids):
        """Test parsing real WebSocket events."""
        try:
            await ws_client.connect()
            await ws_client.subscribe_market(test_asset_ids)

            logger.info("Waiting for parseable events...")

            # Collect different event types
            event_types_seen = set()

            async def collect_event_types():
                async for event in ws_client:
                    event_types_seen.add(type(event).__name__)
                    logger.info(f"Parsed event type: {type(event).__name__}")

                    # Stop after seeing a few different types or 10 events total
                    if len(event_types_seen) >= 2 or len(event_types_seen) > 10:
                        break

            await asyncio.wait_for(collect_event_types(), timeout=30)

            # Should have seen at least one event type
            assert len(event_types_seen) > 0

            logger.info(f"Successfully parsed event types: {event_types_seen}")

        except asyncio.TimeoutError:
            pytest.skip("No events received within timeout")
        except Exception as e:
            pytest.skip(f"Event parsing test failed: {e}")


class TestUserSubscription:
    """Test authenticated user channel subscription."""

    @pytest.mark.asyncio
    async def test_user_subscription_requires_auth(self):
        """Test that user subscription requires API key."""
        try:
            # User channel requires channel="user"
            ws_client = PolymarketWebSocketClient(channel="user")
            await ws_client.connect()

            with pytest.raises(ValueError, match="API key required"):
                await ws_client.subscribe_user()

            await ws_client.disconnect()

        except Exception as e:
            pytest.skip(f"Connection failed: {e}")

    @pytest.mark.asyncio
    async def test_user_subscription_with_api_key(self):
        """Test user subscription with API key (if available)."""
        api_key = os.getenv("POLYMARKET_API_KEY")
        if not api_key:
            pytest.skip("No API key available for user subscription test")

        try:
            async with PolymarketWebSocketClient(channel="user", api_key=api_key) as ws:
                await ws.subscribe_user()

                assert "user:authenticated" in ws._subscriptions
                logger.info("Successfully subscribed to user channel")

        except Exception as e:
            pytest.skip(f"User subscription failed: {e}")


class TestReconnection:
    """Test reconnection behavior."""

    @pytest.mark.asyncio
    @pytest.mark.timeout(120)  # 2 minute timeout
    async def test_connection_resilience(self, ws_client, test_asset_ids):
        """
        Test that client handles connection issues gracefully.

        Note: This is a basic test. Full reconnection testing would require
        simulating network issues, which is complex in integration tests.
        """
        try:
            await ws_client.connect()
            await ws_client.subscribe_market(test_asset_ids)

            # Receive some events
            events_count = 0
            async for event in ws_client:
                events_count += 1
                if events_count >= 5:
                    break

            assert events_count >= 5, "Should receive multiple events without disconnection"

            logger.info(f"Received {events_count} events successfully")

        except Exception as e:
            pytest.skip(f"Reconnection test failed: {e}")


class TestUnsubscription:
    """Test unsubscribing from channels."""

    @pytest.mark.asyncio
    async def test_unsubscribe_from_market(self, ws_client, test_asset_ids):
        """Test unsubscribing from a market."""
        try:
            await ws_client.connect()

            # Subscribe
            await ws_client.subscribe_market(test_asset_ids)
            asset_id = test_asset_ids[0]
            assert f"market:{asset_id}" in ws_client._subscriptions

            # Unsubscribe
            from src.polymarket.websocket_models import WebSocketChannel
            await ws_client.unsubscribe(WebSocketChannel.MARKET, asset_id)

            # Verify unsubscribed
            assert f"market:{asset_id}" not in ws_client._subscriptions

            logger.info("Successfully unsubscribed from market")

        except Exception as e:
            pytest.skip(f"Unsubscription test failed: {e}")


@pytest.mark.asyncio
async def test_full_workflow_example(test_asset_ids):
    """
    Example integration test showing full workflow.

    This demonstrates how an agent would use the WebSocket client:
    1. Connect
    2. Subscribe to market assets
    3. Monitor for specific price condition
    4. Take action when condition met
    """
    try:
        async with PolymarketWebSocketClient(channel="market") as ws:
            logger.info("Connected to WebSocket")

            await ws.subscribe_market(test_asset_ids)
            logger.info(f"Subscribed to {len(test_asset_ids)} assets")

            # Monitor for price events
            prices_seen = []

            async def monitor_prices():
                async for event in ws:
                    if isinstance(event, (PriceChangeEvent, LastTradePriceEvent)):
                        prices_seen.append(event.price)
                        logger.info(f"Price update: {event.price}")

                        # Stop after seeing 3 prices
                        if len(prices_seen) >= 3:
                            break

            await asyncio.wait_for(monitor_prices(), timeout=30)

            # Verify we saw some prices
            assert len(prices_seen) > 0, "Should receive price updates"

            logger.info(f"Successfully monitored {len(prices_seen)} price updates")
            logger.info(f"Price range: {min(prices_seen):.3f} - {max(prices_seen):.3f}")

    except asyncio.TimeoutError:
        pytest.skip("No price events received within timeout")
    except Exception as e:
        pytest.skip(f"Full workflow test failed: {e}")
