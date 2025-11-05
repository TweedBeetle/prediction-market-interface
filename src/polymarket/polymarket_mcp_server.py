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
from .models import OrderSide, OrderParams, SignatureType

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


if __name__ == "__main__":
    mcp.run()
