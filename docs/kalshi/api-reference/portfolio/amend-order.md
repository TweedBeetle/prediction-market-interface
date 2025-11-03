---
url: https://docs.kalshi.com/api-reference/portfolio/amend-order
title: Amend Order - API Documentation
description:  Endpoint for amending the max number of fillable contracts and/or price in an existing order. Max fillable contracts is `remaining_count` + `fill_count`.
scraped_at: 2025-11-03T14:46:23.070212
---

[Skip to main content](https://docs.kalshi.com/api-reference/portfolio/amend-order#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

portfolio

Amend Order

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Amend Order

cURL

Copy

Ask AI

    curl --request POST \
      --url https://api.elections.kalshi.com/trade-api/v2/portfolio/orders/{order_id}/amend \
      --header 'Content-Type: application/json' \
      --header 'KALSHI-ACCESS-KEY: <api-key>' \
      --header 'KALSHI-ACCESS-SIGNATURE: <api-key>' \
      --header 'KALSHI-ACCESS-TIMESTAMP: <api-key>' \
      --data '{
      "ticker": "<string>",
      "side": "yes",
      "action": "buy",
      "client_order_id": "<string>",
      "updated_client_order_id": "<string>",
      "yes_price": 50,
      "no_price": 50,
      "yes_price_dollars": "<string>",
      "no_price_dollars": "<string>",
      "count": 2
    }'

200

400

401

404

500

Copy

Ask AI

    {
      "old_order": {
        "order_id": "<string>",
        "user_id": "<string>",
        "client_order_id": "<string>",
        "ticker": "<string>",
        "side": "yes",
        "action": "buy",
        "type": "limit",
        "status": "resting",
        "yes_price": 123,
        "no_price": 123,
        "yes_price_dollars": "0.5000",
        "no_price_dollars": "0.5000",
        "fill_count": 123,
        "remaining_count": 123,
        "initial_count": 123,
        "taker_fees": 123,
        "maker_fees": 123,
        "taker_fill_cost": 123,
        "maker_fill_cost": 123,
        "taker_fill_cost_dollars": "<string>",
        "maker_fill_cost_dollars": "<string>",
        "queue_position": 123,
        "taker_fees_dollars": "<string>",
        "maker_fees_dollars": "<string>",
        "expiration_time": "2023-11-07T05:31:56Z",
        "created_time": "2023-11-07T05:31:56Z",
        "last_update_time": "2023-11-07T05:31:56Z",
        "self_trade_prevention_type": "taker_at_cross",
        "order_group_id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
        "cancel_order_on_pause": true
      },
      "order": {
        "order_id": "<string>",
        "user_id": "<string>",
        "client_order_id": "<string>",
        "ticker": "<string>",
        "side": "yes",
        "action": "buy",
        "type": "limit",
        "status": "resting",
        "yes_price": 123,
        "no_price": 123,
        "yes_price_dollars": "0.5000",
        "no_price_dollars": "0.5000",
        "fill_count": 123,
        "remaining_count": 123,
        "initial_count": 123,
        "taker_fees": 123,
        "maker_fees": 123,
        "taker_fill_cost": 123,
        "maker_fill_cost": 123,
        "taker_fill_cost_dollars": "<string>",
        "maker_fill_cost_dollars": "<string>",
        "queue_position": 123,
        "taker_fees_dollars": "<string>",
        "maker_fees_dollars": "<string>",
        "expiration_time": "2023-11-07T05:31:56Z",
        "created_time": "2023-11-07T05:31:56Z",
        "last_update_time": "2023-11-07T05:31:56Z",
        "self_trade_prevention_type": "taker_at_cross",
        "order_group_id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
        "cancel_order_on_pause": true
      }
    }

POST

/

portfolio

/

orders

/

{order\_id}

/

amend

Try it

Amend Order

cURL

Copy

Ask AI

    curl --request POST \
      --url https://api.elections.kalshi.com/trade-api/v2/portfolio/orders/{order_id}/amend \
      --header 'Content-Type: application/json' \
      --header 'KALSHI-ACCESS-KEY: <api-key>' \
      --header 'KALSHI-ACCESS-SIGNATURE: <api-key>' \
      --header 'KALSHI-ACCESS-TIMESTAMP: <api-key>' \
      --data '{
      "ticker": "<string>",
      "side": "yes",
      "action": "buy",
      "client_order_id": "<string>",
      "updated_client_order_id": "<string>",
      "yes_price": 50,
      "no_price": 50,
      "yes_price_dollars": "<string>",
      "no_price_dollars": "<string>",
      "count": 2
    }'

200

400

401

404

500

Copy

Ask AI

    {
      "old_order": {
        "order_id": "<string>",
        "user_id": "<string>",
        "client_order_id": "<string>",
        "ticker": "<string>",
        "side": "yes",
        "action": "buy",
        "type": "limit",
        "status": "resting",
        "yes_price": 123,
        "no_price": 123,
        "yes_price_dollars": "0.5000",
        "no_price_dollars": "0.5000",
        "fill_count": 123,
        "remaining_count": 123,
        "initial_count": 123,
        "taker_fees": 123,
        "maker_fees": 123,
        "taker_fill_cost": 123,
        "maker_fill_cost": 123,
        "taker_fill_cost_dollars": "<string>",
        "maker_fill_cost_dollars": "<string>",
        "queue_position": 123,
        "taker_fees_dollars": "<string>",
        "maker_fees_dollars": "<string>",
        "expiration_time": "2023-11-07T05:31:56Z",
        "created_time": "2023-11-07T05:31:56Z",
        "last_update_time": "2023-11-07T05:31:56Z",
        "self_trade_prevention_type": "taker_at_cross",
        "order_group_id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
        "cancel_order_on_pause": true
      },
      "order": {
        "order_id": "<string>",
        "user_id": "<string>",
        "client_order_id": "<string>",
        "ticker": "<string>",
        "side": "yes",
        "action": "buy",
        "type": "limit",
        "status": "resting",
        "yes_price": 123,
        "no_price": 123,
        "yes_price_dollars": "0.5000",
        "no_price_dollars": "0.5000",
        "fill_count": 123,
        "remaining_count": 123,
        "initial_count": 123,
        "taker_fees": 123,
        "maker_fees": 123,
        "taker_fill_cost": 123,
        "maker_fill_cost": 123,
        "taker_fill_cost_dollars": "<string>",
        "maker_fill_cost_dollars": "<string>",
        "queue_position": 123,
        "taker_fees_dollars": "<string>",
        "maker_fees_dollars": "<string>",
        "expiration_time": "2023-11-07T05:31:56Z",
        "created_time": "2023-11-07T05:31:56Z",
        "last_update_time": "2023-11-07T05:31:56Z",
        "self_trade_prevention_type": "taker_at_cross",
        "order_group_id": "3c90c3cc-0d44-4b50-8888-8dd25736052a",
        "cancel_order_on_pause": true
      }
    }

#### Authorizations

[​](https://docs.kalshi.com/api-reference/portfolio/amend-order#authorization-kalshi-access-key)

KALSHI-ACCESS-KEY

string

header

required

Your API key ID

[​](https://docs.kalshi.com/api-reference/portfolio/amend-order#authorization-kalshi-access-signature)

KALSHI-ACCESS-SIGNATURE

string

header

required

RSA-PSS signature of the request

[​](https://docs.kalshi.com/api-reference/portfolio/amend-order#authorization-kalshi-access-timestamp)

KALSHI-ACCESS-TIMESTAMP

string

header

required

Request timestamp in milliseconds

#### Path Parameters

[​](https://docs.kalshi.com/api-reference/portfolio/amend-order#parameter-order-id)

order\_id

string

required

Order ID

#### Body

application/json

[​](https://docs.kalshi.com/api-reference/portfolio/amend-order#body-ticker)

ticker

string

required

Market ticker

[​](https://docs.kalshi.com/api-reference/portfolio/amend-order#body-side)

side

enum<string>

required

Side of the order

Available options:

`yes`,

`no`

[​](https://docs.kalshi.com/api-reference/portfolio/amend-order#body-action)

action

enum<string>

required

Action of the order

Available options:

`buy`,

`sell`

[​](https://docs.kalshi.com/api-reference/portfolio/amend-order#body-client-order-id)

client\_order\_id

string

required

The original client-specified order ID to be amended

[​](https://docs.kalshi.com/api-reference/portfolio/amend-order#body-updated-client-order-id)

updated\_client\_order\_id

string

required

The new client-specified order ID after amendment

[​](https://docs.kalshi.com/api-reference/portfolio/amend-order#body-yes-price)

yes\_price

number

Updated yes price for the order in cents

Required range: `1 <= x <= 99`

[​](https://docs.kalshi.com/api-reference/portfolio/amend-order#body-no-price)

no\_price

number

Updated no price for the order in cents

Required range: `1 <= x <= 99`

[​](https://docs.kalshi.com/api-reference/portfolio/amend-order#body-yes-price-dollars)

yes\_price\_dollars

string

Updated yes price for the order in fixed-point dollars. Exactly one of yes\_price, no\_price, yes\_price\_dollars, and no\_price\_dollars must be passed.

[​](https://docs.kalshi.com/api-reference/portfolio/amend-order#body-no-price-dollars)

no\_price\_dollars

string

Updated no price for the order in fixed-point dollars. Exactly one of yes\_price, no\_price, yes\_price\_dollars, and no\_price\_dollars must be passed.

[​](https://docs.kalshi.com/api-reference/portfolio/amend-order#body-count)

count

integer

Updated quantity for the order

Required range: `x >= 1`

#### Response

200

application/json

Order amended successfully

[​](https://docs.kalshi.com/api-reference/portfolio/amend-order#response-old-order)

old\_order

object

required

The order before amendment

Show child attributes

[​](https://docs.kalshi.com/api-reference/portfolio/amend-order#response-order)

order

object

required

The order after amendment

Show child attributes

[Cancel Order](https://docs.kalshi.com/api-reference/portfolio/cancel-order)
[Decrease Order](https://docs.kalshi.com/api-reference/portfolio/decrease-order)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.