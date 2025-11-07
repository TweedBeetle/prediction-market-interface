# Polymarket API Structure - Discovered During Implementation

This document summarizes the actual Polymarket API structure discovered during implementation and testing, which differs from initial assumptions.

## API Endpoints

Polymarket uses **two separate APIs** with different authentication requirements:

### 1. Gamma API (Read-Only Market Data)

**Base URL**: `https://gamma-api.polymarket.com`
**Authentication**: None required
**Purpose**: Public market metadata and discovery

**Available Endpoints**:
- `GET /markets` - Search and list markets
- `GET /markets/{id}` - Get specific market by ID
- `GET /markets/slug/{slug}` - Get market by URL slug
- `GET /events` - List events (collections of markets)
- `GET /events/{id}` - Get specific event
- `GET /events/slug/{slug}` - Get event by URL slug
- `GET /tags` - Get available tags for filtering
- `GET /sports` - Get sports metadata

**What's NOT in Gamma API**:
- ❌ Trades (requires auth, on CLOB API)
- ❌ Orderbook (public, but on CLOB API)
- ❌ Positions (requires auth, on CLOB API)
- ❌ Orders (requires auth, on CLOB API)

### 2. CLOB API (Trading and Market Data)

**Base URL**: `https://clob.polymarket.com`
**Authentication**: Mixed (some endpoints public, some require L2 headers)
**Purpose**: Order book, trading, and portfolio management

**Public Endpoints** (No Auth Required):
- `GET /book?token_id={id}` - Get orderbook for a token
- `GET /price?token_id={id}&side={BUY|SELL}` - Get market price
- `GET /sampling-markets` - Get sampling markets
- `GET /sampling-simplified-markets` - Get simplified sampling markets

**Authenticated Endpoints** (Require L2 Headers):
- `GET /data/trades` - Get user's trade history
- `POST /orders` - Create order
- `DELETE /orders/{id}` - Cancel order
- `GET /orders` - Get user's orders
- `GET /positions` - Get user's positions
- `GET /fills` - Get user's fills
- `POST /auth/api-key` - Obtain API credentials via EIP-712

**L2 Authentication Headers Required**:
```
POLY-ADDRESS: <wallet_address>
POLY-API-KEY: <api_key>
POLY-PASSPHRASE: <api_passphrase>
POLY-SIGNATURE: <hmac_signature>
POLY-TIMESTAMP: <unix_timestamp>
```

## Implementation Architecture

### GammaClient
**Purpose**: Read-only market discovery
**Authentication**: None
**Endpoints**:
- `search_markets()` → `GET /markets`
- `get_market()` → `GET /markets/{id}`
- `get_market_by_slug()` → `GET /markets/slug/{slug}`
- `get_events()` → `GET /events`
- `get_event()` → `GET /events/{id}`

### ClobClient
**Purpose**: Trading and portfolio (authenticated + some public)
**Authentication**: EIP-712 signing for auth, then API keys

**Public Methods** (no auth required):
- `get_orderbook()` → `GET /book`
- `get_price()` → `GET /price`

**Authenticated Methods**:
- `authenticate()` → `POST /auth/api-key`
- `create_order()` → `POST /orders`
- `cancel_order()` → `DELETE /orders/{id}`
- `get_orders()` → `GET /orders`
- `get_positions()` → `GET /positions`
- `get_trades()` → `GET /data/trades`

## Key Differences from Documentation

### 1. API Response Format

**Expected** (from some docs):
```json
{
  "condition_id": "...",
  "clob_token_ids": ["...", "..."]
}
```

**Actual** (from real API):
```json
{
  "conditionId": "...",  // camelCase!
  "clobTokenIds": "[\"...\", \"...\"]"  // JSON string!
}
```

### 2. Numeric Fields

**Expected**: Numbers as JSON numbers
```json
{
  "volume": 32257.45,
  "liquidity": 1000.0
}
```

**Actual**: Numbers as JSON strings
```json
{
  "volume": "32257.445115",
  "liquidity": "1000.00"
}
```

### 3. Optional Fields

Many markets don't have all fields:
- `clobTokenIds` may be missing (non-tradeable markets)
- `volume`, `liquidity` may be null or empty strings
- `best_bid`, `best_ask` may be missing (no current orders)

## Testing Implications

### Integration Tests WITHOUT Funds

✅ Can test these endpoints (no auth required):
- Gamma API: All endpoints (`/markets`, `/events`)
- CLOB API: Public endpoints (`/book`, `/price`)

❌ Cannot test these without funded wallet:
- CLOB API: Authenticated endpoints (`/data/trades`, `/orders`, `/positions`)

### VCR Cassette Recording

Cassettes work well for:
- Gamma API (stable, no auth)
- CLOB public endpoints (stable, no auth)

Cassettes problematic for:
- CLOB authenticated endpoints (signatures expire, need real wallet)

## MCP Tools Mapping

| MCP Tool | Client | Endpoint | Auth Required |
|----------|--------|----------|---------------|
| `polymarket_search_markets` | GammaClient | `GET /markets` | No |
| `polymarket_get_market` | GammaClient | `GET /markets/{id}` | No |
| `polymarket_list_events` | GammaClient | `GET /events` | No |
| `polymarket_get_orderbook` | ClobClient | `GET /book` | No |
| `polymarket_get_market_trades` | ClobClient | `GET /data/trades` | Yes |
| `polymarket_create_order` | ClobClient | `POST /orders` | Yes |
| `polymarket_cancel_order` | ClobClient | `DELETE /orders/{id}` | Yes |
| `polymarket_get_positions` | ClobClient | `GET /positions` | Yes |
| `polymarket_get_order_history` | ClobClient | `GET /orders` | Yes |

## WebSocket API (Not Yet Implemented)

Polymarket also provides WebSocket APIs for real-time data:

- `wss://ws-subscriptions-clob.polymarket.com/ws/market` - Market channel
- `wss://ws-subscriptions-clob.polymarket.com/ws/user` - User channel (requires auth)

These could be added in Phase 2 for streaming orderbook updates and trade notifications.

## References

- Gamma API: https://gamma-api.polymarket.com
- CLOB API: https://clob.polymarket.com
- Official Docs: https://docs.polymarket.com
- Python SDK: https://github.com/Polymarket/py-clob-client

## Lessons Learned

1. **Test against real API early** - Documentation can be outdated or incomplete
2. **camelCase vs snake_case** - JavaScript APIs often use camelCase
3. **String numbers** - Many APIs return numbers as strings for precision
4. **Mixed authentication** - Some endpoints public, some require auth on same API
5. **No testnet** - All testing is on mainnet with real money (use small amounts)
