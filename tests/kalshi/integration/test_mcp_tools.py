"""Integration tests for MCP tools via FastMCP Client.

These tests properly test the MCP tools as they would be called by Claude,
using the FastMCP Client to interact with the server via MCP protocol.

NOTE: We don't use a fixture for the MCP client because async fixtures cause
event loop context issues with FastMCP Client. Instead, each test creates
its own client instance.
"""

import pytest
from fastmcp.client import Client
from fastmcp.client.transports import FastMCPTransport


@pytest.mark.asyncio
class TestMCPToolsViaProtocol:
    """Test all 4 MVP MCP tools via FastMCP Client (MCP protocol)."""

    async def test_list_tools(self, demo_env):
        """Verify server exposes all expected tools."""
        from src.kalshi.kalshi_mcp_server import mcp

        async with Client(mcp) as client:
            tools = await client.list_tools()

            tool_names = [tool.name for tool in tools]

            assert len(tool_names) == 16
            # Original 4 tools
            assert "kalshi_get_exchange_status" in tool_names
            assert "kalshi_get_balance" in tool_names
            assert "kalshi_search_markets" in tool_names
            assert "kalshi_get_market" in tool_names
            # 5 order execution tools
            assert "kalshi_create_market_order" in tool_names
            assert "kalshi_create_limit_order" in tool_names
            assert "kalshi_cancel_order" in tool_names
            assert "kalshi_amend_order" in tool_names
            assert "kalshi_decrease_order" in tool_names
            # 3 portfolio management tools
            assert "kalshi_get_positions" in tool_names
            assert "kalshi_get_fills" in tool_names
            assert "kalshi_get_orders" in tool_names
            # 4 market discovery tools
            assert "kalshi_get_events" in tool_names
            assert "kalshi_get_event" in tool_names
            assert "kalshi_get_orderbook" in tool_names
            assert "kalshi_get_trades" in tool_names

    async def test_kalshi_get_exchange_status(self, demo_env):
        """Tool: kalshi_get_exchange_status via MCP."""
        from src.kalshi.kalshi_mcp_server import mcp

        async with Client(mcp) as client:
            result = await client.call_tool(
                name="kalshi_get_exchange_status",
                arguments={}
            )

            assert result.data is not None
            assert hasattr(result.data, "exchange_active")
            assert hasattr(result.data, "trading_active")

    async def test_kalshi_get_balance(self, demo_env):
        """Tool: kalshi_get_balance via MCP."""
        from src.kalshi.kalshi_mcp_server import mcp

        async with Client(mcp) as client:
            result = await client.call_tool(
                name="kalshi_get_balance",
                arguments={}
            )

            assert result.data is not None
            assert hasattr(result.data, "balance")
            assert result.data.balance >= 0

    async def test_kalshi_search_markets_default(self, demo_env):
        """Tool: kalshi_search_markets (default) via MCP."""
        from src.kalshi.kalshi_mcp_server import mcp

        async with Client(mcp) as client:
            result = await client.call_tool(
                name="kalshi_search_markets",
                arguments={}
            )

            assert result.data is not None
            assert isinstance(result.data, list)
            assert len(result.data) > 0

    async def test_kalshi_search_markets_with_limit(self, demo_env):
        """Tool: kalshi_search_markets (with limit) via MCP."""
        from src.kalshi.kalshi_mcp_server import mcp

        async with Client(mcp) as client:
            result = await client.call_tool(
                name="kalshi_search_markets",
                arguments={"limit": 5}
            )

            assert result.data is not None
            assert isinstance(result.data, list)
            assert len(result.data) <= 5

    async def test_kalshi_get_market(self, demo_env, active_market):
        """Tool: kalshi_get_market via MCP."""
        from src.kalshi.kalshi_mcp_server import mcp

        async with Client(mcp) as client:
            result = await client.call_tool(
                name="kalshi_get_market",
                arguments={"ticker": active_market.ticker}
            )

            assert result.data is not None
            assert result.data.ticker == active_market.ticker


@pytest.mark.asyncio
class TestMCPResources:
    """Test MCP resources via protocol."""

    async def test_list_resources(self, demo_env):
        """Verify server exposes expected resources."""
        from src.kalshi.kalshi_mcp_server import mcp

        async with Client(mcp) as client:
            resources = await client.list_resources()

            resource_uris = [str(resource.uri) for resource in resources]

            assert len(resource_uris) == 2
            assert "kalshi://account/balance" in resource_uris
            assert "kalshi://exchange/status" in resource_uris

    async def test_read_balance_resource(self, demo_env):
        """Read balance resource via MCP."""
        from src.kalshi.kalshi_mcp_server import mcp

        async with Client(mcp) as client:
            result = await client.read_resource(uri="kalshi://account/balance")
            assert result is not None
            assert len(result) > 0

    async def test_read_status_resource(self, demo_env):
        """Read exchange status resource via MCP."""
        from src.kalshi.kalshi_mcp_server import mcp

        async with Client(mcp) as client:
            result = await client.read_resource(uri="kalshi://exchange/status")
            assert result is not None
            assert len(result) > 0


@pytest.mark.asyncio
class TestMCPWorkflows:
    """Test realistic workflows using MCP protocol."""

    async def test_research_workflow(self, demo_env):
        """
        Workflow: Search → Get details
        Simulates LLM research workflow via MCP.
        """
        from src.kalshi.kalshi_mcp_server import mcp

        async with Client(mcp) as client:
            # 1. Search for markets
            search_result = await client.call_tool(
                name="kalshi_search_markets",
                arguments={"limit": 5}
            )
            assert len(search_result.data) > 0

            # 2. Get details on first market
            # Note: MCP returns dicts, not Market objects
            first_ticker = search_result.data[0]["ticker"]
            market_result = await client.call_tool(
                name="kalshi_get_market",
                arguments={"ticker": first_ticker}
            )
            assert market_result.data.ticker == first_ticker

    async def test_account_check_workflow(self, demo_env):
        """
        Workflow: Check exchange → Check balance
        Simulates LLM checking account readiness via MCP.
        """
        from src.kalshi.kalshi_mcp_server import mcp

        async with Client(mcp) as client:
            # 1. Verify exchange is operational
            status_result = await client.call_tool(
                name="kalshi_get_exchange_status",
                arguments={}
            )
            assert status_result.data.exchange_active is True

            # 2. Check account balance
            balance_result = await client.call_tool(
                name="kalshi_get_balance",
                arguments={}
            )
            assert balance_result.data.balance >= 0
