---
url: https://docs.kalshi.com/api-reference/portfolio/get-positions
title: Get Positions - API Documentation
description: Restricts the positions to those with any of following fields with non-zero values, as a comma separated list. The following values are accepted: position, total_traded, resting_order_count
scraped_at: 2025-11-03T14:46:28.414536
---

[Skip to main content](https://docs.kalshi.com/api-reference/portfolio/get-positions#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

portfolio

Get Positions

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Get Positions

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/portfolio/positions \
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
      "cursor": "<string>",
      "market_positions": [\
        {\
          "ticker": "<string>",\
          "total_traded": 123,\
          "total_traded_dollars": "<string>",\
          "position": 123,\
          "market_exposure": 123,\
          "market_exposure_dollars": "<string>",\
          "realized_pnl": 123,\
          "realized_pnl_dollars": "<string>",\
          "resting_orders_count": 123,\
          "fees_paid": 123,\
          "fees_paid_dollars": "<string>",\
          "last_updated_ts": "2023-11-07T05:31:56Z"\
        }\
      ],
      "event_positions": [\
        {\
          "event_ticker": "<string>",\
          "total_cost": 123,\
          "total_cost_dollars": "<string>",\
          "event_exposure": 123,\
          "event_exposure_dollars": "<string>",\
          "realized_pnl": 123,\
          "realized_pnl_dollars": "<string>",\
          "resting_order_count": 123,\
          "fees_paid": 123,\
          "fees_paid_dollars": "<string>"\
        }\
      ]
    }

GET

/

portfolio

/

positions

Try it

Get Positions

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/portfolio/positions \
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
      "cursor": "<string>",
      "market_positions": [\
        {\
          "ticker": "<string>",\
          "total_traded": 123,\
          "total_traded_dollars": "<string>",\
          "position": 123,\
          "market_exposure": 123,\
          "market_exposure_dollars": "<string>",\
          "realized_pnl": 123,\
          "realized_pnl_dollars": "<string>",\
          "resting_orders_count": 123,\
          "fees_paid": 123,\
          "fees_paid_dollars": "<string>",\
          "last_updated_ts": "2023-11-07T05:31:56Z"\
        }\
      ],
      "event_positions": [\
        {\
          "event_ticker": "<string>",\
          "total_cost": 123,\
          "total_cost_dollars": "<string>",\
          "event_exposure": 123,\
          "event_exposure_dollars": "<string>",\
          "realized_pnl": 123,\
          "realized_pnl_dollars": "<string>",\
          "resting_order_count": 123,\
          "fees_paid": 123,\
          "fees_paid_dollars": "<string>"\
        }\
      ]
    }

#### Authorizations

[​](https://docs.kalshi.com/api-reference/portfolio/get-positions#authorization-kalshi-access-key)

KALSHI-ACCESS-KEY

string

header

required

Your API key ID

[​](https://docs.kalshi.com/api-reference/portfolio/get-positions#authorization-kalshi-access-signature)

KALSHI-ACCESS-SIGNATURE

string

header

required

RSA-PSS signature of the request

[​](https://docs.kalshi.com/api-reference/portfolio/get-positions#authorization-kalshi-access-timestamp)

KALSHI-ACCESS-TIMESTAMP

string

header

required

Request timestamp in milliseconds

#### Query Parameters

[​](https://docs.kalshi.com/api-reference/portfolio/get-positions#parameter-cursor)

cursor

string

The Cursor represents a pointer to the next page of records in the pagination. Use the value returned from the previous response to get the next page.

[​](https://docs.kalshi.com/api-reference/portfolio/get-positions#parameter-limit)

limit

integer

default:100

Parameter to specify the number of results per page. Defaults to 100.

Required range: `1 <= x <= 1000`

[​](https://docs.kalshi.com/api-reference/portfolio/get-positions#parameter-count-filter)

count\_filter

string

Restricts the positions to those with any of following fields with non-zero values, as a comma separated list. The following values are accepted - position, total\_traded, resting\_order\_count

[​](https://docs.kalshi.com/api-reference/portfolio/get-positions#parameter-settlement-status)

settlement\_status

enum<string>

default:unsettled

Settlement status of the markets to return. Defaults to unsettled.

Available options:

`all`,

`unsettled`,

`settled`

[​](https://docs.kalshi.com/api-reference/portfolio/get-positions#parameter-ticker)

ticker

string

Filter by market ticker

[​](https://docs.kalshi.com/api-reference/portfolio/get-positions#parameter-event-ticker)

event\_ticker

string

Event ticker of desired positions. Multiple event tickers can be provided as a comma-separated list (maximum 10).

#### Response

200

application/json

Positions retrieved successfully

[​](https://docs.kalshi.com/api-reference/portfolio/get-positions#response-cursor)

cursor

string

The Cursor represents a pointer to the next page of records in the pagination. Use the value returned here in the cursor query parameter for this end-point to get the next page containing limit records. An empty value of this field indicates there is no next page.

[​](https://docs.kalshi.com/api-reference/portfolio/get-positions#response-market-positions)

market\_positions

object\[\]

List of market positions

Show child attributes

[​](https://docs.kalshi.com/api-reference/portfolio/get-positions#response-event-positions)

event\_positions

object\[\]

List of event positions

Show child attributes

[Get Balance](https://docs.kalshi.com/api-reference/portfolio/get-balance)
[Get Settlements](https://docs.kalshi.com/api-reference/portfolio/get-settlements)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.