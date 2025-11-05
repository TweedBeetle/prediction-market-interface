# Market Orders Deprecated - All Orders Are Limit Orders

**Discovered**: 2025-10-28
**Status**: Confirmed
**Severity**: HIGH

## Description

Kalshi has deprecated market orders. **All orders now require a price parameter and are executed as limit orders**. The API will reject any order submission that attempts to use a market order type or omits the price parameter.

This is a breaking change for systems that previously relied on market orders for immediate execution.

## Evidence

From Kalshi API behavior (confirmed 2025-10-28):
- Market order type is no longer supported
- All order submissions must include a `price` parameter
- Orders without explicit price will be rejected

## Impact

### Code Changes Required

Any order submission code must:
1. Always specify `type: "limit"` (or equivalent in your SDK)
2. Always provide a `price` parameter
3. Remove any logic that attempts to use market orders

### Execution Behavior

**Before (Market Orders)**:
```json
{
  "type": "market",
  "action": "buy",
  "side": "yes",
  "count": 100
}
```
→ Immediate execution at best available price

**After (Limit Orders Only)**:
```json
{
  "type": "limit",
  "action": "buy",
  "side": "yes",
  "count": 100,
  "price": 0.75
}
```
→ Execution only if price is available at or better than 0.75

## Workaround: Simulating Market Orders

To simulate immediate execution (market order behavior) with limit orders, use **extreme limit prices**:

### For BUY orders (YES or NO)
```json
{
  "type": "limit",
  "action": "buy",
  "side": "yes",
  "count": 100,
  "price": 0.9900  // High price = likely to fill immediately
}
```

### For SELL orders (YES or NO)
```json
{
  "type": "limit",
  "action": "sell",
  "side": "yes",
  "count": 100,
  "price": 0.0100  // Low price = likely to fill immediately
}
```

### Price Selection Guidelines

**BUY (want immediate fill)**:
- Use `price: 0.99` to simulate "buy at market"
- This says "I'll pay up to 99¢" which will match against any ask
- More conservative: Use current best ask + small buffer (e.g., `ask_price + 0.02`)

**SELL (want immediate fill)**:
- Use `price: 0.01` to simulate "sell at market"
- This says "I'll sell for as low as 1¢" which will match against any bid
- More conservative: Use current best bid - small buffer (e.g., `bid_price - 0.02`)

## Risks of Extreme Limit Prices

⚠️ **CRITICAL**: Using extreme limit prices (0.99 for buys, 0.01 for sells) introduces **slippage risk**:

1. **Thin Order Books**: If the order book has gaps, you may fill at much worse prices than expected
   - Example: Best ask is 0.60, but only 10 contracts available. Remaining 90 contracts fill at 0.75
   - Your 0.99 limit means you'll accept ANY price up to 0.99

2. **Flash Crashes / Spikes**: Temporary price dislocations can cause catastrophic fills
   - Example: Best bid temporarily drops to 0.10 due to large sell order
   - Your 0.01 limit means you'll sell at 0.10 instead of expected 0.55

3. **Partial Fills at Multiple Prices**: Large orders may fill across multiple price levels
   - Example: Buy 100 contracts with 0.99 limit
   - Fill: 20 @ 0.60, 30 @ 0.65, 50 @ 0.70
   - Average fill price: 0.66 (vs expected 0.60)

### Recommended Mitigation

**Option 1: Use Current Market Price + Buffer**
```python
# For BUY orders
current_ask = get_best_ask(market)
limit_price = min(current_ask + 0.02, 0.99)  # Add 2pp buffer, cap at 0.99

# For SELL orders
current_bid = get_best_bid(market)
limit_price = max(current_bid - 0.02, 0.01)  # Subtract 2pp buffer, floor at 0.01
```

**Option 2: Use Mid-Price + Larger Buffer**
```python
# More aggressive fill, less slippage risk than 0.99/0.01
mid_price = (best_bid + best_ask) / 2

# For BUY orders
limit_price = min(mid_price + 0.05, 0.99)  # Add 5pp buffer

# For SELL orders
limit_price = max(mid_price - 0.05, 0.01)  # Subtract 5pp buffer
```

**Option 3: Query Order Book Depth**
```python
# Most conservative - check total liquidity at each price level
order_book = get_order_book(market)
required_contracts = 100

# For BUY orders - find worst price needed to fill completely
cumulative = 0
worst_price = 0
for level in order_book.asks:
    cumulative += level.size
    worst_price = level.price
    if cumulative >= required_contracts:
        break

limit_price = worst_price + 0.01  # Add 1pp buffer beyond worst expected price
```

## Implementation Checklist

When updating order submission code:

- [ ] Remove all market order logic
- [ ] Add price parameter to all order submissions
- [ ] Decide on price selection strategy (extreme vs conservative)
- [ ] Add order book depth checking if using large position sizes
- [ ] Add post-execution validation (compare fill price to expected)
- [ ] Add slippage monitoring and alerts
- [ ] Update test fixtures to include price parameter
- [ ] Update documentation to reflect limit-only behavior

## Related Issues

- **03_action_side_semantics.md** - Order reconciliation after fills
- **01_volume_always_zero.md** - Can't validate market liquidity before order placement

## Additional Notes

This change makes Kalshi's order execution more transparent (you control max price) but requires more sophisticated order submission logic to avoid adverse fills. Systems must now explicitly manage the trade-off between fill probability and price slippage.

**Production Recommendation**: Use conservative limit prices (Option 1 or 2 above) rather than extreme prices (0.99/0.01) to avoid catastrophic slippage in thin markets.
