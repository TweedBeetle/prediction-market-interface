---
url: https://docs.kalshi.com/api-reference/incentive_programs/get-volume-incentives
title: Get Volume Incentives - API Documentation
description:  List volume incentives with optional filters. Volume incentives are rewards programs for trading activity on specific markets.
scraped_at: 2025-11-03T14:46:19.285770
---

[Skip to main content](https://docs.kalshi.com/api-reference/incentive_programs/get-volume-incentives#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

incentive\_programs

Get Volume Incentives

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Get Volume Incentives

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/incentive_programs

200

400

500

Copy

Ask AI

    {
      "incentive_programs": [\
        {\
          "id": "<string>",\
          "market_ticker": "<string>",\
          "incentive_type": "liquidity",\
          "start_date": "2023-11-07T05:31:56Z",\
          "end_date": "2023-11-07T05:31:56Z",\
          "period_reward": 123,\
          "paid_out": true,\
          "discount_factor_bps": 123,\
          "target_size": 123\
        }\
      ],
      "next_cursor": "<string>"
    }

GET

/

incentive\_programs

Try it

Get Volume Incentives

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/incentive_programs

200

400

500

Copy

Ask AI

    {
      "incentive_programs": [\
        {\
          "id": "<string>",\
          "market_ticker": "<string>",\
          "incentive_type": "liquidity",\
          "start_date": "2023-11-07T05:31:56Z",\
          "end_date": "2023-11-07T05:31:56Z",\
          "period_reward": 123,\
          "paid_out": true,\
          "discount_factor_bps": 123,\
          "target_size": 123\
        }\
      ],
      "next_cursor": "<string>"
    }

#### Query Parameters

[​](https://docs.kalshi.com/api-reference/incentive_programs/get-volume-incentives#parameter-status)

status

enum<string>

Status filter. Can be "all", "active", "upcoming", "closed", or "paid\_out". Default is "all".

Available options:

`all`,

`active`,

`upcoming`,

`closed`,

`paid_out`

[​](https://docs.kalshi.com/api-reference/incentive_programs/get-volume-incentives#parameter-type)

type

enum<string>

Type filter. Can be "all", "liquidity", or "volume". Default is "all".

Available options:

`all`,

`liquidity`,

`volume`

[​](https://docs.kalshi.com/api-reference/incentive_programs/get-volume-incentives#parameter-limit)

limit

integer

Number of results per page. Defaults to 100. Maximum value is 10000.

Required range: `1 <= x <= 10000`

[​](https://docs.kalshi.com/api-reference/incentive_programs/get-volume-incentives#parameter-cursor)

cursor

string

Cursor for pagination

#### Response

200

application/json

Incentive programs retrieved successfully

[​](https://docs.kalshi.com/api-reference/incentive_programs/get-volume-incentives#response-incentive-programs)

incentive\_programs

object\[\]

required

Show child attributes

[​](https://docs.kalshi.com/api-reference/incentive_programs/get-volume-incentives#response-next-cursor)

next\_cursor

string

Cursor for pagination to get the next page of results

[Get Multiple Live Data](https://docs.kalshi.com/api-reference/live_data/get-multiple-live-data)
[Get FCM Orders](https://docs.kalshi.com/api-reference/fcm/get-fcm-orders)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.