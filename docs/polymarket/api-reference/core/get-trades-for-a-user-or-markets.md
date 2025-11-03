---
url: https://docs.polymarket.com/api-reference/core/get-trades-for-a-user-or-markets
title: Get trades for a user or markets - Polymarket Documentation
scraped_at: 2025-11-03T15:03:39.729513
---

[Skip to main content](https://docs.polymarket.com/api-reference/core/get-trades-for-a-user-or-markets#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

⌘K

Search...

Navigation

Core

Get trades for a user or markets

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

Get trades for a user or markets

cURL

Copy

Ask AI

    curl --request GET \
      --url https://data-api.polymarket.com/trades

200

400

401

500

Copy

Ask AI

    [\
      {\
        "proxyWallet": "0x56687bf447db6ffa42ffe2204a05edaa20f55839",\
        "side": "BUY",\
        "asset": "<string>",\
        "conditionId": "0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917",\
        "size": 123,\
        "price": 123,\
        "timestamp": 123,\
        "title": "<string>",\
        "slug": "<string>",\
        "icon": "<string>",\
        "eventSlug": "<string>",\
        "outcome": "<string>",\
        "outcomeIndex": 123,\
        "name": "<string>",\
        "pseudonym": "<string>",\
        "bio": "<string>",\
        "profileImage": "<string>",\
        "profileImageOptimized": "<string>",\
        "transactionHash": "<string>"\
      }\
    ]

GET

/

trades

Try it

Get trades for a user or markets

cURL

Copy

Ask AI

    curl --request GET \
      --url https://data-api.polymarket.com/trades

200

400

401

500

Copy

Ask AI

    [\
      {\
        "proxyWallet": "0x56687bf447db6ffa42ffe2204a05edaa20f55839",\
        "side": "BUY",\
        "asset": "<string>",\
        "conditionId": "0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917",\
        "size": 123,\
        "price": 123,\
        "timestamp": 123,\
        "title": "<string>",\
        "slug": "<string>",\
        "icon": "<string>",\
        "eventSlug": "<string>",\
        "outcome": "<string>",\
        "outcomeIndex": 123,\
        "name": "<string>",\
        "pseudonym": "<string>",\
        "bio": "<string>",\
        "profileImage": "<string>",\
        "profileImageOptimized": "<string>",\
        "transactionHash": "<string>"\
      }\
    ]

#### Query Parameters

[​](https://docs.polymarket.com/api-reference/core/get-trades-for-a-user-or-markets#parameter-limit)

limit

integer

default:100

Required range: `0 <= x <= 10000`

[​](https://docs.polymarket.com/api-reference/core/get-trades-for-a-user-or-markets#parameter-offset)

offset

integer

default:0

Required range: `0 <= x <= 10000`

[​](https://docs.polymarket.com/api-reference/core/get-trades-for-a-user-or-markets#parameter-taker-only)

takerOnly

boolean

default:true

[​](https://docs.polymarket.com/api-reference/core/get-trades-for-a-user-or-markets#parameter-filter-type)

filterType

enum<string>

Must be provided together with filterAmount.

Available options:

`CASH`,

`TOKENS`

[​](https://docs.polymarket.com/api-reference/core/get-trades-for-a-user-or-markets#parameter-filter-amount)

filterAmount

number

Must be provided together with filterType.

Required range: `x >= 0`

[​](https://docs.polymarket.com/api-reference/core/get-trades-for-a-user-or-markets#parameter-market)

market

string\[\]

Comma-separated list of condition IDs. Mutually exclusive with eventId.

0x-prefixed 64-hex string

[​](https://docs.polymarket.com/api-reference/core/get-trades-for-a-user-or-markets#parameter-event-id)

eventId

integer\[\]

Comma-separated list of event IDs. Mutually exclusive with market.

[​](https://docs.polymarket.com/api-reference/core/get-trades-for-a-user-or-markets#parameter-user)

user

string

User Profile Address (0x-prefixed, 40 hex chars)

Example:

`"0x56687bf447db6ffa42ffe2204a05edaa20f55839"`

[​](https://docs.polymarket.com/api-reference/core/get-trades-for-a-user-or-markets#parameter-side)

side

enum<string>

Available options:

`BUY`,

`SELL`

#### Response

200

application/json

Success

[​](https://docs.polymarket.com/api-reference/core/get-trades-for-a-user-or-markets#response-proxy-wallet)

proxyWallet

string

User Profile Address (0x-prefixed, 40 hex chars)

Example:

`"0x56687bf447db6ffa42ffe2204a05edaa20f55839"`

[​](https://docs.polymarket.com/api-reference/core/get-trades-for-a-user-or-markets#response-side)

side

enum<string>

Available options:

`BUY`,

`SELL`

[​](https://docs.polymarket.com/api-reference/core/get-trades-for-a-user-or-markets#response-asset)

asset

string

[​](https://docs.polymarket.com/api-reference/core/get-trades-for-a-user-or-markets#response-condition-id)

conditionId

string

0x-prefixed 64-hex string

Example:

`"0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917"`

[​](https://docs.polymarket.com/api-reference/core/get-trades-for-a-user-or-markets#response-size)

size

number

[​](https://docs.polymarket.com/api-reference/core/get-trades-for-a-user-or-markets#response-price)

price

number

[​](https://docs.polymarket.com/api-reference/core/get-trades-for-a-user-or-markets#response-timestamp)

timestamp

integer

[​](https://docs.polymarket.com/api-reference/core/get-trades-for-a-user-or-markets#response-title)

title

string

[​](https://docs.polymarket.com/api-reference/core/get-trades-for-a-user-or-markets#response-slug)

slug

string

[​](https://docs.polymarket.com/api-reference/core/get-trades-for-a-user-or-markets#response-icon)

icon

string

[​](https://docs.polymarket.com/api-reference/core/get-trades-for-a-user-or-markets#response-event-slug)

eventSlug

string

[​](https://docs.polymarket.com/api-reference/core/get-trades-for-a-user-or-markets#response-outcome)

outcome

string

[​](https://docs.polymarket.com/api-reference/core/get-trades-for-a-user-or-markets#response-outcome-index)

outcomeIndex

integer

[​](https://docs.polymarket.com/api-reference/core/get-trades-for-a-user-or-markets#response-name)

name

string

[​](https://docs.polymarket.com/api-reference/core/get-trades-for-a-user-or-markets#response-pseudonym)

pseudonym

string

[​](https://docs.polymarket.com/api-reference/core/get-trades-for-a-user-or-markets#response-bio)

bio

string

[​](https://docs.polymarket.com/api-reference/core/get-trades-for-a-user-or-markets#response-profile-image)

profileImage

string

[​](https://docs.polymarket.com/api-reference/core/get-trades-for-a-user-or-markets#response-profile-image-optimized)

profileImageOptimized

string

[​](https://docs.polymarket.com/api-reference/core/get-trades-for-a-user-or-markets#response-transaction-hash)

transactionHash

string

[Get current positions for a user](https://docs.polymarket.com/api-reference/core/get-current-positions-for-a-user)
[Get user activity](https://docs.polymarket.com/api-reference/core/get-user-activity)

⌘I