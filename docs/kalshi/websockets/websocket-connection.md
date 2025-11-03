---
url: https://docs.kalshi.com/websockets/websocket-connection
title: WebSocket Connection - API Documentation
description: Main WebSocket connection endpoint. All communication happens through this single connection.
Use the subscribe command to subscribe to specific data channels. For more information, see the [Getting Started](https://docs.kalshi.com/getting_started/quick_start_websockets) guide.

scraped_at: 2025-11-03T14:46:58.057118
---

[Skip to main content](https://docs.kalshi.com/websockets/websocket-connection#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

Websockets

WebSocket Connection

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Messages

Subscribe Command

    {  "id": 1,  "cmd": "subscribe",  "params": {    "channels": [      "orderbook_delta"    ],    "market_ticker": "CPI-22DEC-TN0.1"  }}

Unsubscribe Command

    {  "id": 124,  "cmd": "unsubscribe",  "params": {    "sids": [      1,      2    ]  }}

List Subscriptions Command

    {  "id": 3,  "cmd": "list_subscriptions"}

Update Subscription - Add Markets

    {  "id": 124,  "cmd": "update_subscription",  "params": {    "sids": [      456    ],    "market_tickers": [      "NEW-MARKET-1",      "NEW-MARKET-2"    ],    "action": "add_markets"  }}

Update Subscription - Delete Markets

    {  "id": 125,  "cmd": "update_subscription",  "params": {    "sids": [      456    ],    "market_tickers": [      "MARKET-TO-REMOVE-1",      "MARKET-TO-REMOVE-2"    ],    "action": "delete_markets"  }}

Update Subscription - Single SID Format

    {  "id": 126,  "cmd": "update_subscription",  "params": {    "sid": 456,    "market_tickers": [      "NEW-MARKET-3",      "NEW-MARKET-4"    ],    "action": "add_markets"  }}

Subscribed Response

    {  "id": 1,  "type": "subscribed",  "msg": {    "channel": "orderbook_delta",    "sid": 1  }}

Unsubscribed Response

    {  "sid": 2,  "type": "unsubscribed"}

OK Response

    {  "id": 123,  "sid": 456,  "seq": 222,  "type": "ok",  "market_tickers": [    "MARKET-1",    "MARKET-2",    "MARKET-3"  ]}

List Subscriptions Response

    {  "id": 3,  "type": "ok",  "subscriptions": [    {      "channel": "orderbook_delta",      "sid": 1    },    {      "channel": "ticker",      "sid": 2    },    {      "channel": "fill",      "sid": 3    }  ]}

Error Response

    {  "id": 123,  "type": "error",  "msg": {    "code": 6,    "msg": "Already subscribed"  }}

WSS

wss://api.elections.kalshi.com

Messages

Subscribe Command

    {  "id": 1,  "cmd": "subscribe",  "params": {    "channels": [      "orderbook_delta"    ],    "market_ticker": "CPI-22DEC-TN0.1"  }}

Unsubscribe Command

    {  "id": 124,  "cmd": "unsubscribe",  "params": {    "sids": [      1,      2    ]  }}

List Subscriptions Command

    {  "id": 3,  "cmd": "list_subscriptions"}

Update Subscription - Add Markets

    {  "id": 124,  "cmd": "update_subscription",  "params": {    "sids": [      456    ],    "market_tickers": [      "NEW-MARKET-1",      "NEW-MARKET-2"    ],    "action": "add_markets"  }}

Update Subscription - Delete Markets

    {  "id": 125,  "cmd": "update_subscription",  "params": {    "sids": [      456    ],    "market_tickers": [      "MARKET-TO-REMOVE-1",      "MARKET-TO-REMOVE-2"    ],    "action": "delete_markets"  }}

Update Subscription - Single SID Format

    {  "id": 126,  "cmd": "update_subscription",  "params": {    "sid": 456,    "market_tickers": [      "NEW-MARKET-3",      "NEW-MARKET-4"    ],    "action": "add_markets"  }}

Subscribed Response

    {  "id": 1,  "type": "subscribed",  "msg": {    "channel": "orderbook_delta",    "sid": 1  }}

Unsubscribed Response

    {  "sid": 2,  "type": "unsubscribed"}

OK Response

    {  "id": 123,  "sid": 456,  "seq": 222,  "type": "ok",  "market_tickers": [    "MARKET-1",    "MARKET-2",    "MARKET-3"  ]}

List Subscriptions Response

    {  "id": 3,  "type": "ok",  "subscriptions": [    {      "channel": "orderbook_delta",      "sid": 1    },    {      "channel": "ticker",      "sid": 2    },    {      "channel": "fill",      "sid": 3    }  ]}

Error Response

    {  "id": 123,  "type": "error",  "msg": {    "code": 6,    "msg": "Already subscribed"  }}

Security Schemes

apiKey

type:apiKey

API key authentication required for WebSocket connections. The API key should be provided during the WebSocket handshake.

Bindings

method

type:string

GET

Send

Subscribe Command

type:object

show 3 properties

Subscribe to one or more channels

Unsubscribe Command

type:object

show 3 properties

Cancel one or more subscriptions

List Subscriptions Command

type:object

show 2 properties

List all active subscriptions

Update Subscription - Add Markets

type:object

show 3 properties

Add markets to an existing subscription

Update Subscription - Delete Markets

type:object

show 3 properties

Remove markets from an existing subscription

Update Subscription - Single SID Format

type:object

show 3 properties

Update subscription using sid parameter instead of sids array

Receive

Subscribed Response

type:object

show 3 properties

Confirmation that subscription was successful

Unsubscribed Response

type:object

show 2 properties

Confirmation that unsubscription was successful

OK Response

type:object

show 5 properties

Successful update operation response

List Subscriptions Response

type:object

show 3 properties

Response containing all active subscriptions

Error Response

type:object

show 3 properties

Error response for failed operations

[Connection Keep-Alive](https://docs.kalshi.com/websockets/connection-keep-alive)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.