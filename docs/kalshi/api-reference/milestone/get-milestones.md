---
url: https://docs.kalshi.com/api-reference/milestone/get-milestones
title: Get Milestones - API Documentation
description: Minimum start date to filter milestones. Format: RFC3339 timestamp
scraped_at: 2025-11-03T14:46:23.343058
---

[Skip to main content](https://docs.kalshi.com/api-reference/milestone/get-milestones#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

milestone

Get Milestones

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Get Milestones

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/milestones

200

400

401

500

Copy

Ask AI

    {
      "milestones": [\
        {\
          "id": "<string>",\
          "category": "<string>",\
          "type": "<string>",\
          "start_date": "2023-11-07T05:31:56Z",\
          "end_date": "2023-11-07T05:31:56Z",\
          "related_event_tickers": [\
            "<string>"\
          ],\
          "title": "<string>",\
          "notification_message": "<string>",\
          "source_id": "<string>",\
          "details": {},\
          "primary_event_tickers": [\
            "<string>"\
          ],\
          "last_updated_ts": "2023-11-07T05:31:56Z"\
        }\
      ],
      "cursor": "<string>"
    }

GET

/

milestones

Try it

Get Milestones

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/milestones

200

400

401

500

Copy

Ask AI

    {
      "milestones": [\
        {\
          "id": "<string>",\
          "category": "<string>",\
          "type": "<string>",\
          "start_date": "2023-11-07T05:31:56Z",\
          "end_date": "2023-11-07T05:31:56Z",\
          "related_event_tickers": [\
            "<string>"\
          ],\
          "title": "<string>",\
          "notification_message": "<string>",\
          "source_id": "<string>",\
          "details": {},\
          "primary_event_tickers": [\
            "<string>"\
          ],\
          "last_updated_ts": "2023-11-07T05:31:56Z"\
        }\
      ],
      "cursor": "<string>"
    }

#### Query Parameters

[​](https://docs.kalshi.com/api-reference/milestone/get-milestones#parameter-minimum-start-date)

minimum\_start\_date

string<date-time>

Minimum start date to filter milestones. Format RFC3339 timestamp

[​](https://docs.kalshi.com/api-reference/milestone/get-milestones#parameter-category)

category

string

Filter by milestone category

[​](https://docs.kalshi.com/api-reference/milestone/get-milestones#parameter-competition)

competition

string

Filter by competition

[​](https://docs.kalshi.com/api-reference/milestone/get-milestones#parameter-source-id)

source\_id

string

Filter by source id

[​](https://docs.kalshi.com/api-reference/milestone/get-milestones#parameter-type)

type

string

Filter by milestone type

[​](https://docs.kalshi.com/api-reference/milestone/get-milestones#parameter-related-event-ticker)

related\_event\_ticker

string

Filter by related event ticker

[​](https://docs.kalshi.com/api-reference/milestone/get-milestones#parameter-limit)

limit

integer

required

Number of milestones to return per page

Required range: `1 <= x <= 500`

[​](https://docs.kalshi.com/api-reference/milestone/get-milestones#parameter-cursor)

cursor

string

Pagination cursor. Use the cursor value returned from the previous response to get the next page of results

#### Response

200

application/json

Milestones retrieved successfully

[​](https://docs.kalshi.com/api-reference/milestone/get-milestones#response-milestones)

milestones

object\[\]

required

List of milestones.

Show child attributes

[​](https://docs.kalshi.com/api-reference/milestone/get-milestones#response-cursor)

cursor

string

Cursor for pagination.

[Get Milestone](https://docs.kalshi.com/api-reference/milestone/get-milestone)
[Get Communications ID](https://docs.kalshi.com/api-reference/communications/get-communications-id)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.