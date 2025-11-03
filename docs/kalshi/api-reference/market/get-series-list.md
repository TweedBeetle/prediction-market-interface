---
url: https://docs.kalshi.com/api-reference/market/get-series-list
title: Get Series List - API Documentation
description:  Endpoint for getting data about multiple series with specified filters.  A series represents a template for recurring events that follow the same format and rules (e.g., "Monthly Jobs Report", "Weekly Initial Jobless Claims", "Daily Weather in NYC"). This endpoint allows you to browse and discover available series templates by category.
scraped_at: 2025-11-03T14:46:20.321328
---

[Skip to main content](https://docs.kalshi.com/api-reference/market/get-series-list#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

market

Get Series List

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Get Series List

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/series

200

400

500

Copy

Ask AI

    {
      "series": [\
        {\
          "ticker": "<string>",\
          "frequency": "<string>",\
          "title": "<string>",\
          "category": "<string>",\
          "tags": [\
            "<string>"\
          ],\
          "settlement_sources": [\
            {\
              "name": "<string>",\
              "url": "<string>"\
            }\
          ],\
          "contract_url": "<string>",\
          "contract_terms_url": "<string>",\
          "product_metadata": {},\
          "fee_type": "quadratic",\
          "fee_multiplier": 123,\
          "additional_prohibitions": [\
            "<string>"\
          ]\
        }\
      ]
    }

GET

/

series

Try it

Get Series List

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/series

200

400

500

Copy

Ask AI

    {
      "series": [\
        {\
          "ticker": "<string>",\
          "frequency": "<string>",\
          "title": "<string>",\
          "category": "<string>",\
          "tags": [\
            "<string>"\
          ],\
          "settlement_sources": [\
            {\
              "name": "<string>",\
              "url": "<string>"\
            }\
          ],\
          "contract_url": "<string>",\
          "contract_terms_url": "<string>",\
          "product_metadata": {},\
          "fee_type": "quadratic",\
          "fee_multiplier": 123,\
          "additional_prohibitions": [\
            "<string>"\
          ]\
        }\
      ]
    }

#### Query Parameters

[​](https://docs.kalshi.com/api-reference/market/get-series-list#parameter-category)

category

string

[​](https://docs.kalshi.com/api-reference/market/get-series-list#parameter-tags)

tags

string

[​](https://docs.kalshi.com/api-reference/market/get-series-list#parameter-include-product-metadata)

include\_product\_metadata

boolean

default:false

#### Response

200

application/json

Series list retrieved successfully

[​](https://docs.kalshi.com/api-reference/market/get-series-list#response-series)

series

object\[\]

required

Show child attributes

[Get Series](https://docs.kalshi.com/api-reference/market/get-series)
[Get Markets](https://docs.kalshi.com/api-reference/market/get-markets)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.