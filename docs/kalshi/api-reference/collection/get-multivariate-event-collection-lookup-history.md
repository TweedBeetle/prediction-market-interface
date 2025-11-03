---
url: https://docs.kalshi.com/api-reference/collection/get-multivariate-event-collection-lookup-history
title: Get Multivariate Event Collection Lookup History - API Documentation
description:  Endpoint for retrieving which markets in an event collection were recently looked up.
scraped_at: 2025-11-03T14:46:05.046066
---

[Skip to main content](https://docs.kalshi.com/api-reference/collection/get-multivariate-event-collection-lookup-history#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

collection

Get Multivariate Event Collection Lookup History

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Get Multivariate Event Collection Lookup History

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/multivariate_event_collections/{collection_ticker}/lookup

200

400

500

Copy

Ask AI

    {
      "lookup_points": [\
        {\
          "event_ticker": "<string>",\
          "market_ticker": "<string>",\
          "selected_markets": [\
            {\
              "market_ticker": "<string>",\
              "event_ticker": "<string>",\
              "side": "yes"\
            }\
          ],\
          "last_queried_ts": "2023-11-07T05:31:56Z"\
        }\
      ]
    }

GET

/

multivariate\_event\_collections

/

{collection\_ticker}

/

lookup

Try it

Get Multivariate Event Collection Lookup History

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/multivariate_event_collections/{collection_ticker}/lookup

200

400

500

Copy

Ask AI

    {
      "lookup_points": [\
        {\
          "event_ticker": "<string>",\
          "market_ticker": "<string>",\
          "selected_markets": [\
            {\
              "market_ticker": "<string>",\
              "event_ticker": "<string>",\
              "side": "yes"\
            }\
          ],\
          "last_queried_ts": "2023-11-07T05:31:56Z"\
        }\
      ]
    }

#### Path Parameters

[​](https://docs.kalshi.com/api-reference/collection/get-multivariate-event-collection-lookup-history#parameter-collection-ticker)

collection\_ticker

string

required

Collection ticker

#### Query Parameters

[​](https://docs.kalshi.com/api-reference/collection/get-multivariate-event-collection-lookup-history#parameter-lookback-seconds)

lookback\_seconds

enum<integer>

required

Number of seconds to look back for lookup history. Must be one of 10, 60, 300, or 3600.

Available options:

`10`,

`60`,

`300`,

`3600`

#### Response

200

application/json

Lookup history retrieved successfully

[​](https://docs.kalshi.com/api-reference/collection/get-multivariate-event-collection-lookup-history#response-lookup-points)

lookup\_points

object\[\]

required

List of recent lookup points in the collection.

Show child attributes

[​](https://docs.kalshi.com/api-reference/collection/get-multivariate-event-collection-lookup-history#response-lookup-points-event-ticker)

event\_ticker

string

required

Event ticker for the lookup point.

[​](https://docs.kalshi.com/api-reference/collection/get-multivariate-event-collection-lookup-history#response-lookup-points-market-ticker)

market\_ticker

string

required

Market ticker for the lookup point.

[​](https://docs.kalshi.com/api-reference/collection/get-multivariate-event-collection-lookup-history#response-lookup-points-selected-markets)

selected\_markets

object\[\]

required

Markets that were selected for this lookup.

Show child attributes

[​](https://docs.kalshi.com/api-reference/collection/get-multivariate-event-collection-lookup-history#response-lookup-points-last-queried-ts)

last\_queried\_ts

string<date-time>

required

Timestamp when this lookup was last queried.

[Get Multivariate Event Collections](https://docs.kalshi.com/api-reference/collection/get-multivariate-event-collections)
[Lookup Tickers For Market In Multivariate Event Collection](https://docs.kalshi.com/api-reference/collection/lookup-tickers-for-market-in-multivariate-event-collection)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.