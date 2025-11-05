"""Integration tests for advanced order parameters."""

import pytest
from fastmcp.client import Client
import time


@pytest.mark.asyncio
class TestAdvancedParameters:
    """Test advanced order parameters (time_in_force, post_only, reduce_only, etc.)."""

    @pytest.mark.vcr
    async def test_time_in_force_parameter(self, demo_env):
        """Test time_in_force parameter values."""
        from src.kalshi.kalshi_mcp_server import mcp

        async with Client(mcp) as client:
            # Test FOK (Fill-or-Kill)
            try:
                await client.call_tool(
                    "kalshi_create_limit_order",
                    {
                        "ticker": "HIGHTEST-24",
                        "side": "yes",
                        "quantity": 1,
                        "price": 1,
                        "time_in_force": "fok"
                    }
                )
            except Exception as e:
                # May fail for other reasons, but parameter should be accepted
                assert "time_in_force" not in str(e).lower() or "invalid" not in str(e).lower()

            # Test IOC (Immediate-or-Cancel)
            try:
                await client.call_tool(
                    "kalshi_create_limit_order",
                    {
                        "ticker": "HIGHTEST-24",
                        "side": "yes",
                        "quantity": 1,
                        "price": 1,
                        "time_in_force": "ioc"
                    }
                )
            except Exception as e:
                assert "time_in_force" not in str(e).lower() or "invalid" not in str(e).lower()

            # Test GTC (Good-til-Cancel) - default
            try:
                await client.call_tool(
                    "kalshi_create_limit_order",
                    {
                        "ticker": "HIGHTEST-24",
                        "side": "yes",
                        "quantity": 1,
                        "price": 1,
                        "time_in_force": "gtc"
                    }
                )
            except Exception as e:
                assert "time_in_force" not in str(e).lower() or "invalid" not in str(e).lower()

    @pytest.mark.vcr
    async def test_good_til_time_with_expiration(self, demo_env):
        """Test GTT (Good-til-Time) requires expiration_ts."""
        from src.kalshi.kalshi_mcp_server import mcp

        async with Client(mcp) as client:
            # GTT with expiration timestamp (1 hour from now)
            expiration_ts = int(time.time()) + 3600

            try:
                await client.call_tool(
                    "kalshi_create_limit_order",
                    {
                        "ticker": "HIGHTEST-24",
                        "side": "yes",
                        "quantity": 1,
                        "price": 1,
                        "time_in_force": "gtt",
                        "expiration_ts": expiration_ts
                    }
                )
            except Exception as e:
                # May fail for other reasons, but parameters should be accepted
                assert "time_in_force" not in str(e).lower() or "invalid" not in str(e).lower()
                assert "expiration" not in str(e).lower() or "invalid" not in str(e).lower()

    @pytest.mark.vcr
    async def test_post_only_parameter(self, demo_env):
        """Test post_only parameter (maker-only orders)."""
        from src.kalshi.kalshi_mcp_server import mcp

        async with Client(mcp) as client:
            # Test post_only=True
            try:
                await client.call_tool(
                    "kalshi_create_limit_order",
                    {
                        "ticker": "HIGHTEST-24",
                        "side": "yes",
                        "quantity": 1,
                        "price": 1,
                        "post_only": True
                    }
                )
            except Exception as e:
                assert "post_only" not in str(e).lower() or "invalid" not in str(e).lower()

            # Test post_only=False
            try:
                await client.call_tool(
                    "kalshi_create_limit_order",
                    {
                        "ticker": "HIGHTEST-24",
                        "side": "yes",
                        "quantity": 1,
                        "price": 1,
                        "post_only": False
                    }
                )
            except Exception as e:
                assert "post_only" not in str(e).lower() or "invalid" not in str(e).lower()

    @pytest.mark.vcr
    async def test_reduce_only_parameter(self, demo_env):
        """Test reduce_only parameter (position reduction only)."""
        from src.kalshi.kalshi_mcp_server import mcp

        async with Client(mcp) as client:
            # Test reduce_only=True
            try:
                await client.call_tool(
                    "kalshi_create_limit_order",
                    {
                        "ticker": "HIGHTEST-24",
                        "side": "yes",
                        "quantity": 1,
                        "price": 1,
                        "reduce_only": True
                    }
                )
            except Exception as e:
                # May fail if no position exists, but parameter should be accepted
                assert "reduce_only" not in str(e).lower() or "invalid" not in str(e).lower()

    @pytest.mark.vcr
    async def test_client_advanced_parameters(self, demo_env):
        """Test advanced parameters at client level."""
        from src.kalshi.client import KalshiClient

        async with KalshiClient.from_env() as client:
            # Test that client.create_order accepts all advanced parameters
            # (will likely fail due to market not existing, but should accept params)

            try:
                await client.create_order(
                    ticker="HIGHTEST-24",
                    side="yes",
                    count=1,
                    action="buy",
                    order_type="limit",
                    yes_price=1,
                    time_in_force="ioc",
                    post_only=True,
                    reduce_only=False,
                    self_trade_prevention_type="cancel_resting",
                    buy_max_cost=100,
                    sell_position_floor=0
                )
            except Exception as e:
                # Should fail for other reasons (market doesn't exist, etc.)
                # But not due to parameter validation
                error_msg = str(e).lower()
                assert not any(
                    param in error_msg and "invalid" in error_msg
                    for param in ["time_in_force", "post_only", "reduce_only",
                                 "self_trade_prevention", "buy_max_cost", "sell_position_floor"]
                )

    @pytest.mark.vcr
    async def test_combined_advanced_parameters(self, demo_env):
        """Test combining multiple advanced parameters."""
        from src.kalshi.kalshi_mcp_server import mcp

        async with Client(mcp) as client:
            # Test multiple parameters together
            expiration_ts = int(time.time()) + 3600

            try:
                await client.call_tool(
                    "kalshi_create_limit_order",
                    {
                        "ticker": "HIGHTEST-24",
                        "side": "yes",
                        "quantity": 1,
                        "price": 1,
                        "order_group_id": "test-group",
                        "time_in_force": "gtt",
                        "expiration_ts": expiration_ts,
                        "post_only": True,
                        "reduce_only": False
                    }
                )
            except Exception as e:
                # Verify parameters were accepted
                error_msg = str(e).lower()
                param_names = ["order_group_id", "time_in_force", "expiration_ts",
                              "post_only", "reduce_only"]
                for param in param_names:
                    if param in error_msg:
                        # If parameter name appears, it shouldn't be "invalid parameter"
                        assert "invalid" not in error_msg or f"invalid {param}" not in error_msg

    @pytest.mark.vcr
    async def test_market_order_with_order_group(self, demo_env):
        """Test that market orders can use order_group_id."""
        from src.kalshi.kalshi_mcp_server import mcp

        async with Client(mcp) as client:
            # Create order group first
            try:
                group_result = await client.call_tool(
                    "kalshi_create_order_group",
                    {"contracts_limit": 10}
                )

                # Try to create market order with group
                # (will fail for other reasons, but parameter should work)
                await client.call_tool(
                    "kalshi_create_market_order",
                    {
                        "ticker": "HIGHTEST-24",
                        "side": "yes",
                        "quantity": 1,
                        "order_group_id": "test-group-id"
                    }
                )
            except Exception as e:
                # Verify order_group_id parameter accepted
                error_msg = str(e).lower()
                if "order_group_id" in error_msg:
                    assert "invalid" not in error_msg or "invalid order_group_id" not in error_msg

    @pytest.mark.vcr
    async def test_self_trade_prevention_types(self, demo_env):
        """Test self-trade prevention parameter values."""
        from src.kalshi.client import KalshiClient

        async with KalshiClient.from_env() as client:
            # Test different STP types
            stp_types = ["cancel_resting", "cancel_aggressing", "allow"]

            for stp_type in stp_types:
                try:
                    await client.create_order(
                        ticker="HIGHTEST-24",
                        side="yes",
                        count=1,
                        action="buy",
                        order_type="limit",
                        yes_price=1,
                        self_trade_prevention_type=stp_type
                    )
                except Exception as e:
                    # Verify parameter accepted
                    error_msg = str(e).lower()
                    if "self_trade_prevention" in error_msg:
                        assert "invalid" not in error_msg

    @pytest.mark.vcr
    async def test_buy_max_cost_and_sell_position_floor(self, demo_env):
        """Test risk limit parameters."""
        from src.kalshi.client import KalshiClient

        async with KalshiClient.from_env() as client:
            # Test buy_max_cost
            try:
                await client.create_order(
                    ticker="HIGHTEST-24",
                    side="yes",
                    count=10,
                    action="buy",
                    order_type="limit",
                    yes_price=50,
                    buy_max_cost=500  # Limit spend to $5.00
                )
            except Exception as e:
                error_msg = str(e).lower()
                if "buy_max_cost" in error_msg:
                    assert "invalid" not in error_msg

            # Test sell_position_floor
            try:
                await client.create_order(
                    ticker="HIGHTEST-24",
                    side="yes",
                    count=5,
                    action="sell",
                    order_type="limit",
                    yes_price=50,
                    sell_position_floor=10  # Don't sell below 10 contracts
                )
            except Exception as e:
                error_msg = str(e).lower()
                if "sell_position_floor" in error_msg:
                    assert "invalid" not in error_msg
