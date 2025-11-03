---
url: https://docs.kalshi.com/api-reference/exchange/get-series-fee-changes
title: Get Series Fee Changes - API Documentation
scraped_at: 2025-11-03T14:46:15.240563
---

[Skip to main content](https://docs.kalshi.com/api-reference/exchange/get-series-fee-changes#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

exchange

Get Series Fee Changes

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Get Series Fee Changes

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/series/fee_changes

200

400

500

Copy

Ask AI

    {
      "series_fee_change_arr": [\
        {\
          "id": "<string>",\
          "series_ticker": "<string>",\
          "fee_type": "quadratic",\
          "fee_multiplier": 123,\
          "scheduled_ts": "2023-11-07T05:31:56Z"\
        }\
      ]
    }

GET

/

series

/

fee\_changes

Try it

Get Series Fee Changes

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/series/fee_changes

200

400

500

Copy

Ask AI

    {
      "series_fee_change_arr": [\
        {\
          "id": "<string>",\
          "series_ticker": "<string>",\
          "fee_type": "quadratic",\
          "fee_multiplier": 123,\
          "scheduled_ts": "2023-11-07T05:31:56Z"\
        }\
      ]
    }

#### Query Parameters

[​](https://docs.kalshi.com/api-reference/exchange/get-series-fee-changes#parameter-series-ticker)

series\_ticker

string

[​](https://docs.kalshi.com/api-reference/exchange/get-series-fee-changes#parameter-show-historical)

show\_historical

boolean

default:false

#### Response

200

application/json

Series fee changes retrieved successfully

[​](https://docs.kalshi.com/api-reference/exchange/get-series-fee-changes#response-series-fee-change-arr)

series\_fee\_change\_arr

object\[\]

required

Show child attributes

[​](https://docs.kalshi.com/api-reference/exchange/get-series-fee-changes#response-series-fee-change-arr-id)

id

string

required

Unique identifier for this fee change

[​](https://docs.kalshi.com/api-reference/exchange/get-series-fee-changes#response-series-fee-change-arr-series-ticker)

series\_ticker

string

required

Series ticker this fee change applies to

[​](https://docs.kalshi.com/api-reference/exchange/get-series-fee-changes#response-series-fee-change-arr-fee-type)

fee\_type

enum<string>

required

New fee type for the series

Available options:

`quadratic`,

`quadratic_with_maker_fees`,

`flat`

[​](https://docs.kalshi.com/api-reference/exchange/get-series-fee-changes#response-series-fee-change-arr-fee-multiplier)

fee\_multiplier

number

required

New fee multiplier for the series

[​](https://docs.kalshi.com/api-reference/exchange/get-series-fee-changes#response-series-fee-change-arr-scheduled-ts)

scheduled\_ts

string<date-time>

required

Timestamp when this fee change is scheduled to take effect

[Get Exchange Announcements](https://docs.kalshi.com/api-reference/exchange/get-exchange-announcements)
[Get Exchange Schedule](https://docs.kalshi.com/api-reference/exchange/get-exchange-schedule)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.