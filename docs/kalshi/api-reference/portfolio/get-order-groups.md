---
url: https://docs.kalshi.com/api-reference/portfolio/get-order-groups
title: Get Order Groups - API Documentation
description:  Retrieves all order groups for the authenticated user.
scraped_at: 2025-11-03T14:46:28.933927
---

[Skip to main content](https://docs.kalshi.com/api-reference/portfolio/get-order-groups#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

portfolio

Get Order Groups

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Get Order Groups

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/portfolio/order_groups \
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
      "order_groups": [\
        {\
          "id": "<string>",\
          "is_auto_cancel_enabled": true\
        }\
      ],
      "cursor": "<string>"
    }

GET

/

portfolio

/

order\_groups

Try it

Get Order Groups

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/portfolio/order_groups \
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
      "order_groups": [\
        {\
          "id": "<string>",\
          "is_auto_cancel_enabled": true\
        }\
      ],
      "cursor": "<string>"
    }

#### Authorizations

[​](https://docs.kalshi.com/api-reference/portfolio/get-order-groups#authorization-kalshi-access-key)

KALSHI-ACCESS-KEY

string

header

required

Your API key ID

[​](https://docs.kalshi.com/api-reference/portfolio/get-order-groups#authorization-kalshi-access-signature)

KALSHI-ACCESS-SIGNATURE

string

header

required

RSA-PSS signature of the request

[​](https://docs.kalshi.com/api-reference/portfolio/get-order-groups#authorization-kalshi-access-timestamp)

KALSHI-ACCESS-TIMESTAMP

string

header

required

Request timestamp in milliseconds

#### Query Parameters

[​](https://docs.kalshi.com/api-reference/portfolio/get-order-groups#parameter-status)

status

string

Filter by status. Possible values depend on the endpoint.

[​](https://docs.kalshi.com/api-reference/portfolio/get-order-groups#parameter-limit)

limit

integer

default:100

Number of results per page. Defaults to 100. Maximum value is 200.

Required range: `1 <= x <= 200`

[​](https://docs.kalshi.com/api-reference/portfolio/get-order-groups#parameter-cursor)

cursor

string

Pagination cursor. Use the cursor value returned from the previous response to get the next page of results. Leave empty for the first page.

#### Response

200

application/json

Order groups retrieved successfully

[​](https://docs.kalshi.com/api-reference/portfolio/get-order-groups#response-order-groups)

order\_groups

object\[\]

Show child attributes

[​](https://docs.kalshi.com/api-reference/portfolio/get-order-groups#response-cursor)

cursor

string

[Get Fills](https://docs.kalshi.com/api-reference/portfolio/get-fills)
[Create Order Group](https://docs.kalshi.com/api-reference/portfolio/create-order-group)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.