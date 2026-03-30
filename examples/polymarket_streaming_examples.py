"""
Polymarket WebSocket Streaming Examples

Demonstrates common patterns for using the WebSocket client with MCP tools.
These examples show how LLM agents would combine discovery (MCP tools) with
real-time monitoring (WebSocket client).

Usage:
    # Run individual examples
    python examples/polymarket_streaming_examples.py --example price_alert
    python examples/polymarket_streaming_examples.py --example arbitrage
    python examples/polymarket_streaming_examples.py --example position_monitor

    # Run all examples
    python examples/polymarket_streaming_examples.py --all
"""

import asyncio
import argparse
from datetime import datetime
from loguru import logger

# These imports would be available when agent writes code
from polymarket.websocket_client import PolymarketWebSocketClient
from polymarket.websocket_models import PriceChangeEvent, OrderBookUpdate


# =============================================================================
# Example 1: Basic Price Monitoring
# =============================================================================

async def example_basic_price_monitoring(market_id: str, duration_seconds: int = 30):
    """
    Monitor real-time price updates for a single market.

    This is the simplest streaming pattern: connect, subscribe, stream events.

    Args:
        market_id: Market condition ID to monitor
        duration_seconds: How long to monitor (seconds)
    """
    logger.info("=" * 80)
    logger.info("Example 1: Basic Price Monitoring")
    logger.info("=" * 80)

    logger.info(f"Monitoring market {market_id} for {duration_seconds} seconds...")

    async with PolymarketWebSocketClient() as ws:
        await ws.subscribe_market(market_id)
        logger.success(f"✓ Subscribed to market {market_id}")

        # Track statistics
        price_updates = []
        start_time = asyncio.get_event_loop().time()

        async for event in ws:
            # Only process price change events
            if event.event_type == "price_change":
                price_updates.append({
                    "time": datetime.now(),
                    "price": event.price,
                    "asset_id": event.asset_id
                })

                logger.info(
                    f"Price: ${event.price:.3f} ({event.probability_pct:.1f}%) "
                    f"[{event.asset_id[:16]}...]"
                )

            # Stop after duration
            elapsed = asyncio.get_event_loop().time() - start_time
            if elapsed >= duration_seconds:
                break

        # Print summary
        if price_updates:
            prices = [u["price"] for u in price_updates]
            logger.info(f"\nSummary:")
            logger.info(f"  Updates received: {len(price_updates)}")
            logger.info(f"  Price range: ${min(prices):.3f} - ${max(prices):.3f}")
            logger.info(f"  Average price: ${sum(prices) / len(prices):.3f}")
        else:
            logger.warning("No price updates received")


# =============================================================================
# Example 2: Price Alert System
# =============================================================================

async def example_price_alert(market_id: str, threshold: float):
    """
    Monitor price and trigger alert when threshold crossed.

    Pattern: MCP (discovery) → WebSocket (monitoring) → MCP (action)

    Args:
        market_id: Market condition ID to monitor
        threshold: Price threshold to trigger alert
    """
    logger.info("=" * 80)
    logger.info("Example 2: Price Alert System")
    logger.info("=" * 80)

    # In real agent workflow, this would be:
    # market = await polymarket_get_market(market_id)
    # For demo, we'll simulate

    logger.info(f"Setting up price alert for market {market_id}")
    logger.info(f"Alert threshold: ${threshold:.2f}")

    async with PolymarketWebSocketClient() as ws:
        await ws.subscribe_market(market_id)

        async for event in ws:
            if isinstance(event, PriceChangeEvent):
                logger.info(f"Current price: ${event.price:.3f}")

                if event.price >= threshold:
                    logger.success(f"🚨 ALERT: Price crossed ${threshold:.2f}!")
                    logger.success(f"   Current price: ${event.price:.3f}")

                    # In real agent workflow, would execute action via MCP:
                    # order = await polymarket_create_order(...)
                    logger.info("   → Would execute order via MCP tool here")

                    break


# =============================================================================
# Example 3: Multi-Market Arbitrage Detection
# =============================================================================

async def example_arbitrage_detection(
    market_ids: list[str],
    check_interval: float = 1.0,
    duration: int = 60
):
    """
    Monitor multiple markets for arbitrage opportunities.

    Pattern: MCP (discovery) → WebSocket (multi-market monitoring) → MCP (batch execution)

    Args:
        market_ids: List of related market IDs to monitor
        check_interval: How often to check for arbitrage (seconds)
        duration: How long to run (seconds)
    """
    logger.info("=" * 80)
    logger.info("Example 3: Multi-Market Arbitrage Detection")
    logger.info("=" * 80)

    logger.info(f"Monitoring {len(market_ids)} markets for arbitrage...")

    async with PolymarketWebSocketClient() as ws:
        # Subscribe to all markets
        for market_id in market_ids:
            await ws.subscribe_market(market_id)
            logger.info(f"  ✓ Subscribed to {market_id[:16]}...")

        # Track latest price for each market
        prices = {}
        last_check = 0
        start_time = asyncio.get_event_loop().time()

        async for event in ws:
            if isinstance(event, PriceChangeEvent):
                # Update price cache
                prices[event.market] = event.price

                # Check for arbitrage periodically
                current_time = asyncio.get_event_loop().time()
                if current_time - last_check >= check_interval and len(prices) >= 2:
                    last_check = current_time

                    # Calculate total probability
                    total_prob = sum(prices.values())

                    logger.info(f"\nArbitrage check:")
                    for market_id, price in prices.items():
                        logger.info(f"  {market_id[:16]}...: ${price:.3f}")
                    logger.info(f"  Total: ${total_prob:.3f}")

                    # Check for arbitrage
                    if total_prob < 0.98:
                        profit_pct = (1.0 - total_prob) / total_prob * 100
                        logger.success(f"  🎯 ARBITRAGE FOUND: {profit_pct:.2f}% profit!")
                        logger.success(f"     Buy all outcomes for ${total_prob:.3f}")
                        logger.success(f"     Guaranteed payout: $1.00")
                        logger.success(f"     Profit: ${1.0 - total_prob:.3f}")

                        # In real workflow:
                        # orders = [build order for each market]
                        # result = await polymarket_create_orders_batch(orders)
                        logger.info("     → Would execute batch order via MCP tool")
                        break

                    elif total_prob > 1.02:
                        profit_pct = (total_prob - 1.0) / total_prob * 100
                        logger.success(f"  🎯 ARBITRAGE FOUND: {profit_pct:.2f}% profit!")
                        logger.success(f"     Sell all outcomes for ${total_prob:.3f}")
                        logger.success(f"     Payout: $1.00")
                        logger.success(f"     Profit: ${total_prob - 1.0:.3f}")
                        logger.info("     → Would execute batch order via MCP tool")
                        break

            # Stop after duration
            if asyncio.get_event_loop().time() - start_time >= duration:
                logger.info(f"\nMonitored for {duration}s - no arbitrage found")
                break


# =============================================================================
# Example 4: Position Monitoring with Auto-Exit
# =============================================================================

async def example_position_monitoring(
    market_id: str,
    entry_price: float,
    position_size: float,
    profit_target: float
):
    """
    Monitor position P&L and auto-exit at profit target.

    Pattern: MCP (check position) → WebSocket (monitor) → MCP (close)

    Args:
        market_id: Market condition ID
        entry_price: Position entry price
        position_size: Number of shares
        profit_target: Dollar profit target to exit
    """
    logger.info("=" * 80)
    logger.info("Example 4: Position Monitoring with Auto-Exit")
    logger.info("=" * 80)

    # In real workflow:
    # positions = await polymarket_get_positions()
    # position = positions[0]

    cost_basis = entry_price * position_size

    logger.info(f"Monitoring position:")
    logger.info(f"  Entry price: ${entry_price:.3f}")
    logger.info(f"  Position size: {position_size} shares")
    logger.info(f"  Cost basis: ${cost_basis:.2f}")
    logger.info(f"  Profit target: ${profit_target:.2f}")

    async with PolymarketWebSocketClient() as ws:
        await ws.subscribe_market(market_id)

        async for event in ws:
            if isinstance(event, PriceChangeEvent):
                # Calculate current P&L
                current_value = event.price * position_size
                unrealized_pnl = current_value - cost_basis

                logger.info(
                    f"Price: ${event.price:.3f} | "
                    f"Value: ${current_value:.2f} | "
                    f"P&L: ${unrealized_pnl:+.2f}"
                )

                # Check if profit target hit
                if unrealized_pnl >= profit_target:
                    logger.success(f"🎯 Profit target reached: ${unrealized_pnl:.2f}")
                    logger.success(f"   Exit price: ${event.price:.3f}")

                    # In real workflow:
                    # result = await polymarket_close_position(market_id)
                    logger.info("   → Would close position via MCP tool")
                    break


# =============================================================================
# Example 5: Order Book Analysis
# =============================================================================

async def example_orderbook_analysis(market_id: str, target_size: float):
    """
    Monitor order book depth for optimal execution.

    Pattern: WebSocket (monitor liquidity) → MCP (execute when ready)

    Args:
        market_id: Market condition ID
        target_size: Target order size
    """
    logger.info("=" * 80)
    logger.info("Example 5: Order Book Analysis")
    logger.info("=" * 80)

    logger.info(f"Monitoring order book for execution opportunity...")
    logger.info(f"Target size: {target_size} shares")

    async with PolymarketWebSocketClient() as ws:
        await ws.subscribe_market(market_id)

        async for event in ws:
            if isinstance(event, OrderBookUpdate):
                # Analyze order book depth
                if event.asks:
                    # Calculate available liquidity
                    total_liquidity = sum(level.size for level in event.asks[:5])
                    weighted_price = sum(
                        level.price * level.size for level in event.asks[:5]
                    ) / total_liquidity if total_liquidity > 0 else 0

                    logger.info(f"\nOrder Book Analysis:")
                    logger.info(f"  Best ask: ${event.best_ask.price:.3f}")
                    logger.info(f"  Spread: ${event.spread:.3f}")
                    logger.info(f"  Top 5 levels liquidity: {total_liquidity:.0f} shares")
                    logger.info(f"  Weighted avg price: ${weighted_price:.3f}")

                    # Check if enough liquidity available
                    if total_liquidity >= target_size:
                        logger.success(f"  ✓ Sufficient liquidity for {target_size} shares")
                        logger.success(f"  Estimated execution: ${weighted_price:.3f}")

                        # In real workflow:
                        # order = await polymarket_create_order(
                        #     token_id=...,
                        #     side="BUY",
                        #     price=weighted_price + 0.005,  # Slightly better
                        #     size=target_size
                        # )
                        logger.info("  → Would execute order via MCP tool")
                        break
                    else:
                        logger.warning(
                            f"  ⚠️ Insufficient liquidity "
                            f"({total_liquidity:.0f} < {target_size})"
                        )


# =============================================================================
# Example 6: Multi-Event Stream Processing
# =============================================================================

async def example_multi_event_processing(market_id: str, duration: int = 30):
    """
    Process multiple event types from a single stream.

    Shows how to handle different event types in one stream.

    Args:
        market_id: Market condition ID
        duration: How long to run (seconds)
    """
    logger.info("=" * 80)
    logger.info("Example 6: Multi-Event Stream Processing")
    logger.info("=" * 80)

    logger.info(f"Processing all event types from market {market_id}...")

    # Track statistics
    event_counts = {}
    start_time = asyncio.get_event_loop().time()

    async with PolymarketWebSocketClient() as ws:
        await ws.subscribe_market(market_id)

        async for event in ws:
            # Track event type
            event_type = event.event_type
            event_counts[event_type] = event_counts.get(event_type, 0) + 1

            # Process based on type
            if isinstance(event, PriceChangeEvent):
                logger.info(f"💰 Price: ${event.price:.3f}")

            elif isinstance(event, OrderBookUpdate):
                if event.best_bid and event.best_ask:
                    logger.info(
                        f"📊 Book: Bid ${event.best_bid.price:.3f} / "
                        f"Ask ${event.best_ask.price:.3f} "
                        f"(Spread: ${event.spread:.3f})"
                    )

            # Stop after duration
            if asyncio.get_event_loop().time() - start_time >= duration:
                break

        # Print summary
        logger.info(f"\nEvent Summary ({duration}s):")
        for event_type, count in sorted(event_counts.items()):
            logger.info(f"  {event_type}: {count} events")


# =============================================================================
# Main Example Runner
# =============================================================================

async def main():
    """Run examples based on command line arguments."""
    parser = argparse.ArgumentParser(description="Polymarket WebSocket Examples")
    parser.add_argument(
        "--example",
        choices=[
            "price_monitor",
            "price_alert",
            "arbitrage",
            "position_monitor",
            "orderbook",
            "multi_event"
        ],
        help="Which example to run"
    )
    parser.add_argument("--all", action="store_true", help="Run all examples")
    parser.add_argument("--market-id", default="0x...", help="Market ID to use")
    args = parser.parse_args()

    # Use demo market ID if not provided
    market_id = args.market_id
    if market_id == "0x...":
        logger.warning(
            "No market ID provided. "
            "Use --market-id <condition_id> with a real market."
        )
        logger.info("Examples will use placeholder ID (won't actually run)")
        return

    # Run examples
    if args.all or args.example == "price_monitor":
        await example_basic_price_monitoring(market_id, duration_seconds=15)

    if args.all or args.example == "price_alert":
        await example_price_alert(market_id, threshold=0.60)

    if args.all or args.example == "arbitrage":
        # For arbitrage, need multiple related markets
        # In practice, agent would discover these via MCP tools
        market_ids = [market_id]  # Add more market IDs for real arbitrage
        await example_arbitrage_detection(market_ids, duration=30)

    if args.all or args.example == "position_monitor":
        await example_position_monitoring(
            market_id,
            entry_price=0.45,
            position_size=100,
            profit_target=10.0
        )

    if args.all or args.example == "orderbook":
        await example_orderbook_analysis(market_id, target_size=1000)

    if args.all or args.example == "multi_event":
        await example_multi_event_processing(market_id, duration=30)


if __name__ == "__main__":
    # Configure logging
    logger.remove()  # Remove default handler
    logger.add(
        lambda msg: print(msg, end=""),
        format="<green>{time:HH:mm:ss}</green> | <level>{message}</level>",
        level="INFO"
    )

    asyncio.run(main())
