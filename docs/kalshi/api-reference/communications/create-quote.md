---
url: https://docs.kalshi.com/api-reference/communications/create-quote
title: Create Quote - API Documentation
description:  Endpoint for creating a quote in response to an RFQ
scraped_at: 2025-11-03T14:46:09.092647
---

[Skip to main content](https://docs.kalshi.com/api-reference/communications/create-quote#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

communications

Create Quote

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Create Quote

cURL

Copy

Ask AI

    curl --request POST \
      --url https://api.elections.kalshi.com/trade-api/v2/communications/quotes \
      --header 'Content-Type: application/json' \
      --header 'KALSHI-ACCESS-KEY: <api-key>' \
      --header 'KALSHI-ACCESS-SIGNATURE: <api-key>' \
      --header 'KALSHI-ACCESS-TIMESTAMP: <api-key>' \
      --data '{
      "rfq_id": "<string>",
      "yes_bid": "<string>",
      "no_bid": "<string>",
      "rest_remainder": true
    }'

201

400

401

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

quotes

Try it

Create Quote

cURL

Copy

Ask AI

    curl --request POST \
      --url https://api.elections.kalshi.com/trade-api/v2/communications/quotes \
      --header 'Content-Type: application/json' \
      --header 'KALSHI-ACCESS-KEY: <api-key>' \
      --header 'KALSHI-ACCESS-SIGNATURE: <api-key>' \
      --header 'KALSHI-ACCESS-TIMESTAMP: <api-key>' \
      --data '{
      "rfq_id": "<string>",
      "yes_bid": "<string>",
      "no_bid": "<string>",
      "rest_remainder": true
    }'

201

400

401

500

Copy

Ask AI

    {
      "id": "<string>"
    }

#### Authorizations

[​](https://docs.kalshi.com/api-reference/communications/create-quote#authorization-kalshi-access-key)

KALSHI-ACCESS-KEY

string

header

required

Your API key ID

[​](https://docs.kalshi.com/api-reference/communications/create-quote#authorization-kalshi-access-signature)

KALSHI-ACCESS-SIGNATURE

string

header

required

RSA-PSS signature of the request

[​](https://docs.kalshi.com/api-reference/communications/create-quote#authorization-kalshi-access-timestamp)

KALSHI-ACCESS-TIMESTAMP

string

header

required

Request timestamp in milliseconds

#### Body

application/json

[​](https://docs.kalshi.com/api-reference/communications/create-quote#body-rfq-id)

rfq\_id

string

required

The ID of the RFQ to quote on

[​](https://docs.kalshi.com/api-reference/communications/create-quote#body-yes-bid)

yes\_bid

string

required

The bid price for YES contracts, in dollars

[​](https://docs.kalshi.com/api-reference/communications/create-quote#body-no-bid)

no\_bid

string

required

The bid price for NO contracts, in dollars

[​](https://docs.kalshi.com/api-reference/communications/create-quote#body-rest-remainder)

rest\_remainder

boolean

required

Whether to rest the remainder of the quote after execution

#### Response

201

application/json

Quote created successfully

[​](https://docs.kalshi.com/api-reference/communications/create-quote#response-id)

id

string

required

The ID of the newly created quote

[Get Quotes](https://docs.kalshi.com/api-reference/communications/get-quotes)
[Get Quote](https://docs.kalshi.com/api-reference/communications/get-quote)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.