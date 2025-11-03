---
url: https://docs.kalshi.com/api-reference/search/get-tags-for-series-categories
title: Get Tags for Series Categories - API Documentation
description: Retrieve tags organized by series categories.

This endpoint returns a mapping of series categories to their associated tags, which can be used for filtering and search functionality.

scraped_at: 2025-11-03T14:46:32.721408
---

[Skip to main content](https://docs.kalshi.com/api-reference/search/get-tags-for-series-categories#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

search

Get Tags for Series Categories

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Get Tags for Series Categories

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/search/tags_by_categories

200

401

500

Copy

Ask AI

    {
      "tags_by_categories": {}
    }

GET

/

search

/

tags\_by\_categories

Try it

Get Tags for Series Categories

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/search/tags_by_categories

200

401

500

Copy

Ask AI

    {
      "tags_by_categories": {}
    }

#### Response

200

application/json

Tags retrieved successfully

[​](https://docs.kalshi.com/api-reference/search/get-tags-for-series-categories#response-tags-by-categories)

tags\_by\_categories

object

required

Mapping of series categories to their associated tags

Show child attributes

[​](https://docs.kalshi.com/api-reference/search/get-tags-for-series-categories#response-tags-by-categories-key)

tags\_by\_categories.{key}

string\[\]

[Delete API Key](https://docs.kalshi.com/api-reference/api-keys/delete-api-key)
[Get Filters for Sports](https://docs.kalshi.com/api-reference/search/get-filters-for-sports)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.