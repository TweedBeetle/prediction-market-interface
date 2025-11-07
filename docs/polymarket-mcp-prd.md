# Polymarket MCP Server - Product Requirements Document

**Version**: 1.0
**Date**: 2025-11-05
**Status**: ⏳ Planning - Awaiting Implementation

## Executive Summary

A FastMCP-based server that exposes Polymarket's prediction market trading platform to LLM agents, enabling sophisticated interactive trading and market research through natural language conversations on the world's largest prediction market platform.

### Primary Use Cases
1. **Interactive LLM-Driven Trading**: Claude-powered trading decisions with real-time execution on Polygon blockchain
2. **Market Research & Analysis**: Data exploration, opportunity discovery, arbitrage detection across massive market catalog
3. **Advanced Order Management**: Batch operations, sophisticated order types, WebSocket real-time updates
4. **Cross-Platform Arbitrage**: Compare prices with Kalshi for arbitrage opportunities

### Key Differentiators from Kalshi
- **Blockchain-based**: Non-custodial trading on Polygon (vs centralized Kalshi)
- **EIP-712 Signing**: Wallet-based authentication (vs API key)
- **Token Markets**: Buy/sell binary outcome tokens (vs synthetic contracts)
- **Massive Scale**: 10x+ more markets than Kalshi
- **Zero Fees**: Currently 0% maker/taker fees (vs Kalshi's fee structure)
- **WebSocket Streaming**: Built-in real-time data (vs polling)

### Development Phases
- **Phase 1** (MVP): Market data + basic trading (12 tools)
- **Phase 2**: Advanced trading + portfolio management (8 tools)
- **Phase 3**: Real-time WebSocket streaming (6 tools)
- **Phase 4**: Analytics, arbitrage detection, social features (10+ tools)

---

## Phase 1: MVP - Market Data & Basic Trading

**Goal**: Enable basic market discovery and trading with non-custodial wallet integration.

**Timeline Estimate**: 3-4 weeks

### 1.1 Authentication & Connection

**Challenge**: Polymarket uses two-level authentication different from Kalshi:
- **L1 (Private Key)**: EIP-712 wallet signing for order placement, API key creation
- **L2 (API Key)**: HMAC-based auth for API requests

**Tools:**
- `polymarket_get_api_credentials` - Create/derive API keys using wallet signature
- `polymarket_check_access_status` - Verify account access and restrictions

**Technical Implementation:**
- Private key management (Polygon wallet)
- EIP-712 signing implementation for CLOB auth
- API key derivation and HMAC signature generation
- Support for three wallet types:
  1. Email/Magic link accounts (signature_type=1)
  2. Browser wallets (MetaMask, Coinbase, signature_type=2)
  3. Direct EOA (Externally Owned Account)

**Configuration:**
```python
# Environment variables
POLYMARKET_PRIVATE_KEY=<wallet_private_key>
POLYMARKET_PROXY_ADDRESS=<proxy_wallet_address>  # For Magic/browser wallets
POLYMARKET_CHAIN_ID=137  # Polygon mainnet
POLYMARKET_CLOB_ENDPOINT=https://clob.polymarket.com
POLYMARKET_GAMMA_ENDPOINT=https://gamma-api.polymarket.com
```

**Resources:**
- `polymarket://account/credentials` - Current API key status (read-only)
- `polymarket://account/proxy` - Proxy wallet address information

---

### 1.2 Market Discovery & Research

**Polymarket markets are significantly more complex than Kalshi:**
- Hierarchical structure: Events → Markets (with binary outcomes)
- Rich metadata: Tags, categories, series, collections
- Multiple market IDs: Condition ID, CLOB token IDs, question ID

**Tools:**

**Search & Browse:**
- `polymarket_search` - Universal search across markets, events, profiles
- `polymarket_list_markets` - Browse markets with extensive filtering
  - Filter by: liquidity, volume, date ranges, tags, categories
  - Sort by: volume, liquidity, recency, trending
- `polymarket_get_events` - List events (collections of related markets)
- `polymarket_get_event` - Detailed event information with all markets

**Market Details:**
- `polymarket_get_market` - Comprehensive market information:
  - Question, outcomes, description
  - Current prices (best bid/ask, last trade)
  - Volume (24h, 1w, 1m, 1y - both AMM and CLOB)
  - Liquidity, open interest
  - Resolution source, end date
  - CLOB token IDs (required for trading)
  - Categories, tags, metadata

**Orderbook & Pricing:**
- `polymarket_get_orderbook` - Order book depth for a market
- `polymarket_get_price_history` - Historical price chart data

**Advanced Discovery:**
- `polymarket_get_series` - Recurring market series (e.g., weekly crypto prices)
- `polymarket_get_tags` - Tag-based market discovery
- `polymarket_get_featured_markets` - Currently featured/trending markets

**Resources:**
- `polymarket://markets/trending` - High-volume markets
- `polymarket://markets/{id}` - Market data resource template
- `polymarket://events/{id}` - Event data resource template

**Design Principles:**
- Return rich, structured data suitable for LLM analysis
- Include both CLOB token IDs (for trading) and condition IDs (for querying)
- Provide human-readable interpretations alongside raw data
- Support exploratory workflows ("Show me markets about...")

**Example Market Response:**
```python
{
    "id": "12345",
    "question": "Will Bitcoin reach $100K by end of 2025?",
    "outcomes": ["YES", "NO"],
    "clob_token_ids": ["token_yes_id", "token_no_id"],
    "best_bid": 0.42,  # YES side
    "best_ask": 0.44,
    "last_price": 0.43,
    "volume_24h": 125000.50,
    "liquidity": 50000.00,
    "end_date": "2025-12-31T23:59:59Z",
    "interpretation": "Market implies 43% chance of Bitcoin reaching $100K by Dec 31, 2025"
}
```

---

### 1.3 Order Execution (Basic)

**Polymarket orders are fundamentally different from Kalshi:**
- Trade outcome **tokens** (not synthetic contracts)
- Orders are **EIP-712 signed messages**
- Settlement happens **on-chain** (Polygon blockchain)
- Prices are in **dollars** (0.01 to 0.99), not cents

**Tools:**

**Limit Orders (Primary):**
- `polymarket_create_order` - Create limit order (with signature)
  - Parameters:
    - `token_id` (required) - YES or NO outcome token ID
    - `side` - "BUY" or "SELL"
    - `price` - Float 0.01 to 0.99 (dollars)
    - `size` - Number of shares
    - `order_type` - "GTC", "FOK", "IOC"
    - `negrisk` - Boolean (special market type flag)

**Order Management:**
- `polymarket_cancel_order` - Cancel a pending order
- `polymarket_cancel_orders` - Batch cancel multiple orders
- `polymarket_get_order` - Get order status and details

**Validation & Safety:**
- Pre-execution checks:
  - Sufficient USDC balance
  - Allowances set (for MetaMask/web3 wallets)
  - Market is accepting orders
  - Price within valid range (0.01-0.99)
  - Token ID is valid
- EIP-712 signature validation
- On-chain settlement confirmation

**Order Flow:**
```
1. User requests trade
2. Fetch market details (get token IDs)
3. Build order parameters
4. Sign order with EIP-712 (wallet private key)
5. Submit signed order to CLOB
6. Monitor order status (pending → filled/canceled)
7. Report execution to user
```

**Response Format:**
```python
{
    "status": "success" | "partial" | "failed",
    "order_id": str,
    "market": str,
    "side": "BUY" | "SELL",
    "outcome": "YES" | "NO",
    "price": float,
    "size_requested": float,
    "size_filled": float,
    "size_remaining": float,
    "message": str  # Human-readable explanation
}
```

---

### 1.4 Portfolio Management (Basic)

**Tools:**

**Position Tracking:**
- `polymarket_get_positions` - Current positions across all markets
  - Returns: token balances, avg entry price, current value, P&L
  - Filter by market or show portfolio-wide

**Order History:**
- `polymarket_get_fills` - Trade execution history
  - Returns: price, size, timestamp, fees paid
  - Useful for performance analysis

**Account Metrics:**
- `polymarket_get_portfolio_value` - Total position value
- `polymarket_get_total_markets_traded` - Number of unique markets

**Resources:**
- `polymarket://portfolio/positions` - Current positions summary
- `polymarket://portfolio/pnl` - Realized & unrealized P&L

---

### 1.5 LLM-Friendly Design Patterns

**Structured Outputs:**
- Use Pydantic models for all responses
- Include both machine data AND human context
- Example:
  ```python
  {
      "market_id": "12345",
      "question": "Will Bitcoin reach $100K by end of 2025?",
      "yes_price": 0.43,
      "no_price": 0.57,
      "interpretation": "Market implies 43% chance Bitcoin reaches $100K by Dec 31, 2025",
      "volume_24h": 125000.50,
      "liquidity": 50000.00,
      "recommended_action": "Based on current price and liquidity, this is a good entry point"
  }
  ```

**Natural Language Prompts:**
- Every tool has detailed docstring explaining:
  - What it does in plain English
  - When to use it (vs alternatives)
  - Common parameters
  - Example use cases

**Error Handling:**
- LLM-readable errors: "Cannot place order - insufficient USDC balance. You have $10.50 but need $50.00"
- Not: "HTTP 400: balance_too_low"
- Include recovery suggestions when possible

**Progress & Logging:**
- Use FastMCP Context for progress reporting
- Log important events (signatures created, orders submitted, fills received)
- Enable LLM to provide running commentary to user

**Conversational Workflows:**
Design tools to support multi-turn conversations:
1. User: "What's the most active crypto market?"
2. LLM calls: `polymarket_search("crypto", sort_by="volume")`
3. LLM: "The most active is 'Bitcoin $100K by 2025' with $125K 24h volume, trading at 43¢"
4. User: "What's the orderbook like?"
5. LLM calls: `polymarket_get_orderbook(market_id="12345")`
6. LLM: "Strong support at 42¢ (50K shares), resistance at 44¢ (30K shares)"

---

### 1.6 Safety & Risk Management

**Phase 1 Safeguards:**

**Order Limits:**
- Maximum order size per execution (configurable, default: 100 shares)
- Daily order count limit (default: 50 orders/day)
- Require explicit confirmation for orders > threshold

**Balance Protection:**
- Never allow orders that exceed USDC balance
- Account for allowances (MetaMask users)
- Warning if order would use >25% of balance

**Market Validation:**
- Only allow trading in active markets (acceptingOrders=true)
- Reject orders for closed/resolved markets
- Check if market is restricted

**Blockchain Safety:**
- Non-custodial: user always retains control of funds
- On-chain settlement: trades are cryptographically verified
- No operator risk (unlike centralized exchanges)

**Audit Trail:**
- Log all order attempts (successful and failed)
- Include LLM context (reasoning for trade)
- Store signatures for later verification
- Track on-chain transaction hashes

**Configuration:**
```python
# .env or server config
POLYMARKET_MAX_ORDER_SIZE=100
POLYMARKET_DAILY_ORDER_LIMIT=50
POLYMARKET_LARGE_ORDER_THRESHOLD=50  # Require confirmation
POLYMARKET_MAX_BALANCE_USAGE_PCT=25  # Warning threshold
```

---

## Phase 1 Tool Summary

**Total: 12 tools**

**Authentication (2 tools):**
- ✅ `polymarket_get_api_credentials`
- ✅ `polymarket_check_access_status`

**Market Discovery (6 tools):**
- ✅ `polymarket_search`
- ✅ `polymarket_list_markets`
- ✅ `polymarket_get_market`
- ✅ `polymarket_get_event`
- ✅ `polymarket_get_orderbook`
- ✅ `polymarket_get_price_history`

**Trading (2 tools):**
- ✅ `polymarket_create_order`
- ✅ `polymarket_cancel_order`

**Portfolio (2 tools):**
- ✅ `polymarket_get_positions`
- ✅ `polymarket_get_fills`

---

## Phase 2: Advanced Trading & Portfolio Analytics

**Goal**: Professional trading features, portfolio optimization, batch operations.

**Timeline Estimate**: 2-3 weeks

### 2.1 Advanced Order Types

**Tools:**

**Batch Operations:**
- `polymarket_create_batch_orders` - Submit multiple orders atomically
  - Up to 20 orders in single transaction
  - All-or-nothing execution
  - Useful for: Portfolio rebalancing, spread trading

**Market Making:**
- `polymarket_create_two_sided_order` - Place bid and ask simultaneously
  - Parameters: spread, quantity on each side
  - Useful for providing liquidity

**Advanced Parameters:**
- All orders support:
  - `time_in_force`: "GTC", "FOK", "IOC"
  - `post_only`: Maker-only orders
  - `reduce_only`: Position-only reduction
  - `client_order_id`: Custom order tracking

### 2.2 Portfolio Analytics

**Tools:**

**Performance Tracking:**
- `polymarket_get_portfolio_stats` - Detailed performance metrics
  - Win rate, avg profit, Sharpe ratio
  - Breakdown by category/market type
  - Time-series P&L

**Risk Management:**
- `polymarket_get_position_exposure` - Portfolio concentration analysis
  - Exposure by category, time horizon
  - Correlation analysis across positions

**Trade Analysis:**
- `polymarket_get_trade_history` - Comprehensive trade log
  - Filter by date range, market, outcome
  - Export for external analysis

### 2.3 Advanced Market Discovery

**Tools:**

**Specialized Searches:**
- `polymarket_get_trending_markets` - Currently hot markets
- `polymarket_get_new_markets` - Recently created
- `polymarket_get_closing_soon` - Markets ending in next 24h

**Social Features:**
- `polymarket_get_top_traders` - Leaderboard for a market
- `polymarket_get_comments` - Community discussions

---

## Phase 3: Real-Time WebSocket Streaming

**Goal**: Real-time market data and order updates via WebSocket.

**Timeline Estimate**: 2 weeks

### 3.1 WebSocket Integration

**Polymarket provides two WebSocket channels:**

**Market Channel:**
- Real-time price updates
- Orderbook changes
- Trade executions
- Subscribe to specific markets

**User Channel:**
- Real-time order status updates
- Fill notifications
- Balance changes
- Portfolio updates

**Tools:**

**Stream Management:**
- `polymarket_subscribe_market` - Subscribe to market updates
- `polymarket_subscribe_portfolio` - Subscribe to portfolio updates
- `polymarket_unsubscribe` - Stop streaming
- `polymarket_get_stream_status` - Check active subscriptions

**Event Handlers:**
- Register callbacks for specific events
- Filter events by type
- Batch event processing

**Implementation Notes:**
- Need to research MCP pattern for WebSocket integration
- May require background task management
- Consider using FastMCP Context for streaming updates to LLM

---

## Phase 4: Analytics, Arbitrage & Social Features

**Goal**: Advanced analytics, cross-platform arbitrage detection, social trading features.

**Timeline Estimate**: 3-4 weeks

### 4.1 Cross-Platform Arbitrage

**Tools:**

**Price Comparison:**
- `polymarket_find_arbitrage_kalshi` - Compare prices with Kalshi
  - Identify same markets on both platforms
  - Calculate arbitrage spreads
  - Account for fees and slippage

**Arbitrage Execution:**
- `polymarket_execute_arbitrage` - Atomic cross-platform trade
  - Simultaneous execution on both platforms
  - Risk management (position limits)

### 4.2 Advanced Analytics

**Tools:**

**Historical Analysis:**
- `polymarket_get_candlesticks` - OHLCV data for charting
- `polymarket_analyze_market_depth` - Liquidity heatmaps
- `polymarket_detect_price_anomalies` - Unusual price movements

**Predictive Analytics:**
- `polymarket_calculate_implied_probabilities` - Cross-market consistency
- `polymarket_identify_mispriced_markets` - Value opportunities
- `polymarket_backt est_strategy` - Historical strategy performance

### 4.3 Social & Community Features

**Tools:**

**Community Engagement:**
- `polymarket_get_market_comments` - Read discussions
- `polymarket_post_comment` - Share insights
- `polymarket_get_user_profile` - Trader profiles

**Collaborative Trading:**
- `polymarket_get_popular_positions` - What top traders are doing
- `polymarket_track_trader` - Follow specific traders

---

## Technical Architecture

### Dual Client Architecture

**Polymarket has two separate APIs:**

1. **Gamma Markets API** (read-only market data)
   - Endpoint: https://gamma-api.polymarket.com
   - No authentication required for most endpoints
   - Rich market metadata, historical data

2. **CLOB API** (trading operations)
   - Endpoint: https://clob.polymarket.com
   - Requires L1 (wallet) + L2 (API key) authentication
   - Order placement, cancellation, status

### Project Structure

```
src/
  polymarket/
    __init__.py
    polymarket_mcp_server.py       # Main FastMCP server
    gamma_client.py                # Gamma Markets API client
    clob_client.py                 # CLOB trading client
    signing.py                     # EIP-712 signature utilities
    models.py                      # Pydantic models
    tools/
      __init__.py
      authentication.py            # API key management
      market_discovery.py          # Search, browse, market data
      trading.py                   # Order execution
      portfolio.py                 # Positions, fills, performance
      websocket.py                 # Real-time streaming (Phase 3)
      arbitrage.py                 # Cross-platform trading (Phase 4)
    utils/
      __init__.py
      validation.py                # Input validation, safety checks
      formatting.py                # LLM-friendly response formatting
```

### Key Design Decisions

**1. Dual Client Pattern:**
```python
# gamma_client.py - Market data (read-only)
class GammaClient:
    def __init__(self):
        self.base_url = "https://gamma-api.polymarket.com"

    async def get_market(self, market_id: str) -> Market:
        # No auth required
        return await self._request("GET", f"/markets/{market_id}")

# clob_client.py - Trading (requires auth)
class ClobClient:
    def __init__(self, private_key: str, proxy_address: str = None):
        self.base_url = "https://clob.polymarket.com"
        self.private_key = private_key
        self.proxy_address = proxy_address
        self.api_creds = None

    async def create_api_credentials(self):
        # Sign with EIP-712, get API key
        signature = self._sign_clob_auth()
        self.api_creds = await self._request(
            "POST", "/auth/api-key",
            headers=self._l1_headers(signature)
        )

    async def create_order(self, order: OrderParams) -> OrderResponse:
        # Sign order with EIP-712
        signed_order = self._sign_order(order)
        # Submit with L2 (HMAC) auth
        return await self._request(
            "POST", "/order",
            json=signed_order,
            headers=self._l2_headers()
        )
```

**2. Pydantic Models:**
```python
# models.py
from pydantic import BaseModel, Field
from typing import Optional, List

class Market(BaseModel):
    id: str
    question: str
    outcomes: List[str]  # ["YES", "NO"]
    clob_token_ids: List[str]  # Required for trading
    condition_id: str
    best_bid: Optional[float] = Field(None, ge=0.01, le=0.99)
    best_ask: Optional[float] = Field(None, ge=0.01, le=0.99)
    last_price: Optional[float] = None
    volume_24h: float
    liquidity: float
    end_date: datetime
    active: bool
    accepting_orders: bool
    neg_risk: bool = False

    @property
    def interpretation(self) -> str:
        """Human-readable market summary"""
        if self.last_price:
            pct = int(self.last_price * 100)
            return f"Market implies {pct}% chance: {self.question}"
        return f"Market: {self.question}"

    @property
    def spread_bps(self) -> Optional[int]:
        """Bid-ask spread in basis points"""
        if self.best_bid and self.best_ask:
            return int((self.best_ask - self.best_bid) * 10000)
        return None

class OrderParams(BaseModel):
    token_id: str = Field(..., description="CLOB token ID (YES or NO)")
    side: str = Field(..., pattern="^(BUY|SELL)$")
    price: float = Field(..., ge=0.01, le=0.99)
    size: float = Field(..., gt=0)
    order_type: str = Field(default="GTC", pattern="^(GTC|FOK|IOC)$")
    neg_risk: bool = False
```

**3. EIP-712 Signing:**
```python
# signing.py
from eth_account import Account
from eth_account.messages import encode_structured_data

def sign_clob_auth(private_key: str, timestamp: int, nonce: int = 0) -> str:
    """
    Sign CLOB authentication message with EIP-712.

    Returns signature for L1 authentication.
    """
    domain = {
        "name": "ClobAuthDomain",
        "version": "1",
        "chainId": 137,  # Polygon
    }

    types = {
        "ClobAuth": [
            {"name": "address", "type": "address"},
            {"name": "timestamp", "type": "string"},
            {"name": "nonce", "type": "uint256"},
            {"name": "message", "type": "string"},
        ]
    }

    message = {
        "address": Account.from_key(private_key).address,
        "timestamp": str(timestamp),
        "nonce": nonce,
        "message": "This message attests that I control the given wallet",
    }

    structured_data = encode_structured_data(
        domain_data=domain,
        message_types=types,
        message_data=message
    )

    signed = Account.sign_message(structured_data, private_key)
    return signed.signature.hex()

def sign_order(private_key: str, order_params: OrderParams) -> dict:
    """
    Sign order with EIP-712 for submission to CLOB.
    """
    # Implementation based on Polymarket's order signing spec
    # ...
```

**4. Tool Implementation Pattern:**
```python
# tools/trading.py
from fastmcp import FastMCP, Context
from ..clob_client import ClobClient
from ..gamma_client import GammaClient
from ..models import OrderParams, Market

@mcp.tool
async def polymarket_create_order(
    market_id: str = Field(..., description="Market ID or slug"),
    outcome: str = Field(..., description="YES or NO"),
    side: str = Field(..., description="BUY or SELL"),
    price: float = Field(..., ge=0.01, le=0.99, description="Price in dollars (0.01-0.99)"),
    size: float = Field(..., gt=0, description="Number of shares"),
    order_type: str = Field(default="GTC", description="GTC, FOK, or IOC"),
    ctx: Context = None
) -> dict:
    """
    Create a limit order on Polymarket.

    This places a signed order on the Polymarket CLOB. The order will be settled
    on-chain (Polygon) when matched. You maintain custody of your funds at all times.

    Example: polymarket_create_order(
        market_id="will-bitcoin-reach-100k-2025",
        outcome="YES",
        side="BUY",
        price=0.43,
        size=100,
        order_type="GTC"
    )
    """
    if ctx:
        await ctx.info(f"Creating order: {side} {size} {outcome} @ ${price}")

    # Get market details (need token ID)
    gamma = GammaClient()
    market = await gamma.get_market(market_id)

    if not market.accepting_orders:
        raise ValueError(f"Market {market_id} is not accepting orders")

    # Determine token ID based on outcome
    token_id = market.get_token_id(outcome)

    # Build order params
    order_params = OrderParams(
        token_id=token_id,
        side=side,
        price=price,
        size=size,
        order_type=order_type,
        neg_risk=market.neg_risk
    )

    # Submit order to CLOB
    clob = ClobClient.from_env()
    result = await clob.create_order(order_params)

    if ctx:
        await ctx.info(f"Order placed: {result.order_id} - {result.status}")

    return {
        "status": "success",
        "order_id": result.order_id,
        "market": market.question,
        "outcome": outcome,
        "side": side,
        "price": price,
        "size_requested": size,
        "size_filled": result.filled_size,
        "message": f"Order {result.order_id} placed successfully"
    }
```

---

## Configuration

### Environment Variables

```bash
# Wallet Configuration (REQUIRED)
POLYMARKET_PRIVATE_KEY=<your_polygon_wallet_private_key>

# For Magic link / Browser wallet users (OPTIONAL)
POLYMARKET_PROXY_ADDRESS=<your_polymarket_proxy_wallet_address>
POLYMARKET_SIGNATURE_TYPE=1  # 1=Magic, 2=Browser wallet, omit for EOA

# API Endpoints
POLYMARKET_CLOB_ENDPOINT=https://clob.polymarket.com
POLYMARKET_GAMMA_ENDPOINT=https://gamma-api.polymarket.com
POLYMARKET_CHAIN_ID=137  # Polygon mainnet

# Safety Limits (Phase 1)
POLYMARKET_MAX_ORDER_SIZE=100
POLYMARKET_DAILY_ORDER_LIMIT=50
POLYMARKET_LARGE_ORDER_THRESHOLD=50
POLYMARKET_MAX_BALANCE_USAGE_PCT=25

# Optional: Pre-derived API credentials
POLYMARKET_API_KEY=<optional>
POLYMARKET_API_SECRET=<optional>
POLYMARKET_API_PASSPHRASE=<optional>
```

### Wallet Setup Guide

**Option 1: Magic Link / Email Login**
1. Sign up at polymarket.com with email
2. Export private key from Magic Link (https://reveal.magic.link/polymarket)
3. Copy your Polymarket proxy address (shown below profile picture)
4. Set `POLYMARKET_SIGNATURE_TYPE=1`

**Option 2: Browser Wallet (MetaMask, etc)**
1. Connect wallet to polymarket.com
2. Export private key from your wallet extension
3. Copy your Polymarket proxy address
4. Set `POLYMARKET_SIGNATURE_TYPE=2`
5. **Important**: Set allowances for USDC spending

**Option 3: Direct EOA**
1. Use your own Polygon wallet
2. Fund with USDC on Polygon network
3. No proxy address or signature type needed
4. Full control, but requires blockchain knowledge

---

## Testing Strategy

### Comprehensive Integration Testing

**Philosophy: Test Against Live Polymarket**
- Use Polygon Mumbai testnet when available
- Otherwise, use mainnet with small amounts
- Test signature generation before submission
- VCR cassettes for market data endpoints (no auth)

### Test Fixtures

```python
# tests/conftest.py
import pytest
from src.polymarket.gamma_client import GammaClient
from src.polymarket.clob_client import ClobClient

@pytest.fixture(scope="session")
async def gamma_client():
    """Gamma client (no auth required)."""
    return GammaClient()

@pytest.fixture(scope="session")
async def clob_client():
    """CLOB client with test wallet."""
    # Use dedicated test wallet with small USDC balance
    return ClobClient.from_env(test_mode=True)

@pytest.fixture(scope="session")
async def active_market(gamma_client):
    """Find an active, tradeable market."""
    markets = await gamma_client.list_markets(
        closed=False,
        limit=50,
        order="volume_24h",
        ascending=False
    )

    for market in markets:
        if (market.accepting_orders and
            market.volume_24h > 1000 and
            market.best_bid and market.best_ask):
            return market

    pytest.skip("No suitable market found")

@pytest.fixture
async def fresh_balance(clob_client):
    """Get current USDC balance."""
    return await clob_client.get_balance()
```

### Integration Test Structure

```python
# tests/polymarket/integration/test_trading.py
class TestOrderExecution:
    @pytest.mark.asyncio
    async def test_create_limit_order(self, active_market, fresh_balance):
        """Can create limit order on active market."""
        # Create order well away from market (won't fill)
        result = await polymarket_create_order(
            market_id=active_market.id,
            outcome="YES",
            side="BUY",
            price=0.01,  # Very low, won't fill
            size=1
        )

        assert result["status"] == "success"
        assert result["order_id"] is not None

        # Cleanup: cancel
        await polymarket_cancel_order(order_id=result["order_id"])

    @pytest.mark.asyncio
    async def test_signature_validation(self, active_market):
        """EIP-712 signatures are valid."""
        from src.polymarket.signing import sign_order

        order_params = OrderParams(
            token_id=active_market.clob_token_ids[0],
            side="BUY",
            price=0.50,
            size=1
        )

        signature = sign_order(os.getenv("POLYMARKET_PRIVATE_KEY"), order_params)

        # Signature should be valid hex
        assert signature.startswith("0x")
        assert len(signature) == 132  # 0x + 130 hex chars
```

---

## Success Metrics

### Phase 1 Targets

**Functionality:**
- ✅ All 12 Phase 1 tools implemented and tested
- ✅ EIP-712 signing works correctly
- ✅ Orders execute successfully on mainnet
- ✅ Zero wallet-draining bugs (critical!)

**LLM Usability:**
- ✅ LLM can discover markets via natural language
- ✅ LLM can analyze orderbooks and make informed decisions
- ✅ LLM can execute trades and report results clearly
- ✅ Error recovery: LLM handles failed orders gracefully

**Safety:**
- ✅ All order validations working (size, balance, market status)
- ✅ Non-custodial: user retains control of funds
- ✅ Audit trail captures all order attempts
- ✅ On-chain settlement verified

---

## Comparison: Polymarket vs Kalshi

| Feature | Polymarket | Kalshi |
|---------|-----------|--------|
| **Architecture** | Blockchain (Polygon) | Centralized |
| **Custody** | Non-custodial | Custodial |
| **Authentication** | EIP-712 wallet signing | API key |
| **Settlement** | On-chain (public) | Off-chain (private) |
| **Fees** | 0% (currently) | Varies by volume |
| **Market Count** | 10,000+ | 1,000+ |
| **Real-time Data** | WebSocket (built-in) | Polling (no WS) |
| **Order Types** | Limit only | Limit + Market |
| **Batch Orders** | Yes (native) | Yes (advanced tier) |
| **Liquidity** | Variable (AMM + CLOB) | CLOB only |
| **Resolution** | UMA oracle | Internal |
| **API Complexity** | High (2 APIs, blockchain) | Medium |
| **Geographic Access** | Global (VPN-friendly) | US-restricted |

---

## Future Enhancements (Beyond Phase 4)

### Phase 5: Institutional Features
- **Automated Market Making**: Continuous two-sided quoting
- **Risk Management**: VaR, Greeks, scenario analysis
- **Backtesting Framework**: Historical strategy simulation
- **Multi-Account Management**: Trade from multiple wallets

### Phase 6: Social & Collaborative
- **Copy Trading**: Automatically follow top traders
- **Strategy Sharing**: Publish and subscribe to trading strategies
- **Group Positions**: Syndicated trading pools
- **Reputation System**: Track and display trader performance

### Phase 7: Cross-Chain Integration
- **L2 Bridges**: Arbitrum, Optimism, zkSync support
- **Multi-Chain Wallets**: Manage positions across chains
- **Cross-Chain Arbitrage**: Exploit price differences

---

## Development Roadmap

**Week 1-2: Foundation**
- Dual client architecture (Gamma + CLOB)
- EIP-712 signing utilities
- Core Pydantic models
- Basic FastMCP server structure
- Authentication flow (L1 + L2)

**Week 3-4: Market Discovery**
- Search and browse tools
- Market detail fetching
- Orderbook integration
- Price history charts
- Testing with live data

**Week 5-6: Trading**
- Order creation (with signing)
- Order cancellation
- Portfolio position tracking
- Fill history
- Integration testing with real orders

**Week 7-8: Polish & Safety**
- Comprehensive validation
- Error handling
- LLM conversation testing
- Documentation
- Safety audit

**Total: 8 weeks to production-ready Phase 1**

---

## Risk Assessment & Mitigation

### Technical Risks

**Risk: Private Key Exposure**
- **Mitigation**: Environment variable only, never log
- **Mitigation**: Support hardware wallet integration (future)
- **Mitigation**: Clear documentation on key security

**Risk: EIP-712 Signature Bugs**
- **Mitigation**: Extensive test coverage
- **Mitigation**: Validate against official Polymarket clients
- **Mitigation**: Dry-run mode for order testing

**Risk: On-Chain Transaction Failures**
- **Mitigation**: Gas estimation before submission
- **Mitigation**: Transaction monitoring and retry logic
- **Mitigation**: Clear error messages for blockchain failures

**Risk: Market Data Staleness**
- **Mitigation**: Timestamp all data
- **Mitigation**: Warn if data > X seconds old
- **Mitigation**: WebSocket streaming (Phase 3)

### Business Risks

**Risk: Polymarket API Changes**
- **Mitigation**: Version pin API calls
- **Mitigation**: Monitor changelog
- **Mitigation**: Comprehensive test suite catches breaks

**Risk: Regulatory Concerns**
- **Mitigation**: Clear user warnings
- **Mitigation**: Respect geographic restrictions
- **Mitigation**: Audit trail for compliance

**Risk: Slippage on Large Orders**
- **Mitigation**: Orderbook depth analysis before execution
- **Mitigation**: Suggest splitting large orders
- **Mitigation**: Price impact warnings

---

## Appendix: Example LLM Conversations

### Conversation 1: Market Research

**User:** "What are the most active prediction markets about AI right now?"

**LLM:** Let me search for AI-related markets on Polymarket.
*Calls: `polymarket_search("AI", sort_by="volume")`*

**LLM:** "I found 15 active AI markets. The top 3 by volume are:

1. **AGI by 2027** ($450K 24h volume)
   - Current price: 0.23 (23% chance)
   - Liquidity: $180K
   - Question: 'Will AGI be announced by any AI lab before 2027?'

2. **GPT-5 Release Date** ($320K 24h volume)
   - Current price: 0.67 (67% think before Q2 2025)

3. **AI Nobel Prize** ($215K 24h volume)
   - Current price: 0.41 (41% think AI will win Nobel by 2030)

Which one interests you?"

**User:** "The AGI one. What's the orderbook look like?"

**LLM:** *Calls: `polymarket_get_orderbook(market_id="agi-by-2027")`*

**LLM:** "Here's the AGI by 2027 orderbook:

**YES Side (AGI will be announced):**
- Best bid: $0.22 (50,000 shares)
- Best ask: $0.24 (30,000 shares)
- Spread: 2¢ (870 bps)

**NO Side (AGI won't be announced):**
- Best bid: $0.76 (40,000 shares)
- Best ask: $0.78 (25,000 shares)

The market is quite liquid. You could buy up to 30K shares of YES at $0.24 immediately, or place a limit order at $0.23 and likely get filled."

---

### Conversation 2: Trade Execution

**User:** "I want to buy 100 YES shares on the AGI market at $0.23"

**LLM:** Let me place that order for you.
*Calls: `polymarket_create_order(market_id="agi-by-2027", outcome="YES", side="BUY", price=0.23, size=100)`*

**LLM:** "✅ Order placed successfully!

**Order Details:**
- Order ID: 0x7f8a...
- Market: AGI by 2027
- Side: BUY YES
- Price: $0.23 per share
- Quantity: 100 shares
- Status: Pending (waiting for match)

**Potential Outcomes:**
- If filled at $0.23: Cost = $23.00
- If AGI is announced: Profit = $77.00 (335% ROI)
- If not: Loss = $23.00

Your order is now live on the Polymarket orderbook. I'll monitor for fills."

---

### Conversation 3: Portfolio Review

**User:** "What's my current portfolio?"

**LLM:** *Calls: `polymarket_get_positions()`*

**LLM:** "Here's your portfolio summary:

**Open Positions (4):**

1. **AGI by 2027**
   - Position: 100 YES @ avg $0.23
   - Current price: $0.24
   - P&L: +$1.00 (+4.3%)

2. **Bitcoin $100K by 2025**
   - Position: 250 YES @ avg $0.42
   - Current price: $0.45
   - P&L: +$7.50 (+7.1%)

3. **Trump 2024**
   - Position: 500 NO @ avg $0.31
   - Current price: $0.28
   - P&L: +$15.00 (+9.7%)

4. **Ethereum $5K by 2025**
   - Position: 150 YES @ avg $0.58
   - Current price: $0.55
   - P&L: -$4.50 (-5.2%)

**Portfolio Metrics:**
- Total position value: $289.00
- Unrealized P&L: +$19.00 (+7.0%)
- Markets traded: 12
- Win rate: 67% (8/12 closed positions profitable)"

---

## Implementation Checklist

### Pre-Development
- [ ] Review Polymarket Terms of Service
- [ ] Set up test wallet with small USDC balance
- [ ] Test EIP-712 signing against official client
- [ ] Understand token allowances (MetaMask users)

### Phase 1 Development
- [ ] Dual client architecture (Gamma + CLOB)
- [ ] EIP-712 signing implementation
- [ ] API key derivation flow
- [ ] 12 Phase 1 MCP tools
- [ ] Pydantic models for all data types
- [ ] Comprehensive test suite
- [ ] Safety validation layer
- [ ] Documentation

### Testing & Quality
- [ ] Unit tests for all signing functions
- [ ] Integration tests against live API
- [ ] End-to-end trading workflow test
- [ ] LLM conversation testing
- [ ] Security audit (key handling)
- [ ] Performance testing (large orders)

### Deployment
- [ ] Environment configuration guide
- [ ] Wallet setup instructions
- [ ] MCP server registration
- [ ] User onboarding documentation
- [ ] Troubleshooting guide

---

## Conclusion

The Polymarket MCP Server will provide a powerful, LLM-friendly interface to the world's largest prediction market platform. By leveraging blockchain technology and non-custodial trading, it offers unique advantages over centralized alternatives like Kalshi.

**Key Success Factors:**
1. **Robust EIP-712 signing** - Critical for security and functionality
2. **Dual-client architecture** - Clean separation of concerns (data vs trading)
3. **LLM-first design** - Natural language interfaces, human-readable errors
4. **Safety by default** - Multiple validation layers, non-custodial custody
5. **Comprehensive testing** - Catch signature bugs before they cost users money

**Next Steps:**
1. Review and approve this PRD
2. Set up development environment
3. Implement core authentication and signing
4. Build and test Phase 1 tools
5. Iterate based on user feedback

With this foundation, we can create a sophisticated trading interface that empowers LLM agents to make informed decisions on Polymarket's massive marketplace.
