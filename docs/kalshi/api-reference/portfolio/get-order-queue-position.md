---
url: https://docs.kalshi.com/api-reference/portfolio/get-order-queue-position
title: Get Order Queue Position - API Documentation
description:  Endpoint for getting an order's queue position in the order book. This represents the amount of orders that need to be matched before this order receives a partial or full match. Queue position is determined using a price-time priority.
scraped_at: 2025-11-03T14:46:28.663851
---

[Skip to main content](https://docs.kalshi.com/api-reference/portfolio/get-order-queue-position#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

portfolio

Get Order Queue Position

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Get Order Queue Position

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/portfolio/orders/{order_id}/queue_position \
      --header 'KALSHI-ACCESS-KEY: <api-key>' \
      --header 'KALSHI-ACCESS-SIGNATURE: <api-key>' \
      --header 'KALSHI-ACCESS-TIMESTAMP: <api-key>'

200

401

404

500

Copy

Ask AI

    {
      "queue_position": 123
    }

GET

/

portfolio

/

orders

/

{order\_id}

/

queue\_position

Try it

Get Order Queue Position

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/portfolio/orders/{order_id}/queue_position \
      --header 'KALSHI-ACCESS-KEY: <api-key>' \
      --header 'KALSHI-ACCESS-SIGNATURE: <api-key>' \
      --header 'KALSHI-ACCESS-TIMESTAMP: <api-key>'

200

401

404

500

Copy

Ask AI

    {
      "queue_position": 123
    }

#### Authorizations

[​](https://docs.kalshi.com/api-reference/portfolio/get-order-queue-position#authorization-kalshi-access-key)

KALSHI-ACCESS-KEY

string

header

required

Your API key ID

[​](https://docs.kalshi.com/api-reference/portfolio/get-order-queue-position#authorization-kalshi-access-signature)

KALSHI-ACCESS-SIGNATURE

string

header

required

RSA-PSS signature of the request

[​](https://docs.kalshi.com/api-reference/portfolio/get-order-queue-position#authorization-kalshi-access-timestamp)

KALSHI-ACCESS-TIMESTAMP

string

header

required

Request timestamp in milliseconds

#### Path Parameters

[​](https://docs.kalshi.com/api-reference/portfolio/get-order-queue-position#parameter-order-id)

order\_id

string

required

Order ID

#### Response

200

application/json

Queue position retrieved successfully

[​](https://docs.kalshi.com/api-reference/portfolio/get-order-queue-position#response-queue-position)

queue\_position

integer

required

The position of the order in the queue

[Decrease Order](https://docs.kalshi.com/api-reference/portfolio/decrease-order)
[Get API Keys](https://docs.kalshi.com/api-reference/api-keys/get-api-keys)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.