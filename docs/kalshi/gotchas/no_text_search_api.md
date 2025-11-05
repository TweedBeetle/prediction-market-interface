# No Text Search API

**Discovered**: 2025-11-03
**Status**: Confirmed - API Limitation
**Severity**: High

## Description

Kalshi's API does not provide any text search capability. The `/markets` and `/events` endpoints only support exact filtering by specific fields (event_ticker, series_ticker, status, timestamps), but no fuzzy text matching on titles or descriptions.

## Evidence

**Markets endpoint** (`/markets`) query parameters:
- `event_ticker` - Exact event ticker match (e.g., "KXBTC-25FEB")
- `series_ticker` - Exact series ticker match
- `status` - Market status (open/closed/settled)
- `tickers` - Comma-separated list of exact market tickers
- `mve_filter` - MVE inclusion/exclusion
- ❌ No `query` or `search` parameter for text matching

**Events endpoint** (`/events`) query parameters:
- `series_ticker` - Exact series ticker match
- `status` - Event status
- `min_close_ts` - Timestamp filter
- ❌ No `query` or `search` parameter for text matching

**Searching for "election" fails** because `event_ticker="election"` looks for an event with that exact ticker, which doesn't exist.

## Impact

**For MCP tools:**
- ❌ `kalshi_search_markets("election")` doesn't work as users expect
- ❌ Natural language queries like "Bitcoin markets" fail
- ❌ Discovery workflows are broken

**Current workaround in our code** (client.py:195):
```python
if query:
    params["event_ticker"] = query  # Simple search for MVP
```
This only works if the user provides an exact event ticker.

## Workaround

To implement proper text search, you must:

### Option 1: Client-Side Filtering (Best for small result sets)
1. Fetch all markets (or large batch with pagination)
2. Filter locally based on title/subtitle containing search query
3. Return filtered results

```python
async def search_markets(self, query: Optional[str] = None, limit: int = 20, status: str = "open") -> list[Market]:
    """Search markets with client-side text filtering."""
    # Fetch large batch (or all markets via pagination)
    params = {"limit": 1000, "status": status}
    data = await self._request("GET", "markets", params=params)
    markets = [Market(**m) for m in data.get("markets", [])]

    # Client-side text filter
    if query:
        query_lower = query.lower()
        markets = [
            m for m in markets
            if query_lower in m.title.lower()
            or (m.subtitle and query_lower in m.subtitle.lower())
        ]

    return markets[:limit]
```

**Pros:**
- ✅ Works with natural language queries
- ✅ Can search across title, subtitle, rules, etc.

**Cons:**
- ❌ High API cost (fetches many markets)
- ❌ Slow for large datasets
- ❌ Hits rate limits faster

### Option 2: Series-Based Search (Best for specific categories)
1. Map common search terms to series tickers (e.g., "election" → "PRES2024", "Bitcoin" → "KXBTC")
2. Use `series_ticker` parameter for filtering
3. Fall back to client-side search if no series match

```python
SERIES_MAPPING = {
    "election": ["PRES2024", "SENATE", "HOUSE"],
    "bitcoin": ["KXBTC"],
    "crypto": ["KXBTC", "KXETH"],
    # ... more mappings
}

async def search_markets(self, query: Optional[str] = None, limit: int = 20, status: str = "open") -> list[Market]:
    """Search with series mapping fallback."""
    params = {"limit": limit, "status": status}

    if query:
        query_lower = query.lower()
        # Check series mapping
        for keyword, series_tickers in SERIES_MAPPING.items():
            if keyword in query_lower:
                # Fetch markets for matched series
                all_markets = []
                for series_ticker in series_tickers:
                    params["series_ticker"] = series_ticker
                    data = await self._request("GET", "markets", params=params)
                    all_markets.extend(data.get("markets", []))
                return [Market(**m) for m in all_markets][:limit]

        # Fall back to client-side filtering
        # ... (Option 1 logic)

    # No query - return all
    data = await self._request("GET", "markets", params=params)
    return [Market(**m) for m in data.get("markets", [])]
```

**Pros:**
- ✅ Fast for common queries
- ✅ Lower API cost for mapped terms
- ✅ Graceful fallback

**Cons:**
- ❌ Requires maintaining mapping dictionary
- ❌ May miss markets in unmapped series

### Option 3: Events with Nested Markets (Best for browsing)
Use `/events` endpoint with `with_nested_markets=true` to get events + all their markets in one call:

```python
async def search_markets(self, query: Optional[str] = None, limit: int = 20, status: str = "open") -> list[Market]:
    """Search via events endpoint with nested markets."""
    params = {"limit": 100, "status": status, "with_nested_markets": True}
    data = await self._request("GET", "events", params=params)

    # Flatten events into markets
    all_markets = []
    for event in data.get("events", []):
        all_markets.extend(event.get("markets", []))

    # Client-side filter
    if query:
        query_lower = query.lower()
        all_markets = [
            m for m in all_markets
            if query_lower in m.get("title", "").lower()
        ]

    return [Market(**m) for m in all_markets[:limit]]
```

**Pros:**
- ✅ Fewer API calls (events often have multiple markets)
- ✅ Can search event-level metadata

**Cons:**
- ❌ Still requires client-side filtering
- ❌ Returns many markets per event

## Recommended Fix

For the Kalshi MCP server:

1. **Update tool description** to set correct expectations:
```python
@mcp.tool
async def kalshi_search_markets(
    query: Annotated[
        str | None,
        Field(description="Filter by series ticker OR text to search in titles (client-side). Examples: 'PRES2024', 'election', 'Bitcoin'")
    ] = None,
    # ...
) -> list[Market]:
    """
    Search for prediction markets on Kalshi.

    **Note**: Kalshi API has no text search. This tool:
    - Uses `series_ticker` filter if query matches a known series
    - Falls back to fetching markets and filtering locally by title
    - May be slow for broad searches (fetches up to 1000 markets)

    For best results, use specific series tickers (e.g., "PRES2024" instead of "president").
    """
```

2. **Implement hybrid approach** (series mapping + client-side fallback)

3. **Document in gotchas** (this file)

4. **Add caching** to reduce API calls for repeated searches

## Related Issues

- This makes the `kalshi_search_markets` tool misleading in its current form
- Users expect "search" to work like Google, but it doesn't
- Consider renaming tool to `kalshi_get_markets` or `kalshi_find_markets` to reduce expectations

## References

- API Docs: `/markets` endpoint - docs/kalshi/api-reference/market/get-markets.md
- API Docs: `/events` endpoint - docs/kalshi/api-reference/events/get-events.md
- Code: src/kalshi/client.py:179-199 (search_markets implementation)
