---
url: https://docs.kalshi.com/websockets/public-trades
title: Public Trades - API Documentation
description: Public trade notifications when trades occur.

**Requirements:**
- Market specification optional (omit to receive all trades)
- Updates sent immediately after trade execution

**Use case:** Trade feed, volume analysis

scraped_at: 2025-11-03T14:46:57.936083
---

[Skip to main content](https://docs.kalshi.com/websockets/public-trades#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

Websockets

Public Trades

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Messages

Trade Update

    {  "type": "trade",  "sid": 11,  "msg": {    "market_ticker": "HIGHNY-22DEC23-B53.5",    "yes_price": 36,    "yes_price_dollars": "0.360",    "no_price": 64,    "no_price_dollars": "0.640",    "count": 136,    "taker_side": "no",    "ts": 1669149841  }}

WSS

wss://api.elections.kalshi.com

trade

Messages

Trade Update

    {  "type": "trade",  "sid": 11,  "msg": {    "market_ticker": "HIGHNY-22DEC23-B53.5",    "yes_price": 36,    "yes_price_dollars": "0.360",    "no_price": 64,    "no_price_dollars": "0.640",    "count": 136,    "taker_side": "no",    "ts": 1669149841  }}

Security Schemes

apiKey

type:apiKey

API key authentication required for WebSocket connections. The API key should be provided during the WebSocket handshake.

Receive

Trade Update

type:object

show 3 properties

Public trade information

[Market Ticker](https://docs.kalshi.com/websockets/market-ticker)
[User Fills](https://docs.kalshi.com/websockets/user-fills)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.