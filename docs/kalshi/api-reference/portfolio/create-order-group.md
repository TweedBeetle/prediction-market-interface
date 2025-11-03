---
url: https://docs.kalshi.com/api-reference/portfolio/create-order-group
title: Create Order Group - API Documentation
description:  Creates a new order group with a contracts limit. When the limit is hit, all orders in the group are cancelled and no new orders can be placed until reset.
scraped_at: 2025-11-03T14:46:25.112792
---

[Skip to main content](https://docs.kalshi.com/api-reference/portfolio/create-order-group#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

portfolio

Create Order Group

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Create Order Group

cURL

Copy

Ask AI

    curl --request POST \
      --url https://api.elections.kalshi.com/trade-api/v2/portfolio/order_groups/create \
      --header 'Content-Type: application/json' \
      --header 'KALSHI-ACCESS-KEY: <api-key>' \
      --header 'KALSHI-ACCESS-SIGNATURE: <api-key>' \
      --header 'KALSHI-ACCESS-TIMESTAMP: <api-key>' \
      --data '{
      "contracts_limit": 2
    }'

201

400

401

500

Copy

Ask AI

    {
      "order_group_id": "<string>"
    }

POST

/

portfolio

/

order\_groups

/

create

Try it

Create Order Group

cURL

Copy

Ask AI

    curl --request POST \
      --url https://api.elections.kalshi.com/trade-api/v2/portfolio/order_groups/create \
      --header 'Content-Type: application/json' \
      --header 'KALSHI-ACCESS-KEY: <api-key>' \
      --header 'KALSHI-ACCESS-SIGNATURE: <api-key>' \
      --header 'KALSHI-ACCESS-TIMESTAMP: <api-key>' \
      --data '{
      "contracts_limit": 2
    }'

201

400

401

500

Copy

Ask AI

    {
      "order_group_id": "<string>"
    }

#### Authorizations

[​](https://docs.kalshi.com/api-reference/portfolio/create-order-group#authorization-kalshi-access-key)

KALSHI-ACCESS-KEY

string

header

required

Your API key ID

[​](https://docs.kalshi.com/api-reference/portfolio/create-order-group#authorization-kalshi-access-signature)

KALSHI-ACCESS-SIGNATURE

string

header

required

RSA-PSS signature of the request

[​](https://docs.kalshi.com/api-reference/portfolio/create-order-group#authorization-kalshi-access-timestamp)

KALSHI-ACCESS-TIMESTAMP

string

header

required

Request timestamp in milliseconds

#### Body

application/json

[​](https://docs.kalshi.com/api-reference/portfolio/create-order-group#body-contracts-limit)

contracts\_limit

integer

required

Specifies the maximum number of contracts that can be matched within this group.

Required range: `x >= 1`

#### Response

201

application/json

Order group created successfully

[​](https://docs.kalshi.com/api-reference/portfolio/create-order-group#response-order-group-id)

order\_group\_id

string

The unique identifier for the created order group

[Get Order Groups](https://docs.kalshi.com/api-reference/portfolio/get-order-groups)
[Get Order Group](https://docs.kalshi.com/api-reference/portfolio/get-order-group)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.