---
url: https://docs.kalshi.com/api-reference/events/get-multivariate-events
title: Get Multivariate Events - API Documentation
description: Retrieve multivariate (combo) events. These are dynamically created events from multivariate event collections. Supports filtering by series and collection ticker.
scraped_at: 2025-11-03T14:46:16.267279
---

[Skip to main content](https://docs.kalshi.com/api-reference/events/get-multivariate-events#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

events

Get Multivariate Events

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Get Multivariate Events

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/events/multivariate

200

400

401

500

Copy

Ask AI

    {
      "events": [\
        {\
          "event_ticker": "<string>",\
          "series_ticker": "<string>",\
          "sub_title": "<string>",\
          "title": "<string>",\
          "collateral_return_type": "<string>",\
          "mutually_exclusive": true,\
          "category": "<string>",\
          "strike_date": "2023-11-07T05:31:56Z",\
          "strike_period": "<string>",\
          "markets": [\
            {\
              "ticker": "<string>",\
              "event_ticker": "<string>",\
              "market_type": "binary",\
              "title": "<string>",\
              "subtitle": "<string>",\
              "yes_sub_title": "<string>",\
              "no_sub_title": "<string>",\
              "open_time": "2023-11-07T05:31:56Z",\
              "close_time": "2023-11-07T05:31:56Z",\
              "expected_expiration_time": "2023-11-07T05:31:56Z",\
              "expiration_time": "2023-11-07T05:31:56Z",\
              "latest_expiration_time": "2023-11-07T05:31:56Z",\
              "settlement_timer_seconds": 123,\
              "status": "unopened",\
              "response_price_units": "cents",\
              "yes_bid": 123,\
              "yes_bid_dollars": "<string>",\
              "yes_ask": 123,\
              "yes_ask_dollars": "<string>",\
              "no_bid": 123,\
              "no_bid_dollars": "<string>",\
              "no_ask": 123,\
              "no_ask_dollars": "<string>",\
              "last_price": 123,\
              "last_price_dollars": "<string>",\
              "volume": 123,\
              "volume_24h": 123,\
              "result": "yes",\
              "can_close_early": true,\
              "open_interest": 123,\
              "notional_value": 123,\
              "notional_value_dollars": "<string>",\
              "previous_yes_bid": 123,\
              "previous_yes_bid_dollars": "<string>",\
              "previous_yes_ask": 123,\
              "previous_yes_ask_dollars": "<string>",\
              "previous_price": 123,\
              "previous_price_dollars": "<string>",\
              "liquidity": 123,\
              "liquidity_dollars": "<string>",\
              "settlement_value": 123,\
              "settlement_value_dollars": "<string>",\
              "expiration_value": "<string>",\
              "category": "<string>",\
              "risk_limit_cents": 123,\
              "fee_waiver_expiration_time": "2023-11-07T05:31:56Z",\
              "early_close_condition": "<string>",\
              "tick_size": 123,\
              "strike_type": "greater",\
              "floor_strike": 123,\
              "cap_strike": 123,\
              "functional_strike": "<string>",\
              "custom_strike": {},\
              "rules_primary": "<string>",\
              "rules_secondary": "<string>",\
              "mve_collection_ticker": "<string>",\
              "mve_selected_legs": [\
                {\
                  "event_ticker": "<string>",\
                  "market_ticker": "<string>",\
                  "side": "<string>"\
                }\
              ],\
              "primary_participant_key": "<string>",\
              "price_level_structure": "<string>",\
              "price_ranges": [\
                {\
                  "start": "<string>",\
                  "end": "<string>",\
                  "step": "<string>"\
                }\
              ]\
            }\
          ],\
          "available_on_brokers": true,\
          "product_metadata": {}\
        }\
      ],
      "cursor": "<string>"
    }

GET

/

events

/

multivariate

Try it

Get Multivariate Events

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/events/multivariate

200

400

401

500

Copy

Ask AI

    {
      "events": [\
        {\
          "event_ticker": "<string>",\
          "series_ticker": "<string>",\
          "sub_title": "<string>",\
          "title": "<string>",\
          "collateral_return_type": "<string>",\
          "mutually_exclusive": true,\
          "category": "<string>",\
          "strike_date": "2023-11-07T05:31:56Z",\
          "strike_period": "<string>",\
          "markets": [\
            {\
              "ticker": "<string>",\
              "event_ticker": "<string>",\
              "market_type": "binary",\
              "title": "<string>",\
              "subtitle": "<string>",\
              "yes_sub_title": "<string>",\
              "no_sub_title": "<string>",\
              "open_time": "2023-11-07T05:31:56Z",\
              "close_time": "2023-11-07T05:31:56Z",\
              "expected_expiration_time": "2023-11-07T05:31:56Z",\
              "expiration_time": "2023-11-07T05:31:56Z",\
              "latest_expiration_time": "2023-11-07T05:31:56Z",\
              "settlement_timer_seconds": 123,\
              "status": "unopened",\
              "response_price_units": "cents",\
              "yes_bid": 123,\
              "yes_bid_dollars": "<string>",\
              "yes_ask": 123,\
              "yes_ask_dollars": "<string>",\
              "no_bid": 123,\
              "no_bid_dollars": "<string>",\
              "no_ask": 123,\
              "no_ask_dollars": "<string>",\
              "last_price": 123,\
              "last_price_dollars": "<string>",\
              "volume": 123,\
              "volume_24h": 123,\
              "result": "yes",\
              "can_close_early": true,\
              "open_interest": 123,\
              "notional_value": 123,\
              "notional_value_dollars": "<string>",\
              "previous_yes_bid": 123,\
              "previous_yes_bid_dollars": "<string>",\
              "previous_yes_ask": 123,\
              "previous_yes_ask_dollars": "<string>",\
              "previous_price": 123,\
              "previous_price_dollars": "<string>",\
              "liquidity": 123,\
              "liquidity_dollars": "<string>",\
              "settlement_value": 123,\
              "settlement_value_dollars": "<string>",\
              "expiration_value": "<string>",\
              "category": "<string>",\
              "risk_limit_cents": 123,\
              "fee_waiver_expiration_time": "2023-11-07T05:31:56Z",\
              "early_close_condition": "<string>",\
              "tick_size": 123,\
              "strike_type": "greater",\
              "floor_strike": 123,\
              "cap_strike": 123,\
              "functional_strike": "<string>",\
              "custom_strike": {},\
              "rules_primary": "<string>",\
              "rules_secondary": "<string>",\
              "mve_collection_ticker": "<string>",\
              "mve_selected_legs": [\
                {\
                  "event_ticker": "<string>",\
                  "market_ticker": "<string>",\
                  "side": "<string>"\
                }\
              ],\
              "primary_participant_key": "<string>",\
              "price_level_structure": "<string>",\
              "price_ranges": [\
                {\
                  "start": "<string>",\
                  "end": "<string>",\
                  "step": "<string>"\
                }\
              ]\
            }\
          ],\
          "available_on_brokers": true,\
          "product_metadata": {}\
        }\
      ],
      "cursor": "<string>"
    }

#### Query Parameters

[​](https://docs.kalshi.com/api-reference/events/get-multivariate-events#parameter-limit)

limit

integer

default:100

Number of results per page. Defaults to 100. Maximum value is 200.

Required range: `1 <= x <= 200`

[​](https://docs.kalshi.com/api-reference/events/get-multivariate-events#parameter-cursor)

cursor

string

Pagination cursor. Use the cursor value returned from the previous response to get the next page of results.

[​](https://docs.kalshi.com/api-reference/events/get-multivariate-events#parameter-series-ticker)

series\_ticker

string

Filter events by series ticker. Returns only multivariate events belonging to the specified series. Cannot be used together with collection\_ticker.

[​](https://docs.kalshi.com/api-reference/events/get-multivariate-events#parameter-collection-ticker)

collection\_ticker

string

Filter events by collection ticker. Returns only multivariate events belonging to the specified collection. Cannot be used together with series\_ticker.

[​](https://docs.kalshi.com/api-reference/events/get-multivariate-events#parameter-with-nested-markets)

with\_nested\_markets

boolean

default:false

Parameter to specify if nested markets should be included in the response. When true, each event will include a 'markets' field containing a list of Market objects associated with that event.

#### Response

200

application/json

Multivariate events retrieved successfully

[​](https://docs.kalshi.com/api-reference/events/get-multivariate-events#response-events)

events

object\[\]

required

Array of multivariate events matching the query criteria.

Show child attributes

[​](https://docs.kalshi.com/api-reference/events/get-multivariate-events#response-cursor)

cursor

string

required

Pagination cursor for the next page. Empty if there are no more results.

[Get Events](https://docs.kalshi.com/api-reference/events/get-events)
[Get Event](https://docs.kalshi.com/api-reference/events/get-event)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.