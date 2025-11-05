# Kalshi API Gotchas

This directory documents known issues, quirks, and workarounds when working with the Kalshi API.

## Quick Reference

| Issue | Severity | Status | Impact |
|-------|----------|--------|---------|
| [No Text Search API](no_text_search_api.md) | High | API Limitation | Natural language search doesn't work - requires client-side filtering |
| [Action/Side Semantics](action_side_semantics.md) | High | Undocumented Behavior | Order reconciliation breaks |
| [MVE Market Explosion](mve_market_explosion.md) | High | Working as Intended | 45x cost overrun risk |
| [Market Orders Deprecated](market_orders_deprecated.md) | High | Confirmed | Breaking change - requires price on all orders |
| [Negative Liquidity in Settled Markets](negative_liquidity_settled_markets.md) | Medium | Confirmed | Validation failures on ~1-2% of markets |

## Overview

Kalshi's API has several known issues that can cause confusion or incorrect behavior. These are documented here to help future developers avoid spending time debugging the same problems.

## Known Issues

### No Text Search API
**File**: `no_text_search_api.md`

Kalshi's API does not provide any text search capability. Searching for "election" or "Bitcoin" doesn't work because the API only supports exact filtering by specific fields (event_ticker, series_ticker). Natural language search queries fail.

**Status**: Confirmed - API Limitation (2025-11-03)
**Severity**: High (breaks expected search behavior)
**Workaround**: Implement client-side filtering (fetch all markets, filter locally) or use series ticker mapping

---

### Confusing Action/Side Field Semantics (GetFills endpoint)
**File**: `action_side_semantics.md`

The GetFills endpoint reports action/side fields in a confusing way. When you SELL NO, the API reports this as SELL YES in responses. Similarly, SELL YES becomes SELL NO. This is because Kalshi normalizes sell orders to economically equivalent buy orders (sell NO at 75¢ = buy YES at 25¢), but reports the normalized form instead of what you requested.

**Status**: Confirmed - Undocumented behavior (2025-10-28, via Discord)
**Severity**: High (breaking change risk if Kalshi "fixes" this)
**Workaround**: Community recommends ignoring `action` field entirely and only tracking `side` field (assuming all trades are buys)

---

### MVE Market Explosion (NFL Parlays)
**File**: `mve_market_explosion.md`

Kalshi's NFL MVE (Multivariate Event) parlay markets create massive volumes that dwarf traditional binary markets. At peak, there are 251,979 total markets with only 20,542 (8.2%) being non-MVE. This creates significant cost and performance challenges for systems that scan all markets.

**Status**: Confirmed - Working as Intended (2025-10-28, via Discord)
**Severity**: High (cost & performance impact)
**Workaround**: Filter using `mve_collection_ticker` and `mve_selected_legs` fields. Kalshi is developing official API support for excluding MVE markets.

**Cost Impact**: Scanning all markets costs $5.02/scan ($150/month daily), vs $0.41/scan ($12/month) for non-MVE only (92% reduction)

---

### Market Orders Deprecated - All Orders Are Limit Orders
**File**: `market_orders_deprecated.md`

Kalshi has deprecated market orders. All orders now require a `price` parameter and are executed as limit orders. The API will reject any order submission that attempts to use a market order type or omits the price parameter.

**Status**: Confirmed (2025-10-28)
**Severity**: High (breaking change for order execution)
**Workaround**: Use extreme limit prices to simulate market orders:
- **BUY orders**: Use `price: 0.99` (will match any ask)
- **SELL orders**: Use `price: 0.01` (will match any bid)

**⚠️ Risk**: Extreme limit prices introduce slippage risk in thin order books. Recommended to use current market price + buffer instead (e.g., `best_ask + 0.02` for buys).

---

### Negative Liquidity Values in Settled Markets
**File**: `negative_liquidity_settled_markets.md`

Some markets (primarily settled NFL games) return negative liquidity values (e.g., `-36,792,779.0`), causing Pydantic validation errors when using `Field(ge=0.0)` constraints.

**Status**: Confirmed - Post-Settlement Accounting Artifact (2025-10-30)
**Severity**: Medium (affects ~1-2% of markets, causes parse failures)
**Workaround**: Remove `ge=0.0` validation constraint, use negative values as settled market indicator

**Pattern**: Only observed in past NFL games (Oct 26-30, 2025), appears to be post-settlement accounting balance rather than market depth.

**Recommended Fix**:
```python
# Remove ge=0.0 constraint
liquidity: float = Field(description="Liquidity or post-settlement balance")

# Add detection property
@property
def is_likely_settled(self) -> bool:
    return self.liquidity < 0
```

---

## Contributing

When you discover a new Kalshi API gotcha:

1. Create a new markdown file: `short_description.md` (no numbering)
2. Use the template below
3. Update this README with a link and summary in the Quick Reference table

### Template

```markdown
# Issue Title

**Discovered**: YYYY-MM-DD
**Status**: Confirmed | Suspected | Resolved
**Severity**: Low | Medium | High | Critical

## Description

[Clear description of the issue]

## Evidence

[Examples, API responses, screenshots]

## Impact

[How this affects your code/system]

## Workaround

[Any known workarounds, or "None" if unavailable]

## Related Issues

[Links to other gotchas or external resources]
```

---

## Report New Issues

If you discover a new Kalshi API issue that's not documented here, please:
1. Add it to this directory using the template above
2. Consider reporting it to Kalshi support if it's blocking
3. Update the main project documentation if needed
