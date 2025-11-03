---
url: https://docs.kalshi.com/api-reference/communications/create-rfq
title: Create RFQ - API Documentation
description:  Endpoint for creating a new RFQ. You can have a maximum of 100 open RFQs at a time.
scraped_at: 2025-11-03T14:46:09.344533
---

[Skip to main content](https://docs.kalshi.com/api-reference/communications/create-rfq#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

communications

Create RFQ

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Create RFQ

cURL

Copy

Ask AI

    curl --request POST \
      --url https://api.elections.kalshi.com/trade-api/v2/communications/rfqs \
      --header 'Content-Type: application/json' \
      --header 'KALSHI-ACCESS-KEY: <api-key>' \
      --header 'KALSHI-ACCESS-SIGNATURE: <api-key>' \
      --header 'KALSHI-ACCESS-TIMESTAMP: <api-key>' \
      --data '{
      "market_ticker": "<string>",
      "contracts": 123,
      "target_cost_centi_cents": 123,
      "rest_remainder": true
    }'

201

400

401

409

500

Copy

Ask AI

    {
      "id": "<string>"
    }

POST

/

communications

/

rfqs

Try it

Create RFQ

cURL

Copy

Ask AI

    curl --request POST \
      --url https://api.elections.kalshi.com/trade-api/v2/communications/rfqs \
      --header 'Content-Type: application/json' \
      --header 'KALSHI-ACCESS-KEY: <api-key>' \
      --header 'KALSHI-ACCESS-SIGNATURE: <api-key>' \
      --header 'KALSHI-ACCESS-TIMESTAMP: <api-key>' \
      --data '{
      "market_ticker": "<string>",
      "contracts": 123,
      "target_cost_centi_cents": 123,
      "rest_remainder": true
    }'

201

400

401

409

500

Copy

Ask AI

    {
      "id": "<string>"
    }

#### Authorizations

[​](https://docs.kalshi.com/api-reference/communications/create-rfq#authorization-kalshi-access-key)

KALSHI-ACCESS-KEY

string

header

required

Your API key ID

[​](https://docs.kalshi.com/api-reference/communications/create-rfq#authorization-kalshi-access-signature)

KALSHI-ACCESS-SIGNATURE

string

header

required

RSA-PSS signature of the request

[​](https://docs.kalshi.com/api-reference/communications/create-rfq#authorization-kalshi-access-timestamp)

KALSHI-ACCESS-TIMESTAMP

string

header

required

Request timestamp in milliseconds

#### Body

application/json

[​](https://docs.kalshi.com/api-reference/communications/create-rfq#body-market-ticker)

market\_ticker

string

required

The ticker of the market for which to create an RFQ

[​](https://docs.kalshi.com/api-reference/communications/create-rfq#body-rest-remainder)

rest\_remainder

boolean

required

Whether to rest the remainder of the RFQ after execution

[​](https://docs.kalshi.com/api-reference/communications/create-rfq#body-contracts)

contracts

integer

The number of contracts for the RFQ

[​](https://docs.kalshi.com/api-reference/communications/create-rfq#body-target-cost-centi-cents)

target\_cost\_centi\_cents

integer

The target cost for the RFQ in centi-cents

#### Response

201

application/json

RFQ created successfully

[​](https://docs.kalshi.com/api-reference/communications/create-rfq#response-id)

id

string

required

The ID of the newly created RFQ

[Get RFQs](https://docs.kalshi.com/api-reference/communications/get-rfqs)
[Get RFQ](https://docs.kalshi.com/api-reference/communications/get-rfq)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.