---
url: https://docs.kalshi.com/api-reference/communications/get-quotes
title: Get Quotes - API Documentation
description:  Endpoint for getting quotes
scraped_at: 2025-11-03T14:46:09.093197
---

[Skip to main content](https://docs.kalshi.com/api-reference/communications/get-quotes#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

communications

Get Quotes

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Get Quotes

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/communications/quotes \
      --header 'KALSHI-ACCESS-KEY: <api-key>' \
      --header 'KALSHI-ACCESS-SIGNATURE: <api-key>' \
      --header 'KALSHI-ACCESS-TIMESTAMP: <api-key>'

200

401

500

Copy

Ask AI

    {
      "quotes": [\
        {\
          "id": "<string>",\
          "rfq_id": "<string>",\
          "creator_id": "<string>",\
          "rfq_creator_id": "<string>",\
          "market_ticker": "<string>",\
          "contracts": 123,\
          "yes_bid": 123,\
          "no_bid": 123,\
          "created_ts": "2023-11-07T05:31:56Z",\
          "updated_ts": "2023-11-07T05:31:56Z",\
          "status": "open",\
          "accepted_side": "yes",\
          "accepted_ts": "2023-11-07T05:31:56Z",\
          "confirmed_ts": "2023-11-07T05:31:56Z",\
          "executed_ts": "2023-11-07T05:31:56Z",\
          "cancelled_ts": "2023-11-07T05:31:56Z",\
          "rest_remainder": true,\
          "cancellation_reason": "<string>",\
          "creator_user_id": "<string>",\
          "rfq_creator_user_id": "<string>",\
          "expired_ts": "2023-11-07T05:31:56Z",\
          "rfq_target_cost_centi_cents": 123,\
          "rfq_creator_order_id": "<string>",\
          "creator_order_id": "<string>"\
        }\
      ],
      "cursor": "<string>"
    }

GET

/

communications

/

quotes

Try it

Get Quotes

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/communications/quotes \
      --header 'KALSHI-ACCESS-KEY: <api-key>' \
      --header 'KALSHI-ACCESS-SIGNATURE: <api-key>' \
      --header 'KALSHI-ACCESS-TIMESTAMP: <api-key>'

200

401

500

Copy

Ask AI

    {
      "quotes": [\
        {\
          "id": "<string>",\
          "rfq_id": "<string>",\
          "creator_id": "<string>",\
          "rfq_creator_id": "<string>",\
          "market_ticker": "<string>",\
          "contracts": 123,\
          "yes_bid": 123,\
          "no_bid": 123,\
          "created_ts": "2023-11-07T05:31:56Z",\
          "updated_ts": "2023-11-07T05:31:56Z",\
          "status": "open",\
          "accepted_side": "yes",\
          "accepted_ts": "2023-11-07T05:31:56Z",\
          "confirmed_ts": "2023-11-07T05:31:56Z",\
          "executed_ts": "2023-11-07T05:31:56Z",\
          "cancelled_ts": "2023-11-07T05:31:56Z",\
          "rest_remainder": true,\
          "cancellation_reason": "<string>",\
          "creator_user_id": "<string>",\
          "rfq_creator_user_id": "<string>",\
          "expired_ts": "2023-11-07T05:31:56Z",\
          "rfq_target_cost_centi_cents": 123,\
          "rfq_creator_order_id": "<string>",\
          "creator_order_id": "<string>"\
        }\
      ],
      "cursor": "<string>"
    }

#### Authorizations

[​](https://docs.kalshi.com/api-reference/communications/get-quotes#authorization-kalshi-access-key)

KALSHI-ACCESS-KEY

string

header

required

Your API key ID

[​](https://docs.kalshi.com/api-reference/communications/get-quotes#authorization-kalshi-access-signature)

KALSHI-ACCESS-SIGNATURE

string

header

required

RSA-PSS signature of the request

[​](https://docs.kalshi.com/api-reference/communications/get-quotes#authorization-kalshi-access-timestamp)

KALSHI-ACCESS-TIMESTAMP

string

header

required

Request timestamp in milliseconds

#### Query Parameters

[​](https://docs.kalshi.com/api-reference/communications/get-quotes#parameter-cursor)

cursor

string

The cursor represents a pointer to the next page of records in the pagination

[​](https://docs.kalshi.com/api-reference/communications/get-quotes#parameter-limit)

limit

integer

default:500

Parameter to specify the number of results per page. Defaults to 500.

Required range: `1 <= x <= 500`

[​](https://docs.kalshi.com/api-reference/communications/get-quotes#parameter-market-ticker)

market\_ticker

string

Filter quotes by market ticker

[​](https://docs.kalshi.com/api-reference/communications/get-quotes#parameter-event-ticker)

event\_ticker

string

Filter quotes by event ticker

[​](https://docs.kalshi.com/api-reference/communications/get-quotes#parameter-status)

status

string

Filter quotes by status

[​](https://docs.kalshi.com/api-reference/communications/get-quotes#parameter-quote-creator-user-id)

quote\_creator\_user\_id

string

Filter quotes by quote creator user ID

[​](https://docs.kalshi.com/api-reference/communications/get-quotes#parameter-rfq-creator-user-id)

rfq\_creator\_user\_id

string

Filter quotes by RFQ creator user ID

[​](https://docs.kalshi.com/api-reference/communications/get-quotes#parameter-rfq-id)

rfq\_id

string

Filter quotes by RFQ ID

#### Response

200

application/json

Quotes retrieved successfully

[​](https://docs.kalshi.com/api-reference/communications/get-quotes#response-quotes)

quotes

object\[\]

required

List of quotes matching the query criteria

Show child attributes

[​](https://docs.kalshi.com/api-reference/communications/get-quotes#response-cursor)

cursor

string

Cursor for pagination to get the next page of results

[Delete RFQ](https://docs.kalshi.com/api-reference/communications/delete-rfq)
[Create Quote](https://docs.kalshi.com/api-reference/communications/create-quote)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.