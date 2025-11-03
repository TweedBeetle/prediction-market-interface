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
    BatchOrderResponse,
    OrderGroup,
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
async def kalshi_diagnose_api_health(ctx: Context | None = None) -> dict:
    """
    Comprehensive API health diagnostic tool.

    Tests multiple Kalshi API endpoints to determine which services are available.
    Useful for troubleshooting when specific features aren't working.

    Returns:
        Detailed health report with status for each service category

    Use this when:
    - Debugging unexpected API errors
    - Checking if advanced features (batch ops, order groups) are available
    - Verifying API connectivity before complex operations

    Example output:
    {
        "overall_status": "degraded",
        "services": {
            "exchange": {"available": true, "latency_ms": 123},
            "authentication": {"available": true, "latency_ms": 456},
            "market_data": {"available": true, "latency_ms": 234},
            "order_management": {"available": true, "latency_ms": 345},
            "order_groups": {"available": false, "error": "503 Service Unavailable"},
            "batch_operations": {"available": false, "error": "403 Forbidden"}
        }
    }
    """
    if ctx:
        await ctx.info("🔍 Running comprehensive API health diagnostics...")

    import time
    from httpx import HTTPStatusError

    health_report = {
        "timestamp": time.time(),
        "environment": "unknown",
        "overall_status": "healthy",
        "services": {}
    }

    async with KalshiClient.from_env() as client:
        # Capture environment from client
        health_report["environment"] = "demo" if "demo" in client.base_url else "production"

        # Test 1: Exchange Status (basic connectivity)
        if ctx:
            await ctx.info("Testing: Exchange status...")
        try:
            start = time.time()
            status = await client.get_exchange_status()
            latency = int((time.time() - start) * 1000)
            health_report["services"]["exchange"] = {
                "available": True,
                "exchange_active": status.exchange_active,
                "trading_active": status.trading_active,
                "latency_ms": latency
            }
            if ctx:
                await ctx.info(f"  ✅ Exchange: OK ({latency}ms)")
        except Exception as e:
            health_report["services"]["exchange"] = {
                "available": False,
                "error": str(e)
            }
            health_report["overall_status"] = "critical"
            if ctx:
                await ctx.info(f"  ❌ Exchange: FAILED - {str(e)[:50]}")

        # Test 2: Authentication & Account Access
        if ctx:
            await ctx.info("Testing: Authentication & balance...")
        try:
            start = time.time()
            balance = await client.get_balance()
            latency = int((time.time() - start) * 1000)
            health_report["services"]["authentication"] = {
                "available": True,
                "balance_cents": balance.balance,
                "latency_ms": latency
            }
            if ctx:
                await ctx.info(f"  ✅ Authentication: OK ({latency}ms)")
        except Exception as e:
            health_report["services"]["authentication"] = {
                "available": False,
                "error": str(e)
            }
            health_report["overall_status"] = "critical"
            if ctx:
                await ctx.info(f"  ❌ Authentication: FAILED - {str(e)[:50]}")

        # Test 3: Market Data (read-only)
        if ctx:
            await ctx.info("Testing: Market data access...")
        try:
            start = time.time()
            markets = await client.search_markets(limit=1, status="open")
            latency = int((time.time() - start) * 1000)
            health_report["services"]["market_data"] = {
                "available": True,
                "sample_markets_found": len(markets),
                "latency_ms": latency
            }
            if ctx:
                await ctx.info(f"  ✅ Market Data: OK ({latency}ms)")
        except Exception as e:
            health_report["services"]["market_data"] = {
                "available": False,
                "error": str(e)
            }
            if "critical" not in health_report["overall_status"]:
                health_report["overall_status"] = "degraded"
            if ctx:
                await ctx.info(f"  ⚠️ Market Data: FAILED - {str(e)[:50]}")

        # Test 4: Order Management (portfolio access)
        if ctx:
            await ctx.info("Testing: Order management...")
        try:
            start = time.time()
            orders = await client.get_orders(limit=1)
            latency = int((time.time() - start) * 1000)
            health_report["services"]["order_management"] = {
                "available": True,
                "latency_ms": latency
            }
            if ctx:
                await ctx.info(f"  ✅ Order Management: OK ({latency}ms)")
        except Exception as e:
            health_report["services"]["order_management"] = {
                "available": False,
                "error": str(e)
            }
            if "critical" not in health_report["overall_status"]:
                health_report["overall_status"] = "degraded"
            if ctx:
                await ctx.info(f"  ⚠️ Order Management: FAILED - {str(e)[:50]}")

        # Test 5: Order Groups (advanced feature)
        if ctx:
            await ctx.info("Testing: Order groups (advanced)...")
        try:
            start = time.time()
            groups = await client.get_order_groups(limit=1)
            latency = int((time.time() - start) * 1000)
            health_report["services"]["order_groups"] = {
                "available": True,
                "latency_ms": latency
            }
            if ctx:
                await ctx.info(f"  ✅ Order Groups: OK ({latency}ms)")
        except HTTPStatusError as e:
            error_code = e.response.status_code
            health_report["services"]["order_groups"] = {
                "available": False,
                "error_code": error_code,
                "error": str(e)[:100]
            }
            if error_code == 503:
                if ctx:
                    await ctx.info(f"  ⚠️ Order Groups: Service unavailable (503) - temporary outage")
            elif error_code == 403:
                if ctx:
                    await ctx.info(f"  ℹ️ Order Groups: Access denied (403) - feature requires advanced access")
            else:
                if ctx:
                    await ctx.info(f"  ⚠️ Order Groups: FAILED ({error_code})")
        except Exception as e:
            health_report["services"]["order_groups"] = {
                "available": False,
                "error": str(e)[:100]
            }
            if ctx:
                await ctx.info(f"  ⚠️ Order Groups: FAILED - {str(e)[:50]}")

        # Test 6: Batch Operations (advanced feature, likely needs special access)
        if ctx:
            await ctx.info("Testing: Batch operations (advanced)...")
        try:
            start = time.time()
            # Try to create empty batch (will fail validation but tests endpoint access)
            await client.batch_create_orders([])
        except ValueError as e:
            # Expected: "exceeds maximum of 20" or similar validation
            if "exceeds" in str(e).lower() or "batch size 0" in str(e).lower():
                latency = int((time.time() - start) * 1000)
                health_report["services"]["batch_operations"] = {
                    "available": True,
                    "note": "Endpoint accessible (validation working)",
                    "latency_ms": latency
                }
                if ctx:
                    await ctx.info(f"  ✅ Batch Operations: OK (endpoint accessible)")
            else:
                health_report["services"]["batch_operations"] = {
                    "available": False,
                    "error": str(e)[:100]
                }
                if ctx:
                    await ctx.info(f"  ⚠️ Batch Operations: Unexpected error - {str(e)[:50]}")
        except HTTPStatusError as e:
            error_code = e.response.status_code
            latency = int((time.time() - start) * 1000)

            if error_code == 400:
                # 400 means endpoint is accessible, just bad input (empty array)
                health_report["services"]["batch_operations"] = {
                    "available": True,
                    "note": "Endpoint accessible (validation working)",
                    "latency_ms": latency
                }
                if ctx:
                    await ctx.info(f"  ✅ Batch Operations: OK (endpoint accessible)")
            elif error_code == 403:
                health_report["services"]["batch_operations"] = {
                    "available": False,
                    "error_code": error_code,
                    "note": "Advanced access required"
                }
                if ctx:
                    await ctx.info(f"  ℹ️ Batch Operations: Access denied (403) - requires advanced access")
            elif error_code == 503:
                health_report["services"]["batch_operations"] = {
                    "available": False,
                    "error_code": error_code,
                    "error": str(e)[:100]
                }
                if ctx:
                    await ctx.info(f"  ⚠️ Batch Operations: Service unavailable (503)")
            else:
                health_report["services"]["batch_operations"] = {
                    "available": False,
                    "error_code": error_code,
                    "error": str(e)[:100]
                }
                if ctx:
                    await ctx.info(f"  ⚠️ Batch Operations: FAILED ({error_code})")
        except Exception as e:
            health_report["services"]["batch_operations"] = {
                "available": False,
                "error": str(e)[:100]
            }
            if ctx:
                await ctx.info(f"  ⚠️ Batch Operations: FAILED - {str(e)[:50]}")

    # Calculate overall status
    critical_services = ["exchange", "authentication"]
    important_services = ["market_data", "order_management"]

    critical_down = any(
        not health_report["services"].get(s, {}).get("available", False)
        for s in critical_services
    )
    important_down = any(
        not health_report["services"].get(s, {}).get("available", False)
        for s in important_services
    )

    if critical_down:
        health_report["overall_status"] = "critical"
    elif important_down:
        health_report["overall_status"] = "degraded"
    else:
        health_report["overall_status"] = "healthy"

    if ctx:
        status_emoji = {
            "healthy": "✅",
            "degraded": "⚠️",
            "critical": "❌"
        }
        emoji = status_emoji.get(health_report["overall_status"], "❓")
        await ctx.info(f"\n{emoji} Overall Status: {health_report['overall_status'].upper()}")

        if health_report["overall_status"] == "degraded":
            await ctx.info("Some advanced features may be temporarily unavailable.")
        elif health_report["overall_status"] == "critical":
            await ctx.info("Critical services are down. Trading operations will fail.")

    return health_report


@mcp.tool
async def kalshi_search_markets(
    query: Annotated[
        str | None,
        Field(description="Text to search in market titles/subtitles (e.g., 'Bitcoin', 'election', 'Trump')")
    ] = None,
    limit: Annotated[
        int,
        Field(description="Maximum number of RESULTS to return (automatically fetches multiple pages if needed)", ge=1, le=1000)
    ] = 20,
    status: Annotated[
        str,
        Field(description="Filter by market status: 'open', 'closed', or 'settled'")
    ] = "open",
    ctx: Context | None = None,
) -> list[Market]:
    """
    Search for prediction markets on Kalshi by text query.

    **Pagination**: Automatically fetches multiple pages (100 items/page) to return up to
    the requested limit. For searches with queries, stops early once enough matches are found.

    **Text Search**: Kalshi's API has no native text search. This tool uses client-side
    filtering - fetches pages of markets and checks if your query appears in titles/subtitles.

    Args:
        query: Text to search for in market titles (case-insensitive, e.g., "Bitcoin", "election")
        limit: Maximum number of RESULTS to return (1-1000). Fetches multiple API pages automatically.
        status: Filter by status - "open" for active markets, "closed" for settled

    Returns:
        List of matching markets with prices, volume, and details

    Use this to discover markets about topics you're interested in.

    Examples:
        - Find Bitcoin markets: kalshi_search_markets("Bitcoin")
        - Get 200 open markets: kalshi_search_markets(limit=200)  # Fetches 2 pages automatically
        - Find settled election markets: kalshi_search_markets("election", status="settled")
        - Find Trump-related markets: kalshi_search_markets("Trump", limit=50)
    """
    if ctx:
        search_desc = f"'{query}'" if query else "all markets"
        if query:
            await ctx.info(f"Searching for {search_desc} (returning up to {limit} results, status={status})...")
            await ctx.info("Note: Using client-side text search (fetches pages until enough matches found)")
        else:
            pages_needed = (limit + 99) // 100  # Round up
            await ctx.info(f"Fetching {limit} {search_desc} (status={status}, ~{pages_needed} API pages)...")

    async with KalshiClient.from_env() as client:
        markets = await client.search_markets(query=query, limit=limit, status=status)

    if ctx:
        await ctx.info(f"Found {len(markets)} matching markets")
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
    order_group_id: Annotated[
        str | None,
        Field(description="Optional order group ID to associate order with (for OCO/bracket strategies)")
    ] = None,
    ctx: Context | None = None,
) -> Order:
    """
    Create a market order (executes immediately at current market price).

    Args:
        ticker: Market ticker symbol
        side: "yes" or "no"
        quantity: Number of contracts (1-MAX_ORDER_SIZE)
        action: "buy" or "sell" (default: "buy")
        order_group_id: Optional order group ID for linking orders (OCO strategies)

    Returns:
        Order details including fill information

    Market orders execute immediately at the best available price.
    Use this when you want immediate execution and don't need price control.

    **Order Groups**: Can be used with order groups for OCO (One-Cancels-Other) strategies.
    When any order in the group hits the contract limit, all other orders in the group
    are automatically canceled.

    Example:
        order = kalshi_create_market_order("KXBTC-31DEC-50K", "yes", 10)
        # Buys 10 YES contracts immediately at market price

        # With order group (OCO):
        order = kalshi_create_market_order("KXBTC-31DEC-50K", "yes", 10, order_group_id="group123")
    """
    # Validate order size
    if quantity > MAX_ORDER_SIZE:
        raise ValueError(f"Order size {quantity} exceeds maximum {MAX_ORDER_SIZE}")

    if ctx:
        if quantity > LARGE_ORDER_THRESHOLD:
            await ctx.info(f"⚠️ Large order: {quantity} contracts")
        order_msg = f"Creating market order: {action.upper()} {quantity}x {side.upper()} on {ticker}"
        if order_group_id:
            order_msg += f" (group: {order_group_id})"
        await ctx.info(order_msg)

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
            order_type="market",
            order_group_id=order_group_id
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
    order_group_id: Annotated[
        str | None,
        Field(description="Optional order group ID to associate order with (for OCO/bracket strategies)")
    ] = None,
    time_in_force: Annotated[
        str | None,
        Field(description="Time-in-force: 'fok' (Fill-or-Kill), 'ioc' (Immediate-or-Cancel), 'gtc' (Good-til-Cancel), or 'gtt' (Good-til-Time)")
    ] = None,
    expiration_ts: Annotated[
        int | None,
        Field(description="Unix timestamp for order expiration (required if time_in_force='gtt')")
    ] = None,
    post_only: Annotated[
        bool | None,
        Field(description="If True, order will only be accepted as maker order (no immediate fill)")
    ] = None,
    reduce_only: Annotated[
        bool | None,
        Field(description="If True, order will only reduce existing position, not increase it")
    ] = None,
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
        order_group_id: Optional order group ID (for OCO/bracket strategies)
        time_in_force: Optional time-in-force ("fok", "ioc", "gtc", or "gtt")
        expiration_ts: Optional expiration timestamp (required if time_in_force="gtt")
        post_only: If True, only accept as maker order
        reduce_only: If True, only reduce position (don't increase)

    Returns:
        Order details including resting order information

    Limit orders only execute at your specified price or better.
    The order will rest on the orderbook until filled or canceled.

    Advanced Features:
    - **Order Groups**: Link orders with contract limits for OCO behavior
    - **Time-in-Force**: Control how long order stays active
    - **Post-only**: Ensure you're always the maker (get maker rebates)
    - **Reduce-only**: Risk management, prevent position increases

    Example:
        order = kalshi_create_limit_order("KXBTC-31DEC-50K", "yes", 10, 45)
        # Buys 10 YES contracts only if price is 45¢ or less

        # With order group for OCO
        order = kalshi_create_limit_order(
            "KXBTC-31DEC-50K", "yes", 10, 45,
            order_group_id="group_123", post_only=True
        )
    """
    # Validate order size
    if quantity > MAX_ORDER_SIZE:
        raise ValueError(f"Order size {quantity} exceeds maximum {MAX_ORDER_SIZE}")

    if ctx:
        if quantity > LARGE_ORDER_THRESHOLD:
            await ctx.info(f"⚠️ Large order: {quantity} contracts")
        order_desc = f"Creating limit order: {action.upper()} {quantity}x {side.upper()} on {ticker} @ {price}¢"
        if order_group_id:
            order_desc += f" (group: {order_group_id})"
        await ctx.info(order_desc)

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

        # Add optional advanced parameters
        if order_group_id:
            kwargs["order_group_id"] = order_group_id
        if time_in_force:
            kwargs["time_in_force"] = time_in_force
        if expiration_ts:
            kwargs["expiration_ts"] = expiration_ts
        if post_only is not None:
            kwargs["post_only"] = post_only
        if reduce_only is not None:
            kwargs["reduce_only"] = reduce_only

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
# BATCH OPERATIONS
# ============================================================================


@mcp.tool
async def kalshi_batch_create_orders(
    orders: Annotated[
        list[dict],
        Field(description="List of order specifications (max 20 orders). Each order should have: ticker, type, action, side, count, yes_price/no_price (for limit orders)")
    ],
    ctx: Context | None = None,
) -> list[BatchOrderResponse]:
    """
    Create multiple orders in a single batch request (up to 20 orders).

    **Advanced Access Required**: This feature requires advanced access from Kalshi.
    If you don't have access, you'll receive a 403 error.

    Args:
        orders: List of order specifications (max 20)
            Each order dict should contain:
            - ticker: Market ticker symbol
            - type: "market" or "limit"
            - action: "buy" or "sell"
            - side: "yes" or "no"
            - count: Number of contracts
            - client_order_id: Optional tracking ID
            - yes_price or no_price: Limit price in cents (for limit orders)

    Returns:
        List of batch order responses, one per order.
        Each response contains either a successful Order or an error.

    Use this for:
    - Portfolio rebalancing across multiple markets
    - Simultaneous entry/exit across related positions
    - Multi-leg trading strategies

    Example:
        orders = [
            {"ticker": "KXBTC-31DEC-50K", "type": "limit", "action": "buy",
             "side": "yes", "count": 10, "yes_price": 42},
            {"ticker": "KXETH-31DEC-5K", "type": "limit", "action": "buy",
             "side": "yes", "count": 5, "yes_price": 35}
        ]
        results = kalshi_batch_create_orders(orders)
        # Process results - some may succeed, some may fail
    """
    if len(orders) > 20:
        raise ValueError(f"Batch size {len(orders)} exceeds maximum of 20 orders")

    if ctx:
        await ctx.info(f"Creating batch of {len(orders)} orders...")
        await ctx.info("⚠️ Note: Batch operations require advanced access from Kalshi")

    try:
        async with KalshiClient.from_env() as client:
            responses = await client.batch_create_orders(orders)

        if ctx:
            successful = sum(1 for r in responses if r.is_success)
            failed = len(responses) - successful
            await ctx.info(f"✅ Batch complete: {successful} succeeded, {failed} failed")

            # Show details of failed orders
            if failed > 0:
                for i, resp in enumerate(responses):
                    if not resp.is_success:
                        await ctx.info(f"❌ Order {i+1} failed: {resp.error_message}")

        return responses

    except Exception as e:
        if "403" in str(e) or "Forbidden" in str(e):
            error_msg = (
                "⚠️ Batch operations require advanced access from Kalshi. "
                "Contact Kalshi support to enable this feature for your account."
            )
            if ctx:
                await ctx.info(error_msg)
            raise ValueError(error_msg) from e
        raise


@mcp.tool
async def kalshi_batch_cancel_orders(
    order_ids: Annotated[
        list[str],
        Field(description="List of order IDs to cancel (max 20 orders)")
    ],
    ctx: Context | None = None,
) -> list[dict]:
    """
    Cancel multiple orders in a single batch request (up to 20 orders).

    **Advanced Access Required**: This feature requires advanced access from Kalshi.
    If you don't have access, you'll receive a 403 error.

    Args:
        order_ids: List of order IDs to cancel (max 20)

    Returns:
        List of cancellation results

    Use this for:
    - Quickly closing out multiple positions
    - Canceling stale orders across markets
    - Risk management (cancel all orders quickly)

    Example:
        order_ids = [
            "01234567-89ab-cdef-0123-456789abcdef",
            "abcdef01-2345-6789-abcd-ef0123456789"
        ]
        results = kalshi_batch_cancel_orders(order_ids)
    """
    if len(order_ids) > 20:
        raise ValueError(f"Batch size {len(order_ids)} exceeds maximum of 20 orders")

    if ctx:
        await ctx.info(f"Canceling batch of {len(order_ids)} orders...")
        await ctx.info("⚠️ Note: Batch operations require advanced access from Kalshi")

    try:
        async with KalshiClient.from_env() as client:
            results = await client.batch_cancel_orders(order_ids)

        if ctx:
            await ctx.info(f"✅ Batch cancel complete: {len(order_ids)} orders processed")

        return results

    except Exception as e:
        if "403" in str(e) or "Forbidden" in str(e):
            error_msg = (
                "⚠️ Batch operations require advanced access from Kalshi. "
                "Contact Kalshi support to enable this feature for your account."
            )
            if ctx:
                await ctx.info(error_msg)
            raise ValueError(error_msg) from e
        raise


# ============================================================================
# ORDER GROUPS
# ============================================================================


@mcp.tool
async def kalshi_create_order_group(
    contracts_limit: Annotated[
        int,
        Field(description="Maximum contracts that can be filled across all orders in group", ge=1)
    ],
    ctx: Context | None = None,
) -> OrderGroup:
    """
    Create an order group with a contract limit.

    Order groups allow you to link multiple orders with a shared contract limit.
    When the limit is reached, all remaining orders in the group are automatically canceled.

    Args:
        contracts_limit: Maximum contracts that can be filled (minimum: 1)

    Returns:
        OrderGroup details including group ID

    Use this for:
    - OCO (One-Cancels-Other) strategies
    - Risk-limited multi-market positions
    - Bracket-style orders (entry + stop + target)

    Example:
        # Create group with 100 contract limit
        group = kalshi_create_order_group(contracts_limit=100)

        # Place multiple orders in the group
        # When 100 contracts fill across all orders, rest are canceled
    """
    if ctx:
        await ctx.info(f"Creating order group with {contracts_limit} contract limit...")

    async with KalshiClient.from_env() as client:
        group = await client.create_order_group(contracts_limit)

    if ctx:
        await ctx.info(f"✅ Order group created: {group.order_group_id}")
        await ctx.info(
            f"   Note: Kalshi API doesn't return contracts_limit in response. "
            f"Track it client-side if needed."
        )

    return group


@mcp.tool
async def kalshi_get_order_group(
    group_id: Annotated[
        str,
        Field(description="Order group ID")
    ],
    ctx: Context | None = None,
) -> OrderGroup:
    """
    Get order group details.

    Args:
        group_id: Order group ID

    Returns:
        OrderGroup details (limited info - API doesn't return much)

    Note: The Kalshi API has limited data for order groups. It returns:
    - is_auto_cancel_enabled: Whether auto-cancel is enabled
    - orders: List of order IDs in the group

    The API does NOT return contracts_limit or contracts_filled, making it
    impossible to track progress toward the limit.

    Example:
        group = kalshi_get_order_group("group_123abc")
        print(f"Auto-cancel enabled: {group.is_auto_cancel_enabled}")
        print(f"Orders in group: {len(group.orders or [])}")
    """
    if ctx:
        await ctx.info(f"Fetching order group: {group_id}")

    async with KalshiClient.from_env() as client:
        group = await client.get_order_group(group_id)

    if ctx:
        await ctx.info(f"Order group: {group.order_group_id}")
        await ctx.info(f"   Auto-cancel enabled: {group.is_auto_cancel_enabled}")
        await ctx.info(f"   Orders in group: {len(group.orders or [])}")

    return group


@mcp.tool
async def kalshi_get_order_groups(
    limit: Annotated[
        int,
        Field(description="Maximum number of RESULTS to return (automatically fetches multiple pages if needed)", ge=1, le=1000)
    ] = 100,
    ctx: Context | None = None,
) -> list[OrderGroup]:
    """
    Get list of order groups.

    **Pagination**: Automatically fetches multiple pages (100 items/page) to return up to
    the requested limit.

    Args:
        limit: Maximum number of RESULTS to return (1-1000). Fetches multiple API pages automatically.

    Returns:
        List of order groups (limited info - API doesn't return much)

    Note: Each group contains:
    - id or order_group_id: The group identifier
    - is_auto_cancel_enabled: Whether auto-cancel is enabled

    The API does NOT return contracts_limit or contracts_filled.

    Example:
        groups = kalshi_get_order_groups(limit=50)
        for group in groups:
            print(f"Group {group.group_id}: auto-cancel={group.is_auto_cancel_enabled}")
    """
    if ctx:
        pages_needed = (limit + 99) // 100
        await ctx.info(f"Fetching {limit} order groups (~{pages_needed} API pages)...")

    async with KalshiClient.from_env() as client:
        groups = await client.get_order_groups(limit=limit)

    if ctx:
        if groups:
            await ctx.info(f"Found {len(groups)} order group(s)")
            # Show top 3 groups
            for i, group in enumerate(groups[:3], 1):
                await ctx.info(
                    f"{i}. Group {group.group_id}: "
                    f"auto-cancel={group.is_auto_cancel_enabled}"
                )
        else:
            await ctx.info("No order groups found")

    return groups


@mcp.tool
async def kalshi_reset_order_group(
    group_id: Annotated[
        str,
        Field(description="Order group ID to reset")
    ],
    ctx: Context | None = None,
) -> OrderGroup:
    """
    Reset an order group.

    Resetting a group:
    - Resets the group state (API-specific behavior)
    - Allows new orders to be placed in the group
    - Does NOT cancel existing orders

    Args:
        group_id: Order group ID

    Returns:
        Updated OrderGroup details

    Note: The exact effect of resetting is API-defined. The API doesn't return
    contracts_filled or contracts_limit, so progress tracking must be done client-side.

    Example:
        group = kalshi_reset_order_group("group_123abc")
    """
    if ctx:
        await ctx.info(f"Resetting order group: {group_id}")

    async with KalshiClient.from_env() as client:
        group = await client.reset_order_group(group_id)

    if ctx:
        await ctx.info(f"✅ Order group reset: {group.order_group_id}")

    return group


@mcp.tool
async def kalshi_delete_order_group(
    group_id: Annotated[
        str,
        Field(description="Order group ID to delete")
    ],
    ctx: Context | None = None,
) -> dict:
    """
    Delete an order group.

    **Warning**: This cancels all active orders in the group!

    Args:
        group_id: Order group ID

    Returns:
        Confirmation message

    Use this when:
    - You want to exit a strategy completely
    - Need to cancel all orders in a group at once
    - Cleaning up old/unused groups

    Example:
        result = kalshi_delete_order_group("group_123abc")
        # All orders in group are now canceled
    """
    if ctx:
        await ctx.info(f"Deleting order group: {group_id}")
        await ctx.info("⚠️  Warning: This will cancel all active orders in the group")

    async with KalshiClient.from_env() as client:
        await client.delete_order_group(group_id)

    if ctx:
        await ctx.info(f"✅ Order group deleted: {group_id}")

    return {"status": "deleted", "group_id": group_id}


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
        Field(description="Maximum number of RESULTS to return (automatically fetches multiple pages if needed)", ge=1, le=1000)
    ] = 100,
    ctx: Context | None = None,
) -> list[Position]:
    """
    Get current portfolio positions.

    **Pagination**: Automatically fetches multiple pages (100 items/page) to return up to
    the requested limit.

    Args:
        ticker: Filter by ticker (optional)
        limit: Maximum number of RESULTS to return (1-1000). Fetches multiple API pages automatically.

    Returns:
        List of current positions with P&L information

    Shows your current holdings across all markets or filtered by ticker.
    Includes realized and unrealized P&L, position size, and market exposure.

    Example:
        positions = kalshi_get_positions()
        # Returns all current positions with P&L

        positions = kalshi_get_positions(limit=400)  # Fetches 4 pages automatically
    """
    if ctx:
        filter_desc = f" for {ticker}" if ticker else ""
        pages_needed = (limit + 99) // 100  # Round up
        await ctx.info(f"Fetching {limit} positions{filter_desc} (~{pages_needed} API pages)...")

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
        Field(description="Maximum number of RESULTS to return (automatically fetches multiple pages if needed)", ge=1, le=1000)
    ] = 100,
    ctx: Context | None = None,
) -> list[Fill]:
    """
    Get trade execution history (fills).

    **Pagination**: Automatically fetches multiple pages (100 items/page) to return up to
    the requested limit.

    Args:
        ticker: Filter by ticker (optional)
        order_id: Filter by order ID (optional)
        limit: Maximum number of RESULTS to return (1-1000). Fetches multiple API pages automatically.

    Returns:
        List of trade fills with prices and fees

    Shows your trade execution history - when orders were filled,
    at what price, and with what fees. Useful for tracking execution
    quality and analyzing trading costs.

    Example:
        fills = kalshi_get_fills(ticker="KXBTC-31DEC-50K")
        # Returns all fills for this market

        fills = kalshi_get_fills(limit=350)  # Fetches 4 pages automatically
    """
    if ctx:
        filters = []
        if ticker:
            filters.append(f"ticker={ticker}")
        if order_id:
            filters.append(f"order_id={order_id}")
        filter_desc = f" ({', '.join(filters)})" if filters else ""
        pages_needed = (limit + 99) // 100  # Round up
        await ctx.info(f"Fetching {limit} fill history{filter_desc} (~{pages_needed} API pages)...")

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
        Field(description="Maximum number of RESULTS to return (automatically fetches multiple pages if needed)", ge=1, le=1000)
    ] = 100,
    ctx: Context | None = None,
) -> list[Order]:
    """
    Get orders (active, filled, or canceled).

    **Pagination**: Automatically fetches multiple pages (100 items/page) to return up to
    the requested limit.

    Args:
        ticker: Filter by ticker (optional)
        status: Filter by status (default: "resting")
        limit: Maximum number of RESULTS to return (1-1000). Fetches multiple API pages automatically.

    Returns:
        List of orders matching filters

    Shows your orders across all markets or filtered by ticker and status.
    Use status="resting" for active orders, "filled" for completed orders,
    or "canceled" for canceled orders.

    Example:
        orders = kalshi_get_orders(status="resting")
        # Returns all active orders waiting to be filled

        orders = kalshi_get_orders(status="filled", limit=250)  # Fetches 3 pages automatically
    """
    if ctx:
        filter_desc = f" for {ticker}" if ticker else ""
        pages_needed = (limit + 99) // 100  # Round up
        await ctx.info(f"Fetching {limit} {status} orders{filter_desc} (~{pages_needed} API pages)...")

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
        Field(description="Maximum number of RESULTS to return (automatically fetches multiple pages if needed)", ge=1, le=1000)
    ] = 50,
    status: Annotated[
        str,
        Field(description="Filter by status: 'open', 'closed', 'settled'")
    ] = "open",
    ctx: Context | None = None,
) -> list[Event]:
    """
    Get list of prediction market events.

    **Pagination**: Automatically fetches multiple pages (100 items/page) to return up to
    the requested limit.

    Args:
        limit: Maximum number of RESULTS to return (1-1000). Fetches multiple API pages automatically.
        status: Filter by status (default: "open")

    Returns:
        List of events

    Events are collections of related markets. For example, an event
    might be "2024 Presidential Election" with multiple markets for
    different outcomes or timeframes.

    Example:
        events = kalshi_get_events(status="open", limit=20)
        # Returns active events with their markets

        events = kalshi_get_events(limit=500)  # Fetches 5 pages automatically
    """
    if ctx:
        pages_needed = (limit + 99) // 100  # Round up
        await ctx.info(f"Fetching {limit} {status} events (~{pages_needed} API pages)...")

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
        Field(description="Maximum number of RESULTS to return (automatically fetches multiple pages if needed)", ge=1, le=1000)
    ] = 100,
    ctx: Context | None = None,
) -> list[Trade]:
    """
    Get recent public trades (market activity).

    **Pagination**: Automatically fetches multiple pages (100 items/page) to return up to
    the requested limit.

    Args:
        ticker: Filter by market ticker (optional)
        limit: Maximum number of RESULTS to return (1-1000). Fetches multiple API pages automatically.

    Returns:
        List of recent trades with prices and volumes

    Shows recent trade flow - useful for understanding market
    momentum, execution prices, and trading activity patterns.

    Example:
        trades = kalshi_get_trades(ticker="KXBTC-31DEC-50K", limit=50)
        # Returns last 50 trades on this market

        trades = kalshi_get_trades(limit=300)  # Fetches 3 pages automatically
    """
    if ctx:
        filter_desc = f" for {ticker}" if ticker else ""
        pages_needed = (limit + 99) // 100  # Round up
        await ctx.info(f"Fetching {limit} recent trades{filter_desc} (~{pages_needed} API pages)...")

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
