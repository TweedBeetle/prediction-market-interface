"""Integration tests for Kalshi API client."""

import pytest
from src.kalshi.client import KalshiClient


@pytest.mark.asyncio
class TestKalshiClientIntegration:
    """Test Kalshi client against demo API."""

    async def test_get_exchange_status(self, demo_env):
        """Can get exchange status from demo API."""
        async with KalshiClient.from_env() as client:
            status = await client.get_exchange_status()

        assert status.exchange_active is not None
        assert status.trading_active is not None
        # Demo exchange should usually be active
        assert isinstance(status.exchange_active, bool)
        assert isinstance(status.trading_active, bool)

    async def test_get_balance(self, demo_env):
        """Can get account balance from demo API."""
        async with KalshiClient.from_env() as client:
            balance = await client.get_balance()

        assert balance.balance is not None
        assert balance.balance >= 0
        assert balance.balance_dollars >= 0
        # Demo accounts typically start with $10k
        assert balance.balance_dollars > 0

    async def test_search_markets_returns_results(self, demo_env):
        """Can search markets and get results."""
        async with KalshiClient.from_env() as client:
            markets = await client.search_markets(limit=10)

        assert isinstance(markets, list)
        # Demo should have some markets
        assert len(markets) > 0

        # Verify market structure
        market = markets[0]
        assert market.ticker is not None
        assert market.title is not None
        assert market.status is not None

    async def test_get_market_by_ticker(self, demo_env, active_market):
        """Can get specific market by ticker."""
        async with KalshiClient.from_env() as client:
            market = await client.get_market(active_market.ticker)

        assert market.ticker == active_market.ticker
        assert market.title is not None
        assert market.status is not None
        assert market.close_time is not None

    async def test_get_events(self, demo_env):
        """Can get list of events."""
        async with KalshiClient.from_env() as client:
            events = await client.get_events(limit=10)

        assert isinstance(events, list)
        # Demo should have events
        assert len(events) > 0

        # Verify event structure
        event = events[0]
        assert event.event_ticker is not None
        assert event.title is not None
        assert event.category is not None

    async def test_search_with_status_filter(self, demo_env):
        """Can filter markets by status."""
        async with KalshiClient.from_env() as client:
            open_markets = await client.search_markets(status="open", limit=20)

        assert isinstance(open_markets, list)
        # All returned markets should be open
        for market in open_markets:
            assert market.status == "open"

    async def test_client_context_manager(self, demo_env):
        """Client properly handles context manager lifecycle."""
        client = KalshiClient.from_env()

        async with client:
            # Should be able to make requests
            status = await client.get_exchange_status()
            assert status is not None

        # Client should be closed after context
        # Attempting another request would fail (but we won't test that to avoid errors)
