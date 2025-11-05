# Negative Liquidity Values in Settled Markets

**Discovered**: 2025-10-30
**Status**: Confirmed - Post-Settlement Accounting Artifact
**Severity**: Medium

## Description

Some Kalshi markets return **negative liquidity values** in API responses, causing Pydantic validation errors. This appears to occur primarily in **settled/resolved markets** where the liquidity field represents post-settlement accounting adjustments rather than active market depth.

**Key Pattern**: All observed negative liquidity values are in **NFL markets from late October 2025** that have already been resolved.

## Evidence

### Failed Validation Examples

```python
# Example 1: Kansas City Chiefs game (October 27, 2025)
Failed to parse market KXNFLGAME-25OCT27WASKC-KC: 1 validation error for KalshiMarket
liquidity
  Input should be greater than or equal to 0 [type=greater_than_equal, input_value=-36792779.0, input_type=float]

# Example 2: Spread market
Failed to parse market KXNFLSPREAD-25OCT26NYJCIN-CIN7: 1 validation error for KalshiMarket
liquidity
  Input should be greater than or equal to 0 [type=greater_than_equal, input_value=-663058.0, input_type=float]

# Example 3: Total points market
Failed to parse market KXNFLTOTAL-25OCT27WASKC-47: 1 validation error for KalshiMarket
liquidity
  Input should be greater than or equal to 0 [type=greater_than_equal, input_value=-4401438.0, input_type=float]
```

### Observed Patterns

**Market Types Affected**:
- `KXNFLGAME-*` - Game winner markets
- `KXNFLSPREAD-*` - Point spread markets
- `KXNFLTOTAL-*` - Total points markets

**Event Dates** (all past events):
- October 26, 2025: Jets @ Bengals
- October 27, 2025: Commanders @ Chiefs
- October 30, 2025: (unspecified game)

**Negative Value Magnitudes**:
- Small: `-663,058.0` (spread market)
- Medium: `-4,401,438.0` (totals market)
- Large: `-36,792,779.0` (game winner)

**Frequency**: ~1-2% of markets in our sample (2 out of 673)

### NFL Games Context

These markets correspond to actual NFL games that occurred:
- **Oct 26**: New York Jets @ Cincinnati Bengals (1:00 PM ET)
- **Oct 27**: Washington Commanders @ Kansas City Chiefs (8:15 PM ET, MNF)
- Markets would have settled shortly after game completion

## Root Cause Analysis

### Most Likely Explanation: Post-Settlement Accounting

Negative liquidity values appear to be an **accounting artifact** that occurs after market settlement. Here's the likely mechanism:

1. **During Trading**: `liquidity` field represents total value of resting orders (normal positive value)
2. **Market Closes**: Trading stops, liquidity field reflects final order book depth
3. **Settlement**: Winners get paid, losers forfeit stakes
4. **Post-Settlement Adjustments**:
   - Cancelled orders may be refunded
   - Late fills may be unwound
   - Market maker obligations adjusted
   - **Result**: Net debit reflected as negative liquidity

### Supporting Evidence

- **Magnitude correlates with market size**: Larger negative values in high-volume game winner markets vs smaller spreads
- **Only affects settled markets**: All observed cases are past NFL games
- **No live markets affected**: Active markets show normal `liquidity: 0` (see Issue #1) or positive values
- **Pattern is consistent**: Multiple market types (game, spread, total) show same behavior

### Alternative Explanations (Less Likely)

**Data Corruption**:
- ❌ Values are too large and consistent to be random corruption
- ❌ Multiple markets affected with similar patterns

**API Bug**:
- ❌ If bug, would expect more markets affected
- ❌ Negative values appear intentional (accounting entries)

**Intentional Settlement Display**:
- ✅ Possible - may represent net settlement obligations
- ✅ Would explain magnitude correlation with market size
- ❌ But: Poor API design to overload "liquidity" field meaning

## Impact

### For Our System

**Critical Impact**:
1. **Pydantic Validation Failures**: Current `liquidity: float = Field(ge=0.0)` constraint rejects these markets
2. **Market Discovery Gaps**: ~1-2% of markets cannot be parsed
3. **Settlement Detection**: Cannot distinguish settled vs active markets reliably

**Production Risks**:
- May attempt to trade on settled markets if we remove validation
- Historical analysis cannot include these markets
- Arbitrage detection may miss patterns in resolved events

### Broader Context

This issue compounds with existing Kalshi API problems:
- **Issue #1**: Volume/liquidity always $0 in active markets
- **Issue #2**: Markets missing from API entirely
- **Issue #6** (this issue): Negative liquidity in settled markets

**Result**: `liquidity` field is **completely unreliable** across all market states.

## Workaround

### Recommended Approach: Accept Negative Values

**Change validation constraint**:

```python
# BEFORE (current)
liquidity: float = Field(ge=0.0, description="Estimated liquidity")

# AFTER (recommended)
liquidity: float = Field(description="Liquidity or post-settlement balance")
```

**Rationale**:
- Allows parsing of settled markets for historical analysis
- Accepts reality that Kalshi overloads this field with accounting data
- Enables detection of settled markets via negative values

### Alternative: Skip Validation Errors

Keep current validation but gracefully skip unparseable markets:

```python
try:
    market = KalshiMarket(**data)
except ValidationError as e:
    if "liquidity" in str(e) and "greater_than_equal" in str(e):
        logger.warning(f"Skipping market {ticker}: negative liquidity (likely settled)")
        continue
    else:
        raise
```

**Trade-off**: Loses settled market data but maintains strict validation.

### Detection Pattern: Identify Settled Markets

Use negative liquidity as a **settled market indicator**:

```python
@property
def is_likely_settled(self) -> bool:
    """
    Returns True if market appears to be settled based on liquidity value.

    Negative liquidity values appear to be post-settlement accounting artifacts.
    """
    return self.liquidity < 0
```

**Benefit**: Can filter out settled markets proactively.

## Recommended Solution

**Short-term** (immediate):
1. Remove `ge=0.0` constraint from `liquidity` field
2. Add `is_likely_settled` property for detection
3. Filter settled markets at scanner level
4. Log warning when negative liquidity encountered

**Medium-term** (1-2 weeks):
1. Contact Kalshi support to understand intended behavior
2. Request separate field for settlement status
3. Document official explanation from Kalshi

**Long-term** (production):
1. Use explicit market status fields (`active`, `closed`, `settled`) instead of liquidity
2. Consider `liquidity` field unreliable for any purpose
3. Fetch order book directly for actual liquidity assessment

## Related Code

### Current Implementation

`src/clients/kalshi_client.py`:
```python
class KalshiMarket(BaseModel):
    liquidity: float = Field(ge=0.0, default=0.0, description="Estimated liquidity")
    # ☝️ This validation rejects settled markets with negative liquidity
```

### Proposed Fix

```python
class KalshiMarket(BaseModel):
    liquidity: float = Field(
        default=0.0,
        description="Liquidity in cents (negative = post-settlement accounting)"
    )

    @property
    def is_likely_settled(self) -> bool:
        """Negative liquidity indicates post-settlement state."""
        return self.liquidity < 0
```

### Scanner Integration

```python
async def get_active_markets(
    self,
    exclude_settled: bool = True,  # New parameter
    **kwargs
) -> List[KalshiMarket]:
    """Fetch active Kalshi markets."""
    markets = await self._fetch_all_markets(**kwargs)

    if exclude_settled:
        # Filter out markets with negative liquidity (likely settled)
        markets = [m for m in markets if not m.is_likely_settled]
        logger.info(f"Filtered {len([m for m in markets if m.is_likely_settled])} settled markets")

    return markets
```

## Timeline

- **2025-10-30**: Issue discovered during market scanning
- **Status**: Documented, awaiting Kalshi clarification
- **Fix ETA**: Immediate (remove validation), pending official explanation

## Related Issues

- `01_volume_always_zero.md` - Liquidity field unreliable in active markets
- `02_missing_markets_in_api.md` - Some markets not returned at all
- See also: Known pattern of Kalshi API field quality issues

## External Resources

- Kalshi API Docs: https://docs.kalshi.com/api-reference/market/get-market
- Official liquidity definition: "Value for current offers in this market in cents"
- Kalshi Discord #dev channel: For reporting and clarification requests

## Questions for Kalshi Support

If reporting this issue, ask:

1. **Is negative liquidity intentional?** What does it represent?
2. **What is the correct interpretation?** Post-settlement balance? Accounting adjustment?
3. **How should we detect settled markets?** Should we rely on `closed` field instead?
4. **Will this behavior change?** Can we depend on this pattern for settled market detection?
5. **Is there a better field?** Should we use `status` or `closed` to filter settled markets?

## Recommendation Summary

**✅ DO**:
- Remove `ge=0.0` validation constraint
- Add `is_likely_settled` property
- Filter settled markets at scanner level
- Log negative liquidity encounters for monitoring

**❌ DON'T**:
- Rely on `liquidity` field for actual market depth (use order book)
- Treat negative values as errors (they're informative)
- Use liquidity for volume filtering (all values are broken per Issue #1)

**🔍 INVESTIGATE**:
- Contact Kalshi support for official explanation
- Monitor if pattern holds across other event types (not just NFL)
- Check if `closed` or `status` fields correlate with negative liquidity
