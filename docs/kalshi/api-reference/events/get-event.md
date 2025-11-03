---
url: https://docs.kalshi.com/api-reference/events/get-event
title: Get Event - API Documentation
description:  Endpoint for getting data about an event by its ticker.  An event represents a real-world occurrence that can be traded on, such as an election, sports game, or economic indicator release. Events contain one or more markets where users can place trades on different outcomes.
scraped_at: 2025-11-03T14:46:10.157583
---

[Skip to main content](https://docs.kalshi.com/api-reference/events/get-event#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

events

Get Event

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Get Event

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/events/{event_ticker}

200

400

401

404

500

Copy

Ask AI

    {
      "event": {
        "event_ticker": "<string>",
        "series_ticker": "<string>",
        "sub_title": "<string>",
        "title": "<string>",
        "collateral_return_type": "<string>",
        "mutually_exclusive": true,
        "category": "<string>",
        "strike_date": "2023-11-07T05:31:56Z",
        "strike_period": "<string>",
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
        ],
        "available_on_brokers": true,
        "product_metadata": {}
      },
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
      ]
    }

GET

/

events

/

{event\_ticker}

Try it

Get Event

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/events/{event_ticker}

200

400

401

404

500

Copy

Ask AI

    {
      "event": {
        "event_ticker": "<string>",
        "series_ticker": "<string>",
        "sub_title": "<string>",
        "title": "<string>",
        "collateral_return_type": "<string>",
        "mutually_exclusive": true,
        "category": "<string>",
        "strike_date": "2023-11-07T05:31:56Z",
        "strike_period": "<string>",
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
        ],
        "available_on_brokers": true,
        "product_metadata": {}
      },
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
      ]
    }

#### Path Parameters

[​](https://docs.kalshi.com/api-reference/events/get-event#parameter-event-ticker)

event\_ticker

string

required

Event ticker

#### Query Parameters

[​](https://docs.kalshi.com/api-reference/events/get-event#parameter-with-nested-markets)

with\_nested\_markets

boolean

default:false

If true, markets are included within the event object. If false (default), markets are returned as a separate top-level field in the response.

#### Response

200

application/json

Event retrieved successfully

[​](https://docs.kalshi.com/api-reference/events/get-event#response-event)

event

object

required

Data for the event.

Show child attributes

[​](https://docs.kalshi.com/api-reference/events/get-event#response-markets)

markets

object\[\]

required

Data for the markets in this event. This field is deprecated in favour of the "markets" field inside the event. Which will be filled with the same value if you use the query parameter "with\_nested\_markets=true".

Show child attributes

[Get Multivariate Events](https://docs.kalshi.com/api-reference/events/get-multivariate-events)
[Get Event Metadata](https://docs.kalshi.com/api-reference/events/get-event-metadata)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.