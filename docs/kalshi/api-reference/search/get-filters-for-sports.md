---
url: https://docs.kalshi.com/api-reference/search/get-filters-for-sports
title: Get Filters for Sports - API Documentation
description: Retrieve available filters organized by sport.

This endpoint returns filtering options available for each sport, including scopes and competitions. It also provides an ordered list of sports for display purposes.

scraped_at: 2025-11-03T14:46:29.669081
---

[Skip to main content](https://docs.kalshi.com/api-reference/search/get-filters-for-sports#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

search

Get Filters for Sports

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Get Filters for Sports

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/search/filters_by_sport

200

401

500

Copy

Ask AI

    {
      "filters_by_sports": {},
      "sport_ordering": [\
        "<string>"\
      ]
    }

GET

/

search

/

filters\_by\_sport

Try it

Get Filters for Sports

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/search/filters_by_sport

200

401

500

Copy

Ask AI

    {
      "filters_by_sports": {},
      "sport_ordering": [\
        "<string>"\
      ]
    }

#### Response

200

application/json

Filters retrieved successfully

[​](https://docs.kalshi.com/api-reference/search/get-filters-for-sports#response-filters-by-sports)

filters\_by\_sports

object

required

Mapping of sports to their filter details

Show child attributes

[​](https://docs.kalshi.com/api-reference/search/get-filters-for-sports#response-filters-by-sports-key)

filters\_by\_sports.{key}

object

Show child attributes

[​](https://docs.kalshi.com/api-reference/search/get-filters-for-sports#response-sport-ordering)

sport\_ordering

string\[\]

required

Ordered list of sports for display

[Get Tags for Series Categories](https://docs.kalshi.com/api-reference/search/get-tags-for-series-categories)
[Get Market Candlesticks](https://docs.kalshi.com/api-reference/market/get-market-candlesticks)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.