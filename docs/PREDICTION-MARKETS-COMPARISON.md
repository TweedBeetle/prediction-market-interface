# Prediction Market Platforms - Comparison & Implementation Status

**Last Updated**: 2025-11-05

## Overview

This repository contains MCP (Model Context Protocol) server implementations for two major prediction market platforms: **Kalshi** and **Polymarket**. These servers enable LLM agents (like Claude) to discover markets, analyze opportunities, and execute trades through natural language conversations.

---

## Implementation Status

### Kalshi MCP Server

**Status**: ✅ **Phase 1 Complete** | ✅ **Phase 2 Complete**

- **24 MCP tools** implemented and tested
- **107 integration tests** passing
- **Live data verified** - All endpoints functional
- **Advanced features** - Batch operations, order groups, OCO strategies

**Documentation**:
- PRD: `docs/kalshi-mcp-prd.md`
- Gotchas: `docs/kalshi/gotchas/CLAUDE.md`
- API Docs: `docs/kalshi/` (scraped from docs.kalshi.com)

**Quick Start**:
```bash
# Register demo server (safe testing)
claude mcp add kalshi_demo --scope project -- bash -c "cd $(pwd) && uv run run_kalshi_mcp_demo.py"

# Use in Claude Code
User: "@kalshi_demo search for election markets"
```

### Polymarket MCP Server

**Status**: 📋 **Planning Complete** | ⏳ **Implementation Not Started**

- **PRD**: Comprehensive 4-phase plan (12 → 20 → 26 → 36+ tools)
- **Architecture**: Dual-client system (Gamma + CLOB APIs)
- **Technical Spec**: Complete data models, authentication system, signing utilities

**Documentation**:
- PRD: `docs/polymarket-mcp-prd.md`
- Implementation Plan: `docs/polymarket-implementation-plan.md`
- API Docs: `docs/polymarket/` (scraped from docs.polymarket.com)

**Timeline**: 8 weeks for Phase 1 (estimated)

---

## Platform Comparison

| Feature | Kalshi | Polymarket |
|---------|--------|------------|
| **Architecture** | Centralized | Blockchain (Polygon) |
| **Custody** | Custodial | Non-custodial |
| **Authentication** | API key (RSA-PSS) | EIP-712 wallet signing |
| **Settlement** | Off-chain (internal) | On-chain (public blockchain) |
| **Fees** | Volume-based | 0% (currently) |
| **Market Count** | ~1,000+ | ~10,000+ |
| **Real-time Data** | Polling only | WebSocket (built-in) |
| **Order Types** | Limit (market deprecated) | Limit only |
| **Batch Orders** | Yes (advanced tier) | Yes (native) |
| **Geographic Access** | US-only (CFTC regulated) | Global (blockchain-based) |
| **Liquidity** | CLOB only | AMM + CLOB hybrid |
| **Resolution** | Internal Kalshi process | UMA oracle (decentralized) |
| **API Complexity** | Medium | High (2 APIs + blockchain) |
| **Regulatory Status** | CFTC regulated | Unregulated |

---

## Feature Comparison

### Market Discovery

| Feature | Kalshi | Polymarket |
|---------|--------|------------|
| **Search** | Client-side filtering | Native search API |
| **Text Search** | ❌ Not supported | ✅ Full-text search |
| **Metadata** | Basic (ticker, title) | Rich (tags, categories, series, collections) |
| **Hierarchy** | Events → Markets | Events → Markets, Series, Collections |
| **Price History** | ❌ Not available | ✅ OHLCV candlesticks |
| **Orderbook Depth** | ✅ Supported | ✅ Supported |

### Trading Capabilities

| Feature | Kalshi | Polymarket |
|---------|--------|------------|
| **Limit Orders** | ✅ | ✅ |
| **Market Orders** | ❌ Deprecated | ❌ Not supported |
| **Batch Orders** | ✅ (up to 20) | ✅ (up to 20) |
| **Order Groups** | ✅ (OCO strategies) | ❌ Not supported |
| **Amend Orders** | ✅ Without losing queue | ❌ Cancel and replace |
| **Advanced Params** | ✅ FOK/IOC/GTC/GTT, post-only, reduce-only | ✅ FOK/IOC/GTC |
| **Order Signing** | Server-side | Client-side (EIP-712) |

### Portfolio Management

| Feature | Kalshi | Polymarket |
|---------|--------|------------|
| **Positions** | ✅ | ✅ |
| **Fill History** | ✅ | ✅ |
| **P&L Tracking** | ✅ | ✅ |
| **Active Orders** | ✅ | ✅ |
| **Top Holders** | ❌ | ✅ |
| **Social Features** | ❌ | ✅ (comments, profiles) |

### Real-Time Features

| Feature | Kalshi | Polymarket |
|---------|--------|------------|
| **WebSocket** | ❌ Not available | ✅ Market + User channels |
| **Price Updates** | Polling required | ✅ Real-time streaming |
| **Order Status** | Polling required | ✅ Real-time updates |
| **Fill Notifications** | Polling required | ✅ Real-time notifications |

---

## Use Cases

### Best for Kalshi

1. **US-Based Trading**
   - CFTC regulated, legal for US residents
   - Fiat on/off ramps (ACH, wire)

2. **Institutional Use**
   - Regulatory compliance
   - Traditional finance integration

3. **Advanced Order Strategies**
   - Order groups (OCO strategies)
   - Complex multi-leg trades

4. **Small Market Focus**
   - Lower fees for smaller trades
   - Good for testing strategies

### Best for Polymarket

1. **Global Trading**
   - No geographic restrictions
   - Crypto-native users

2. **High Volume Trading**
   - Zero fees (currently)
   - Deep liquidity on popular markets

3. **Market Research**
   - 10x more markets than Kalshi
   - Rich metadata and categorization
   - Full-text search

4. **Non-Custodial Preference**
   - Users retain control of funds
   - On-chain settlement verification
   - Trustless execution

5. **Real-Time Trading**
   - WebSocket streaming
   - Instant price updates

---

## Cross-Platform Arbitrage

**Opportunity**: Same events often exist on both platforms with different prices.

**Example**:
```
Event: "Bitcoin reaches $100K by Dec 31, 2025"

Kalshi:  YES @ 42¢
Polymarket: YES @ 45¢

Arbitrage: Sell YES on Polymarket, Buy YES on Kalshi
Spread: 3¢ per share (7% profit potential)
```

**Phase 4 Feature** (Polymarket):
- `polymarket_find_arbitrage_kalshi()` - Detect opportunities
- `polymarket_execute_arbitrage()` - Atomic cross-platform execution

---

## Technical Architecture

### Kalshi Architecture

```
┌─────────────────────┐
│   Kalshi MCP Server │
└──────────┬──────────┘
           │
           ↓
    ┌──────────────┐
    │ KalshiClient │ (Single API)
    └──────┬───────┘
           │
           ↓
  ┌────────────────┐
  │ Kalshi REST API│ (trading-api.kalshi.com)
  └────────────────┘
           │
           ↓
  ┌────────────────┐
  │ Kalshi Exchange│ (Centralized)
  └────────────────┘
```

### Polymarket Architecture

```
┌──────────────────────┐
│ Polymarket MCP Server│
└──────────┬───────────┘
           │
    ┌──────┴───────┐
    │              │
    ↓              ↓
┌──────────┐  ┌──────────┐
│  Gamma   │  │   CLOB   │
│  Client  │  │  Client  │
└────┬─────┘  └────┬─────┘
     │             │
     ↓             ↓
┌──────────┐  ┌──────────┐
│ Gamma API│  │ CLOB API │
│(read-only)  │(trading) │
└──────────┘  └────┬─────┘
                   │
              EIP-712 Signing
                   │
                   ↓
           ┌───────────────┐
           │Polygon Network│
           │ (Blockchain)  │
           └───────────────┘
```

---

## Development Roadmap

### Kalshi (Completed)

- ✅ Phase 1: Basic trading (16 tools) - **Complete**
- ✅ Phase 2: Advanced features (8 tools) - **Complete**
- ⏭️ Phase 3: WebSocket streaming - **Deferred** (API doesn't support)
- ⏭️ Phase 4: Analytics & intelligence - **Future**

### Polymarket (Planned)

- 📋 Phase 1: MVP (12 tools) - **8 weeks** (not started)
  - Market discovery
  - Basic trading
  - EIP-712 signing
  - Dual-client architecture

- 📋 Phase 2: Advanced trading (8 tools) - **2-3 weeks**
  - Batch operations
  - Portfolio analytics
  - Advanced searches

- 📋 Phase 3: Real-time streaming (6 tools) - **2 weeks**
  - WebSocket integration
  - Real-time price updates
  - Order status streaming

- 📋 Phase 4: Analytics & arbitrage (10+ tools) - **3-4 weeks**
  - Cross-platform arbitrage
  - Historical analysis
  - Social features

**Total Polymarket Timeline**: ~15-17 weeks for all phases

---

## Testing Strategy Comparison

### Kalshi

**Infrastructure**:
- VCR cassettes (2.5x faster tests)
- Integration tests against demo API
- E2E tests bypass VCR for correctness

**Coverage**:
- 107 integration tests
- 13 Pydantic models
- 49 VCR cassettes

**Key Learnings**:
- VCR can mask bugs (see Phase 2 order groups bug)
- Always test MCP tools directly
- Unit tests for model parsing essential

### Polymarket

**Planned Infrastructure**:
- VCR for market data (Gamma API)
- Live testing for trading (CLOB API)
- Signature validation tests
- Small-amount mainnet testing

**Challenges**:
- No testnet for Polygon CLOB
- Must test with real USDC (small amounts)
- EIP-712 signature bugs can be costly

---

## Dependencies

### Kalshi

```toml
[dependencies]
httpx = ">=0.27.0"
pydantic = ">=2.0.0"
python-dotenv = ">=1.0.0"
loguru = ">=0.7.0"
cryptography = ">=42.0.0"  # RSA-PSS signing
fastmcp = ">=2.0.0"
```

### Polymarket (Additional)

```toml
[dependencies]
# All Kalshi dependencies plus:
eth-account = ">=0.10.0"  # EIP-712 signing
web3 = ">=6.0.0"          # Blockchain interaction
eth-keys = ">=0.4.0"      # Key management
```

---

## Configuration Examples

### Kalshi

```bash
# Demo environment
KALSHI_API_KEY=your_demo_api_key
KALSHI_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----"
KALSHI_ENVIRONMENT=demo
KALSHI_BASE_URL=https://demo-api.kalshi.co
```

### Polymarket

```bash
# Mainnet (no testnet available)
POLYMARKET_PRIVATE_KEY=0x...  # Polygon wallet private key
POLYMARKET_PROXY_ADDRESS=0x...  # If using Magic/browser wallet
POLYMARKET_SIGNATURE_TYPE=1  # 1=Magic, 2=Browser, omit=EOA
POLYMARKET_CHAIN_ID=137  # Polygon mainnet
```

---

## Security Considerations

### Kalshi

**Risks**:
- API key compromise (can trade on your behalf)
- Private key exposure (full account access)

**Mitigations**:
- Environment variables only
- Never log credentials
- Separate demo/prod keys

### Polymarket

**Risks**:
- Private key exposure (full wallet access - all crypto!)
- Signature bugs (can drain wallet)
- On-chain transactions (gas fees, irreversible)

**Mitigations**:
- **CRITICAL**: Use dedicated trading wallet with limited funds
- Hardware wallet support (future)
- Extensive signature validation tests
- Dry-run mode for testing
- Clear user warnings about non-custodial risks

---

## Getting Started

### For Developers

**1. Clone Repository**
```bash
git clone https://github.com/your-org/prediction-market-interface
cd prediction-market-interface
```

**2. Install Dependencies**
```bash
uv sync
```

**3. Set Up Kalshi (Working)**
```bash
# Copy environment template
cp .env.kalshi.demo.example .env.kalshi.demo

# Add your credentials
vim .env.kalshi.demo

# Run tests
uv run pytest tests/kalshi/

# Register MCP server
claude mcp add kalshi_demo --scope project -- bash -c "cd $(pwd) && uv run run_kalshi_mcp_demo.py"
```

**4. Set Up Polymarket (Not Implemented)**
```bash
# Will be available after Phase 1 implementation
# See docs/polymarket-mcp-prd.md for roadmap
```

### For Users

**Kalshi**:
1. Sign up at https://kalshi.com or https://demo.kalshi.co
2. Generate API key in settings
3. Use `@kalshi_demo` or `@kalshi_prod` in Claude Code

**Polymarket** (Future):
1. Create Polygon wallet or use existing
2. Fund with USDC on Polygon network
3. Use `@polymarket` in Claude Code

---

## Future Enhancements

### Cross-Platform Features

1. **Unified Interface**
   - Single MCP server for both platforms
   - Automatic routing based on market availability
   - Unified position tracking

2. **Arbitrage Detection**
   - Real-time price comparison
   - Automatic arbitrage execution
   - Fee & slippage calculation

3. **Portfolio Aggregation**
   - Combined P&L across platforms
   - Correlation analysis
   - Risk management

4. **Market Intelligence**
   - Compare liquidity across platforms
   - Historical price divergence
   - Platform-specific patterns

---

## Contributing

### Kalshi

Contributions welcome! Areas of focus:
- Phase 3 alternatives (since no WebSocket)
- Phase 4 analytics
- Improved error handling
- Additional safety validations

### Polymarket

**Phase 1 Implementation** - seeking contributors:
- EIP-712 signing implementation
- Dual-client architecture
- MCP tools development
- Testing infrastructure

---

## Resources

### Kalshi

- **Official API Docs**: https://docs.kalshi.com
- **Trading Console**: https://kalshi.com
- **Demo Environment**: https://demo.kalshi.co

### Polymarket

- **Official API Docs**: https://docs.polymarket.com
- **Trading Console**: https://polymarket.com
- **GitHub Clients**:
  - Python: https://github.com/Polymarket/py-clob-client
  - TypeScript: https://github.com/Polymarket/clob-client

### General

- **FastMCP Framework**: https://github.com/jlowin/fastmcp
- **Claude Code**: https://docs.anthropic.com/claude-code
- **MCP Protocol**: https://modelcontextprotocol.io

---

## License

MIT License - See LICENSE file for details

---

## Acknowledgments

- **Kalshi** for CFTC-regulated prediction markets
- **Polymarket** for pioneering blockchain-based prediction markets
- **FastMCP** for making MCP server development simple
- **Claude Code** for enabling LLM-powered trading interfaces

---

## Contact & Support

For questions or issues:
- Kalshi Implementation: See `docs/kalshi-mcp-prd.md`
- Polymarket Implementation: See `docs/polymarket-mcp-prd.md`
- General Questions: Open an issue on GitHub
