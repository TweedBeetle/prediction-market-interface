# Polymarket WebSocket Streaming Guide

**Real-time market data streaming for LLM agents**

## Overview

This guide explains how to use Polymarket's WebSocket client for real-time market data streaming. The architecture separates concerns between **MCP tools** (request/response operations) and **Python WebSocket client** (streaming operations), giving agents maximum flexibility.

## Architecture

### Design Principle: Separation of Concerns

**MCP Tools** = Request/Response Operations
- Market discovery (`polymarket_search_markets`)
- Order execution (`polymarket_create_order`)
- Portfolio queries (`polymarket_get_positions`)
- Historical data (`polymarket_get_trades`)

**Python WebSocket Client** = Streaming Operations
- Real-time price updates
- Order book changes
- User order/fill notifications
- Custom event processing

###Why This Architecture?

✅ **MCP Protocol Alignment**: MCP is request/response, not designed for streaming
✅ **Agent Flexibility**: Full control over streaming logic in Python code
✅ **Performance**: Direct WebSocket connection, no MCP overhead
✅ **Maintainability**: Clear separation, independent testing

## Quick Start

### Installation

Dependencies are already included in `pyproject.toml`:
```bash
uv sync
```

### Basic Usage

```python
from polymarket.websocket_client import PolymarketWebSocketClient

# Connect and stream market data
async with PolymarketWebSocketClient() as ws:
    # Subscribe to a market
    await ws.subscribe_market("0xabc123...")

    # Stream events
    async for event in ws:
        if event.event_type == "price_change":
            print(f"New price: {event.price}")
            print(f"Probability: {event.probability_pct:.1f}%")
```

## Agent Workflow Patterns

### Pattern 1: Discovery + Monitoring

**Use Case**: Find markets, then monitor prices in real-time

```python
# Step 1: Agent uses MCP tool for discovery
markets = await polymarket_search_markets("Bitcoin $100K", limit=5)
btc_market = markets[0]

print(f"Monitoring: {btc_market['question']}")
print(f"Current price: ${btc_market['best_ask']:.2f}")

# Step 2: Agent writes code for real-time monitoring
from polymarket.websocket_client import PolymarketWebSocketClient

async with PolymarketWebSocketClient() as ws:
    await ws.subscribe_market(btc_market["condition_id"])

    async for event in ws:
        if event.event_type == "price_change":
            print(f"Price update: ${event.price:.2f}")

            # Alert if price crosses threshold
            if event.price > 0.60:
                print("⚠️ ALERT: Price crossed $0.60!")
                break
```

### Pattern 2: Arbitrage Detection

**Use Case**: Monitor multiple markets for arbitrage opportunities

```python
# Step 1: Agent discovers related markets via MCP tools
presidential_markets = await polymarket_search_markets("2024 presidential", limit=10)

trump_market = next(m for m in presidential_markets if "Trump" in m["question"])
harris_market = next(m for m in presidential_markets if "Harris" in m["question"])

# Step 2: Agent monitors both for arbitrage
from polymarket.websocket_client import PolymarketWebSocketClient

async with PolymarketWebSocketClient() as ws:
    # Subscribe to both markets
    await ws.subscribe_market(trump_market["condition_id"])
    await ws.subscribe_market(harris_market["condition_id"])

    # Track prices
    prices = {}

    async for event in ws:
        if event.event_type == "price_change":
            prices[event.market] = event.price

            # Check if both prices available
            if len(prices) == 2:
                total = sum(prices.values())

                print(f"Trump: {prices[trump_market['condition_id']]:.3f}")
                print(f"Harris: {prices[harris_market['condition_id']]:.3f}")
                print(f"Total: {total:.3f}")

                # Arbitrage exists if total ≠ 1.00
                if total < 0.98:
                    profit_pct = (1.0 - total) / total * 100
                    print(f"🎯 ARBITRAGE: {profit_pct:.2f}% profit available!")

                    # Agent executes via MCP tool
                    await polymarket_create_orders_batch([
                        {
                            "token_id": trump_market["clob_token_ids"][0],
                            "side": "BUY",
                            "price": prices[trump_market["condition_id"]],
                            "size": 100
                        },
                        {
                            "token_id": harris_market["clob_token_ids"][0],
                            "side": "BUY",
                            "price": prices[harris_market["condition_id"]],
                            "size": 100
                        }
                    ])

                    print("✓ Arbitrage executed!")
                    break
```

### Pattern 3: Position Monitoring + Auto-Exit

**Use Case**: Monitor position P&L and auto-exit at profit target

```python
# Step 1: Agent checks current position via MCP tool
positions = await polymarket_get_positions()
my_position = positions[0]  # Monitoring first position

print(f"Position: {my_position['outcome']} {my_position['size']} shares")
print(f"Entry: ${my_position['entry_price']:.2f}")
print(f"Current P&L: ${my_position['pnl_dollars']:.2f}")

# Step 2: Agent monitors for profit target
from polymarket.websocket_client import PolymarketWebSocketClient

PROFIT_TARGET = 50.00  # $50 profit target

async with PolymarketWebSocketClient() as ws:
    await ws.subscribe_market(my_position["market_id"])

    async for event in ws:
        if event.event_type == "price_change":
            # Calculate current P&L
            current_value = event.price * my_position["size"]
            cost_basis = my_position["entry_price"] * my_position["size"]
            unrealized_pnl = current_value - cost_basis

            print(f"Price: ${event.price:.2f} | P&L: ${unrealized_pnl:.2f}")

            # Exit if profit target hit
            if unrealized_pnl >= PROFIT_TARGET:
                print(f"✓ Profit target reached: ${unrealized_pnl:.2f}")

                # Agent closes position via MCP tool
                result = await polymarket_close_position(my_position["market_id"])

                print(f"✓ Position closed at ${event.price:.2f}")
                print(f"✓ Realized profit: ${result['position']['pnl_dollars']:.2f}")
                break
```

### Pattern 4: Order Book Analysis

**Use Case**: Monitor order book depth for optimal execution

```python
# Step 1: Agent discovers market
market = await polymarket_get_market("election-market-id")

# Step 2: Agent monitors order book for liquidity
from polymarket.websocket_client import PolymarketWebSocketClient

TARGET_SIZE = 1000  # Want to buy 1000 shares

async with PolymarketWebSocketClient() as ws:
    await ws.subscribe_market(market["condition_id"])

    async for event in ws:
        if event.event_type == "book":  # Order book update
            # Calculate available liquidity
            available_liquidity = sum(level.size for level in event.asks[:5])
            avg_price = sum(l.price * l.size for l in event.asks[:5]) / available_liquidity

            print(f"Liquidity: {available_liquidity:.0f} shares")
            print(f"Avg price (top 5 levels): ${avg_price:.3f}")
            print(f"Spread: ${event.spread:.3f}")

            # Execute if enough liquidity
            if available_liquidity >= TARGET_SIZE:
                print(f"✓ Sufficient liquidity available!")

                # Agent places order via MCP tool
                order = await polymarket_create_order(
                    token_id=market["clob_token_ids"][0],
                    side="BUY",
                    price=avg_price + 0.005,  # 0.5¢ better than avg
                    size=TARGET_SIZE
                )

                print(f"✓ Order placed: {order['order_id']}")
                break
```

## Event Types

### Market Data Events (Public)

#### PriceChangeEvent
```python
{
    "event_type": "price_change",
    "asset_id": "token_yes_abc123",
    "market": "0xabc123...",
    "price": 0.55,
    "side": "ASK"
}
```

**Properties**:
- `price`: Price as decimal (0.001-0.999)
- `probability_pct`: Auto-calculated percentage (55%)
- `asset_id`: Token ID (YES or NO outcome)

#### LastTradePriceEvent
```python
{
    "event_type": "last_trade_price",
    "asset_id": "token_yes_abc123",
    "market": "0xabc123...",
    "price": 0.547,
    "size": 150.0
}
```

#### OrderBookUpdate
```python
{
    "event_type": "book",
    "asset_id": "token_yes_abc123",
    "market": "0xabc123...",
    "bids": [
        {"price": 0.54, "size": 100.0},
        {"price": 0.53, "size": 50.0}
    ],
    "asks": [
        {"price": 0.56, "size": 75.0}
    ]
}
```

**Properties**:
- `best_bid`: Top bid level
- `best_ask`: Top ask level
- `spread`: Bid-ask spread

### User Events (Authenticated)

#### UserOrderEvent
```python
{
    "event_type": "user_order",
    "order_id": "0x789...",
    "market": "0xabc123...",
    "side": "BUY",
    "price": 0.55,
    "size": 100.0,
    "size_matched": 50.0,
    "status": "LIVE"
}
```

**Properties**:
- `is_filled`: Boolean (fully filled?)
- `fill_percentage`: Percentage filled

#### UserFillEvent
```python
{
    "event_type": "user_fill",
    "fill_id": "fill_123",
    "order_id": "0x789...",
    "price": 0.55,
    "size": 50.0,
    "fee": 0.0
}
```

**Properties**:
- `total_cost`: Price × size + fee

## Advanced Features

### Authenticated Streams

For order/fill notifications, provide API key:

```python
from polymarket.websocket_client import PolymarketWebSocketClient

# Initialize with API key
ws_client = PolymarketWebSocketClient(api_key="your_api_key")

async with ws_client:
    # Subscribe to user channel
    await ws_client.subscribe_user()

    async for event in ws_client:
        if event.event_type == "user_fill":
            print(f"✓ Order filled: {event.size} @ ${event.price}")

        elif event.event_type == "user_order":
            print(f"Order status: {event.status} ({event.fill_percentage:.1f}% filled)")
```

### Multiple Markets

Monitor multiple markets simultaneously:

```python
async with PolymarketWebSocketClient() as ws:
    # Subscribe to multiple markets
    await ws.subscribe_market("market_1")
    await ws.subscribe_market("market_2")
    await ws.subscribe_market("market_3")

    # Stream all events
    async for event in ws:
        print(f"Market {event.market}: {event.event_type}")
```

### Custom Filtering

Filter events in your code:

```python
async with PolymarketWebSocketClient() as ws:
    await ws.subscribe_market(market_id)

    # Only process price changes > 1% movement
    last_price = None

    async for event in ws:
        if event.event_type == "price_change":
            if last_price is not None:
                change_pct = abs(event.price - last_price) / last_price * 100

                if change_pct > 1.0:
                    print(f"⚠️ Large move: {change_pct:.1f}% ({last_price:.3f} → {event.price:.3f})")

            last_price = event.price
```

### Reconnection Handling

Client automatically reconnects on disconnect:

```python
async with PolymarketWebSocketClient() as ws:
    await ws.subscribe_market(market_id)

    try:
        async for event in ws:
            # Process events
            # If connection drops, client will:
            # 1. Reconnect automatically
            # 2. Resubscribe to all channels
            # 3. Resume streaming
            pass

    except Exception as e:
        print(f"Error: {e}")
        # Client will attempt reconnection
```

## Error Handling

### Connection Errors

```python
from polymarket.websocket_client import PolymarketWebSocketClient

try:
    async with PolymarketWebSocketClient() as ws:
        await ws.subscribe_market(market_id)
        async for event in ws:
            # Process events
            pass

except ConnectionError as e:
    print(f"Failed to connect: {e}")

except Exception as e:
    print(f"Unexpected error: {e}")
```

### Event Parsing Errors

Invalid events are logged and skipped:

```python
# Client automatically:
# 1. Logs parsing errors
# 2. Skips invalid messages
# 3. Continues streaming valid events

# You see only successfully parsed events
async for event in ws:
    # This is always a valid, parsed event
    print(event.model_dump())
```

## Performance Considerations

### Message Rate

Polymarket WebSocket can send many messages per second during high activity:

```python
# Rate limiting pattern
from time import time

last_process_time = 0
MIN_INTERVAL = 0.1  # Process max once per 100ms

async for event in ws:
    current_time = time()

    if current_time - last_process_time >= MIN_INTERVAL:
        # Process event
        print(f"Price: {event.price}")
        last_process_time = current_time
    # else: skip (too frequent)
```

### Multiple Markets

Subscribing to many markets increases message volume:

```python
# Good: Monitor 1-5 markets actively
await ws.subscribe_market("market_1")
await ws.subscribe_market("market_2")

# Careful: 10+ markets = high message rate
# Consider filtering or sampling
```

## Testing

### Unit Tests

```bash
# Run unit tests (mocked WebSocket)
uv run pytest tests/polymarket/unit/test_websocket_client.py -v
```

### Integration Tests

```bash
# Run integration tests (real WebSocket)
uv run pytest tests/polymarket/integration/test_websocket_integration.py -v

# Skip if endpoint unavailable
SKIP_WEBSOCKET_INTEGRATION=true uv run pytest tests/polymarket/integration/test_websocket_integration.py
```

### Setting Test Market ID

```bash
# Provide real market for integration tests
export TEST_MARKET_ID="0xabc123..."
uv run pytest tests/polymarket/integration/test_websocket_integration.py -v
```

## Comparison: MCP Tools vs WebSocket Client

| Operation | Use MCP Tool | Use WebSocket Client |
|-----------|--------------|----------------------|
| Search markets | ✅ `polymarket_search_markets` | ❌ |
| Get current price | ✅ `polymarket_get_market` | ❌ (snapshot) |
| Stream price updates | ❌ | ✅ `subscribe_market` |
| Place order | ✅ `polymarket_create_order` | ❌ |
| Monitor order fills | ❌ (polling) | ✅ `subscribe_user` |
| Close position | ✅ `polymarket_close_position` | ❌ |
| Real-time arbitrage | ❌ (too slow) | ✅ (streaming) |

**Rule of Thumb**: If it's a one-time operation or mutation, use MCP tools. If it's continuous monitoring, use WebSocket client.

## Common Patterns Summary

### 1. Price Alert
```python
# MCP: Discovery → WebSocket: Monitoring → MCP: Action
market = await polymarket_get_market(...)
async with WebSocketClient() as ws:
    await ws.subscribe_market(market["condition_id"])
    async for event in ws:
        if event.price > threshold:
            await polymarket_create_order(...)
```

### 2. Arbitrage Detection
```python
# WebSocket: Monitor multiple markets → MCP: Batch execution
async with WebSocketClient() as ws:
    await ws.subscribe_market(market1)
    await ws.subscribe_market(market2)
    # Calculate arbitrage → execute via MCP batch order
```

### 3. Position Management
```python
# MCP: Check position → WebSocket: Monitor → MCP: Close
position = await polymarket_get_positions()
async with WebSocketClient() as ws:
    await ws.subscribe_market(position["market_id"])
    # Monitor P&L → close via MCP when target hit
```

## Troubleshooting

### Connection Issues

**Problem**: `ConnectionError: WebSocket connection failed`

**Solutions**:
1. Check internet connectivity
2. Verify WebSocket URL is correct
3. Check if Polymarket API is operational
4. Review firewall/proxy settings

### No Events Received

**Problem**: Connected but no events streaming

**Solutions**:
1. Verify market is active (not closed/settled)
2. Check subscription was successful: `print(ws._subscriptions)`
3. Ensure market ID is correct (condition_id, not question ID)
4. Try a high-liquidity market (more activity = more events)

### Authentication Errors

**Problem**: User channel subscription fails

**Solutions**:
1. Verify API key is set: `PolymarketWebSocketClient(api_key="...")`
2. Check API key is valid (not expired)
3. Ensure API key has correct permissions

## Additional Resources

- **MCP Tools Reference**: See `docs/polymarket/index.md`
- **API Models**: See `src/polymarket/websocket_models.py`
- **Example Scripts**: See `examples/polymarket_streaming_examples.py`
- **Integration Tests**: See `tests/polymarket/integration/test_websocket_integration.py`

## Support

For issues or questions:
- Check integration tests for working examples
- Review unit tests for detailed behavior
- See `src/polymarket/websocket_client.py` for implementation details
