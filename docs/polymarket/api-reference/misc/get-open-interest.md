---
url: https://docs.polymarket.com/api-reference/misc/get-open-interest
title: Get open interest - Polymarket Documentation
scraped_at: 2025-11-03T15:03:45.309880
---

[Skip to main content](https://docs.polymarket.com/api-reference/misc/get-open-interest#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

Ctrl K

Search...

Navigation

Misc

Get open interest

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

Get open interest

cURL

Copy

Ask AI

    curl --request GET \
      --url https://data-api.polymarket.com/oi

200

400

500

Copy

Ask AI

    [\
      {\
        "market": "0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917",\
        "value": 123\
      }\
    ]

GET

/

oi

Try it

Get open interest

cURL

Copy

Ask AI

    curl --request GET \
      --url https://data-api.polymarket.com/oi

200

400

500

Copy

Ask AI

    [\
      {\
        "market": "0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917",\
        "value": 123\
      }\
    ]

#### Query Parameters

[​](https://docs.polymarket.com/api-reference/misc/get-open-interest#parameter-market)

market

string\[\]

0x-prefixed 64-hex string

#### Response

200

application/json

Success

[​](https://docs.polymarket.com/api-reference/misc/get-open-interest#response-market)

market

string

0x-prefixed 64-hex string

Example:

`"0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917"`

[​](https://docs.polymarket.com/api-reference/misc/get-open-interest#response-value)

value

number

[Get total markets a user has traded](https://docs.polymarket.com/api-reference/misc/get-total-markets-a-user-has-traded)
[Get live volume for an event](https://docs.polymarket.com/api-reference/misc/get-live-volume-for-an-event)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.