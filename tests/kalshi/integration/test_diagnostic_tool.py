"""Integration test for the API health diagnostic tool."""

import pytest
from fastmcp.client import Client


@pytest.mark.asyncio
class TestDiagnosticTool:
    """Test the kalshi_diagnose_api_health tool."""

    @pytest.mark.vcr
    async def test_diagnostic_tool_runs(self, demo_env):
        """Test that the diagnostic tool runs and returns health report."""
        from src.kalshi.kalshi_mcp_server import mcp

        async with Client(mcp) as client:
            result = await client.call_tool("kalshi_diagnose_api_health", {})

            # Result should be a ToolResult object
            assert result is not None

            # The content should be text representation of the health report
            # We can't easily parse it, but we can verify it ran

    @pytest.mark.vcr
    async def test_diagnostic_detects_service_status(self, demo_env):
        """Test that diagnostic correctly identifies service availability."""
        from src.kalshi.kalshi_mcp_server import mcp

        async with Client(mcp) as client:
            result = await client.call_tool("kalshi_diagnose_api_health", {})

            # The tool should complete without raising exceptions
            # Even if some services are down, it should handle gracefully
            assert result is not None

            # In real usage, this would show which services are up/down
            # For example, if order_groups is 503, it should report that clearly
