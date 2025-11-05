"""End-to-end tests for complete order lifecycle.

These tests actually create, verify, and cancel orders on the demo API.
They test real success paths, not just validation failures.

IMPORTANT: These tests do NOT use VCR cassettes - they always make real API calls.
This ensures we test actual order workflows, not just replayed recordings.
"""

import pytest
from loguru import logger


# Disable VCR for all E2E tests - we want real API calls
pytestmark = [pytest.mark.asyncio, pytest.mark.disable_recording]


class TestOrderLifecycleE2E:
    """End-to-end tests for order creation, management, and cancellation."""

    async def test_limit_order_full_lifecycle(self, demo_env):
        """
        Test complete limit order lifecycle:
        1. Create limit order at unlikely price (won't fill)
        2. Verify it appears in active orders
        3. Cancel the order
        4. Verify it no longer appears in active orders
        """
        from src.kalshi.client import KalshiClient

        async with KalshiClient.from_env() as client:
            # Step 1: Find an open market to trade
            markets = await client.search_markets(limit=5, status="open")
            assert len(markets) > 0, "No open markets found in demo"

            ticker = markets[0].ticker
            logger.info(f"Testing with market: {ticker}")

            # Step 2: Create limit order with very low price (won't fill)
            order = await client.create_order(
                ticker=ticker,
                side="yes",
                count=1,
                action="buy",
                order_type="limit",
                yes_price=1,  # 1¢ - very unlikely to fill
            )

            # Verify order was created
            assert order.order_id is not None
            assert order.status == "resting"
            assert order.ticker == ticker
            assert order.side == "yes"
            assert order.yes_price == 1
            assert order.initial_count == 1
            assert order.remaining_count == 1

            logger.info(f"Created order: {order.order_id}")

            # Step 3: Verify order appears in active orders
            active_orders = await client.get_orders(ticker=ticker, status="resting")
            order_ids = [o.order_id for o in active_orders]
            assert order.order_id in order_ids, "Order not found in active orders"

            logger.info(f"Verified order appears in active orders ({len(active_orders)} total)")

            # Step 4: Cancel the order
            canceled_order = await client.cancel_order(order.order_id)
            assert canceled_order.order_id == order.order_id
            assert canceled_order.status == "canceled"
            assert canceled_order.remaining_count == 0

            logger.info(f"Canceled order: {order.order_id}")

            # Step 5: Verify order no longer in active orders
            active_orders_after = await client.get_orders(ticker=ticker, status="resting")
            active_order_ids_after = [o.order_id for o in active_orders_after]
            assert order.order_id not in active_order_ids_after, "Canceled order still appears in active orders"

            logger.info("Full lifecycle test passed")

    @pytest.mark.skip(reason="Amend endpoint returns 404 in demo API - possibly not supported or order fills immediately")
    async def test_amend_order_workflow(self, demo_env):
        """
        Test order amendment:
        1. Create limit order
        2. Amend price and quantity
        3. Verify changes
        4. Clean up
        """
        from src.kalshi.client import KalshiClient

        async with KalshiClient.from_env() as client:
            # Find an open market
            markets = await client.search_markets(limit=1, status="open")
            assert len(markets) > 0, "No open markets found"

            ticker = markets[0].ticker

            # Create order
            order = await client.create_order(
                ticker=ticker,
                side="yes",
                count=1,
                action="buy",
                order_type="limit",
                yes_price=1,
            )

            logger.info(f"Created order {order.order_id} with quantity=1, price=1")

            # Amend order (increase quantity and price)
            amended_order = await client.amend_order(
                order_id=order.order_id,
                new_count=2,
                new_price=2,
            )

            assert amended_order.order_id == order.order_id
            assert amended_order.initial_count == 2, f"Expected count=2, got {amended_order.initial_count}"
            assert amended_order.yes_price == 2, f"Expected price=2, got {amended_order.yes_price}"

            logger.info(f"Amended order to quantity=2, price=2")

            # Clean up
            await client.cancel_order(order.order_id)

            logger.info("Amend workflow test passed")

    async def test_decrease_order_workflow(self, demo_env):
        """
        Test order decrease:
        1. Create limit order with quantity=5
        2. Decrease by 3
        3. Verify remaining quantity is 2
        4. Clean up
        """
        from src.kalshi.client import KalshiClient

        async with KalshiClient.from_env() as client:
            # Find an open market
            markets = await client.search_markets(limit=1, status="open")
            assert len(markets) > 0, "No open markets found"

            ticker = markets[0].ticker

            # Create order with quantity=5
            order = await client.create_order(
                ticker=ticker,
                side="yes",
                count=5,
                action="buy",
                order_type="limit",
                yes_price=1,
            )

            logger.info(f"Created order {order.order_id} with quantity=5")

            # Decrease by 3
            decreased_order = await client.decrease_order(
                order_id=order.order_id,
                reduce_by=3,
            )

            assert decreased_order.order_id == order.order_id
            assert decreased_order.remaining_count == 2, f"Expected remaining=2, got {decreased_order.remaining_count}"

            logger.info(f"Decreased order to quantity=2")

            # Clean up
            await client.cancel_order(order.order_id)

            logger.info("Decrease workflow test passed")

    async def test_batch_order_cleanup(self, demo_env):
        """
        Test creating multiple orders and batch canceling them.
        1. Create 3 limit orders
        2. Verify all appear in active orders
        3. Cancel all
        4. Verify none remain active
        """
        from src.kalshi.client import KalshiClient

        async with KalshiClient.from_env() as client:
            # Find an open market
            markets = await client.search_markets(limit=1, status="open")
            assert len(markets) > 0, "No open markets found"

            ticker = markets[0].ticker

            # Create 3 orders
            order_ids = []
            for i in range(3):
                order = await client.create_order(
                    ticker=ticker,
                    side="yes",
                    count=1,
                    action="buy",
                    order_type="limit",
                    yes_price=1,
                )
                order_ids.append(order.order_id)
                logger.info(f"Created order {i+1}/3: {order.order_id}")

            # Verify all appear in active orders
            active_orders = await client.get_orders(ticker=ticker, status="resting")
            active_ids = [o.order_id for o in active_orders]

            for order_id in order_ids:
                assert order_id in active_ids, f"Order {order_id} not found in active orders"

            logger.info(f"Verified all {len(order_ids)} orders are active")

            # Cancel all orders
            for i, order_id in enumerate(order_ids):
                await client.cancel_order(order_id)
                logger.info(f"Canceled order {i+1}/3: {order_id}")

            # Verify none remain active
            active_orders_after = await client.get_orders(ticker=ticker, status="resting")
            active_ids_after = [o.order_id for o in active_orders_after]

            for order_id in order_ids:
                assert order_id not in active_ids_after, f"Order {order_id} still active after cancel"

            logger.info("Batch cleanup test passed")

    async def test_order_status_transitions(self, demo_env):
        """
        Test order status queries:
        1. Create order (resting)
        2. Verify appears in resting orders
        3. Cancel order
        4. Verify appears in canceled orders
        5. Verify does not appear in resting orders
        """
        from src.kalshi.client import KalshiClient

        async with KalshiClient.from_env() as client:
            # Find an open market
            markets = await client.search_markets(limit=1, status="open")
            assert len(markets) > 0, "No open markets found"

            ticker = markets[0].ticker

            # Create order
            order = await client.create_order(
                ticker=ticker,
                side="yes",
                count=1,
                action="buy",
                order_type="limit",
                yes_price=1,
            )

            # Verify in resting orders
            resting_orders = await client.get_orders(status="resting")
            resting_ids = [o.order_id for o in resting_orders]
            assert order.order_id in resting_ids, "New order not in resting orders"

            logger.info(f"Order {order.order_id} confirmed in resting status")

            # Cancel order
            await client.cancel_order(order.order_id)

            # Verify in canceled orders
            canceled_orders = await client.get_orders(status="canceled")
            canceled_ids = [o.order_id for o in canceled_orders]
            assert order.order_id in canceled_ids, "Canceled order not in canceled orders"

            # Verify NOT in resting orders
            resting_orders_after = await client.get_orders(status="resting")
            resting_ids_after = [o.order_id for o in resting_orders_after]
            assert order.order_id not in resting_ids_after, "Canceled order still in resting orders"

            logger.info("Status transitions test passed")
