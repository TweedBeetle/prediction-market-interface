---
url: https://docs.kalshi.com/api-reference/portfolio/get-settlements
title: Get Settlements - API Documentation
description:  Endpoint for getting the member's settlements historical track.
scraped_at: 2025-11-03T14:46:28.890006
---

[Skip to main content](https://docs.kalshi.com/api-reference/portfolio/get-settlements#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

portfolio

Get Settlements

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Get Settlements

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/portfolio/settlements \
      --header 'KALSHI-ACCESS-KEY: <api-key>' \
      --header 'KALSHI-ACCESS-SIGNATURE: <api-key>' \
      --header 'KALSHI-ACCESS-TIMESTAMP: <api-key>'

200

400

401

500

Copy

Ask AI

    {
      "settlements": [\
        {\
          "ticker": "<string>",\
          "market_result": "yes",\
          "yes_count": 123,\
          "yes_total_cost": 123,\
          "no_count": 123,\
          "no_total_cost": 123,\
          "revenue": 123,\
          "settled_time": "2023-11-07T05:31:56Z",\
          "value": 123\
        }\
      ],
      "cursor": "<string>"
    }

GET

/

portfolio

/

settlements

Try it

Get Settlements

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/portfolio/settlements \
      --header 'KALSHI-ACCESS-KEY: <api-key>' \
      --header 'KALSHI-ACCESS-SIGNATURE: <api-key>' \
      --header 'KALSHI-ACCESS-TIMESTAMP: <api-key>'

200

400

401

500

Copy

Ask AI

    {
      "settlements": [\
        {\
          "ticker": "<string>",\
          "market_result": "yes",\
          "yes_count": 123,\
          "yes_total_cost": 123,\
          "no_count": 123,\
          "no_total_cost": 123,\
          "revenue": 123,\
          "settled_time": "2023-11-07T05:31:56Z",\
          "value": 123\
        }\
      ],
      "cursor": "<string>"
    }

#### Authorizations

[​](https://docs.kalshi.com/api-reference/portfolio/get-settlements#authorization-kalshi-access-key)

KALSHI-ACCESS-KEY

string

header

required

Your API key ID

[​](https://docs.kalshi.com/api-reference/portfolio/get-settlements#authorization-kalshi-access-signature)

KALSHI-ACCESS-SIGNATURE

string

header

required

RSA-PSS signature of the request

[​](https://docs.kalshi.com/api-reference/portfolio/get-settlements#authorization-kalshi-access-timestamp)

KALSHI-ACCESS-TIMESTAMP

string

header

required

Request timestamp in milliseconds

#### Query Parameters

[​](https://docs.kalshi.com/api-reference/portfolio/get-settlements#parameter-limit)

limit

integer

default:100

Number of results per page. Defaults to 100. Maximum value is 200.

Required range: `1 <= x <= 200`

[​](https://docs.kalshi.com/api-reference/portfolio/get-settlements#parameter-cursor)

cursor

string

Pagination cursor. Use the cursor value returned from the previous response to get the next page of results. Leave empty for the first page.

[​](https://docs.kalshi.com/api-reference/portfolio/get-settlements#parameter-ticker)

ticker

string

Filter by market ticker

[​](https://docs.kalshi.com/api-reference/portfolio/get-settlements#parameter-event-ticker)

event\_ticker

string

Event ticker of desired positions. Multiple event tickers can be provided as a comma-separated list (maximum 10).

[​](https://docs.kalshi.com/api-reference/portfolio/get-settlements#parameter-min-ts)

min\_ts

integer

Filter items after this Unix timestamp

[​](https://docs.kalshi.com/api-reference/portfolio/get-settlements#parameter-max-ts)

max\_ts

integer

Filter items before this Unix timestamp

#### Response

200

application/json

Settlements retrieved successfully

[​](https://docs.kalshi.com/api-reference/portfolio/get-settlements#response-settlements)

settlements

object\[\]

required

Show child attributes

[​](https://docs.kalshi.com/api-reference/portfolio/get-settlements#response-cursor)

cursor

string

[Get Positions](https://docs.kalshi.com/api-reference/portfolio/get-positions)
[Get Total Resting Order Value](https://docs.kalshi.com/api-reference/portfolio/get-total-resting-order-value)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.