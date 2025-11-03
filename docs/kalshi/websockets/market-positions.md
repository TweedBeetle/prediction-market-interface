---
url: https://docs.kalshi.com/websockets/market-positions
title: Market Positions - API Documentation
description: Real-time updates of your positions in markets. Requires authentication.

**Requirements:**
- Authentication required
- Market specification optional (omit to receive all positions)
- Updates sent when your position changes due to trades, settlements, etc.

**Monetary Values:**
All monetary values (position_cost, realized_pnl, fees_paid) are returned in centi-cents (1/10,000th of a dollar).
To convert to dollars, divide by 10,000.

**Use case:** Portfolio tracking, position monitoring, P&L calculations

scraped_at: 2025-11-03T14:46:58.056353
---

[Skip to main content](https://docs.kalshi.com/websockets/market-positions#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

Websockets

Market Positions

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Messages

Market Position Update

    {  "type": "market_position",  "sid": 14,  "msg": {    "user_id": "user123",    "market_ticker": "FED-23DEC-T3.00",    "position": 100,    "position_cost": 500000,    "realized_pnl": 100000,    "fees_paid": 10000,    "volume": 15  }}

WSS

wss://api.elections.kalshi.com

market\_positions

Messages

Market Position Update

    {  "type": "market_position",  "sid": 14,  "msg": {    "user_id": "user123",    "market_ticker": "FED-23DEC-T3.00",    "position": 100,    "position_cost": 500000,    "realized_pnl": 100000,    "fees_paid": 10000,    "volume": 15  }}

Security Schemes

apiKey

type:apiKey

API key authentication required for WebSocket connections. The API key should be provided during the WebSocket handshake.

Receive

Market Position Update

type:object

show 3 properties

Real-time position updates for authenticated user

[User Fills](https://docs.kalshi.com/websockets/user-fills)
[Market & Event Lifecycle](https://docs.kalshi.com/websockets/market-&-event-lifecycle)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.