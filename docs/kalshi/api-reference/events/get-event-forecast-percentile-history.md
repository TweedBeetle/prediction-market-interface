---
url: https://docs.kalshi.com/api-reference/events/get-event-forecast-percentile-history
title: Get Event Forecast Percentile History - API Documentation
description: Endpoint for getting the historical raw and formatted forecast numbers for an event at specific percentiles.
scraped_at: 2025-11-03T14:46:10.624478
---

[Skip to main content](https://docs.kalshi.com/api-reference/events/get-event-forecast-percentile-history#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

events

Get Event Forecast Percentile History

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Get Event Forecast Percentile History

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/series/{series_ticker}/events/{ticker}/forecast_percentile_history \
      --header 'KALSHI-ACCESS-KEY: <api-key>' \
      --header 'KALSHI-ACCESS-SIGNATURE: <api-key>' \
      --header 'KALSHI-ACCESS-TIMESTAMP: <api-key>'

200

400

401

500

Copy

Ask AI

    {
      "forecast_history": [\
        {\
          "event_ticker": "<string>",\
          "end_period_ts": 123,\
          "period_interval": 123,\
          "percentile_points": [\
            {\
              "percentile": 123,\
              "raw_numerical_forecast": 123,\
              "numerical_forecast": 123,\
              "formatted_forecast": "<string>"\
            }\
          ]\
        }\
      ]
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

forecast\_percentile\_history

Try it

Get Event Forecast Percentile History

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/series/{series_ticker}/events/{ticker}/forecast_percentile_history \
      --header 'KALSHI-ACCESS-KEY: <api-key>' \
      --header 'KALSHI-ACCESS-SIGNATURE: <api-key>' \
      --header 'KALSHI-ACCESS-TIMESTAMP: <api-key>'

200

400

401

500

Copy

Ask AI

    {
      "forecast_history": [\
        {\
          "event_ticker": "<string>",\
          "end_period_ts": 123,\
          "period_interval": 123,\
          "percentile_points": [\
            {\
              "percentile": 123,\
              "raw_numerical_forecast": 123,\
              "numerical_forecast": 123,\
              "formatted_forecast": "<string>"\
            }\
          ]\
        }\
      ]
    }

#### Authorizations

[​](https://docs.kalshi.com/api-reference/events/get-event-forecast-percentile-history#authorization-kalshi-access-key)

KALSHI-ACCESS-KEY

string

header

required

Your API key ID

[​](https://docs.kalshi.com/api-reference/events/get-event-forecast-percentile-history#authorization-kalshi-access-signature)

KALSHI-ACCESS-SIGNATURE

string

header

required

RSA-PSS signature of the request

[​](https://docs.kalshi.com/api-reference/events/get-event-forecast-percentile-history#authorization-kalshi-access-timestamp)

KALSHI-ACCESS-TIMESTAMP

string

header

required

Request timestamp in milliseconds

#### Path Parameters

[​](https://docs.kalshi.com/api-reference/events/get-event-forecast-percentile-history#parameter-ticker)

ticker

string

required

The event ticker

[​](https://docs.kalshi.com/api-reference/events/get-event-forecast-percentile-history#parameter-series-ticker)

series\_ticker

string

required

The series ticker

#### Query Parameters

[​](https://docs.kalshi.com/api-reference/events/get-event-forecast-percentile-history#parameter-percentiles)

percentiles

integer\[\]

required

Array of percentile values to retrieve (0-10000, max 10 values)

Maximum length: `10`

[​](https://docs.kalshi.com/api-reference/events/get-event-forecast-percentile-history#parameter-start-ts)

start\_ts

integer

required

Start timestamp for the range

[​](https://docs.kalshi.com/api-reference/events/get-event-forecast-percentile-history#parameter-end-ts)

end\_ts

integer

required

End timestamp for the range

[​](https://docs.kalshi.com/api-reference/events/get-event-forecast-percentile-history#parameter-period-interval)

period\_interval

enum<integer>

required

Specifies the length of each forecast period, in minutes. 0 for 5-second intervals, or 1, 60, or 1440 for minute-based intervals.

Available options:

`0`,

`1`,

`60`,

`1440`

#### Response

200

application/json

Event forecast percentile history retrieved successfully

[​](https://docs.kalshi.com/api-reference/events/get-event-forecast-percentile-history#response-forecast-history)

forecast\_history

object\[\]

required

Array of forecast percentile data points over time.

Show child attributes

[Get Event Metadata](https://docs.kalshi.com/api-reference/events/get-event-metadata)
[Get Live Data](https://docs.kalshi.com/api-reference/live_data/get-live-data)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.