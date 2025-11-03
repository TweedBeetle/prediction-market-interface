---
url: https://docs.kalshi.com/api-reference/collection/get-multivariate-event-collections
title: Get Multivariate Event Collections - API Documentation
description:  Endpoint for getting data about multivariate event collections.
scraped_at: 2025-11-03T14:46:05.027035
---

[Skip to main content](https://docs.kalshi.com/api-reference/collection/get-multivariate-event-collections#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

collection

Get Multivariate Event Collections

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Get Multivariate Event Collections

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/multivariate_event_collections

200

400

500

Copy

Ask AI

    {
      "multivariate_contracts": [\
        {\
          "collection_ticker": "<string>",\
          "series_ticker": "<string>",\
          "title": "<string>",\
          "description": "<string>",\
          "open_date": "2023-11-07T05:31:56Z",\
          "close_date": "2023-11-07T05:31:56Z",\
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
          ],\
          "associated_event_tickers": [\
            "<string>"\
          ],\
          "is_ordered": true,\
          "is_single_market_per_event": true,\
          "is_all_yes": true,\
          "size_min": 123,\
          "size_max": 123,\
          "functional_description": "<string>"\
        }\
      ],
      "cursor": "<string>"
    }

GET

/

multivariate\_event\_collections

Try it

Get Multivariate Event Collections

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/multivariate_event_collections

200

400

500

Copy

Ask AI

    {
      "multivariate_contracts": [\
        {\
          "collection_ticker": "<string>",\
          "series_ticker": "<string>",\
          "title": "<string>",\
          "description": "<string>",\
          "open_date": "2023-11-07T05:31:56Z",\
          "close_date": "2023-11-07T05:31:56Z",\
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
          ],\
          "associated_event_tickers": [\
            "<string>"\
          ],\
          "is_ordered": true,\
          "is_single_market_per_event": true,\
          "is_all_yes": true,\
          "size_min": 123,\
          "size_max": 123,\
          "functional_description": "<string>"\
        }\
      ],
      "cursor": "<string>"
    }

#### Query Parameters

[​](https://docs.kalshi.com/api-reference/collection/get-multivariate-event-collections#parameter-status)

status

enum<string>

Only return collections of a certain status. Can be unopened, open, or closed.

Available options:

`unopened`,

`open`,

`closed`

[​](https://docs.kalshi.com/api-reference/collection/get-multivariate-event-collections#parameter-associated-event-ticker)

associated\_event\_ticker

string

Only return collections associated with a particular event ticker.

[​](https://docs.kalshi.com/api-reference/collection/get-multivariate-event-collections#parameter-series-ticker)

series\_ticker

string

Only return collections with a particular series ticker.

[​](https://docs.kalshi.com/api-reference/collection/get-multivariate-event-collections#parameter-limit)

limit

integer

Specify the maximum number of results.

Required range: `1 <= x <= 200`

[​](https://docs.kalshi.com/api-reference/collection/get-multivariate-event-collections#parameter-cursor)

cursor

string

The Cursor represents a pointer to the next page of records in the pagination. This optional parameter, when filled, should be filled with the cursor string returned in a previous request to this end-point.

#### Response

200

application/json

Collections retrieved successfully

[​](https://docs.kalshi.com/api-reference/collection/get-multivariate-event-collections#response-multivariate-contracts)

multivariate\_contracts

object\[\]

required

List of multivariate event collections.

Show child attributes

[​](https://docs.kalshi.com/api-reference/collection/get-multivariate-event-collections#response-cursor)

cursor

string

The Cursor represents a pointer to the next page of records in the pagination. Use the value returned here in the cursor query parameter for this end-point to get the next page containing limit records. An empty value of this field indicates there is no next page.

[Create Market In Multivariate Event Collection](https://docs.kalshi.com/api-reference/collection/create-market-in-multivariate-event-collection)
[Get Multivariate Event Collection Lookup History](https://docs.kalshi.com/api-reference/collection/get-multivariate-event-collection-lookup-history)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.