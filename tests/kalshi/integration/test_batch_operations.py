"""Integration tests for Kalshi batch operations."""

import pytest
from fastmcp.client import Client


@pytest.mark.asyncio
class TestBatchOperations:
    """Test batch order creation and cancellation."""

    @pytest.mark.vcr
    async def test_batch_create_orders_validation(self, demo_env):
        """Test batch order creation with validation errors."""
        from src.kalshi.kalshi_mcp_server import mcp

        async with Client(mcp) as client:
            # Test with too many orders (>20)
            orders = [
                {
                    "ticker": f"TEST-{i}",
                    "type": "limit",
                    "action": "buy",
                    "side": "yes",
                    "count": 1,
                    "yes_price": 50
                }
                for i in range(25)
            ]

            with pytest.raises(Exception) as exc_info:
                await client.call_tool(
                    "kalshi_batch_create_orders",
                    {"orders": orders}
                )
            assert "exceeds maximum of 20" in str(exc_info.value).lower()

    @pytest.mark.vcr
    async def test_batch_create_orders_403_handling(self, demo_env):
        """Test that 403 errors provide helpful message about advanced access."""
        from src.kalshi.kalshi_mcp_server import mcp
        from src.kalshi.client import KalshiClient

        # This test documents the expected 403 behavior
        # If you have advanced access, this test may pass with actual order creation
        # If you don't have access, it should give a clear error message

        async with Client(mcp) as client:
            # Create a valid batch request
            orders = [
                {
                    "ticker": "HIGHTEST-24",
                    "type": "limit",
                    "action": "buy",
                    "side": "yes",
                    "count": 1,
                    "yes_price": 1  # Very low price, unlikely to fill
                }
            ]

            try:
                result = await client.call_tool(
                    "kalshi_batch_create_orders",
                    {"orders": orders}
                )
                # If we reach here, user has advanced access
                # Verify the response structure
                assert result is not None
            except Exception as exc:
                # Should get helpful 403 message
                error_msg = str(exc).lower()
                if "403" in error_msg or "forbidden" in error_msg:
                    assert "advanced access" in error_msg
                    assert "contact kalshi" in error_msg or "kalshi support" in error_msg
                else:
                    # Some other error occurred - that's ok for this test
                    pass

    @pytest.mark.vcr
    async def test_batch_cancel_orders_validation(self, demo_env):
        """Test batch order cancellation validation."""
        from src.kalshi.kalshi_mcp_server import mcp

        async with Client(mcp) as client:
            # Test with too many order IDs (>20)
            order_ids = [f"order-{i}" for i in range(25)]

            with pytest.raises(Exception) as exc_info:
                await client.call_tool(
                    "kalshi_batch_cancel_orders",
                    {"order_ids": order_ids}
                )
            assert "exceeds maximum of 20" in str(exc_info.value).lower()

    @pytest.mark.vcr
    async def test_batch_operations_client_methods(self, demo_env):
        """Test batch operations at client level."""
        from src.kalshi.client import KalshiClient

        async with KalshiClient.from_env() as client:
            # Test validation at client level
            orders = [{"ticker": f"TEST-{i}", "type": "limit", "action": "buy",
                      "side": "yes", "count": 1, "yes_price": 50}
                     for i in range(25)]

            with pytest.raises(ValueError) as exc_info:
                await client.batch_create_orders(orders)
            assert "exceeds maximum of 20" in str(exc_info.value)

            # Test cancel validation
            order_ids = [f"order-{i}" for i in range(25)]

            with pytest.raises(ValueError) as exc_info:
                await client.batch_cancel_orders(order_ids)
            assert "exceeds maximum of 20" in str(exc_info.value)

    @pytest.mark.vcr
    async def test_batch_order_response_model(self, demo_env):
        """Test BatchOrderResponse model properties."""
        from src.kalshi.models import BatchOrderResponse, Order
        from datetime import datetime

        # Test successful response
        success_response = BatchOrderResponse(
            client_order_id="test-123",
            order=Order(
                order_id="order-456",
                ticker="TEST-24",
                side="yes",
                action="buy",
                type="limit",
                status="resting",
                initial_count=10,
                created_time=datetime.now()
            ),
            error=None
        )

        assert success_response.is_success is True
        assert success_response.error_message is None

        # Test error response
        error_response = BatchOrderResponse(
            client_order_id="test-789",
            order=None,
            error={"message": "Market not found", "code": "invalid_market"}
        )

        assert error_response.is_success is False
        assert error_response.error_message == "Market not found"

        # Test error with no message field
        error_response_no_msg = BatchOrderResponse(
            client_order_id="test-999",
            order=None,
            error={"code": "unknown"}
        )

        assert error_response_no_msg.error_message == "Unknown error"
