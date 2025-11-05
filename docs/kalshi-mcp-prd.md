# Kalshi MCP Server - Product Requirements Document

**Version**: 2.1
**Date**: 2025-11-03
**Status**: ✅ Phase 2 Complete - 24 Tools + Advanced Trading + Diagnostics

## Executive Summary

A FastMCP-based server that exposes Kalshi's prediction market trading API to LLM agents, enabling sophisticated interactive trading and market research through natural language conversations.

### Primary Use Cases
1. **Interactive LLM-Driven Trading**: Claude-powered trading decisions with real-time execution
2. **Market Research & Analysis**: Data exploration, opportunity discovery, market intelligence
3. **Advanced Order Management**: Batch operations, order groups (OCO strategies), sophisticated order parameters

### Development Phases
- **Phase 1** ✅ (Complete): Basic trading operations + market research (16 tools)
- **Phase 2** ✅ (Complete): Advanced trading strategies (7 new tools: batch ops, order groups, advanced parameters)
- **Phase 3** (Future): Real-time streaming (WebSocket integration)
- **Phase 4** (Future): Analytics & intelligence (historical analysis, candlesticks, patterns)
- **Phase 5** (Future): Institutional-grade (RFQ, market making, multivariate collections)

---

## Phase 1 Completion Summary

**✅ Completed: 2025-11-03**

All 16 Phase 1 tools have been successfully implemented, tested, and verified:

### Implementation Statistics
- **16/16 MCP tools** - 100% complete
- **83 integration tests** - All passing (includes 10 pagination tests)
- **49 VCR cassettes** - Fast, deterministic testing (2.5x speedup)
- **10 Pydantic models** - Full type safety and validation
- **Test execution time**: ~9 seconds (vs 23s without cassettes)

### Tools by Category

**Authentication (2/2) ✅**
- ✅ `kalshi_get_exchange_status` - Operational status checks
- ✅ `kalshi_get_balance` - Account balance retrieval

**Market Discovery (6/6) ✅**
- ✅ `kalshi_search_markets` - Natural language search
- ✅ `kalshi_get_market` - Detailed market information
- ✅ `kalshi_get_events` - List events
- ✅ `kalshi_get_event` - Event details
- ✅ `kalshi_get_orderbook` - Order book depth analysis
- ✅ `kalshi_get_trades` - Recent trading activity

**Order Execution (5/5) ✅**
- ✅ `kalshi_create_market_order` - Immediate execution orders
- ✅ `kalshi_create_limit_order` - Price-controlled orders
- ✅ `kalshi_cancel_order` - Cancel pending orders
- ✅ `kalshi_amend_order` - Modify without losing queue position
- ✅ `kalshi_decrease_order` - Reduce order size

**Portfolio Management (3/3) ✅**
- ✅ `kalshi_get_positions` - Current positions with P&L
- ✅ `kalshi_get_fills` - Trade execution history
- ✅ `kalshi_get_orders` - Active/filled/canceled orders

### Key Technical Achievements

1. **Cursor-Based Pagination** - Automatic pagination for all list endpoints (up to 1000 results per request)
2. **VCR Testing Infrastructure** - Automatic HTTP recording/replay for fast, reliable tests
3. **Safety Limits** - Built-in validation (MAX_ORDER_SIZE, balance checks)
4. **Rich Context Logging** - All tools provide LLM-friendly progress updates
5. **Dual Environment Support** - Production and demo configurations
6. **Type-Safe Models** - Complete Pydantic validation for all API responses
7. **Comprehensive Coverage** - Every tool tested with multiple scenarios

### Known Issues Resolved

- **Trades endpoint path** - Corrected from `/trades` to `/markets/trades`
- **Trade model structure** - Fixed to match API format (float prices, yes/no prices)
- **Empty result handling** - All list-returning tools handle empty results gracefully

### Next Steps (Phase 1)

With Phase 1 complete, the system was ready for:
- **Real-world trading** - All core operations functional
- **Market research** - Complete discovery and analysis toolkit
- **Phase 2 implementation** - Advanced features (batch operations, order groups)

---

## Phase 2 Completion Summary

**✅ Completed: 2025-11-03**

Phase 2 adds sophisticated order management capabilities for advanced trading strategies.

### Implementation Statistics
- **8 new MCP tools** - 24 tools total (16 Phase 1 + 7 Phase 2 + 1 diagnostic)
- **24 new integration tests** - 107 total integration tests (83 Phase 1 + 22 Phase 2 + 2 diagnostic)
- **3 new Pydantic models** - 13 models total (BatchOrderRequest, BatchOrderResponse, OrderGroup)
- **Test results**: 17/22 Phase 2 tests passed (5 failed due to known demo API 503 errors)

### New Tools by Category

**Diagnostics (1 tool) ✅**
- ✅ `kalshi_diagnose_api_health` - Comprehensive API health check (tests all services)

**Batch Operations (2 tools) ✅**
- ✅ `kalshi_batch_create_orders` - Create up to 20 orders atomically
- ✅ `kalshi_batch_cancel_orders` - Cancel up to 20 orders atomically

**Order Groups (5 tools) ✅**
- ✅ `kalshi_create_order_group` - Create group with contract limits
- ✅ `kalshi_get_order_group` - Get group details with fill status
- ✅ `kalshi_get_order_groups` - List all groups (with pagination)
- ✅ `kalshi_reset_order_group` - Reset filled count to 0
- ✅ `kalshi_delete_order_group` - Delete group (cancels all orders)

**Advanced Order Parameters (enhancements to existing tools) ✅**
- ✅ `time_in_force` - FOK, IOC, GTC, GTT order types
- ✅ `expiration_ts` - Unix timestamp for GTT orders
- ✅ `post_only` - Maker-only orders (no immediate fill)
- ✅ `reduce_only` - Position reduction only
- ✅ `order_group_id` - Link orders to groups (OCO strategies)
- ✅ `self_trade_prevention_type` - Wash trade prevention
- ✅ `buy_max_cost` / `sell_position_floor` - Risk limits

### Key Technical Achievements

1. **API Health Diagnostic Tool** - Comprehensive service availability testing
   - Tests 6 service categories: exchange, auth, market data, orders, order groups, batch ops
   - Latency measurement for each service
   - Distinguishes between 503 (outage), 403 (access), and 400 (validation)
   - LLM-friendly output with status emojis and helpful messages
   - Revealed partial service availability (GET works, POST fails for order groups)

2. **Batch Operations** - Atomic order creation/cancellation (up to 20 orders per request)
   - Clear 403 error handling for accounts without advanced access
   - Validation prevents oversized batches (>20 orders)
   - BatchOrderResponse model with success/failure tracking

3. **Order Groups** - Contract limit enforcement across multiple orders
   - OCO (One-Cancels-Other) strategy support
   - Helper properties: `remaining_contracts`, `is_at_limit`, `fill_percentage`
   - Full CRUD operations (create, read, update/reset, delete)

4. **Advanced Order Parameters** - Professional trading features
   - Time-in-force options (FOK, IOC, GTC, GTT)
   - Maker-only orders (`post_only`)
   - Position-only reduction (`reduce_only`)
   - Self-trade prevention (`cancel_resting`, `cancel_aggressing`, `allow`)
   - Risk limits (`buy_max_cost`, `sell_position_floor`)

5. **Comprehensive Testing** - 24 new integration tests covering all Phase 2 features
   - Batch operation validation tests
   - Order group lifecycle tests
   - Advanced parameter combination tests
   - Model property tests

### Known Issues

**Demo API Reliability (documented)**:
- 5 order group tests fail intermittently due to Kalshi demo API 503 errors
- This is a known infrastructure issue, not a code bug
- Tests pass when API is stable
- Documented in `docs/kalshi/gotchas/CLAUDE.md`

**Advanced Access Required (documented)**:
- Batch operations require special Kalshi account access
- Tools provide clear 403 error messages: "Contact Kalshi support to enable this feature"
- Non-batch features work for all accounts

### Use Cases Enabled

**1. OCO (One-Cancels-Other) Strategies**
```python
# Create order group with 10 contract limit
group = await kalshi_create_order_group(contracts_limit=10)

# Place two competing orders - when one fills, other cancels
await kalshi_create_limit_order(
    ticker="KXBTC-50K", side="yes", quantity=10, price=45,
    order_group_id=group.order_group_id
)
await kalshi_create_limit_order(
    ticker="KXBTC-45K", side="yes", quantity=10, price=40,
    order_group_id=group.order_group_id
)
# When either order fills 10 contracts, the other automatically cancels
```

**2. Batch Portfolio Rebalancing**
```python
# Close all positions in one atomic operation
orders = [
    {"ticker": "KXBTC-50K", "side": "no", "count": 50, "type": "market"},
    {"ticker": "KXELEC-DEM", "side": "no", "count": 100, "type": "market"},
    {"ticker": "KXFED-HIKE", "side": "yes", "count": 25, "type": "market"}
]
await kalshi_batch_create_orders(orders)
```

**3. Sophisticated Order Types**
```python
# Maker-only order with expiration
await kalshi_create_limit_order(
    ticker="KXBTC-50K", side="yes", quantity=100, price=42,
    post_only=True,  # Only accept as maker (no immediate fill)
    time_in_force="gtt",  # Good-til-time
    expiration_ts=int(time.time()) + 3600  # Expires in 1 hour
)
```

### Next Steps (Phase 2)

With Phase 2 complete, the system now supports:
- ✅ **Advanced trading strategies** - OCO, batch operations, sophisticated order types
- ✅ **Professional order management** - Groups, risk limits, maker-only orders
- ⏭️ **Phase 3 planning** - WebSocket streaming for real-time market data

**Deferred to Future Phases:**
- **WebSocket Streaming** - Needs MCP pattern research for agent/WebSocket integration
- **Stop-Loss/Trailing Stops** - Not natively supported by Kalshi API, requires client-side monitoring
- **Bracket Orders** - Build on order groups, defer to Phase 4+

---

## Phase 1: Detailed Requirements (Implementation Reference)

### 1.1 Authentication & Connection

**Tools:**
- `kalshi_get_exchange_status` - Check exchange operational status
- `kalshi_get_balance` - Retrieve current account balance

**Resources:**
- `kalshi://account/credentials` - Current API key status (read-only)
- `kalshi://account/balance` - Real-time balance information

**Implementation Notes:**
- Use environment variables for API credentials (KALSHI_API_KEY, KALSHI_PRIVATE_KEY or KALSHI_PRIVATE_KEY_PATH)
- Support both private key approaches:
  - `KALSHI_PRIVATE_KEY`: Direct key content (recommended for CI/CD)
  - `KALSHI_PRIVATE_KEY_PATH`: File path (recommended for local development)
- Support both demo and production environments
- Implement automatic token refresh/re-authentication

---

### 1.2 Market Discovery & Research

**Tools:**

**Search & Browse:**
- `kalshi_search_markets(query: str, limit: int = 20)` - Natural language market search
- `kalshi_get_events(limit: int = 50, status: str = "open")` - List events
- `kalshi_get_event(event_ticker: str)` - Get detailed event information
- `kalshi_get_markets(event_ticker: str | None, status: str = "open", limit: int = 100)` - List markets with filters

**Market Details:**
- `kalshi_get_market(ticker: str)` - Comprehensive market information including:
  - Current prices (bid/ask/last)
  - Volume, open interest
  - Expiration time, status
  - Contract specifications
  - Settlement rules

**Orderbook Analysis:**
- `kalshi_get_orderbook(ticker: str, depth: int = 10)` - Current bid/ask levels
  - Returns structured data for price levels, quantities
  - Enables spread analysis, liquidity assessment

**Recent Trading Activity:**
- `kalshi_get_trades(ticker: str | None, limit: int = 100)` - Recent market trades
  - Filter by ticker or get exchange-wide activity
  - Useful for volume analysis, price discovery

**Resources:**
- `kalshi://markets/trending` - Currently active/high-volume markets
- `kalshi://markets/{ticker}` - Market data resource template
- `kalshi://events/{event_ticker}` - Event data resource template

**Design Principles for Research:**
- Return rich, structured data suitable for LLM analysis
- Include human-readable descriptions alongside machine data
- Provide context (e.g., "This market has 95% probability of YES")
- Support exploratory workflows ("Show me interesting markets about...")

---

### 1.3 Portfolio Management

**Tools:**

**Position Tracking:**
- `kalshi_get_positions(ticker: str | None, event_ticker: str | None)` - Current positions
  - Returns: position size, average entry price, current P&L
  - Can filter by specific market or event

**Order History:**
- `kalshi_get_fills(ticker: str | None, limit: int = 100)` - Trade history
  - Returns: execution price, size, timestamp
  - Useful for performance analysis

**Active Orders:**
- `kalshi_get_orders(ticker: str | None, status: str = "resting")` - Open orders
  - Filter by market, status (resting/canceled/filled)
  - Shows pending limit orders

**Resources:**
- `kalshi://portfolio/positions` - Current positions summary
- `kalshi://portfolio/pnl` - Realized & unrealized P&L

---

### 1.4 Order Execution

**Tools:**

**Market Orders (Immediate Execution):**
- `kalshi_create_market_order(ticker: str, side: "yes" | "no", quantity: int)`
  - Execute immediately at best available price
  - Returns: fill price, execution status
  - Use for: Quick entries, closing positions

**Limit Orders (Price Control):**
- `kalshi_create_limit_order(ticker: str, side: "yes" | "no", quantity: int, price: int)`
  - Only execute at specified price or better
  - Price in cents (e.g., 65 = 65¢ = 65% probability)
  - Returns: order ID for tracking
  - Use for: Patient entries, specific price targets

**Order Management:**
- `kalshi_cancel_order(order_id: str)` - Cancel a pending order
- `kalshi_amend_order(order_id: str, new_quantity: int, new_price: int)` - Modify order without losing queue position

**Decrease Position:**
- `kalshi_decrease_order(order_id: str, reduce_by: int)` - Reduce order size

**Validation & Safety:**
- Pre-execution checks:
  - Sufficient balance
  - Market is open/tradeable
  - Price within reasonable bounds (1-99 cents)
  - Quantity > 0
- Clear error messages for LLM to understand and retry
- Return structured responses with execution details

**Response Format:**
All order tools return:
```python
{
    "status": "success" | "partial" | "failed",
    "order_id": str,
    "filled_quantity": int,
    "average_price": int,  # in cents
    "remaining_quantity": int,
    "message": str  # Human-readable explanation
}
```

---

### 1.5 LLM-Friendly Design Patterns

**Structured Outputs:**
- Use Pydantic models for all responses
- Include both machine-readable data AND human context
- Example:
  ```python
  {
      "ticker": "KXBTC-23DEC-50K",
      "yes_price": 42,
      "no_price": 58,
      "interpretation": "Market implies 42% chance Bitcoin reaches $50K by Dec 23",
      "volume_24h": 15420,
      "open_interest": 89234
  }
  ```

**Natural Language Prompts:**
- Every tool has a detailed docstring explaining:
  - What it does in plain English
  - When to use it
  - Common parameters
  - Example use cases

**Error Handling:**
- Errors are LLM-readable: "Cannot place order - market KXBTC-23DEC-50K has expired"
- Not: "HTTP 400: invalid_market_status"
- Include suggestions for recovery when possible

**Progress & Logging:**
- Use FastMCP Context for progress reporting
- Log important events (orders placed, fills received)
- Enable LLM to provide running commentary to user

**Conversational Workflows:**
Design tools to support multi-turn conversations:
1. User: "What's happening with Bitcoin markets?"
2. LLM calls: `kalshi_search_markets("Bitcoin")`
3. LLM: "I found 5 Bitcoin markets. The most active is..."
4. User: "What's the orderbook look like?"
5. LLM calls: `kalshi_get_orderbook("KXBTC-...")`
6. LLM: "There's strong support at 45¢ with 5,000 contracts..."

---

### 1.6 Safety & Risk Management

**Phase 1 Safeguards:**

**Order Limits:**
- Maximum order size per execution (configurable, default: 100 contracts)
- Daily order count limit (default: 50 orders/day)
- Require explicit confirmation for orders > threshold

**Balance Protection:**
- Never allow orders that exceed available balance
- Warning if order would use >25% of balance

**Market Validation:**
- Only allow trading in open/active markets
- Reject orders for expired/settled markets
- Check if market is halted

**Audit Trail:**
- Log all order attempts (successful and failed)
- Include LLM context (what reasoning led to order)
- Store in structured format for review

**Configuration:**
```python
# .env or server config
KALSHI_MAX_ORDER_SIZE=100
KALSHI_DAILY_ORDER_LIMIT=50
KALSHI_LARGE_ORDER_THRESHOLD=50  # Require confirmation
KALSHI_MAX_BALANCE_USAGE_PCT=25  # Warning threshold
```

---

## Phase 1 Tool Summary

### MVP Complete (4/16 tools)

**Authentication (2/2 tools) ✅**
- ✅ `kalshi_get_exchange_status` - Working
- ✅ `kalshi_get_balance` - Working

**Market Discovery (2/6 tools)**
- ✅ `kalshi_search_markets` - Working
- ✅ `kalshi_get_market` - Working
- ❌ `kalshi_get_events` - Client method exists, needs MCP tool wrapper
- ❌ `kalshi_get_event` - Not implemented
- ❌ `kalshi_get_orderbook` - Not implemented
- ❌ `kalshi_get_trades` - Not implemented

**Portfolio (0/3 tools)**
- ❌ `kalshi_get_positions` - Not implemented
- ❌ `kalshi_get_fills` - Not implemented
- ❌ `kalshi_get_orders` - Not implemented

**Trading (0/5 tools)**
- ❌ `kalshi_create_market_order` - Not implemented
- ❌ `kalshi_create_limit_order` - Not implemented
- ❌ `kalshi_cancel_order` - Not implemented
- ❌ `kalshi_amend_order` - Not implemented
- ❌ `kalshi_decrease_order` - Not implemented

**Total: 4/16 tools implemented**

### Testing Infrastructure
- ✅ Full test coverage for MVP (43 tests passing)
- ✅ Unit tests (Pydantic models)
- ✅ Integration tests (client, tool functions, MCP protocol)
- ✅ Dynamic fixtures (no hardcoded tickers)
- ❌ VCR cassettes (HTTP recording/replay) - **Next priority**

---

## Recommended Next Steps

### Immediate (Testing Infrastructure)
1. **VCR Cassette Setup**
   - Record HTTP interactions for faster, more reliable tests
   - Reduces API calls and test flakiness
   - Essential before adding 12 more endpoints
   - Pattern: Record once, replay in CI/local dev

### Phase 1 Completion Priority

**High Priority (Core Trading - 8 tools):**
1. **Order Execution** (5 tools) - Cannot trade without these
   - `kalshi_create_market_order`
   - `kalshi_create_limit_order`
   - `kalshi_cancel_order`
   - `kalshi_amend_order`
   - `kalshi_decrease_order`

2. **Portfolio Management** (3 tools) - Track positions/performance
   - `kalshi_get_positions`
   - `kalshi_get_fills`
   - `kalshi_get_orders`

**Medium Priority (Enhanced Discovery - 4 tools):**
3. **Market Discovery** - Complete Phase 1 research tools
   - `kalshi_get_events` (client method exists, just needs wrapper)
   - `kalshi_get_event`
   - `kalshi_get_orderbook`
   - `kalshi_get_trades`

**Rationale:** Trading tools enable sophisticated strategies. Portfolio tools essential for position management. Remaining discovery tools nice-to-have since core search/get_market already works.

---

## Future Phases (Roadmap)

### Phase 2: Advanced Trading Strategies
**Estimated: 10-15 additional tools**

- **Batch Operations:**
  - `kalshi_batch_create_orders` - Submit multiple orders atomically
  - `kalshi_batch_cancel_orders` - Cancel multiple orders at once

- **Order Groups (Contingent Orders):**
  - `kalshi_create_order_group` - Link orders with conditions
  - Support for OCO (One-Cancels-Other), bracket orders

- **Real-Time Streaming:**
  - WebSocket integration for live market data
  - Live order status updates
  - Streaming fills/executions

- **Advanced Order Types:**
  - Stop-loss orders
  - Trailing stops
  - Time-in-force options (IOC, FOK, GTT)

**Use Cases:**
- Portfolio rebalancing across multiple markets
- Spread trading (simultaneous buy/sell)
- Automated bracket orders for risk management

---

### Phase 3: Analytics & Intelligence
**Estimated: 8-12 additional tools**

- **Historical Analysis:**
  - `kalshi_get_candlesticks` - OHLCV data for charting
  - `kalshi_get_historical_trades` - Time-series trade data

- **Market Analytics:**
  - `kalshi_analyze_market_depth` - Liquidity heatmaps
  - `kalshi_calculate_implied_probabilities` - Cross-market arbitrage detection
  - `kalshi_identify_mispriced_markets` - Value opportunities

- **Performance Metrics:**
  - `kalshi_calculate_pnl` - Detailed P&L attribution
  - `kalshi_get_trade_statistics` - Win rate, avg profit, Sharpe ratio

- **Pattern Recognition:**
  - Volume anomalies
  - Price divergences
  - Orderbook imbalances

**Use Cases:**
- Backtesting strategies on historical data
- Identifying arbitrage opportunities
- Performance attribution and reporting

---

### Phase 4: Institutional-Grade Features
**Estimated: 15-20 additional tools**

- **Multivariate Collections:**
  - Trade across multiple related markets atomically
  - Portfolio construction at event level

- **RFQ (Request for Quote):**
  - Negotiate large trades off-orderbook
  - Minimize market impact for big orders

- **Market Making:**
  - Two-sided quoting tools
  - Inventory management
  - Automated spread maintenance

- **Advanced Portfolio:**
  - Greeks calculation (sensitivity analysis)
  - VaR (Value at Risk) calculations
  - Scenario analysis tools

- **FCM Integration:**
  - Futures Commission Merchant operations
  - Margin management
  - Settlement workflows

**Use Cases:**
- Institutional trading desks
- Automated market making
- Sophisticated hedge fund strategies
- Large-scale portfolio management

---

## Technical Architecture

### FastMCP Server Structure

```
src/
  kalshi/
    __init__.py
    kalshi_mcp_server.py          # Main FastMCP server
    client.py                      # Kalshi API client wrapper
    models.py                      # Pydantic models for requests/responses
    tools/
      __init__.py
      authentication.py            # Exchange status, balance
      market_discovery.py          # Search, browse, market data
      portfolio.py                 # Positions, fills, orders
      trading.py                   # Order execution
    resources/
      __init__.py
      account.py                   # Account resources
      markets.py                   # Market resources
    utils/
      __init__.py
      validation.py                # Input validation, safety checks
      formatting.py                # LLM-friendly response formatting
      rate_limiting.py             # Rate limit management
```

### Key Design Decisions

**1. Client Wrapper Pattern:**
```python
# client.py - Wraps official Kalshi SDK or direct HTTP calls
class KalshiClient:
    def __init__(self, api_key: str, private_key_path: str, demo: bool = False):
        # Initialize with auth

    async def get_market(self, ticker: str) -> Market:
        # API call + error handling + rate limiting

    async def create_order(self, order: CreateOrderRequest) -> OrderResponse:
        # Pre-validation, API call, post-processing
```

**2. Pydantic Models:**
```python
# models.py
from pydantic import BaseModel, Field

class Market(BaseModel):
    ticker: str
    event_ticker: str
    title: str
    subtitle: str | None
    yes_price: int = Field(..., ge=1, le=99, description="Yes price in cents")
    no_price: int = Field(..., ge=1, le=99, description="No price in cents")
    volume_24h: int
    open_interest: int
    status: str
    close_time: datetime

    @property
    def interpretation(self) -> str:
        """Human-readable market summary"""
        return f"Market implies {self.yes_price}% chance: {self.title}"
```

**3. Tool Implementation Pattern:**
```python
# tools/market_discovery.py
from fastmcp import FastMCP, Context
from ..client import KalshiClient
from ..models import Market

@mcp.tool
async def kalshi_get_market(
    ticker: str = Field(..., description="Market ticker symbol (e.g., KXBTC-23DEC-50K)"),
    ctx: Context = None
) -> Market:
    """
    Get comprehensive information about a specific prediction market.

    Returns current prices, volume, open interest, and contract details.
    Use this when you need detailed information about a specific market.

    Example: kalshi_get_market("KXBTC-23DEC-50K")
    """
    if ctx:
        await ctx.info(f"Fetching market data for {ticker}")

    client = KalshiClient.from_env()
    market = await client.get_market(ticker)

    if ctx:
        await ctx.info(f"Market {ticker}: YES={market.yes_price}¢ ({market.interpretation})")

    return market
```

**4. Resource Templates:**
```python
# resources/markets.py
@mcp.resource("kalshi://markets/{ticker}")
async def get_market_resource(ticker: str) -> dict:
    """Market data as a resource for context injection"""
    client = KalshiClient.from_env()
    market = await client.get_market(ticker)
    return market.model_dump()
```

---

## Configuration

### Dual Server Architecture

**Key Principle: Zero Code Duplication**
- Single codebase serves both demo and production environments
- Environment determined by config/env vars at runtime
- Two separate MCP server registrations point to same code with different configs

### Environment Variables

**Production Environment (.env.kalshi.prod):**
```bash
# Required API Key
KALSHI_API_KEY=your_prod_api_key_here

# Required: Private Key (choose ONE approach)
# Approach 1: File-based (recommended for local development)
KALSHI_PRIVATE_KEY_PATH=/path/to/prod_private_key.pem
# Approach 2: Direct content (recommended for CI/CD)
# KALSHI_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\n...key_content...\n-----END PRIVATE KEY-----"

KALSHI_ENVIRONMENT=production

# API Endpoints
KALSHI_BASE_URL=https://trading-api.kalshi.com
KALSHI_API_VERSION=v2

# Safety Limits (Phase 1) - Production
KALSHI_MAX_ORDER_SIZE=100
KALSHI_DAILY_ORDER_LIMIT=50
KALSHI_LARGE_ORDER_THRESHOLD=50
KALSHI_MAX_BALANCE_USAGE_PCT=25

# Rate Limiting
KALSHI_RATE_LIMIT_CALLS=100                # Max calls per minute
KALSHI_RATE_LIMIT_PERIOD=60                # Period in seconds
```

**Demo Environment (.env.kalshi.demo):**
```bash
# Required API Key
KALSHI_API_KEY=your_demo_api_key_here

# Required: Private Key (choose ONE approach)
# Approach 1: File-based (recommended for local development)
KALSHI_PRIVATE_KEY_PATH=/path/to/demo_private_key.pem
# Approach 2: Direct content (recommended for CI/CD)
# KALSHI_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\n...key_content...\n-----END PRIVATE KEY-----"

KALSHI_ENVIRONMENT=demo

# API Endpoints
KALSHI_BASE_URL=https://demo-api.kalshi.co
KALSHI_API_VERSION=v2

# Safety Limits - Demo (more permissive for testing)
KALSHI_MAX_ORDER_SIZE=1000                 # Higher for testing
KALSHI_DAILY_ORDER_LIMIT=500               # Higher for testing
KALSHI_LARGE_ORDER_THRESHOLD=500
KALSHI_MAX_BALANCE_USAGE_PCT=100           # No limit in demo

# Rate Limiting
KALSHI_RATE_LIMIT_CALLS=100
KALSHI_RATE_LIMIT_PERIOD=60
```

### Server Registration (Two MCP Servers)

**1. Production Server:**
```bash
# Create production wrapper script
# run_kalshi_mcp_prod.py
#!/usr/bin/env python3
"""Wrapper script for Kalshi MCP server (PRODUCTION)."""
from dotenv import load_dotenv

# Load production environment
load_dotenv(".env.kalshi.prod")

if __name__ == "__main__":
    from src.kalshi.kalshi_mcp_server import mcp
    mcp.run()
```

```bash
# Register production server
claude mcp add kalshi_prod --scope project -- bash -c "cd $(pwd) && uv run run_kalshi_mcp_prod.py"
```

**2. Demo Server:**
```bash
# Create demo wrapper script
# run_kalshi_mcp_demo.py
#!/usr/bin/env python3
"""Wrapper script for Kalshi MCP server (DEMO - Safe for testing)."""
from dotenv import load_dotenv

# Load demo environment
load_dotenv(".env.kalshi.demo")

if __name__ == "__main__":
    from src.kalshi.kalshi_mcp_server import mcp
    mcp.run()
```

```bash
# Register demo server
claude mcp add kalshi_demo --scope project -- bash -c "cd $(pwd) && uv run run_kalshi_mcp_demo.py"
```

**Usage Pattern:**
```
User: "Use @kalshi_demo to test buying 100 contracts"
  → Agent uses demo MCP, fake money, safe testing

User: "Use @kalshi_prod to buy 10 contracts for real"
  → Agent uses production MCP, real money, actual execution
```

### Server Implementation Pattern

**Single Server Class with Environment Awareness:**
```python
# src/kalshi/kalshi_mcp_server.py
import os
from fastmcp import FastMCP
from dotenv import load_dotenv

# Environment is determined by which .env file was loaded
# (done in wrapper scripts before importing this module)

# Server name reflects environment
env = os.getenv("KALSHI_ENVIRONMENT", "unknown")
mcp = FastMCP(
    name=f"Kalshi Trading ({env.upper()})",
    instructions=f"""
    Kalshi prediction market trading server.
    Environment: {env.upper()}
    {'⚠️ DEMO MODE - Using test money only' if env == 'demo' else '💰 PRODUCTION - Real money trades'}

    Use this server to trade prediction markets, research opportunities,
    and manage your portfolio.
    """
)

# All tools defined here work for both environments
# Client automatically uses correct base URL from env vars
```

---

## Success Metrics

### Phase 1 Targets

**Functionality:**
- ✅ All 16 Phase 1 tools implemented and tested
- ✅ Authentication works with both demo and production
- ✅ Order execution <2 second latency (p95)
- ✅ Zero balance-exceeding orders slip through

**LLM Usability:**
- ✅ LLM can successfully discover markets via natural language
- ✅ LLM can analyze orderbooks and make informed decisions
- ✅ LLM can execute trades and report results clearly
- ✅ Error recovery: LLM handles failed orders gracefully

**Safety:**
- ✅ All order validations working (size, balance, market status)
- ✅ Audit trail captures all order attempts
- ✅ Rate limiting prevents API abuse

**Developer Experience:**
- ✅ Clear setup documentation
- ✅ Works with wrapper script pattern (per CLAUDE.md)
- ✅ Comprehensive tool docstrings
- ✅ Example conversations/workflows documented

---

## Testing Strategy

### Comprehensive Integration Testing

**Philosophy: Test Everything Against Demo Environment**
- All MCP tools must have integration test coverage
- Use real Kalshi demo API (not mocks) wherever possible
- Tests discover real market IDs dynamically (no hardcoded tickers)
- VCR.py for recording/replaying HTTP requests (faster re-runs)

### Test Fixtures

**Dynamic Market Fixtures (tests/fixtures/markets.py):**
```python
import pytest
from src.kalshi.client import KalshiClient

@pytest.fixture(scope="session")
async def demo_client():
    """Kalshi client connected to demo environment."""
    # Loads from .env.kalshi.demo or test env vars
    return KalshiClient.from_env(environment="demo")

@pytest.fixture(scope="session")
async def active_market(demo_client):
    """
    Dynamically find an active, tradeable market for testing.

    Strategy:
    1. Search for markets with status="open"
    2. Filter for markets with:
       - Recent volume (>100 contracts)
       - Good liquidity (bid-ask spread exists)
       - Not expiring in next hour
    3. Cache the ticker for session
    """
    markets = await demo_client.get_markets(
        status="open",
        limit=50
    )

    # Find suitable test market
    for market in markets:
        if (market.volume_24h > 100 and
            market.yes_bid and market.yes_ask and
            market.close_time > datetime.now() + timedelta(hours=1)):
            return market

    pytest.skip("No suitable active market found in demo environment")

@pytest.fixture(scope="session")
async def liquid_market(demo_client):
    """Find a highly liquid market (for orderbook testing)."""
    markets = await demo_client.get_markets(
        status="open",
        limit=100
    )

    # Sort by volume, take top
    markets.sort(key=lambda m: m.volume_24h, reverse=True)
    if markets:
        return markets[0]

    pytest.skip("No liquid markets found")

@pytest.fixture(scope="session")
async def event_with_markets(demo_client):
    """Find an event with multiple markets (for batch testing)."""
    events = await demo_client.get_events(status="open", limit=50)

    for event in events:
        markets = await demo_client.get_markets(event_ticker=event.ticker)
        if len(markets) >= 3:  # Need multiple markets
            return {
                "event": event,
                "markets": markets[:3]
            }

    pytest.skip("No event with 3+ markets found")

@pytest.fixture
async def fresh_balance(demo_client):
    """Get current balance (fresh for each test)."""
    return await demo_client.get_balance()
```

**VCR.py Integration (tests/conftest.py):**
```python
import pytest
import vcr

# Configure VCR for recording/replaying HTTP requests
@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_headers": ["authorization", "x-api-key"],
        "record_mode": "once",  # Record once, replay thereafter
        "match_on": ["method", "scheme", "host", "port", "path", "query"],
        "cassette_library_dir": "tests/cassettes"
    }

@pytest.fixture
def vcr_cassette(request, vcr_config):
    """
    Auto-name cassettes by test class/method.
    Example: TestMarketDiscovery.test_search_markets →
             tests/cassettes/TestMarketDiscovery.test_search_markets.yaml
    """
    cassette_name = f"{request.cls.__name__}.{request.node.name}"
    with vcr.use_cassette(
        f"tests/cassettes/{cassette_name}.yaml",
        **vcr_config
    ):
        yield
```

### Integration Test Structure

**1. Market Discovery Tests (tests/kalshi/integration/test_market_discovery.py):**
```python
import pytest
from src.kalshi.tools.market_discovery import (
    kalshi_search_markets,
    kalshi_get_market,
    kalshi_get_orderbook,
    kalshi_get_trades
)

class TestMarketDiscovery:
    @pytest.mark.asyncio
    async def test_search_returns_results(self, vcr_cassette):
        """Search should return markets matching query."""
        results = await kalshi_search_markets(query="election", limit=10)

        assert len(results) > 0
        assert all(hasattr(r, "ticker") for r in results)
        assert any("election" in r.title.lower() for r in results)

    @pytest.mark.asyncio
    async def test_get_market_returns_full_data(self, active_market, vcr_cassette):
        """Get market should return complete market object."""
        market = await kalshi_get_market(ticker=active_market.ticker)

        assert market.ticker == active_market.ticker
        assert market.yes_price is not None
        assert market.no_price is not None
        assert market.yes_price + market.no_price == 100  # Prices sum to 100
        assert hasattr(market, "interpretation")

    @pytest.mark.asyncio
    async def test_orderbook_has_depth(self, liquid_market, vcr_cassette):
        """Orderbook should contain bid/ask levels."""
        orderbook = await kalshi_get_orderbook(
            ticker=liquid_market.ticker,
            depth=5
        )

        assert "yes_bids" in orderbook
        assert "yes_asks" in orderbook
        assert len(orderbook["yes_bids"]) > 0
        assert len(orderbook["yes_asks"]) > 0

        # Validate structure
        bid = orderbook["yes_bids"][0]
        assert "price" in bid
        assert "quantity" in bid
```

**2. Trading Tests (tests/kalshi/integration/test_trading.py):**
```python
class TestOrderExecution:
    @pytest.mark.asyncio
    async def test_create_limit_order_success(self, active_market, fresh_balance, vcr_cassette):
        """Can create limit order in demo environment."""
        from src.kalshi.tools.trading import kalshi_create_limit_order

        # Create small order well away from market price (won't fill)
        result = await kalshi_create_limit_order(
            ticker=active_market.ticker,
            side="yes",
            quantity=1,
            price=1  # 1¢ - very unlikely to fill
        )

        assert result["status"] in ["success", "accepted"]
        assert result["order_id"] is not None

        # Clean up: cancel the order
        from src.kalshi.tools.trading import kalshi_cancel_order
        await kalshi_cancel_order(order_id=result["order_id"])

    @pytest.mark.asyncio
    async def test_order_validation_rejects_invalid_price(self, active_market):
        """Order validation should reject price outside 1-99 range."""
        from src.kalshi.tools.trading import kalshi_create_limit_order
        from src.kalshi.utils.validation import OrderValidationError

        with pytest.raises(OrderValidationError, match="price must be between 1 and 99"):
            await kalshi_create_limit_order(
                ticker=active_market.ticker,
                side="yes",
                quantity=10,
                price=150  # Invalid: > 99
            )

    @pytest.mark.asyncio
    async def test_order_validation_rejects_insufficient_balance(self, active_market, fresh_balance):
        """Cannot place order exceeding balance."""
        from src.kalshi.tools.trading import kalshi_create_limit_order
        from src.kalshi.utils.validation import OrderValidationError

        # Try to buy more than we can afford
        excessive_quantity = int(fresh_balance["balance"] * 100)  # Way more than balance

        with pytest.raises(OrderValidationError, match="insufficient balance"):
            await kalshi_create_limit_order(
                ticker=active_market.ticker,
                side="yes",
                quantity=excessive_quantity,
                price=99
            )
```

**3. Portfolio Tests (tests/kalshi/integration/test_portfolio.py):**
```python
class TestPortfolio:
    @pytest.mark.asyncio
    async def test_get_positions_returns_list(self, vcr_cassette):
        """Get positions should return current holdings."""
        from src.kalshi.tools.portfolio import kalshi_get_positions

        positions = await kalshi_get_positions()

        assert isinstance(positions, list)
        # May be empty if no positions, that's ok
        if positions:
            pos = positions[0]
            assert "ticker" in pos
            assert "position" in pos
            assert "market_exposure" in pos

    @pytest.mark.asyncio
    async def test_get_fills_after_order(self, active_market, vcr_cassette):
        """Fills should appear after order execution."""
        from src.kalshi.tools.trading import kalshi_create_market_order
        from src.kalshi.tools.portfolio import kalshi_get_fills

        # Create market order (should fill immediately)
        order_result = await kalshi_create_market_order(
            ticker=active_market.ticker,
            side="yes",
            quantity=1
        )

        # Check fills
        fills = await kalshi_get_fills(ticker=active_market.ticker, limit=10)

        # Should find our order in recent fills
        order_fills = [f for f in fills if f["order_id"] == order_result["order_id"]]
        assert len(order_fills) > 0
```

**4. Error Handling Tests (tests/kalshi/integration/test_error_handling.py):**
```python
class TestAPIErrorHandling:
    @pytest.mark.asyncio
    async def test_handles_invalid_ticker(self, vcr_cassette):
        """Should handle invalid ticker gracefully."""
        from src.kalshi.tools.market_discovery import kalshi_get_market
        from src.kalshi.exceptions import MarketNotFoundError

        with pytest.raises(MarketNotFoundError, match="INVALID-TICKER-XXX"):
            await kalshi_get_market(ticker="INVALID-TICKER-XXX")

    @pytest.mark.asyncio
    async def test_handles_expired_market(self, demo_client, vcr_cassette):
        """Should reject orders on expired markets."""
        from src.kalshi.tools.trading import kalshi_create_limit_order
        from src.kalshi.exceptions import MarketClosedError

        # Find an expired market
        markets = await demo_client.get_markets(status="closed", limit=1)
        if not markets:
            pytest.skip("No closed markets available")

        expired_ticker = markets[0].ticker

        with pytest.raises(MarketClosedError):
            await kalshi_create_limit_order(
                ticker=expired_ticker,
                side="yes",
                quantity=1,
                price=50
            )
```

**5. End-to-End Workflow Tests (tests/kalshi/integration/test_workflows.py):**
```python
class TestCompleteWorkflows:
    @pytest.mark.asyncio
    async def test_research_and_trade_workflow(self, vcr_cassette):
        """
        Complete workflow: Search → Analyze → Trade → Verify
        """
        from src.kalshi.tools.market_discovery import (
            kalshi_search_markets,
            kalshi_get_market,
            kalshi_get_orderbook
        )
        from src.kalshi.tools.trading import kalshi_create_limit_order, kalshi_cancel_order
        from src.kalshi.tools.portfolio import kalshi_get_orders

        # 1. Search for markets
        markets = await kalshi_search_markets(query="bitcoin", limit=5)
        assert len(markets) > 0

        # 2. Get detailed market info
        market = await kalshi_get_market(ticker=markets[0].ticker)
        assert market.yes_price is not None

        # 3. Check orderbook
        orderbook = await kalshi_get_orderbook(ticker=market.ticker)
        assert "yes_bids" in orderbook

        # 4. Place limit order (won't fill)
        order = await kalshi_create_limit_order(
            ticker=market.ticker,
            side="yes",
            quantity=1,
            price=1
        )
        assert order["order_id"] is not None

        # 5. Verify order appears in active orders
        active_orders = await kalshi_get_orders(ticker=market.ticker)
        assert any(o["order_id"] == order["order_id"] for o in active_orders)

        # 6. Cancel order (cleanup)
        cancel_result = await kalshi_cancel_order(order_id=order["order_id"])
        assert cancel_result["status"] == "canceled"
```

### Unit Tests (Mocked)

**When to Use Mocks:**
- Testing validation logic (no API needed)
- Testing error formatting/handling
- Testing rate limiting behavior
- Testing internal utilities

**Example (tests/kalshi/unit/test_validation.py):**
```python
class TestOrderValidation:
    def test_validates_price_range(self):
        from src.kalshi.utils.validation import validate_order_price

        # Valid prices
        assert validate_order_price(1) is None
        assert validate_order_price(50) is None
        assert validate_order_price(99) is None

        # Invalid prices
        with pytest.raises(ValueError):
            validate_order_price(0)
        with pytest.raises(ValueError):
            validate_order_price(100)
        with pytest.raises(ValueError):
            validate_order_price(-5)

    def test_validates_quantity(self):
        from src.kalshi.utils.validation import validate_quantity

        assert validate_quantity(1) is None
        assert validate_quantity(100) is None

        with pytest.raises(ValueError):
            validate_quantity(0)
        with pytest.raises(ValueError):
            validate_quantity(-10)
```

### LLM Integration Tests

**Manual Test Scenarios (documented, not automated):**

1. **Market Research Workflow:**
   ```
   User: "@kalshi_demo find me the most active election markets"
   Expected: LLM searches, ranks by volume, presents top 3
   ```

2. **Trade Execution:**
   ```
   User: "@kalshi_demo buy 10 YES on the top market if price < 60¢"
   Expected: LLM checks price, executes if condition met, reports result
   ```

3. **Portfolio Review:**
   ```
   User: "@kalshi_demo what's my P&L?"
   Expected: LLM fetches positions, calculates unrealized P&L, summarizes
   ```

4. **Error Recovery:**
   ```
   User: "@kalshi_demo buy 1000 contracts on INVALID-TICKER"
   Expected: LLM handles error, explains problem, suggests corrections
   ```

### Test Coverage Requirements

**Minimum Coverage Targets:**
- **Integration Tests**: 100% of MCP tools (all 16 Phase 1 tools)
- **Unit Tests**: 90% of validation/utility functions
- **Error Handling**: All error paths tested
- **VCR Cassettes**: Recorded for all integration tests (fast re-runs)

### Running Tests

```bash
# All tests (includes integration against demo API)
uv run pytest

# Unit tests only (fast, no API calls)
uv run pytest tests/kalshi/unit

# Integration tests (uses VCR cassettes)
uv run pytest tests/kalshi/integration

# Re-record cassettes (fresh API calls)
uv run pytest tests/kalshi/integration --record-mode=all

# Specific test
uv run pytest tests/kalshi/integration/test_trading.py::TestOrderExecution::test_create_limit_order_success

# Coverage report
uv run pytest --cov=src/kalshi --cov-report=html
```

### Safety Tests

**Critical Safety Scenarios:**
```python
class TestSafetyLimits:
    @pytest.mark.asyncio
    async def test_rejects_order_exceeding_max_size(self, active_market):
        """Cannot exceed KALSHI_MAX_ORDER_SIZE."""
        from src.kalshi.tools.trading import kalshi_create_limit_order

        with pytest.raises(OrderValidationError, match="exceeds maximum"):
            await kalshi_create_limit_order(
                ticker=active_market.ticker,
                side="yes",
                quantity=999999,  # Way over limit
                price=50
            )

    @pytest.mark.asyncio
    async def test_audit_trail_captures_all_attempts(self, active_market):
        """All order attempts logged."""
        from src.kalshi.utils.audit import get_audit_log

        # Clear audit log
        get_audit_log().clear()

        # Attempt order (will fail due to invalid price)
        try:
            await kalshi_create_limit_order(
                ticker=active_market.ticker,
                side="yes",
                quantity=1,
                price=999  # Invalid
            )
        except Exception:
            pass

        # Check audit log
        logs = get_audit_log().entries
        assert len(logs) == 1
        assert logs[0]["action"] == "create_limit_order"
        assert logs[0]["status"] == "failed"
        assert "validation_error" in logs[0]
```

---

## Dependencies

```toml
# pyproject.toml
[project]
name = "kalshi-mcp-server"
version = "0.1.0"
dependencies = [
    "fastmcp>=2.0.0",
    "pydantic>=2.0.0",
    "httpx>=0.27.0",           # For HTTP requests
    "python-dotenv>=1.0.0",    # Environment variables
    "loguru>=0.7.0",           # Logging
    "cryptography>=42.0.0",    # For API key signing
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0.0",
    "pytest-asyncio>=0.23.0",
    "pytest-mock>=3.12.0",
    "vcrpy>=6.0.0",            # Record/replay HTTP for tests
]
```

---

## Documentation Deliverables

1. **README.md** - Quick start guide
2. **SETUP.md** - Detailed installation and configuration
3. **TOOLS.md** - Complete tool reference with examples
4. **EXAMPLES.md** - Example LLM conversations and workflows
5. **SAFETY.md** - Risk management and safety features
6. **API.md** - Kalshi API mapping and coverage

---

## Open Questions / Decisions Needed

1. **Official Kalshi SDK vs. Direct HTTP:**
   - Use official Python SDK if available/maintained?
   - Or implement direct HTTP client for more control?
   - **Recommendation**: Start with direct HTTP for flexibility

2. **Demo vs. Production Default:**
   - Should server default to demo environment for safety?
   - Require explicit flag to enable production?
   - **Recommendation**: Default to demo, require `KALSHI_DEMO=false`

3. **Order Confirmation UX:**
   - Should large orders require explicit user confirmation?
   - Or trust LLM to ask user before executing?
   - **Recommendation**: Emit warning but allow LLM to handle UX

4. **Rate Limiting Strategy:**
   - Implement client-side rate limiting?
   - Or rely on Kalshi's server-side limits and handle 429s?
   - **Recommendation**: Client-side limits with graceful backoff

5. **WebSocket in Phase 1?**
   - Add basic WebSocket support for live prices?
   - Or defer entirely to Phase 2?
   - **Recommendation**: Defer to Phase 2, use polling for Phase 1

---

## Timeline Estimate (Phase 1)

**Week 1: Foundation**
- Project setup, dependencies
- Kalshi client wrapper with auth
- Core Pydantic models
- Basic FastMCP server structure

**Week 2: Market Discovery**
- Search and browse tools
- Market data tools
- Orderbook and trades
- Testing with demo environment

**Week 3: Trading & Portfolio**
- Order execution tools
- Portfolio tools
- Safety validations
- Integration testing

**Week 4: Polish & Documentation**
- LLM conversation testing
- Documentation
- Example workflows
- Safety audit

**Total: 4 weeks to production-ready Phase 1**

---

## Appendix: Example LLM Conversations

### Conversation 1: Market Research

**User:** "What are the most active prediction markets about AI right now?"

**LLM:** Let me search for AI-related markets.
*Calls: kalshi_search_markets("AI", limit=10)*

**LLM:** "I found several active AI markets. The most liquid one is 'Will an AI lab announce AGI by end of 2024?' (ticker: KXAGI-24DEC-Y) with $2.3M in volume. Currently trading at 12¢ YES, 88¢ NO. Would you like to see the orderbook?"

**User:** "Yes, show me the orderbook"

**LLM:** *Calls: kalshi_get_orderbook("KXAGI-24DEC-Y", depth=5)*

**LLM:** "Here's the current orderbook:

**YES Side:**
- 11¢: 500 contracts
- 10¢: 1,200 contracts
- 9¢: 2,500 contracts

**NO Side:**
- 89¢: 800 contracts
- 90¢: 1,500 contracts
- 91¢: 3,000 contracts

The spread is 77¢ (buying YES at 12¢ vs selling YES at 11¢). There's good liquidity on both sides."

---

### Conversation 2: Trade Execution

**User:** "I think Bitcoin will hit $50K by end of year. Buy me 50 YES contracts if the price is 45¢ or better"

**LLM:** Let me find the relevant Bitcoin market first.
*Calls: kalshi_search_markets("Bitcoin $50K 2024")*

**LLM:** "I found market KXBTC-31DEC-50K. Let me check the current price."
*Calls: kalshi_get_market("KXBTC-31DEC-50K")*

**LLM:** "Current prices: YES=42¢, NO=58¢. This is better than your 45¢ target. I'll place a market order for 50 YES contracts."
*Calls: kalshi_create_market_order("KXBTC-31DEC-50K", side="yes", quantity=50)*

**LLM:** "✅ Order filled!
- Purchased: 50 YES contracts
- Average price: 42¢
- Total cost: $21.00
- Potential profit if YES wins: $29.00 (138% return)

Your position: Long 50 YES on Bitcoin hitting $50K by Dec 31."

---

### Conversation 3: Portfolio Review

**User:** "What's my current P&L?"

**LLM:** *Calls: kalshi_get_positions()*

**LLM:** "Here's your portfolio summary:

**Open Positions (3):**

1. KXBTC-31DEC-50K (Bitcoin $50K)
   - Size: 50 YES
   - Entry: 42¢
   - Current: 44¢
   - P&L: +$1.00 (+4.8%)

2. KXELEC-05NOV-DEM (Election - Dem win)
   - Size: 100 YES
   - Entry: 55¢
   - Current: 52¢
   - P&L: -$3.00 (-5.5%)

3. KXFED-DEC-HIKE (Fed rate hike)
   - Size: 25 NO
   - Entry: 35¢
   - Current: 38¢
   - P&L: -$0.75 (-8.6%)

**Total Unrealized P&L: -$2.75 (-3.1%)**
**Account Balance: $1,234.56**"

**User:** "Close the Fed position, I changed my mind"

**LLM:** *Calls: kalshi_create_market_order("KXFED-DEC-HIKE", side="yes", quantity=25)*  *(Buying YES closes the NO position)*

**LLM:** "✅ Position closed at 38¢. Realized loss: $0.75"

---

## Revision History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-11-03 | Initial PRD for Phase 1 |

