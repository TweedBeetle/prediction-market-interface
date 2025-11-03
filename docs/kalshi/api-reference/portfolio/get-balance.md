---
url: https://docs.kalshi.com/api-reference/portfolio/get-balance
title: Get Balance - API Documentation
description:  Endpoint for getting the balance and portfolio value of a member. Both values are returned in cents.
scraped_at: 2025-11-03T14:46:25.113317
---

[Skip to main content](https://docs.kalshi.com/api-reference/portfolio/get-balance#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

portfolio

Get Balance

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Get Balance

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/portfolio/balance \
      --header 'KALSHI-ACCESS-KEY: <api-key>' \
      --header 'KALSHI-ACCESS-SIGNATURE: <api-key>' \
      --header 'KALSHI-ACCESS-TIMESTAMP: <api-key>'

200

401

500

Copy

Ask AI

    {
      "balance": 123,
      "portfolio_value": 123,
      "updated_ts": 123
    }

GET

/

portfolio

/

balance

Try it

Get Balance

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/portfolio/balance \
      --header 'KALSHI-ACCESS-KEY: <api-key>' \
      --header 'KALSHI-ACCESS-SIGNATURE: <api-key>' \
      --header 'KALSHI-ACCESS-TIMESTAMP: <api-key>'

200

401

500

Copy

Ask AI

    {
      "balance": 123,
      "portfolio_value": 123,
      "updated_ts": 123
    }

#### Authorizations

[​](https://docs.kalshi.com/api-reference/portfolio/get-balance#authorization-kalshi-access-key)

KALSHI-ACCESS-KEY

string

header

required

Your API key ID

[​](https://docs.kalshi.com/api-reference/portfolio/get-balance#authorization-kalshi-access-signature)

KALSHI-ACCESS-SIGNATURE

string

header

required

RSA-PSS signature of the request

[​](https://docs.kalshi.com/api-reference/portfolio/get-balance#authorization-kalshi-access-timestamp)

KALSHI-ACCESS-TIMESTAMP

string

header

required

Request timestamp in milliseconds

#### Response

200

application/json

Balance retrieved successfully

[​](https://docs.kalshi.com/api-reference/portfolio/get-balance#response-balance)

balance

integer

required

Member's available balance in cents. This represents the amount available for trading.

[​](https://docs.kalshi.com/api-reference/portfolio/get-balance#response-portfolio-value)

portfolio\_value

integer

required

Member's portfolio value in cents. This is the current value of all positions held.

[​](https://docs.kalshi.com/api-reference/portfolio/get-balance#response-updated-ts)

updated\_ts

integer

required

Unix timestamp of the last update to the balance.

[Get User Data Timestamp](https://docs.kalshi.com/api-reference/exchange/get-user-data-timestamp)
[Get Positions](https://docs.kalshi.com/api-reference/portfolio/get-positions)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.