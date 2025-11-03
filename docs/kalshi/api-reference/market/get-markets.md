---
url: https://docs.kalshi.com/api-reference/market/get-markets
title: Get Markets - API Documentation
description: Filter by market status. Comma-separated list. Possible values: 'unopened', 'open', 'closed', 'settled'. Leave empty to return markets with any status.
scraped_at: 2025-11-03T14:46:20.572037
---

[Skip to main content](https://docs.kalshi.com/api-reference/market/get-markets#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

market

Get Markets

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Get Markets

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/markets

200

400

401

500

Copy

Ask AI

    {
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
      "cursor": "<string>"
    }

GET

/

markets

Try it

Get Markets

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/markets

200

400

401

500

Copy

Ask AI

    {
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
      "cursor": "<string>"
    }

#### Query Parameters

[​](https://docs.kalshi.com/api-reference/market/get-markets#parameter-limit)

limit

integer

default:100

Number of results per page. Defaults to 100. Maximum value is 1000.

Required range: `1 <= x <= 1000`

[​](https://docs.kalshi.com/api-reference/market/get-markets#parameter-cursor)

cursor

string

Pagination cursor. Use the cursor value returned from the previous response to get the next page of results. Leave empty for the first page.

[​](https://docs.kalshi.com/api-reference/market/get-markets#parameter-event-ticker)

event\_ticker

string

Event ticker of desired positions. Multiple event tickers can be provided as a comma-separated list (maximum 10).

[​](https://docs.kalshi.com/api-reference/market/get-markets#parameter-series-ticker)

series\_ticker

string

Filter by series ticker

[​](https://docs.kalshi.com/api-reference/market/get-markets#parameter-max-close-ts)

max\_close\_ts

integer

Filter items that close before this Unix timestamp

[​](https://docs.kalshi.com/api-reference/market/get-markets#parameter-min-close-ts)

min\_close\_ts

integer

Filter items that close after this Unix timestamp

[​](https://docs.kalshi.com/api-reference/market/get-markets#parameter-status)

status

string

Filter by market status. Comma-separated list. Possible values are 'unopened', 'open', 'closed', 'settled'. Leave empty to return markets with any status.

[​](https://docs.kalshi.com/api-reference/market/get-markets#parameter-tickers)

tickers

string

Filter by specific market tickers. Comma-separated list of market tickers to retrieve.

[​](https://docs.kalshi.com/api-reference/market/get-markets#parameter-mve-filter)

mve\_filter

enum<string>

Filter by multivariate events (combos). 'only' returns only multivariate events, 'exclude' excludes multivariate events.

Available options:

`only`,

`exclude`

#### Response

200

application/json

Markets retrieved successfully

[​](https://docs.kalshi.com/api-reference/market/get-markets#response-markets)

markets

object\[\]

required

Show child attributes

[​](https://docs.kalshi.com/api-reference/market/get-markets#response-cursor)

cursor

string

required

[Get Series List](https://docs.kalshi.com/api-reference/market/get-series-list)
[Get Market](https://docs.kalshi.com/api-reference/market/get-market)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.