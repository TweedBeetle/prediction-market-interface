---
url: https://docs.kalshi.com/websockets/connection-keep-alive
title: Connection Keep-Alive - API Documentation
description: WebSocket control frames for connection management.

Kalshi sends Ping frames (`0x9`) every 10 seconds with body `heartbeat` to maintain the connection.
Clients should respond with Pong frames (`0xA`). Clients may also send Ping frames to which Kalshi will respond with Pong.

scraped_at: 2025-11-03T14:46:58.064415
---

[Skip to main content](https://docs.kalshi.com/websockets/connection-keep-alive#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

Websockets

Connection Keep-Alive

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Messages

Ping

    ""

Pong

    ""

Ping

    "heartbeat"

Pong

    ""

WSS

wss://api.elections.kalshi.com

Messages

Ping

    ""

Pong

    ""

Ping

    "heartbeat"

Pong

    ""

Security Schemes

apiKey

type:apiKey

API key authentication required for WebSocket connections. The API key should be provided during the WebSocket handshake.

Send

Ping

type:string

Client sends Ping frame (0x9) to elicit Pong from Kalshi

Pong

type:string

Client replies to Ping with Pong Frame (0xA)

Receive

Ping

type:string

Kalshi sends Ping (0x9) with body 'heartbeat' to elicit Pong from client

Pong

type:string

Kalshi responds to client Ping with Pong frame (0xA)

[WebSocket Connection](https://docs.kalshi.com/websockets/websocket-connection)
[Orderbook Updates](https://docs.kalshi.com/websockets/orderbook-updates)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.