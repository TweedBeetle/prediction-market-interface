---
url: https://docs.kalshi.com/api-reference/exchange/get-exchange-announcements
title: Get Exchange Announcements - API Documentation
description:  Endpoint for getting all exchange-wide announcements.
scraped_at: 2025-11-03T14:46:15.758756
---

[Skip to main content](https://docs.kalshi.com/api-reference/exchange/get-exchange-announcements#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

exchange

Get Exchange Announcements

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Get Exchange Announcements

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/exchange/announcements

200

500

Copy

Ask AI

    {
      "announcements": [\
        {\
          "type": "info",\
          "message": "<string>",\
          "delivery_time": "2023-11-07T05:31:56Z",\
          "status": "active"\
        }\
      ]
    }

GET

/

exchange

/

announcements

Try it

Get Exchange Announcements

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/exchange/announcements

200

500

Copy

Ask AI

    {
      "announcements": [\
        {\
          "type": "info",\
          "message": "<string>",\
          "delivery_time": "2023-11-07T05:31:56Z",\
          "status": "active"\
        }\
      ]
    }

#### Response

200

application/json

Exchange announcements retrieved successfully

[​](https://docs.kalshi.com/api-reference/exchange/get-exchange-announcements#response-announcements)

announcements

object\[\]

required

A list of exchange-wide announcements.

Show child attributes

[​](https://docs.kalshi.com/api-reference/exchange/get-exchange-announcements#response-announcements-type)

type

enum<string>

required

The type of the announcement.

Available options:

`info`,

`warning`,

`error`

[​](https://docs.kalshi.com/api-reference/exchange/get-exchange-announcements#response-announcements-message)

message

string

required

The message contained within the announcement.

[​](https://docs.kalshi.com/api-reference/exchange/get-exchange-announcements#response-announcements-delivery-time)

delivery\_time

string<date-time>

required

The time the announcement was delivered.

[​](https://docs.kalshi.com/api-reference/exchange/get-exchange-announcements#response-announcements-status)

status

enum<string>

required

The current status of this announcement.

Available options:

`active`,

`inactive`

[Get Exchange Status](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Get Series Fee Changes](https://docs.kalshi.com/api-reference/exchange/get-series-fee-changes)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.