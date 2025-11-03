---
url: https://docs.polymarket.com/api-reference/core/get-total-value-of-a-users-positions
title: Get total value of a user's positions - Polymarket Documentation
scraped_at: 2025-11-03T15:03:39.728902
---

[Skip to main content](https://docs.polymarket.com/api-reference/core/get-total-value-of-a-users-positions#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

Ctrl K

Search...

Navigation

Core

Get total value of a user's positions

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

Get total value of a user's positions

cURL

Copy

Ask AI

    curl --request GET \
      --url https://data-api.polymarket.com/value

200

400

500

Copy

Ask AI

    [\
      {\
        "user": "0x56687bf447db6ffa42ffe2204a05edaa20f55839",\
        "value": 123\
      }\
    ]

GET

/

value

Try it

Get total value of a user's positions

cURL

Copy

Ask AI

    curl --request GET \
      --url https://data-api.polymarket.com/value

200

400

500

Copy

Ask AI

    [\
      {\
        "user": "0x56687bf447db6ffa42ffe2204a05edaa20f55839",\
        "value": 123\
      }\
    ]

#### Query Parameters

[​](https://docs.polymarket.com/api-reference/core/get-total-value-of-a-users-positions#parameter-user)

user

string

required

User Profile Address (0x-prefixed, 40 hex chars)

Example:

`"0x56687bf447db6ffa42ffe2204a05edaa20f55839"`

[​](https://docs.polymarket.com/api-reference/core/get-total-value-of-a-users-positions#parameter-market)

market

string\[\]

0x-prefixed 64-hex string

#### Response

200

application/json

Success

[​](https://docs.polymarket.com/api-reference/core/get-total-value-of-a-users-positions#response-user)

user

string

User Profile Address (0x-prefixed, 40 hex chars)

Example:

`"0x56687bf447db6ffa42ffe2204a05edaa20f55839"`

[​](https://docs.polymarket.com/api-reference/core/get-total-value-of-a-users-positions#response-value)

value

number

[Get top holders for markets](https://docs.polymarket.com/api-reference/core/get-top-holders-for-markets)
[Get closed positions for a user](https://docs.polymarket.com/api-reference/core/get-closed-positions-for-a-user)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.