# Kalshi API Documentation

**Mirror of**: https://docs.kalshi.com/
**Scraped**: 2025-11-03
**Total pages**: 127

## Structure

This documentation mirror preserves the original URL structure as a directory hierarchy for easy navigation.

## Quick Links

### Getting Started
- [Welcome](index.md)
- [API Keys](getting_started/api_keys.md)
- [Demo Environment](getting_started/demo_env.md)
- [Making Your First Request](getting_started/making_your_first_request.md)
- [Quick Start: Authenticated Requests](getting_started/quick_start_authenticated_requests.md)
- [Quick Start: Market Data](getting_started/quick_start_market_data.md)
- [Quick Start: Create Order](getting_started/quick_start_create_order.md)
- [Quick Start: WebSockets](getting_started/quick_start_websockets.md)

### Core Concepts
- [Orderbook Responses](getting_started/orderbook_responses.md)
- [Pagination](getting_started/pagination.md)
- [Rate Limits](getting_started/rate_limits.md)
- [Subpenny Pricing](getting_started/subpenny_pricing.md)
- [Terms](getting_started/terms.md)

### API Reference

#### Portfolio Operations
- [Create Order](api-reference/portfolio/create-order.md)
- [Amend Order](api-reference/portfolio/amend-order.md)
- [Cancel Order](api-reference/portfolio/cancel-order.md)
- [Get Orders](api-reference/portfolio/get-orders.md)
- [Get Order](api-reference/portfolio/get-order.md)
- [Get Positions](api-reference/portfolio/get-positions.md)
- [Get Balance](api-reference/portfolio/get-balance.md)
- [Get Fills](api-reference/portfolio/get-fills.md)
- [Get Settlements](api-reference/portfolio/get-settlements.md)
- [Batch Create Orders](api-reference/portfolio/batch-create-orders.md)
- [Batch Cancel Orders](api-reference/portfolio/batch-cancel-orders.md)

#### Market Data
- [Get Markets](api-reference/market/get-markets.md)
- [Get Market](api-reference/market/get-market.md)
- [Get Market Orderbook](api-reference/market/get-market-orderbook.md)
- [Get Market Candlesticks](api-reference/market/get-market-candlesticks.md)
- [Get Trades](api-reference/market/get-trades.md)
- [Get Series](api-reference/market/get-series.md)
- [Get Series List](api-reference/market/get-series-list.md)

#### Events
- [Get Events](api-reference/events/get-events.md)
- [Get Event](api-reference/events/get-event.md)
- [Get Event Metadata](api-reference/events/get-event-metadata.md)
- [Get Event Candlesticks](api-reference/events/get-event-candlesticks.md)
- [Get Event Forecast Percentile History](api-reference/events/get-event-forecast-percentile-history.md)
- [Get Multivariate Events](api-reference/events/get-multivariate-events.md)

#### API Keys
- [Get API Keys](api-reference/api-keys/get-api-keys.md)
- [Create API Key](api-reference/api-keys/create-api-key.md)
- [Generate API Key](api-reference/api-keys/generate-api-key.md)
- [Delete API Key](api-reference/api-keys/delete-api-key.md)

#### Exchange Status
- [Get Exchange Status](api-reference/exchange/get-exchange-status.md)
- [Get Exchange Schedule](api-reference/exchange/get-exchange-schedule.md)
- [Get Exchange Announcements](api-reference/exchange/get-exchange-announcements.md)
- [Get User Data Timestamp](api-reference/exchange/get-user-data-timestamp.md)
- [Get Series Fee Changes](api-reference/exchange/get-series-fee-changes.md)

#### Communications (RFQ)
- [Create RFQ](api-reference/communications/create-rfq.md)
- [Get RFQ](api-reference/communications/get-rfq.md)
- [Get RFQs](api-reference/communications/get-rfqs.md)
- [Delete RFQ](api-reference/communications/delete-rfq.md)
- [Create Quote](api-reference/communications/create-quote.md)
- [Get Quote](api-reference/communications/get-quote.md)
- [Get Quotes](api-reference/communications/get-quotes.md)
- [Accept Quote](api-reference/communications/accept-quote.md)
- [Confirm Quote](api-reference/communications/confirm-quote.md)
- [Delete Quote](api-reference/communications/delete-quote.md)
- [Get Communications ID](api-reference/communications/get-communications-id.md)

#### Other APIs
- [Milestones](api-reference/milestone/) - Get milestone, get milestones
- [Multivariate Collections](api-reference/collection/) - Create, get, lookup operations
- [Structured Targets](api-reference/structured-targets/) - Get structured target, get structured targets
- [Live Data](api-reference/live_data/) - Get live data, get multiple live data
- [FCM Operations](api-reference/fcm/) - Get FCM orders, get FCM positions
- [Incentive Programs](api-reference/incentive_programs/) - Get volume incentives
- [Search](api-reference/search/) - Get filters for sports, get tags for series categories

### WebSockets
- [WebSocket Connection](websockets/websocket-connection.md)
- [Connection Keep-Alive](websockets/connection-keep-alive.md)
- [Market Ticker](websockets/market-ticker.md)
- [Orderbook Updates](websockets/orderbook-updates.md)
- [Public Trades](websockets/public-trades.md)
- [User Fills](websockets/user-fills.md)
- [Market Positions](websockets/market-positions.md)
- [Market & Event Lifecycle](websockets/market-&-event-lifecycle.md)
- [Communications](websockets/communications.md)
- [Multivariate Lookups](websockets/multivariate-lookups.md)

### SDKs
- [Overview](sdks/overview.md)
- [Python SDK Quickstart](sdks/python/quickstart.md)
- [TypeScript SDK Quickstart](sdks/typescript/quickstart.md)

#### Python SDK API
- [ApiKeysApi](python-sdk/api/ApiKeysApi.md)
- [CommunicationsApi](python-sdk/api/CommunicationsApi.md)
- [EventsApi](python-sdk/api/EventsApi.md)
- [ExchangeApi](python-sdk/api/ExchangeApi.md)
- [MarketsApi](python-sdk/api/MarketsApi.md)
- [MilestonesApi](python-sdk/api/MilestonesApi.md)
- [MultivariateCollectionsApi](python-sdk/api/MultivariateCollectionsApi.md)
- [PortfolioApi](python-sdk/api/PortfolioApi.md)
- [SeriesApi](python-sdk/api/SeriesApi.md)
- [StructuredTargetsApi](python-sdk/api/StructuredTargetsApi.md)

#### TypeScript SDK API
- [ApiKeysApi](typescript-sdk/api/ApiKeysApi.md)
- [CommunicationsApi](typescript-sdk/api/CommunicationsApi.md)
- [EventsApi](typescript-sdk/api/EventsApi.md)
- [ExchangeApi](typescript-sdk/api/ExchangeApi.md)
- [MarketsApi](typescript-sdk/api/MarketsApi.md)
- [MilestonesApi](typescript-sdk/api/MilestonesApi.md)
- [MultivariateCollectionsApi](typescript-sdk/api/MultivariateCollectionsApi.md)
- [PortfolioApi](typescript-sdk/api/PortfolioApi.md)
- [SeriesApi](typescript-sdk/api/SeriesApi.md)
- [StructuredTargetsApi](typescript-sdk/api/StructuredTargetsApi.md)

### FIX Protocol
- [Overview](fix/index.md)
- [Connectivity](fix/connectivity.md)
- [Session Management](fix/session-management.md)
- [Order Entry](fix/order-entry.md)
- [Order Groups](fix/order-groups.md)
- [RFQ Messages](fix/rfq-messages.md)
- [Drop Copy](fix/drop-copy.md)
- [Market Settlement](fix/market-settlement.md)
- [Subpenny Pricing](fix/subpenny-pricing.md)
- [Error Handling](fix/error-handling.md)

### Other
- [Changelog](changelog.md)

## File Format

All files include YAML frontmatter with metadata:
```yaml
---
url: https://docs.kalshi.com/api-reference/portfolio/create-order
title: Create Order | Kalshi API
description: API endpoint for creating orders
scraped_at: 2025-11-03T14:30:00.123456
---
```

## Usage

**Search across all docs**:
```bash
cd /Users/christo/projects/prediction-market-interface/docs/kalshi
grep -r "search term" .
```

**Find specific endpoints**:
```bash
find . -name "*order*.md"
find . -path "*/portfolio/*"
```

**Browse by section**:
```bash
ls api-reference/
ls getting_started/
ls websockets/
```

## Notes

- This is a static mirror - check [docs.kalshi.com](https://docs.kalshi.com/) for the latest updates
- All files preserve original URL in frontmatter for reference
- Base64 images removed for cleaner markdown
- Main content only (navigation/footers stripped by Firecrawl)
- Total mirror size: ~1.5MB of clean markdown

## Regenerating

To update this mirror:
```bash
# 1. Discover URLs
fc-map https://docs.kalshi.com/ > /tmp/kalshi_map.json

# 2. Create mapping (use Python script in /tmp/create_kalshi_mapping.py)
python3 /tmp/create_kalshi_mapping.py

# 3. Scrape
uv run ~/.claude/skills/docs2md/docs2md.py -m /tmp/kalshi_mapping.json -o . -w 10
```
