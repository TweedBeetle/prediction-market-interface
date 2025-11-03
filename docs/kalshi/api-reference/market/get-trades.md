---
url: https://docs.kalshi.com/api-reference/market/get-trades
title: Get Trades - API Documentation
description:  Endpoint for getting all trades for all markets.  A trade represents a completed transaction between two users on a specific market. Each trade includes the market ticker, price, quantity, and timestamp information.  This endpoint returns a paginated response. Use the 'limit' parameter to control page size (1-1000, defaults to 100). The response includes a 'cursor' field - pass this value in the 'cursor' parameter of your next request to get the next page. An empty cursor indicates no more pages are available.
scraped_at: 2025-11-03T14:46:20.326908
---

[Skip to main content](https://docs.kalshi.com/api-reference/market/get-trades#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

market

Get Trades

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Get Trades

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/markets/trades

200

400

500

Copy

Ask AI

    {
      "trades": [\
        {\
          "trade_id": "<string>",\
          "ticker": "<string>",\
          "price": 123,\
          "count": 123,\
          "yes_price": 123,\
          "no_price": 123,\
          "yes_price_dollars": "<string>",\
          "no_price_dollars": "<string>",\
          "taker_side": "yes",\
          "created_time": "2023-11-07T05:31:56Z"\
        }\
      ],
      "cursor": "<string>"
    }

GET

/

markets

/

trades

Try it

Get Trades

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/markets/trades

200

400

500

Copy

Ask AI

    {
      "trades": [\
        {\
          "trade_id": "<string>",\
          "ticker": "<string>",\
          "price": 123,\
          "count": 123,\
          "yes_price": 123,\
          "no_price": 123,\
          "yes_price_dollars": "<string>",\
          "no_price_dollars": "<string>",\
          "taker_side": "yes",\
          "created_time": "2023-11-07T05:31:56Z"\
        }\
      ],
      "cursor": "<string>"
    }

#### Query Parameters

[​](https://docs.kalshi.com/api-reference/market/get-trades#parameter-limit)

limit

integer

default:100

Number of results per page. Defaults to 100. Maximum value is 1000.

Required range: `1 <= x <= 1000`

[​](https://docs.kalshi.com/api-reference/market/get-trades#parameter-cursor)

cursor

string

Pagination cursor. Use the cursor value returned from the previous response to get the next page of results. Leave empty for the first page.

[​](https://docs.kalshi.com/api-reference/market/get-trades#parameter-ticker)

ticker

string

Filter by market ticker

[​](https://docs.kalshi.com/api-reference/market/get-trades#parameter-min-ts)

min\_ts

integer

Filter items after this Unix timestamp

[​](https://docs.kalshi.com/api-reference/market/get-trades#parameter-max-ts)

max\_ts

integer

Filter items before this Unix timestamp

#### Response

200

application/json

Trades retrieved successfully

[​](https://docs.kalshi.com/api-reference/market/get-trades#response-trades)

trades

object\[\]

Show child attributes

[​](https://docs.kalshi.com/api-reference/market/get-trades#response-cursor)

cursor

string

[Get Market Candlesticks](https://docs.kalshi.com/api-reference/market/get-market-candlesticks)
[Get Market Orderbook](https://docs.kalshi.com/api-reference/market/get-market-orderbook)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.