---
url: https://docs.kalshi.com/api-reference/portfolio/delete-order-group
title: Delete Order Group - API Documentation
description:  Deletes an order group and cancels all orders within it. This permanently removes the group.
scraped_at: 2025-11-03T14:46:25.120777
---

[Skip to main content](https://docs.kalshi.com/api-reference/portfolio/delete-order-group#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

portfolio

Delete Order Group

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Delete Order Group

cURL

Copy

Ask AI

    curl --request DELETE \
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

    {}

DELETE

/

portfolio

/

order\_groups

/

{order\_group\_id}

Try it

Delete Order Group

cURL

Copy

Ask AI

    curl --request DELETE \
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

    {}

#### Authorizations

[​](https://docs.kalshi.com/api-reference/portfolio/delete-order-group#authorization-kalshi-access-key)

KALSHI-ACCESS-KEY

string

header

required

Your API key ID

[​](https://docs.kalshi.com/api-reference/portfolio/delete-order-group#authorization-kalshi-access-signature)

KALSHI-ACCESS-SIGNATURE

string

header

required

RSA-PSS signature of the request

[​](https://docs.kalshi.com/api-reference/portfolio/delete-order-group#authorization-kalshi-access-timestamp)

KALSHI-ACCESS-TIMESTAMP

string

header

required

Request timestamp in milliseconds

#### Path Parameters

[​](https://docs.kalshi.com/api-reference/portfolio/delete-order-group#parameter-order-group-id)

order\_group\_id

string

required

Order group ID

#### Response

200

application/json

Order group deleted successfully

An empty response body

[Get Order Group](https://docs.kalshi.com/api-reference/portfolio/get-order-group)
[Reset Order Group](https://docs.kalshi.com/api-reference/portfolio/reset-order-group)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.