---
url: https://docs.kalshi.com/api-reference/events/get-event-candlesticks
title: Get Event Candlesticks - API Documentation
description:  End-point for returning aggregated data across all markets corresponding to an event.
scraped_at: 2025-11-03T14:46:14.233754
---

[Skip to main content](https://docs.kalshi.com/api-reference/events/get-event-candlesticks#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

events

Get Event Candlesticks

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Get Event Candlesticks

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/series/{series_ticker}/events/{ticker}/candlesticks

200

400

401

500

Copy

Ask AI

    {
      "market_tickers": [\
        "<string>"\
      ],
      "market_candlesticks": [\
        [\
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
        ]\
      ],
      "adjusted_end_ts": 123
    }

GET

/

series

/

{series\_ticker}

/

events

/

{ticker}

/

candlesticks

Try it

Get Event Candlesticks

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/series/{series_ticker}/events/{ticker}/candlesticks

200

400

401

500

Copy

Ask AI

    {
      "market_tickers": [\
        "<string>"\
      ],
      "market_candlesticks": [\
        [\
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
        ]\
      ],
      "adjusted_end_ts": 123
    }

#### Path Parameters

[​](https://docs.kalshi.com/api-reference/events/get-event-candlesticks#parameter-ticker)

ticker

string

required

The event ticker

[​](https://docs.kalshi.com/api-reference/events/get-event-candlesticks#parameter-series-ticker)

series\_ticker

string

required

The series ticker

#### Query Parameters

[​](https://docs.kalshi.com/api-reference/events/get-event-candlesticks#parameter-start-ts)

start\_ts

integer

required

Start timestamp for the range

[​](https://docs.kalshi.com/api-reference/events/get-event-candlesticks#parameter-end-ts)

end\_ts

integer

required

End timestamp for the range

[​](https://docs.kalshi.com/api-reference/events/get-event-candlesticks#parameter-period-interval)

period\_interval

enum<integer>

required

Specifies the length of each candlestick period, in minutes. Must be one minute, one hour, or one day.

Available options:

`1`,

`60`,

`1440`

#### Response

200

application/json

Event candlesticks retrieved successfully

[​](https://docs.kalshi.com/api-reference/events/get-event-candlesticks#response-market-tickers)

market\_tickers

string\[\]

required

Array of market tickers in the event.

[​](https://docs.kalshi.com/api-reference/events/get-event-candlesticks#response-market-candlesticks)

market\_candlesticks

object\[\]\[\]

required

Array of market candlestick arrays, one for each market in the event.

Show child attributes

[​](https://docs.kalshi.com/api-reference/events/get-event-candlesticks#response-adjusted-end-ts)

adjusted\_end\_ts

integer

required

Adjusted end timestamp if the requested candlesticks would be larger than maxAggregateCandidates.

[Get Market](https://docs.kalshi.com/api-reference/market/get-market)
[Get Events](https://docs.kalshi.com/api-reference/events/get-events)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.