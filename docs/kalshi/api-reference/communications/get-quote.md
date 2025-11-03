---
url: https://docs.kalshi.com/api-reference/communications/get-quote
title: Get Quote - API Documentation
description:  Endpoint for getting a particular quote
scraped_at: 2025-11-03T14:46:07.578134
---

[Skip to main content](https://docs.kalshi.com/api-reference/communications/get-quote#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

communications

Get Quote

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Get Quote

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/communications/quotes/{quote_id} \
      --header 'KALSHI-ACCESS-KEY: <api-key>' \
      --header 'KALSHI-ACCESS-SIGNATURE: <api-key>' \
      --header 'KALSHI-ACCESS-TIMESTAMP: <api-key>'

200

401

404

500

Copy

Ask AI

    {
      "quote": {
        "id": "<string>",
        "rfq_id": "<string>",
        "creator_id": "<string>",
        "rfq_creator_id": "<string>",
        "market_ticker": "<string>",
        "contracts": 123,
        "yes_bid": 123,
        "no_bid": 123,
        "created_ts": "2023-11-07T05:31:56Z",
        "updated_ts": "2023-11-07T05:31:56Z",
        "status": "open",
        "accepted_side": "yes",
        "accepted_ts": "2023-11-07T05:31:56Z",
        "confirmed_ts": "2023-11-07T05:31:56Z",
        "executed_ts": "2023-11-07T05:31:56Z",
        "cancelled_ts": "2023-11-07T05:31:56Z",
        "rest_remainder": true,
        "cancellation_reason": "<string>",
        "creator_user_id": "<string>",
        "rfq_creator_user_id": "<string>",
        "expired_ts": "2023-11-07T05:31:56Z",
        "rfq_target_cost_centi_cents": 123,
        "rfq_creator_order_id": "<string>",
        "creator_order_id": "<string>"
      }
    }

GET

/

communications

/

quotes

/

{quote\_id}

Try it

Get Quote

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/communications/quotes/{quote_id} \
      --header 'KALSHI-ACCESS-KEY: <api-key>' \
      --header 'KALSHI-ACCESS-SIGNATURE: <api-key>' \
      --header 'KALSHI-ACCESS-TIMESTAMP: <api-key>'

200

401

404

500

Copy

Ask AI

    {
      "quote": {
        "id": "<string>",
        "rfq_id": "<string>",
        "creator_id": "<string>",
        "rfq_creator_id": "<string>",
        "market_ticker": "<string>",
        "contracts": 123,
        "yes_bid": 123,
        "no_bid": 123,
        "created_ts": "2023-11-07T05:31:56Z",
        "updated_ts": "2023-11-07T05:31:56Z",
        "status": "open",
        "accepted_side": "yes",
        "accepted_ts": "2023-11-07T05:31:56Z",
        "confirmed_ts": "2023-11-07T05:31:56Z",
        "executed_ts": "2023-11-07T05:31:56Z",
        "cancelled_ts": "2023-11-07T05:31:56Z",
        "rest_remainder": true,
        "cancellation_reason": "<string>",
        "creator_user_id": "<string>",
        "rfq_creator_user_id": "<string>",
        "expired_ts": "2023-11-07T05:31:56Z",
        "rfq_target_cost_centi_cents": 123,
        "rfq_creator_order_id": "<string>",
        "creator_order_id": "<string>"
      }
    }

#### Authorizations

[​](https://docs.kalshi.com/api-reference/communications/get-quote#authorization-kalshi-access-key)

KALSHI-ACCESS-KEY

string

header

required

Your API key ID

[​](https://docs.kalshi.com/api-reference/communications/get-quote#authorization-kalshi-access-signature)

KALSHI-ACCESS-SIGNATURE

string

header

required

RSA-PSS signature of the request

[​](https://docs.kalshi.com/api-reference/communications/get-quote#authorization-kalshi-access-timestamp)

KALSHI-ACCESS-TIMESTAMP

string

header

required

Request timestamp in milliseconds

#### Path Parameters

[​](https://docs.kalshi.com/api-reference/communications/get-quote#parameter-quote-id)

quote\_id

string

required

Quote ID

#### Response

200

application/json

Quote retrieved successfully

[​](https://docs.kalshi.com/api-reference/communications/get-quote#response-quote)

quote

object

required

The details of the requested quote

Show child attributes

[Create Quote](https://docs.kalshi.com/api-reference/communications/create-quote)
[Delete Quote](https://docs.kalshi.com/api-reference/communications/delete-quote)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.