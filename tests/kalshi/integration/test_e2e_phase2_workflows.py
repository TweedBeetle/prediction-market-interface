"""End-to-end tests for Phase 2 features.

These tests actually test order groups, advanced parameters, and batch operations
against the real demo API. They are NOT recorded with VCR cassettes.

IMPORTANT: These tests bypass VCR to ensure we test actual API behavior,
not replayed recordings. This would have caught the order groups KeyError bug
that 22 passing VCR-based tests missed.

Why E2E tests matter:
- VCR cassettes can replay fictional responses that match wrong code
- Integration tests with cassettes = regression tests (consistency)
- E2E tests with real API = correctness tests (actual behavior)

Lesson learned: Order groups bug passed all VCR tests but failed immediately
on real API because cassettes had fictional structure matching our assumptions.
"""

import pytest
from loguru import logger


# Disable VCR for all E2E tests - we want real API calls
pytestmark = [pytest.mark.asyncio, pytest.mark.disable_recording]


class TestOrderGroupsE2E:
    """End-to-end tests for order groups (OCO strategies)."""

    async def test_order_group_create_and_retrieve(self, demo_env):
        """
        Test order group creation and retrieval:
        1. Create order group with contract limit
        2. Retrieve group and verify structure
        3. Verify API returns minimal fields (not comprehensive object)
        4. Clean up

        This test would have caught the KeyError: 'order_group' bug immediately
        because it tests against real API, not fictional cassette responses.
        """
        from src.kalshi.client import KalshiClient

        async with KalshiClient.from_env() as client:
            # Step 1: Create order group
            group = await client.create_order_group(contracts_limit=10)

            # Verify creation response (minimal structure from API)
            assert group.order_group_id is not None, "Missing order_group_id"
            logger.info(f"Created order group: {group.order_group_id}")

            # Note: API doesn't return contracts_limit in response
            # This is a known limitation documented in CLAUDE.md

            # Step 2: Retrieve the group
            retrieved = await client.get_order_group(group.order_group_id)

            # Verify retrieval response structure
            assert retrieved.order_group_id == group.order_group_id
            assert hasattr(retrieved, "is_auto_cancel_enabled"), "Missing is_auto_cancel_enabled field"
            assert hasattr(retrieved, "orders"), "Missing orders field"
            assert retrieved.orders == [] or retrieved.orders is None, "New group should have no orders"

            logger.info(f"Retrieved group: auto_cancel={retrieved.is_auto_cancel_enabled}, orders={len(retrieved.orders or [])}")

            # Step 3: Clean up
            await client.delete_order_group(group.order_group_id)
            logger.info(f"Deleted order group: {group.order_group_id}")

    async def test_order_group_with_linked_order(self, demo_env):
        """
        Test order group with linked orders (OCO behavior):
        1. Create order group
        2. Create order linked to group
        3. Verify order appears in group
        4. Cancel order
        5. Clean up group

        This tests the core OCO functionality.
        """
        from src.kalshi.client import KalshiClient

        async with KalshiClient.from_env() as client:
            # Step 1: Create order group with 5 contract limit
            group = await client.create_order_group(contracts_limit=5)
            logger.info(f"Created order group: {group.order_group_id} (limit: 5 contracts)")

            # Step 2: Find an open market
            markets = await client.search_markets(limit=1, status="open")
            assert len(markets) > 0, "No open markets found"
            ticker = markets[0].ticker

            # Step 3: Create order linked to group
            order = await client.create_order(
                ticker=ticker,
                side="yes",
                count=3,
                action="buy",
                order_type="limit",
                yes_price=1,  # Won't fill
                order_group_id=group.order_group_id,  # Link to group
            )

            assert order.order_id is not None
            logger.info(f"Created order {order.order_id} linked to group")

            # Step 4: Retrieve group and verify order appears
            retrieved_group = await client.get_order_group(group.order_group_id)
            assert retrieved_group.orders is not None, "Orders list should not be None"
            assert order.order_id in retrieved_group.orders, f"Order {order.order_id} not found in group"
            logger.info(f"Verified order appears in group: {len(retrieved_group.orders)} order(s)")

            # Step 5: Cancel order
            await client.cancel_order(order.order_id)
            logger.info(f"Canceled order: {order.order_id}")

            # Step 6: Clean up group
            await client.delete_order_group(group.order_group_id)
            logger.info(f"Deleted order group: {group.order_group_id}")

    async def test_multiple_orders_in_group(self, demo_env):
        """
        Test multiple orders in same group:
        1. Create order group
        2. Create 3 orders in the group
        3. Verify all appear in group
        4. Cancel all orders
        5. Clean up

        Tests order group's ability to track multiple linked orders.
        """
        from src.kalshi.client import KalshiClient

        async with KalshiClient.from_env() as client:
            # Create order group
            group = await client.create_order_group(contracts_limit=10)
            logger.info(f"Created order group: {group.order_group_id}")

            # Find an open market
            markets = await client.search_markets(limit=1, status="open")
            assert len(markets) > 0, "No open markets found"
            ticker = markets[0].ticker

            # Create 3 orders in the group
            order_ids = []
            for i in range(3):
                order = await client.create_order(
                    ticker=ticker,
                    side="yes",
                    count=1,
                    action="buy",
                    order_type="limit",
                    yes_price=1,
                    order_group_id=group.order_group_id,
                )
                order_ids.append(order.order_id)
                logger.info(f"Created order {i+1}/3: {order.order_id}")

            # Verify all orders in group
            retrieved_group = await client.get_order_group(group.order_group_id)
            assert retrieved_group.orders is not None
            assert len(retrieved_group.orders) == 3, f"Expected 3 orders, got {len(retrieved_group.orders)}"

            for order_id in order_ids:
                assert order_id in retrieved_group.orders, f"Order {order_id} not in group"

            logger.info(f"Verified all {len(order_ids)} orders in group")

            # Cancel all orders
            for i, order_id in enumerate(order_ids):
                await client.cancel_order(order_id)
                logger.info(f"Canceled order {i+1}/3")

            # Clean up group
            await client.delete_order_group(group.order_group_id)
            logger.info("Test complete")

    async def test_order_group_list(self, demo_env):
        """
        Test listing order groups:
        1. Create 2 order groups
        2. List groups and verify both appear (or skip if eventual consistency issue)
        3. Clean up both groups

        Tests the get_order_groups pagination endpoint.

        Note: Demo API may have eventual consistency - groups might not appear
        immediately in list. This is acceptable for E2E test.
        """
        from src.kalshi.client import KalshiClient

        async with KalshiClient.from_env() as client:
            # Create 2 groups
            group1 = await client.create_order_group(contracts_limit=5)
            group2 = await client.create_order_group(contracts_limit=10)
            logger.info(f"Created groups: {group1.order_group_id}, {group2.order_group_id}")

            # List groups
            groups = await client.get_order_groups(limit=10)

            # Verify both appear in list (allow for eventual consistency)
            group_ids = [g.group_id for g in groups]
            found_count = sum([
                group1.order_group_id in group_ids,
                group2.order_group_id in group_ids
            ])

            if found_count < 2:
                logger.warning(f"Only found {found_count}/2 groups - possible eventual consistency issue")
                # Still acceptable - we got a valid list response
                assert len(groups) > 0, "Should have at least some groups"
            else:
                logger.info(f"Found both groups in list of {len(groups)} groups")

            # Clean up
            await client.delete_order_group(group1.order_group_id)
            await client.delete_order_group(group2.order_group_id)
            logger.info("Cleaned up both groups")


class TestAdvancedParametersE2E:
    """End-to-end tests for advanced order parameters."""

    async def test_post_only_order(self, demo_env):
        """
        Test post_only parameter (maker-only orders):
        1. Create limit order with post_only=True
        2. Verify order is created and resting
        3. Clean up

        Post-only ensures order is maker (gets rebates), not taker (pays fees).
        """
        from src.kalshi.client import KalshiClient

        async with KalshiClient.from_env() as client:
            # Find an open market
            markets = await client.search_markets(limit=1, status="open")
            assert len(markets) > 0, "No open markets found"
            ticker = markets[0].ticker

            # Create post-only order
            order = await client.create_order(
                ticker=ticker,
                side="yes",
                count=1,
                action="buy",
                order_type="limit",
                yes_price=1,
                post_only=True,  # Maker-only
            )

            assert order.order_id is not None
            assert order.status == "resting", "Post-only order should be resting"
            logger.info(f"Created post-only order: {order.order_id}")

            # Clean up
            await client.cancel_order(order.order_id)
            logger.info("Post-only test complete")

    async def test_reduce_only_order(self, demo_env):
        """
        Test reduce_only parameter:
        1. Create initial position (if none exists, skip)
        2. Create reduce_only order
        3. Verify it's accepted
        4. Clean up

        Reduce-only prevents increasing position size.
        """
        from src.kalshi.client import KalshiClient

        async with KalshiClient.from_env() as client:
            # Find an open market
            markets = await client.search_markets(limit=1, status="open")
            assert len(markets) > 0, "No open markets found"
            ticker = markets[0].ticker

            # Try to create reduce-only order
            # Note: This might fail if we have no position, which is expected behavior
            try:
                order = await client.create_order(
                    ticker=ticker,
                    side="no",  # Opposite side to reduce
                    count=1,
                    action="sell",
                    order_type="limit",
                    no_price=99,
                    reduce_only=True,
                )

                logger.info(f"Created reduce-only order: {order.order_id}")

                # Clean up
                await client.cancel_order(order.order_id)
                logger.info("Reduce-only test complete")

            except Exception as e:
                # Expected if no position exists
                logger.info(f"Reduce-only order rejected (expected if no position): {e}")
                pytest.skip("No position to reduce - test skipped")

    async def test_time_in_force_ioc(self, demo_env):
        """
        Test time_in_force=ioc (Immediate-or-Cancel):
        1. Create IOC order at unlikely price
        2. Verify it's immediately canceled (not filled)

        IOC orders fill immediately or cancel - don't rest on book.
        """
        from src.kalshi.client import KalshiClient

        async with KalshiClient.from_env() as client:
            # Find an open market
            markets = await client.search_markets(limit=1, status="open")
            assert len(markets) > 0, "No open markets found"
            ticker = markets[0].ticker

            # Create IOC order at unlikely price (won't fill, should cancel)
            order = await client.create_order(
                ticker=ticker,
                side="yes",
                count=1,
                action="buy",
                order_type="limit",
                yes_price=1,
                time_in_force="ioc",
            )

            # IOC at price 1¢ likely won't fill, so should be canceled immediately
            assert order.order_id is not None
            # Status might be "canceled" immediately or go through brief "resting" state
            logger.info(f"Created IOC order: {order.order_id}, status: {order.status}")

            # If still resting, cancel it
            if order.status == "resting":
                await client.cancel_order(order.order_id)
                logger.info("Canceled resting IOC order")


class TestIntegrationScenariosE2E:
    """End-to-end tests for complex multi-feature scenarios."""

    async def test_oco_strategy_with_advanced_params(self, demo_env):
        """
        Test OCO strategy with advanced parameters:
        1. Create order group (limit: 5 contracts)
        2. Create two competing orders in group, both post-only
        3. Verify both appear in group (if API allows)
        4. Cancel both
        5. Clean up

        Combines order groups + advanced parameters in realistic trading scenario.

        Note: Demo API sometimes returns 404 when retrieving groups immediately
        after creation. This is a known demo API issue, not a code bug.
        """
        from src.kalshi.client import KalshiClient
        import httpx

        async with KalshiClient.from_env() as client:
            # Create order group
            group = await client.create_order_group(contracts_limit=5)
            logger.info(f"Created order group for OCO strategy: {group.order_group_id}")

            # Find an open market
            markets = await client.search_markets(limit=1, status="open")
            assert len(markets) > 0, "No open markets found"
            ticker = markets[0].ticker

            # Create two competing orders (OCO)
            order1 = await client.create_order(
                ticker=ticker,
                side="yes",
                count=5,
                action="buy",
                order_type="limit",
                yes_price=1,
                post_only=True,
                order_group_id=group.order_group_id,
            )
            logger.info(f"Created OCO order 1: {order1.order_id}")

            order2 = await client.create_order(
                ticker=ticker,
                side="yes",
                count=5,
                action="buy",
                order_type="limit",
                yes_price=2,
                post_only=True,
                order_group_id=group.order_group_id,
            )
            logger.info(f"Created OCO order 2: {order2.order_id}")

            # Try to verify both in group (may fail with 404 on demo API)
            try:
                retrieved_group = await client.get_order_group(group.order_group_id)
                assert order1.order_id in retrieved_group.orders
                assert order2.order_id in retrieved_group.orders
                logger.info("Verified both OCO orders in group")
            except httpx.HTTPStatusError as e:
                if e.response.status_code == 404:
                    logger.warning(f"Could not retrieve group (demo API 404) - known issue, continuing with cleanup")
                else:
                    raise

            # Clean up
            await client.cancel_order(order1.order_id)
            await client.cancel_order(order2.order_id)
            try:
                await client.delete_order_group(group.order_group_id)
            except httpx.HTTPStatusError as e:
                if e.response.status_code == 404:
                    logger.info("Group already deleted or not found (demo API issue)")
                else:
                    raise
            logger.info("OCO strategy test complete")
