# Polymarket Phase 2 Scope

**Based on:** API documentation review (November 5, 2025)
**Status:** Planning

---

## Phase 2 Features (From API Docs)

After reviewing the Polymarket CLOB API documentation, here are the Phase 2 features available:

### 1. Market Orders (FOK/FAK Order Types)

**Available Order Types:**
- **FOK (Fill-Or-Kill)**: Execute immediately and fully, or cancel entirely
  - Use case: "Buy at market price, but only if I can get the full amount now"
  - Perfect for: Quick entries, avoiding partial fills

- **FAK (Fill-And-Kill)**: Execute what's available immediately, cancel the rest
  - Use case: "Buy as much as possible right now, don't leave remainder on book"
  - Perfect for: Large orders that may not fill completely

- **GTC (Good-Til-Cancelled)**: Already implemented in Phase 1
  - Limit order that rests on book until filled or cancelled

- **GTD (Good-Til-Date)**: Limit order with expiration timestamp
  - Use case: "Keep order active for 24 hours, then auto-cancel"
  - Perfect for: Time-limited opportunities

**Implementation Notes:**
- Polymarket says: "All orders are limit orders, but market orders are supported"
- Market orders = limit orders with aggressive pricing + FOK/FAK type
- For buy: Price = best ask or higher (execute against sellers)
- For sell: Price = best bid or lower (execute against buyers)

---

### 2. Batch Order Operations

**Endpoint:** `POST /orders` (note the plural)

**Capabilities:**
- Create up to **15 orders in a single request**
- Each order can have different: token, side, price, size, order type
- All orders signed independently
- Atomic-ish: Some may succeed while others fail

**Use Cases:**
- **Spread trading**: Simultaneously buy and sell related markets
- **Portfolio rebalancing**: Close multiple positions at once
- **OCO strategies**: Place conditional orders (though not truly atomic)
- **Efficiency**: Reduce API calls and latency

**Response:**
- Returns array of results (one per order)
- Each result has: success, errorMsg, orderId, orderHashes, status

---

### 3. Batch Cancel Operations

**Four Cancel Endpoints:**

#### A. Cancel Single Order (Phase 1)
`DELETE /order` - Already implemented

#### B. Cancel Multiple Orders
`DELETE /orders` - Cancel specific list of order IDs
- Takes array of order IDs
- Returns: canceled array + not_canceled map with reasons

#### C. Cancel ALL Orders
`DELETE /cancel-all` - Cancel every active order
- No parameters needed
- Use case: "Emergency exit, cancel everything"
- Returns: canceled array + not_canceled map

#### D. Cancel Orders by Market
`DELETE /cancel-market-orders` - Cancel orders for specific market or token
- Parameters: market (condition ID) or asset_id (token ID)
- Use case: "Exit all positions in Bitcoin markets"
- Returns: canceled array + not_canceled map

**Implementation Notes:**
- All cancel endpoints return same response format
- not_canceled map explains why each failed cancel happened
- Reasons: order already filled, order doesn't exist, etc.

---

### 4. Position Management Helpers

**New Tools to Add:**

#### Close Position Tool
- Gets current position
- Fetches orderbook
- Creates opposite-side order at best price
- Monitors execution
- Confirms position closed

#### Close All Positions Tool
- Lists all positions
- For each position: Get orderbook, create sell order
- Uses batch order creation for efficiency
- Returns summary of closed positions

#### Calculate Portfolio Metrics Tool
- Aggregate P&L across all positions
- Win rate calculation
- Average hold time
- Total fees paid

---

## Phase 2 Scope (What We'll Implement)

### New Models (4 models)

1. **OrderType** (enum) - FOK, FAK, GTC, GTD
2. **BatchOrderRequest** - Container for multiple orders
3. **BatchOrderResponse** - Results from batch creation
4. **CancelResponse** - Standard cancel response format

### New Client Methods (7 methods)

**ClobClient additions:**

1. `create_market_order()` - Helper to create FOK/FAK orders with market pricing
2. `create_gtd_order()` - Create order with expiration timestamp
3. `create_orders_batch()` - Create up to 15 orders in one call
4. `cancel_orders_batch()` - Cancel multiple orders by ID list
5. `cancel_all_orders()` - Cancel all active orders
6. `cancel_market_orders()` - Cancel orders for specific market/token
7. `close_position()` - Helper to close a single position

### New MCP Tools (8 tools)

**Total Phase 1+2: 20 tools**

1. `polymarket_create_market_order` - Create FOK/FAK market order
2. `polymarket_create_gtd_order` - Create order with expiration
3. `polymarket_create_orders_batch` - Create multiple orders at once
4. `polymarket_cancel_orders_batch` - Cancel specific list of orders
5. `polymarket_cancel_all_orders` - Cancel all active orders
6. `polymarket_cancel_market_orders` - Cancel orders for market/token
7. `polymarket_close_position` - Close a single position
8. `polymarket_close_all_positions` - Close all positions

### Updated Tests

**Unit Tests (add ~15 tests):**
- OrderType enum tests
- Market order creation logic tests
- GTD order expiration validation tests
- Batch order signing tests
- Cancel response parsing tests

**Integration Tests (add ~12 tests):**
- Market order execution (requires funds, skipped by default)
- GTD order creation and cancellation
- Batch order creation (all succeed, some fail)
- Cancel multiple orders
- Cancel all orders
- Cancel by market
- Close position workflow

---

## What's NOT in Phase 2

### Order Amendment
- **Why not:** Polymarket API doesn't have amendment endpoint
- **Workaround:** Users can cancel + recreate manually
- **Future:** Could add helper tool that does cancel + recreate atomically

### WebSocket Subscriptions
- **Why not:** Complex, requires separate connection management
- **Defer to:** Phase 3 (Real-time Data)
- **Scope:** Market data streams, user event notifications

### Blockchain Operations
- **Why not:** Requires web3 integration, gas management
- **Defer to:** Phase 3 (Blockchain Integration)
- **Scope:** Check balances, approve USDC, claim winnings

### Advanced Analytics
- **Why not:** Requires historical data aggregation
- **Defer to:** Phase 3 (Market Analysis)
- **Scope:** Price charts, volume analysis, sentiment

---

## Implementation Plan

### Step 1: Update Models (30 minutes)

```python
# Add to models.py

class OrderType(str, Enum):
    """Order type enum."""
    FOK = "FOK"  # Fill-Or-Kill
    FAK = "FAK"  # Fill-And-Kill
    GTC = "GTC"  # Good-Til-Cancelled (default)
    GTD = "GTD"  # Good-Til-Date

class BatchOrderResult(BaseModel):
    """Result from batch order creation."""
    success: bool
    error_msg: str = Field(default="", alias="errorMsg")
    order_id: Optional[str] = Field(None, alias="orderId")
    order_hashes: List[str] = Field(default_factory=list, alias="orderHashes")
    status: Optional[str] = None  # matched, live, delayed, unmatched

class CancelResponse(BaseModel):
    """Response from cancel operations."""
    canceled: List[str] = Field(default_factory=list)
    not_canceled: Dict[str, str] = Field(default_factory=dict, alias="notCanceled")
```

### Step 2: Update ClobClient (2 hours)

Add 7 new methods with proper:
- EIP-712 signing for orders
- L2 header authentication
- Error handling
- Batch processing logic

### Step 3: Update MCP Server (1 hour)

Add 8 new tools with:
- Clear descriptions
- Input validation
- Safety warnings (market orders use real money!)
- Context logging for LLM

### Step 4: Write Tests (2 hours)

- Unit tests for all new models
- Integration tests for all new client methods
- Mark funded tests as skippable

### Step 5: Documentation (1 hour)

- Update testing guide with Phase 2 workflows
- Document order types and use cases
- Add examples for batch operations

**Total Estimated Time:** 6-7 hours

---

## Success Criteria

### Functionality
- ✅ All 8 new tools working via MCP
- ✅ Market orders execute correctly
- ✅ Batch operations handle partial failures
- ✅ Cancel operations work for all variants

### Testing
- ✅ All unit tests passing
- ✅ Integration tests pass (when funded)
- ✅ Phase 1 regression tests still pass

### Documentation
- ✅ Testing guide updated with Phase 2 workflows
- ✅ All tools have clear descriptions
- ✅ Safety warnings for dangerous operations

### User Experience
- ✅ Claude understands market order vs limit order
- ✅ Claude can suggest batch operations
- ✅ Claude warns about FOK/FAK risks

---

## Risk Assessment

### Low Risk
- ✅ GTD orders (just adds expiration field)
- ✅ Batch cancel operations (safe, just cancels)
- ✅ Models and enums (pure data structures)

### Medium Risk
- ⚠️ Batch order creation (complex, many failure modes)
- ⚠️ Close position helper (involves market orders)
- ⚠️ Integration tests (may hit API rate limits)

### High Risk
- 🚨 Market orders (immediate execution, no price guarantee)
- 🚨 Cancel all orders (accidental use could exit everything)
- 🚨 FOK orders (all-or-nothing, may fail unexpectedly)

**Mitigation:**
- Add explicit confirmations for dangerous operations
- Log all operations clearly for user visibility
- Provide dry-run mode for testing
- Add safety limits (max batch size, etc.)

---

## Phase 3 Preview

After Phase 2, possible Phase 3 features:

1. **WebSocket Subscriptions**
   - Real-time orderbook updates
   - User event notifications
   - Trade stream monitoring

2. **Blockchain Integration**
   - Check USDC/MATIC balances
   - Approve token spending
   - Claim winnings from won positions
   - Split/merge conditional tokens

3. **Market Analysis**
   - Price history charts
   - Volume analysis
   - Market sentiment indicators
   - Arbitrage opportunity detection

4. **Advanced Strategies**
   - OCO (One-Cancels-Other) coordination
   - Stop-loss automation
   - Portfolio rebalancing
   - Cross-market hedging

**Phase 3 Estimate:** 2-3 weeks (15+ additional tools)

---

**Document Version:** 1.0
**Last Updated:** November 5, 2025
**Status:** Ready to Begin Phase 2 Implementation
