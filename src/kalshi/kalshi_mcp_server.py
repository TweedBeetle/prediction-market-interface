"""Kalshi MCP Server - FastMCP-based prediction market trading interface."""

import os
from typing import Annotated

from fastmcp import FastMCP, Context
from pydantic import Field
from loguru import logger

from .client import KalshiClient
from .models import (
    ExchangeStatus,
    Balance,
    Market,
    Event,
    Order,
    Position,
    Fill,
    OrderBook,
    Trade,
)

# Determine environment from loaded env vars
# (Wrapper scripts load .env.kalshi.demo or .env.kalshi.prod before importing)
env = os.getenv("KALSHI_ENVIRONMENT", "unknown")

# Safety limits for order execution
MAX_ORDER_SIZE = int(os.getenv("KALSHI_MAX_ORDER_SIZE", "100"))
LARGE_ORDER_THRESHOLD = int(os.getenv("KALSHI_LARGE_ORDER_THRESHOLD", "50"))

# Create FastMCP server with environment-specific name
mcp = FastMCP(
    name=f"Kalshi Trading ({env.upper()})",
    instructions=f"""
    Kalshi prediction market trading server.

    Environment: {env.upper()}
    {'⚠️ DEMO MODE - Using test money only, safe for experimentation' if env == 'demo' else '💰 PRODUCTION - Real money trades, use with caution'}

    This server enables you to:
    - Research prediction markets on current events
    - View market prices and orderbooks
    - Get account balance and positions
    - Execute trades (market and limit orders)

    Always check the environment before placing real orders!
    """,
)

logger.info(f"Initializing Kalshi MCP server - Environment: {env}")


# ============================================================================
# TOOLS
# ============================================================================


@mcp.tool
async def kalshi_get_exchange_status(ctx: Context | None = None) -> ExchangeStatus:
    """
    Check if the Kalshi exchange is operational and accepting trades.

    Returns:
        Exchange status including whether trading is active

    Use this to verify the exchange is online before attempting trades.
    """
    if ctx:
        await ctx.info("Checking Kalshi exchange status...")

    async with KalshiClient.from_env() as client:
        status = await client.get_exchange_status()

    if ctx:
        state = "✅ ONLINE" if status.exchange_active else "❌ OFFLINE"
        trading = "✅ TRADING" if status.trading_active else "⏸️ HALTED"
        await ctx.info(f"Exchange: {state} | Trading: {trading}")

    return status


@mcp.tool
async def kalshi_get_balance(ctx: Context | None = None) -> Balance:
    """
    Get current account balance.

    Returns:
        Account balance in cents and dollars

    Use this to check available funds before placing orders.
    """
    if ctx:
        await ctx.info("Fetching account balance...")

    async with KalshiClient.from_env() as client:
        balance = await client.get_balance()

    if ctx:
        await ctx.info(f"Balance: ${balance.balance_dollars:.2f} (${balance.balance} cents)")

    return balance


@mcp.tool
async def kalshi_search_markets(
    query: Annotated[
        str | None,
        Field(description="Search query to find markets (e.g., 'Bitcoin', 'election', 'AI')")
    ] = None,
    limit: Annotated[
        int,
        Field(description="Maximum number of markets to return", ge=1, le=100)
    ] = 20,
    status: Annotated[
        str,
        Field(description="Filter by market status: 'open', 'closed', or 'settled'")
    ] = "open",
    ctx: Context | None = None,
) -> list[Market]:
    """
    Search for prediction markets on Kalshi.

    Args:
        query: Keywords to search for (e.g., "Bitcoin", "election")
        limit: Maximum number of results (1-100)
        status: Filter by status - "open" for active markets, "closed" for settled

    Returns:
        List of matching markets with prices, volume, and details

    Use this to discover markets about topics you're interested in.
    Perfect for researching opportunities or finding specific markets.

    Examples:
        - Find Bitcoin markets: kalshi_search_markets("Bitcoin")
        - Get all open markets: kalshi_search_markets(limit=50)
        - Find settled election markets: kalshi_search_markets("election", status="settled")
    """
    if ctx:
        search_desc = f"'{query}'" if query else "all markets"
        await ctx.info(f"Searching for {search_desc} (limit={limit}, status={status})...")

    async with KalshiClient.from_env() as client:
        markets = await client.search_markets(query=query, limit=limit, status=status)

    if ctx:
        await ctx.info(f"Found {len(markets)} markets")
        if markets:
            top_market = markets[0]
            await ctx.info(f"Top result: {top_market.ticker} - {top_market.title}")

    return markets


@mcp.tool
async def kalshi_get_market(
    ticker: Annotated[
        str,
        Field(description="Market ticker symbol (e.g., 'KXBTC-23DEC-50K')")
    ],
    ctx: Context | None = None,
) -> Market:
    """
    Get detailed information about a specific prediction market.

    Args:
        ticker: The market's ticker symbol (from search results)

    Returns:
        Complete market details including:
        - Current bid/ask prices
        - Trading volume and open interest
        - Market status and expiration time
        - Human-readable interpretation

    Use this after searching to get full details about a specific market
    before deciding whether to trade.

    Example:
        market = kalshi_get_market("KXBTC-31DEC-50K")
        # Returns prices, volume, and interpretation like:
        # "Market implies 42% chance: Bitcoin reaches $50K by Dec 31"
    """
    if ctx:
        await ctx.info(f"Fetching market details for {ticker}...")

    async with KalshiClient.from_env() as client:
        market = await client.get_market(ticker)

    if ctx:
        await ctx.info(f"Market: {market.title}")
        if market.yes_ask:
            await ctx.info(f"YES price: {market.yes_ask}¢ | {market.interpretation}")
        await ctx.info(f"Status: {market.status} | Volume 24h: {market.volume_24h or 0:,}")

    return market


@mcp.tool
async def kalshi_create_market_order(
    ticker: Annotated[
        str,
        Field(description="Market ticker symbol (e.g., 'KXBTC-23DEC-50K')")
    ],
    side: Annotated[
        str,
        Field(description="Order side: 'yes' or 'no'")
    ],
    quantity: Annotated[
        int,
        Field(description="Number of contracts to buy", ge=1)
    ],
    action: Annotated[
        str,
        Field(description="Order action: 'buy' or 'sell'")
    ] = "buy",
    ctx: Context | None = None,
) -> Order:
    """
    Create a market order (executes immediately at current market price).

    Args:
        ticker: Market ticker symbol
        side: "yes" or "no"
        quantity: Number of contracts (1-MAX_ORDER_SIZE)
        action: "buy" or "sell" (default: "buy")

    Returns:
        Order details including fill information

    Market orders execute immediately at the best available price.
    Use this when you want immediate execution and don't need price control.

    Example:
        order = kalshi_create_market_order("KXBTC-31DEC-50K", "yes", 10)
        # Buys 10 YES contracts immediately at market price
    """
    # Validate order size
    if quantity > MAX_ORDER_SIZE:
        raise ValueError(f"Order size {quantity} exceeds maximum {MAX_ORDER_SIZE}")

    if ctx:
        if quantity > LARGE_ORDER_THRESHOLD:
            await ctx.info(f"⚠️ Large order: {quantity} contracts")
        await ctx.info(f"Creating market order: {action.upper()} {quantity}x {side.upper()} on {ticker}")

    async with KalshiClient.from_env() as client:
        # Check balance
        balance = await client.get_balance()
        estimated_cost = quantity * 100  # Rough estimate (max is 100¢ per contract)
        if estimated_cost > balance.balance:
            raise ValueError(
                f"Insufficient balance: need ~${estimated_cost/100:.2f}, "
                f"have ${balance.balance_dollars:.2f}"
            )

        # Create order
        order = await client.create_order(
            ticker=ticker,
            side=side,
            count=quantity,
            action=action,
            order_type="market"
        )

    if ctx:
        if order.is_filled:
            avg_price = order.average_fill_price or 0
            await ctx.info(f"✅ Filled {order.fill_count}/{quantity} @ {avg_price}¢ avg")
        else:
            await ctx.info(f"⏳ Order created: {order.order_id} (status: {order.status})")

    return order


@mcp.tool
async def kalshi_create_limit_order(
    ticker: Annotated[
        str,
        Field(description="Market ticker symbol (e.g., 'KXBTC-23DEC-50K')")
    ],
    side: Annotated[
        str,
        Field(description="Order side: 'yes' or 'no'")
    ],
    quantity: Annotated[
        int,
        Field(description="Number of contracts to buy", ge=1)
    ],
    price: Annotated[
        int,
        Field(description="Limit price in cents (1-99)", ge=1, le=99)
    ],
    action: Annotated[
        str,
        Field(description="Order action: 'buy' or 'sell'")
    ] = "buy",
    ctx: Context | None = None,
) -> Order:
    """
    Create a limit order (only executes at specified price or better).

    Args:
        ticker: Market ticker symbol
        side: "yes" or "no"
        quantity: Number of contracts (1-MAX_ORDER_SIZE)
        price: Limit price in cents (1-99)
        action: "buy" or "sell" (default: "buy")

    Returns:
        Order details including resting order information

    Limit orders only execute at your specified price or better.
    The order will rest on the orderbook until filled or canceled.

    Example:
        order = kalshi_create_limit_order("KXBTC-31DEC-50K", "yes", 10, 45)
        # Buys 10 YES contracts only if price is 45¢ or less
    """
    # Validate order size
    if quantity > MAX_ORDER_SIZE:
        raise ValueError(f"Order size {quantity} exceeds maximum {MAX_ORDER_SIZE}")

    if ctx:
        if quantity > LARGE_ORDER_THRESHOLD:
            await ctx.info(f"⚠️ Large order: {quantity} contracts")
        await ctx.info(
            f"Creating limit order: {action.upper()} {quantity}x {side.upper()} "
            f"on {ticker} @ {price}¢"
        )

    async with KalshiClient.from_env() as client:
        # Check balance for buy orders
        if action == "buy":
            balance = await client.get_balance()
            estimated_cost = quantity * price
            if estimated_cost > balance.balance:
                raise ValueError(
                    f"Insufficient balance: need ${estimated_cost/100:.2f}, "
                    f"have ${balance.balance_dollars:.2f}"
                )

        # Create order
        kwargs = {
            "ticker": ticker,
            "side": side,
            "count": quantity,
            "action": action,
            "order_type": "limit",
        }
        if side == "yes":
            kwargs["yes_price"] = price
        else:
            kwargs["no_price"] = price

        order = await client.create_order(**kwargs)

    if ctx:
        if order.is_active:
            await ctx.info(
                f"📋 Limit order resting: {order.order_id} "
                f"(queue position: {order.queue_position or 'N/A'})"
            )
        elif order.is_filled:
            avg_price = order.average_fill_price or price
            await ctx.info(f"✅ Immediately filled {order.fill_count}/{quantity} @ {avg_price}¢")
        else:
            await ctx.info(f"Order created: {order.order_id} (status: {order.status})")

    return order


@mcp.tool
async def kalshi_cancel_order(
    order_id: Annotated[
        str,
        Field(description="Order ID to cancel")
    ],
    ctx: Context | None = None,
) -> Order:
    """
    Cancel a pending order.

    Args:
        order_id: The order ID to cancel

    Returns:
        Canceled order details

    Cancels a resting limit order. Market orders cannot be canceled
    as they execute immediately. Only works for orders that haven't
    been fully filled yet.

    Example:
        order = kalshi_cancel_order("01234567-89ab-cdef-0123-456789abcdef")
        # Cancels the specified order
    """
    if ctx:
        await ctx.info(f"Canceling order: {order_id}")

    async with KalshiClient.from_env() as client:
        order = await client.cancel_order(order_id)

    if ctx:
        if order.status == "canceled":
            await ctx.info(f"✅ Order canceled: {order.remaining_count} unfilled contracts")
        else:
            await ctx.info(f"Order status: {order.status}")

    return order


@mcp.tool
async def kalshi_amend_order(
    order_id: Annotated[
        str,
        Field(description="Order ID to amend")
    ],
    new_quantity: Annotated[
        int,
        Field(description="New contract count", ge=1)
    ],
    new_price: Annotated[
        int,
        Field(description="New price in cents (1-99)", ge=1, le=99)
    ],
    ctx: Context | None = None,
) -> Order:
    """
    Amend an order (modify price/quantity without losing queue position).

    Args:
        order_id: Order ID to amend
        new_quantity: New contract count
        new_price: New price in cents (1-99)

    Returns:
        Amended order details

    Amending an order modifies it without losing your place in the queue
    (unlike cancel + create). Only works for resting limit orders.

    Example:
        order = kalshi_amend_order(
            "01234567-89ab-cdef-0123-456789abcdef",
            new_quantity=20,
            new_price=46
        )
        # Changes order to 20 contracts @ 46¢
    """
    if new_quantity > MAX_ORDER_SIZE:
        raise ValueError(f"Order size {new_quantity} exceeds maximum {MAX_ORDER_SIZE}")

    if ctx:
        await ctx.info(f"Amending order {order_id}: {new_quantity} contracts @ {new_price}¢")

    async with KalshiClient.from_env() as client:
        order = await client.amend_order(order_id, new_quantity, new_price)

    if ctx:
        await ctx.info(
            f"✅ Order amended: {order.remaining_count} remaining @ {new_price}¢ "
            f"(queue: {order.queue_position or 'N/A'})"
        )

    return order


@mcp.tool
async def kalshi_decrease_order(
    order_id: Annotated[
        str,
        Field(description="Order ID to decrease")
    ],
    reduce_by: Annotated[
        int,
        Field(description="Number of contracts to reduce by", ge=1)
    ],
    ctx: Context | None = None,
) -> Order:
    """
    Decrease order size without losing queue position.

    Args:
        order_id: Order ID to decrease
        reduce_by: Number of contracts to reduce by

    Returns:
        Updated order details

    Reduces the size of a resting order while maintaining queue position.
    Useful for partially unwinding a position without full cancellation.

    Example:
        order = kalshi_decrease_order(
            "01234567-89ab-cdef-0123-456789abcdef",
            reduce_by=5
        )
        # Reduces order by 5 contracts (e.g., 20 → 15)
    """
    if ctx:
        await ctx.info(f"Decreasing order {order_id} by {reduce_by} contracts")

    async with KalshiClient.from_env() as client:
        order = await client.decrease_order(order_id, reduce_by)

    if ctx:
        await ctx.info(
            f"✅ Order decreased: {order.remaining_count} remaining "
            f"(queue: {order.queue_position or 'N/A'})"
        )

    return order


# ============================================================================
# PORTFOLIO MANAGEMENT
# ============================================================================


@mcp.tool
async def kalshi_get_positions(
    ticker: Annotated[
        str | None,
        Field(description="Filter by ticker (optional)")
    ] = None,
    limit: Annotated[
        int,
        Field(description="Maximum number of positions to return", ge=1, le=200)
    ] = 100,
    ctx: Context | None = None,
) -> list[Position]:
    """
    Get current portfolio positions.

    Args:
        ticker: Filter by ticker (optional)
        limit: Maximum results (1-200)

    Returns:
        List of current positions with P&L information

    Shows your current holdings across all markets or filtered by ticker.
    Includes realized and unrealized P&L, position size, and market exposure.

    Example:
        positions = kalshi_get_positions()
        # Returns all current positions with P&L
    """
    if ctx:
        filter_desc = f" for {ticker}" if ticker else ""
        await ctx.info(f"Fetching positions{filter_desc}...")

    async with KalshiClient.from_env() as client:
        positions = await client.get_positions(ticker=ticker, limit=limit)

    if ctx:
        if positions:
            total_pnl = sum(p.pnl_dollars for p in positions)
            await ctx.info(
                f"Found {len(positions)} position(s) | "
                f"Total P&L: ${total_pnl:.2f}"
            )
            # Show top 3 positions by absolute P&L
            sorted_positions = sorted(positions, key=lambda p: abs(p.pnl_dollars), reverse=True)
            for i, pos in enumerate(sorted_positions[:3], 1):
                pnl_emoji = "📈" if pos.pnl_dollars > 0 else "📉" if pos.pnl_dollars < 0 else "➡️"
                await ctx.info(
                    f"{i}. {pos.ticker}: {pos.position:+d} {pos.side_name} | "
                    f"{pnl_emoji} ${pos.pnl_dollars:+.2f}"
                )
        else:
            await ctx.info("No positions found")

    return positions


@mcp.tool
async def kalshi_get_fills(
    ticker: Annotated[
        str | None,
        Field(description="Filter by ticker (optional)")
    ] = None,
    order_id: Annotated[
        str | None,
        Field(description="Filter by order ID (optional)")
    ] = None,
    limit: Annotated[
        int,
        Field(description="Maximum number of fills to return", ge=1, le=200)
    ] = 100,
    ctx: Context | None = None,
) -> list[Fill]:
    """
    Get trade execution history (fills).

    Args:
        ticker: Filter by ticker (optional)
        order_id: Filter by order ID (optional)
        limit: Maximum results (1-200)

    Returns:
        List of trade fills with prices and fees

    Shows your trade execution history - when orders were filled,
    at what price, and with what fees. Useful for tracking execution
    quality and analyzing trading costs.

    Example:
        fills = kalshi_get_fills(ticker="KXBTC-31DEC-50K")
        # Returns all fills for this market
    """
    if ctx:
        filters = []
        if ticker:
            filters.append(f"ticker={ticker}")
        if order_id:
            filters.append(f"order_id={order_id}")
        filter_desc = f" ({', '.join(filters)})" if filters else ""
        await ctx.info(f"Fetching fill history{filter_desc}...")

    async with KalshiClient.from_env() as client:
        fills = await client.get_fills(ticker=ticker, order_id=order_id, limit=limit)

    if ctx:
        if fills:
            total_volume = sum(f.cost_dollars for f in fills)
            total_fees = sum(f.fees_dollars for f in fills)
            await ctx.info(
                f"Found {len(fills)} fill(s) | "
                f"Total volume: ${total_volume:.2f} | "
                f"Total fees: ${total_fees:.2f}"
            )
            # Show most recent 3 fills
            for i, fill in enumerate(fills[:3], 1):
                action_emoji = "🟢" if fill.action == "buy" else "🔴"
                taker_marker = " (taker)" if fill.is_taker else " (maker)"
                await ctx.info(
                    f"{i}. {fill.ticker}: {action_emoji} {fill.action.upper()} "
                    f"{fill.count}x {fill.side.upper()} @ {fill.price}¢{taker_marker}"
                )
        else:
            await ctx.info("No fills found")

    return fills


@mcp.tool
async def kalshi_get_orders(
    ticker: Annotated[
        str | None,
        Field(description="Filter by ticker (optional)")
    ] = None,
    status: Annotated[
        str,
        Field(description="Filter by status: 'resting', 'canceled', 'filled'")
    ] = "resting",
    limit: Annotated[
        int,
        Field(description="Maximum number of orders to return", ge=1, le=200)
    ] = 100,
    ctx: Context | None = None,
) -> list[Order]:
    """
    Get orders (active, filled, or canceled).

    Args:
        ticker: Filter by ticker (optional)
        status: Filter by status (default: "resting")
        limit: Maximum results (1-200)

    Returns:
        List of orders matching filters

    Shows your orders across all markets or filtered by ticker and status.
    Use status="resting" for active orders, "filled" for completed orders,
    or "canceled" for canceled orders.

    Example:
        orders = kalshi_get_orders(status="resting")
        # Returns all active orders waiting to be filled
    """
    if ctx:
        filter_desc = f" for {ticker}" if ticker else ""
        await ctx.info(f"Fetching {status} orders{filter_desc}...")

    async with KalshiClient.from_env() as client:
        orders = await client.get_orders(ticker=ticker, status=status, limit=limit)

    if ctx:
        if orders:
            await ctx.info(f"Found {len(orders)} order(s)")
            # Show up to 3 orders
            for i, order in enumerate(orders[:3], 1):
                status_emoji = "📋" if order.is_active else "✅" if order.is_filled else "❌"
                progress = f"{order.fill_count}/{order.initial_count}" if order.initial_count else "N/A"
                await ctx.info(
                    f"{i}. {status_emoji} {order.ticker}: "
                    f"{order.action.upper()} {order.side.upper()} "
                    f"({progress} filled)"
                )
        else:
            await ctx.info("No orders found")

    return orders


# ============================================================================
# MARKET DISCOVERY (ADVANCED)
# ============================================================================


@mcp.tool
async def kalshi_get_events(
    limit: Annotated[
        int,
        Field(description="Maximum number of events to return", ge=1, le=200)
    ] = 50,
    status: Annotated[
        str,
        Field(description="Filter by status: 'open', 'closed', 'settled'")
    ] = "open",
    ctx: Context | None = None,
) -> list[Event]:
    """
    Get list of prediction market events.

    Args:
        limit: Maximum results (1-200)
        status: Filter by status (default: "open")

    Returns:
        List of events

    Events are collections of related markets. For example, an event
    might be "2024 Presidential Election" with multiple markets for
    different outcomes or timeframes.

    Example:
        events = kalshi_get_events(status="open", limit=20)
        # Returns active events with their markets
    """
    if ctx:
        await ctx.info(f"Fetching {status} events (limit={limit})...")

    async with KalshiClient.from_env() as client:
        events = await client.get_events(limit=limit, status=status)

    if ctx:
        if events:
            await ctx.info(f"Found {len(events)} event(s)")
            # Show up to 3 events
            for i, event in enumerate(events[:3], 1):
                await ctx.info(f"{i}. {event.event_ticker}: {event.title}")
        else:
            await ctx.info("No events found")

    return events


@mcp.tool
async def kalshi_get_event(
    event_ticker: Annotated[
        str,
        Field(description="Event ticker (e.g., 'INXD-25JAN31')")
    ],
    ctx: Context | None = None,
) -> Event:
    """
    Get detailed information about a specific event.

    Args:
        event_ticker: Event ticker symbol

    Returns:
        Event details

    Get full details about an event including its category, title,
    settlement date, and whether markets are mutually exclusive.

    Example:
        event = kalshi_get_event("INXD-25JAN31")
        # Returns event details and structure
    """
    if ctx:
        await ctx.info(f"Fetching event: {event_ticker}")

    async with KalshiClient.from_env() as client:
        event = await client.get_event(event_ticker)

    if ctx:
        await ctx.info(f"Event: {event.title}")
        await ctx.info(f"Category: {event.category}")
        if event.strike_date:
            await ctx.info(f"Strike date: {event.strike_date}")

    return event


@mcp.tool
async def kalshi_get_orderbook(
    ticker: Annotated[
        str,
        Field(description="Market ticker symbol")
    ],
    depth: Annotated[
        int,
        Field(description="Number of price levels per side", ge=1, le=100)
    ] = 10,
    ctx: Context | None = None,
) -> OrderBook:
    """
    Get order book depth for a market (bids and asks).

    Args:
        ticker: Market ticker
        depth: Number of price levels per side (default: 10)

    Returns:
        Order book with bids and asks for YES and NO sides

    Shows available liquidity at each price level. Useful for
    understanding market depth before placing large orders.

    Example:
        book = kalshi_get_orderbook("KXBTC-31DEC-50K", depth=5)
        # Returns top 5 levels of bids/asks for both YES and NO
    """
    if ctx:
        await ctx.info(f"Fetching order book for {ticker} (depth={depth})...")

    async with KalshiClient.from_env() as client:
        orderbook = await client.get_orderbook(ticker, depth=depth)

    if ctx:
        if orderbook.yes_bids or orderbook.yes_asks:
            yes_best_bid = orderbook.yes_bids[0].price if orderbook.yes_bids else None
            yes_best_ask = orderbook.yes_asks[0].price if orderbook.yes_asks else None
            spread = orderbook.yes_spread

            await ctx.info(
                f"YES market: "
                f"Best bid: {yes_best_bid}¢ | "
                f"Best ask: {yes_best_ask}¢ | "
                f"Spread: {spread}¢" if spread else "N/A"
            )
            await ctx.info(f"Total YES liquidity: {orderbook.yes_depth} contracts")
        else:
            await ctx.info("No liquidity in order book")

    return orderbook


@mcp.tool
async def kalshi_get_trades(
    ticker: Annotated[
        str | None,
        Field(description="Filter by market ticker (optional)")
    ] = None,
    limit: Annotated[
        int,
        Field(description="Maximum number of trades to return", ge=1, le=200)
    ] = 100,
    ctx: Context | None = None,
) -> list[Trade]:
    """
    Get recent public trades (market activity).

    Args:
        ticker: Filter by market ticker (optional)
        limit: Maximum results (1-200)

    Returns:
        List of recent trades with prices and volumes

    Shows recent trade flow - useful for understanding market
    momentum, execution prices, and trading activity patterns.

    Example:
        trades = kalshi_get_trades(ticker="KXBTC-31DEC-50K", limit=50)
        # Returns last 50 trades on this market
    """
    if ctx:
        filter_desc = f" for {ticker}" if ticker else ""
        await ctx.info(f"Fetching recent trades{filter_desc}...")

    async with KalshiClient.from_env() as client:
        trades = await client.get_trades(ticker=ticker, limit=limit)

    if ctx:
        if trades:
            total_volume = sum(t.volume_dollars for t in trades)
            await ctx.info(
                f"Found {len(trades)} trade(s) | "
                f"Total volume: ${total_volume:.2f}"
            )
            # Show 3 most recent trades
            for i, trade in enumerate(trades[:3], 1):
                side_emoji = "🟢" if trade.side == "yes" else "🔴"
                await ctx.info(
                    f"{i}. {side_emoji} {trade.side.upper()} "
                    f"{trade.count}x @ {trade.price}¢ "
                    f"(${trade.volume_dollars:.2f})"
                )
        else:
            await ctx.info("No recent trades found")

    return trades


# ============================================================================
# RESOURCES (Optional but useful for context)
# ============================================================================


@mcp.resource("kalshi://account/balance")
async def get_balance_resource() -> str:
    """Current account balance as a resource."""
    async with KalshiClient.from_env() as client:
        balance = await client.get_balance()
    return f"Account Balance: ${balance.balance_dollars:.2f} ({balance.balance} cents)"


@mcp.resource("kalshi://exchange/status")
async def get_exchange_status_resource() -> str:
    """Exchange operational status as a resource."""
    async with KalshiClient.from_env() as client:
        status = await client.get_exchange_status()

    lines = [
        f"Exchange Status: {'✅ ONLINE' if status.exchange_active else '❌ OFFLINE'}",
        f"Trading: {'✅ ACTIVE' if status.trading_active else '⏸️ HALTED'}"
    ]
    return "\n".join(lines)


# ============================================================================
# SERVER LIFECYCLE
# ============================================================================


if __name__ == "__main__":
    # This allows running the server directly for testing
    # In production, wrapper scripts import and run via mcp.run()
    logger.info(f"Starting Kalshi MCP server in {env} mode...")
    mcp.run()
