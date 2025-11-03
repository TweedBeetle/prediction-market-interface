---
url: https://docs.kalshi.com/getting_started/subpenny_pricing
title: Subpenny Pricing - API Documentation
description: Understanding Kalshi subpenny pricing.
scraped_at: 2025-11-03T14:46:38.470607
---

[Skip to main content](https://docs.kalshi.com/getting_started/subpenny_pricing#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

Subpenny Pricing

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

On this page

*   [Format](https://docs.kalshi.com/getting_started/subpenny_pricing#format)
    
*   [Motivation](https://docs.kalshi.com/getting_started/subpenny_pricing#motivation)
    
*   [Status](https://docs.kalshi.com/getting_started/subpenny_pricing#status)
    

[​](https://docs.kalshi.com/getting_started/subpenny_pricing#format)

Format
------------------------------------------------------------------------------

Copy

Ask AI

    {
        "price": 12,              // legacy: cents
        "price_dollars": "0.1200" // new: fixed-point dollars
    }
    

Starting soon in the API, you will begin to see prices and money represented in 2 different formats: integer cents (legacy) and fixed-point dollars (new). A fixed-point dollar is a string bearing a fixed-point representation of money accurate to at least 4 decimal points.

[​](https://docs.kalshi.com/getting_started/subpenny_pricing#motivation)

Motivation
--------------------------------------------------------------------------------------

Subpenny pricing will allow for more accurate pricing and the tail end of markets where likelihood of a given event are close to 100% or 0%.

[​](https://docs.kalshi.com/getting_started/subpenny_pricing#status)

Status
------------------------------------------------------------------------------

Currently the minimum tick size on all markets is still 1 cent. Additionally, all prices and money fields will continue to be available in the legacy integer cents format. However, in the near future we will be introducing sub-penny pricing on orders. As such, we will eventually the legacy integer cents format. Therefore, please update systems to parse the new fixed-point dollars fields and prepare for subpenny precision.

[Orderbook Responses](https://docs.kalshi.com/getting_started/orderbook_responses)
[Kalshi Glossary](https://docs.kalshi.com/getting_started/terms)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.