---
url: https://docs.kalshi.com/websockets/orderbook-updates
title: Orderbook Updates - API Documentation
description: Real-time orderbook price level changes. Provides incremental updates to maintain a live orderbook.

**Requirements:**
- Market specification required:
  - Use `market_ticker` (string) for a single market
  - Use `market_tickers` (array of strings) for multiple markets
- Sends `orderbook_snapshot` first, then incremental `orderbook_delta` updates

**Use case:** Building and maintaining a real-time orderbook

scraped_at: 2025-11-03T14:46:58.057030
---

[Skip to main content](https://docs.kalshi.com/websockets/orderbook-updates#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

Websockets

Orderbook Updates

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Messages

Orderbook Snapshot

    {  "type": "orderbook_snapshot",  "sid": 2,  "seq": 2,  "msg": {    "market_ticker": "FED-23DEC-T3.00",    "yes": [      [        8,        300      ],      [        22,        333      ]    ],    "yes_dollars": [      [        "0.080",        300      ],      [        "0.220",        333      ]    ],    "no": [      [        54,        20      ],      [        56,        146      ]    ],    "no_dollars": [      [        "0.540",        20      ],      [        "0.560",        146      ]    ]  }}

Orderbook Delta

    {  "type": "orderbook_delta",  "sid": 2,  "seq": 3,  "msg": {    "market_ticker": "FED-23DEC-T3.00",    "price": 96,    "price_dollars": "0.960",    "delta": -54,    "side": "yes"  }}

WSS

wss://api.elections.kalshi.com

orderbook\_delta

Messages

Orderbook Snapshot

    {  "type": "orderbook_snapshot",  "sid": 2,  "seq": 2,  "msg": {    "market_ticker": "FED-23DEC-T3.00",    "yes": [      [        8,        300      ],      [        22,        333      ]    ],    "yes_dollars": [      [        "0.080",        300      ],      [        "0.220",        333      ]    ],    "no": [      [        54,        20      ],      [        56,        146      ]    ],    "no_dollars": [      [        "0.540",        20      ],      [        "0.560",        146      ]    ]  }}

Orderbook Delta

    {  "type": "orderbook_delta",  "sid": 2,  "seq": 3,  "msg": {    "market_ticker": "FED-23DEC-T3.00",    "price": 96,    "price_dollars": "0.960",    "delta": -54,    "side": "yes"  }}

Security Schemes

apiKey

type:apiKey

API key authentication required for WebSocket connections. The API key should be provided during the WebSocket handshake.

Receive

Orderbook Snapshot

type:object

show 4 properties

Complete view of the order book's aggregated price levels

Orderbook Delta

type:object

show 4 properties

Update to be applied to the current order book view

[Connection Keep-Alive](https://docs.kalshi.com/websockets/connection-keep-alive)
[Market Ticker](https://docs.kalshi.com/websockets/market-ticker)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.