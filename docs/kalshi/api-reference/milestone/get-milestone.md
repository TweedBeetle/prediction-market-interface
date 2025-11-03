---
url: https://docs.kalshi.com/api-reference/milestone/get-milestone
title: Get Milestone - API Documentation
description:  Endpoint for getting data about a specific milestone by its ID.
scraped_at: 2025-11-03T14:46:20.827052
---

[Skip to main content](https://docs.kalshi.com/api-reference/milestone/get-milestone#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

milestone

Get Milestone

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Get Milestone

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/milestones/{milestone_id}

200

400

401

404

500

Copy

Ask AI

    {
      "milestone": {
        "id": "<string>",
        "category": "<string>",
        "type": "<string>",
        "start_date": "2023-11-07T05:31:56Z",
        "end_date": "2023-11-07T05:31:56Z",
        "related_event_tickers": [\
          "<string>"\
        ],
        "title": "<string>",
        "notification_message": "<string>",
        "source_id": "<string>",
        "details": {},
        "primary_event_tickers": [\
          "<string>"\
        ],
        "last_updated_ts": "2023-11-07T05:31:56Z"
      }
    }

GET

/

milestones

/

{milestone\_id}

Try it

Get Milestone

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/milestones/{milestone_id}

200

400

401

404

500

Copy

Ask AI

    {
      "milestone": {
        "id": "<string>",
        "category": "<string>",
        "type": "<string>",
        "start_date": "2023-11-07T05:31:56Z",
        "end_date": "2023-11-07T05:31:56Z",
        "related_event_tickers": [\
          "<string>"\
        ],
        "title": "<string>",
        "notification_message": "<string>",
        "source_id": "<string>",
        "details": {},
        "primary_event_tickers": [\
          "<string>"\
        ],
        "last_updated_ts": "2023-11-07T05:31:56Z"
      }
    }

#### Path Parameters

[​](https://docs.kalshi.com/api-reference/milestone/get-milestone#parameter-milestone-id)

milestone\_id

string

required

Milestone ID

#### Response

200

application/json

Milestone retrieved successfully

[​](https://docs.kalshi.com/api-reference/milestone/get-milestone#response-milestone)

milestone

object

required

The milestone data.

Show child attributes

[​](https://docs.kalshi.com/api-reference/milestone/get-milestone#response-milestone-id)

milestone.id

string

required

Unique identifier for the milestone.

[​](https://docs.kalshi.com/api-reference/milestone/get-milestone#response-milestone-category)

milestone.category

string

required

Category of the milestone.

[​](https://docs.kalshi.com/api-reference/milestone/get-milestone#response-milestone-type)

milestone.type

string

required

Type of the milestone.

[​](https://docs.kalshi.com/api-reference/milestone/get-milestone#response-milestone-start-date)

milestone.start\_date

string<date-time>

required

Start date of the milestone.

[​](https://docs.kalshi.com/api-reference/milestone/get-milestone#response-milestone-related-event-tickers)

milestone.related\_event\_tickers

string\[\]

required

List of event tickers related to this milestone.

[​](https://docs.kalshi.com/api-reference/milestone/get-milestone#response-milestone-title)

milestone.title

string

required

Title of the milestone.

[​](https://docs.kalshi.com/api-reference/milestone/get-milestone#response-milestone-notification-message)

milestone.notification\_message

string

required

Notification message for the milestone.

[​](https://docs.kalshi.com/api-reference/milestone/get-milestone#response-milestone-details)

milestone.details

object

required

Additional details about the milestone.

[​](https://docs.kalshi.com/api-reference/milestone/get-milestone#response-milestone-primary-event-tickers)

milestone.primary\_event\_tickers

string\[\]

required

List of event tickers directly related to the outcome of this milestone.

[​](https://docs.kalshi.com/api-reference/milestone/get-milestone#response-milestone-last-updated-ts)

milestone.last\_updated\_ts

string<date-time>

required

Last time this structured target was updated.

[​](https://docs.kalshi.com/api-reference/milestone/get-milestone#response-milestone-end-date)

milestone.end\_date

string<date-time> | null

End date of the milestone, if any.

[​](https://docs.kalshi.com/api-reference/milestone/get-milestone#response-milestone-source-id)

milestone.source\_id

string | null

Source id of milestone if available.

[Get Structured Target](https://docs.kalshi.com/api-reference/structured-targets/get-structured-target)
[Get Milestones](https://docs.kalshi.com/api-reference/milestone/get-milestones)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.