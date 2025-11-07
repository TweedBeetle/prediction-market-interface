# Prediction Market Interface - Project Documentation

## ⚠️ CRITICAL: When MCP Server Restart is Required

**ANY code changes to the MCP server or its dependencies (server, client, models) require a Claude Code session restart to take effect when testing via MCP tools.**

### When Restart IS Required:

✅ **After ANY code changes when testing MCP tools** - Claude Code caches the MCP server process
- Changes to: `src/kalshi/kalshi_mcp_server.py`, `src/kalshi/client.py`, `src/kalshi/models.py`
- **How to restart:** User must completely restart Claude Code session (quit and reopen)
- Example: After fixing orderbook bug, user must restart before `@kalshi_demo get_orderbook` will work

✅ **All MCP tool testing via `@kalshi_demo` or `@kalshi_prod`**
- MCP server is launched once and cached by Claude Code
- Code changes don't reload until full session restart

### When Restart is NOT Required:

❌ **Running integration tests** - Tests import code directly, see changes immediately
❌ **Testing via `uv run pytest`** - Always uses latest code
❌ **General development work** - Edit/test cycle doesn't need restarts

### Development Workflow:

**Correct pattern:**
```
1. Make code changes (fix bug, add feature)
2. Run tests: `uv run pytest` - Changes visible immediately ✓
3. User restarts Claude Code session
4. Test MCP tools: `@kalshi_demo <command>` - Changes now visible ✓
```

**Common mistake:**
```
1. Make code changes
2. Try `@kalshi_demo <command>` - OLD CODE still running ✗
3. Wonder why changes don't work ✗
```

**DO NOT:**
- ❌ Tell user to restart for running integration tests (not needed)
- ❌ Attempt to use `claude mcp restart` (doesn't exist - must restart full session)
- ❌ Expect MCP tools to reflect code changes without restart

---

## Project Documentation

### Development Journal

The `journal/` directory contains timestamped chronological records of development progress:

- **journal/CLAUDE.md** — Explains journal organization and guidelines
- **journal/polymarket/** — Polymarket development milestones
  - `2025-11-05-phase1-completion.md` — Phase 1 implementation summary (12 tools)
  - `2025-11-05-phase2-scope.md` — Phase 2 planning and feature analysis
  - `2025-11-05-phase2-completion.md` — Phase 2 implementation summary (7 additional tools)

**Journal vs Docs:**
- **Journal** = Timestamped snapshots of progress, milestones, and decisions (never modified)
- **Docs** = Living reference documentation that gets updated over time

### Product Requirements

- docs/kalshi-mcp-prd.md — **Kalshi MCP Server PRD** - Complete product requirements, Phase 1 completion status, implementation statistics, and roadmap for future phases.
- docs/polymarket-mcp-prd.md — **Polymarket MCP Server PRD** - 4-phase development plan (12 → 36+ tools), authentication via EIP-712 signing, dual API architecture (Gamma + CLOB), LLM-friendly design patterns, and 15-17 week timeline estimate.

### Implementation Plans

- docs/polymarket-implementation-plan.md — **Polymarket Technical Implementation** - Complete project structure, Pydantic model definitions, dual-client architecture, EIP-712 signing utilities, and code examples for authentication and order execution workflows.

### Platform Comparison

- docs/PREDICTION-MARKETS-COMPARISON.md — **Kalshi vs Polymarket Comparison** - Feature-by-feature analysis, implementation status tracking, use case recommendations, cross-platform arbitrage opportunities, and configuration examples.

### Agent Documentation

Refer to the curated docs for detailed guidance:

- docs/kalshi/index.md and related subpages — Kalshi agent architecture, SDK usage, and API reference.
- docs/kalshi/gotchas/CLAUDE.md — **Known Kalshi API gotchas and workarounds** - Critical issues, undocumented behaviors, and cost traps (action/side semantics, MVE market explosion, market orders deprecated, negative liquidity in settled markets)
- docs/polymarket/index.md and related subpages — Polymarket agent overview, quickstarts, and developer guides.
- docs/gofastmcp/INDEX.md and related subpages— Complete FastMCP framework documentation mirror including servers, clients, deployment, integrations, and Python SDK reference.

## MCP Server Setup - FastMCP

### FastMCP + UV Dependency Resolution

**Issue**: When registering a FastMCP server with Claude Code, using `fastmcp run server.py` directly fails with "No module named" errors, even if dependencies are in `pyproject.toml`.

**Root Cause**: The `fastmcp run` command doesn't inherit the project's `uv` environment. It spawns a subprocess that can't find project dependencies, only globally-installed packages.

#### ✅ Solution: Wrapper Script

Instead of pointing Claude Code directly at the FastMCP server file, create a wrapper script that runs within the `uv` project environment:

**1. Create wrapper script** (`run_kalshi_mcp.py` in project root):
```python
#!/usr/bin/env python3
"""Wrapper script to run the Kalshi MCP server."""

if __name__ == "__main__":
    from src.kalshi.kalshi_mcp_server import mcp
    mcp.run()
```

**2. Register with Claude Code**:
```bash
# Install fastmcp as a uv tool (one-time)
uv tool install fastmcp

# Add to Claude Code (respects project dependencies via uv run)
claude mcp add kalshi_mcp_server -- uv run run_kalshi_mcp.py
```

**3. Verify**:
```bash
claude mcp list | grep kalshi_mcp_server  # Should show ✓ Connected
```

#### Why This Works

- ✅ `uv run wrapper.py` automatically loads project dependencies from `pyproject.toml`
- ✅ Wrapper imports and runs the FastMCP server within that dependency-rich environment
- ✅ No need to hardcode `--with loguru --with fastmcp` flags (dependencies are in config)
- ✅ Avoids subprocess isolation issues with `fastmcp run`

#### ❌ Anti-Pattern: Direct fastmcp run

```bash
# ❌ DON'T - Subprocess can't find project dependencies
claude mcp add kalshi_mcp_server -- uv run fastmcp run src/kalshi/kalshi_mcp_server.py

# ❌ DON'T - Even with explicit --with flags, dependency resolution is fragile
fastmcp install claude-code src/kalshi/kalshi_mcp_server.py --with loguru
```

#### Key Insight

The wrapper approach works because:
1. `uv run wrapper.py` = "run this Python file in the project environment"
2. Project environment includes all `pyproject.toml` dependencies
3. `wrapper.py` imports the actual MCP server (now dependencies are already loaded)
4. FastMCP's `mcp.run()` uses STDIO by default (what Claude Code expects)

**Reference**: Kalshi MCP server setup (Nov 2025)

### Project-Level MCP Configuration - Proper Pattern

**Pattern**: Store project-specific MCP servers in `.mcp.json` at project root with explicit working directories.

#### Setup Steps

**1. Create wrapper script** that loads `.env` BEFORE importing server:

```python
#!/usr/bin/env python3
"""Wrapper script must load env vars before importing server."""

from dotenv import load_dotenv

# Load .env FIRST - server validates credentials at import time
load_dotenv()

if __name__ == "__main__":
    from src.kalshi.kalshi_mcp_server import mcp
    mcp.run()
```

**2. Register with project scope:**

```bash
# Use --scope project flag to store in .mcp.json
claude mcp add kalshi_mcp_server --scope project -- bash -c "cd /full/path && uv run wrapper.py"
```

This creates `.mcp.json`:

```json
{
  "mcpServers": {
    "server_name": {
      "type": "stdio",
      "command": "bash",
      "args": ["-c", "cd /full/path && uv run wrapper.py"],
      "env": {}
    }
  }
}
```

**3. Enable project servers in `.claude/settings.json`:**

```json
{
  "enableAllProjectMcpServers": true
}
```

#### Key Patterns

| Pattern | Why |
|---------|-----|
| `.mcp.json` at project root | Claude Code auto-discovers it |
| Explicit working directory in bash command | MCP may run from different context |
| `load_dotenv()` BEFORE import | Server validates credentials at module load |
| `--scope project` flag | Keeps servers isolated from user config |
| `enableAllProjectMcpServers: true` | Allows project config to be recognized |

#### What NOT to Do

```bash
❌ Don't: .claude/claude.json (wrong location)
❌ Don't: load_dotenv() AFTER import (env vars unavailable)
❌ Don't: Relative paths in bash command (fails from different contexts)
❌ Don't: Add to user level if project-specific (pollutes global config)
```

## Credentials & Secrets Management

### Overview

The project uses a dual-environment credential system for Kalshi trading:
- **Production** environment (real money) - `.env.kalshi.prod`
- **Demo** environment (test money) - `.env.kalshi.demo`

Both `.env` files and the `secrets/` directory are gitignored for security.

### File Structure

```
.
├── .env.kalshi.prod           # Production API credentials (gitignored)
├── .env.kalshi.demo           # Demo API credentials (gitignored)
├── secrets/                   # Private keys directory (gitignored)
│   ├── kalshi_prod_private_key.txt
│   └── kalshi_demo_private_key.txt
├── .gitignore                 # Excludes .env* and secrets/
└── run_kalshi_mcp_*.py        # Wrapper scripts (load appropriate .env)
```

### Environment File Format

**Option 1: File-based private key (recommended for local development)**

**Production (.env.kalshi.prod):**
```bash
# Kalshi Production API Credentials
KALSHI_API_KEY=your_prod_api_key_here
KALSHI_PRIVATE_KEY_PATH=/path/to/secrets/kalshi_prod_private_key.pem
KALSHI_ENVIRONMENT=production

# API Configuration
KALSHI_BASE_URL=https://trading-api.kalshi.com
KALSHI_API_VERSION=v2

# Safety Limits (Production)
KALSHI_MAX_ORDER_SIZE=100
KALSHI_DAILY_ORDER_LIMIT=50
KALSHI_LARGE_ORDER_THRESHOLD=50
KALSHI_MAX_BALANCE_USAGE_PCT=25
```

**Option 2: Direct private key content (recommended for CI/CD)**

**Demo (.env.kalshi.demo):**
```bash
# Kalshi Demo API Credentials
KALSHI_API_KEY=your_demo_api_key_here
KALSHI_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG...key_content_here...\n-----END PRIVATE KEY-----"
KALSHI_ENVIRONMENT=demo

# API Configuration
KALSHI_BASE_URL=https://demo-api.kalshi.co
KALSHI_API_VERSION=v2

# Safety Limits (Demo - more permissive)
KALSHI_MAX_ORDER_SIZE=1000
KALSHI_DAILY_ORDER_LIMIT=500
KALSHI_LARGE_ORDER_THRESHOLD=500
KALSHI_MAX_BALANCE_USAGE_PCT=100
```

### Private Keys

**Two Approaches:**

1. **File-based (Recommended for local development):**
   - Private keys stored in `secrets/` directory
   - Referenced by path in `.env` files using `KALSHI_PRIVATE_KEY_PATH`
   - Example: `KALSHI_PRIVATE_KEY_PATH=/path/to/secrets/kalshi_demo_private_key.pem`

2. **Direct content (Recommended for CI/CD):**
   - Private key content provided directly via `KALSHI_PRIVATE_KEY` env var
   - Useful for secrets managers, cloud deployments
   - Example: `KALSHI_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\n...key content...\n-----END PRIVATE KEY-----"`

**Priority:** If both are set, `KALSHI_PRIVATE_KEY` (direct content) takes precedence.

**Obtaining Private Keys:**
1. Log into Kalshi (production or demo environment)
2. Navigate to API settings
3. Generate API key pair
4. For file-based approach:
   - Save private key to `secrets/kalshi_{env}_private_key.pem`
   - Add path to `.env.kalshi.{env}` as `KALSHI_PRIVATE_KEY_PATH`
5. For direct content approach:
   - Copy PEM-encoded private key
   - Add to `.env.kalshi.{env}` as `KALSHI_PRIVATE_KEY="...key content..."`
6. Add public key to `.env.kalshi.{env}` as `KALSHI_API_KEY`

### Wrapper Scripts Load Environment

Each MCP server wrapper loads its specific environment:

**run_kalshi_mcp_prod.py:**
```python
#!/usr/bin/env python3
"""Wrapper for Kalshi MCP server (PRODUCTION)."""
from dotenv import load_dotenv

# Load production environment BEFORE importing server
load_dotenv(".env.kalshi.prod")

if __name__ == "__main__":
    from src.kalshi.kalshi_mcp_server import mcp
    mcp.run()
```

**run_kalshi_mcp_demo.py:**
```python
#!/usr/bin/env python3
"""Wrapper for Kalshi MCP server (DEMO - Safe for testing)."""
from dotenv import load_dotenv

# Load demo environment BEFORE importing server
load_dotenv(".env.kalshi.demo")

if __name__ == "__main__":
    from src.kalshi.kalshi_mcp_server import mcp
    mcp.run()
```

### Security Notes

✅ **What IS gitignored:**
- `.env.kalshi.prod`
- `.env.kalshi.demo`
- `secrets/` directory and all contents
- `.env` (legacy/default)

✅ **What is NOT gitignored (safe to commit):**
- `.env.example` - Template showing required variables
- Wrapper scripts (`run_kalshi_mcp_*.py`)
- Documentation about credential setup

### Setup Checklist

When setting up on a new machine:

1. **Create secrets directory:**
   ```bash
   mkdir -p secrets
   chmod 700 secrets  # Owner only
   ```

2. **Obtain Kalshi credentials:**
   - Sign up at https://kalshi.com (production)
   - Sign up at https://demo.kalshi.co (demo)
   - Generate API keys for both

3. **Create production private key file:**
   ```bash
   echo "your_prod_private_key_here" > secrets/kalshi_prod_private_key.txt
   chmod 600 secrets/kalshi_prod_private_key.txt
   ```

4. **Create demo private key file:**
   ```bash
   echo "your_demo_private_key_here" > secrets/kalshi_demo_private_key.txt
   chmod 600 secrets/kalshi_demo_private_key.txt
   ```

5. **Create .env.kalshi.prod:**
   ```bash
   cp .env.example .env.kalshi.prod
   # Edit and fill in production values
   ```

6. **Create .env.kalshi.demo:**
   ```bash
   cp .env.example .env.kalshi.demo
   # Edit and fill in demo values
   ```

7. **Verify setup:**
   ```bash
   # Check files exist and are secure
   ls -la .env.kalshi.*
   ls -la secrets/

   # Ensure proper permissions
   chmod 600 .env.kalshi.*
   chmod 600 secrets/*
   ```

### Testing with Credentials

**Integration tests** use demo credentials automatically:

```bash
# Tests load .env.kalshi.demo via conftest.py
uv run pytest tests/kalshi/integration/
```

**Manual testing** via MCP servers:

```bash
# Test with demo server (safe, fake money)
# In Claude Code:
User: "@kalshi_demo search for bitcoin markets"

# Use production server (real money - be careful!)
User: "@kalshi_prod check my balance"
```

### Testing Patterns

**FastMCP Client in pytest** - Don't use fixtures, creates event loop context mismatch:

```python
# ❌ DON'T - Async fixture hangs
@pytest.fixture
async def mcp_client():
    async with Client(mcp) as client:
        yield client  # Test hangs when using client

# ✅ DO - Create client directly in test
@pytest.mark.asyncio
async def test_my_tool(demo_env):
    from src.kalshi.kalshi_mcp_server import mcp
    async with Client(mcp) as client:
        result = await client.call_tool("my_tool", {})
```

### Troubleshooting

**Error: "Invalid API credentials"**
- Check API key is correct in `.env` file
- Verify private key file exists at path specified
- Ensure no trailing whitespace in credentials
- Confirm you're using matching env (demo key → demo API, prod key → prod API)

**Error: "Permission denied" reading private key**
- Check file permissions: `chmod 600 secrets/*`
- Verify file path in `.env` is correct (relative or absolute)

**Error: "Module not found" when running wrapper**
- Ensure you're using `uv run wrapper.py` (loads project dependencies)
- Don't use `python wrapper.py` directly

**⚠️ CRITICAL: Environment Variable Override Required**

When multiple `.env` files exist, `load_dotenv()` **does NOT override by default**:

```python
# ❌ WRONG - Won't override existing vars from .env
load_dotenv(".env.kalshi.demo")

# ✅ CORRECT - Forces demo values to replace .env values
load_dotenv(".env.kalshi.demo", override=True)
```

**Why this matters:**
- If `.env` loads first (production credentials)
- Then `.env.kalshi.demo` loads without `override=True`
- Result: Mixed credentials (demo API key + prod private key) → 401 errors

**Always use `override=True` in environment-specific wrapper scripts** to ensure the intended credentials win.

---

## Testing Anti-Patterns & Gotchas

### VCR Cassettes Can Hide Bugs

**Problem:** VCR cassettes replay successful HTTP interactions, masking bugs that only appear with real API calls.

**Example bugs missed by cassettes:**

1. **Auth signature bugs** - Cassettes replay old successful auth, even if signature algorithm is completely wrong
2. **Parsing bugs with null data** - If cassettes have `null` orderbooks, bad parsing code never executes
3. **Env loading issues** - Tests explicitly load `.env.kalshi.demo` in `conftest.py`, bypassing wrapper script bugs

**Prevention checklist:**

- [x] Audit VCR cassettes for realistic data (not just nulls/empty responses)
- [x] Periodically re-record cassettes to catch API changes
- [x] Add tests with real API responses, not just null data
- [x] Test MCP tools via `@kalshi_demo` in addition to running `uv run pytest`
- [x] When auth works in tests but fails in MCP, check env loading in wrapper scripts
- [x] **Add E2E tests that bypass VCR** (see E2E Testing Strategy below)

**Pattern from this project:**

```
✅ Tests passed (using VCR cassettes)
❌ MCP tools failed (real API calls)

Root causes found:
1. Auth signature included body (wrong per docs, but cassettes masked it)
2. Orderbook parser expected nested structure (cassettes had null, didn't trigger)
3. Env vars mixed prod/demo (tests bypass wrapper script, didn't catch)
4. Fill model expected int prices, API returns floats (cassettes had empty arrays)
```

**Case Study: Fill Model Bug (2025-11-03)**

During system demonstration, `kalshi_get_fills` crashed with:
```
ValidationError: Input should be a valid integer, got a number with a fractional part
price: 0.01  ← API returns float in dollars
```

**Why tests didn't catch it:**
```yaml
# tests/cassettes/TestPortfolioTools.test_get_fills.yaml
response:
  body:
    string: '{"cursor":"","fills":[]}'  # ← Empty array!
```

- Integration tests ran against demo API with no trading activity
- VCR recorded empty fill arrays `[]`
- Empty arrays bypass model validation (no Fill objects created)
- Bug in Fill model never triggered
- **Tests passed ✅ but code was broken ❌**

**The fix:**
1. Changed Fill model `price` field from `int` to `float`
2. Added unit tests that validate model structure with mock data
3. Unit tests catch model bugs even when cassettes are empty

**Prevention:**
- ✅ Add unit tests for model parsing (don't rely only on integration tests)
- ✅ Use realistic mock data in unit tests (simulate actual API responses)
- ✅ Cassette validation tests check for empty/null data patterns
- ✅ Periodically test MCP tools directly (bypasses cassettes)

**Code references:**
- Bug fix: `src/kalshi/models.py:158` (Fill.price changed to float)
- Unit tests: `tests/kalshi/unit/test_fill_model.py` (6 tests for Fill model)
- Cassette validation: `tests/kalshi/integration/test_cassette_validation.py`

**Lesson:** **Passing tests ≠ working code** when cassettes have unrealistic data. Always test MCP tools directly after code changes, and add unit tests for model parsing.

---

**Case Study: Phase 2 Order Groups (2025-11-03)**

During Phase 2 demonstration, order groups immediately failed with `KeyError: 'order_group'` when testing via MCP tools, despite 22 integration tests passing.

**Why tests didn't catch it:**

1. **Tests were written based on wrong documentation**:
   - Python SDK docs suggested: `{"order_group": {...}}`
   - Tests validated that expected structure
   - VCR cassettes recorded fictional responses matching wrong code
   - **Actual API** returns: `{"order_group_id": "..."}`

2. **Cassettes replayed fictional success**:
   ```python
   # tests/kalshi/integration/test_order_groups.py (BEFORE fix)
   group = await client.create_order_group(contracts_limit=100)
   assert group.contracts_limit == 100  # ✅ Test passed (cassette had this)
   assert group.contracts_filled == 0   # ✅ Test passed (cassette had this)

   # But real API NEVER returns these fields!
   ```

3. **Integration tests weren't actually integrating**:
   - Tests verified code behaved consistently with cassettes (regression tests)
   - Tests did NOT verify code worked with real API
   - First real API test was via MCP tools → immediate failure

**The discovery process:**
1. User asked to test MCP tools directly (bypasses cassettes)
2. Immediate failure: `KeyError: 'order_group'`
3. User said "look athe api docs mauybe again" (critical feedback!)
4. Found actual API reference docs (not SDK docs)
5. Discovered real API structure completely different

**The fix:**
1. Rewrote `OrderGroup` model to match actual API responses
2. Fixed all 5 client methods (create, get, list, reset, delete)
3. Updated integration tests to expect correct structure
4. Documented API limitation (contracts_limit never returned)

**Root cause:** Tests validated consistency with cassettes, not correctness against real API.

**Prevention:**
- ✅ Test MCP tools directly after code changes (bypasses cassettes)
- ✅ Periodically re-record cassettes to catch API drift
- ✅ Add cassette validation tests (check for realistic data)
- ✅ Unit tests with mock data (don't rely only on cassettes)
- ✅ When docs conflict, verify against actual API

**Key insight:** **First test against real API wins**. MCP tools found bugs in minutes that 22 passing tests missed entirely.

**Code references:**
- Investigation: Commit `62ab18a` - "Fix Phase 2 bugs: Order Groups response parsing and Amend Order endpoint"
- Model fix: `src/kalshi/models.py:284-310` (OrderGroup rewrite)
- Client fixes: `src/kalshi/client.py:740-817` (all order group methods)
- Test updates: `tests/kalshi/integration/test_order_groups.py`

---

### E2E Testing Strategy (Bypassing VCR)

**Problem Solved**: VCR-based integration tests can pass while code is broken against real API.

**Solution**: E2E tests that explicitly bypass VCR cassettes and always hit real demo API.

**Pattern**:
```python
# tests/kalshi/integration/test_e2e_*.py

# Disable VCR for all E2E tests
pytestmark = [pytest.mark.asyncio, pytest.mark.disable_recording]

class TestOrderGroupsE2E:
    async def test_order_group_create_and_retrieve(self, demo_env):
        """
        Test against REAL API - no cassettes.
        This would have caught the KeyError: 'order_group' immediately.
        """
        # ... test implementation ...
```

**When to Add E2E Tests**:

1. **New Phase 2 features** - Order groups, advanced parameters, batch operations
2. **Critical workflows** - Complete order lifecycle (create → verify → cancel)
3. **Cross-feature integration** - OCO strategies combining groups + advanced params
4. **After finding cassette-masked bugs** - Convert to E2E test

**Test Files**:
- `test_e2e_order_lifecycle.py` - Basic order operations (Phase 1)
- `test_e2e_phase2_workflows.py` - Order groups, advanced params, OCO strategies (Phase 2)

**Coverage**:

| Feature | Integration Tests (VCR) | E2E Tests (Real API) |
|---------|------------------------|----------------------|
| Phase 1: Basic orders | ✅ 53 tests | ✅ 5 tests |
| Phase 2: Order groups | ✅ 8 tests | ✅ 4 tests |
| Phase 2: Advanced params | ✅ 9 tests | ✅ 3 tests |
| Phase 2: Integration | ✅ 5 tests | ✅ 1 test |

**Key Differences**:

**Integration Tests (VCR)**:
- ✅ Fast (replay cached responses)
- ✅ Deterministic (same every time)
- ✅ Test consistency (regression)
- ❌ Can pass with wrong code (fictional cassettes)
- ❌ Don't catch API changes

**E2E Tests (Real API)**:
- ✅ Test correctness (actual API behavior)
- ✅ Catch API changes immediately
- ✅ Would have caught order groups bug
- ⚠️ Slower (~15s vs 2s)
- ⚠️ May fail due to demo API reliability

**Best Practice**: **Both are needed!**
- Integration tests for fast feedback and regression protection
- E2E tests for correctness verification and API change detection

**Running E2E Tests**:
```bash
# Run all E2E tests (bypasses VCR)
uv run pytest tests/kalshi/integration/test_e2e_*.py -v

# Run Phase 2 E2E tests only
uv run pytest tests/kalshi/integration/test_e2e_phase2_workflows.py -v
```

**E2E Test Resilience**:

E2E tests are designed to handle demo API flakiness:
- Eventual consistency (groups may not appear in list immediately)
- 404 errors on recently created resources
- 503 service unavailable errors

Tests log warnings but continue when encountering known demo API issues.

---

### Search Markets Implementation - Client-Side Filtering

**Implementation Detail:** The `kalshi_search_markets` tool uses **client-side text filtering** because Kalshi's API has no text search endpoint.

**How it works:**
1. When query is provided: Fetches up to 1000 markets, filters locally by title/subtitle
2. When no query: Returns requested limit directly from API

**Why:**
- ❌ Kalshi API only supports exact filtering (event_ticker, series_ticker, status)
- ❌ No fuzzy text search or keyword matching
- ✅ Client-side filtering allows natural language queries like "election", "Bitcoin", "Trump"

**Performance:**
- First call with query: ~1-2 seconds (fetches 1000 markets)
- Subsequent calls: Fast (if markets cached by API/network layer)
- No query: Fast (direct API call with requested limit)

**Code locations:**
- Client implementation: `src/kalshi/client.py:179-215` (search_markets method)
- MCP tool: `src/kalshi/kalshi_mcp_server.py:104-160` (kalshi_search_markets)
- Documentation: `docs/kalshi/gotchas/no_text_search_api.md`

**Testing note:** After modifying this implementation, VCR cassettes need re-recording:
```bash
# Re-record affected cassettes
./scripts/rerecord_cassettes.sh test_client.py test_mcp_tools.py
```

---

### Pagination Implementation

**Overview:** The Kalshi API uses cursor-based pagination for list endpoints. The client handles this transparently.

**Implementation Pattern:**
```python
# Internal helper method (_paginate)
async def _paginate(
    endpoint: str,
    result_key: str,
    params: dict,
    max_results: Optional[int] = None
) -> list[dict]:
    """Fetches all pages using cursor-based pagination."""
    # 1. Initial request with limit=100 (max per page)
    # 2. Extract cursor from response
    # 3. Loop with cursor until no more pages
    # 4. Stop early if max_results reached
```

**Which methods use pagination:**
- ✅ `search_markets()` - Custom incremental pagination for query filtering
- ✅ `get_events()` - Uses `_paginate` helper
- ✅ `get_trades()` - Uses `_paginate` helper
- ✅ `get_orders()` - Uses `_paginate` helper
- ✅ `get_positions()` - Uses `_paginate` helper
- ✅ `get_fills()` - Uses `_paginate` helper

**Key characteristics:**
- **Transparent**: Callers request N results, client fetches pages as needed
- **Efficient**: Stops fetching when limit reached (doesn't over-fetch)
- **Simple API**: Returns `list[Model]` directly, no cursor exposure
- **Max page size**: 100 items per page (Kalshi's limit)

**Example:**
```python
# User requests 250 fills
fills = await client.get_fills(limit=250)

# Internally:
# - Fetches page 1 (100 fills) with cursor=None
# - Fetches page 2 (100 fills) with cursor from page 1
# - Fetches page 3 (50 fills) with cursor from page 2
# - Returns combined list of 250 fills
```

**Code locations:**
- Pagination helper: `src/kalshi/client.py:169-213` (`_paginate` method)
- Search markets: `src/kalshi/client.py:225-295` (custom incremental pagination)
- Other methods: `src/kalshi/client.py:310+` (use `_paginate` helper)

**Documentation reference:** `docs/kalshi/getting_started/pagination.md`

**Future Enhancement Idea:**
> **Problem:** Search with queries can be slow, potentially fetching 100+ pages from Kalshi (10,000+ markets) for client-side filtering.
>
> **Solution:** Continuous market sync with vector database:
> - Background process periodically fetches all markets (every 5-15 minutes)
> - Stores market metadata (title, subtitle, ticker, etc.) in vector database
> - Embeds market text for semantic search
> - MCP tool `kalshi_search_markets_fast()` queries local vector DB instead of API
> - Benefits:
>   - **100x faster**: Local semantic search vs 100+ API calls
>   - **Semantic matching**: "presidential race" finds "election" markets
>   - **Always fresh**: Background sync keeps data current
>   - **Cost efficient**: One full fetch every 15min vs per-query fetching
> - Implementation: ChromaDB or similar, with embedding model (text-embedding-3-small)
> - Trade-off: Adds infrastructure complexity (background worker, database)
>
> **Related:** This pattern could extend to Polymarket too, enabling cross-platform semantic arbitrage detection.

---

### Demo API Reliability

**Known Issue:** Kalshi's demo API (`demo-api.kalshi.co`) experiences intermittent infrastructure errors.

**Symptoms:**
```
❌ 503 Service Unavailable - Order creation endpoint
✅ Success (retry works)
❌ 502 Bad Gateway - Order cancellation endpoint
✅ Success (retry works)
```

**Impact:**
- Order creation/cancellation endpoints may fail temporarily
- Tests pass because they use VCR cassettes (recorded successful responses)
- MCP tool testing may encounter errors that aren't in test results

**Root Cause:** Infrastructure flakiness in demo environment, NOT a code bug.

**Evidence:**
1. ✅ Authentication implementation verified correct against Kalshi docs
2. ✅ Same code succeeds on retry without changes
3. ✅ Health check shows API alternates between working/failing
4. ✅ Tests pass using cassettes even when API is down

**When testing MCP tools directly:**
- Expect occasional 502/503 errors during API instability
- Retry once if you encounter these errors
- Check API health first: `curl https://demo-api.kalshi.co/trade-api/v2/exchange/status`

**Tools to help:**
- **Health check fixture** - `tests/conftest.py` warns if API is down before running tests
- **E2E tests** - `tests/kalshi/integration/test_e2e_order_lifecycle.py` tests real order workflows
- **Cassette validation** - `tests/kalshi/integration/test_cassette_validation.py` verifies cassettes have realistic data
- **Re-record script** - `scripts/rerecord_cassettes.sh` updates cassettes with fresh API data

**Re-recording cassettes:**
```bash
# Re-record all cassettes (use when API is healthy)
./scripts/rerecord_cassettes.sh

# Only record new cassettes (preserve existing)
./scripts/rerecord_cassettes.sh --new-only

# Re-record specific test file
./scripts/rerecord_cassettes.sh test_mcp_tools.py
```

### When Tests Pass But MCP Fails

**Debugging checklist:**

1. **Check if using VCR cassettes**
   - Look for `@pytest.mark.vcr` or `tests/cassettes/` directory
   - Cassettes bypass real authentication and API calls

2. **Test outside MCP first**
   - Run `uv run python -c "...test code..."` with `load_dotenv()` explicitly
   - This bypasses both MCP caching AND test fixtures

3. **Check environment loading**
   - Print env vars in wrapper script to verify values
   - Ensure `override=True` in `load_dotenv()` calls
   - Look for multiple `.env` files that might conflict

4. **Verify credentials are paired correctly**
   - API key and private key must come from same generation
   - Check file paths are absolute (or relative to correct directory)
   - Confirm demo/prod environments aren't mixed

5. **Restart Claude Code after fixes**
   - MCP server is cached - code changes need full restart
   - Don't expect changes to take effect until restart

**Common pattern:** If direct client test works but MCP fails, the issue is in environment loading or MCP server initialization, not the core logic.

---

## Project Structure

### Data Models (`src/kalshi/models.py`)

**Core Models (10 total)**:

1. **ExchangeStatus** - Exchange operational status
2. **Balance** - Account balance with dollar conversions
3. **Market** - Market details with prices, volume, interpretation
4. **Event** - Event metadata (collection of related markets)
5. **Order** - Order details with fill status and prices
6. **Position** - Portfolio position with P&L calculations
7. **Fill** - Trade execution details with costs and fees
8. **OrderBook** - Order book depth with bids/asks for YES/NO sides
9. **OrderBookLevel** - Single price level in order book
10. **Trade** - Public trade details with volume calculations

**Key Model Patterns:**
- All models use Pydantic v2 for validation
- Helper properties for computed values (e.g., `balance_dollars`, `pnl_dollars`)
- Optional fields for API flexibility
- Type-safe datetime handling

### MCP Tools (16 total)

**Authentication (2 tools):**
- `kalshi_get_exchange_status` - Check exchange operational status
- `kalshi_get_balance` - Get account balance

**Market Discovery (6 tools):**
- `kalshi_search_markets` - Search markets by query/status
- `kalshi_get_market` - Get single market details
- `kalshi_get_events` - List events (collections of markets)
- `kalshi_get_event` - Get single event details
- `kalshi_get_orderbook` - Get order book depth (bids/asks)
- `kalshi_get_trades` - Get recent public trades

**Order Execution (5 tools):**
- `kalshi_create_market_order` - Create market order (immediate execution)
- `kalshi_create_limit_order` - Create limit order (price-controlled)
- `kalshi_cancel_order` - Cancel pending order
- `kalshi_amend_order` - Modify order without losing queue position
- `kalshi_decrease_order` - Reduce order size

**Portfolio Management (3 tools):**
- `kalshi_get_positions` - Get current positions with P&L
- `kalshi_get_fills` - Get trade execution history
- `kalshi_get_orders` - Get orders (active/filled/canceled)

### Client Methods (`src/kalshi/client.py`)

**KalshiClient** provides async methods for all API operations:
- Authentication with RSA-PSS signature
- Rate limiting and error handling
- Context manager support (`async with KalshiClient() as client`)
- Environment-based initialization (`from_env()`)

**Key Methods:**
- Exchange: `get_exchange_status()`, `get_balance()`
- Markets: `search_markets()`, `get_market()`, `get_orderbook()`, `get_trades()`
- Events: `get_events()`, `get_event()`
- Orders: `create_order()`, `cancel_order()`, `amend_order()`, `decrease_order()`, `get_orders()`
- Portfolio: `get_positions()`, `get_fills()`

### Testing Infrastructure

**VCR Cassettes (48 total)**:
- Automatic HTTP interaction recording/replay
- Configured in `tests/conftest.py` with automatic marking
- Filter sensitive headers (API keys, signatures)
- Tests run 2.5x faster (9s vs 23s without cassettes)

**Test Structure:**
```
tests/kalshi/integration/
├── test_client.py                    # Client method tests
├── test_mcp_tools.py                 # Protocol-level MCP tests
├── test_mcp_order_tools.py          # Order execution tests
├── test_mcp_portfolio_tools.py      # Portfolio management tests
├── test_mcp_discovery_tools.py      # Market discovery tests
└── test_tool_functions.py           # Direct tool function tests
```

**53 integration tests** covering:
- All 16 MCP tools
- Client methods
- Error handling
- Workflow scenarios
- Safety limits validation

### Common API Patterns

**Endpoint Path Corrections:**
- ✅ Trades: `/markets/trades` (NOT `/trades`)
- ✅ Market: `/markets/{ticker}`
- ✅ Events: `/events` and `/events/{event_ticker}`

**API Response Structures:**
- Most endpoints return data wrapped: `{"markets": [...]}`, `{"orders": [...]}`
- Trade endpoint returns prices as floats (dollars), not cents
- Order book returns nested structure with YES/NO bids/asks
- Pagination uses `cursor` parameter (implemented automatically by client)

**Pagination Support (Added 2025-11-03):**

Kalshi uses cursor-based pagination with a maximum of 100 items per page. All client methods that return lists now support automatic pagination:

**Paginated Methods:**
- `search_markets()` - Fetches all pages when query is provided, respects limit otherwise
- `get_events()` - Automatically paginates for limit >100
- `get_trades()` - Automatically paginates for limit >100
- `get_orders()` - Automatically paginates for limit >100
- `get_positions()` - Automatically paginates for limit >100
- `get_fills()` - Automatically paginates for limit >100

**Implementation Details:**
- Internal `_paginate()` helper handles cursor-based iteration
- Page size: 100 items (Kalshi's maximum)
- Query searches use incremental pagination (stop early once limit reached)
- Safety limit: Max 100 pages per request (10,000 items) to prevent runaway loops
- VCR cassettes updated to match new pagination parameters

**Example:**
```python
# Request 500 markets - automatically fetches 5 pages
markets = await client.search_markets(limit=500, status="open")

# Search with query - fetches pages until 50 matches found
matches = await client.search_markets(query="election", limit=50)
```

**Safety Patterns:**
- Always check balance before order creation
- Validate order size against MAX_ORDER_SIZE
- Log context updates for LLM visibility
- Handle empty result sets gracefully (positions, fills, orders)

---

## Known Issues & Gotchas

### Trade Model vs Fill Model

- **Trade** = Public trades endpoint (`/markets/trades`) - uses float prices in dollars
- **Fill** = Personal fills endpoint (`/portfolio/fills`) - uses int prices in cents
- These are different data structures despite similar concepts

### Order Book Data Format

API returns order book levels as nested arrays:
```python
{
  "yes": {"bids": [[price, quantity], ...], "asks": [...]},
  "no": {"bids": [...], "asks": [...]}
}
```

Client converts to structured `OrderBookLevel` objects for type safety.

### Empty Response Handling

Tools that return lists (positions, fills, orders) may return empty lists. MCP tools handle this gracefully with appropriate context messages ("No positions found").
```