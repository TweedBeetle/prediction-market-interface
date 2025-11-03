---
url: https://docs.kalshi.com/websockets/market-ticker
title: Market Ticker - API Documentation
description: Market price, volume, and open interest updates.

**Requirements:**
- Market specification optional (omit to receive all markets)
- Updates sent whenever any ticker field changes

**Use case:** Displaying current market prices and statistics

scraped_at: 2025-11-03T14:46:57.560910
---

[Skip to main content](https://docs.kalshi.com/websockets/market-ticker#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

Websockets

Market Ticker

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Messages

Ticker Update

    {  "type": "ticker",  "sid": 11,  "msg": {    "market_ticker": "FED-23DEC-T3.00",    "price": 48,    "yes_bid": 45,    "yes_ask": 53,    "price_dollars": "0.480",    "yes_bid_dollars": "0.345",    "no_bid_dollars": "0.655",    "volume": 33896,    "open_interest": 20422,    "dollar_volume": 16948,    "dollar_open_interest": 10211,    "ts": 1669149841  }}

WSS

wss://api.elections.kalshi.com

ticker

Messages

Ticker Update

    {  "type": "ticker",  "sid": 11,  "msg": {    "market_ticker": "FED-23DEC-T3.00",    "price": 48,    "yes_bid": 45,    "yes_ask": 53,    "price_dollars": "0.480",    "yes_bid_dollars": "0.345",    "no_bid_dollars": "0.655",    "volume": 33896,    "open_interest": 20422,    "dollar_volume": 16948,    "dollar_open_interest": 10211,    "ts": 1669149841  }}

Security Schemes

apiKey

type:apiKey

API key authentication required for WebSocket connections. The API key should be provided during the WebSocket handshake.

Receive

Ticker Update

type:object

show 3 properties

Market price ticker information

[Orderbook Updates](https://docs.kalshi.com/websockets/orderbook-updates)
[Public Trades](https://docs.kalshi.com/websockets/public-trades)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.