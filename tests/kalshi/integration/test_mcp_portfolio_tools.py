"""Integration tests for Kalshi MCP portfolio management tools."""

import pytest
from fastmcp.client import Client


@pytest.mark.asyncio
class TestPortfolioTools:
    """Test portfolio management MCP tools."""

    async def test_get_positions(self, demo_env):
        """Test getting portfolio positions via MCP."""
        from src.kalshi.kalshi_mcp_server import mcp

        async with Client(mcp) as client:
            result = await client.call_tool("kalshi_get_positions", {})

            # Should return valid result (even if empty list)
            assert result is not None
            # Result may have no content if empty
            if result.content:
                positions_text = result.content[0].text
                assert "position" in positions_text.lower() or "Position" in positions_text

    async def test_get_positions_with_filter(self, demo_env):
        """Test getting positions filtered by ticker."""
        from src.kalshi.kalshi_mcp_server import mcp

        async with Client(mcp) as client:
            result = await client.call_tool(
                "kalshi_get_positions",
                {"ticker": "HIGHTEST", "limit": 10}
            )

            # Should work even if no positions exist for that ticker
            assert result is not None

    async def test_get_fills(self, demo_env):
        """Test getting trade fills via MCP."""
        from src.kalshi.kalshi_mcp_server import mcp

        async with Client(mcp) as client:
            result = await client.call_tool("kalshi_get_fills", {})

            # Should return valid result (even if empty list)
            assert result is not None
            # Result may have no content if empty
            if result.content:
                fills_text = result.content[0].text
                assert "fill" in fills_text.lower() or "Fill" in fills_text

    async def test_get_fills_with_ticker_filter(self, demo_env):
        """Test getting fills filtered by ticker."""
        from src.kalshi.kalshi_mcp_server import mcp

        async with Client(mcp) as client:
            result = await client.call_tool(
                "kalshi_get_fills",
                {"ticker": "HIGHTEST-24", "limit": 20}
            )

            assert result is not None

    async def test_get_orders_resting(self, demo_env):
        """Test getting active orders via MCP."""
        from src.kalshi.kalshi_mcp_server import mcp

        async with Client(mcp) as client:
            result = await client.call_tool(
                "kalshi_get_orders",
                {"status": "resting"}
            )
            orders_text = result.content[0].text

            # Should return valid result (even if no active orders)
            assert result is not None
            assert "order" in orders_text.lower() or "Order" in orders_text

    async def test_get_orders_filled(self, demo_env):
        """Test getting filled orders via MCP."""
        from src.kalshi.kalshi_mcp_server import mcp

        async with Client(mcp) as client:
            result = await client.call_tool(
                "kalshi_get_orders",
                {"status": "filled", "limit": 10}
            )

            assert result is not None

    async def test_get_orders_with_ticker_filter(self, demo_env):
        """Test getting orders filtered by ticker."""
        from src.kalshi.kalshi_mcp_server import mcp

        async with Client(mcp) as client:
            result = await client.call_tool(
                "kalshi_get_orders",
                {
                    "ticker": "HIGHTEST-24",
                    "status": "resting",
                    "limit": 10
                }
            )

            assert result is not None

    async def test_portfolio_workflow(self, demo_env):
        """Test complete portfolio workflow: positions → fills → orders."""
        from src.kalshi.kalshi_mcp_server import mcp

        async with Client(mcp) as client:
            # Step 1: Check current positions
            positions_result = await client.call_tool("kalshi_get_positions", {})
            assert positions_result is not None

            # Step 2: Check trade history
            fills_result = await client.call_tool(
                "kalshi_get_fills",
                {"limit": 50}
            )
            assert fills_result is not None

            # Step 3: Check active orders
            orders_result = await client.call_tool(
                "kalshi_get_orders",
                {"status": "resting"}
            )
            assert orders_result is not None

            # All three should be callable without errors
            # (Results may be empty if account has no activity)
