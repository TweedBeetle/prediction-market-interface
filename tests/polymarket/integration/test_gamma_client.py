"""
Integration tests for Polymarket Gamma API client (market data).

These tests hit the real Polymarket Gamma API and do NOT require:
- Wallet credentials
- Funds
- Authentication

They test read-only market data endpoints.
"""

import pytest

from src.polymarket.gamma_client import GammaClient


@pytest.mark.asyncio
class TestGammaClientMarketData:
    """Test Gamma client market data endpoints (no auth required)."""

    async def test_search_markets(self):
        """Test searching for markets."""
        async with GammaClient() as client:
            markets = await client.search_markets(
                query="election",
                active=True,
                limit=5
            )

            # Verify we got results
            assert isinstance(markets, list)
            assert len(markets) <= 5

            # If we have results, verify market structure
            if markets:
                market = markets[0]
                assert hasattr(market, 'id')
                assert hasattr(market, 'question')
                assert hasattr(market, 'clob_token_ids')
                assert isinstance(market.clob_token_ids, list)

    async def test_search_markets_no_query(self):
        """Test searching without query returns active markets."""
        async with GammaClient() as client:
            markets = await client.search_markets(
                active=True,
                limit=10
            )

            assert isinstance(markets, list)
            assert len(markets) <= 10

    async def test_get_market_by_id(self):
        """Test getting a specific market by ID."""
        # First search for a market to get an ID
        async with GammaClient() as client:
            markets = await client.search_markets(active=True, limit=1)

            if not markets:
                pytest.skip("No active markets available for testing")

            market_id = markets[0].id

            # Now get that specific market
            market = await client.get_market(market_id)

            assert market.id == market_id
            assert market.question
            assert len(market.clob_token_ids) >= 1
            assert market.yes_token_id  # Should have YES token
            assert market.no_token_id if len(market.clob_token_ids) > 1 else True

    async def test_get_orderbook(self):
        """Test getting orderbook for a token."""
        # First get a market to get token ID
        async with GammaClient() as client:
            markets = await client.search_markets(active=True, limit=1)

            if not markets:
                pytest.skip("No active markets available for testing")

            token_id = markets[0].yes_token_id

            if not token_id:
                pytest.skip("Market has no YES token ID")

            # Get orderbook
            orderbook = await client.get_orderbook(token_id)

            assert orderbook.token_id == token_id
            assert isinstance(orderbook.bids, list)
            assert isinstance(orderbook.asks, list)

            # Orderbook may be empty, but structure should be correct
            if orderbook.bids:
                bid = orderbook.bids[0]
                assert hasattr(bid, 'price')
                assert hasattr(bid, 'size')
                assert 0 < bid.price < 1

            if orderbook.asks:
                ask = orderbook.asks[0]
                assert hasattr(ask, 'price')
                assert hasattr(ask, 'size')
                assert 0 < ask.price < 1

    # NOTE: Trades endpoint moved to ClobClient (requires authentication)
    # See tests/polymarket/integration/test_clob_client.py for trades tests

    async def test_get_events(self):
        """Test listing events."""
        async with GammaClient() as client:
            events = await client.get_events(active=True, limit=5)

            assert isinstance(events, list)
            assert len(events) <= 5

            # If we have events, verify structure
            if events:
                event = events[0]
                assert hasattr(event, 'id')
                assert hasattr(event, 'title')
                assert hasattr(event, 'markets')
                assert isinstance(event.markets, list)

    async def test_get_event_by_id(self):
        """Test getting a specific event."""
        async with GammaClient() as client:
            # First get list of events
            events = await client.get_events(active=True, limit=1)

            if not events:
                pytest.skip("No active events available")

            event_id = events[0].id

            # Now get that specific event
            event = await client.get_event(event_id)

            assert event.id == event_id
            assert event.title
            assert isinstance(event.markets, list)

    async def test_market_helper_properties(self):
        """Test market helper properties work correctly."""
        async with GammaClient() as client:
            markets = await client.search_markets(active=True, limit=1)

            if not markets:
                pytest.skip("No markets available")

            market = markets[0]

            # Test token ID properties
            assert isinstance(market.yes_token_id, str)
            assert isinstance(market.no_token_id, str)

            # Test spread calculation (if prices available)
            if market.best_bid and market.best_ask:
                spread = market.spread
                assert spread is not None
                assert spread >= 0
                assert spread < 1

                midpoint = market.midpoint_price
                assert midpoint is not None
                assert 0 < midpoint < 1
                assert market.best_bid <= midpoint <= market.best_ask

            # Test interpretation
            interpretation = market.interpretation
            assert isinstance(interpretation, str)
            assert market.question in interpretation

    async def test_client_from_env(self):
        """Test creating client from environment variables."""
        # Should work with defaults even if no env vars set
        client = GammaClient.from_env()

        assert client is not None
        assert client.base_url

        # Test it works
        async with client:
            markets = await client.search_markets(active=True, limit=1)
            assert isinstance(markets, list)


@pytest.mark.asyncio
class TestGammaClientErrorHandling:
    """Test error handling for Gamma client."""

    async def test_invalid_market_id(self):
        """Test getting non-existent market raises error."""
        from src.polymarket.base_client import MarketNotFoundError

        async with GammaClient() as client:
            with pytest.raises((MarketNotFoundError, Exception)):
                await client.get_market("invalid_market_id_12345")

    async def test_invalid_token_id_orderbook(self):
        """Test getting orderbook for invalid token."""
        async with GammaClient() as client:
            # May return empty orderbook or raise error
            try:
                orderbook = await client.get_orderbook("invalid_token_id")
                # If it succeeds, should return empty orderbook
                assert isinstance(orderbook.bids, list)
                assert isinstance(orderbook.asks, list)
            except Exception:
                # Error is also acceptable
                pass


@pytest.mark.asyncio
class TestGammaClientPagination:
    """Test pagination and limits."""

    async def test_search_markets_respects_limit(self):
        """Test limit parameter is respected."""
        async with GammaClient() as client:
            markets = await client.search_markets(active=True, limit=3)

            assert len(markets) <= 3

    # NOTE: Trades tests removed (moved to ClobClient)

    async def test_get_events_respects_limit(self):
        """Test events limit parameter."""
        async with GammaClient() as client:
            events = await client.get_events(active=True, limit=2)

            assert len(events) <= 2
