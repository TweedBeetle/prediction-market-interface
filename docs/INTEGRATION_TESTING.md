# Integration Testing Guide - Kalshi MCP Server

**Last Updated**: November 2025

## Overview

This guide explains how to run comprehensive integration tests for the Kalshi MCP server using the demo environment with mock funds.

**Key Features:**
- 47 integration tests organized by functionality
- Zero financial risk (uses mock funds)
- Tests all 53 MCP tools
- Covers critical trading workflows to advanced features
- Can be run on-demand without affecting production

## Quick Start

### 1. Set Up Demo Credentials

Create `.env` in project root:

```bash
KALSHI_DEMO_API_KEY_ID=your-demo-api-key-id
KALSHI_DEMO_PRIVATE_KEY_PATH=/absolute/path/to/demo_private_key.pem
```

See [Demo Environment Setup](../.claude/CLAUDE.md#demo-environment-setup) in CLAUDE.md for detailed instructions.

### 2. Run All Demo Tests

```bash
pytest tests/kalshi/test_integration_demo.py -m manual -v
```

Expected output:
```
tests/kalshi/test_integration_demo.py::TestDemoEnvironmentSetup::test_demo_client_initializes PASSED
tests/kalshi/test_integration_demo.py::TestDemoEnvironmentSetup::test_demo_mcp_server_loads PASSED
...
47 passed in X.XXs
```

### 3. Run Specific Test Class

```bash
pytest tests/kalshi/test_integration_demo.py::TestCriticalPathTrading -m manual -v
```

## Test Organization

### Phase 0: Environment Setup (4 tests)

**Class**: `TestDemoEnvironmentSetup`

Validates that the demo environment is properly configured:

| Test | Purpose | Validates |
|------|---------|-----------|
| `test_demo_client_initializes` | Client creation | Credentials loaded, API key formatted correctly |
| `test_demo_mcp_server_loads` | Server registration | All 53 tools registered and available |
| `test_demo_api_connectivity` | API reachability | Can reach demo API endpoint |
| `test_demo_account_has_mock_funds` | Account funding | Balance > 0 for trading |

**Example Run:**
```bash
pytest tests/kalshi/test_integration_demo.py::TestDemoEnvironmentSetup -m manual -v
```

### Phase 1: Critical Path Trading (10 tests)

**Class**: `TestCriticalPathTrading`

Tests essential order lifecycle workflows - the most critical trading operations:

| Test | Purpose | MCP Tools Used |
|------|---------|---|
| `test_search_open_markets` | Find tradeable markets | `kalshi_search_markets` |
| `test_get_market_details_with_orderbook` | View market + order book | `kalshi_get_market`, `kalshi_get_orderbook` |
| `test_create_limit_order_buy` | Place limit order (YES side) | `kalshi_create_order` |
| `test_create_limit_order_sell` | Place limit order (NO side) | `kalshi_create_order` |
| `test_create_market_order` | Immediate execution | `kalshi_create_order` |
| `test_check_order_status` | Monitor resting orders | `kalshi_get_orders` |
| `test_amend_order_price` | Modify limit price | `kalshi_amend_order` |
| `test_amend_order_quantity` | Modify contract count | `kalshi_amend_order` |
| `test_cancel_order` | Cancel resting order | `kalshi_cancel_order` |
| `test_get_account_balance` | Check available funds | `kalshi_get_balance` |
| `test_get_current_positions` | View open positions | `kalshi_get_positions` |
| `test_get_fill_history` | View executed trades | `kalshi_get_fills` |

**Workflow:**
1. Find an open market
2. Create limit buy order
3. Check order status (should be resting)
4. Amend order price (improve terms)
5. Amend order quantity (reduce size)
6. Cancel order
7. Check balance and positions

**Example Run:**
```bash
pytest tests/kalshi/test_integration_demo.py::TestCriticalPathTrading::test_create_limit_order_buy -m manual -v
```

### Phase 2: Portfolio Management (7 tests)

**Class**: `TestPhase1PortfolioManagement`

Tests portfolio management and risk control tools:

| Test | Purpose | MCP Tools Used |
|------|---------|---|
| `test_create_order_group` | Risk management | `kalshi_create_order_group` |
| `test_get_order_group_details` | View group state | `kalshi_get_order_groups` |
| `test_reset_order_group_counter` | Reset contract limit | `kalshi_reset_order_group` |
| `test_delete_order_group` | Clean up groups | `kalshi_delete_order_group` |
| `test_get_settlements` | Track P&L | `kalshi_get_settlements` |
| `test_decrease_order_quantity` | Partial exit | `kalshi_decrease_order` |
| `test_get_bulk_queue_positions` | Monitor priority queue | `kalshi_get_queue_positions` |

**Purpose**: Order groups automatically cancel resting orders when a contract limit is reached, preventing over-exposure.

**Example Run:**
```bash
pytest tests/kalshi/test_integration_demo.py::TestPhase1PortfolioManagement -m manual -v
```

### Phase 3: Market Intelligence (5 tests)

**Class**: `TestPhase2MarketIntelligence`

Tests market analysis and intelligence capabilities:

| Test | Purpose | Calculation |
|------|---------|---|
| `test_get_event_metadata` | Event details | Fetch event information |
| `test_analyze_market_probability` | Implied probability | YES_PRICE / (YES_PRICE + NO_PRICE) |
| `test_analyze_market_spread` | Bid-ask spread | ASK - BID for each side |
| `test_calculate_liquidity_score` | Liquidity rating (0-100) | Combine spread, depth, volume |
| `test_analyze_portfolio_risk` | Aggregate risk metrics | Sum positions, check exposure |

**Example Run:**
```bash
pytest tests/kalshi/test_integration_demo.py::TestPhase2MarketIntelligence -m manual -v
```

### Phase 4: WebSocket Streaming (4 tests)

**Class**: `TestPhase3WebSocketStreaming`

Tests real-time data feeds (live market updates, order book changes, trade feeds):

| Test | Purpose | Channel |
|------|---------|---------|
| `test_websocket_connect_ticker_channel` | Real-time prices | `ticker` |
| `test_websocket_subscribe_orderbook_snapshot` | Full order book state | `orderbook_snapshot` |
| `test_websocket_subscribe_trades_feed` | Public trade feed | `trades` |
| `test_websocket_disconnect_graceful` | Clean shutdown | Connection management |

**Note**: WebSocket tests are slow (real-time subscriptions). Run with `-m slow` if using that marker.

**Example Run:**
```bash
pytest tests/kalshi/test_integration_demo.py::TestPhase3WebSocketStreaming -m manual -v -s
```

### Phase 5: Advanced Features (12 tests)

**Class**: `TestPhase4AdvancedFeatures`

Tests advanced trading features for sophisticated traders:

#### Multivariate Collections (4 tests)

Collections of related markets with conditional trading:

```
test_get_multivariate_collections          → List all collections
test_get_multivariate_collection_details    → Fetch collection structure
test_get_markets_in_collection              → Enumerate markets in collection
test_lookup_market_in_collection            → Lookup specific market
```

#### RFQ/Quote Lifecycle (5 tests)

Request-for-Quote system for market maker negotiations:

```
test_create_rfq                    → Create RFQ (bulk quote request)
test_get_rfq_list                  → List open RFQs
test_create_quote_response         → Submit quote (as market maker)
test_get_quotes_for_rfq            → View all quotes for an RFQ
test_accept_quote                  → Accept and execute quote
```

#### Market Maker Analysis (2 tests)

Tools for analyzing market making opportunities:

```
test_analyze_market_maker_opportunity    → Score markets by spread/depth/volatility
test_assess_rfq_demand_patterns          → Analyze RFQ volume by ticker
```

**Example Run:**
```bash
pytest tests/kalshi/test_integration_demo.py::TestPhase4AdvancedFeatures -m manual -v
```

### Phase 6: Error Handling (5 tests)

**Class**: `TestErrorHandling`

Tests edge cases and error conditions:

| Test | Validates |
|------|-----------|
| `test_invalid_market_ticker` | Non-existent market returns appropriate error |
| `test_order_price_out_of_range` | Price must be 1-99 cents |
| `test_insufficient_balance_check` | Can't order more than available balance |
| `test_batch_order_max_limit` | Batch create limited to 20 orders |
| `test_concurrent_order_operations` | Multiple simultaneous operations handled correctly |

**Example Run:**
```bash
pytest tests/kalshi/test_integration_demo.py::TestErrorHandling -m manual -v
```

## Running Tests in Different Modes

### Run All Tests with Verbose Output

```bash
pytest tests/kalshi/test_integration_demo.py -m manual -v
```

### Show Print Statements and Logging

```bash
pytest tests/kalshi/test_integration_demo.py -m manual -v -s
```

### Run with Timing Information

```bash
pytest tests/kalshi/test_integration_demo.py -m manual -v --durations=10
```

Shows slowest 10 tests - useful for identifying performance issues.

### Run with Coverage Report

```bash
pytest tests/kalshi/test_integration_demo.py -m manual -v --cov=src.kalshi --cov-report=html
```

Opens `htmlcov/index.html` to view coverage by line.

### Run Tests in Parallel

```bash
pytest tests/kalshi/test_integration_demo.py -m manual -v -n auto
```

**Note**: Requires `pytest-xdist` plugin. Be careful with parallel execution when tests modify state.

## Test Execution Examples

### Example 1: Complete Integration Test Suite

```bash
# Run all 47 tests with detailed output
$ pytest tests/kalshi/test_integration_demo.py -m manual -v

============= test session starts =============
platform darwin -- Python 3.11.0, pytest-8.4.2
collected 47 items

tests/kalshi/test_integration_demo.py::TestDemoEnvironmentSetup::test_demo_client_initializes PASSED [ 2%]
tests/kalshi/test_integration_demo.py::TestDemoEnvironmentSetup::test_demo_mcp_server_loads PASSED [ 4%]
tests/kalshi/test_integration_demo.py::TestDemoEnvironmentSetup::test_demo_api_connectivity PASSED [ 6%]
tests/kalshi/test_integration_demo.py::TestDemoEnvironmentSetup::test_demo_account_has_mock_funds PASSED [ 8%]
tests/kalshi/test_integration_demo.py::TestCriticalPathTrading::test_search_open_markets PASSED [ 10%]
... [35 more tests] ...

============= 47 passed in 145.32s =============
```

### Example 2: Just Critical Path Tests (10 tests, ~30 seconds)

```bash
$ pytest tests/kalshi/test_integration_demo.py::TestCriticalPathTrading -m manual -v --durations=5

============= test session starts =============
tests/kalshi/test_integration_demo.py::TestCriticalPathTrading::test_search_open_markets PASSED [ 10%]
tests/kalshi/test_integration_demo.py::TestCriticalPathTrading::test_get_market_details_with_orderbook PASSED [ 20%]
... [8 more tests] ...

============= 10 passed in 28.45s =============

============= slowest 5 durations =============
15.23s call     tests/kalshi/test_integration_demo.py::TestCriticalPathTrading::test_create_market_order
8.34s call      tests/kalshi/test_integration_demo.py::TestCriticalPathTrading::test_get_fill_history
4.12s call      tests/kalshi/test_integration_demo.py::TestCriticalPathTrading::test_create_limit_order_buy
```

### Example 3: Test a Single Order Creation

```bash
$ pytest tests/kalshi/test_integration_demo.py::TestCriticalPathTrading::test_create_limit_order_buy -m manual -vvs

============= test session starts =============
tests/kalshi/test_integration_demo.py::TestCriticalPathTrading::test_create_limit_order_buy PASSED
[test output with print statements shown]
```

## Common Issues and Troubleshooting

### Issue: Tests marked with `@pytest.mark.manual` not running

**Problem**: By default, pytest doesn't run tests marked `manual`.

**Solution**: Always include `-m manual` flag:
```bash
pytest tests/kalshi/test_integration_demo.py -m manual -v
```

### Issue: "KALSHI_DEMO_API_KEY_ID environment variable is required"

**Problem**: Demo credentials not configured.

**Solution**:
1. Create demo account at https://demo.kalshi.co/
2. Generate API keys
3. Add to `.env`:
```bash
KALSHI_DEMO_API_KEY_ID=your-key
KALSHI_DEMO_PRIVATE_KEY_PATH=/path/to/private_key.pem
```

### Issue: "401 Unauthorized" errors in tests

**Problem**: Demo API key is invalid or expired.

**Solution**:
1. Log in to https://demo.kalshi.co/
2. Check that API key is active
3. Regenerate if needed
4. Update `.env` with new key
5. Restart test suite

### Issue: "Insufficient balance" errors

**Problem**: Demo account has insufficient mock funds.

**Solution**:
1. Check balance at https://demo.kalshi.co/account
2. If low, you can:
   - Create a new demo account (get fresh $10,000)
   - Contact Kalshi support to reset your demo account
   - Reduce order sizes in tests to fit available balance

### Issue: WebSocket tests timeout

**Problem**: Demo API WebSocket has high latency or connectivity issues.

**Solution**:
1. Increase timeout in test fixture (modify `conftest.py`):
```python
@pytest.fixture
def mock_demo_kalshi_client(demo_client_credentials):
    return DemoKalshiClient(timeout=60.0)  # Increase from 30.0
```
2. Check network connectivity: `ping demo-api.kalshi.co`
3. Try running test with `-v -s` to see connection logs

### Issue: Tests pass individually but fail when run together

**Problem**: Tests may have shared state or resource conflicts.

**Solution**:
1. Check test fixtures for cleanup code
2. Ensure each test creates independent orders
3. Use `pytest -x` to stop on first failure
4. Review test isolation in `conftest.py`

## Test Maintenance

### Adding a New Test

1. Determine which phase it belongs to (critical path, portfolio, etc.)
2. Add to appropriate test class in `test_integration_demo.py`
3. Use existing fixtures: `mock_demo_kalshi_client`, `sample_market`, etc.
4. Mark with decorators:
```python
@pytest.mark.manual
@pytest.mark.demo
@pytest.mark.integration
async def test_my_new_feature(self, mock_demo_kalshi_client):
    """Test description."""
    result = await mock_demo_kalshi_client.my_method()
    assert result is not None
```

### Updating Test Documentation

When test purposes change or new phases are added, update:
1. This file (`docs/INTEGRATION_TESTING.md`)
2. Test docstrings in `test_integration_demo.py`
3. CLAUDE.md Demo Environment section

### Monitoring Test Health

Track test results over time:

```bash
# Generate test report with timestamps
pytest tests/kalshi/test_integration_demo.py -m manual -v --tb=short 2>&1 | tee test_run_$(date +%Y%m%d_%H%M%S).log
```

## Performance Baselines

Expected execution times for full test suite:

| Phase | Test Count | Typical Duration |
|-------|-----------|------------------|
| Environment Setup | 4 | 5-10s |
| Critical Path | 10 | 30-45s |
| Portfolio Mgmt | 7 | 20-30s |
| Market Intelligence | 5 | 15-25s |
| WebSocket (slow) | 4 | 30-60s |
| Advanced Features | 12 | 40-60s |
| Error Handling | 5 | 10-15s |
| **Total** | **47** | **2-3 minutes** |

If tests consistently exceed these times, there may be:
- Network latency to demo API
- Overloaded demo API server
- Test timeout settings too low

## Next Steps

1. ✅ Set up demo credentials (see CLAUDE.md)
2. ✅ Run environment setup tests to verify connectivity
3. ✅ Run critical path tests to validate core functionality
4. ✅ Run full suite to exercise all features
5. 📝 Review any failing tests and update as needed
6. 🚀 Use demo environment for ongoing development and testing

## Reference

- **Demo Environment Setup**: See `.claude/CLAUDE.md` → "Demo Environment Setup"
- **Test Code**: `tests/kalshi/test_integration_demo.py`
- **Test Fixtures**: `tests/conftest.py`
- **Demo Client**: `src/kalshi/client_demo.py`
- **Demo MCP Server**: `src/kalshi/kalshi_mcp_server_demo.py`
- **Kalshi Demo API**: https://demo.kalshi.co/

---

**Last Updated**: November 2025
