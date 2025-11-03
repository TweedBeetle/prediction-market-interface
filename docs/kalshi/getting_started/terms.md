---
url: https://docs.kalshi.com/getting_started/terms
title: Kalshi Glossary - API Documentation
description: Core terminology used in the Kalshi exchange
scraped_at: 2025-11-03T14:46:38.745136
---

[Skip to main content](https://docs.kalshi.com/getting_started/terms#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

Kalshi Glossary

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Here are some core terminologies used in Kalshi exchange: **Market:** A single binary market. This is a low level object which rarely will need to be exposed on its own to members. The usage of the term “market” here is consistent with how it’s used in the backend and API. **Event:** An event is a collection of markets and the basic unit that members should interact with on Kalshi. **Series:** A series is a collection of related events. The following should hold true for events that make up a series:

*   Each event should look at similar data for determination, but translated over another, disjoint time period.
*   Series should never have a logical outcome dependency between events.
*   Events in a series should have the same ticker prefix.

Please see the “Timeline and Payout” dropdown on a market’s page to find the Market, Event, and Series tickers. Note that the market ticker will depend on which market you are looking at on that page. For example, Trump and Harris are each their own market.

[Subpenny Pricing](https://docs.kalshi.com/getting_started/subpenny_pricing)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.