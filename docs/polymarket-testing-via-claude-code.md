# Testing Polymarket MCP Server via Claude Code

**Purpose:** This guide provides step-by-step workflows for testing all Polymarket MCP tools through Claude Code's MCP integration.

**Prerequisites:**
- Polymarket MCP server registered with Claude Code
- `.env.polymarket` configured with wallet credentials
- USDC and MATIC on Polygon mainnet (for trading tests)
- Claude Code session running

---

## Setup Verification

### 1. Check MCP Server Connection

**In Claude Code:**
```
User: Check if the polymarket_mcp_server is connected
```

**Expected Response:**
- Claude should confirm the server is available
- Should list available tools (12 tools for Phase 1)

**If server not found:**
```bash
# Register the server
claude mcp add polymarket_mcp_server --scope project -- bash -c "cd /home/user/prediction-market-interface && uv run run_polymarket_mcp.py"

# Verify in .mcp.json
cat .mcp.json

# Check .claude/settings.json has enableAllProjectMcpServers: true
```

---

## Testing Workflow by Category

### Category 1: Market Discovery (No Auth Required)

**Test 1.1: Search Markets**

```
User: @polymarket_mcp_server search for "election" markets, show me the top 5 active markets
```

**Verify:**
- ✅ Returns 5 or fewer markets
- ✅ Each market has: question, ID, prices (best_bid, best_ask)
- ✅ Markets are active (not closed/archived)
- ✅ Has YES/NO token IDs

**What to look for:**
- Markets should be relevant to "election"
- Prices should be between 0 and 1 (probabilities)
- Volume and liquidity data (may be null for some markets)

---

**Test 1.2: Get Market Details**

```
User: @polymarket_mcp_server get details for market ID <market_id_from_search>
```

**Verify:**
- ✅ Returns detailed market information
- ✅ Has question, description, outcomes
- ✅ Has price data (best_bid, best_ask, last_price)
- ✅ Has volume and liquidity metrics
- ✅ Has clob_token_ids for YES/NO tokens

**What to look for:**
- Spread calculation (best_ask - best_bid)
- Midpoint price calculation
- Market interpretation (YES favored vs NO favored)

---

**Test 1.3: Get Orderbook**

```
User: @polymarket_mcp_server get the orderbook for token ID <yes_token_id_from_market>
```

**Verify:**
- ✅ Returns bids and asks arrays
- ✅ Each level has price and size
- ✅ Bids sorted descending (highest first)
- ✅ Asks sorted ascending (lowest first)
- ✅ Has best bid/ask prices

**What to look for:**
- Spread between best bid and best ask
- Depth of orderbook (total liquidity)
- Price levels near 0.5 (competitive markets)

---

**Test 1.4: List Events**

```
User: @polymarket_mcp_server list active events, show me the top 10
```

**Verify:**
- ✅ Returns events with titles and slugs
- ✅ Each event has market list
- ✅ Events have tags and descriptions
- ✅ Total volume calculated across markets

**What to look for:**
- Events are collections of related markets
- High-volume events (popular topics)
- Event categories (politics, sports, crypto, etc.)

---

**Test 1.5: Get Event Details**

```
User: @polymarket_mcp_server get details for event ID <event_id_from_list>
```

**Verify:**
- ✅ Returns full event with all markets
- ✅ Markets have complete data
- ✅ Event metadata (tags, descriptions)
- ✅ Total volume calculation

**What to look for:**
- Related markets within event
- Cross-market opportunities
- Event-level volume vs individual market volume

---

### Category 2: Authentication (Required Before Trading)

**Test 2.1: Authenticate Wallet**

```
User: @polymarket_mcp_server authenticate my wallet
```

**Verify:**
- ✅ Successfully signs EIP-712 message
- ✅ Returns API key, secret, passphrase
- ✅ Credentials stored in client
- ✅ No errors in authentication flow

**What to look for:**
- Signature creation (should take <1 second)
- API credentials returned (should see in context)
- Future requests should use these credentials

**If authentication fails:**
- Check `POLYMARKET_PRIVATE_KEY` in `.env.polymarket`
- Check `POLYMARKET_WALLET_ADDRESS` matches private key
- Verify private key has "0x" prefix
- Check network connectivity to Polymarket API

---

### Category 3: Portfolio Management (Auth Required)

**Test 3.1: Get Current Positions**

```
User: @polymarket_mcp_server show me my current positions
```

**Verify:**
- ✅ Returns list of positions (may be empty)
- ✅ Each position has: market_id, size, outcome
- ✅ Has P&L calculations (pnl_dollars, pnl_percentage)
- ✅ Shows profitable vs losing positions

**What to look for:**
- Positions should match actual holdings
- P&L should be accurate (check against UI)
- Size should be in contract units

**If positions missing:**
- Verify authentication completed
- Check if wallet actually has positions
- Try refreshing with a second call

---

**Test 3.2: Get Order History**

```
User: @polymarket_mcp_server show me my order history for the last 24 hours
```

**Verify:**
- ✅ Returns list of orders (may be empty)
- ✅ Each order has: id, market, price, size, side, status
- ✅ Has fill information (filled_size, fill_percentage)
- ✅ Orders sorted by timestamp (newest first)

**What to look for:**
- Order statuses: LIVE (pending), MATCHED (filled), CANCELED
- Fill percentage (0% = unfilled, 100% = fully filled)
- Order side (BUY = betting YES, SELL = betting NO)

**Filter options to test:**
```
# Get only live orders
User: @polymarket_mcp_server show me my active orders

# Get orders for specific market
User: @polymarket_mcp_server show me my orders for market <market_id>
```

---

**Test 3.3: Get Trade History**

```
User: @polymarket_mcp_server show me my recent trades
```

**Verify:**
- ✅ Returns list of executed trades (may be empty)
- ✅ Each trade has: market_id, price, size, side, timestamp
- ✅ Has total value calculation
- ✅ Trades sorted by timestamp

**What to look for:**
- Trades should match filled orders
- Price should be execution price
- Size should match order fill

**Filter options to test:**
```
# Get trades for specific market
User: @polymarket_mcp_server show me my trades for market <market_id>

# Get trades with limit
User: @polymarket_mcp_server show me my last 50 trades
```

---

### Category 4: Trading Operations (Auth + Funds Required)

⚠️ **WARNING: These tests use REAL MONEY on Polygon mainnet!**

**Pre-Trade Checklist:**
- [ ] Wallet has sufficient USDC balance
- [ ] Wallet has MATIC for gas fees
- [ ] Using small amounts for testing ($1-5 USD)
- [ ] Understanding market before trading
- [ ] Aware of bid/ask spread and liquidity

---

**Test 4.1: Create Limit Order (Safe Test)**

**Strategy:** Place order far from current price (unlikely to fill)

```
User: @polymarket_mcp_server I want to test creating an order.
Find an active election market with good liquidity.
Check the current best bid.
Place a BUY order 0.20 below the best bid for 1 contract.
This is just a test order that shouldn't fill.
```

**What Claude should do:**
1. Search for suitable market
2. Get orderbook to check best bid
3. Calculate safe price (far from market)
4. Create order with small size
5. Return order confirmation

**Verify:**
- ✅ Order created successfully
- ✅ Order ID returned
- ✅ Order appears in order history
- ✅ Order status is LIVE (not filled)
- ✅ Price is far enough to not fill

**Example values:**
- Market: "Will candidate X win?"
- Best bid: 0.65
- Test order price: 0.45 (0.20 below)
- Size: 1 contract
- Expected cost: ~$0.45

---

**Test 4.2: Cancel Order**

```
User: @polymarket_mcp_server cancel my order with ID <order_id_from_previous_test>
```

**Verify:**
- ✅ Order canceled successfully
- ✅ Cancellation confirmation returned
- ✅ Order no longer in active orders
- ✅ Funds returned to balance

**What to look for:**
- Cancellation should be instant
- Order should disappear from live orders
- No fill should have occurred

---

**Test 4.3: Create and Fill Order (Real Trade)**

⚠️ **EXTREME CAUTION: This will execute a real trade with real money!**

```
User: @polymarket_mcp_server I want to make a small real trade for testing.
Find a liquid market with tight spread.
Place a BUY order AT the current best ask for 1 contract.
This should fill immediately.
```

**What Claude should do:**
1. Find market with good liquidity
2. Get orderbook to find best ask
3. Create order at best ask price (market taker)
4. Order should fill immediately
5. Verify fill in trade history

**Verify:**
- ✅ Order created and filled
- ✅ Fill appears in trade history
- ✅ Position created in portfolio
- ✅ USDC balance decreased by cost
- ✅ Cost = price × size

**Example values:**
- Market: "Will Bitcoin be above $50k?"
- Best ask: 0.55
- Order: BUY 1 contract at 0.55
- Expected cost: $0.55 USDC
- Expected position: +1 YES token

**After trade:**
```
User: @polymarket_mcp_server show me my positions
```

Should see the new position with:
- Size: 1 contract
- Outcome: YES
- Entry price: 0.55

---

**Test 4.4: Close Position (Sell)**

```
User: @polymarket_mcp_server I want to close my position from the previous test.
Find the market, check the best bid, and sell my 1 YES token at the best bid price.
```

**What Claude should do:**
1. Get position details
2. Get current orderbook
3. Create SELL order at best bid
4. Verify trade execution
5. Confirm position closed

**Verify:**
- ✅ Order created and filled
- ✅ Position reduced to 0
- ✅ USDC balance increased
- ✅ Realized P&L calculated

**Example:**
- Position: +1 YES at 0.55 entry
- Best bid: 0.58
- Sell order: 1 contract at 0.58
- Revenue: $0.58 USDC
- P&L: +$0.03 (5.45% gain)

---

## Complete Workflow Tests

### Workflow 1: Market Research → Trade → Close

**Objective:** Complete trading lifecycle from research to exit

```
User: @polymarket_mcp_server Let's do a complete trading workflow.

1. Search for active political markets about the 2024 election
2. Pick one with good liquidity (>$100k)
3. Get the orderbook and analyze spread
4. If spread is tight (<5%), place a small test order
5. Monitor the order status
6. If it fills, check my position
7. Close the position at best price
8. Report final P&L
```

**Expected Claude behavior:**
- Uses search_markets tool
- Filters by liquidity
- Uses get_orderbook tool
- Calculates spread
- Uses create_order tool
- Uses get_order_history to monitor
- Uses get_positions to verify
- Uses create_order (SELL) to close
- Uses get_trades for P&L

**Verify complete flow:**
- ✅ All steps execute in sequence
- ✅ Data flows between steps (market ID, order ID, etc.)
- ✅ Trade logic is sound (buy low, sell high)
- ✅ Final P&L matches expectations

---

### Workflow 2: Portfolio Analysis

**Objective:** Comprehensive portfolio review

```
User: @polymarket_mcp_server Give me a complete portfolio analysis:

1. Show all my current positions
2. For each position, get the current market data
3. Calculate unrealized P&L
4. Show my order history (last 7 days)
5. Show my trade history (last 7 days)
6. Summarize total P&L and win rate
```

**Expected output:**
- List of positions with current values
- Market prices for each position
- Unrealized P&L per position
- Order history with fill rates
- Trade history with outcomes
- Summary statistics

---

### Workflow 3: Market Comparison

**Objective:** Compare related markets for arbitrage opportunities

```
User: @polymarket_mcp_server I want to compare related markets:

1. Search for all markets about "presidential election"
2. Get current prices for each
3. Look for inconsistencies (e.g., sum > 1.0)
4. Get orderbooks for interesting markets
5. Identify arbitrage opportunities
```

**Expected behavior:**
- Finds related markets
- Compares probabilities
- Identifies mispricing
- Suggests trades

**Look for:**
- Markets that sum to more than 100% probability
- Identical markets with different prices
- Correlated events with inconsistent pricing

---

## Error Handling Tests

### Test Error 1: Invalid Market ID

```
User: @polymarket_mcp_server get market details for ID "invalid_market_123"
```

**Expected:**
- ✅ Graceful error message
- ✅ Explains market not found
- ✅ Suggests using search instead

---

### Test Error 2: Unauthenticated Request

```
User: @polymarket_mcp_server show me my positions
# (Without authenticating first)
```

**Expected:**
- ✅ Error about missing authentication
- ✅ Instructs to authenticate first
- ✅ Doesn't crash

---

### Test Error 3: Invalid Order Parameters

```
User: @polymarket_mcp_server create an order with price 1.5
# (Price must be 0.001-0.999)
```

**Expected:**
- ✅ Validation error before API call
- ✅ Explains price constraints
- ✅ Suggests valid range

---

### Test Error 4: Insufficient Balance

```
User: @polymarket_mcp_server buy 10000 contracts at 0.50
# (Requires $5000 USDC)
```

**Expected:**
- ✅ API error about insufficient balance
- ✅ Shows required vs available balance
- ✅ Suggests smaller size

---

## Performance Tests

### Test Perf 1: Large Result Sets

```
User: @polymarket_mcp_server search for all active markets, limit 100
```

**Measure:**
- Response time (<5 seconds expected)
- Data completeness (all 100 markets)
- No timeout errors

---

### Test Perf 2: Rapid Sequential Calls

```
User: @polymarket_mcp_server
1. Get market A orderbook
2. Get market B orderbook
3. Get market C orderbook
4. Get market D orderbook
5. Get market E orderbook
```

**Measure:**
- All calls succeed
- Rate limiting handled
- No 429 errors
- Total time <10 seconds

---

## Regression Tests (After Code Changes)

**After ANY code changes to MCP server:**

1. **Restart Claude Code session** (critical - server is cached)
2. Run basic smoke test:
   ```
   User: @polymarket_mcp_server search for "test" markets
   ```
3. Verify response format unchanged
4. Run authentication test
5. Run one trade workflow test

---

## Common Issues & Solutions

### Issue 1: Server Not Found

**Symptom:** Claude says "polymarket_mcp_server not available"

**Solutions:**
1. Check `.mcp.json` exists in project root
2. Check `.claude/settings.json` has `enableAllProjectMcpServers: true`
3. Restart Claude Code session
4. Re-register server with correct command

---

### Issue 2: Authentication Fails

**Symptom:** "Invalid signature" or "Authentication failed"

**Solutions:**
1. Check `.env.polymarket` has correct private key
2. Verify private key has "0x" prefix
3. Check wallet address matches private key
4. Verify network connectivity
5. Try generating new API credentials on Polymarket

---

### Issue 3: Orders Not Filling

**Symptom:** Orders stay LIVE forever

**Solutions:**
1. Check price is at or better than market price
2. Verify market has liquidity
3. Check orderbook depth
4. Ensure market is still active
5. Wait longer (can take minutes for limit orders)

---

### Issue 4: Empty Results

**Symptom:** Tools return empty arrays

**Solutions:**
1. Verify authentication for portfolio tools
2. Check wallet actually has positions/trades
3. Try different search terms
4. Check market IDs are valid
5. Verify time ranges for history queries

---

## Test Checklist Template

Copy this checklist for each test session:

```
## Pre-Test
- [ ] Claude Code session restarted (if code changed)
- [ ] MCP server registered and connected
- [ ] Environment variables configured
- [ ] Wallet has USDC and MATIC (for trading tests)

## Market Discovery Tests
- [ ] Search markets by query
- [ ] Get market details
- [ ] Get orderbook
- [ ] List events
- [ ] Get event details

## Authentication Tests
- [ ] Authenticate wallet
- [ ] Verify credentials stored

## Portfolio Tests
- [ ] Get current positions
- [ ] Get order history
- [ ] Get trade history

## Trading Tests (CAUTION: REAL MONEY)
- [ ] Create limit order (far from market)
- [ ] Cancel order
- [ ] Create and fill order (at market)
- [ ] Close position

## Workflow Tests
- [ ] Complete trading lifecycle
- [ ] Portfolio analysis
- [ ] Market comparison

## Error Handling Tests
- [ ] Invalid market ID
- [ ] Unauthenticated request
- [ ] Invalid order parameters
- [ ] Insufficient balance

## Post-Test
- [ ] All tests documented
- [ ] Issues logged
- [ ] Balance verified (if traded)
- [ ] Positions closed (if opened)
```

---

## Success Criteria

**All tests should:**
- ✅ Complete without crashes
- ✅ Return valid data structures
- ✅ Handle errors gracefully
- ✅ Provide helpful error messages
- ✅ Execute in reasonable time (<5s per call)

**Trading tests should:**
- ✅ Execute trades correctly
- ✅ Update positions accurately
- ✅ Calculate P&L correctly
- ✅ Maintain data consistency

**User experience should:**
- ✅ Be intuitive (Claude understands requests)
- ✅ Be informative (Claude explains results)
- ✅ Be safe (Claude warns about real money)
- ✅ Be helpful (Claude suggests next steps)

---

## Testing Frequency

**Before every commit:**
- Smoke test (search markets)
- Authentication test

**Before every push:**
- All market discovery tests
- Authentication + portfolio tests
- One workflow test

**Before Phase 2:**
- Complete test checklist
- All workflows tested
- All error cases verified

**After Phase 2:**
- All Phase 1 tests (regression)
- All Phase 2 tests
- Integration between phases

---

## Reporting Issues

When filing issues, include:

1. **Test being run:** (e.g., "Test 1.1: Search Markets")
2. **User prompt:** Exact message sent to Claude
3. **Expected behavior:** What should happen
4. **Actual behavior:** What actually happened
5. **Error messages:** Full error text
6. **Environment:** OS, Claude Code version, Python version
7. **Server logs:** Check loguru output if available

---

**Document Version:** 1.0
**Last Updated:** November 5, 2025
**Status:** Ready for Phase 1 Testing
