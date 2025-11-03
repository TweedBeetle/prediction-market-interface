---
url: https://docs.kalshi.com/api-reference/portfolio/get-orders
title: Get Orders - API Documentation
description: Restricts the response to orders that have a certain status: resting, canceled, or executed.
scraped_at: 2025-11-03T14:46:27.904296
---

[Skip to main content](https://docs.kalshi.com/api-reference/portfolio/get-orders#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

portfolio

Get Orders

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Get Orders

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/portfolio/orders \
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
      "orders": [\
        {\
          "order_id": "<string>",\
          "user_id": "<string>",\
          "client_order_id": "<string>",\
          "ticker": "<string>",\
          "side": "yes",\
          "action": "buy",\
          "type": "limit",\
          "status": "resting",\
          "yes_price": 123,\
          "no_price": 123,\
          "yes_price_dollars": "0.5000",\
          "no_price_dollars": "0.5000",\
          "fill_count": 123,\
          "remaining_count": 123,\
          "initial_count": 123,\
          "taker_fees": 123,\
          "maker_fees": 123,\
          "taker_fill_cost": 123,\
          "maker_fill_cost": 123,\
          "taker_fill_cost_dollars": "<string>",\
          "maker_fill_cost_dollars": "<string>",\
          "queue_position": 123,\
          "taker_fees_dollars": "<string>",\
          "maker_fees_dollars": "<string>",\
          "expiration_time": "2023-11-07T05:31:56Z",\
          "created_time": "2023-11-07T05:31:56Z",\
          "last_update_time": "2023-11-07T05:31:56Z",\
          "self_trade_prevention_type": "taker_at_cross",\
          "order_group_id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",\
          "cancel_order_on_pause": true\
        }\
      ],
      "cursor": "<string>"
    }

GET

/

portfolio

/

orders

Try it

Get Orders

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/portfolio/orders \
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
      "orders": [\
        {\
          "order_id": "<string>",\
          "user_id": "<string>",\
          "client_order_id": "<string>",\
          "ticker": "<string>",\
          "side": "yes",\
          "action": "buy",\
          "type": "limit",\
          "status": "resting",\
          "yes_price": 123,\
          "no_price": 123,\
          "yes_price_dollars": "0.5000",\
          "no_price_dollars": "0.5000",\
          "fill_count": 123,\
          "remaining_count": 123,\
          "initial_count": 123,\
          "taker_fees": 123,\
          "maker_fees": 123,\
          "taker_fill_cost": 123,\
          "maker_fill_cost": 123,\
          "taker_fill_cost_dollars": "<string>",\
          "maker_fill_cost_dollars": "<string>",\
          "queue_position": 123,\
          "taker_fees_dollars": "<string>",\
          "maker_fees_dollars": "<string>",\
          "expiration_time": "2023-11-07T05:31:56Z",\
          "created_time": "2023-11-07T05:31:56Z",\
          "last_update_time": "2023-11-07T05:31:56Z",\
          "self_trade_prevention_type": "taker_at_cross",\
          "order_group_id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",\
          "cancel_order_on_pause": true\
        }\
      ],
      "cursor": "<string>"
    }

#### Authorizations

[​](https://docs.kalshi.com/api-reference/portfolio/get-orders#authorization-kalshi-access-key)

KALSHI-ACCESS-KEY

string

header

required

Your API key ID

[​](https://docs.kalshi.com/api-reference/portfolio/get-orders#authorization-kalshi-access-signature)

KALSHI-ACCESS-SIGNATURE

string

header

required

RSA-PSS signature of the request

[​](https://docs.kalshi.com/api-reference/portfolio/get-orders#authorization-kalshi-access-timestamp)

KALSHI-ACCESS-TIMESTAMP

string

header

required

Request timestamp in milliseconds

#### Query Parameters

[​](https://docs.kalshi.com/api-reference/portfolio/get-orders#parameter-ticker)

ticker

string

Filter by market ticker

[​](https://docs.kalshi.com/api-reference/portfolio/get-orders#parameter-event-ticker)

event\_ticker

string

Event ticker of desired positions. Multiple event tickers can be provided as a comma-separated list (maximum 10).

[​](https://docs.kalshi.com/api-reference/portfolio/get-orders#parameter-min-ts)

min\_ts

integer

Filter items after this Unix timestamp

[​](https://docs.kalshi.com/api-reference/portfolio/get-orders#parameter-max-ts)

max\_ts

integer

Filter items before this Unix timestamp

[​](https://docs.kalshi.com/api-reference/portfolio/get-orders#parameter-status)

status

string

Filter by status. Possible values depend on the endpoint.

[​](https://docs.kalshi.com/api-reference/portfolio/get-orders#parameter-limit)

limit

integer

default:100

Number of results per page. Defaults to 100. Maximum value is 200.

Required range: `1 <= x <= 200`

[​](https://docs.kalshi.com/api-reference/portfolio/get-orders#parameter-cursor)

cursor

string

Pagination cursor. Use the cursor value returned from the previous response to get the next page of results. Leave empty for the first page.

#### Response

200

application/json

Orders retrieved successfully

[​](https://docs.kalshi.com/api-reference/portfolio/get-orders#response-orders)

orders

object\[\]

required

Show child attributes

[​](https://docs.kalshi.com/api-reference/portfolio/get-orders#response-cursor)

cursor

string

required

[Reset Order Group](https://docs.kalshi.com/api-reference/portfolio/reset-order-group)
[Create Order](https://docs.kalshi.com/api-reference/portfolio/create-order)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.