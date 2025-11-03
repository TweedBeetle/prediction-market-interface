---
url: https://docs.kalshi.com/api-reference/collection/get-multivariate-event-collection
title: Get Multivariate Event Collection - API Documentation
description:  Endpoint for getting data about a multivariate event collection by its ticker.
scraped_at: 2025-11-03T14:46:05.044149
---

[Skip to main content](https://docs.kalshi.com/api-reference/collection/get-multivariate-event-collection#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

collection

Get Multivariate Event Collection

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Get Multivariate Event Collection

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/multivariate_event_collections/{collection_ticker}

200

400

404

500

Copy

Ask AI

    {
      "multivariate_contract": {
        "collection_ticker": "<string>",
        "series_ticker": "<string>",
        "title": "<string>",
        "description": "<string>",
        "open_date": "2023-11-07T05:31:56Z",
        "close_date": "2023-11-07T05:31:56Z",
        "associated_events": [\
          {\
            "ticker": "<string>",\
            "is_yes_only": true,\
            "size_max": 123,\
            "size_min": 123,\
            "active_quoters": [\
              "<string>"\
            ]\
          }\
        ],
        "associated_event_tickers": [\
          "<string>"\
        ],
        "is_ordered": true,
        "is_single_market_per_event": true,
        "is_all_yes": true,
        "size_min": 123,
        "size_max": 123,
        "functional_description": "<string>"
      }
    }

GET

/

multivariate\_event\_collections

/

{collection\_ticker}

Try it

Get Multivariate Event Collection

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/multivariate_event_collections/{collection_ticker}

200

400

404

500

Copy

Ask AI

    {
      "multivariate_contract": {
        "collection_ticker": "<string>",
        "series_ticker": "<string>",
        "title": "<string>",
        "description": "<string>",
        "open_date": "2023-11-07T05:31:56Z",
        "close_date": "2023-11-07T05:31:56Z",
        "associated_events": [\
          {\
            "ticker": "<string>",\
            "is_yes_only": true,\
            "size_max": 123,\
            "size_min": 123,\
            "active_quoters": [\
              "<string>"\
            ]\
          }\
        ],
        "associated_event_tickers": [\
          "<string>"\
        ],
        "is_ordered": true,
        "is_single_market_per_event": true,
        "is_all_yes": true,
        "size_min": 123,
        "size_max": 123,
        "functional_description": "<string>"
      }
    }

#### Path Parameters

[​](https://docs.kalshi.com/api-reference/collection/get-multivariate-event-collection#parameter-collection-ticker)

collection\_ticker

string

required

Collection ticker

#### Response

200

application/json

Collection retrieved successfully

[​](https://docs.kalshi.com/api-reference/collection/get-multivariate-event-collection#response-multivariate-contract)

multivariate\_contract

object

required

The multivariate event collection.

Show child attributes

[​](https://docs.kalshi.com/api-reference/collection/get-multivariate-event-collection#response-multivariate-contract-collection-ticker)

multivariate\_contract.collection\_ticker

string

required

Unique identifier for the collection.

[​](https://docs.kalshi.com/api-reference/collection/get-multivariate-event-collection#response-multivariate-contract-series-ticker)

multivariate\_contract.series\_ticker

string

required

Series associated with the collection. Events produced in the collection will be associated with this series.

[​](https://docs.kalshi.com/api-reference/collection/get-multivariate-event-collection#response-multivariate-contract-title)

multivariate\_contract.title

string

required

Title of the collection.

[​](https://docs.kalshi.com/api-reference/collection/get-multivariate-event-collection#response-multivariate-contract-description)

multivariate\_contract.description

string

required

Short description of the collection.

[​](https://docs.kalshi.com/api-reference/collection/get-multivariate-event-collection#response-multivariate-contract-open-date)

multivariate\_contract.open\_date

string<date-time>

required

The open date of the collection. Before this time, the collection cannot be interacted with.

[​](https://docs.kalshi.com/api-reference/collection/get-multivariate-event-collection#response-multivariate-contract-close-date)

multivariate\_contract.close\_date

string<date-time>

required

The close date of the collection. After this time, the collection cannot be interacted with.

[​](https://docs.kalshi.com/api-reference/collection/get-multivariate-event-collection#response-multivariate-contract-associated-events)

multivariate\_contract.associated\_events

object\[\]

required

List of events with their individual configuration.

Show child attributes

[​](https://docs.kalshi.com/api-reference/collection/get-multivariate-event-collection#response-multivariate-contract-associated-event-tickers)

multivariate\_contract.associated\_event\_tickers

string\[\]

required

\[DEPRECATED - Use associated\_events instead\] A list of events associated with the collection. Markets in these events can be passed as inputs to the Lookup and Create endpoints.

[​](https://docs.kalshi.com/api-reference/collection/get-multivariate-event-collection#response-multivariate-contract-is-ordered)

multivariate\_contract.is\_ordered

boolean

required

Whether the collection is ordered. If true, the order of markets passed into Lookup/Create affects the output. If false, the order does not matter.

[​](https://docs.kalshi.com/api-reference/collection/get-multivariate-event-collection#response-multivariate-contract-is-single-market-per-event)

multivariate\_contract.is\_single\_market\_per\_event

boolean

required

\[DEPRECATED - Use associated\_events instead\] Whether the collection accepts multiple markets from the same event passed into Lookup/Create.

[​](https://docs.kalshi.com/api-reference/collection/get-multivariate-event-collection#response-multivariate-contract-is-all-yes)

multivariate\_contract.is\_all\_yes

boolean

required

\[DEPRECATED - Use associated\_events instead\] Whether the collection requires that only the market side of 'yes' may be used.

[​](https://docs.kalshi.com/api-reference/collection/get-multivariate-event-collection#response-multivariate-contract-size-min)

multivariate\_contract.size\_min

integer

required

The minimum number of markets that must be passed into Lookup/Create (inclusive).

[​](https://docs.kalshi.com/api-reference/collection/get-multivariate-event-collection#response-multivariate-contract-size-max)

multivariate\_contract.size\_max

integer

required

The maximum number of markets that must be passed into Lookup/Create (inclusive).

[​](https://docs.kalshi.com/api-reference/collection/get-multivariate-event-collection#response-multivariate-contract-functional-description)

multivariate\_contract.functional\_description

string

required

A functional description of the collection describing how inputs affect the output.

[Confirm Quote](https://docs.kalshi.com/api-reference/communications/confirm-quote)
[Create Market In Multivariate Event Collection](https://docs.kalshi.com/api-reference/collection/create-market-in-multivariate-event-collection)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.