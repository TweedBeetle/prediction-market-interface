---
url: https://docs.kalshi.com/api-reference/communications/get-rfq
title: Get RFQ - API Documentation
description:  Endpoint for getting a single RFQ by id
scraped_at: 2025-11-03T14:46:09.342082
---

[Skip to main content](https://docs.kalshi.com/api-reference/communications/get-rfq#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

communications

Get RFQ

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Get RFQ

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/communications/rfqs/{rfq_id} \
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
      "rfq": {
        "id": "<string>",
        "creator_id": "<string>",
        "market_ticker": "<string>",
        "contracts": 123,
        "target_cost_centi_cents": 123,
        "status": "open",
        "created_ts": "2023-11-07T05:31:56Z",
        "mve_collection_ticker": "<string>",
        "mve_selected_legs": [\
          {\
            "event_ticker": "<string>",\
            "market_ticker": "<string>",\
            "side": "<string>"\
          }\
        ],
        "rest_remainder": true,
        "cancellation_reason": "<string>",
        "creator_user_id": "<string>",
        "cancelled_ts": "2023-11-07T05:31:56Z",
        "updated_ts": "2023-11-07T05:31:56Z"
      }
    }

GET

/

communications

/

rfqs

/

{rfq\_id}

Try it

Get RFQ

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/communications/rfqs/{rfq_id} \
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
      "rfq": {
        "id": "<string>",
        "creator_id": "<string>",
        "market_ticker": "<string>",
        "contracts": 123,
        "target_cost_centi_cents": 123,
        "status": "open",
        "created_ts": "2023-11-07T05:31:56Z",
        "mve_collection_ticker": "<string>",
        "mve_selected_legs": [\
          {\
            "event_ticker": "<string>",\
            "market_ticker": "<string>",\
            "side": "<string>"\
          }\
        ],
        "rest_remainder": true,
        "cancellation_reason": "<string>",
        "creator_user_id": "<string>",
        "cancelled_ts": "2023-11-07T05:31:56Z",
        "updated_ts": "2023-11-07T05:31:56Z"
      }
    }

#### Authorizations

[​](https://docs.kalshi.com/api-reference/communications/get-rfq#authorization-kalshi-access-key)

KALSHI-ACCESS-KEY

string

header

required

Your API key ID

[​](https://docs.kalshi.com/api-reference/communications/get-rfq#authorization-kalshi-access-signature)

KALSHI-ACCESS-SIGNATURE

string

header

required

RSA-PSS signature of the request

[​](https://docs.kalshi.com/api-reference/communications/get-rfq#authorization-kalshi-access-timestamp)

KALSHI-ACCESS-TIMESTAMP

string

header

required

Request timestamp in milliseconds

#### Path Parameters

[​](https://docs.kalshi.com/api-reference/communications/get-rfq#parameter-rfq-id)

rfq\_id

string

required

RFQ ID

#### Response

200

application/json

RFQ retrieved successfully

[​](https://docs.kalshi.com/api-reference/communications/get-rfq#response-rfq)

rfq

object

required

The details of the requested RFQ

Show child attributes

[Create RFQ](https://docs.kalshi.com/api-reference/communications/create-rfq)
[Delete RFQ](https://docs.kalshi.com/api-reference/communications/delete-rfq)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.