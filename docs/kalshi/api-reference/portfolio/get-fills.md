---
url: https://docs.kalshi.com/api-reference/portfolio/get-fills
title: Get Fills - API Documentation
description:  Endpoint for getting all fills for the member. A fill is when a trade you have is matched.
scraped_at: 2025-11-03T14:46:25.624762
---

[Skip to main content](https://docs.kalshi.com/api-reference/portfolio/get-fills#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

portfolio

Get Fills

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Get Fills

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/portfolio/fills \
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
      "fills": [\
        {\
          "fill_id": "<string>",\
          "trade_id": "<string>",\
          "order_id": "<string>",\
          "client_order_id": "<string>",\
          "ticker": "<string>",\
          "market_ticker": "<string>",\
          "side": "yes",\
          "action": "buy",\
          "count": 123,\
          "price": 123,\
          "yes_price": 123,\
          "no_price": 123,\
          "yes_price_fixed": "<string>",\
          "no_price_fixed": "<string>",\
          "is_taker": true,\
          "created_time": "2023-11-07T05:31:56Z",\
          "ts": 123\
        }\
      ],
      "cursor": "<string>"
    }

GET

/

portfolio

/

fills

Try it

Get Fills

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/portfolio/fills \
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
      "fills": [\
        {\
          "fill_id": "<string>",\
          "trade_id": "<string>",\
          "order_id": "<string>",\
          "client_order_id": "<string>",\
          "ticker": "<string>",\
          "market_ticker": "<string>",\
          "side": "yes",\
          "action": "buy",\
          "count": 123,\
          "price": 123,\
          "yes_price": 123,\
          "no_price": 123,\
          "yes_price_fixed": "<string>",\
          "no_price_fixed": "<string>",\
          "is_taker": true,\
          "created_time": "2023-11-07T05:31:56Z",\
          "ts": 123\
        }\
      ],
      "cursor": "<string>"
    }

#### Authorizations

[​](https://docs.kalshi.com/api-reference/portfolio/get-fills#authorization-kalshi-access-key)

KALSHI-ACCESS-KEY

string

header

required

Your API key ID

[​](https://docs.kalshi.com/api-reference/portfolio/get-fills#authorization-kalshi-access-signature)

KALSHI-ACCESS-SIGNATURE

string

header

required

RSA-PSS signature of the request

[​](https://docs.kalshi.com/api-reference/portfolio/get-fills#authorization-kalshi-access-timestamp)

KALSHI-ACCESS-TIMESTAMP

string

header

required

Request timestamp in milliseconds

#### Query Parameters

[​](https://docs.kalshi.com/api-reference/portfolio/get-fills#parameter-ticker)

ticker

string

Filter by market ticker

[​](https://docs.kalshi.com/api-reference/portfolio/get-fills#parameter-order-id)

order\_id

string

Filter by order ID

[​](https://docs.kalshi.com/api-reference/portfolio/get-fills#parameter-min-ts)

min\_ts

integer

Filter items after this Unix timestamp

[​](https://docs.kalshi.com/api-reference/portfolio/get-fills#parameter-max-ts)

max\_ts

integer

Filter items before this Unix timestamp

[​](https://docs.kalshi.com/api-reference/portfolio/get-fills#parameter-limit)

limit

integer

default:100

Number of results per page. Defaults to 100. Maximum value is 200.

Required range: `1 <= x <= 200`

[​](https://docs.kalshi.com/api-reference/portfolio/get-fills#parameter-cursor)

cursor

string

Pagination cursor. Use the cursor value returned from the previous response to get the next page of results. Leave empty for the first page.

#### Response

200

application/json

Fills retrieved successfully

[​](https://docs.kalshi.com/api-reference/portfolio/get-fills#response-fills)

fills

object\[\]

Show child attributes

[​](https://docs.kalshi.com/api-reference/portfolio/get-fills#response-cursor)

cursor

string

[Get Total Resting Order Value](https://docs.kalshi.com/api-reference/portfolio/get-total-resting-order-value)
[Get Order Groups](https://docs.kalshi.com/api-reference/portfolio/get-order-groups)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.