# MVE Market Explosion (NFL Parlays)

**Discovered**: 2025-10-28 (via Discord discussion)
**Status**: Confirmed - Working as Intended
**Severity**: High (Cost & Performance Impact)

## Description

Kalshi's MVE (Multivariate Event) parlay markets, particularly NFL player props, create **massive market volumes** that dwarf traditional binary markets.

**Scale** (as of October 26, 2025):
- **251,979 total markets** at peak
- **Only 20,542 non-MVE markets** (8.2%)
- **231,437 NFL MVE parlays** (91.8%)

This creates significant challenges for systems that scan all markets:
- ❌ **High API pagination costs** (hundreds of pages to fetch all markets)
- ❌ **Expensive embedding costs** (251k × $0.00002 = $5.02 per scan)
- ❌ **Slow processing times** (filtering 250k+ markets per scan)
- ❌ **Low signal-to-noise** (most MVE parlays unlikely arbitrage candidates)

## Evidence

### Discord Conversation (2025-10-26)

User **Arbgame**:
> "FYI just refreshed, currently 107,122 events, 2,854 non-MVE, 251,979 markets, 20,542 non-MVE"

User **lactobacillus** (explaining weekly cycle):
> "weekly NFL MVE cycle, they just launched week 9 about an hour ago and markets are now being created as app users select new combos. peaks on sunday/monday, then they all settle, then it repeats"

User **Ilya9040**:
> "Thanks! So, 100K+ events from NFL only?"

User **lactobacillus**:
> "250k+ at peak this week, iirc!"

### Market Distribution

| Category | Count | Percentage |
|----------|-------|------------|
| Total Markets | 251,979 | 100% |
| NFL MVE Parlays | ~231,437 | 91.8% |
| Non-MVE Markets | 20,542 | 8.2% |
| Total Events | 107,122 | - |
| Non-MVE Events | 2,854 | 2.7% |

**Key Insight**: MVE markets outnumber traditional binary markets **11:1**.

### Weekly NFL Cycle

```
Week N Launch (Thursday)
    ↓
Markets Created as Users Select Combos (Thu-Sun)
    ↓
Peak Volume (Sunday/Monday) - 250k+ markets
    ↓
Markets Settle (Monday/Tuesday)
    ↓
Volume Drops (Tuesday-Thursday)
    ↓
Week N+1 Launch
```

## Impact

### For Our System

**Current approach** (scan all markets):
- **Stage 0 embeddings**: 251,979 markets × $0.00002 = **$5.02 per scan**
- **Monthly cost** (daily scans): $5.02 × 30 = **$150.60/month**
- **Budget**: Target is $3.34/month → **45x over budget**

**Performance issues**:
- API pagination: ~2,520 requests (100 markets/page)
- Embedding batching: ~1,008 batches (250 items/batch)
- Filter processing: 251,979 × 4,224 = **1.06 billion pairwise comparisons**

**Signal-to-noise**:
- Most NFL parlays are NOT cross-platform arbitrage candidates
- Polymarket doesn't offer equivalent parlay markets for most combos
- Processing 231k irrelevant markets to find ~20k relevant ones

### For Other Kalshi API Users

From Discord:

User **Ilya9040**:
> "omg. Is it possible to fetch all events except NFL? 🙂"

User **lactobacillus**:
> "i hear it's coming soon, @NotPikachu (Kalshi) might be able to provide more info"

User **NotPikachu (Kalshi)**:
> "Yeah its currently in development"

**Implication**: This is a widespread pain point, Kalshi is building API support to filter out NFL markets.

## Workaround (Current)

### Option 1: Filter by MVE Properties (Recommended)

User **lactobacillus** (current approach):
> "until then you can filter on the mve_collection_ticker and mve_selected_legs property and walk the hundreds of pages"

```python
# src/clients/kalshi_client.py

async def get_active_markets(
    self,
    min_volume: float = 0,
    exclude_mve: bool = True  # New parameter
) -> list[KalshiMarket]:
    """
    Fetch all active Kalshi markets with optional MVE filtering.

    Args:
        min_volume: Minimum 24h volume in USD (note: currently always 0 due to API bug)
        exclude_mve: If True, filter out MVE parlay markets (default: True)

    Returns:
        List of KalshiMarket objects
    """
    markets = []
    cursor = None

    while True:
        params = {
            "limit": 100,
            "status": "open",
            "with_nested_markets": "true"
        }
        if cursor:
            params["cursor"] = cursor

        response = await self._request("GET", "/trade-api/v2/markets", params=params)

        for market_data in response.get("markets", []):
            # Filter MVE markets if requested
            if exclude_mve:
                # MVE markets have mve_collection_ticker set
                if market_data.get("mve_collection_ticker"):
                    continue
                # Also check mve_selected_legs as backup
                if market_data.get("mve_selected_legs"):
                    continue

            # Apply volume filter (when API bug is fixed)
            volume_24h = market_data.get("volume_24h", 0)
            if volume_24h < min_volume * 100:  # Convert to cents
                continue

            markets.append(KalshiMarket(**market_data))

        # Check pagination
        cursor = response.get("cursor")
        if not cursor:
            break

    return markets
```

**Results**:
- **Before filtering**: 251,979 markets → $5.02/scan, 2,520 API requests
- **After filtering**: 20,542 markets → $0.41/scan, 206 API requests
- **Cost reduction**: 92% savings ($150.60/mo → $12.30/mo)
- **Still over budget**: $12.30/mo vs $3.34/mo target, but much better

### Option 2: Wait for Official API Support

Kalshi is developing official API support to exclude NFL markets:

User **NotPikachu (Kalshi)**:
> "Yeah its currently in development"

**ETA**: Unknown
**Risk**: May be weeks/months away

### Option 3: Hybrid Approach (Recommended)

```python
async def get_non_mve_markets(self) -> list[KalshiMarket]:
    """
    Fetch only non-MVE markets using client-side filtering.

    Once Kalshi releases official API support, this can be updated
    to use server-side filtering via query parameter.
    """
    all_markets = await self.get_active_markets(exclude_mve=False)

    # Filter client-side for now
    non_mve = [
        m for m in all_markets
        if not m.mve_collection_ticker and not m.mve_selected_legs
    ]

    logger.info(f"Filtered {len(all_markets)} → {len(non_mve)} markets (excluded MVE)")
    return non_mve
```

**When Kalshi API is ready**, update to:
```python
async def get_non_mve_markets(self) -> list[KalshiMarket]:
    """
    Fetch only non-MVE markets using server-side filtering.
    """
    params = {
        "limit": 100,
        "status": "open",
        "exclude_mve": "true"  # ← New Kalshi API parameter (future)
    }
    # ... pagination logic ...
```

## Additional Considerations

### 1. MVE Markets May Still Be Valuable

Some MVE parlays could have arbitrage opportunities:
- Users might misprice complex combinations
- Could arbitrage against individual legs on other platforms
- Higher variance → potentially higher edge

**Don't automatically exclude ALL MVE markets** - consider:
```python
# Option: Include MVE markets with high volume/liquidity
exclude_low_volume_mve = True  # Exclude most MVE
include_high_volume_mve = True  # But keep high-volume ones

if market.mve_collection_ticker:
    if exclude_low_volume_mve:
        # Only include if volume is substantial
        if market.volume_24h < 10000:  # $100 threshold
            continue
```

### 2. Different MVE Categories

Not all MVE markets are NFL:
- NBA player props
- Political outcomes (multiple events)
- Financial indicators (multi-leg)

**Filtering strategy** should be granular:
```python
# Filter specific MVE collections
EXCLUDED_MVE_COLLECTIONS = {
    "NFLW9",   # NFL Week 9
    "NFLW10",  # NFL Week 10
    # ... add more as needed
}

if market.mve_collection_ticker in EXCLUDED_MVE_COLLECTIONS:
    continue
```

### 3. Cost-Benefit Analysis

**Question**: Are MVE markets worth the cost?

| Scenario | Markets | Cost/Scan | Monthly Cost | Arbitrage Yield |
|----------|---------|-----------|--------------|-----------------|
| All markets | 251,979 | $5.02 | $150.60 | Unknown |
| Non-MVE only | 20,542 | $0.41 | $12.30 | Lower volume |
| High-volume MVE | ~5,000 | $0.50 | $15.00 | Potentially higher |

**Recommendation**: Start with non-MVE markets, add high-volume MVE if early results justify cost.

## Timeline

- **2025-10-26**: Scale discovered via Discord (Arbgame data)
- **2025-10-28**: Documented in gotchas
- **Future**: Kalshi API will support server-side MVE filtering (ETA unknown)

## How to Get Resolution Rules for MVE Markets

**Problem**: MVE markets have empty `rules_primary` and `rules_secondary` fields because rules are implicit in the parlay structure.

**Solution - Validated Implementation** (2025-10-28):

Fetch individual leg markets to get their resolution criteria:

```python
# Step 1: Identify MVE market
if market.get("mve_selected_legs") and not market.get("rules_primary"):
    leg_tickers = [leg["market_ticker"] for leg in market["mve_selected_legs"]]

# Step 2: Fetch each leg's rules individually
for ticker in leg_tickers:
    headers = client._sign_request("GET", f"/markets/{ticker}")
    response = await client.client.get(f"/markets/{ticker}", headers=headers)
    leg_data = response.json()["market"]

    # leg_data["rules_primary"] and leg_data["rules_secondary"] contain the rules
```

**Performance**:
- ✅ 100% of leg markets have complete rules (tested on real API)
- ✅ ~130ms per leg (5-13 legs typical, ~650ms-1.7s total per MVE market)
- ✅ No batch endpoint needed - sequential fetches work fine

**Example**:
```
MVE Market: KXMVENFLMULTIGAMEEXTENDED-S2025713422598AF-48E9C2B5B6B
  Rules: (empty)
  Legs: 5

Leg 1: KXNFLGAME-25NOV02CHICIN-CIN
  Rules: "If Cincinnati wins the Chicago at Cincinnati professional football game..."

Leg 2: KXNFLGAME-25NOV02DENHOU-DEN
  Rules: "If Denver wins the Denver at Houston professional football game..."

(etc. for remaining legs)
```

See `docs/KALSHI_MARKET_DETAILS_API.md` § 6 for complete implementation example.

---

## Related Issues

- **01_volume_always_zero.md** - Can't filter by volume currently
- **02_missing_markets_in_api.md** - Some markets not discoverable via API
- **05_market_orders_deprecated.md** - All orders require price parameter (limit orders only)

## External Resources

- Discord conversation: Kalshi API Users (2025-10-26)
- Users: Arbgame, lactobacillus, Ilya9040, NotPikachu (Kalshi)
- MVP fields: `mve_collection_ticker`, `mve_selected_legs`

## Questions for Kalshi Support

1. When will server-side MVE filtering be available?
2. Can we get a webhook/RSS feed for non-MVE market launches only?
3. Is there a way to fetch only traditional binary markets without pagination?
4. What's the retention policy for settled MVE markets (affects historical analysis)?
5. Are there MVE categories besides NFL that have similar scale?
