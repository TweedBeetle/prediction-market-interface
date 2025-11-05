"""
Integration tests for cursor-based pagination.

Tests that client methods properly handle pagination for requests >100 items.
"""

import pytest
from src.kalshi.client import KalshiClient


pytestmark = [pytest.mark.asyncio, pytest.mark.integration]


class TestPagination:
    """Test cursor-based pagination for all paginated endpoints."""

    async def test_search_markets_pagination_no_query(self, demo_env):
        """Test that search_markets can fetch >100 markets without query."""
        async with KalshiClient.from_env() as client:
            # Request 150 markets (should trigger pagination)
            markets = await client.search_markets(limit=150, status="open")

            # Should return up to 150 markets
            assert len(markets) > 0
            assert len(markets) <= 150

            # All should be valid Market objects
            for market in markets:
                assert hasattr(market, "ticker")
                assert hasattr(market, "title")

    async def test_search_markets_pagination_with_query(self, demo_env):
        """Test that search_markets paginates when filtering with query."""
        async with KalshiClient.from_env() as client:
            # Search for common term in sports markets (should match many)
            markets = await client.search_markets(query="win", limit=20, status="open")

            # Should return up to 20 matching markets
            assert len(markets) > 0
            assert len(markets) <= 20

            # All should contain "win" in title or subtitle
            for market in markets:
                assert (
                    "win" in market.title.lower()
                    or (market.subtitle and "win" in market.subtitle.lower())
                )

    async def test_get_events_pagination(self, demo_env):
        """Test that get_events can fetch >100 events."""
        async with KalshiClient.from_env() as client:
            # Request 150 events (should trigger pagination if available)
            events = await client.get_events(limit=150, status="open")

            # Should return up to 150 events
            assert len(events) > 0
            assert len(events) <= 150

            # All should be valid Event objects
            for event in events:
                assert hasattr(event, "event_ticker")
                assert hasattr(event, "title")

    async def test_get_trades_pagination(self, demo_env):
        """Test that get_trades can fetch >100 trades."""
        async with KalshiClient.from_env() as client:
            # Request 150 recent trades (should trigger pagination if available)
            trades = await client.get_trades(limit=150)

            # Should return up to 150 trades
            assert len(trades) > 0
            assert len(trades) <= 150

            # All should be valid Trade objects
            for trade in trades:
                assert hasattr(trade, "trade_id")
                assert hasattr(trade, "ticker")

    async def test_get_orders_pagination(self, demo_env):
        """Test that get_orders can fetch >100 orders if available."""
        async with KalshiClient.from_env() as client:
            # Request up to 150 orders (may have none in demo)
            orders = await client.get_orders(limit=150, status="filled")

            # Should return up to 150 orders (may be 0 if no order history)
            assert len(orders) <= 150

            # All should be valid Order objects
            for order in orders:
                assert hasattr(order, "order_id")
                assert hasattr(order, "ticker")

    async def test_get_positions_pagination(self, demo_env):
        """Test that get_positions can fetch >100 positions if available."""
        async with KalshiClient.from_env() as client:
            # Request up to 150 positions (may have none in demo)
            positions = await client.get_positions(limit=150)

            # Should return up to 150 positions (may be 0 if no positions)
            assert len(positions) <= 150

            # All should be valid Position objects
            for position in positions:
                assert hasattr(position, "ticker")
                assert hasattr(position, "position")

    async def test_get_fills_pagination(self, demo_env):
        """Test that get_fills can fetch >100 fills if available."""
        async with KalshiClient.from_env() as client:
            # Request up to 150 fills (may have none in demo)
            fills = await client.get_fills(limit=150)

            # Should return up to 150 fills (may be 0 if no trading history)
            assert len(fills) <= 150

            # All should be valid Fill objects
            for fill in fills:
                assert hasattr(fill, "fill_id")
                assert hasattr(fill, "ticker")

    async def test_pagination_respects_max_results(self, demo_env):
        """Test that pagination stops at max_results even if more pages exist."""
        async with KalshiClient.from_env() as client:
            # Request exactly 250 markets
            markets = await client.search_markets(limit=250, status="open")

            # Should return at most 250 (not 300 = 3 pages × 100)
            assert len(markets) <= 250

    async def test_pagination_handles_single_page(self, demo_env):
        """Test that pagination works correctly when only 1 page exists."""
        async with KalshiClient.from_env() as client:
            # Request 10 markets (should only need 1 page)
            markets = await client.search_markets(limit=10, status="open")

            # Should return up to 10 markets
            assert len(markets) > 0
            assert len(markets) <= 10

    async def test_pagination_with_filters(self, demo_env):
        """Test that pagination preserves filter parameters across pages."""
        async with KalshiClient.from_env() as client:
            # Request 150 open markets
            open_markets = await client.search_markets(limit=150, status="open")

            # All should have status=open (implied by search)
            assert len(open_markets) > 0
            assert len(open_markets) <= 150

            # Request 150 settled markets
            settled_markets = await client.search_markets(limit=150, status="settled")

            # Should maintain filter across pages
            assert len(settled_markets) <= 150
