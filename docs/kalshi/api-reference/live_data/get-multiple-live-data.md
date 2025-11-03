---
url: https://docs.kalshi.com/api-reference/live_data/get-multiple-live-data
title: Get Multiple Live Data - API Documentation
description: Get live data for multiple milestones
scraped_at: 2025-11-03T14:46:18.809266
---

[Skip to main content](https://docs.kalshi.com/api-reference/live_data/get-multiple-live-data#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

live\_data

Get Multiple Live Data

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Get Multiple Live Data

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/live_data/batch

200

500

Copy

Ask AI

    {
      "live_datas": [\
        {\
          "type": "<string>",\
          "details": {}\
        }\
      ]
    }

GET

/

live\_data

/

batch

Try it

Get Multiple Live Data

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/live_data/batch

200

500

Copy

Ask AI

    {
      "live_datas": [\
        {\
          "type": "<string>",\
          "details": {}\
        }\
      ]
    }

#### Query Parameters

[​](https://docs.kalshi.com/api-reference/live_data/get-multiple-live-data#parameter-milestone-ids)

milestone\_ids

string\[\]

required

Array of milestone IDs

Maximum length: `100`

#### Response

200

application/json

Live data retrieved successfully

[​](https://docs.kalshi.com/api-reference/live_data/get-multiple-live-data#response-live-datas)

live\_datas

object\[\]

required

Show child attributes

[​](https://docs.kalshi.com/api-reference/live_data/get-multiple-live-data#response-live-datas-type)

type

string

required

Type of live data

[​](https://docs.kalshi.com/api-reference/live_data/get-multiple-live-data#response-live-datas-details)

details

object

required

Live data details as a flexible object

[Get Live Data](https://docs.kalshi.com/api-reference/live_data/get-live-data)
[Get Volume Incentives](https://docs.kalshi.com/api-reference/incentive_programs/get-volume-incentives)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.