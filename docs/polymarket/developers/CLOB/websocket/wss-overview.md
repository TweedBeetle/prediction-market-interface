---
url: https://docs.polymarket.com/developers/CLOB/websocket/wss-overview
title: WSS Overview - Polymarket Documentation
description: Overview and general information about the Polymarket Websocket
scraped_at: 2025-11-03T15:04:03.681646
---

[Skip to main content](https://docs.polymarket.com/developers/CLOB/websocket/wss-overview#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

Ctrl K

Search...

Navigation

Websocket

WSS Overview

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

On this page

*   [Overview](https://docs.polymarket.com/developers/CLOB/websocket/wss-overview#overview)
    
*   [Subscription](https://docs.polymarket.com/developers/CLOB/websocket/wss-overview#subscription)
    

[​](https://docs.polymarket.com/developers/CLOB/websocket/wss-overview#overview)

Overview
--------------------------------------------------------------------------------------------

The Polymarket CLOB API provides websocket (wss) channels through which clients can get pushed updates. These endpoints allow clients to maintain almost real-time views of their orders, their trades and markets in general. There are two available channels `user` and `market`.

[​](https://docs.polymarket.com/developers/CLOB/websocket/wss-overview#subscription)

Subscription
----------------------------------------------------------------------------------------------------

To subscribe send a message including the following authentication and intent information upon opening the connection.

| Field | Type | Description |
| --- | --- | --- |
| auth | Auth | see next page for auth information |
| markets | string\[\] | array of markets (condition IDs) to receive events for (for `user` channel) |
| assets\_ids | string\[\] | array of asset ids (token IDs) to receive events for (for `market` channel) |
| type | string | id of channel to subscribe to (USER or MARKET) |

Where the `auth` field is of type `Auth` which has the form described in the WSS Authentication section below.

[Get Trades](https://docs.polymarket.com/developers/CLOB/trades/trades)
[WSS Quickstart](https://docs.polymarket.com/quickstart/websocket/WSS-Quickstart)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.