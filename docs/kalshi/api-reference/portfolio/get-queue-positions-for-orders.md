---
url: https://docs.kalshi.com/api-reference/portfolio/get-queue-positions-for-orders
title: Get Queue Positions for Orders - API Documentation
description:  Endpoint for getting queue positions for all resting orders. Queue position represents the number of contracts that need to be matched before an order receives a partial or full match, determined using price-time priority.
scraped_at: 2025-11-03T14:46:28.934399
---

[Skip to main content](https://docs.kalshi.com/api-reference/portfolio/get-queue-positions-for-orders#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

portfolio

Get Queue Positions for Orders

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Get Queue Positions for Orders

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/portfolio/orders/queue_positions \
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
      "queue_positions": [\
        {\
          "order_id": "<string>",\
          "market_ticker": "<string>",\
          "queue_position": 123\
        }\
      ]
    }

GET

/

portfolio

/

orders

/

queue\_positions

Try it

Get Queue Positions for Orders

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/portfolio/orders/queue_positions \
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
      "queue_positions": [\
        {\
          "order_id": "<string>",\
          "market_ticker": "<string>",\
          "queue_position": 123\
        }\
      ]
    }

#### Authorizations

[​](https://docs.kalshi.com/api-reference/portfolio/get-queue-positions-for-orders#authorization-kalshi-access-key)

KALSHI-ACCESS-KEY

string

header

required

Your API key ID

[​](https://docs.kalshi.com/api-reference/portfolio/get-queue-positions-for-orders#authorization-kalshi-access-signature)

KALSHI-ACCESS-SIGNATURE

string

header

required

RSA-PSS signature of the request

[​](https://docs.kalshi.com/api-reference/portfolio/get-queue-positions-for-orders#authorization-kalshi-access-timestamp)

KALSHI-ACCESS-TIMESTAMP

string

header

required

Request timestamp in milliseconds

#### Query Parameters

[​](https://docs.kalshi.com/api-reference/portfolio/get-queue-positions-for-orders#parameter-market-tickers)

market\_tickers

string

Comma-separated list of market tickers to filter by

[​](https://docs.kalshi.com/api-reference/portfolio/get-queue-positions-for-orders#parameter-event-ticker)

event\_ticker

string

Event ticker to filter by

#### Response

200

application/json

Queue positions retrieved successfully

[​](https://docs.kalshi.com/api-reference/portfolio/get-queue-positions-for-orders#response-queue-positions)

queue\_positions

object\[\]

required

Queue positions for all matching orders

Show child attributes

[Batch Cancel Orders](https://docs.kalshi.com/api-reference/portfolio/batch-cancel-orders)
[Get Order](https://docs.kalshi.com/api-reference/portfolio/get-order)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.