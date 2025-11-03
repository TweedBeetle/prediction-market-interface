---
url: https://docs.kalshi.com/api-reference/exchange/get-exchange-status
title: Get Exchange Status - API Documentation
description:  Endpoint for getting the exchange status.
scraped_at: 2025-11-03T14:46:15.758452
---

[Skip to main content](https://docs.kalshi.com/api-reference/exchange/get-exchange-status#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

exchange

Get Exchange Status

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Get Exchange Status

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/exchange/status

200

500

503

504

Copy

Ask AI

    {
      "exchange_active": true,
      "trading_active": true,
      "exchange_estimated_resume_time": "2023-11-07T05:31:56Z"
    }

GET

/

exchange

/

status

Try it

Get Exchange Status

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/exchange/status

200

500

503

504

Copy

Ask AI

    {
      "exchange_active": true,
      "trading_active": true,
      "exchange_estimated_resume_time": "2023-11-07T05:31:56Z"
    }

#### Response

200

application/json

Exchange status retrieved successfully

[​](https://docs.kalshi.com/api-reference/exchange/get-exchange-status#response-exchange-active)

exchange\_active

boolean

required

False if the core Kalshi exchange is no longer taking any state changes at all. This includes but is not limited to trading, new users, and transfers. True unless we are under maintenance.

[​](https://docs.kalshi.com/api-reference/exchange/get-exchange-status#response-trading-active)

trading\_active

boolean

required

True if we are currently permitting trading on the exchange. This is true during trading hours and false outside exchange hours. Kalshi reserves the right to pause at any time in case issues are detected.

[​](https://docs.kalshi.com/api-reference/exchange/get-exchange-status#response-exchange-estimated-resume-time)

exchange\_estimated\_resume\_time

string<date-time> | null

Estimated downtime for the current exchange maintenance window. However, this is not guaranteed and can be extended.

[Get Exchange Announcements](https://docs.kalshi.com/api-reference/exchange/get-exchange-announcements)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.