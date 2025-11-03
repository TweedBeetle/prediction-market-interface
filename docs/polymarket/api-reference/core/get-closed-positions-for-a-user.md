---
url: https://docs.polymarket.com/api-reference/core/get-closed-positions-for-a-user
title: Get closed positions for a user - Polymarket Documentation
description: Fetches closed positions for a user(address)
scraped_at: 2025-11-03T15:03:37.188239
---

[Skip to main content](https://docs.polymarket.com/api-reference/core/get-closed-positions-for-a-user#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

Ctrl K

Search...

Navigation

Core

Get closed positions for a user

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

Get closed positions for a user

cURL

Copy

Ask AI

    curl --request GET \
      --url https://data-api.polymarket.com/closed-positions

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
        "avgPrice": 123,\
        "totalBought": 123,\
        "realizedPnl": 123,\
        "curPrice": 123,\
        "title": "<string>",\
        "slug": "<string>",\
        "icon": "<string>",\
        "eventSlug": "<string>",\
        "outcome": "<string>",\
        "outcomeIndex": 123,\
        "oppositeOutcome": "<string>",\
        "oppositeAsset": "<string>",\
        "endDate": "<string>"\
      }\
    ]

GET

/

closed-positions

Try it

Get closed positions for a user

cURL

Copy

Ask AI

    curl --request GET \
      --url https://data-api.polymarket.com/closed-positions

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
        "avgPrice": 123,\
        "totalBought": 123,\
        "realizedPnl": 123,\
        "curPrice": 123,\
        "title": "<string>",\
        "slug": "<string>",\
        "icon": "<string>",\
        "eventSlug": "<string>",\
        "outcome": "<string>",\
        "outcomeIndex": 123,\
        "oppositeOutcome": "<string>",\
        "oppositeAsset": "<string>",\
        "endDate": "<string>"\
      }\
    ]

#### Query Parameters

[​](https://docs.polymarket.com/api-reference/core/get-closed-positions-for-a-user#parameter-user)

user

string

required

The address of the user in question

Example:

`"0x56687bf447db6ffa42ffe2204a05edaa20f55839"`

[​](https://docs.polymarket.com/api-reference/core/get-closed-positions-for-a-user#parameter-market)

market

string\[\]

The conditionId of the market in question. Supports multiple csv separated values. Cannot be used with the eventId param.

0x-prefixed 64-hex string

[​](https://docs.polymarket.com/api-reference/core/get-closed-positions-for-a-user#parameter-title)

title

string

Filter by market title

Maximum length: `100`

[​](https://docs.polymarket.com/api-reference/core/get-closed-positions-for-a-user#parameter-event-id)

eventId

integer\[\]

The event id of the event in question. Supports multiple csv separated values. Returns positions for all markets for those event ids. Cannot be used with the market param.

[​](https://docs.polymarket.com/api-reference/core/get-closed-positions-for-a-user#parameter-limit)

limit

integer

default:50

The max number of positions to return

Required range: `0 <= x <= 500`

[​](https://docs.polymarket.com/api-reference/core/get-closed-positions-for-a-user#parameter-offset)

offset

integer

default:0

The starting index for pagination

Required range: `0 <= x <= 10000`

[​](https://docs.polymarket.com/api-reference/core/get-closed-positions-for-a-user#parameter-sort-by)

sortBy

enum<string>

default:REALIZEDPNL

The sort criteria

Available options:

`REALIZEDPNL`,

`TITLE`,

`PRICE`,

`AVGPRICE`

[​](https://docs.polymarket.com/api-reference/core/get-closed-positions-for-a-user#parameter-sort-direction)

sortDirection

enum<string>

default:DESC

The sort direction

Available options:

`ASC`,

`DESC`

#### Response

200

application/json

Success

[​](https://docs.polymarket.com/api-reference/core/get-closed-positions-for-a-user#response-proxy-wallet)

proxyWallet

string

User Profile Address (0x-prefixed, 40 hex chars)

Example:

`"0x56687bf447db6ffa42ffe2204a05edaa20f55839"`

[​](https://docs.polymarket.com/api-reference/core/get-closed-positions-for-a-user#response-asset)

asset

string

[​](https://docs.polymarket.com/api-reference/core/get-closed-positions-for-a-user#response-condition-id)

conditionId

string

0x-prefixed 64-hex string

Example:

`"0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917"`

[​](https://docs.polymarket.com/api-reference/core/get-closed-positions-for-a-user#response-avg-price)

avgPrice

number

[​](https://docs.polymarket.com/api-reference/core/get-closed-positions-for-a-user#response-total-bought)

totalBought

number

[​](https://docs.polymarket.com/api-reference/core/get-closed-positions-for-a-user#response-realized-pnl)

realizedPnl

number

[​](https://docs.polymarket.com/api-reference/core/get-closed-positions-for-a-user#response-cur-price)

curPrice

number

[​](https://docs.polymarket.com/api-reference/core/get-closed-positions-for-a-user#response-title)

title

string

[​](https://docs.polymarket.com/api-reference/core/get-closed-positions-for-a-user#response-slug)

slug

string

[​](https://docs.polymarket.com/api-reference/core/get-closed-positions-for-a-user#response-icon)

icon

string

[​](https://docs.polymarket.com/api-reference/core/get-closed-positions-for-a-user#response-event-slug)

eventSlug

string

[​](https://docs.polymarket.com/api-reference/core/get-closed-positions-for-a-user#response-outcome)

outcome

string

[​](https://docs.polymarket.com/api-reference/core/get-closed-positions-for-a-user#response-outcome-index)

outcomeIndex

integer

[​](https://docs.polymarket.com/api-reference/core/get-closed-positions-for-a-user#response-opposite-outcome)

oppositeOutcome

string

[​](https://docs.polymarket.com/api-reference/core/get-closed-positions-for-a-user#response-opposite-asset)

oppositeAsset

string

[​](https://docs.polymarket.com/api-reference/core/get-closed-positions-for-a-user#response-end-date)

endDate

string

[Get total value of a user's positions](https://docs.polymarket.com/api-reference/core/get-total-value-of-a-users-positions)
[Get total markets a user has traded](https://docs.polymarket.com/api-reference/misc/get-total-markets-a-user-has-traded)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.