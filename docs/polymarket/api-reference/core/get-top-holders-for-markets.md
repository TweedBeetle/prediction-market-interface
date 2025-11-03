---
url: https://docs.polymarket.com/api-reference/core/get-top-holders-for-markets
title: Get top holders for markets - Polymarket Documentation
scraped_at: 2025-11-03T15:03:39.234029
---

[Skip to main content](https://docs.polymarket.com/api-reference/core/get-top-holders-for-markets#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

Ctrl K

Search...

Navigation

Core

Get top holders for markets

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

Get top holders for markets

cURL

Copy

Ask AI

    curl --request GET \
      --url https://data-api.polymarket.com/holders

200

400

401

500

Copy

Ask AI

    [\
      {\
        "token": "<string>",\
        "holders": [\
          {\
            "proxyWallet": "0x56687bf447db6ffa42ffe2204a05edaa20f55839",\
            "bio": "<string>",\
            "asset": "<string>",\
            "pseudonym": "<string>",\
            "amount": 123,\
            "displayUsernamePublic": true,\
            "outcomeIndex": 123,\
            "name": "<string>",\
            "profileImage": "<string>",\
            "profileImageOptimized": "<string>"\
          }\
        ]\
      }\
    ]

GET

/

holders

Try it

Get top holders for markets

cURL

Copy

Ask AI

    curl --request GET \
      --url https://data-api.polymarket.com/holders

200

400

401

500

Copy

Ask AI

    [\
      {\
        "token": "<string>",\
        "holders": [\
          {\
            "proxyWallet": "0x56687bf447db6ffa42ffe2204a05edaa20f55839",\
            "bio": "<string>",\
            "asset": "<string>",\
            "pseudonym": "<string>",\
            "amount": 123,\
            "displayUsernamePublic": true,\
            "outcomeIndex": 123,\
            "name": "<string>",\
            "profileImage": "<string>",\
            "profileImageOptimized": "<string>"\
          }\
        ]\
      }\
    ]

#### Query Parameters

[​](https://docs.polymarket.com/api-reference/core/get-top-holders-for-markets#parameter-limit)

limit

integer

default:100

Required range: `0 <= x <= 500`

[​](https://docs.polymarket.com/api-reference/core/get-top-holders-for-markets#parameter-market)

market

string\[\]

required

Comma-separated list of condition IDs.

0x-prefixed 64-hex string

[​](https://docs.polymarket.com/api-reference/core/get-top-holders-for-markets#parameter-min-balance)

minBalance

integer

default:1

Required range: `0 <= x <= 999999`

#### Response

200

application/json

Success

[​](https://docs.polymarket.com/api-reference/core/get-top-holders-for-markets#response-token)

token

string

[​](https://docs.polymarket.com/api-reference/core/get-top-holders-for-markets#response-holders)

holders

object\[\]

Show child attributes

[​](https://docs.polymarket.com/api-reference/core/get-top-holders-for-markets#response-holders-proxy-wallet)

proxyWallet

string

User Profile Address (0x-prefixed, 40 hex chars)

Example:

`"0x56687bf447db6ffa42ffe2204a05edaa20f55839"`

[​](https://docs.polymarket.com/api-reference/core/get-top-holders-for-markets#response-holders-bio)

bio

string

[​](https://docs.polymarket.com/api-reference/core/get-top-holders-for-markets#response-holders-asset)

asset

string

[​](https://docs.polymarket.com/api-reference/core/get-top-holders-for-markets#response-holders-pseudonym)

pseudonym

string

[​](https://docs.polymarket.com/api-reference/core/get-top-holders-for-markets#response-holders-amount)

amount

number

[​](https://docs.polymarket.com/api-reference/core/get-top-holders-for-markets#response-holders-display-username-public)

displayUsernamePublic

boolean

[​](https://docs.polymarket.com/api-reference/core/get-top-holders-for-markets#response-holders-outcome-index)

outcomeIndex

integer

[​](https://docs.polymarket.com/api-reference/core/get-top-holders-for-markets#response-holders-name)

name

string

[​](https://docs.polymarket.com/api-reference/core/get-top-holders-for-markets#response-holders-profile-image)

profileImage

string

[​](https://docs.polymarket.com/api-reference/core/get-top-holders-for-markets#response-holders-profile-image-optimized)

profileImageOptimized

string

[Get user activity](https://docs.polymarket.com/api-reference/core/get-user-activity)
[Get total value of a user's positions](https://docs.polymarket.com/api-reference/core/get-total-value-of-a-users-positions)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.