---
url: https://docs.kalshi.com/api-reference/market/get-market-candlesticks
title: Get Market Candlesticks - API Documentation
description: Time period length of each candlestick in minutes. Valid values: 1 (1 minute), 60 (1 hour), 1440 (1 day).
scraped_at: 2025-11-03T14:46:19.835358
---

[Skip to main content](https://docs.kalshi.com/api-reference/market/get-market-candlesticks#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

market

Get Market Candlesticks

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Get Market Candlesticks

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/series/{series_ticker}/markets/{ticker}/candlesticks

200

400

404

500

Copy

Ask AI

    {
      "ticker": "<string>",
      "candlesticks": [\
        {\
          "end_period_ts": 123,\
          "yes_bid": {\
            "open": 123,\
            "open_dollars": "<string>",\
            "low": 123,\
            "low_dollars": "<string>",\
            "high": 123,\
            "high_dollars": "<string>",\
            "close": 123,\
            "close_dollars": "<string>"\
          },\
          "yes_ask": {\
            "open": 123,\
            "open_dollars": "<string>",\
            "low": 123,\
            "low_dollars": "<string>",\
            "high": 123,\
            "high_dollars": "<string>",\
            "close": 123,\
            "close_dollars": "<string>"\
          },\
          "price": {\
            "open": 123,\
            "open_dollars": "<string>",\
            "low": 123,\
            "low_dollars": "<string>",\
            "high": 123,\
            "high_dollars": "<string>",\
            "close": 123,\
            "close_dollars": "<string>",\
            "mean": 123,\
            "mean_dollars": "<string>",\
            "previous": 123,\
            "previous_dollars": "<string>",\
            "min": 123,\
            "min_dollars": "<string>",\
            "max": 123,\
            "max_dollars": "<string>"\
          },\
          "volume": 123,\
          "open_interest": 123\
        }\
      ]
    }

GET

/

series

/

{series\_ticker}

/

markets

/

{ticker}

/

candlesticks

Try it

Get Market Candlesticks

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/series/{series_ticker}/markets/{ticker}/candlesticks

200

400

404

500

Copy

Ask AI

    {
      "ticker": "<string>",
      "candlesticks": [\
        {\
          "end_period_ts": 123,\
          "yes_bid": {\
            "open": 123,\
            "open_dollars": "<string>",\
            "low": 123,\
            "low_dollars": "<string>",\
            "high": 123,\
            "high_dollars": "<string>",\
            "close": 123,\
            "close_dollars": "<string>"\
          },\
          "yes_ask": {\
            "open": 123,\
            "open_dollars": "<string>",\
            "low": 123,\
            "low_dollars": "<string>",\
            "high": 123,\
            "high_dollars": "<string>",\
            "close": 123,\
            "close_dollars": "<string>"\
          },\
          "price": {\
            "open": 123,\
            "open_dollars": "<string>",\
            "low": 123,\
            "low_dollars": "<string>",\
            "high": 123,\
            "high_dollars": "<string>",\
            "close": 123,\
            "close_dollars": "<string>",\
            "mean": 123,\
            "mean_dollars": "<string>",\
            "previous": 123,\
            "previous_dollars": "<string>",\
            "min": 123,\
            "min_dollars": "<string>",\
            "max": 123,\
            "max_dollars": "<string>"\
          },\
          "volume": 123,\
          "open_interest": 123\
        }\
      ]
    }

#### Path Parameters

[​](https://docs.kalshi.com/api-reference/market/get-market-candlesticks#parameter-series-ticker)

series\_ticker

string

required

Series ticker - the series that contains the target market

[​](https://docs.kalshi.com/api-reference/market/get-market-candlesticks#parameter-ticker)

ticker

string

required

Market ticker - unique identifier for the specific market

#### Query Parameters

[​](https://docs.kalshi.com/api-reference/market/get-market-candlesticks#parameter-start-ts)

start\_ts

integer

required

Start timestamp (Unix timestamp). Candlesticks will include those ending on or after this time.

[​](https://docs.kalshi.com/api-reference/market/get-market-candlesticks#parameter-end-ts)

end\_ts

integer

required

End timestamp (Unix timestamp). Candlesticks will include those ending on or before this time.

[​](https://docs.kalshi.com/api-reference/market/get-market-candlesticks#parameter-period-interval)

period\_interval

enum<integer>

required

Time period length of each candlestick in minutes. Valid values are 1 (1 minute), 60 (1 hour), or 1440 (1 day).

Available options:

`1`,

`60`,

`1440`

#### Response

200

application/json

Candlesticks retrieved successfully

[​](https://docs.kalshi.com/api-reference/market/get-market-candlesticks#response-ticker)

ticker

string

required

Unique identifier for the market.

[​](https://docs.kalshi.com/api-reference/market/get-market-candlesticks#response-candlesticks)

candlesticks

object\[\]

required

Array of candlestick data points for the specified time range.

Show child attributes

[Get Filters for Sports](https://docs.kalshi.com/api-reference/search/get-filters-for-sports)
[Get Trades](https://docs.kalshi.com/api-reference/market/get-trades)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.