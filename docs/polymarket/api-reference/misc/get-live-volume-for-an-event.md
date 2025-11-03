---
url: https://docs.polymarket.com/api-reference/misc/get-live-volume-for-an-event
title: Get live volume for an event - Polymarket Documentation
scraped_at: 2025-11-03T15:03:44.807252
---

[Skip to main content](https://docs.polymarket.com/api-reference/misc/get-live-volume-for-an-event#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

Ctrl K

Search...

Navigation

Misc

Get live volume for an event

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

Get live volume for an event

cURL

Copy

Ask AI

    curl --request GET \
      --url https://data-api.polymarket.com/live-volume

200

400

500

Copy

Ask AI

    [\
      {\
        "total": 123,\
        "markets": [\
          {\
            "market": "0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917",\
            "value": 123\
          }\
        ]\
      }\
    ]

GET

/

live-volume

Try it

Get live volume for an event

cURL

Copy

Ask AI

    curl --request GET \
      --url https://data-api.polymarket.com/live-volume

200

400

500

Copy

Ask AI

    [\
      {\
        "total": 123,\
        "markets": [\
          {\
            "market": "0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917",\
            "value": 123\
          }\
        ]\
      }\
    ]

#### Query Parameters

[​](https://docs.polymarket.com/api-reference/misc/get-live-volume-for-an-event#parameter-id)

id

integer

required

Required range: `x >= 1`

#### Response

200

application/json

Success

[​](https://docs.polymarket.com/api-reference/misc/get-live-volume-for-an-event#response-total)

total

number

[​](https://docs.polymarket.com/api-reference/misc/get-live-volume-for-an-event#response-markets)

markets

object\[\]

Show child attributes

[​](https://docs.polymarket.com/api-reference/misc/get-live-volume-for-an-event#response-markets-market)

market

string

0x-prefixed 64-hex string

Example:

`"0xdd22472e552920b8438158ea7238bfadfa4f736aa4cee91a6b86c39ead110917"`

[​](https://docs.polymarket.com/api-reference/misc/get-live-volume-for-an-event#response-markets-value)

value

number

[Get open interest](https://docs.polymarket.com/api-reference/misc/get-open-interest)
[Overview](https://docs.polymarket.com/developers/subgraph/overview)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.