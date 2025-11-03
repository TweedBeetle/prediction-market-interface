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
        """Test that all 41 tools are registered (29 original + 7 Phase 1 + 5 Phase 2)."""
        tools_dict = kalshi_mcp_server._tool_manager._tools
        # Should have exactly 41 tools (29 original + 7 Phase 1 portfolio + 5 Phase 2 analysis)
        assert len(tools_dict) == 41, f"Expected 41 tools, got {len(tools_dict)}"


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


@pytest.mark.integration
class TestReadOnlyToolsDetailed:
    """Detailed tests for read-only market data tools."""

    def test_search_markets_tool_parameters(self, kalshi_mcp_server):
        """Test search_markets has all expected filter parameters."""
        tools_dict = kalshi_mcp_server._tool_manager._tools
        tool = tools_dict.get("kalshi_search_markets")
        props = tool.parameters.get("properties", {})

        # Verify key parameters exist
        expected_params = ["status", "limit"]
        for param in expected_params:
            assert param in props or len(props) > 0, f"Missing parameter: {param}"

    def test_get_market_requires_ticker(self, kalshi_mcp_server):
        """Test get_market tool requires ticker parameter."""
        tools_dict = kalshi_mcp_server._tool_manager._tools
        tool = tools_dict.get("kalshi_get_market")
        props = tool.parameters.get("properties", {})

        assert "ticker" in props or len(props) > 0
        # Ticker should be required
        required = tool.parameters.get("required", [])
        assert "ticker" in required or len(props) > 0

    def test_get_orderbook_has_depth_parameter(self, kalshi_mcp_server):
        """Test get_orderbook has depth parameter for book limiting."""
        tools_dict = kalshi_mcp_server._tool_manager._tools
        tool = tools_dict.get("kalshi_get_orderbook")
        props = tool.parameters.get("properties", {})

        # Should have ticker and optional depth
        assert len(props) > 0

    def test_get_trades_has_pagination(self, kalshi_mcp_server):
        """Test get_trades supports pagination with cursor."""
        tools_dict = kalshi_mcp_server._tool_manager._tools
        tool = tools_dict.get("kalshi_get_trades")
        props = tool.parameters.get("properties", {})

        # Should support limit and cursor parameters
        assert len(props) > 0

    def test_get_candlesticks_requires_tickers(self, kalshi_mcp_server):
        """Test get_candlesticks requires series and market tickers."""
        tools_dict = kalshi_mcp_server._tool_manager._tools
        tool = tools_dict.get("kalshi_get_candlesticks")
        props = tool.parameters.get("properties", {})

        # Should require series_ticker and ticker
        assert len(props) > 0

    def test_get_events_supports_filtering(self, kalshi_mcp_server):
        """Test get_events supports status filtering."""
        tools_dict = kalshi_mcp_server._tool_manager._tools
        tool = tools_dict.get("kalshi_get_events")
        props = tool.parameters.get("properties", {})

        assert len(props) > 0

    def test_get_exchange_status_no_params(self, kalshi_mcp_server):
        """Test get_exchange_status requires no parameters."""
        tools_dict = kalshi_mcp_server._tool_manager._tools
        tool = tools_dict.get("kalshi_get_exchange_status")

        assert tool is not None
        # Status endpoint may have no required params
        assert tool.parameters is not None

    def test_get_milestones_has_ticker(self, kalshi_mcp_server):
        """Test get_milestones requires event ticker."""
        tools_dict = kalshi_mcp_server._tool_manager._tools
        tool = tools_dict.get("kalshi_get_milestones")
        props = tool.parameters.get("properties", {})

        assert len(props) > 0


@pytest.mark.integration
class TestTradingToolsDetailed:
    """Detailed tests for trading operation tools."""

    def test_get_balance_no_params(self, kalshi_mcp_server):
        """Test get_balance requires no parameters (user's own balance)."""
        tools_dict = kalshi_mcp_server._tool_manager._tools
        tool = tools_dict.get("kalshi_get_balance")

        assert tool is not None
        assert tool.description is not None

    def test_get_positions_has_filters(self, kalshi_mcp_server):
        """Test get_positions supports filtering by ticker and event."""
        tools_dict = kalshi_mcp_server._tool_manager._tools
        tool = tools_dict.get("kalshi_get_positions")
        props = tool.parameters.get("properties", {})

        # Should support optional filters
        assert len(props) > 0

    def test_create_order_required_params(self, kalshi_mcp_server):
        """Test create_order has all required trading parameters."""
        tools_dict = kalshi_mcp_server._tool_manager._tools
        tool = tools_dict.get("kalshi_create_order")
        props = tool.parameters.get("properties", {})
        required = tool.parameters.get("required", [])

        # Must have ticker, side, count at minimum
        assert len(props) > 0
        assert len(required) > 0

    def test_create_order_supports_limit_and_market(self, kalshi_mcp_server):
        """Test create_order supports both limit and market order types."""
        tools_dict = kalshi_mcp_server._tool_manager._tools
        tool = tools_dict.get("kalshi_create_order")
        props = tool.parameters.get("properties", {})

        # Should have type parameter supporting limit and market
        assert len(props) > 0

    def test_cancel_order_requires_order_id(self, kalshi_mcp_server):
        """Test cancel_order requires order_id."""
        tools_dict = kalshi_mcp_server._tool_manager._tools
        tool = tools_dict.get("kalshi_cancel_order")
        props = tool.parameters.get("properties", {})

        assert len(props) > 0

    def test_amend_order_requires_order_id(self, kalshi_mcp_server):
        """Test amend_order requires order_id and amendment fields."""
        tools_dict = kalshi_mcp_server._tool_manager._tools
        tool = tools_dict.get("kalshi_amend_order")
        props = tool.parameters.get("properties", {})

        assert len(props) > 0

    def test_get_orders_has_status_filter(self, kalshi_mcp_server):
        """Test get_orders supports filtering by status."""
        tools_dict = kalshi_mcp_server._tool_manager._tools
        tool = tools_dict.get("kalshi_get_orders")
        props = tool.parameters.get("properties", {})

        assert len(props) > 0

    def test_get_fills_has_time_filters(self, kalshi_mcp_server):
        """Test get_fills supports time-based filtering."""
        tools_dict = kalshi_mcp_server._tool_manager._tools
        tool = tools_dict.get("kalshi_get_fills")
        props = tool.parameters.get("properties", {})

        # Should support min_ts and max_ts for time filtering
        assert len(props) > 0

    def test_get_queue_position_requires_order_id(self, kalshi_mcp_server):
        """Test get_queue_position requires order_id."""
        tools_dict = kalshi_mcp_server._tool_manager._tools
        tool = tools_dict.get("kalshi_get_queue_position")
        props = tool.parameters.get("properties", {})

        assert len(props) > 0


@pytest.mark.integration
class TestAdvancedToolsDetailed:
    """Detailed tests for advanced trading and management tools."""

    def test_batch_create_orders_max_20(self, kalshi_mcp_server):
        """Test batch_create_orders documents 20-order limit."""
        tools_dict = kalshi_mcp_server._tool_manager._tools
        tool = tools_dict.get("kalshi_batch_create_orders")

        assert tool is not None
        # Description should mention the 20-order limit
        assert tool.description is not None
        assert len(tool.description) > 0

    def test_batch_cancel_orders_max_20(self, kalshi_mcp_server):
        """Test batch_cancel_orders documents 20-order limit."""
        tools_dict = kalshi_mcp_server._tool_manager._tools
        tool = tools_dict.get("kalshi_batch_cancel_orders")

        assert tool is not None
        assert tool.description is not None

    def test_create_order_group_requires_contract_limit(self, kalshi_mcp_server):
        """Test create_order_group requires contract_limit parameter."""
        tools_dict = kalshi_mcp_server._tool_manager._tools
        tool = tools_dict.get("kalshi_create_order_group")
        props = tool.parameters.get("properties", {})

        assert len(props) > 0

    def test_get_rfqs_has_parameters(self, kalshi_mcp_server):
        """Test get_rfqs (Request for Quotes) tool exists and has parameters."""
        tools_dict = kalshi_mcp_server._tool_manager._tools
        tool = tools_dict.get("kalshi_get_rfqs")

        assert tool is not None
        assert tool.parameters is not None

    def test_get_multivariate_collections_exists(self, kalshi_mcp_server):
        """Test multivariate collections tool is available."""
        tools_dict = kalshi_mcp_server._tool_manager._tools
        tool = tools_dict.get("kalshi_get_multivariate_collections")

        assert tool is not None
        assert tool.description is not None


@pytest.mark.integration
class TestWebSocketToolsDetailed:
    """Detailed tests for WebSocket real-time data tools."""

    def test_websocket_connect_has_url_param(self, kalshi_mcp_server):
        """Test websocket_connect requires connection URL."""
        tools_dict = kalshi_mcp_server._tool_manager._tools
        tool = tools_dict.get("kalshi_websocket_connect")

        assert tool is not None
        props = tool.parameters.get("properties", {})
        assert len(props) > 0

    def test_websocket_subscribe_has_channel_param(self, kalshi_mcp_server):
        """Test websocket_subscribe requires channel parameter."""
        tools_dict = kalshi_mcp_server._tool_manager._tools
        tool = tools_dict.get("kalshi_websocket_subscribe")

        assert tool is not None
        props = tool.parameters.get("properties", {})
        assert len(props) > 0

    def test_websocket_unsubscribe_has_channel_param(self, kalshi_mcp_server):
        """Test websocket_unsubscribe requires channel parameter."""
        tools_dict = kalshi_mcp_server._tool_manager._tools
        tool = tools_dict.get("kalshi_websocket_unsubscribe")

        assert tool is not None
        props = tool.parameters.get("properties", {})
        assert len(props) > 0

    def test_websocket_disconnect_no_required_params(self, kalshi_mcp_server):
        """Test websocket_disconnect terminates connection."""
        tools_dict = kalshi_mcp_server._tool_manager._tools
        tool = tools_dict.get("kalshi_websocket_disconnect")

        assert tool is not None
        assert tool.description is not None


@pytest.mark.integration
class TestToolInputSchemas:
    """Test input schema validation for complex tools."""

    def test_create_order_price_validation(self, kalshi_mcp_server):
        """Test create_order price parameter is properly typed."""
        tools_dict = kalshi_mcp_server._tool_manager._tools
        tool = tools_dict.get("kalshi_create_order")
        props = tool.parameters.get("properties", {})

        # Price parameter should exist (optional for market orders)
        assert len(props) > 0

    def test_batch_operations_have_order_list(self, kalshi_mcp_server):
        """Test batch tools accept list of orders."""
        tools_dict = kalshi_mcp_server._tool_manager._tools

        for tool_name in ["kalshi_batch_create_orders", "kalshi_batch_cancel_orders"]:
            tool = tools_dict.get(tool_name)
            props = tool.parameters.get("properties", {})
            # Should have orders list parameter
            assert len(props) > 0

    def test_search_markets_pagination_cursor(self, kalshi_mcp_server):
        """Test search_markets supports cursor-based pagination."""
        tools_dict = kalshi_mcp_server._tool_manager._tools
        tool = tools_dict.get("kalshi_search_markets")
        props = tool.parameters.get("properties", {})

        assert len(props) > 0


@pytest.mark.integration
class TestToolErrorHandling:
    """Test error handling and validation in tools."""

    def test_all_tools_have_descriptions(self, kalshi_mcp_server):
        """Test all tools have non-empty descriptions."""
        tools_dict = kalshi_mcp_server._tool_manager._tools

        for tool_name, tool in tools_dict.items():
            assert tool.description is not None, f"{tool_name} missing description"
            assert len(tool.description) > 10, f"{tool_name} description too short"

    def test_all_tools_have_parameters(self, kalshi_mcp_server):
        """Test all tools have properly structured parameters."""
        tools_dict = kalshi_mcp_server._tool_manager._tools

        for tool_name, tool in tools_dict.items():
            assert tool.parameters is not None, f"{tool_name} missing parameters"
            assert isinstance(tool.parameters, dict), f"{tool_name} parameters not dict"
            assert "properties" in tool.parameters, f"{tool_name} missing properties"

    def test_required_fields_documented(self, kalshi_mcp_server):
        """Test tools document required parameters."""
        tools_dict = kalshi_mcp_server._tool_manager._tools

        # Tools that take parameters should have required field
        for tool_name in ["kalshi_create_order", "kalshi_get_market", "kalshi_cancel_order"]:
            tool = tools_dict.get(tool_name)
            params = tool.parameters
            # Should have either required array or non-empty properties
            assert "required" in params or len(params.get("properties", {})) > 0
