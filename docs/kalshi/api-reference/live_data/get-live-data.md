---
url: https://docs.kalshi.com/api-reference/live_data/get-live-data
title: Get Live Data - API Documentation
description: Get live data for a specific milestone
scraped_at: 2025-11-03T14:46:18.786418
---

[Skip to main content](https://docs.kalshi.com/api-reference/live_data/get-live-data#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

live\_data

Get Live Data

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Get Live Data

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/live_data/{type}/milestone/{milestone_id}

200

404

500

Copy

Ask AI

    {
      "live_data": {
        "type": "<string>",
        "details": {}
      }
    }

GET

/

live\_data

/

{type}

/

milestone

/

{milestone\_id}

Try it

Get Live Data

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/live_data/{type}/milestone/{milestone_id}

200

404

500

Copy

Ask AI

    {
      "live_data": {
        "type": "<string>",
        "details": {}
      }
    }

#### Path Parameters

[​](https://docs.kalshi.com/api-reference/live_data/get-live-data#parameter-type)

type

string

required

Type of live data

[​](https://docs.kalshi.com/api-reference/live_data/get-live-data#parameter-milestone-id)

milestone\_id

string

required

Milestone ID

#### Response

200

application/json

Live data retrieved successfully

[​](https://docs.kalshi.com/api-reference/live_data/get-live-data#response-live-data)

live\_data

object

required

Show child attributes

[​](https://docs.kalshi.com/api-reference/live_data/get-live-data#response-live-data-type)

live\_data.type

string

required

Type of live data

[​](https://docs.kalshi.com/api-reference/live_data/get-live-data#response-live-data-details)

live\_data.details

object

required

Live data details as a flexible object

[Get Event Forecast Percentile History](https://docs.kalshi.com/api-reference/events/get-event-forecast-percentile-history)
[Get Multiple Live Data](https://docs.kalshi.com/api-reference/live_data/get-multiple-live-data)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.