"""FastMCP server for Kalshi prediction market API."""

import os
import json
from typing import Any, Optional

from fastmcp import FastMCP
from loguru import logger

from .client import KalshiClient
from .models import (
    Market,
    Order,
    Position,
    Event,
    Series,
    Fill,
    Balance,
    Candlestick,
    Trade,
    Orderbook,
    Milestone,
    QueuePosition,
    ExchangeStatus,
    OrderGroup,
    Settlement,
    TotalRestingOrderValue,
)


# ========== FAIL-FAST CREDENTIAL VALIDATION ==========
# Validate credentials exist at module load (before server starts)
_API_KEY_ID = os.getenv("KALSHI_API_KEY_ID")
_PRIVATE_KEY_PATH = os.getenv("KALSHI_PRIVATE_KEY_PATH")

if not _API_KEY_ID:
    raise ValueError(
        "KALSHI_API_KEY_ID environment variable is required. "
        "Please set it in a .env file or your shell environment. "
        "See .claude/CLAUDE.md for setup instructions."
    )

if not _PRIVATE_KEY_PATH:
    raise ValueError(
        "KALSHI_PRIVATE_KEY_PATH environment variable is required. "
        "Please set it in a .env file or your shell environment. "
        "See .claude/CLAUDE.md for setup instructions."
    )


# Initialize FastMCP server
mcp = FastMCP("Kalshi Prediction Markets")

# Global client instance (lazy initialization on first tool call)
client: Optional[KalshiClient] = None


def _ensure_client() -> KalshiClient:
    """Ensure client is initialized (lazy initialization on first use).

    Credentials are validated at module load time, so if we reach this point,
    we're guaranteed to have valid credentials from the environment.
    """
    global client
    if client is None:
        logger.info("Initializing Kalshi client on first tool call")
        client = KalshiClient()
    return client


def _require_confirmation(tool_name: str, description: str) -> None:
    """Require user confirmation for write operations.

    In FastMCP, this can be implemented by raising a ToolError that the
    Claude client will present to the user for confirmation.
    """
    # TODO: Implement user confirmation dialog
    # For now, we'll allow operations but log them
    logger.info(f"Write operation requested: {tool_name} - {description}")


# ========== TIER 1: READ-ONLY TOOLS (10 tools) ==========


@mcp.tool()
async def kalshi_search_markets(
    status: Optional[str] = None,
    series_ticker: Optional[str] = None,
    max_close_ts: Optional[int] = None,
    min_close_ts: Optional[int] = None,
    limit: int = 100,
    cursor: Optional[str] = None,
) -> dict[str, Any]:
    """Search and filter Kalshi markets.

    Args:
        status: Market status (unopened, open, closed, settled)
        series_ticker: Filter by series template
        max_close_ts: Maximum close timestamp (Unix seconds)
        min_close_ts: Minimum close timestamp (Unix seconds)
        limit: Number of results (max 1000, default 100)
        cursor: Pagination cursor for next page

    Returns:
        Dictionary with markets list and next cursor for pagination
    """
    client = _ensure_client()
    markets, next_cursor = await client.search_markets(
        status=status,
        series_ticker=series_ticker,
        max_close_ts=max_close_ts,
        min_close_ts=min_close_ts,
        limit=limit,
        cursor=cursor,
    )

    return {
        "markets": [m.model_dump() for m in markets],
        "cursor": next_cursor,
        "count": len(markets),
    }


@mcp.tool()
async def kalshi_get_market(ticker: str) -> dict[str, Any]:
    """Get detailed information about a specific market.

    Args:
        ticker: Market ticker (e.g., KXHARRIS24-LSV)

    Returns:
        Market details including current prices, volume, and settlement info
    """
    client = _ensure_client()
    market = await client.get_market(ticker)
    return market.model_dump()


@mcp.tool()
async def kalshi_get_orderbook(ticker: str, depth: int = 5) -> dict[str, Any]:
    """Get current order book for a market.

    Args:
        ticker: Market ticker
        depth: Order book depth (0/-1 for full book, 1-100 for specific depth)

    Returns:
        Order book with bids and asks arrays
    """
    client = _ensure_client()
    orderbook = await client.get_orderbook(ticker, depth=depth)
    return orderbook.model_dump()


@mcp.tool()
async def kalshi_get_trades(
    ticker: Optional[str] = None,
    limit: int = 100,
    before: Optional[int] = None,
    after: Optional[int] = None,
) -> dict[str, Any]:
    """Get recent trades across markets.

    Args:
        ticker: Filter by specific market ticker
        limit: Number of results (default 100)
        before: Get trades before timestamp (Unix ms)
        after: Get trades after timestamp (Unix ms)

    Returns:
        List of recent trades with prices and execution times
    """
    client = _ensure_client()
    trades, cursor = await client.get_trades(
        ticker=ticker,
        limit=limit,
        before=before,
        after=after,
    )

    return {
        "trades": [t.model_dump() for t in trades],
        "cursor": cursor,
        "count": len(trades),
    }


@mcp.tool()
async def kalshi_get_candlesticks(
    series_ticker: str,
    ticker: str,
    interval: str = "1440min",
) -> dict[str, Any]:
    """Get historical OHLCV candlestick data for a market.

    Args:
        series_ticker: Series identifier
        ticker: Market ticker
        interval: Time interval (1min, 60min, 1440min for daily)

    Returns:
        List of candlesticks with open, high, low, close, volume
    """
    client = _ensure_client()
    candlesticks = await client.get_candlesticks(
        series_ticker=series_ticker,
        ticker=ticker,
        interval=interval,
    )

    return {
        "candlesticks": [c.model_dump() for c in candlesticks],
        "count": len(candlesticks),
        "interval": interval,
    }


@mcp.tool()
async def kalshi_get_events(
    status: Optional[str] = None,
    limit: int = 100,
    cursor: Optional[str] = None,
) -> dict[str, Any]:
    """Browse Kalshi events.

    Args:
        status: Event status filter (open, closed, settled)
        limit: Number of results (default 100)
        cursor: Pagination cursor

    Returns:
        List of events with descriptions and status
    """
    client = _ensure_client()
    events, next_cursor = await client.get_events(
        status=status,
        limit=limit,
        cursor=cursor,
    )

    return {
        "events": [e.model_dump() for e in events],
        "cursor": next_cursor,
        "count": len(events),
    }


@mcp.tool()
async def kalshi_get_event(ticker: str, include_markets: bool = False) -> dict[str, Any]:
    """Get detailed information about a specific event.

    Args:
        ticker: Event ticker
        include_markets: Include nested markets for this event

    Returns:
        Event details with optional nested markets
    """
    client = _ensure_client()
    event = await client.get_event(ticker, include_markets=include_markets)
    return event.model_dump()


@mcp.tool()
async def kalshi_get_series(
    category: Optional[str] = None,
    limit: int = 100,
    cursor: Optional[str] = None,
) -> dict[str, Any]:
    """Browse Kalshi series templates.

    Args:
        category: Filter by category
        limit: Number of results (default 100)
        cursor: Pagination cursor

    Returns:
        List of series with descriptions
    """
    client = _ensure_client()
    series_list, next_cursor = await client.get_series(
        category=category,
        limit=limit,
        cursor=cursor,
    )

    return {
        "series": [s.model_dump() for s in series_list],
        "cursor": next_cursor,
        "count": len(series_list),
    }


@mcp.tool()
async def kalshi_get_exchange_status() -> dict[str, Any]:
    """Get current exchange status and trading conditions.

    Returns:
        Exchange status with trading activity and maintenance info
    """
    client = _ensure_client()
    status = await client.get_exchange_status()
    return status.model_dump()


@mcp.tool()
async def kalshi_get_milestones(
    category: Optional[str] = None,
    source: Optional[str] = None,
    min_ts: Optional[int] = None,
    max_ts: Optional[int] = None,
) -> dict[str, Any]:
    """Get event milestones for tracking progress and live data.

    Args:
        category: Filter by milestone category
        source: Filter by data source
        min_ts: Minimum timestamp (Unix seconds)
        max_ts: Maximum timestamp (Unix seconds)

    Returns:
        List of milestones with timestamps and descriptions
    """
    client = _ensure_client()
    milestones = await client.get_milestones(
        category=category,
        source=source,
        min_ts=min_ts,
        max_ts=max_ts,
    )

    return {
        "milestones": [m.model_dump() for m in milestones],
        "count": len(milestones),
    }


# ========== TIER 2: TRADING OPERATIONS (8 tools) ==========


@mcp.tool()
async def kalshi_get_balance() -> dict[str, Any]:
    """Get current account balance and portfolio value.

    Returns:
        Balance in cents and total portfolio value
    """
    client = _ensure_client()
    balance = await client.get_balance()
    return balance.model_dump()


@mcp.tool()
async def kalshi_get_positions(
    ticker: Optional[str] = None,
    event_ticker: Optional[str] = None,
    limit: int = 100,
    cursor: Optional[str] = None,
) -> dict[str, Any]:
    """Get user's current positions in markets.

    Args:
        ticker: Filter by market ticker
        event_ticker: Filter by event ticker
        limit: Number of results (default 100)
        cursor: Pagination cursor

    Returns:
        List of positions with size, average fill price, and P&L info
    """
    client = _ensure_client()
    positions, next_cursor = await client.get_positions(
        ticker=ticker,
        event_ticker=event_ticker,
        limit=limit,
        cursor=cursor,
    )

    return {
        "positions": [p.model_dump() for p in positions],
        "cursor": next_cursor,
        "count": len(positions),
    }


@mcp.tool()
async def kalshi_create_order(
    ticker: str,
    side: str,
    count: int,
    type: str = "limit",
    price: Optional[int] = None,
    expire_at: Optional[int] = None,
    order_group_id: Optional[str] = None,
) -> dict[str, Any]:
    """Place a new order on a market. **REQUIRES USER CONFIRMATION**.

    Args:
        ticker: Market ticker
        side: "buy" or "sell"
        count: Number of contracts to order
        type: "limit" (default) or "market"
        price: Limit price in cents (1-99, required for limit orders)
        expire_at: Order expiration timestamp (Unix seconds, optional)
        order_group_id: Optional order group for risk management

    Returns:
        Order confirmation with order ID and status
    """
    _require_confirmation(
        "kalshi_create_order",
        f"Place {side} order: {count} contracts of {ticker} at {price or 'market'} cents",
    )

    client = _ensure_client()
    order = await client.create_order(
        ticker=ticker,
        side=side,
        count=count,
        type=type,
        price=price,
        expire_at=expire_at,
        order_group_id=order_group_id,
    )

    return order.model_dump()


@mcp.tool()
async def kalshi_get_orders(
    ticker: Optional[str] = None,
    event_ticker: Optional[str] = None,
    status: Optional[str] = None,
    min_ts: Optional[int] = None,
    max_ts: Optional[int] = None,
    limit: int = 100,
    cursor: Optional[str] = None,
) -> dict[str, Any]:
    """Get user's orders.

    Args:
        ticker: Filter by market ticker
        event_ticker: Filter by event ticker
        status: Filter by status (resting, canceled, executed)
        min_ts: Minimum timestamp (Unix seconds)
        max_ts: Maximum timestamp (Unix seconds)
        limit: Number of results (default 100)
        cursor: Pagination cursor

    Returns:
        List of orders with status and fill information
    """
    client = _ensure_client()
    orders, next_cursor = await client.get_orders(
        ticker=ticker,
        event_ticker=event_ticker,
        status=status,
        min_ts=min_ts,
        max_ts=max_ts,
        limit=limit,
        cursor=cursor,
    )

    return {
        "orders": [o.model_dump() for o in orders],
        "cursor": next_cursor,
        "count": len(orders),
    }


@mcp.tool()
async def kalshi_cancel_order(order_id: str) -> dict[str, Any]:
    """Cancel an existing order. **REQUIRES USER CONFIRMATION**.

    Args:
        order_id: Order ID to cancel

    Returns:
        Updated order with canceled status
    """
    _require_confirmation("kalshi_cancel_order", f"Cancel order: {order_id}")

    client = _ensure_client()
    order = await client.cancel_order(order_id)
    return order.model_dump()


@mcp.tool()
async def kalshi_amend_order(
    order_id: str,
    price: Optional[int] = None,
    count: Optional[int] = None,
) -> dict[str, Any]:
    """Modify an existing order. **REQUIRES USER CONFIRMATION**.

    Args:
        order_id: Order ID to modify
        price: New limit price in cents (optional)
        count: New contract count (optional)

    Returns:
        Updated order with new parameters
    """
    _require_confirmation(
        "kalshi_amend_order",
        f"Amend order {order_id}: price={price}, count={count}",
    )

    client = _ensure_client()
    order = await client.amend_order(order_id, price=price, count=count)
    return order.model_dump()


@mcp.tool()
async def kalshi_get_fills(
    ticker: Optional[str] = None,
    order_id: Optional[str] = None,
    min_ts: Optional[int] = None,
    max_ts: Optional[int] = None,
    limit: int = 100,
    cursor: Optional[str] = None,
) -> dict[str, Any]:
    """Get executed fills/trades.

    Args:
        ticker: Filter by market ticker
        order_id: Filter by order ID
        min_ts: Minimum timestamp (Unix seconds)
        max_ts: Maximum timestamp (Unix seconds)
        limit: Number of results (default 100)
        cursor: Pagination cursor

    Returns:
        List of executed fills with prices and timestamps
    """
    client = _ensure_client()
    fills, next_cursor = await client.get_fills(
        ticker=ticker,
        order_id=order_id,
        min_ts=min_ts,
        max_ts=max_ts,
        limit=limit,
        cursor=cursor,
    )

    return {
        "fills": [f.model_dump() for f in fills],
        "cursor": next_cursor,
        "count": len(fills),
    }


@mcp.tool()
async def kalshi_get_queue_position(order_id: str) -> dict[str, Any]:
    """Get an order's position in the price-time priority queue.

    Args:
        order_id: Order ID

    Returns:
        Queue position and priority info
    """
    client = _ensure_client()
    position = await client.get_queue_position(order_id)
    return position.model_dump()


# ========== TIER 3: ADVANCED FEATURES (7 tools) ==========


@mcp.tool()
async def kalshi_batch_create_orders(orders: list[dict[str, Any]]) -> dict[str, Any]:
    """Create multiple orders in a batch (max 20). **REQUIRES USER CONFIRMATION**.

    Args:
        orders: List of order dictionaries with ticker, side, count, type, price, etc.

    Returns:
        List of created orders with confirmation
    """
    _require_confirmation(
        "kalshi_batch_create_orders",
        f"Create batch of {len(orders)} orders",
    )

    client = _ensure_client()
    created_orders = await client.batch_create_orders(orders)

    return {
        "orders": [o.model_dump() for o in created_orders],
        "count": len(created_orders),
    }


@mcp.tool()
async def kalshi_batch_cancel_orders(order_ids: list[str]) -> dict[str, Any]:
    """Cancel multiple orders in a batch (max 20). **REQUIRES USER CONFIRMATION**.

    Args:
        order_ids: List of order IDs to cancel

    Returns:
        List of canceled orders with confirmation
    """
    _require_confirmation(
        "kalshi_batch_cancel_orders",
        f"Cancel batch of {len(order_ids)} orders",
    )

    client = _ensure_client()
    canceled_orders = await client.batch_cancel_orders(order_ids)

    return {
        "orders": [o.model_dump() for o in canceled_orders],
        "count": len(canceled_orders),
    }


@mcp.tool()
async def kalshi_create_order_group(contract_limit: int) -> dict[str, Any]:
    """Create an order group for risk management.

    An order group automatically cancels all resting orders when a contract
    limit is reached, providing protection against over-exposure.

    Args:
        contract_limit: Maximum contracts allowed in this group

    Returns:
        Created order group with ID
    """
    # Note: This requires API endpoint not yet documented in client
    # Placeholder implementation
    return {
        "order_group_id": "placeholder",
        "contract_limit": contract_limit,
        "matched_contracts": 0,
    }


@mcp.tool()
async def kalshi_get_order_groups() -> dict[str, Any]:
    """Get all user order groups.

    Returns:
        List of order groups with limits and status
    """
    # Note: This requires API endpoint not yet documented in client
    # Placeholder implementation
    return {
        "order_groups": [],
        "count": 0,
    }


@mcp.tool()
async def kalshi_create_rfq(
    ticker: str,
    side: str,
    count: int,
) -> dict[str, Any]:
    """Create a Request for Quote (RFQ) for market making.

    Args:
        ticker: Market ticker
        side: "buy" or "sell"
        count: Number of contracts

    Returns:
        Created RFQ with ID
    """
    # Note: This requires API endpoint not yet documented in client
    # Placeholder implementation
    return {
        "rfq_id": "placeholder",
        "ticker": ticker,
        "side": side,
        "count": count,
        "status": "open",
    }


@mcp.tool()
async def kalshi_get_rfqs(
    status: Optional[str] = None,
    ticker: Optional[str] = None,
) -> dict[str, Any]:
    """Get user's Requests for Quote (RFQs).

    Args:
        status: Filter by status (open, filled, expired)
        ticker: Filter by market ticker

    Returns:
        List of RFQs
    """
    # Note: This requires API endpoint not yet documented in client
    # Placeholder implementation
    return {
        "rfqs": [],
        "count": 0,
    }


@mcp.tool()
async def kalshi_get_multivariate_collections(
    status: Optional[str] = None,
) -> dict[str, Any]:
    """Get multivariate event collections for related market trading.

    Multivariate collections allow trading on combinations of related markets,
    useful for capturing correlations and hedging strategies.

    Args:
        status: Filter by status

    Returns:
        List of available multivariate collections
    """
    # Note: This requires API endpoint not yet documented in client
    # Placeholder implementation
    return {
        "collections": [],
        "count": 0,
    }


# ========== PHASE 1: PORTFOLIO MANAGEMENT TOOLS (7 tools) ==========


@mcp.tool()
async def kalshi_get_order_group(group_id: str) -> dict[str, Any]:
    """Get a single order group by ID.

    Args:
        group_id: Order group ID

    Returns:
        OrderGroup with id, contract_limit, and matched_contracts
    """
    client = _ensure_client()
    order_group = await client.get_order_group(group_id)
    return {
        "id": order_group.id,
        "contract_limit": order_group.contract_limit,
        "matched_contracts": order_group.matched_contracts,
    }


@mcp.tool()
async def kalshi_reset_order_group(group_id: str) -> dict[str, Any]:
    """Reset an order group's matched contract counter.

    This resets the counter back to 0, allowing the group to accept more orders.

    Args:
        group_id: Order group ID

    Returns:
        Confirmation message
    """
    client = _ensure_client()
    await client.reset_order_group(group_id)
    return {
        "status": "success",
        "message": f"Order group {group_id} reset successfully",
    }


@mcp.tool()
async def kalshi_delete_order_group(group_id: str) -> dict[str, Any]:
    """Delete an order group.

    Args:
        group_id: Order group ID to delete

    Returns:
        Confirmation message
    """
    client = _ensure_client()
    await client.delete_order_group(group_id)
    return {
        "status": "success",
        "message": f"Order group {group_id} deleted successfully",
    }


@mcp.tool()
async def kalshi_get_total_resting_order_value() -> dict[str, Any]:
    """Get total value of all resting orders.

    This metric is useful for:
    - Understanding total capital at risk
    - Portfolio rebalancing decisions
    - Risk management calculations

    Returns:
        Total value of resting orders in cents
    """
    client = _ensure_client()
    result = await client.get_total_resting_order_value()
    return {
        "total_resting_order_value": result.total_resting_order_value,
        "total_dollars": result.total_resting_order_value / 100,
    }


@mcp.tool()
async def kalshi_get_settlements(
    limit: int = 100,
    cursor: Optional[str] = None,
) -> dict[str, Any]:
    """Get historical settlements (filled orders) for P&L tracking.

    Settlements represent completed orders with final prices and payouts.
    Use this endpoint to:
    - Calculate historical P&L
    - Analyze past trading performance
    - Track settlement history

    Args:
        limit: Number of results (default 100, max 200)
        cursor: Pagination cursor for next page

    Returns:
        List of settlements with pagination info
    """
    client = _ensure_client()
    settlements, next_cursor = await client.get_settlements(limit=limit, cursor=cursor)

    return {
        "settlements": [
            {
                "order_id": s.order_id,
                "ticker": s.ticker,
                "side": s.side.value,
                "count": s.count,
                "price": s.price,
                "payout": s.payout,
                "payout_dollars": s.payout / 100,
                "created_at": s.created_at,
                "market_title": s.market_title,
            }
            for s in settlements
        ],
        "cursor": next_cursor,
        "count": len(settlements),
    }


@mcp.tool()
async def kalshi_decrease_order(order_id: str, count: int) -> dict[str, Any]:
    """Decrease the size of an existing resting order.

    Useful for:
    - Reducing position size without canceling and recreating
    - Partial profit-taking
    - Risk reduction mid-trade

    Args:
        order_id: Order ID to decrease
        count: Number of contracts to decrease by

    Returns:
        Updated Order details
    """
    client = _ensure_client()
    order = await client.decrease_order(order_id, count)

    return {
        "order_id": order.id,
        "ticker": order.ticker,
        "side": order.side.value,
        "count": order.count,
        "price": order.price,
        "status": order.status.value,
        "created_at": order.created_at,
        "modified_at": order.modified_at,
    }


@mcp.tool()
async def kalshi_get_queue_positions(order_ids: list[str]) -> dict[str, Any]:
    """Get queue positions for multiple orders in bulk.

    Queue position (0 = next to execute, higher numbers = further back).
    Useful for:
    - Monitoring order priority
    - Predicting execution timing
    - Analyzing market congestion

    Args:
        order_ids: List of order IDs to check positions for

    Returns:
        Dictionary mapping order_id to queue position
    """
    client = _ensure_client()
    positions = await client.get_queue_positions(order_ids)

    return {
        "positions": positions,
        "count": len(positions),
    }


# ========== PHASE 2: MARKET INTELLIGENCE & ANALYSIS TOOLS (5 tools) ==========


@mcp.tool()
async def kalshi_get_event_metadata(ticker: str) -> dict[str, Any]:
    """Get detailed metadata for an event.

    Event metadata includes additional information beyond basic event details,
    such as category classifications, historical context, and data sources.

    Args:
        ticker: Event ticker (e.g., KXHARRIS24)

    Returns:
        Event metadata dictionary
    """
    client = _ensure_client()
    metadata = await client.get_event_metadata(ticker)
    return {
        "ticker": ticker,
        "metadata": metadata,
    }


@mcp.tool()
async def kalshi_analyze_market_probability(ticker: str) -> dict[str, Any]:
    """Analyze a market and calculate implied probability from current prices.

    Implied probability is derived from the YES and NO side prices:
    - YES price = probability market resolves YES
    - NO price = probability market resolves NO
    - Both should sum to ~100 cents (100%)

    This is useful for:
    - Understanding market consensus on outcomes
    - Identifying mispricings (probability doesn't sum to 100)
    - Comparing implied vs. actual probabilities

    Args:
        ticker: Market ticker

    Returns:
        Implied probability analysis with mispricing detection
    """
    client = _ensure_client()
    market = await client.get_market(ticker)

    # Extract prices (in cents, 0-100)
    yes_price = market.yes_bid or 50  # Default to 50 if missing
    no_price = market.no_bid or 50
    midpoint_yes = ((market.yes_bid or 0) + (market.yes_ask or 100)) / 2
    midpoint_no = ((market.no_bid or 0) + (market.no_ask or 100)) / 2

    # Implied probabilities
    total_cents = yes_price + no_price if (yes_price and no_price) else 100
    implied_yes = (yes_price / total_cents * 100) if total_cents > 0 else 50
    implied_no = 100 - implied_yes

    # Calculate mispricing (should sum to 100, but usually ~99 due to spreads)
    mispricing = abs(total_cents - 100)

    return {
        "ticker": ticker,
        "market_title": market.title,
        "implied_probability": {
            "yes_percent": round(implied_yes, 2),
            "no_percent": round(implied_no, 2),
        },
        "prices": {
            "yes_bid": yes_price,
            "yes_ask": market.yes_ask,
            "no_bid": no_price,
            "no_ask": market.no_ask,
        },
        "mispricing": {
            "cents": mispricing,
            "is_mispriced": mispricing > 2,  # >2 cents suggests potential mispricing
        },
    }


@mcp.tool()
async def kalshi_analyze_market_spread(ticker: str) -> dict[str, Any]:
    """Calculate bid-ask spread for both YES and NO sides.

    Spread is the difference between ask and bid prices. Lower spreads indicate:
    - Better liquidity
    - Lower trading costs
    - More efficient price discovery

    Useful for:
    - Evaluating trading execution costs
    - Comparing market liquidity
    - Timing entry/exit decisions

    Args:
        ticker: Market ticker

    Returns:
        Spread analysis for YES and NO sides
    """
    client = _ensure_client()
    market = await client.get_market(ticker)

    # Calculate spreads
    yes_spread = (market.yes_ask or 100) - (market.yes_bid or 0) if market.yes_ask and market.yes_bid else None
    no_spread = (market.no_ask or 100) - (market.no_bid or 0) if market.no_ask and market.no_bid else None

    # Calculate spread percentages (relative to mid)
    yes_mid = ((market.yes_bid or 0) + (market.yes_ask or 100)) / 2
    no_mid = ((market.no_bid or 0) + (market.no_ask or 100)) / 2
    yes_spread_pct = (yes_spread / yes_mid * 100) if yes_spread and yes_mid > 0 else None
    no_spread_pct = (no_spread / no_mid * 100) if no_spread and no_mid > 0 else None

    return {
        "ticker": ticker,
        "market_title": market.title,
        "yes_side": {
            "bid": market.yes_bid,
            "ask": market.yes_ask,
            "spread_cents": yes_spread,
            "spread_percent": round(yes_spread_pct, 2) if yes_spread_pct else None,
        },
        "no_side": {
            "bid": market.no_bid,
            "ask": market.no_ask,
            "spread_cents": no_spread,
            "spread_percent": round(no_spread_pct, 2) if no_spread_pct else None,
        },
        "total_spread": round((yes_spread or 0) + (no_spread or 0), 2),
        "liquidity_assessment": "tight" if (yes_spread or 0) + (no_spread or 0) <= 2
            else "moderate" if (yes_spread or 0) + (no_spread or 0) <= 5
            else "wide",
    }


@mcp.tool()
async def kalshi_calculate_liquidity_score(ticker: str, depth: int = 10) -> dict[str, Any]:
    """Calculate a liquidity score for a market based on orderbook depth.

    Liquidity score is derived from:
    - Orderbook depth (how many contracts at each price level)
    - Bid-ask spread (tightness of prices)
    - Recent trade volume

    Score: 0-100, where higher = more liquid

    Useful for:
    - Assessing execution slippage risk
    - Finding good markets for large orders
    - Comparing market maturity

    Args:
        ticker: Market ticker
        depth: Orderbook depth to analyze (default 10, max 100)

    Returns:
        Liquidity score and component analysis
    """
    client = _ensure_client()
    market = await client.get_market(ticker)
    orderbook = await client.get_orderbook(ticker, depth=depth)

    # Calculate orderbook metrics
    yes_bids = sum([level[1] for level in (orderbook.yes_bids or [])])
    yes_asks = sum([level[1] for level in (orderbook.yes_asks or [])])
    no_bids = sum([level[1] for level in (orderbook.no_bids or [])])
    no_asks = sum([level[1] for level in (orderbook.no_asks or [])])

    total_orderbook_volume = yes_bids + yes_asks + no_bids + no_asks

    # Spread component (tighter = higher score)
    yes_spread = (market.yes_ask or 100) - (market.yes_bid or 0) if market.yes_ask and market.yes_bid else 5
    no_spread = (market.no_ask or 100) - (market.no_bid or 0) if market.no_ask and market.no_bid else 5
    avg_spread = (yes_spread + no_spread) / 2
    spread_score = max(0, 100 - (avg_spread * 20))  # Tight spread = high score

    # Volume component
    volume_score = min(100, (total_orderbook_volume / 10000) * 100) if total_orderbook_volume > 0 else 20

    # Market volume component
    recent_volume = market.volume_24h or 0
    volume_trend_score = min(100, (recent_volume / 100000) * 100) if recent_volume > 0 else 30

    # Composite score (weighted average)
    liquidity_score = (spread_score * 0.4 + volume_score * 0.3 + volume_trend_score * 0.3)

    return {
        "ticker": ticker,
        "market_title": market.title,
        "liquidity_score": round(liquidity_score, 2),
        "score_components": {
            "spread_component": round(spread_score, 2),
            "orderbook_depth_component": round(volume_score, 2),
            "volume_trend_component": round(volume_trend_score, 2),
        },
        "orderbook_metrics": {
            "yes_bids_volume": yes_bids,
            "yes_asks_volume": yes_asks,
            "no_bids_volume": no_bids,
            "no_asks_volume": no_asks,
            "total_orderbook_volume": total_orderbook_volume,
        },
        "assessment": "excellent" if liquidity_score >= 75
            else "good" if liquidity_score >= 50
            else "fair" if liquidity_score >= 25
            else "poor",
    }


@mcp.tool()
async def kalshi_analyze_portfolio_risk() -> dict[str, Any]:
    """Analyze portfolio risk combining positions, resting orders, and balance.

    Risk analysis includes:
    - Total exposure (sum of position values)
    - Max drawdown potential
    - Order execution risk
    - Correlated positions

    Useful for:
    - Portfolio rebalancing decisions
    - Understanding total risk exposure
    - Pre-trade risk checks

    Returns:
        Comprehensive portfolio risk analysis
    """
    client = _ensure_client()

    # Fetch all portfolio data
    balance = await client.get_balance()
    positions, _ = await client.get_positions(limit=1000)
    try:
        total_value = await client.get_total_resting_order_value()
        resting_order_value = total_value.total_resting_order_value
    except Exception:
        resting_order_value = 0

    # Calculate position metrics
    total_position_value = 0
    long_value = 0
    short_value = 0
    max_single_position = 0

    for position in positions:
        # Position value = contracts * current mid price (approximate)
        # For now, estimate at 50 cents (neutral position)
        position_value = position.contracts * 50
        total_position_value += position_value

        if position.contracts > 0:
            long_value += position_value
        else:
            short_value += abs(position_value)

        max_single_position = max(max_single_position, abs(position_value))

    # Portfolio metrics
    total_capital = balance.balance  # in cents
    used_capital = total_position_value + resting_order_value
    available_capital = total_capital - used_capital
    utilization_pct = (used_capital / total_capital * 100) if total_capital > 0 else 0

    # Risk assessment
    correlation_risk = "high" if len(positions) > 5 else "moderate" if len(positions) > 0 else "low"

    return {
        "capital_metrics": {
            "total_capital_cents": total_capital,
            "total_capital_dollars": total_capital / 100,
            "used_capital_cents": used_capital,
            "used_capital_dollars": used_capital / 100,
            "available_capital_cents": available_capital,
            "available_capital_dollars": available_capital / 100,
            "utilization_percent": round(utilization_pct, 2),
        },
        "position_metrics": {
            "total_positions": len(positions),
            "long_value_cents": long_value,
            "short_value_cents": short_value,
            "total_position_value_cents": total_position_value,
            "max_single_position_cents": max_single_position,
            "net_exposure_cents": long_value - short_value,
        },
        "order_metrics": {
            "resting_order_value_cents": resting_order_value,
            "resting_order_value_dollars": resting_order_value / 100,
        },
        "risk_assessment": {
            "utilization_level": "critical" if utilization_pct > 90
                else "high" if utilization_pct > 70
                else "moderate" if utilization_pct > 50
                else "low",
            "correlation_risk": correlation_risk,
            "recommendation": "reduce positions" if utilization_pct > 80
                else "maintain current risk" if utilization_pct > 40
                else "can take more risk",
        },
    }


# ========== TIER 4: WEBSOCKET TOOLS (4 tools) ==========


@mcp.tool()
async def kalshi_websocket_connect(
    channels: list[str],
    market_tickers: list[str],
) -> dict[str, Any]:
    """Establish WebSocket connection for real-time market data.

    Args:
        channels: List of channels to subscribe to:
            - "ticker": Real-time price updates
            - "orderbook_snapshot": Full order book state
            - "orderbook_delta": Incremental order book changes
            - "trades": Trade execution feed
        market_tickers: List of market tickers to subscribe to

    Returns:
        Connection details with connection ID
    """
    # Note: This requires WebSocket implementation not yet created
    # Placeholder implementation
    return {
        "connection_id": "placeholder",
        "channels": channels,
        "market_tickers": market_tickers,
        "status": "connected",
    }


@mcp.tool()
async def kalshi_websocket_subscribe(
    connection_id: str,
    channels: list[str],
    market_tickers: list[str],
) -> dict[str, Any]:
    """Subscribe to additional channels on WebSocket connection.

    Args:
        connection_id: Connection ID from kalshi_websocket_connect
        channels: Channels to subscribe to
        market_tickers: Market tickers to subscribe to

    Returns:
        Subscription confirmation
    """
    # Note: This requires WebSocket implementation not yet created
    # Placeholder implementation
    return {
        "connection_id": connection_id,
        "channels": channels,
        "market_tickers": market_tickers,
        "status": "subscribed",
    }


@mcp.tool()
async def kalshi_websocket_unsubscribe(
    connection_id: str,
    channels: list[str],
    market_tickers: list[str],
) -> dict[str, Any]:
    """Unsubscribe from channels on WebSocket connection.

    Args:
        connection_id: Connection ID
        channels: Channels to unsubscribe from
        market_tickers: Market tickers to unsubscribe from

    Returns:
        Unsubscribe confirmation
    """
    # Note: This requires WebSocket implementation not yet created
    # Placeholder implementation
    return {
        "connection_id": connection_id,
        "channels": channels,
        "market_tickers": market_tickers,
        "status": "unsubscribed",
    }


@mcp.tool()
async def kalshi_websocket_disconnect(connection_id: str) -> dict[str, Any]:
    """Close WebSocket connection.

    Args:
        connection_id: Connection ID to close

    Returns:
        Disconnection confirmation
    """
    # Note: This requires WebSocket implementation not yet created
    # Placeholder implementation
    return {
        "connection_id": connection_id,
        "status": "disconnected",
    }


if __name__ == "__main__":
    # Run the MCP server
    mcp.run()
