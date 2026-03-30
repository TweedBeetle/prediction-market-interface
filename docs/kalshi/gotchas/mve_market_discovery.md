# MVE Market Discovery Fix (November 2025)

## Problem: Fed Rate Markets Not Found

**Symptoms:**
- Searching for "Fed" returned 0 results despite Fed markets existing
- Direct ticker lookup worked (`KXFEDDECISION-25DEC`, `KXRATECUTCOUNT-25DEC31`)
- Regular search checked 6,000+ markets across 60+ pages with ZERO matches

**Example:**
```python
# Regular search - Returns [] after checking 6000+ markets
markets = await client.search_markets("Fed", limit=20)
# 60+ API calls, 60+ seconds, 0 results ❌

# But these work fine:
market = await client.get_market("KXFEDDECISION-25DEC-T1")  # ✅
markets = await client.get_markets_by_series("KXRATECUTCOUNT")  # ✅
```

## Root Cause: MVE Markets Excluded

**MVE (Mutually Exclusive Event)** markets don't appear in the general `/trade-api/v2/markets?status=open` listing.

**What are MVE markets:**
- Markets where only one outcome can occur
- Examples:
  - "Exactly 2 Fed rate cuts in 2025" (T2)
  - "Exactly 3 Fed rate cuts in 2025" (T3)
  - "Trump wins" vs "Biden wins" vs "Other"
- Identifiable by `-T1`, `-T2`, `-T3` suffixes in ticker

**API Behavior:**
- `/markets?status=open` → Returns NON-MVE markets only
- `/markets?series_ticker=KXRATECUTCOUNT` → Returns MVE markets for that series
- `/markets?event_ticker=KXFEDDECISION-25DEC` → Returns MVE markets for that event

**Verification:**
```bash
# General listing - NO Fed markets in 10,000+ results
curl "https://demo-api.kalshi.co/trade-api/v2/markets?status=open&limit=100" | grep -i "fed"
# (empty)

# Series filter - IMMEDIATE results
curl "https://demo-api.kalshi.co/trade-api/v2/markets?series_ticker=KXRATECUTCOUNT&limit=3"
# {"markets": [
#   {"ticker": "KXRATECUTCOUNT-25DEC31-T2", ...},
#   {"ticker": "KXRATECUTCOUNT-25DEC31-T3", ...},
#   ...
# ]}
```

## Solution: Three-Tier Comprehensive Search

**New Implementation (November 2025):**

1. **Added 5 new client methods:**
   - `search_series(query)` - Search series titles
   - `search_events_by_text(query)` - Search event titles
   - `get_markets_by_series(series_ticker)` - Get all markets in series
   - `get_markets_by_event(event_ticker)` - Get all markets in event
   - `search_markets_comprehensive(query, include_mve=True)` - **Main fix**

2. **Added MCP tool:**
   - `kalshi_search_markets_comprehensive()` - Exposes comprehensive search via MCP

3. **Search strategy:**
   ```
   Comprehensive Search Flow:
   1. Search regular markets (fast)
   2. If include_mve=True AND not enough results:
      a. Search series titles → fetch markets from matching series
      b. Search event titles → fetch markets from matching events
   3. Deduplicate by ticker
   4. Return combined results
   ```

**Code locations:**
- Client methods: `src/kalshi/client.py:352-546`
- MCP tool: `src/kalshi/kalshi_mcp_server.py:452-533`

## Usage

### For MVE Markets (Fed, Elections, etc.)

```python
# ✅ Use comprehensive search
markets = await client.search_markets_comprehensive(
    query="Fed",
    limit=20,
    include_mve=True  # Default is True
)
# Finds: KXFEDDECISION, KXRATECUTCOUNT, etc.
```

### For Non-MVE Markets (Bitcoin, Weather, etc.)

```python
# ✅ Regular search is fine (and faster)
markets = await client.search_markets(
    query="Bitcoin",
    limit=20
)
# Finds: KXBTC markets immediately
```

### Via MCP Tools

```python
# In Claude Code:
@kalshi_demo search_markets_comprehensive("Fed")
# or
@kalshi_demo search_markets("Bitcoin")  # Regular search for non-MVE
```

## Performance

| Search Type | Markets Searched | API Calls | Time | MVE Markets Found |
|-------------|------------------|-----------|------|-------------------|
| Regular (`search_markets("Fed")`) | 6,000+ | 60+ | 60s | ❌ 0 |
| Comprehensive (`search_markets_comprehensive("Fed")`) | ~200 | 2-3 | 2-3s | ✅ Found |
| Direct series (`get_markets_by_series("KXRATECUTCOUNT")`) | ~10 | 1 | <1s | ✅ Found |

**Why comprehensive is fast:**
- Series/event APIs return much smaller result sets
- Stops early when limit is reached
- Text search happens locally (not across 10,000+ markets)

## When to Use Which

| Use Case | Tool | include_mve |
|----------|------|-------------|
| Search Fed/election/economic indicators | `search_markets_comprehensive()` | `True` (default) |
| Search Bitcoin/weather/sports | `search_markets()` | N/A |
| Unknown market type | `search_markets_comprehensive()` | `True` (safer) |
| Speed critical + know it's not MVE | `search_markets()` | N/A |
| Direct ticker lookup | `get_market(ticker)` | N/A |
| All markets in a series | `get_markets_by_series()` | N/A |

## Identifying MVE Markets

**By ticker pattern:**
- `-T1`, `-T2`, `-T3` suffix = MVE market
- Examples: `KXRATECUTCOUNT-25DEC31-T2`, `KXFEDDECISION-25DEC-T1`

**By topic:**
- Fed rate decisions
- Election outcomes (Senate, House, Presidential)
- Economic indicators (GDP ranges, inflation ranges)
- Count-based markets ("How many X will happen?")

**By series/event structure:**
- Series ticker: `KXRATECUTCOUNT`, `KXFEDDECISION`, `KXSEATSP`
- Multiple markets under same series/event, only one can win

## Arbitrage Impact

This fix enables discovering cross-platform arbitrage opportunities:

**Example found (November 2025):**
- "Exactly 2 Fed rate cuts in 2025"
- Kalshi: 37¢ (implies 37% probability)
- Polymarket: 26.5¢ (implies 26.5% probability)
- **Spread: 10.5¢ = 28% profit opportunity!**

Before this fix, you couldn't even find the Kalshi market to compare prices.

## Implementation Notes

**Why not fix the regular search:**
- Would make ALL searches slower (need to query 3 endpoints)
- Most searches work fine with current behavior
- Better to have two tools: fast (regular) and thorough (comprehensive)

**Design decision:**
- Keep `search_markets()` unchanged (fast, backward compatible)
- Add `search_markets_comprehensive()` (slower, finds everything)
- Let users choose based on use case

**Future Enhancement:**
Vector database approach could make this instant:
- Background sync of all markets every 5-15min
- Semantic search on local DB
- Benefits: 100x faster, semantic matching, always fresh
- Trade-off: Adds infrastructure complexity

## Testing

**Test scripts:**
- `test_fed_discovery_fast.py` - Demonstrates comprehensive search works
- Regular search would take 60+ seconds and find nothing
- Comprehensive search finds markets in 2-3 seconds

**To verify fix works:**
```bash
# Should find Fed markets quickly
uv run python3 -c "
import asyncio
from src.kalshi.client import KalshiClient
async def test():
    async with KalshiClient.from_env() as client:
        markets = await client.search_markets_comprehensive('Fed', limit=5)
        print(f'Found {len(markets)} markets')
        for m in markets[:3]:
            print(f'  - {m.ticker}: {m.title}')
asyncio.run(test())
"
```

## Documentation Updates

**Related files:**
- Client implementation: `src/kalshi/client.py`
- MCP server: `src/kalshi/kalshi_mcp_server.py`
- Arbitrage analysis: `/fed_rate_cuts_arbitrage_2025-11-08.md`
- This gotcha: `docs/kalshi/gotchas/mve_market_discovery.md`

**CLAUDE.md updates needed:**
- Add to "Known Issues & Gotchas" section
- Document the two search methods and when to use each
- Add examples to "Common Patterns" section

## References

- Kalshi API docs: https://docs.kalshi.com/
- Series endpoint: `/trade-api/v2/series`
- Events endpoint: `/trade-api/v2/events`
- Markets endpoint: `/trade-api/v2/markets`
- Issue discovered: November 8, 2025
- Fix implemented: November 8, 2025
