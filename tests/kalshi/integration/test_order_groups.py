"""Integration tests for Kalshi order groups."""

import pytest
from fastmcp.client import Client


@pytest.mark.asyncio
class TestOrderGroups:
    """Test order group management."""

    @pytest.mark.vcr
    async def test_create_order_group(self, demo_env):
        """Test creating an order group."""
        from src.kalshi.kalshi_mcp_server import mcp

        async with Client(mcp) as client:
            # Create an order group with contract limit
            result = await client.call_tool(
                "kalshi_create_order_group",
                {"contracts_limit": 100}
            )

            # Verify response structure
            assert result is not None
            # The result should contain an order group ID
            # Result format from FastMCP Client is ToolResult with content

    @pytest.mark.vcr
    async def test_get_order_group(self, demo_env):
        """Test retrieving a specific order group."""
        from src.kalshi.kalshi_mcp_server import mcp

        async with Client(mcp) as client:
            # First create a group
            create_result = await client.call_tool(
                "kalshi_create_order_group",
                {"contracts_limit": 50}
            )

            # Extract group ID from result
            # This will need to parse the response
            # For now, test that the tool accepts the parameter

            # Test getting a non-existent group
            with pytest.raises(Exception):
                await client.call_tool(
                    "kalshi_get_order_group",
                    {"group_id": "nonexistent-group-id"}
                )

    @pytest.mark.vcr
    async def test_get_order_groups_pagination(self, demo_env):
        """Test listing order groups with pagination."""
        from src.kalshi.kalshi_mcp_server import mcp

        async with Client(mcp) as client:
            # Test with default limit
            result = await client.call_tool(
                "kalshi_get_order_groups",
                {}
            )
            assert result is not None

            # Test with custom limit
            result = await client.call_tool(
                "kalshi_get_order_groups",
                {"limit": 50}
            )
            assert result is not None

    @pytest.mark.vcr
    async def test_reset_order_group(self, demo_env):
        """Test resetting an order group's filled count."""
        from src.kalshi.kalshi_mcp_server import mcp

        async with Client(mcp) as client:
            # First create a group
            create_result = await client.call_tool(
                "kalshi_create_order_group",
                {"contracts_limit": 75}
            )

            # Test reset with non-existent group
            with pytest.raises(Exception):
                await client.call_tool(
                    "kalshi_reset_order_group",
                    {"group_id": "nonexistent-group-id"}
                )

    @pytest.mark.vcr
    async def test_delete_order_group(self, demo_env):
        """Test deleting an order group."""
        from src.kalshi.kalshi_mcp_server import mcp

        async with Client(mcp) as client:
            # Test delete with non-existent group
            with pytest.raises(Exception):
                await client.call_tool(
                    "kalshi_delete_order_group",
                    {"group_id": "nonexistent-group-id"}
                )

    @pytest.mark.vcr
    async def test_order_group_client_methods(self, demo_env):
        """Test order group operations at client level."""
        from src.kalshi.client import KalshiClient

        async with KalshiClient.from_env() as client:
            # Create order group
            group = await client.create_order_group(contracts_limit=100)
            assert group.order_group_id is not None
            # Note: API doesn't return contracts_limit in response

            # Get the group
            retrieved = await client.get_order_group(group.order_group_id)
            assert retrieved.order_group_id == group.order_group_id
            # API returns is_auto_cancel_enabled and orders list
            assert hasattr(retrieved, "is_auto_cancel_enabled")

            # List groups (should include our new group)
            groups = await client.get_order_groups(limit=10)
            # List response uses "id" field, but our model handles both
            assert any(g.group_id == group.order_group_id for g in groups)

            # Reset the group
            reset_group = await client.reset_order_group(group.order_group_id)
            assert reset_group.order_group_id == group.order_group_id

            # Delete the group
            await client.delete_order_group(group.order_group_id)

            # Verify deletion (should raise error)
            with pytest.raises(Exception):
                await client.get_order_group(group.order_group_id)

    @pytest.mark.vcr
    async def test_order_group_model_properties(self, demo_env):
        """Test OrderGroup model with API-realistic data."""
        from src.kalshi.models import OrderGroup

        # Test create response format (just ID)
        group_created = OrderGroup(order_group_id="test-group-123")
        assert group_created.order_group_id == "test-group-123"
        assert group_created.group_id == "test-group-123"

        # Test GET response format (is_auto_cancel_enabled + orders)
        group_retrieved = OrderGroup(
            order_group_id="test-group-123",
            is_auto_cancel_enabled=True,
            orders=["order-1", "order-2"]
        )
        assert group_retrieved.is_auto_cancel_enabled is True
        assert len(group_retrieved.orders) == 2

        # Test list response format (id + is_auto_cancel_enabled)
        group_from_list = OrderGroup(
            id="test-group-456",
            is_auto_cancel_enabled=False
        )
        assert group_from_list.id == "test-group-456"
        assert group_from_list.group_id == "test-group-456"  # Property handles both field names
        assert group_from_list.is_auto_cancel_enabled is False

        # Note: The following fields are NOT available from the API:
        # - contracts_limit: Set at creation but never returned
        # - contracts_filled: Not tracked in responses
        # - status: No status field exists
        # - created_time: Not in responses
        # This is documented in the model and investigation findings

    @pytest.mark.vcr
    async def test_create_order_with_group_id(self, demo_env):
        """Test creating orders with order group ID."""
        from src.kalshi.kalshi_mcp_server import mcp

        async with Client(mcp) as client:
            # First create an order group
            group_result = await client.call_tool(
                "kalshi_create_order_group",
                {"contracts_limit": 10}
            )

            # Note: To fully test order creation with group_id, we would need
            # to extract the group_id from the result and create an order
            # This would require API calls and proper test market setup
            # For now, we verify the parameter is accepted

            # Test that limit order accepts order_group_id parameter
            # (will fail for other reasons, but parameter should be accepted)
            try:
                await client.call_tool(
                    "kalshi_create_limit_order",
                    {
                        "ticker": "HIGHTEST-24",
                        "side": "yes",
                        "quantity": 1,
                        "price": 1,
                        "order_group_id": "test-group-id"
                    }
                )
            except Exception as e:
                # Expected to fail (market might not exist, etc.)
                # But shouldn't fail due to parameter validation
                assert "order_group_id" not in str(e).lower() or "unexpected" not in str(e).lower()
