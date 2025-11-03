---
url: https://docs.kalshi.com/api-reference/communications/get-rfqs
title: Get RFQs - API Documentation
description:  Endpoint for getting RFQs
scraped_at: 2025-11-03T14:46:09.878678
---

[Skip to main content](https://docs.kalshi.com/api-reference/communications/get-rfqs#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

communications

Get RFQs

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Get RFQs

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/communications/rfqs \
      --header 'KALSHI-ACCESS-KEY: <api-key>' \
      --header 'KALSHI-ACCESS-SIGNATURE: <api-key>' \
      --header 'KALSHI-ACCESS-TIMESTAMP: <api-key>'

200

401

500

Copy

Ask AI

    {
      "rfqs": [\
        {\
          "id": "<string>",\
          "creator_id": "<string>",\
          "market_ticker": "<string>",\
          "contracts": 123,\
          "target_cost_centi_cents": 123,\
          "status": "open",\
          "created_ts": "2023-11-07T05:31:56Z",\
          "mve_collection_ticker": "<string>",\
          "mve_selected_legs": [\
            {\
              "event_ticker": "<string>",\
              "market_ticker": "<string>",\
              "side": "<string>"\
            }\
          ],\
          "rest_remainder": true,\
          "cancellation_reason": "<string>",\
          "creator_user_id": "<string>",\
          "cancelled_ts": "2023-11-07T05:31:56Z",\
          "updated_ts": "2023-11-07T05:31:56Z"\
        }\
      ],
      "cursor": "<string>"
    }

GET

/

communications

/

rfqs

Try it

Get RFQs

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/communications/rfqs \
      --header 'KALSHI-ACCESS-KEY: <api-key>' \
      --header 'KALSHI-ACCESS-SIGNATURE: <api-key>' \
      --header 'KALSHI-ACCESS-TIMESTAMP: <api-key>'

200

401

500

Copy

Ask AI

    {
      "rfqs": [\
        {\
          "id": "<string>",\
          "creator_id": "<string>",\
          "market_ticker": "<string>",\
          "contracts": 123,\
          "target_cost_centi_cents": 123,\
          "status": "open",\
          "created_ts": "2023-11-07T05:31:56Z",\
          "mve_collection_ticker": "<string>",\
          "mve_selected_legs": [\
            {\
              "event_ticker": "<string>",\
              "market_ticker": "<string>",\
              "side": "<string>"\
            }\
          ],\
          "rest_remainder": true,\
          "cancellation_reason": "<string>",\
          "creator_user_id": "<string>",\
          "cancelled_ts": "2023-11-07T05:31:56Z",\
          "updated_ts": "2023-11-07T05:31:56Z"\
        }\
      ],
      "cursor": "<string>"
    }

#### Authorizations

[​](https://docs.kalshi.com/api-reference/communications/get-rfqs#authorization-kalshi-access-key)

KALSHI-ACCESS-KEY

string

header

required

Your API key ID

[​](https://docs.kalshi.com/api-reference/communications/get-rfqs#authorization-kalshi-access-signature)

KALSHI-ACCESS-SIGNATURE

string

header

required

RSA-PSS signature of the request

[​](https://docs.kalshi.com/api-reference/communications/get-rfqs#authorization-kalshi-access-timestamp)

KALSHI-ACCESS-TIMESTAMP

string

header

required

Request timestamp in milliseconds

#### Query Parameters

[​](https://docs.kalshi.com/api-reference/communications/get-rfqs#parameter-cursor)

cursor

string

The cursor represents a pointer to the next page of records in the pagination

[​](https://docs.kalshi.com/api-reference/communications/get-rfqs#parameter-limit)

limit

integer

default:100

Parameter to specify the number of results per page. Defaults to 100.

Required range: `1 <= x <= 100`

[​](https://docs.kalshi.com/api-reference/communications/get-rfqs#parameter-market-ticker)

market\_ticker

string

Filter RFQs by market ticker

[​](https://docs.kalshi.com/api-reference/communications/get-rfqs#parameter-event-ticker)

event\_ticker

string

Filter RFQs by event ticker

[​](https://docs.kalshi.com/api-reference/communications/get-rfqs#parameter-status)

status

string

Filter RFQs by status

[​](https://docs.kalshi.com/api-reference/communications/get-rfqs#parameter-creator-user-id)

creator\_user\_id

string

Filter RFQs by creator user ID

#### Response

200

application/json

RFQs retrieved successfully

[​](https://docs.kalshi.com/api-reference/communications/get-rfqs#response-rfqs)

rfqs

object\[\]

required

List of RFQs matching the query criteria

Show child attributes

[​](https://docs.kalshi.com/api-reference/communications/get-rfqs#response-cursor)

cursor

string

Cursor for pagination to get the next page of results

[Get Communications ID](https://docs.kalshi.com/api-reference/communications/get-communications-id)
[Create RFQ](https://docs.kalshi.com/api-reference/communications/create-rfq)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.