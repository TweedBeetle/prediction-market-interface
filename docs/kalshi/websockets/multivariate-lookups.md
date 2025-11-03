---
url: https://docs.kalshi.com/websockets/multivariate-lookups
title: Multivariate Lookups - API Documentation
description: Multivariate collection lookup notifications.

**Requirements:**
- Market specification optional

**Use case:** Tracking multivariate market relationships

scraped_at: 2025-11-03T14:46:58.055146
---

[Skip to main content](https://docs.kalshi.com/websockets/multivariate-lookups#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

Websockets

Multivariate Lookups

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Messages

Multivariate Lookup

    {  "type": "multivariate_lookup",  "sid": 13,  "msg": {    "collection_ticker": "KXOSCARWINNERS-25",    "event_ticker": "KXOSCARWINNERS-25C0CE5",    "market_ticker": "KXOSCARWINNERS-25C0CE5-36353",    "selected_markets": [      {        "event_ticker": "KXOSCARACTO-25",        "market_ticker": "KXOSCARACTO-25-AB",        "side": "yes"      },      {        "event_ticker": "KXOSCARACTR-25",        "market_ticker": "KXOSCARACTR-25-DM",        "side": "yes"      }    ]  }}

WSS

wss://api.elections.kalshi.com

multivariate

Messages

Multivariate Lookup

    {  "type": "multivariate_lookup",  "sid": 13,  "msg": {    "collection_ticker": "KXOSCARWINNERS-25",    "event_ticker": "KXOSCARWINNERS-25C0CE5",    "market_ticker": "KXOSCARWINNERS-25C0CE5-36353",    "selected_markets": [      {        "event_ticker": "KXOSCARACTO-25",        "market_ticker": "KXOSCARACTO-25-AB",        "side": "yes"      },      {        "event_ticker": "KXOSCARACTR-25",        "market_ticker": "KXOSCARACTR-25-DM",        "side": "yes"      }    ]  }}

Security Schemes

apiKey

type:apiKey

API key authentication required for WebSocket connections. The API key should be provided during the WebSocket handshake.

Receive

Multivariate Lookup

type:object

show 3 properties

Multivariate collection lookup notification

[Market & Event Lifecycle](https://docs.kalshi.com/websockets/market-&-event-lifecycle)
[Communications](https://docs.kalshi.com/websockets/communications)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.