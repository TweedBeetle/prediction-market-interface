"""
Polymarket MCP Server - FastMCP implementation.

Provides LLM-accessible tools for:
- Market discovery and research
- Order execution and management
- Portfolio tracking
- Authentication

Phase 1: 12 tools for core trading functionality
"""

from typing import Optional, List

from fastmcp import FastMCP, Context
from pydantic import Field
from loguru import logger

from .gamma_client import GammaClient
from .clob_client import ClobClient
from .models import OrderSide, OrderParams, OrderType, SignatureType

# Initialize FastMCP server
mcp = FastMCP(
    name="Polymarket Trading",
    instructions="""
Polymarket prediction market trading and research server.

**IMPORTANT:** Polymarket is a decentralized prediction market on Polygon blockchain.
- **Non-custodial**: You control your funds via wallet
- **Real money**: All trades use real USDC on Polygon
- **No testnet**: There is no demo environment (use small amounts for testing)

Use this server to:
- Research prediction markets on any topic
- Analyze odds and find trading opportunities
- Execute trades on blockchain-based markets
- Track portfolio performance

**Phase 1 Features** (12 tools):
- Authentication (get status, authenticate, check API key)
- Market discovery (search, get details, orderbook, trades, events)
- Order execution (create, cancel)
- Portfolio management (positions, order history)

**Phase 2 Features** (8 additional tools):
- Batch operations (create multiple orders, cancel multiple orders)
- Market orders (FOK/FAK for immediate execution)
- Advanced cancellation (cancel all, cancel by market)
- Position closing helpers
"""
)

# Global client instances (initialized from environment)
_gamma_client: Optional[GammaClient] = None
_clob_client: Optional[ClobClient] = None


def get_gamma_client() -> GammaClient:
    """Get or create Gamma client instance."""
    global _gamma_client
    if _gamma_client is None:
        _gamma_client = GammaClient.from_env()
    return _gamma_client


def get_clob_client() -> ClobClient:
    """Get or create CLOB client instance."""
    global _clob_client
    if _clob_client is None:
        _clob_client = ClobClient.from_env()
    return _clob_client


# ============================================================================
# AUTHENTICATION TOOLS (3 tools)
# ============================================================================

@mcp.tool
async def polymarket_get_api_status(ctx: Context = None) -> dict:
    """
    Check Polymarket API connectivity and status.

    Tests connection to both Gamma (market data) and CLOB (trading) APIs.

    Returns:
        Dictionary with API status for each service

    Example:
        status = await polymarket_get_api_status()
        # Returns: {"gamma_api": "connected", "clob_api": "requires_auth", ...}
    """
    if ctx:
        await ctx.info("Checking Polymarket API status...")

    status = {
        "gamma_api": "unknown",
        "clob_api": "unknown",
        "wallet_address": None,
    }

    # Test Gamma API (no auth required)
    try:
        async with GammaClient.from_env() as gamma:
            markets = await gamma.search_markets(limit=1)
            status["gamma_api"] = "connected"
            if ctx:
                await ctx.info("✓ Gamma API (market data) is accessible")
    except Exception as e:
        status["gamma_api"] = f"error: {str(e)}"
        if ctx:
            await ctx.error(f"✗ Gamma API error: {e}")

    # Test CLOB API (requires auth)
    try:
        clob = get_clob_client()
        status["wallet_address"] = clob.credentials.wallet_address

        if clob._api_key:
            status["clob_api"] = "authenticated"
            if ctx:
                await ctx.info(f"✓ CLOB API authenticated for {clob.credentials.wallet_address}")
        else:
            status["clob_api"] = "requires_authentication"
            if ctx:
                await ctx.info("⚠ CLOB API requires authentication (call polymarket_authenticate)")

    except Exception as e:
        status["clob_api"] = f"error: {str(e)}"
        if ctx:
            await ctx.error(f"✗ CLOB API error: {e}")

    return status


@mcp.tool
async def polymarket_authenticate(ctx: Context = None) -> dict:
    """
    Authenticate with Polymarket CLOB API.

    Uses EIP-712 signing to prove wallet ownership and obtain API credentials
    for trading operations. Required before placing or canceling orders.

    Returns:
        Dictionary with authentication status and wallet address

    Raises:
        AuthenticationError: If authentication fails

    Example:
        result = await polymarket_authenticate()
        # Returns: {"status": "authenticated", "wallet_address": "0x...", ...}
    """
    if ctx:
        await ctx.info("Authenticating with Polymarket CLOB API...")

    try:
        async with get_clob_client() as clob:
            credentials = await clob.authenticate()

            result = {
                "status": "authenticated",
                "wallet_address": clob.credentials.wallet_address,
                "api_key": credentials["apiKey"][:8] + "...",  # Redacted
                "message": "Successfully authenticated. You can now place and cancel orders.",
            }

            if ctx:
                await ctx.info(f"✓ Authenticated as {clob.credentials.wallet_address}")

            return result

    except Exception as e:
        logger.error(f"Authentication failed: {e}")
        if ctx:
            await ctx.error(f"Authentication failed: {e}")
        raise


@mcp.tool
async def polymarket_get_api_key(ctx: Context = None) -> dict:
    """
    Get current API key status and wallet information.

    Returns information about the currently configured wallet and
    whether API credentials have been obtained.

    Returns:
        Dictionary with wallet address and API key status

    Example:
        info = await polymarket_get_api_key()
        # Returns: {"wallet_address": "0x...", "has_api_key": true, ...}
    """
    if ctx:
        await ctx.info("Checking API key status...")

    clob = get_clob_client()

    result = {
        "wallet_address": clob.credentials.wallet_address,
        "chain_id": clob.credentials.chain_id,
        "has_api_key": clob._api_key is not None,
        "authenticated": clob._api_key is not None,
    }

    if ctx:
        if result["authenticated"]:
            await ctx.info(f"✓ Authenticated as {result['wallet_address']}")
        else:
            await ctx.info(f"⚠ Not authenticated. Call polymarket_authenticate() to authenticate.")

    return result


# ============================================================================
# MARKET DISCOVERY TOOLS (5 tools)
# ============================================================================

@mcp.tool
async def polymarket_search_markets(
    query: str = Field(default="", description="Search query (searches title and description)"),
    active: bool = Field(default=True, description="Include active markets"),
    closed: bool = Field(default=False, description="Include closed markets"),
    limit: int = Field(default=20, ge=1, le=100, description="Maximum number of results"),
    ctx: Context = None
) -> List[dict]:
    """
    Search for prediction markets on Polymarket.

    Searches market titles and descriptions for the given query.
    Returns detailed market information including current prices,
    volume, and outcome tokens.

    Args:
        query: Search query (e.g., "election", "Bitcoin", "Trump")
        active: Include active/tradeable markets
        closed: Include closed/settled markets
        limit: Maximum number of results (1-100)

    Returns:
        List of matching markets with prices, volume, and metadata

    Example:
        markets = await polymarket_search_markets("election", limit=5)
        # Returns list of election-related markets with current odds
    """
    if ctx:
        await ctx.info(f"Searching for markets matching '{query}'...")

    try:
        async with get_gamma_client() as gamma:
            markets = await gamma.search_markets(
                query=query if query else None,
                active=active,
                closed=closed,
                limit=limit
            )

            # Convert to dict for JSON serialization
            results = [market.model_dump() for market in markets]

            if ctx:
                await ctx.info(f"Found {len(results)} markets")
                if results:
                    # Show top 3 market summaries
                    for i, market in enumerate(markets[:3]):
                        await ctx.info(f"{i+1}. {market.interpretation}")

            return results

    except Exception as e:
        logger.error(f"Market search failed: {e}")
        if ctx:
            await ctx.error(f"Search failed: {e}")
        raise


@mcp.tool
async def polymarket_get_market(
    market_id: str = Field(..., description="Market ID or condition ID"),
    ctx: Context = None
) -> dict:
    """
    Get detailed information about a specific market.

    Returns comprehensive market data including:
    - Current prices (bid, ask, last)
    - Volume and liquidity
    - Token IDs for trading
    - Market status and metadata

    Args:
        market_id: Market ID or condition ID

    Returns:
        Market data with prices, volume, and token IDs

    Raises:
        MarketNotFoundError: If market doesn't exist

    Example:
        market = await polymarket_get_market("12345")
        # Returns full market details including YES/NO token IDs
    """
    if ctx:
        await ctx.info(f"Fetching market {market_id}...")

    try:
        async with get_gamma_client() as gamma:
            market = await gamma.get_market(market_id)

            if ctx:
                await ctx.info(f"Market: {market.interpretation}")
                if market.best_bid and market.best_ask:
                    await ctx.info(f"Prices: Bid {market.best_bid:.3f} / Ask {market.best_ask:.3f}")
                if market.volume_24h:
                    await ctx.info(f"24h volume: ${market.volume_24h:,.2f}")

            return market.model_dump()

    except Exception as e:
        logger.error(f"Failed to get market {market_id}: {e}")
        if ctx:
            await ctx.error(f"Failed to get market: {e}")
        raise


@mcp.tool
async def polymarket_get_orderbook(
    token_id: str = Field(..., description="Token ID (YES or NO outcome)"),
    ctx: Context = None
) -> dict:
    """
    Get order book snapshot for a market outcome.

    Returns current bids and asks with price and size at each level.
    Useful for analyzing liquidity and finding best execution prices.

    Args:
        token_id: Token ID for the outcome (get from market data)

    Returns:
        Order book with bids and asks sorted by price

    Example:
        orderbook = await polymarket_get_orderbook("token_id_here")
        # Returns: {"bids": [...], "asks": [...], "spread": 0.05, ...}
    """
    if ctx:
        await ctx.info(f"Fetching orderbook for token {token_id}...")

    try:
        async with get_gamma_client() as gamma:
            orderbook = await gamma.get_orderbook(token_id)

            if ctx:
                if orderbook.best_bid and orderbook.best_ask:
                    await ctx.info(
                        f"Best Bid: {orderbook.best_bid.price:.3f} ({orderbook.best_bid.size:.0f}) | "
                        f"Best Ask: {orderbook.best_ask.price:.3f} ({orderbook.best_ask.size:.0f})"
                    )
                    await ctx.info(f"Spread: {orderbook.spread:.3f}")
                else:
                    await ctx.info("⚠ Order book is empty")

            return orderbook.model_dump()

    except Exception as e:
        logger.error(f"Failed to get orderbook: {e}")
        if ctx:
            await ctx.error(f"Failed to get orderbook: {e}")
        raise


@mcp.tool
async def polymarket_get_market_trades(
    market_id: str = Field(default=None, description="Filter by market ID (condition ID)"),
    limit: int = Field(default=100, ge=1, le=500, description="Maximum number of trades"),
    ctx: Context = None
) -> List[dict]:
    """
    Get your trade history for a market.

    **REQUIRES AUTHENTICATION**: You must authenticate first via polymarket_authenticate().

    Returns your trade history with prices, sizes, and timestamps.
    Useful for analyzing your trading activity and P&L.

    Args:
        market_id: Filter by specific market (condition ID)
        limit: Maximum trades to return (1-500)

    Returns:
        List of your recent trades with execution details

    Raises:
        AuthenticationError: If not authenticated

    Example:
        # First authenticate
        await polymarket_authenticate()

        # Then get trades
        trades = await polymarket_get_market_trades(market_id="0x...", limit=50)
        # Returns list of your trades
    """
    if ctx:
        await ctx.info(f"Fetching your trade history (limit={limit})...")

    try:
        async with get_clob_client() as clob:
            trades = await clob.get_trades(
                market_id=market_id,
                limit=limit
            )

            results = [trade.model_dump() for trade in trades]

            if ctx:
                if trades:
                    await ctx.info(f"Retrieved {len(results)} trades")
                    # Show most recent trade
                    latest = trades[0]
                    await ctx.info(
                        f"Latest: {latest.side.value} {latest.size:.0f} @ {latest.price:.3f}"
                    )
                else:
                    await ctx.info("No trades found for your account")

            return results

    except Exception as e:
        logger.error(f"Failed to get trades: {e}")
        if ctx:
            await ctx.error(f"Failed to get trades: {e}")
        raise


@mcp.tool
async def polymarket_list_events(
    active: bool = Field(default=True, description="Include active events"),
    closed: bool = Field(default=False, description="Include closed events"),
    limit: int = Field(default=20, ge=1, le=100, description="Maximum number of events"),
    ctx: Context = None
) -> List[dict]:
    """
    List events (collections of related markets).

    Events group related markets together. For example, "2024 Presidential
    Election" would contain markets for different candidates and outcomes.

    Args:
        active: Include active events
        closed: Include closed/resolved events
        limit: Maximum events to return (1-100)

    Returns:
        List of events with associated markets

    Example:
        events = await polymarket_list_events(limit=10)
        # Returns list of events with market counts
    """
    if ctx:
        await ctx.info(f"Fetching events (limit={limit})...")

    try:
        async with get_gamma_client() as gamma:
            events = await gamma.get_events(
                active=active,
                closed=closed,
                limit=limit
            )

            results = [event.model_dump() for event in events]

            if ctx:
                await ctx.info(f"Retrieved {len(results)} events")
                if events:
                    for i, event in enumerate(events[:3]):
                        await ctx.info(f"{i+1}. {event.title} ({event.market_count} markets)")

            return results

    except Exception as e:
        logger.error(f"Failed to get events: {e}")
        if ctx:
            await ctx.error(f"Failed to get events: {e}")
        raise


# ============================================================================
# ORDER EXECUTION TOOLS (2 tools)
# ============================================================================

@mcp.tool
async def polymarket_create_order(
    token_id: str = Field(..., description="Token ID to trade (YES or NO outcome)"),
    side: str = Field(..., description="Order side: 'BUY' or 'SELL'"),
    price: float = Field(..., ge=0.001, le=0.999, description="Price between 0.001 and 0.999"),
    size: float = Field(..., gt=0, description="Order size in outcome tokens"),
    ctx: Context = None
) -> dict:
    """
    Create a new order on Polymarket.

    Places a limit order to buy or sell outcome tokens at a specified price.
    Requires prior authentication via polymarket_authenticate().

    **IMPORTANT:**
    - This uses real money (USDC on Polygon)
    - Ensure you have sufficient balance in your wallet
    - Orders are blockchain transactions and irreversible once filled

    Args:
        token_id: Token ID to trade (get from market data)
        side: 'BUY' or 'SELL'
        price: Price as decimal (0.65 = 65% probability = 65 cents)
        size: Number of outcome tokens to trade

    Returns:
        Order details with ID, status, and fill information

    Raises:
        OrderError: If order placement fails
        AuthenticationError: If not authenticated

    Example:
        order = await polymarket_create_order(
            token_id="token_id_here",
            side="BUY",
            price=0.65,
            size=10
        )
        # Returns order details with order_id
    """
    if ctx:
        await ctx.info(f"Creating order: {side} {size} @ {price} (token {token_id})...")

    try:
        async with get_clob_client() as clob:
            # Parse side
            order_side = OrderSide.BUY if side.upper() == "BUY" else OrderSide.SELL

            # Build order parameters
            order_params = OrderParams(
                token_id=token_id,
                price=price,
                size=size,
                side=order_side,
                maker=clob.credentials.wallet_address,
                signature_type=SignatureType.EOA,
            )

            # Create order
            order = await clob.create_order(order_params)

            if ctx:
                await ctx.info(f"✓ Order created: {order.order_id}")
                await ctx.info(f"Status: {order.status}")
                if order.size_matched > 0:
                    await ctx.info(f"Filled: {order.size_matched}/{order.size} ({order.fill_percentage:.1f}%)")

            return order.model_dump()

    except Exception as e:
        logger.error(f"Order creation failed: {e}")
        if ctx:
            await ctx.error(f"Order failed: {e}")
        raise


@mcp.tool
async def polymarket_cancel_order(
    order_id: str = Field(..., description="Order ID to cancel"),
    ctx: Context = None
) -> dict:
    """
    Cancel an existing order.

    Cancels a pending limit order that hasn't been fully filled.
    Filled portions of the order cannot be reversed.

    Args:
        order_id: Order ID to cancel (from create order response)

    Returns:
        Cancellation status

    Raises:
        OrderError: If cancellation fails

    Example:
        result = await polymarket_cancel_order("order_id_here")
        # Returns: {"status": "canceled", "order_id": "...", ...}
    """
    if ctx:
        await ctx.info(f"Canceling order {order_id}...")

    try:
        async with get_clob_client() as clob:
            result = await clob.cancel_order(order_id)

            if ctx:
                await ctx.info(f"✓ Order {order_id} canceled")

            return result

    except Exception as e:
        logger.error(f"Order cancellation failed: {e}")
        if ctx:
            await ctx.error(f"Cancellation failed: {e}")
        raise


# ============================================================================
# PORTFOLIO MANAGEMENT TOOLS (2 tools)
# ============================================================================

@mcp.tool
async def polymarket_get_positions(
    market_id: str = Field(default=None, description="Filter by market ID"),
    ctx: Context = None
) -> List[dict]:
    """
    Get current positions in all markets.

    Returns holdings across all markets with cost basis, current value,
    and unrealized P&L.

    Args:
        market_id: Optional filter for specific market

    Returns:
        List of positions with P&L calculations

    Example:
        positions = await polymarket_get_positions()
        # Returns list of current holdings with P&L
    """
    if ctx:
        await ctx.info("Fetching current positions...")

    try:
        async with get_clob_client() as clob:
            positions = await clob.get_positions(market_id=market_id)

            results = [pos.model_dump() for pos in positions]

            if ctx:
                if positions:
                    await ctx.info(f"Found {len(positions)} position(s)")

                    # Calculate total P&L
                    total_pnl = sum(p.unrealized_pnl or 0 for p in positions)
                    await ctx.info(f"Total unrealized P&L: ${total_pnl:,.2f}")

                    # Show top positions
                    for i, pos in enumerate(positions[:5]):
                        pnl_str = f"${pos.unrealized_pnl:,.2f}" if pos.unrealized_pnl else "N/A"
                        await ctx.info(
                            f"{i+1}. {pos.outcome} {pos.size:.0f} tokens | P&L: {pnl_str}"
                        )
                else:
                    await ctx.info("No open positions")

            return results

    except Exception as e:
        logger.error(f"Failed to get positions: {e}")
        if ctx:
            await ctx.error(f"Failed to get positions: {e}")
        raise


@mcp.tool
async def polymarket_get_order_history(
    market_id: str = Field(default=None, description="Filter by market ID"),
    status: str = Field(default=None, description="Filter by status (LIVE, MATCHED, CANCELLED)"),
    ctx: Context = None
) -> List[dict]:
    """
    Get order history and active orders.

    Returns all orders (active, filled, and canceled) with details
    about execution status.

    Args:
        market_id: Filter by specific market
        status: Filter by order status

    Returns:
        List of orders with status and fill details

    Example:
        orders = await polymarket_get_order_history(status="LIVE")
        # Returns list of active orders
    """
    if ctx:
        await ctx.info("Fetching order history...")

    try:
        async with get_clob_client() as clob:
            orders = await clob.get_orders(market_id=market_id, status=status)

            results = [order.model_dump() for order in orders]

            if ctx:
                if orders:
                    await ctx.info(f"Found {len(orders)} order(s)")

                    # Count by status
                    live = sum(1 for o in orders if o.status == "LIVE")
                    matched = sum(1 for o in orders if o.status == "MATCHED")
                    cancelled = sum(1 for o in orders if o.status == "CANCELLED")

                    await ctx.info(f"Status: {live} live, {matched} filled, {cancelled} canceled")

                    # Show recent orders
                    for i, order in enumerate(orders[:5]):
                        await ctx.info(
                            f"{i+1}. {order.side.value} {order.size:.0f} @ {order.price:.3f} "
                            f"({order.status})"
                        )
                else:
                    await ctx.info("No orders found")

            return results

    except Exception as e:
        logger.error(f"Failed to get order history: {e}")
        if ctx:
            await ctx.error(f"Failed to get order history: {e}")
        raise


# ============================================================================
# PHASE 2: BATCH OPERATIONS (3 tools)
# ============================================================================

@mcp.tool
async def polymarket_create_orders_batch(
    orders: List[dict] = Field(..., description="List of orders, each with: token_id, price, size, side, order_type"),
    ctx: Context = None,
) -> List[dict]:
    """
    Create multiple orders in a single request (up to 15 orders).

    **REQUIRES AUTHENTICATION** via polymarket_authenticate().
    ⚠️ **USES REAL MONEY** - Places actual orders on Polygon mainnet.

    Batch order creation is useful for:
    - Spread trading (buy and sell related markets simultaneously)
    - Portfolio rebalancing (close multiple positions at once)
    - OCO strategies (place conditional orders)
    - Efficiency (reduce API calls and latency)

    Args:
        orders: List of order dictionaries with fields:
            - token_id (str): Token ID to trade
            - price (float): Limit price (0.001-0.999)
            - size (float): Order size in contracts
            - side (str): "BUY" or "SELL"
            - order_type (str): "FOK", "FAK", "GTC", or "GTD"

    Returns:
        List of batch results with success status for each order

    Example:
        orders = [
            {"token_id": "123", "price": 0.55, "size": 10, "side": "BUY", "order_type": "GTC"},
            {"token_id": "456", "price": 0.45, "size": 10, "side": "SELL", "order_type": "GTC"}
        ]
        results = await polymarket_create_orders_batch(orders=orders)
    """
    if ctx:
        await ctx.info(f"Creating batch of {len(orders)} orders...")

    if len(orders) > 15:
        error_msg = f"Maximum 15 orders per batch, got {len(orders)}"
        if ctx:
            await ctx.error(error_msg)
        raise ValueError(error_msg)

    try:
        async with get_clob_client() as clob:
            # Parse orders
            order_tuples = []
            for i, order_dict in enumerate(orders):
                try:
                    order_params = OrderParams(
                        token_id=order_dict["token_id"],
                        price=float(order_dict["price"]),
                        size=float(order_dict["size"]),
                        side=OrderSide(order_dict["side"].upper()),
                    )
                    order_type = OrderType(order_dict.get("order_type", "GTC").upper())
                    order_tuples.append((order_params, order_type))

                    if ctx:
                        await ctx.info(
                            f"Order {i+1}: {order_params.side.value} {order_params.size} "
                            f"@ {order_params.price} ({order_type.value})"
                        )
                except Exception as e:
                    if ctx:
                        await ctx.error(f"Invalid order {i+1}: {e}")
                    raise ValueError(f"Invalid order {i+1}: {e}")

            # Create batch
            results = await clob.create_orders_batch(order_tuples)

            # Report results
            if ctx:
                success_count = sum(1 for r in results if r.success)
                await ctx.info(f"Batch complete: {success_count}/{len(results)} successful")

                for i, result in enumerate(results):
                    if result.success:
                        await ctx.info(
                            f"✓ Order {i+1}: {result.status} (ID: {result.order_id})"
                        )
                    else:
                        await ctx.error(f"✗ Order {i+1}: {result.error_msg}")

            return [
                {
                    "success": r.success,
                    "error_msg": r.error_msg,
                    "order_id": r.order_id,
                    "status": r.status,
                }
                for r in results
            ]

    except Exception as e:
        logger.error(f"Failed to create batch orders: {e}")
        if ctx:
            await ctx.error(f"Failed to create batch orders: {e}")
        raise


@mcp.tool
async def polymarket_cancel_orders_batch(
    order_ids: List[str] = Field(..., description="List of order IDs to cancel"),
    ctx: Context = None,
) -> dict:
    """
    Cancel multiple orders by their IDs.

    **REQUIRES AUTHENTICATION** via polymarket_authenticate().

    Useful for quickly exiting multiple positions or cleaning up
    old orders.

    Args:
        order_ids: List of order IDs to cancel

    Returns:
        Dictionary with:
        - canceled: List of successfully canceled order IDs
        - not_canceled: Map of order ID -> failure reason
        - success_count: Number of successful cancellations
        - failure_count: Number of failed cancellations

    Example:
        result = await polymarket_cancel_orders_batch(
            order_ids=["0x123...", "0x456...", "0x789..."]
        )
    """
    if ctx:
        await ctx.info(f"Canceling {len(order_ids)} order(s)...")

    try:
        async with get_clob_client() as clob:
            response = await clob.cancel_orders_batch(order_ids)

            if ctx:
                await ctx.info(
                    f"Canceled {response.success_count} order(s), "
                    f"{response.failure_count} failed"
                )

                for order_id in response.canceled[:5]:  # Show first 5
                    await ctx.info(f"✓ Canceled: {order_id[:16]}...")

                for order_id, reason in list(response.not_canceled.items())[:5]:
                    await ctx.error(f"✗ Failed {order_id[:16]}...: {reason}")

            return {
                "canceled": response.canceled,
                "not_canceled": response.not_canceled,
                "success_count": response.success_count,
                "failure_count": response.failure_count,
            }

    except Exception as e:
        logger.error(f"Failed to cancel orders batch: {e}")
        if ctx:
            await ctx.error(f"Failed to cancel orders batch: {e}")
        raise


@mcp.tool
async def polymarket_cancel_all_orders(ctx: Context = None) -> dict:
    """
    Cancel ALL active orders for the authenticated user.

    **REQUIRES AUTHENTICATION** via polymarket_authenticate().
    ⚠️ **WARNING**: This cancels ALL active orders. Use with caution!

    Useful for emergency exits or resetting your order book.

    Returns:
        Dictionary with:
        - canceled: List of successfully canceled order IDs
        - not_canceled: Map of order ID -> failure reason
        - success_count: Number of successful cancellations
        - failure_count: Number of failed cancellations

    Example:
        result = await polymarket_cancel_all_orders()
        # Cancels all active orders
    """
    if ctx:
        await ctx.warn("⚠️ Canceling ALL active orders...")

    try:
        async with get_clob_client() as clob:
            response = await clob.cancel_all_orders()

            if ctx:
                await ctx.info(
                    f"Canceled {response.success_count} order(s), "
                    f"{response.failure_count} failed"
                )

                if response.success_count > 0:
                    await ctx.info(f"✓ Successfully canceled {response.success_count} order(s)")

                if response.failure_count > 0:
                    await ctx.error(f"✗ Failed to cancel {response.failure_count} order(s)")

            return {
                "canceled": response.canceled,
                "not_canceled": response.not_canceled,
                "success_count": response.success_count,
                "failure_count": response.failure_count,
            }

    except Exception as e:
        logger.error(f"Failed to cancel all orders: {e}")
        if ctx:
            await ctx.error(f"Failed to cancel all orders: {e}")
        raise


# ============================================================================
# PHASE 2: MARKET ORDERS (2 tools)
# ============================================================================

@mcp.tool
async def polymarket_create_market_order(
    token_id: str = Field(..., description="Token ID to trade"),
    side: str = Field(..., description="Order side: BUY or SELL"),
    size: float = Field(..., description="Order size in contracts", gt=0),
    order_type: str = Field(default="FOK", description="Order type: FOK (fill-or-kill) or FAK (fill-and-kill)"),
    ctx: Context = None,
) -> dict:
    """
    Create a market order for immediate execution at best available price.

    **REQUIRES AUTHENTICATION** via polymarket_authenticate().
    ⚠️ **USES REAL MONEY** - Executes immediately with NO PRICE GUARANTEE.

    Market orders execute immediately against the current orderbook:
    - **FOK (Fill-Or-Kill)**: Execute fully and immediately, or cancel entirely
    - **FAK (Fill-And-Kill)**: Execute what's available immediately, cancel rest

    **RISK**: You get whatever price is available on the book. In illiquid
    markets, you may get unfavorable execution.

    Args:
        token_id: Token ID to trade
        side: "BUY" or "SELL"
        size: Order size in contracts
        order_type: "FOK" (default) or "FAK"

    Returns:
        Order details with execution status

    Example:
        order = await polymarket_create_market_order(
            token_id="123...",
            side="BUY",
            size=10,
            order_type="FOK"
        )
    """
    if ctx:
        await ctx.warn(f"⚠️ Creating MARKET order: {side} {size} ({order_type})")
        await ctx.warn("No price guarantee - will execute at best available price")

    try:
        # Validate order type
        if order_type.upper() not in ("FOK", "FAK"):
            raise ValueError(f"Market orders must be FOK or FAK, got {order_type}")

        async with get_clob_client() as clob:
            order = await clob.create_market_order(
                token_id=token_id,
                side=OrderSide(side.upper()),
                size=size,
                order_type=OrderType(order_type.upper()),
            )

            if ctx:
                await ctx.info(f"Market order created: {order.order_id}")
                await ctx.info(f"Status: {order.status}")
                await ctx.info(
                    f"Fill: {order.fill_percentage:.1f}% "
                    f"({order.size_matched}/{order.size})"
                )

            return order.model_dump()

    except Exception as e:
        logger.error(f"Failed to create market order: {e}")
        if ctx:
            await ctx.error(f"Failed to create market order: {e}")
        raise


@mcp.tool
async def polymarket_close_position(
    market_id: str = Field(..., description="Market ID to close position in"),
    ctx: Context = None,
) -> dict:
    """
    Close a position by creating an opposite-side market order.

    **REQUIRES AUTHENTICATION** via polymarket_authenticate().
    ⚠️ **USES REAL MONEY** - Creates market order to close position.

    This is a helper that:
    1. Gets your current position in the market
    2. Fetches current orderbook to find best price
    3. Creates opposite-side market order to close position
    4. Returns execution details

    Args:
        market_id: Market condition ID to close position in

    Returns:
        Dictionary with:
        - position: Original position details
        - order: Closing order details
        - success: Whether position was closed

    Example:
        result = await polymarket_close_position(market_id="0xabc...")
    """
    if ctx:
        await ctx.info(f"Closing position in market {market_id[:16]}...")

    try:
        async with get_clob_client() as clob:
            # Get positions for this market
            positions = await clob.get_positions(market_id=market_id)

            if not positions:
                if ctx:
                    await ctx.error("No position found in this market")
                return {"success": False, "error": "No position found"}

            position = positions[0]

            if ctx:
                await ctx.info(
                    f"Position: {position.outcome} {position.size} @ {position.entry_price:.3f}"
                )
                await ctx.info(f"Current P&L: ${position.pnl_dollars:.2f}")

            # Determine opposite side
            # If holding YES tokens (outcome="YES"), we SELL
            # If holding NO tokens (outcome="NO"), we SELL
            side = OrderSide.SELL  # We're always selling our position

            if ctx:
                await ctx.info(f"Creating closing order: {side.value} {position.size}")

            # Create market order to close
            order = await clob.create_market_order(
                token_id=position.token_id if hasattr(position, 'token_id') else "",
                side=side,
                size=abs(position.size),
                order_type=OrderType.FOK,
            )

            if ctx:
                await ctx.info(f"Closing order created: {order.order_id}")
                await ctx.info(f"Status: {order.status}")

                if order.is_filled:
                    await ctx.info("✓ Position closed successfully")
                else:
                    await ctx.warn("⚠️ Position may not be fully closed - check status")

            return {
                "success": order.is_filled,
                "position": position.model_dump(),
                "order": order.model_dump(),
            }

    except Exception as e:
        logger.error(f"Failed to close position: {e}")
        if ctx:
            await ctx.error(f"Failed to close position: {e}")
        raise


# ============================================================================
# PHASE 2: ADVANCED CANCELLATION (2 tools)
# ============================================================================

@mcp.tool
async def polymarket_cancel_market_orders(
    market_id: Optional[str] = Field(None, description="Market condition ID to cancel orders for"),
    token_id: Optional[str] = Field(None, description="Token/asset ID to cancel orders for"),
    ctx: Context = None,
) -> dict:
    """
    Cancel all orders for a specific market or token.

    **REQUIRES AUTHENTICATION** via polymarket_authenticate().

    Useful for exiting a specific market while keeping other orders active.

    Args:
        market_id: Market condition ID (optional)
        token_id: Token/asset ID (optional)

    Note: Provide either market_id or token_id (or both)

    Returns:
        Dictionary with:
        - canceled: List of successfully canceled order IDs
        - not_canceled: Map of order ID -> failure reason
        - success_count: Number of successful cancellations
        - failure_count: Number of failed cancellations

    Example:
        result = await polymarket_cancel_market_orders(market_id="0xabc...")
    """
    if not market_id and not token_id:
        error_msg = "Must provide either market_id or token_id"
        if ctx:
            await ctx.error(error_msg)
        raise ValueError(error_msg)

    if ctx:
        filter_desc = f"market={market_id[:16] if market_id else 'None'}, token={token_id[:16] if token_id else 'None'}"
        await ctx.info(f"Canceling orders for {filter_desc}...")

    try:
        async with get_clob_client() as clob:
            response = await clob.cancel_market_orders(
                market_id=market_id,
                token_id=token_id,
            )

            if ctx:
                await ctx.info(
                    f"Canceled {response.success_count} order(s), "
                    f"{response.failure_count} failed"
                )

            return {
                "canceled": response.canceled,
                "not_canceled": response.not_canceled,
                "success_count": response.success_count,
                "failure_count": response.failure_count,
            }

    except Exception as e:
        logger.error(f"Failed to cancel market orders: {e}")
        if ctx:
            await ctx.error(f"Failed to cancel market orders: {e}")
        raise


@mcp.tool
async def polymarket_close_all_positions(ctx: Context = None) -> dict:
    """
    Close all open positions by creating market orders.

    **REQUIRES AUTHENTICATION** via polymarket_authenticate().
    ⚠️ **USES REAL MONEY** - Creates market orders for all positions.
    ⚠️ **WARNING**: This closes ALL positions. Use with caution!

    This helper:
    1. Gets all current positions
    2. For each position, creates closing market order
    3. Returns summary of closed positions

    Returns:
        Dictionary with:
        - total_positions: Number of positions to close
        - closed: List of successfully closed positions
        - failed: List of positions that failed to close
        - total_pnl: Total realized P&L

    Example:
        result = await polymarket_close_all_positions()
    """
    if ctx:
        await ctx.warn("⚠️ Closing ALL positions...")

    try:
        async with get_clob_client() as clob:
            # Get all positions
            positions = await clob.get_positions()

            if not positions:
                if ctx:
                    await ctx.info("No positions to close")
                return {
                    "total_positions": 0,
                    "closed": [],
                    "failed": [],
                    "total_pnl": 0.0,
                }

            if ctx:
                await ctx.info(f"Found {len(positions)} position(s) to close")

            # Close each position
            closed = []
            failed = []
            total_pnl = 0.0

            for position in positions:
                try:
                    if ctx:
                        await ctx.info(
                            f"Closing: {position.outcome} {position.size} @ "
                            f"{position.entry_price:.3f} (P&L: ${position.pnl_dollars:.2f})"
                        )

                    # Create closing order
                    order = await clob.create_market_order(
                        token_id=position.token_id if hasattr(position, 'token_id') else "",
                        side=OrderSide.SELL,
                        size=abs(position.size),
                        order_type=OrderType.FOK,
                    )

                    closed.append({
                        "market_id": position.market_id,
                        "size": position.size,
                        "pnl": position.pnl_dollars,
                        "order_id": order.order_id,
                    })

                    total_pnl += position.pnl_dollars or 0.0

                    if ctx:
                        await ctx.info(f"✓ Closed position (Order: {order.order_id})")

                except Exception as e:
                    logger.warning(f"Failed to close position: {e}")
                    failed.append({
                        "market_id": position.market_id,
                        "error": str(e),
                    })

                    if ctx:
                        await ctx.error(f"✗ Failed to close: {e}")

            if ctx:
                await ctx.info(
                    f"Summary: {len(closed)} closed, {len(failed)} failed, "
                    f"Total P&L: ${total_pnl:.2f}"
                )

            return {
                "total_positions": len(positions),
                "closed": closed,
                "failed": failed,
                "total_pnl": total_pnl,
            }

    except Exception as e:
        logger.error(f"Failed to close all positions: {e}")
        if ctx:
            await ctx.error(f"Failed to close all positions: {e}")
        raise


if __name__ == "__main__":
    mcp.run()
