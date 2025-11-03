---
url: https://docs.kalshi.com/websockets/user-fills
title: User Fills - API Documentation
description: Your order fill notifications. Requires authentication.

**Requirements:**
- Authentication required
- Market specification ignored (always sends all your fills)
- Updates sent immediately when your orders are filled

**Use case:** Tracking your trading activity

scraped_at: 2025-11-03T14:46:58.055364
---

[Skip to main content](https://docs.kalshi.com/websockets/user-fills#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

Websockets

User Fills

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Messages

Fill Update

    {  "type": "fill",  "sid": 13,  "msg": {    "trade_id": "d91bc706-ee49-470d-82d8-11418bda6fed",    "order_id": "ee587a1c-8b87-4dcf-b721-9f6f790619fa",    "market_ticker": "HIGHNY-22DEC23-B53.5",    "is_taker": true,    "side": "yes",    "yes_price": 75,    "yes_price_dollars": "0.750",    "count": 278,    "action": "buy",    "ts": 1671899397,    "post_position": 500  }}

WSS

wss://api.elections.kalshi.com

fill

Messages

Fill Update

    {  "type": "fill",  "sid": 13,  "msg": {    "trade_id": "d91bc706-ee49-470d-82d8-11418bda6fed",    "order_id": "ee587a1c-8b87-4dcf-b721-9f6f790619fa",    "market_ticker": "HIGHNY-22DEC23-B53.5",    "is_taker": true,    "side": "yes",    "yes_price": 75,    "yes_price_dollars": "0.750",    "count": 278,    "action": "buy",    "ts": 1671899397,    "post_position": 500  }}

Security Schemes

apiKey

type:apiKey

API key authentication required for WebSocket connections. The API key should be provided during the WebSocket handshake.

Receive

Fill Update

type:object

show 3 properties

Private fill information for authenticated user

[Public Trades](https://docs.kalshi.com/websockets/public-trades)
[Market Positions](https://docs.kalshi.com/websockets/market-positions)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.