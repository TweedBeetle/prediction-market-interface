---
url: https://docs.kalshi.com/api-reference/collection/create-market-in-multivariate-event-collection
title: Create Market In Multivariate Event Collection - API Documentation
description:  Endpoint for looking up an individual market in a multivariate event collection. This endpoint must be hit at least once before trading or looking up a market.
scraped_at: 2025-11-03T14:46:05.025259
---

[Skip to main content](https://docs.kalshi.com/api-reference/collection/create-market-in-multivariate-event-collection#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

collection

Create Market In Multivariate Event Collection

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Create Market In Multivariate Event Collection

cURL

Copy

Ask AI

    curl --request POST \
      --url https://api.elections.kalshi.com/trade-api/v2/multivariate_event_collections/{collection_ticker} \
      --header 'Content-Type: application/json' \
      --header 'KALSHI-ACCESS-KEY: <api-key>' \
      --header 'KALSHI-ACCESS-SIGNATURE: <api-key>' \
      --header 'KALSHI-ACCESS-TIMESTAMP: <api-key>' \
      --data '{
      "selected_markets": [\
        {\
          "market_ticker": "<string>",\
          "event_ticker": "<string>",\
          "side": "yes"\
        }\
      ]
    }'

200

400

401

500

Copy

Ask AI

    {
      "event_ticker": "<string>",
      "market_ticker": "<string>"
    }

POST

/

multivariate\_event\_collections

/

{collection\_ticker}

Try it

Create Market In Multivariate Event Collection

cURL

Copy

Ask AI

    curl --request POST \
      --url https://api.elections.kalshi.com/trade-api/v2/multivariate_event_collections/{collection_ticker} \
      --header 'Content-Type: application/json' \
      --header 'KALSHI-ACCESS-KEY: <api-key>' \
      --header 'KALSHI-ACCESS-SIGNATURE: <api-key>' \
      --header 'KALSHI-ACCESS-TIMESTAMP: <api-key>' \
      --data '{
      "selected_markets": [\
        {\
          "market_ticker": "<string>",\
          "event_ticker": "<string>",\
          "side": "yes"\
        }\
      ]
    }'

200

400

401

500

Copy

Ask AI

    {
      "event_ticker": "<string>",
      "market_ticker": "<string>"
    }

#### Authorizations

[​](https://docs.kalshi.com/api-reference/collection/create-market-in-multivariate-event-collection#authorization-kalshi-access-key)

KALSHI-ACCESS-KEY

string

header

required

Your API key ID

[​](https://docs.kalshi.com/api-reference/collection/create-market-in-multivariate-event-collection#authorization-kalshi-access-signature)

KALSHI-ACCESS-SIGNATURE

string

header

required

RSA-PSS signature of the request

[​](https://docs.kalshi.com/api-reference/collection/create-market-in-multivariate-event-collection#authorization-kalshi-access-timestamp)

KALSHI-ACCESS-TIMESTAMP

string

header

required

Request timestamp in milliseconds

#### Path Parameters

[​](https://docs.kalshi.com/api-reference/collection/create-market-in-multivariate-event-collection#parameter-collection-ticker)

collection\_ticker

string

required

Collection ticker

#### Body

application/json

[​](https://docs.kalshi.com/api-reference/collection/create-market-in-multivariate-event-collection#body-selected-markets)

selected\_markets

object\[\]

required

List of selected markets that act as parameters to determine which market is created.

Show child attributes

#### Response

200

application/json

Market created successfully

[​](https://docs.kalshi.com/api-reference/collection/create-market-in-multivariate-event-collection#response-event-ticker)

event\_ticker

string

required

Event ticker for the created market.

[​](https://docs.kalshi.com/api-reference/collection/create-market-in-multivariate-event-collection#response-market-ticker)

market\_ticker

string

required

Market ticker for the created market.

[Get Multivariate Event Collection](https://docs.kalshi.com/api-reference/collection/get-multivariate-event-collection)
[Get Multivariate Event Collections](https://docs.kalshi.com/api-reference/collection/get-multivariate-event-collections)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.