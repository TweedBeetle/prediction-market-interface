---
url: https://docs.kalshi.com/api-reference/portfolio/batch-create-orders
title: Batch Create Orders - API Documentation
description:  Endpoint for submitting a batch of orders. Each order in the batch is counted against the total rate limit for order operations. Consequently, the size of the batch is capped by the current per-second rate-limit configuration applicable to the user. At the moment of writing, the limit is 20 orders per batch. Available to members with advanced access only.
scraped_at: 2025-11-03T14:46:24.654621
---

[Skip to main content](https://docs.kalshi.com/api-reference/portfolio/batch-create-orders#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

portfolio

Batch Create Orders

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Batch Create Orders

cURL

Copy

Ask AI

    curl --request POST \
      --url https://api.elections.kalshi.com/trade-api/v2/portfolio/orders/batched \
      --header 'Content-Type: application/json' \
      --header 'KALSHI-ACCESS-KEY: <api-key>' \
      --header 'KALSHI-ACCESS-SIGNATURE: <api-key>' \
      --header 'KALSHI-ACCESS-TIMESTAMP: <api-key>' \
      --data '{
      "orders": [\
        {\
          "ticker": "<string>",\
          "client_order_id": "<string>",\
          "side": "yes",\
          "action": "buy",\
          "count": 2,\
          "type": "limit",\
          "yes_price": 50,\
          "no_price": 50,\
          "yes_price_dollars": "0.5000",\
          "no_price_dollars": "0.5000",\
          "expiration_ts": 123,\
          "time_in_force": "FOK",\
          "buy_max_cost": 123,\
          "post_only": true,\
          "reduce_only": true,\
          "sell_position_floor": 123,\
          "self_trade_prevention_type": "taker_at_cross",\
          "order_group_id": "<string>",\
          "cancel_order_on_pause": true\
        }\
      ]
    }'

201

400

401

403

500

Copy

Ask AI

    {
      "orders": [\
        {\
          "client_order_id": "<string>",\
          "order": {\
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
          },\
          "error": {\
            "code": "<string>",\
            "message": "<string>",\
            "details": "<string>",\
            "service": "<string>"\
          }\
        }\
      ]
    }

POST

/

portfolio

/

orders

/

batched

Try it

Batch Create Orders

cURL

Copy

Ask AI

    curl --request POST \
      --url https://api.elections.kalshi.com/trade-api/v2/portfolio/orders/batched \
      --header 'Content-Type: application/json' \
      --header 'KALSHI-ACCESS-KEY: <api-key>' \
      --header 'KALSHI-ACCESS-SIGNATURE: <api-key>' \
      --header 'KALSHI-ACCESS-TIMESTAMP: <api-key>' \
      --data '{
      "orders": [\
        {\
          "ticker": "<string>",\
          "client_order_id": "<string>",\
          "side": "yes",\
          "action": "buy",\
          "count": 2,\
          "type": "limit",\
          "yes_price": 50,\
          "no_price": 50,\
          "yes_price_dollars": "0.5000",\
          "no_price_dollars": "0.5000",\
          "expiration_ts": 123,\
          "time_in_force": "FOK",\
          "buy_max_cost": 123,\
          "post_only": true,\
          "reduce_only": true,\
          "sell_position_floor": 123,\
          "self_trade_prevention_type": "taker_at_cross",\
          "order_group_id": "<string>",\
          "cancel_order_on_pause": true\
        }\
      ]
    }'

201

400

401

403

500

Copy

Ask AI

    {
      "orders": [\
        {\
          "client_order_id": "<string>",\
          "order": {\
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
          },\
          "error": {\
            "code": "<string>",\
            "message": "<string>",\
            "details": "<string>",\
            "service": "<string>"\
          }\
        }\
      ]
    }

#### Authorizations

[​](https://docs.kalshi.com/api-reference/portfolio/batch-create-orders#authorization-kalshi-access-key)

KALSHI-ACCESS-KEY

string

header

required

Your API key ID

[​](https://docs.kalshi.com/api-reference/portfolio/batch-create-orders#authorization-kalshi-access-signature)

KALSHI-ACCESS-SIGNATURE

string

header

required

RSA-PSS signature of the request

[​](https://docs.kalshi.com/api-reference/portfolio/batch-create-orders#authorization-kalshi-access-timestamp)

KALSHI-ACCESS-TIMESTAMP

string

header

required

Request timestamp in milliseconds

#### Body

application/json

[​](https://docs.kalshi.com/api-reference/portfolio/batch-create-orders#body-orders)

orders

object\[\]

required

Show child attributes

#### Response

201

application/json

Batch order creation completed

[​](https://docs.kalshi.com/api-reference/portfolio/batch-create-orders#response-orders)

orders

object\[\]

required

Show child attributes

[Create Order](https://docs.kalshi.com/api-reference/portfolio/create-order)
[Batch Cancel Orders](https://docs.kalshi.com/api-reference/portfolio/batch-cancel-orders)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.