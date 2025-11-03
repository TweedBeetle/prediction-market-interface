---
url: https://docs.kalshi.com/websockets/communications
title: Communications - API Documentation
description: Real-time Request for Quote (RFQ) and quote notifications. Requires authentication.

**Requirements:**
- Authentication required
- Market specification ignored
- RFQ events (RFQCreated, RFQDeleted) always sent
- Quote events (QuoteCreated, QuoteAccepted) are only sent if you created the quote OR you created the RFQ

**Use case:** Tracking RFQs you create and quotes on your RFQs, or quotes you create on others' RFQs

scraped_at: 2025-11-03T14:46:58.057220
---

[Skip to main content](https://docs.kalshi.com/websockets/communications#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

Websockets

Communications

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Messages

RFQ Created

    {  "type": "rfq_created",  "sid": 15,  "msg": {    "id": "rfq_123",    "creator_id": "comm_abc123",    "market_ticker": "FED-23DEC-T3.00",    "event_ticker": "FED-23DEC",    "contracts": 100,    "target_cost": 3500,    "target_cost_dollars": "0.35",    "created_ts": "2024-12-01T10:00:00Z"  }}

RFQ Deleted

    {  "type": "rfq_deleted",  "sid": 15,  "msg": {    "id": "rfq_123",    "creator_id": "comm_abc123",    "market_ticker": "FED-23DEC-T3.00",    "event_ticker": "FED-23DEC",    "contracts": 100,    "target_cost": 3500,    "target_cost_dollars": "0.35",    "deleted_ts": "2024-12-01T10:05:00Z"  }}

Quote Created

    {  "type": "quote_created",  "sid": 15,  "msg": {    "quote_id": "quote_456",    "rfq_id": "rfq_123",    "quote_creator_id": "comm_def456",    "rfq_creator_id": "comm_abc123",    "market_ticker": "FED-23DEC-T3.00",    "event_ticker": "FED-23DEC",    "yes_bid": 35,    "no_bid": 65,    "yes_bid_dollars": "0.35",    "no_bid_dollars": "0.65",    "yes_contracts_offered": 100,    "no_contracts_offered": 200,    "rfq_target_cost": 3500,    "rfq_target_cost_dollars": "0.35",    "created_ts": "2024-12-01T10:02:00Z"  }}

Quote Accepted

    {  "type": "quote_accepted",  "sid": 15,  "msg": {    "quote_id": "quote_456",    "rfq_id": "rfq_123",    "quote_creator_id": "comm_def456",    "rfq_creator_id": "comm_abc123",    "market_ticker": "FED-23DEC-T3.00",    "event_ticker": "FED-23DEC",    "yes_bid": 35,    "no_bid": 65,    "yes_bid_dollars": "0.35",    "no_bid_dollars": "0.65",    "accepted_side": "yes",    "yes_contracts_offered": 100,    "no_contracts_offered": 200,    "rfq_target_cost": 3500,    "rfq_target_cost_dollars": "0.35"  }}

WSS

wss://api.elections.kalshi.com

communications

Messages

RFQ Created

    {  "type": "rfq_created",  "sid": 15,  "msg": {    "id": "rfq_123",    "creator_id": "comm_abc123",    "market_ticker": "FED-23DEC-T3.00",    "event_ticker": "FED-23DEC",    "contracts": 100,    "target_cost": 3500,    "target_cost_dollars": "0.35",    "created_ts": "2024-12-01T10:00:00Z"  }}

RFQ Deleted

    {  "type": "rfq_deleted",  "sid": 15,  "msg": {    "id": "rfq_123",    "creator_id": "comm_abc123",    "market_ticker": "FED-23DEC-T3.00",    "event_ticker": "FED-23DEC",    "contracts": 100,    "target_cost": 3500,    "target_cost_dollars": "0.35",    "deleted_ts": "2024-12-01T10:05:00Z"  }}

Quote Created

    {  "type": "quote_created",  "sid": 15,  "msg": {    "quote_id": "quote_456",    "rfq_id": "rfq_123",    "quote_creator_id": "comm_def456",    "rfq_creator_id": "comm_abc123",    "market_ticker": "FED-23DEC-T3.00",    "event_ticker": "FED-23DEC",    "yes_bid": 35,    "no_bid": 65,    "yes_bid_dollars": "0.35",    "no_bid_dollars": "0.65",    "yes_contracts_offered": 100,    "no_contracts_offered": 200,    "rfq_target_cost": 3500,    "rfq_target_cost_dollars": "0.35",    "created_ts": "2024-12-01T10:02:00Z"  }}

Quote Accepted

    {  "type": "quote_accepted",  "sid": 15,  "msg": {    "quote_id": "quote_456",    "rfq_id": "rfq_123",    "quote_creator_id": "comm_def456",    "rfq_creator_id": "comm_abc123",    "market_ticker": "FED-23DEC-T3.00",    "event_ticker": "FED-23DEC",    "yes_bid": 35,    "no_bid": 65,    "yes_bid_dollars": "0.35",    "no_bid_dollars": "0.65",    "accepted_side": "yes",    "yes_contracts_offered": 100,    "no_contracts_offered": 200,    "rfq_target_cost": 3500,    "rfq_target_cost_dollars": "0.35"  }}

Security Schemes

apiKey

type:apiKey

API key authentication required for WebSocket connections. The API key should be provided during the WebSocket handshake.

Receive

RFQ Created

type:object

show 3 properties

Notification when an RFQ is created

RFQ Deleted

type:object

show 3 properties

Notification when an RFQ is deleted

Quote Created

type:object

show 3 properties

Notification when a quote is created on an RFQ

Quote Accepted

type:object

show 3 properties

Notification when a quote is accepted

[Multivariate Lookups](https://docs.kalshi.com/websockets/multivariate-lookups)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.