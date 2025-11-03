---
url: https://docs.kalshi.com/api-reference/portfolio/reset-order-group
title: Reset Order Group - API Documentation
description:  Resets the order group's matched contracts counter to zero, allowing new orders to be placed again after the limit was hit.
scraped_at: 2025-11-03T14:46:28.646520
---

[Skip to main content](https://docs.kalshi.com/api-reference/portfolio/reset-order-group#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

portfolio

Reset Order Group

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Reset Order Group

cURL

Copy

Ask AI

    curl --request PUT \
      --url https://api.elections.kalshi.com/trade-api/v2/portfolio/order_groups/{order_group_id}/reset \
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

PUT

/

portfolio

/

order\_groups

/

{order\_group\_id}

/

reset

Try it

Reset Order Group

cURL

Copy

Ask AI

    curl --request PUT \
      --url https://api.elections.kalshi.com/trade-api/v2/portfolio/order_groups/{order_group_id}/reset \
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

[​](https://docs.kalshi.com/api-reference/portfolio/reset-order-group#authorization-kalshi-access-key)

KALSHI-ACCESS-KEY

string

header

required

Your API key ID

[​](https://docs.kalshi.com/api-reference/portfolio/reset-order-group#authorization-kalshi-access-signature)

KALSHI-ACCESS-SIGNATURE

string

header

required

RSA-PSS signature of the request

[​](https://docs.kalshi.com/api-reference/portfolio/reset-order-group#authorization-kalshi-access-timestamp)

KALSHI-ACCESS-TIMESTAMP

string

header

required

Request timestamp in milliseconds

#### Path Parameters

[​](https://docs.kalshi.com/api-reference/portfolio/reset-order-group#parameter-order-group-id)

order\_group\_id

string

required

Order group ID

#### Response

200

application/json

Order group reset successfully

An empty response body

[Delete Order Group](https://docs.kalshi.com/api-reference/portfolio/delete-order-group)
[Get Orders](https://docs.kalshi.com/api-reference/portfolio/get-orders)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.