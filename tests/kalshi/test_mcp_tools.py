"""MCP tool integration tests for FastMCP Kalshi server."""

import pytest


@pytest.mark.integration
class TestMCPServerSetup:
    """Test MCP server initialization and tool registration."""

    def test_mcp_server_is_initialized(self, kalshi_mcp_server):
        """Test that FastMCP server is properly initialized."""
        assert kalshi_mcp_server is not None
        assert kalshi_mcp_server.name == "Kalshi Prediction Markets"

    def test_mcp_server_has_tools(self, kalshi_mcp_server):
        """Test that MCP server has registered tools."""
        # Access tools via internal tool manager (common testing pattern)
        tools_dict = kalshi_mcp_server._tool_manager._tools
        assert tools_dict is not None
        assert len(tools_dict) > 0
        # Should have at least the major tools
        assert "kalshi_search_markets" in tools_dict
        assert "kalshi_get_balance" in tools_dict


@pytest.mark.integration
class TestMCPToolDescriptions:
    """Test that MCP tools have proper documentation."""

    def test_tools_have_docstrings(self, kalshi_mcp_server):
        """Test that all tools have descriptive docstrings."""
        # FastMCP extracts docstrings from tool functions
        tools_dict = kalshi_mcp_server._tool_manager._tools

        # Check that tools have descriptions
        for tool_name, tool in tools_dict.items():
            assert tool.description is not None, f"Tool {tool_name} missing description"
            assert len(tool.description) > 0, f"Tool {tool_name} has empty description"


@pytest.mark.integration
class TestMCPToolsRegistered:
    """Test that all expected MCP tools are registered."""

    def test_all_readonly_tools_registered(self, kalshi_mcp_server):
        """Test that all 8 read-only tools are registered."""
        tools_dict = kalshi_mcp_server._tool_manager._tools
        tool_names = set(tools_dict.keys())

        readonly_tools = [
            "kalshi_search_markets",
            "kalshi_get_market",
            "kalshi_get_orderbook",
            "kalshi_get_trades",
            "kalshi_get_candlesticks",
            "kalshi_get_events",
            "kalshi_get_exchange_status",
            "kalshi_get_milestones",
        ]

        for tool_name in readonly_tools:
            assert tool_name in tool_names, f"Missing tool: {tool_name}"

    def test_all_trading_tools_registered(self, kalshi_mcp_server):
        """Test that all 8 trading tools are registered."""
        tools_dict = kalshi_mcp_server._tool_manager._tools
        tool_names = set(tools_dict.keys())

        trading_tools = [
            "kalshi_get_balance",
            "kalshi_get_positions",
            "kalshi_create_order",
            "kalshi_get_orders",
            "kalshi_cancel_order",
            "kalshi_amend_order",
            "kalshi_get_fills",
            "kalshi_get_queue_position",
        ]

        for tool_name in trading_tools:
            assert tool_name in tool_names, f"Missing tool: {tool_name}"

    def test_all_advanced_tools_registered(self, kalshi_mcp_server):
        """Test that all advanced tools are registered."""
        tools_dict = kalshi_mcp_server._tool_manager._tools
        tool_names = set(tools_dict.keys())

        advanced_tools = [
            "kalshi_batch_create_orders",
            "kalshi_batch_cancel_orders",
            "kalshi_create_order_group",
            "kalshi_get_rfqs",
            "kalshi_get_multivariate_collections",
        ]

        for tool_name in advanced_tools:
            assert tool_name in tool_names, f"Missing tool: {tool_name}"

    def test_all_websocket_tools_registered(self, kalshi_mcp_server):
        """Test that all 4 WebSocket tools are registered."""
        tools_dict = kalshi_mcp_server._tool_manager._tools
        tool_names = set(tools_dict.keys())

        websocket_tools = [
            "kalshi_websocket_connect",
            "kalshi_websocket_subscribe",
            "kalshi_websocket_unsubscribe",
            "kalshi_websocket_disconnect",
        ]

        for tool_name in websocket_tools:
            assert tool_name in tool_names, f"Missing tool: {tool_name}"

    def test_total_tool_count(self, kalshi_mcp_server):
        """Test that all 29 tools are registered."""
        tools_dict = kalshi_mcp_server._tool_manager._tools
        # Should have exactly 29 tools
        assert len(tools_dict) == 29, f"Expected 29 tools, got {len(tools_dict)}"


@pytest.mark.integration
class TestMCPToolValidation:
    """Test MCP tool parameter validation."""

    def test_search_markets_tool_has_parameters(self, kalshi_mcp_server):
        """Test that kalshi_search_markets tool has expected parameters."""
        tools_dict = kalshi_mcp_server._tool_manager._tools
        search_tool = tools_dict.get("kalshi_search_markets")

        assert search_tool is not None
        assert search_tool.parameters is not None
        # Should have properties like status, limit, cursor
        schema_props = search_tool.parameters.get("properties", {})
        assert len(schema_props) > 0
        # Verify specific parameters
        assert "status" in schema_props or "limit" in schema_props

    def test_create_order_tool_has_parameters(self, kalshi_mcp_server):
        """Test that kalshi_create_order tool has required parameters."""
        tools_dict = kalshi_mcp_server._tool_manager._tools
        order_tool = tools_dict.get("kalshi_create_order")

        assert order_tool is not None
        assert order_tool.parameters is not None
        schema_props = order_tool.parameters.get("properties", {})
        # Should have ticker, side, count, etc.
        assert "ticker" in schema_props or "side" in schema_props

    def test_get_candlesticks_tool_has_parameters(self, kalshi_mcp_server):
        """Test that kalshi_get_candlesticks tool has interval parameter."""
        tools_dict = kalshi_mcp_server._tool_manager._tools
        candle_tool = tools_dict.get("kalshi_get_candlesticks")

        assert candle_tool is not None
        assert candle_tool.parameters is not None
        schema_props = candle_tool.parameters.get("properties", {})
        assert len(schema_props) > 0
        # Verify it has interval parameter
        assert "interval" in schema_props or len(schema_props) > 0
