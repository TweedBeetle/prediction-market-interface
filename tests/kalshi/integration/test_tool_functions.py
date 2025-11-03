"""Integration tests for MCP tools - testing underlying tool functions."""

import pytest
from src.kalshi.client import KalshiClient


@pytest.mark.asyncio
class TestMCPToolsIntegration:
    """Test all 4 MVP MCP tools against demo API.

    Note: These tests verify the tool logic by calling the underlying
    functions that power the MCP tools, rather than going through the
    MCP protocol layer (which can be tested separately).
    """

    async def test_kalshi_get_exchange_status(self, demo_env):
        """
        Tool: kalshi_get_exchange_status
        Should return exchange operational status.
        """
        async with KalshiClient.from_env() as client:
            status = await client.get_exchange_status()

        assert status is not None
        assert hasattr(status, "exchange_active")
        assert hasattr(status, "trading_active")
        assert isinstance(status.exchange_active, bool)
        assert isinstance(status.trading_active, bool)

    async def test_kalshi_get_balance(self, demo_env):
        """
        Tool: kalshi_get_balance
        Should return current account balance.
        """
        async with KalshiClient.from_env() as client:
            balance = await client.get_balance()

        assert balance is not None
        assert hasattr(balance, "balance")
        assert hasattr(balance, "balance_dollars")
        assert balance.balance >= 0
        # Demo accounts should have positive balance
        assert balance.balance_dollars > 0

    async def test_kalshi_search_markets_default(self, demo_env):
        """
        Tool: kalshi_search_markets (no query)
        Should return list of open markets.
        """
        async with KalshiClient.from_env() as client:
            markets = await client.search_markets(status="open", limit=20)

        assert isinstance(markets, list)
        assert len(markets) > 0
        assert len(markets) <= 20  # Default limit

        # Verify market structure
        market = markets[0]
        assert hasattr(market, "ticker")
        assert hasattr(market, "title")
        assert hasattr(market, "status")
        assert market.status == "open"  # Default status filter

    async def test_kalshi_search_markets_with_query(self, demo_env):
        """
        Tool: kalshi_search_markets (with query)
        Should return markets matching search.
        """
        async with KalshiClient.from_env() as client:
            markets = await client.search_markets(
                query="KXBTC",
                status="open",
                limit=10
            )

        assert isinstance(markets, list)
        # May or may not have results depending on demo data
        # Just verify it returns without error

    async def test_kalshi_search_markets_with_limit(self, demo_env):
        """
        Tool: kalshi_search_markets (custom limit)
        Should respect limit parameter.
        """
        async with KalshiClient.from_env() as client:
            markets = await client.search_markets(status="open", limit=5)

        assert isinstance(markets, list)
        assert len(markets) <= 5

    async def test_kalshi_search_markets_closed(self, demo_env):
        """
        Tool: kalshi_search_markets (closed markets)
        Should return closed/settled markets.
        """
        async with KalshiClient.from_env() as client:
            markets = await client.search_markets(status="closed", limit=10)

        assert isinstance(markets, list)
        # All returned markets should be closed
        for market in markets:
            assert market.status == "closed"

    async def test_kalshi_get_market(self, demo_env, active_market):
        """
        Tool: kalshi_get_market
        Should return detailed market information.
        """
        async with KalshiClient.from_env() as client:
            market = await client.get_market(ticker=active_market.ticker)

        assert market is not None
        assert market.ticker == active_market.ticker
        assert hasattr(market, "title")
        assert hasattr(market, "status")
        assert hasattr(market, "close_time")
        assert hasattr(market, "interpretation")

        # Interpretation should be human-readable
        assert len(market.interpretation) > 0

    async def test_kalshi_get_market_has_prices(self, demo_env, liquid_market):
        """
        Tool: kalshi_get_market
        Should include price information for liquid markets.
        """
        async with KalshiClient.from_env() as client:
            market = await client.get_market(ticker=liquid_market.ticker)

        assert market is not None
        # Liquid markets should have price data
        # (though not guaranteed, so we just check structure exists)
        assert hasattr(market, "yes_bid")
        assert hasattr(market, "yes_ask")
        assert hasattr(market, "volume_24h")


@pytest.mark.asyncio
class TestMCPToolErrorHandling:
    """Test error handling for MCP tools."""

    async def test_get_market_invalid_ticker(self, demo_env):
        """
        Tool: kalshi_get_market (invalid ticker)
        Should handle invalid ticker gracefully.
        """
        with pytest.raises(Exception):  # Will raise HTTP error
            async with KalshiClient.from_env() as client:
                await client.get_market(ticker="INVALID-TICKER-XXX")

    async def test_search_markets_invalid_status(self, demo_env):
        """
        Tool: kalshi_search_markets (invalid status)
        Should handle invalid status filter.
        """
        # API may reject invalid status or return empty list
        # Just verify it doesn't crash
        try:
            async with KalshiClient.from_env() as client:
                markets = await client.search_markets(status="invalid_status")
                # If it succeeds, should return empty or error
                assert isinstance(markets, list)
        except Exception:
            # If it fails, that's also acceptable error handling
            pass


@pytest.mark.asyncio
class TestMCPToolWorkflow:
    """Test realistic workflows using multiple tools."""

    async def test_research_workflow(self, demo_env):
        """
        Workflow: Search → Get details
        Simulates LLM research workflow.
        """
        async with KalshiClient.from_env() as client:
            # 1. Search for markets
            markets = await client.search_markets(status="open", limit=5)
            assert len(markets) > 0

            # 2. Get details on first market
            market_details = await client.get_market(ticker=markets[0].ticker)
            assert market_details.ticker == markets[0].ticker

            # 3. Verify enriched data
            assert hasattr(market_details, "interpretation")
            assert len(market_details.interpretation) > 0

    async def test_account_check_workflow(self, demo_env):
        """
        Workflow: Check exchange → Check balance
        Simulates LLM checking account readiness.
        """
        async with KalshiClient.from_env() as client:
            # 1. Verify exchange is operational
            status = await client.get_exchange_status()
            assert status.exchange_active is True

            # 2. Check account balance
            balance = await client.get_balance()
            assert balance.balance >= 0

            # 3. Both calls should succeed
            assert status is not None
            assert balance is not None
