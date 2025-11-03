---
url: https://docs.kalshi.com/websockets/market-&-event-lifecycle
title: Market & Event Lifecycle - API Documentation
description: Market state changes and event creation notifications.

**Requirements:**
- Market specification optional (omit to receive all events)
- Event creation notifications

**Use case:** Tracking market lifecycle including creation, de(activation), close date changes, determination, settlement

scraped_at: 2025-11-03T14:46:57.803969
---

[Skip to main content](https://docs.kalshi.com/websockets/market-&-event-lifecycle#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

Websockets

Market & Event Lifecycle

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Messages

Market Lifecycle V2

    {  "type": "market_lifecycle_v2",  "sid": 13,  "msg": {    "market_ticker": "INXD-23SEP14-B4487",    "event_type": "created",    "open_ts": 1694635200,    "close_ts": 1694721600,    "additional_metadata": {      "name": "S&P 500 daily return on Sep 14",      "title": "S&P 500 closes up by 0.02% or more",      "yes_sub_title": "S&P 500 closes up 0.02%+",      "no_sub_title": "S&P 500 closes up <0.02%",      "rules_primary": "The S&P 500 index level at 4:00 PM ET...",      "can_close_early": true,      "expected_expiration_ts": 1694721600,      "strike_type": "greater",      "floor_strike": "4487"    }  }}

Event Lifecycle

    {  "type": "event_lifecycle",  "sid": 5,  "msg": {    "event_ticker": "INXD-23SEP14",    "title": "INX title",    "sub_title": "INX subtitle",    "collateral_return_type": "DIRECNET",    "series_ticker": "INXD",    "strike_date": 1694721600  }}

WSS

wss://api.elections.kalshi.com

market\_lifecycle\_v2

Messages

Market Lifecycle V2

    {  "type": "market_lifecycle_v2",  "sid": 13,  "msg": {    "market_ticker": "INXD-23SEP14-B4487",    "event_type": "created",    "open_ts": 1694635200,    "close_ts": 1694721600,    "additional_metadata": {      "name": "S&P 500 daily return on Sep 14",      "title": "S&P 500 closes up by 0.02% or more",      "yes_sub_title": "S&P 500 closes up 0.02%+",      "no_sub_title": "S&P 500 closes up <0.02%",      "rules_primary": "The S&P 500 index level at 4:00 PM ET...",      "can_close_early": true,      "expected_expiration_ts": 1694721600,      "strike_type": "greater",      "floor_strike": "4487"    }  }}

Event Lifecycle

    {  "type": "event_lifecycle",  "sid": 5,  "msg": {    "event_ticker": "INXD-23SEP14",    "title": "INX title",    "sub_title": "INX subtitle",    "collateral_return_type": "DIRECNET",    "series_ticker": "INXD",    "strike_date": 1694721600  }}

Security Schemes

apiKey

type:apiKey

API key authentication required for WebSocket connections. The API key should be provided during the WebSocket handshake.

Receive

Market Lifecycle V2

type:object

show 3 properties

Market lifecycle events (created, activated, deactivated, close\_date\_updated, determined, settled)

Event Lifecycle

type:object

show 3 properties

Event creation notification

[Market Positions](https://docs.kalshi.com/websockets/market-positions)
[Multivariate Lookups](https://docs.kalshi.com/websockets/multivariate-lookups)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.