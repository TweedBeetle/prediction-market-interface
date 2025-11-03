---
url: https://docs.polymarket.com/api-reference/core/get-current-positions-for-a-user
title: Get current positions for a user - Polymarket Documentation
description: Returns positions filtered by user and optional filters.
scraped_at: 2025-11-03T15:03:39.229630
---

[Skip to main content](https://docs.polymarket.com/api-reference/core/get-current-positions-for-a-user#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

Ctrl K

Search...

Navigation

Core

Get current positions for a user

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

Get current positions for a user

cURL

Copy

Ask AI

    curl --request GET \
      --url https://data-api.polymarket.com/positions

200

400

401

500

Copy

Ask AI

    [\
      {\
        "proxyWallet": "0x56687bf447db6ffa42ffe2204a05edaa20f55839",\
        "asset": "<string>",\
        "conditionId": "0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917",\
        "size": 123,\
        "avgPrice": 123,\
        "initialValue": 123,\
        "currentValue": 123,\
        "cashPnl": 123,\
        "percentPnl": 123,\
        "totalBought": 123,\
        "realizedPnl": 123,\
        "percentRealizedPnl": 123,\
        "curPrice": 123,\
        "redeemable": true,\
        "mergeable": true,\
        "title": "<string>",\
        "slug": "<string>",\
        "icon": "<string>",\
        "eventSlug": "<string>",\
        "outcome": "<string>",\
        "outcomeIndex": 123,\
        "oppositeOutcome": "<string>",\
        "oppositeAsset": "<string>",\
        "endDate": "<string>",\
        "negativeRisk": true\
      }\
    ]

GET

/

positions

Try it

Get current positions for a user

cURL

Copy

Ask AI

    curl --request GET \
      --url https://data-api.polymarket.com/positions

200

400

401

500

Copy

Ask AI

    [\
      {\
        "proxyWallet": "0x56687bf447db6ffa42ffe2204a05edaa20f55839",\
        "asset": "<string>",\
        "conditionId": "0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917",\
        "size": 123,\
        "avgPrice": 123,\
        "initialValue": 123,\
        "currentValue": 123,\
        "cashPnl": 123,\
        "percentPnl": 123,\
        "totalBought": 123,\
        "realizedPnl": 123,\
        "percentRealizedPnl": 123,\
        "curPrice": 123,\
        "redeemable": true,\
        "mergeable": true,\
        "title": "<string>",\
        "slug": "<string>",\
        "icon": "<string>",\
        "eventSlug": "<string>",\
        "outcome": "<string>",\
        "outcomeIndex": 123,\
        "oppositeOutcome": "<string>",\
        "oppositeAsset": "<string>",\
        "endDate": "<string>",\
        "negativeRisk": true\
      }\
    ]

#### Query Parameters

[​](https://docs.polymarket.com/api-reference/core/get-current-positions-for-a-user#parameter-user)

user

string

required

User address (required)

Example:

`"0x56687bf447db6ffa42ffe2204a05edaa20f55839"`

[​](https://docs.polymarket.com/api-reference/core/get-current-positions-for-a-user#parameter-market)

market

string\[\]

Comma-separated list of condition IDs. Mutually exclusive with eventId.

0x-prefixed 64-hex string

[​](https://docs.polymarket.com/api-reference/core/get-current-positions-for-a-user#parameter-event-id)

eventId

integer\[\]

Comma-separated list of event IDs. Mutually exclusive with market.

[​](https://docs.polymarket.com/api-reference/core/get-current-positions-for-a-user#parameter-size-threshold)

sizeThreshold

number

default:1

Required range: `x >= 0`

[​](https://docs.polymarket.com/api-reference/core/get-current-positions-for-a-user#parameter-redeemable)

redeemable

boolean

default:false

[​](https://docs.polymarket.com/api-reference/core/get-current-positions-for-a-user#parameter-mergeable)

mergeable

boolean

default:false

[​](https://docs.polymarket.com/api-reference/core/get-current-positions-for-a-user#parameter-limit)

limit

integer

default:100

Required range: `0 <= x <= 500`

[​](https://docs.polymarket.com/api-reference/core/get-current-positions-for-a-user#parameter-offset)

offset

integer

default:0

Required range: `0 <= x <= 10000`

[​](https://docs.polymarket.com/api-reference/core/get-current-positions-for-a-user#parameter-sort-by)

sortBy

enum<string>

default:TOKENS

Available options:

`CURRENT`,

`INITIAL`,

`TOKENS`,

`CASHPNL`,

`PERCENTPNL`,

`TITLE`,

`RESOLVING`,

`PRICE`,

`AVGPRICE`

[​](https://docs.polymarket.com/api-reference/core/get-current-positions-for-a-user#parameter-sort-direction)

sortDirection

enum<string>

default:DESC

Available options:

`ASC`,

`DESC`

[​](https://docs.polymarket.com/api-reference/core/get-current-positions-for-a-user#parameter-title)

title

string

Maximum length: `100`

#### Response

200

application/json

Success

[​](https://docs.polymarket.com/api-reference/core/get-current-positions-for-a-user#response-proxy-wallet)

proxyWallet

string

User Profile Address (0x-prefixed, 40 hex chars)

Example:

`"0x56687bf447db6ffa42ffe2204a05edaa20f55839"`

[​](https://docs.polymarket.com/api-reference/core/get-current-positions-for-a-user#response-asset)

asset

string

[​](https://docs.polymarket.com/api-reference/core/get-current-positions-for-a-user#response-condition-id)

conditionId

string

0x-prefixed 64-hex string

Example:

`"0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917"`

[​](https://docs.polymarket.com/api-reference/core/get-current-positions-for-a-user#response-size)

size

number

[​](https://docs.polymarket.com/api-reference/core/get-current-positions-for-a-user#response-avg-price)

avgPrice

number

[​](https://docs.polymarket.com/api-reference/core/get-current-positions-for-a-user#response-initial-value)

initialValue

number

[​](https://docs.polymarket.com/api-reference/core/get-current-positions-for-a-user#response-current-value)

currentValue

number

[​](https://docs.polymarket.com/api-reference/core/get-current-positions-for-a-user#response-cash-pnl)

cashPnl

number

[​](https://docs.polymarket.com/api-reference/core/get-current-positions-for-a-user#response-percent-pnl)

percentPnl

number

[​](https://docs.polymarket.com/api-reference/core/get-current-positions-for-a-user#response-total-bought)

totalBought

number

[​](https://docs.polymarket.com/api-reference/core/get-current-positions-for-a-user#response-realized-pnl)

realizedPnl

number

[​](https://docs.polymarket.com/api-reference/core/get-current-positions-for-a-user#response-percent-realized-pnl)

percentRealizedPnl

number

[​](https://docs.polymarket.com/api-reference/core/get-current-positions-for-a-user#response-cur-price)

curPrice

number

[​](https://docs.polymarket.com/api-reference/core/get-current-positions-for-a-user#response-redeemable)

redeemable

boolean

[​](https://docs.polymarket.com/api-reference/core/get-current-positions-for-a-user#response-mergeable)

mergeable

boolean

[​](https://docs.polymarket.com/api-reference/core/get-current-positions-for-a-user#response-title)

title

string

[​](https://docs.polymarket.com/api-reference/core/get-current-positions-for-a-user#response-slug)

slug

string

[​](https://docs.polymarket.com/api-reference/core/get-current-positions-for-a-user#response-icon)

icon

string

[​](https://docs.polymarket.com/api-reference/core/get-current-positions-for-a-user#response-event-slug)

eventSlug

string

[​](https://docs.polymarket.com/api-reference/core/get-current-positions-for-a-user#response-outcome)

outcome

string

[​](https://docs.polymarket.com/api-reference/core/get-current-positions-for-a-user#response-outcome-index)

outcomeIndex

integer

[​](https://docs.polymarket.com/api-reference/core/get-current-positions-for-a-user#response-opposite-outcome)

oppositeOutcome

string

[​](https://docs.polymarket.com/api-reference/core/get-current-positions-for-a-user#response-opposite-asset)

oppositeAsset

string

[​](https://docs.polymarket.com/api-reference/core/get-current-positions-for-a-user#response-end-date)

endDate

string

[​](https://docs.polymarket.com/api-reference/core/get-current-positions-for-a-user#response-negative-risk)

negativeRisk

boolean

[Health check](https://docs.polymarket.com/api-reference/health/health-check)
[Get trades for a user or markets](https://docs.polymarket.com/api-reference/core/get-trades-for-a-user-or-markets)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.