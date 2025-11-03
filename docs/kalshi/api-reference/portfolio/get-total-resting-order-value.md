---
url: https://docs.kalshi.com/api-reference/portfolio/get-total-resting-order-value
title: Get Total Resting Order Value - API Documentation
description:  Endpoint for getting the total value, in cents, of resting orders. This endpoint is only intended for use by FCM members (rare). Note: If you're uncertain about this endpoint, it likely does not apply to you.
scraped_at: 2025-11-03T14:46:28.933664
---

[Skip to main content](https://docs.kalshi.com/api-reference/portfolio/get-total-resting-order-value#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

portfolio

Get Total Resting Order Value

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Get Total Resting Order Value

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/portfolio/summary/total_resting_order_value \
      --header 'KALSHI-ACCESS-KEY: <api-key>' \
      --header 'KALSHI-ACCESS-SIGNATURE: <api-key>' \
      --header 'KALSHI-ACCESS-TIMESTAMP: <api-key>'

200

401

500

Copy

Ask AI

    {
      "total_resting_order_value": 123
    }

GET

/

portfolio

/

summary

/

total\_resting\_order\_value

Try it

Get Total Resting Order Value

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/portfolio/summary/total_resting_order_value \
      --header 'KALSHI-ACCESS-KEY: <api-key>' \
      --header 'KALSHI-ACCESS-SIGNATURE: <api-key>' \
      --header 'KALSHI-ACCESS-TIMESTAMP: <api-key>'

200

401

500

Copy

Ask AI

    {
      "total_resting_order_value": 123
    }

#### Authorizations

[​](https://docs.kalshi.com/api-reference/portfolio/get-total-resting-order-value#authorization-kalshi-access-key)

KALSHI-ACCESS-KEY

string

header

required

Your API key ID

[​](https://docs.kalshi.com/api-reference/portfolio/get-total-resting-order-value#authorization-kalshi-access-signature)

KALSHI-ACCESS-SIGNATURE

string

header

required

RSA-PSS signature of the request

[​](https://docs.kalshi.com/api-reference/portfolio/get-total-resting-order-value#authorization-kalshi-access-timestamp)

KALSHI-ACCESS-TIMESTAMP

string

header

required

Request timestamp in milliseconds

#### Response

200

application/json

Total resting order value retrieved successfully

[​](https://docs.kalshi.com/api-reference/portfolio/get-total-resting-order-value#response-total-resting-order-value)

total\_resting\_order\_value

integer

required

Total value of resting orders in cents

[Get Settlements](https://docs.kalshi.com/api-reference/portfolio/get-settlements)
[Get Fills](https://docs.kalshi.com/api-reference/portfolio/get-fills)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.