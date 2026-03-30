# Polymarket MCP Server - Issue Analysis & Fix Recommendations

**Date**: 2025-11-07
**Analysis by**: Claude (Sonnet 4.5)
**Testing Status**: Comprehensive read-only testing completed

## Executive Summary

Three issues identified during comprehensive testing:

1. **CRITICAL**: Authentication completely broken - wrong EIP-712 signature format and missing L1 headers
2. **MODERATE**: Search query filtering non-functional - API ignores query parameter
3. **MINOR**: Response size limits need better handling for large result sets

## Issue #1: Authentication Failure (CRITICAL)

### Problem

Authentication fails with error: `Invalid L1 Request headers`

**Impact**: Complete blocker for all trading functionality:
- ❌ Cannot authenticate
- ❌ Cannot view positions
- ❌ Cannot view order history
- ❌ Cannot place/cancel orders
- ❌ Cannot view personal trade history

### Root Cause

The auth implementation has **multiple critical errors**:

#### 1. Wrong EIP-712 Domain Name
```python
# ❌ CURRENT (WRONG)
AUTH_DOMAIN = {
    "name": "Polymarket",  # WRONG!
    "version": "1",
    "chainId": 137,
}

# ✅ CORRECT (per Polymarket docs)
AUTH_DOMAIN = {
    "name": "ClobAuthDomain",  # Must be this exact string
    "version": "1",
    "chainId": 137,
}
```

#### 2. Wrong Message Structure
```python
# ❌ CURRENT (WRONG)
types = {
    "ClobAuth": [
        {"name": "account", "type": "address"},  # Wrong field name!
        {"name": "nonce", "type": "uint256"},    # Missing fields!
    ]
}

value = {
    "account": self.address,  # Wrong field name!
    "nonce": nonce,           # Missing timestamp and message!
}

# ✅ CORRECT (per Polymarket docs)
types = {
    "ClobAuth": [
        {"name": "address", "type": "address"},  # Correct field name
        {"name": "timestamp", "type": "string"}, # NEW: Required!
        {"name": "nonce", "type": "uint256"},
        {"name": "message", "type": "string"},   # NEW: Required!
    ]
}

value = {
    "address": self.address,
    "timestamp": str(timestamp),  # Must be string, not int!
    "nonce": nonce,
    "message": "This message attests that I control the given wallet",
}
```

#### 3. Missing L1 Headers
```python
# ❌ CURRENT: No L1 headers sent to /auth/api-key

# ✅ CORRECT: Must include L1 auth headers
headers = {
    "POLY_ADDRESS": wallet_address,
    "POLY_SIGNATURE": eip712_signature,
    "POLY_TIMESTAMP": str(timestamp),
    "POLY_NONCE": str(nonce),
}
```

### Fix Required

**File**: `src/polymarket/utils/auth_signer.py`

1. Change AUTH_DOMAIN name to "ClobAuthDomain"
2. Update EIP-712 message structure to include `address`, `timestamp`, `message`
3. Change `create_api_creds_message()` to accept timestamp parameter
4. Update `sign_api_creds_message()` to return (signature, timestamp, nonce) tuple

**File**: `src/polymarket/clob_client.py`

1. Update `authenticate()` to generate timestamp
2. Add L1 headers (POLY_ADDRESS, POLY_SIGNATURE, POLY_TIMESTAMP, POLY_NONCE) to auth request
3. Update to use new auth_signer interface

**Estimated Effort**: 2-3 hours
**Priority**: CRITICAL - Blocks all trading functionality
**Risk**: Medium - Requires careful EIP-712 implementation matching docs exactly

### Testing Plan

1. Unit test EIP-712 signature generation matches expected format
2. Integration test authentication flow against demo wallet
3. Verify obtained API credentials work for authenticated endpoints
4. Test full order lifecycle (create → cancel) after auth

### Reference

- Official docs: `docs/polymarket/developers/CLOB/authentication.md:103-126`
- TypeScript reference: https://github.com/Polymarket/clob-client/blob/main/src/signing/eip712.ts
- Python reference: https://github.com/Polymarket/py-clob-client/blob/main/py_clob_client/signing/eip712.py

---

## Issue #2: Search Query Filtering (MODERATE)

### Problem

Search query parameter is passed to API but completely ignored:

```python
# Query "Trump" returns same results as query "Bitcoin"
markets_trump = await client.search_markets(query="Trump", limit=5)
markets_bitcoin = await client.search_markets(query="Bitcoin", limit=5)
# Both return: ["Fed rate hike", "US recession", "Tether insolvency", ...]
```

### Root Cause

The Gamma API (`/markets` endpoint) **does not support text search**. The `query` parameter is accepted but ignored by the server.

**Evidence**:
```bash
# API ignores query parameter
curl "https://gamma-api.polymarket.com/markets?query=Bitcoin&limit=3"
# Returns: ["Biden COVID", "Airbnb IPO", "Supreme Court"] (no Bitcoin!)
```

### Fix Options

#### Option A: Client-Side Filtering (Like Kalshi)

**Pros**:
- Works immediately
- No API changes needed
- Can use fuzzy matching

**Cons**:
- Must fetch many pages to find matches
- Slower for queries with few matches
- Higher API usage

**Implementation**:
```python
async def search_markets(self, query: str = "", limit: int = 20):
    if not query:
        # No filtering - return directly from API
        return await self.get("/markets", params={"limit": limit})

    # Client-side filtering - fetch and filter locally
    matches = []
    offset = 0
    page_size = 100

    while len(matches) < limit:
        page = await self.get("/markets", params={
            "limit": page_size,
            "offset": offset,
        })

        # Filter by query (case-insensitive substring match)
        for market in page:
            if query.lower() in market.question.lower() or \
               query.lower() in market.description.lower():
                matches.append(market)
                if len(matches) >= limit:
                    break

        if len(page) < page_size:  # No more results
            break
        offset += page_size

    return matches[:limit]
```

#### Option B: Document Limitation

Simply document that text search is not supported and queries are ignored.

**Pros**:
- No code changes
- Fast implementation

**Cons**:
- Poor UX for users expecting search to work
- Less useful for discovery

#### Option C: Hybrid Approach

1. Document limitation clearly
2. Add client-side filtering as opt-in
3. Warn users about performance implications

### Recommendation

**Implement Option A (Client-Side Filtering)**

**Rationale**:
1. Provides expected UX (search actually works)
2. Consistent with Kalshi implementation pattern
3. Gamma API has pagination support (offset parameter works)
4. Can optimize with caching if needed

**Estimated Effort**: 2-3 hours
**Priority**: MODERATE - Impacts discoverability but workaround exists
**Risk**: Low - Same pattern already working in Kalshi client

### Testing Plan

1. Test query "election" finds relevant markets
2. Test query "Bitcoin" finds crypto-related markets
3. Test pagination works correctly (fetches multiple pages)
4. Test limit parameter stops at requested count
5. Verify performance with large datasets

---

## Issue #3: Response Size Limits (MINOR)

### Problem

Large result sets exceed MCP tool response token limit (25,000 tokens):

```
Error: MCP tool response (39,003 tokens) exceeds maximum allowed tokens (25000)
```

Triggered by: `polymarket_search_markets(limit=100)`

### Root Cause

FastMCP has built-in token limits for tool responses to prevent excessive context usage. Limit=100 markets returns ~39K tokens, which exceeds the 25K limit.

### Impact

**LOW** - Only affects users requesting large result sets:
- ✅ Normal queries (limit ≤ 20) work fine
- ⚠️  Large queries (limit > 50) may fail
- ✅ Error message is clear and actionable

### Fix Options

#### Option A: Reduce Default Limit

Change default from 20 to 10, document that large queries need pagination.

#### Option B: Add Response Truncation

Automatically truncate responses with warning when approaching limit.

#### Option C: Paginated Response Format

Return summary + pagination info instead of full market objects.

```python
# Instead of returning full markets, return summary
{
    "markets": [...],  # First N markets
    "total_count": 137,
    "returned_count": 20,
    "next_offset": 20,
    "note": "Use offset parameter for more results"
}
```

#### Option D: Document Limitation

Simply add warning in tool description about token limits.

### Recommendation

**Implement Option D (Documentation) + Small Code Change**

1. Update tool description to recommend limit ≤ 20
2. Add validation warning when limit > 20
3. Document pagination pattern in CLAUDE.md

**Rationale**:
- Least invasive solution
- Error message already clear
- Most users don't need 100 markets at once
- Pagination handles edge cases

**Code Change**:
```python
@mcp.tool
async def polymarket_search_markets(
    query: str = "",
    limit: int = Field(default=20, le=50),  # Cap at 50
    ...
) -> dict:
    """
    Search for prediction markets on Polymarket.

    Note: For performance, limit is capped at 50 markets per request.
    Use offset parameter for pagination if you need more results.
    """
    if limit > 20:
        logger.warning(f"Large limit ({limit}) may approach token limits")
    ...
```

**Estimated Effort**: 30 minutes
**Priority**: LOW - Workaround is simple (use smaller limits)
**Risk**: None

---

## Summary of Recommendations

| Issue | Priority | Effort | Recommendation |
|-------|----------|--------|----------------|
| **Authentication** | 🔴 CRITICAL | 2-3 hrs | Fix EIP-712 + L1 headers (required for trading) |
| **Search Filtering** | 🟡 MODERATE | 2-3 hrs | Implement client-side filtering (improves UX) |
| **Response Limits** | 🟢 LOW | 30 mins | Document + add validation (good practice) |

## Implementation Priority

**Phase 1** (Must Fix):
1. Fix authentication (Issue #1)
   - Blocks all trading functionality
   - Required for Phase 1 completion

**Phase 2** (Should Fix):
2. Implement client-side search (Issue #2)
   - Significantly improves user experience
   - Aligns with Kalshi implementation

**Phase 3** (Nice to Have):
3. Add response limit handling (Issue #3)
   - Edge case, already has workaround
   - Low priority polish

## Total Estimated Effort

- **Must Fix**: 2-3 hours (authentication)
- **Should Fix**: 4-6 hours (authentication + search)
- **Full Fix**: 5-7 hours (all issues)

## Testing Requirements

### Authentication Testing
- [ ] Unit tests for EIP-712 signing
- [ ] Integration test auth flow
- [ ] End-to-end order lifecycle test
- [ ] Verify against official Python/TS clients

### Search Testing
- [ ] Client-side filtering accuracy
- [ ] Pagination performance
- [ ] Edge cases (no matches, exact matches)
- [ ] Compare results with manual API calls

### Response Limit Testing
- [ ] Various limit values (1, 20, 50, 100)
- [ ] Token counting accuracy
- [ ] Error message clarity

## Risk Assessment

**Overall Risk**: Low-Medium

- **Authentication fix**: Medium risk (EIP-712 is finicky, must match spec exactly)
- **Search fix**: Low risk (same pattern as Kalshi, well-tested)
- **Response limit**: Very low risk (documentation + simple validation)

**Mitigation**:
1. Reference official TypeScript/Python implementations
2. Add comprehensive unit tests for crypto operations
3. Test against actual API with demo wallet
4. Keep VCR cassettes for regression testing

---

## Conclusion

The Polymarket MCP server is **production-ready for read-only market research**, but authentication must be fixed before trading functionality can be used.

**Recommended Action**: Implement fixes in priority order (authentication → search → limits)

**Alternative**: Ship now with authentication fix only, defer search improvements to Phase 3.
