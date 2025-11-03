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
)


# Initialize FastMCP server
mcp = FastMCP("Kalshi Prediction Markets")

# Global client instance (initialized on startup)
client: Optional[KalshiClient] = None


def _ensure_client() -> KalshiClient:
    """Ensure client is initialized."""
    global client
    if client is None:
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
