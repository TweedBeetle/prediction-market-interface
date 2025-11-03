# Quick Start Guide

## Installation & Setup

### 1. Install Dependencies
```bash
cd ~/projects/prediction-market-interface
uv sync
```

### 2. Configure Credentials
```bash
# Add your Kalshi API key ID to .env
echo "KALSHI_API_KEY_ID=your-uuid-here" >> .env

# Copy your private key
cp /path/to/kalshi_private_key.pem secrets/kalshi_private_key.txt

# Update path in .env
echo "KALSHI_PRIVATE_KEY_PATH=secrets/kalshi_private_key.txt" >> .env
```

### 3. Verify Setup
```bash
uv run python -c "from src.kalshi import KalshiClient; print('✓ Ready')"
```

## Running the MCP Server

### Start Server
```bash
uv run python -m src.kalshi.kalshi_mcp_server
```

### Use with Claude Code
Add to `.claude/settings.json`:
```json
{
  "mcpServers": {
    "kalshi": {
      "command": "uv",
      "args": ["run", "python", "-m", "src.kalshi.kalshi_mcp_server"],
      "env": {
        "KALSHI_API_KEY_ID": "${KALSHI_API_KEY_ID}",
        "KALSHI_PRIVATE_KEY_PATH": "secrets/kalshi_private_key.txt"
      }
    }
  }
}
```

## Using the Python Client Directly

### Example 1: Search Markets
```python
import asyncio
from src.kalshi import KalshiClient

async def main():
    client = KalshiClient()

    # Search open markets
    markets, cursor = await client.search_markets(status="open", limit=5)

    for market in markets:
        print(f"{market.ticker}: {market.title}")
        print(f"  Yes: {market.yes_bid}¢ / {market.yes_ask}¢")
        print(f"  Volume: {market.volume} contracts")
        print()

asyncio.run(main())
```

### Example 2: Get Account Info
```python
import asyncio
from src.kalshi import KalshiClient

async def main():
    client = KalshiClient()

    # Check balance
    balance = await client.get_balance()
    print(f"Balance: ${balance.balance / 100:.2f}")
    print(f"Portfolio: ${balance.portfolio_value / 100:.2f}")

    # Get positions
    positions, cursor = await client.get_positions()
    print(f"\nPositions ({len(positions)} total):")
    for pos in positions:
        print(f"  {pos.ticker}: {pos.position} contracts @ {pos.fill_price}¢")

asyncio.run(main())
```

### Example 3: Place an Order
```python
import asyncio
from src.kalshi import KalshiClient

async def main():
    client = KalshiClient()

    # Place a buy order
    order = await client.create_order(
        ticker="KXHARRIS24-LSV",
        side="buy",
        count=10,
        type="limit",
        price=65  # 65 cents
    )

    print(f"Order placed: {order.id}")
    print(f"  Status: {order.status}")
    print(f"  {order.count} contracts @ {order.price}¢")

asyncio.run(main())
```

### Example 4: Get Historical Data
```python
import asyncio
from src.kalshi import KalshiClient

async def main():
    client = KalshiClient()

    # Get daily candlesticks for past month
    candlesticks = await client.get_candlesticks(
        series_ticker="PRES-2024",
        ticker="KXHARRIS24-LSV",
        interval="1440min"  # daily
    )

    print(f"Historical data ({len(candlesticks)} days):")
    for candle in candlesticks[-5:]:  # Last 5 days
        print(f"  {candle.start_ts}: O:{candle.open} H:{candle.high} L:{candle.low} C:{candle.close} V:{candle.volume}")

asyncio.run(main())
```

## Using with Claude

Once MCP server is running, you can ask Claude questions like:

**Market Research:**
- "Search for open markets related to elections"
- "What's the current price of KXHARRIS24-LSV?"
- "Show me the order book for that market"
- "Give me historical prices for the past week"

**Portfolio Management:**
- "What's my current balance?"
- "Show me all my open positions"
- "What orders do I have?"
- "How much have I traded in KXHARRIS24-LSV?"

**Trading:**
- "Buy 100 contracts of KXHARRIS24-LSV at 65 cents"
- "Cancel order [order-id]"
- "Modify my order to 70 cents"

**Analysis:**
- "Find all trending markets"
- "List markets closing in the next week"
- "Show me markets with the highest volume"

## Available Tools

### Read-Only (Market Data)
- `kalshi_search_markets`
- `kalshi_get_market`
- `kalshi_get_orderbook`
- `kalshi_get_trades`
- `kalshi_get_candlesticks`
- `kalshi_get_events`
- `kalshi_get_event`
- `kalshi_get_series`
- `kalshi_get_exchange_status`
- `kalshi_get_milestones`

### Trading
- `kalshi_get_balance`
- `kalshi_get_positions`
- `kalshi_create_order` ⚠️
- `kalshi_get_orders`
- `kalshi_cancel_order` ⚠️
- `kalshi_amend_order` ⚠️
- `kalshi_get_fills`
- `kalshi_get_queue_position`

### Advanced
- `kalshi_batch_create_orders` ⚠️
- `kalshi_batch_cancel_orders` ⚠️
- `kalshi_create_order_group`
- `kalshi_get_order_groups`
- `kalshi_create_rfq`
- `kalshi_get_rfqs`
- `kalshi_get_multivariate_collections`

### Real-Time (WebSocket)
- `kalshi_websocket_connect`
- `kalshi_websocket_subscribe`
- `kalshi_websocket_unsubscribe`
- `kalshi_websocket_disconnect`

⚠️ = Requires user confirmation

## Troubleshooting

### Import Error: ModuleNotFoundError
```bash
# Sync dependencies
uv sync

# Verify imports
uv run python -c "from src.kalshi import KalshiClient"
```

### Authentication Error: 401 Unauthorized
```bash
# Check API key is correct
echo $KALSHI_API_KEY_ID

# Verify private key exists
ls -la secrets/kalshi_private_key.txt

# Test client
uv run python -c "
from src.kalshi import KalshiClient
import asyncio
client = KalshiClient()
asyncio.run(client.get_exchange_status())
"
```

### Rate Limit Error: 429 Too Many Requests
```bash
# Reduce request rate or wait before retrying
# Default: 20 reads/sec, 10 writes/sec (Basic tier)

# If you need higher limits, apply at Kalshi
# https://kalshi.com/api
```

## Environment Variables

| Variable | Example | Required |
|----------|---------|----------|
| `KALSHI_API_KEY_ID` | `550e8400-e29b-41d4-a716-446655440000` | ✅ |
| `KALSHI_PRIVATE_KEY_PATH` | `secrets/kalshi_private_key.txt` | ✅ |
| `KALSHI_READ_ONLY` | `false` | ❌ |
| `KALSHI_TIMEOUT` | `30` | ❌ |

## Next Steps

1. **Run MCP Server**: `uv run python -m src.kalshi.kalshi_mcp_server`
2. **Configure Claude**: Add to `.claude/settings.json`
3. **Start Trading**: Ask Claude to help with market analysis and trading

## Documentation

- **README.md** - Full documentation
- **IMPLEMENTATION_SUMMARY.md** - Technical details
- **src/kalshi/client.py** - API client docstrings
- **src/kalshi/models.py** - Data model definitions
- **src/kalshi/kalshi_mcp_server.py** - MCP tool descriptions

## Support

- Kalshi API Docs: https://kalshi.com/api
- MCP Docs: https://modelcontextprotocol.io
- Issues: GitHub Issues
