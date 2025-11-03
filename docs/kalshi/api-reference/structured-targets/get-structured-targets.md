---
url: https://docs.kalshi.com/api-reference/structured-targets/get-structured-targets
title: Get Structured Targets - API Documentation
description: Page size (min: 1, max: 2000)
scraped_at: 2025-11-03T14:46:33.699629
---

[Skip to main content](https://docs.kalshi.com/api-reference/structured-targets/get-structured-targets#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

structured-targets

Get Structured Targets

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Get Structured Targets

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/structured_targets

200

401

500

Copy

Ask AI

    {
      "structured_targets": [\
        {\
          "id": "<string>",\
          "name": "<string>",\
          "type": "<string>",\
          "details": {},\
          "source_id": "<string>",\
          "last_updated_ts": "2023-11-07T05:31:56Z"\
        }\
      ],
      "cursor": "<string>"
    }

GET

/

structured\_targets

Try it

Get Structured Targets

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/structured_targets

200

401

500

Copy

Ask AI

    {
      "structured_targets": [\
        {\
          "id": "<string>",\
          "name": "<string>",\
          "type": "<string>",\
          "details": {},\
          "source_id": "<string>",\
          "last_updated_ts": "2023-11-07T05:31:56Z"\
        }\
      ],
      "cursor": "<string>"
    }

#### Query Parameters

[​](https://docs.kalshi.com/api-reference/structured-targets/get-structured-targets#parameter-type)

type

string

Filter by structured target type

[​](https://docs.kalshi.com/api-reference/structured-targets/get-structured-targets#parameter-competition)

competition

string

Filter by competition

[​](https://docs.kalshi.com/api-reference/structured-targets/get-structured-targets#parameter-page-size)

page\_size

integer

default:100

Number of items per page (min 1, max 2000, default 100)

Required range: `1 <= x <= 2000`

[​](https://docs.kalshi.com/api-reference/structured-targets/get-structured-targets#parameter-cursor)

cursor

string

Pagination cursor

#### Response

200

application/json

Structured targets retrieved successfully

[​](https://docs.kalshi.com/api-reference/structured-targets/get-structured-targets#response-structured-targets)

structured\_targets

object\[\]

Show child attributes

[​](https://docs.kalshi.com/api-reference/structured-targets/get-structured-targets#response-cursor)

cursor

string

Pagination cursor for the next page. Empty if there are no more results.

[Get FCM Positions](https://docs.kalshi.com/api-reference/fcm/get-fcm-positions)
[Get Structured Target](https://docs.kalshi.com/api-reference/structured-targets/get-structured-target)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.