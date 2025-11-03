---
url: https://docs.kalshi.com/api-reference/portfolio/get-order-group
title: Get Order Group - API Documentation
description:  Retrieves details for a single order group including all order IDs and auto-cancel status.
scraped_at: 2025-11-03T14:46:27.925461
---

[Skip to main content](https://docs.kalshi.com/api-reference/portfolio/get-order-group#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

portfolio

Get Order Group

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Get Order Group

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/portfolio/order_groups/{order_group_id} \
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
      "is_auto_cancel_enabled": true,
      "orders": [\
        "<string>"\
      ]
    }

GET

/

portfolio

/

order\_groups

/

{order\_group\_id}

Try it

Get Order Group

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/portfolio/order_groups/{order_group_id} \
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
      "is_auto_cancel_enabled": true,
      "orders": [\
        "<string>"\
      ]
    }

#### Authorizations

[​](https://docs.kalshi.com/api-reference/portfolio/get-order-group#authorization-kalshi-access-key)

KALSHI-ACCESS-KEY

string

header

required

Your API key ID

[​](https://docs.kalshi.com/api-reference/portfolio/get-order-group#authorization-kalshi-access-signature)

KALSHI-ACCESS-SIGNATURE

string

header

required

RSA-PSS signature of the request

[​](https://docs.kalshi.com/api-reference/portfolio/get-order-group#authorization-kalshi-access-timestamp)

KALSHI-ACCESS-TIMESTAMP

string

header

required

Request timestamp in milliseconds

#### Path Parameters

[​](https://docs.kalshi.com/api-reference/portfolio/get-order-group#parameter-order-group-id)

order\_group\_id

string

required

Order group ID

#### Response

200

application/json

Order group retrieved successfully

[​](https://docs.kalshi.com/api-reference/portfolio/get-order-group#response-is-auto-cancel-enabled)

is\_auto\_cancel\_enabled

boolean

Whether auto-cancel is enabled for this order group

[​](https://docs.kalshi.com/api-reference/portfolio/get-order-group#response-orders)

orders

string\[\]

List of order IDs that belong to this order group

[Create Order Group](https://docs.kalshi.com/api-reference/portfolio/create-order-group)
[Delete Order Group](https://docs.kalshi.com/api-reference/portfolio/delete-order-group)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.