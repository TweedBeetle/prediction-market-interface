---
url: https://docs.kalshi.com/api-reference/communications/confirm-quote
title: Confirm Quote - API Documentation
description:  Endpoint for confirming a quote. This will start a timer for order execution
scraped_at: 2025-11-03T14:46:09.097290
---

[Skip to main content](https://docs.kalshi.com/api-reference/communications/confirm-quote#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

communications

Confirm Quote

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Confirm Quote

cURL

Copy

Ask AI

    curl --request PUT \
      --url https://api.elections.kalshi.com/trade-api/v2/communications/quotes/{quote_id}/confirm \
      --header 'KALSHI-ACCESS-KEY: <api-key>' \
      --header 'KALSHI-ACCESS-SIGNATURE: <api-key>' \
      --header 'KALSHI-ACCESS-TIMESTAMP: <api-key>'

204

401

404

500

Copy

Ask AI

    This response does not have an example.

PUT

/

communications

/

quotes

/

{quote\_id}

/

confirm

Try it

Confirm Quote

cURL

Copy

Ask AI

    curl --request PUT \
      --url https://api.elections.kalshi.com/trade-api/v2/communications/quotes/{quote_id}/confirm \
      --header 'KALSHI-ACCESS-KEY: <api-key>' \
      --header 'KALSHI-ACCESS-SIGNATURE: <api-key>' \
      --header 'KALSHI-ACCESS-TIMESTAMP: <api-key>'

204

401

404

500

Copy

Ask AI

    This response does not have an example.

#### Authorizations

[​](https://docs.kalshi.com/api-reference/communications/confirm-quote#authorization-kalshi-access-key)

KALSHI-ACCESS-KEY

string

header

required

Your API key ID

[​](https://docs.kalshi.com/api-reference/communications/confirm-quote#authorization-kalshi-access-signature)

KALSHI-ACCESS-SIGNATURE

string

header

required

RSA-PSS signature of the request

[​](https://docs.kalshi.com/api-reference/communications/confirm-quote#authorization-kalshi-access-timestamp)

KALSHI-ACCESS-TIMESTAMP

string

header

required

Request timestamp in milliseconds

#### Path Parameters

[​](https://docs.kalshi.com/api-reference/communications/confirm-quote#parameter-quote-id)

quote\_id

string

required

Quote ID

#### Response

204

Quote confirmed successfully

[Accept Quote](https://docs.kalshi.com/api-reference/communications/accept-quote)
[Get Multivariate Event Collection](https://docs.kalshi.com/api-reference/collection/get-multivariate-event-collection)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.