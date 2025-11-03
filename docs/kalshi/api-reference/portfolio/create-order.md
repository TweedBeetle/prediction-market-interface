---
url: https://docs.kalshi.com/api-reference/portfolio/create-order
title: Create Order - API Documentation
description:  Endpoint for submitting orders in a market.
scraped_at: 2025-11-03T14:46:25.113100
---

[Skip to main content](https://docs.kalshi.com/api-reference/portfolio/create-order#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

portfolio

Create Order

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Create Order

cURL

Copy

Ask AI

    curl --request POST \
      --url https://api.elections.kalshi.com/trade-api/v2/portfolio/orders \
      --header 'Content-Type: application/json' \
      --header 'KALSHI-ACCESS-KEY: <api-key>' \
      --header 'KALSHI-ACCESS-SIGNATURE: <api-key>' \
      --header 'KALSHI-ACCESS-TIMESTAMP: <api-key>' \
      --data '{
      "ticker": "<string>",
      "client_order_id": "<string>",
      "side": "yes",
      "action": "buy",
      "count": 2,
      "type": "limit",
      "yes_price": 50,
      "no_price": 50,
      "yes_price_dollars": "0.5000",
      "no_price_dollars": "0.5000",
      "expiration_ts": 123,
      "time_in_force": "FOK",
      "buy_max_cost": 123,
      "post_only": true,
      "reduce_only": true,
      "sell_position_floor": 123,
      "self_trade_prevention_type": "taker_at_cross",
      "order_group_id": "<string>",
      "cancel_order_on_pause": true
    }'

201

400

401

409

429

500

Copy

Ask AI

    {
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

Try it

Create Order

cURL

Copy

Ask AI

    curl --request POST \
      --url https://api.elections.kalshi.com/trade-api/v2/portfolio/orders \
      --header 'Content-Type: application/json' \
      --header 'KALSHI-ACCESS-KEY: <api-key>' \
      --header 'KALSHI-ACCESS-SIGNATURE: <api-key>' \
      --header 'KALSHI-ACCESS-TIMESTAMP: <api-key>' \
      --data '{
      "ticker": "<string>",
      "client_order_id": "<string>",
      "side": "yes",
      "action": "buy",
      "count": 2,
      "type": "limit",
      "yes_price": 50,
      "no_price": 50,
      "yes_price_dollars": "0.5000",
      "no_price_dollars": "0.5000",
      "expiration_ts": 123,
      "time_in_force": "FOK",
      "buy_max_cost": 123,
      "post_only": true,
      "reduce_only": true,
      "sell_position_floor": 123,
      "self_trade_prevention_type": "taker_at_cross",
      "order_group_id": "<string>",
      "cancel_order_on_pause": true
    }'

201

400

401

409

429

500

Copy

Ask AI

    {
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

[​](https://docs.kalshi.com/api-reference/portfolio/create-order#authorization-kalshi-access-key)

KALSHI-ACCESS-KEY

string

header

required

Your API key ID

[​](https://docs.kalshi.com/api-reference/portfolio/create-order#authorization-kalshi-access-signature)

KALSHI-ACCESS-SIGNATURE

string

header

required

RSA-PSS signature of the request

[​](https://docs.kalshi.com/api-reference/portfolio/create-order#authorization-kalshi-access-timestamp)

KALSHI-ACCESS-TIMESTAMP

string

header

required

Request timestamp in milliseconds

#### Body

application/json

[​](https://docs.kalshi.com/api-reference/portfolio/create-order#body-ticker)

ticker

string

required

[​](https://docs.kalshi.com/api-reference/portfolio/create-order#body-side)

side

enum<string>

required

Available options:

`yes`,

`no`

[​](https://docs.kalshi.com/api-reference/portfolio/create-order#body-action)

action

enum<string>

required

Available options:

`buy`,

`sell`

[​](https://docs.kalshi.com/api-reference/portfolio/create-order#body-count)

count

integer

required

Required range: `x >= 1`

[​](https://docs.kalshi.com/api-reference/portfolio/create-order#body-client-order-id)

client\_order\_id

string

[​](https://docs.kalshi.com/api-reference/portfolio/create-order#body-type)

type

enum<string>

default:limit

Available options:

`limit`,

`market`

[​](https://docs.kalshi.com/api-reference/portfolio/create-order#body-yes-price)

yes\_price

number

Required range: `1 <= x <= 99`

[​](https://docs.kalshi.com/api-reference/portfolio/create-order#body-no-price)

no\_price

number

Required range: `1 <= x <= 99`

[​](https://docs.kalshi.com/api-reference/portfolio/create-order#body-yes-price-dollars)

yes\_price\_dollars

string

Submitting price of the Yes side in fixed-point dollars

Example:

`"0.5000"`

[​](https://docs.kalshi.com/api-reference/portfolio/create-order#body-no-price-dollars)

no\_price\_dollars

string

Submitting price of the No side in fixed-point dollars

Example:

`"0.5000"`

[​](https://docs.kalshi.com/api-reference/portfolio/create-order#body-expiration-ts)

expiration\_ts

integer

[​](https://docs.kalshi.com/api-reference/portfolio/create-order#body-time-in-force)

time\_in\_force

enum<string>

Available options:

`FOK`,

`GTC`,

`IOC`

[​](https://docs.kalshi.com/api-reference/portfolio/create-order#body-buy-max-cost)

buy\_max\_cost

integer

Maximum cost in cents. When specified, the order will automatically have Fill-or-Kill (FoK) behavior.

[​](https://docs.kalshi.com/api-reference/portfolio/create-order#body-post-only)

post\_only

boolean

[​](https://docs.kalshi.com/api-reference/portfolio/create-order#body-reduce-only)

reduce\_only

boolean

[​](https://docs.kalshi.com/api-reference/portfolio/create-order#body-sell-position-floor)

sell\_position\_floor

integer

Deprecated: Use reduce\_only instead. Only accepts value of 0.

[​](https://docs.kalshi.com/api-reference/portfolio/create-order#body-self-trade-prevention-type)

self\_trade\_prevention\_type

enum<string>

The self-trade prevention type for this order

Available options:

`taker_at_cross`,

`maker`

[​](https://docs.kalshi.com/api-reference/portfolio/create-order#body-order-group-id)

order\_group\_id

string

The order group this order is part of

[​](https://docs.kalshi.com/api-reference/portfolio/create-order#body-cancel-order-on-pause)

cancel\_order\_on\_pause

boolean

If this flag is set to true, the order will be canceled if the order is open and trading on the exchange is paused for any reason.

#### Response

201

application/json

Order created successfully

[​](https://docs.kalshi.com/api-reference/portfolio/create-order#response-order)

order

object

required

Show child attributes

[Get Orders](https://docs.kalshi.com/api-reference/portfolio/get-orders)
[Batch Create Orders](https://docs.kalshi.com/api-reference/portfolio/batch-create-orders)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.