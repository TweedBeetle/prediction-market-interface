---
url: https://docs.kalshi.com/api-reference/market/get-market
title: Get Market - API Documentation
description:  Endpoint for getting data about a specific market by its ticker. A market represents a specific binary outcome within an event that users can trade on (e.g., "Will candidate X win?"). Markets have yes/no positions, current prices, volume, and settlement rules.
scraped_at: 2025-11-03T14:46:20.310168
---

[Skip to main content](https://docs.kalshi.com/api-reference/market/get-market#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

market

Get Market

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Get Market

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/markets/{ticker}

200

401

404

500

Copy

Ask AI

    {
      "market": {
        "ticker": "<string>",
        "event_ticker": "<string>",
        "market_type": "binary",
        "title": "<string>",
        "subtitle": "<string>",
        "yes_sub_title": "<string>",
        "no_sub_title": "<string>",
        "open_time": "2023-11-07T05:31:56Z",
        "close_time": "2023-11-07T05:31:56Z",
        "expected_expiration_time": "2023-11-07T05:31:56Z",
        "expiration_time": "2023-11-07T05:31:56Z",
        "latest_expiration_time": "2023-11-07T05:31:56Z",
        "settlement_timer_seconds": 123,
        "status": "unopened",
        "response_price_units": "cents",
        "yes_bid": 123,
        "yes_bid_dollars": "<string>",
        "yes_ask": 123,
        "yes_ask_dollars": "<string>",
        "no_bid": 123,
        "no_bid_dollars": "<string>",
        "no_ask": 123,
        "no_ask_dollars": "<string>",
        "last_price": 123,
        "last_price_dollars": "<string>",
        "volume": 123,
        "volume_24h": 123,
        "result": "yes",
        "can_close_early": true,
        "open_interest": 123,
        "notional_value": 123,
        "notional_value_dollars": "<string>",
        "previous_yes_bid": 123,
        "previous_yes_bid_dollars": "<string>",
        "previous_yes_ask": 123,
        "previous_yes_ask_dollars": "<string>",
        "previous_price": 123,
        "previous_price_dollars": "<string>",
        "liquidity": 123,
        "liquidity_dollars": "<string>",
        "settlement_value": 123,
        "settlement_value_dollars": "<string>",
        "expiration_value": "<string>",
        "category": "<string>",
        "risk_limit_cents": 123,
        "fee_waiver_expiration_time": "2023-11-07T05:31:56Z",
        "early_close_condition": "<string>",
        "tick_size": 123,
        "strike_type": "greater",
        "floor_strike": 123,
        "cap_strike": 123,
        "functional_strike": "<string>",
        "custom_strike": {},
        "rules_primary": "<string>",
        "rules_secondary": "<string>",
        "mve_collection_ticker": "<string>",
        "mve_selected_legs": [\
          {\
            "event_ticker": "<string>",\
            "market_ticker": "<string>",\
            "side": "<string>"\
          }\
        ],
        "primary_participant_key": "<string>",
        "price_level_structure": "<string>",
        "price_ranges": [\
          {\
            "start": "<string>",\
            "end": "<string>",\
            "step": "<string>"\
          }\
        ]
      }
    }

GET

/

markets

/

{ticker}

Try it

Get Market

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/markets/{ticker}

200

401

404

500

Copy

Ask AI

    {
      "market": {
        "ticker": "<string>",
        "event_ticker": "<string>",
        "market_type": "binary",
        "title": "<string>",
        "subtitle": "<string>",
        "yes_sub_title": "<string>",
        "no_sub_title": "<string>",
        "open_time": "2023-11-07T05:31:56Z",
        "close_time": "2023-11-07T05:31:56Z",
        "expected_expiration_time": "2023-11-07T05:31:56Z",
        "expiration_time": "2023-11-07T05:31:56Z",
        "latest_expiration_time": "2023-11-07T05:31:56Z",
        "settlement_timer_seconds": 123,
        "status": "unopened",
        "response_price_units": "cents",
        "yes_bid": 123,
        "yes_bid_dollars": "<string>",
        "yes_ask": 123,
        "yes_ask_dollars": "<string>",
        "no_bid": 123,
        "no_bid_dollars": "<string>",
        "no_ask": 123,
        "no_ask_dollars": "<string>",
        "last_price": 123,
        "last_price_dollars": "<string>",
        "volume": 123,
        "volume_24h": 123,
        "result": "yes",
        "can_close_early": true,
        "open_interest": 123,
        "notional_value": 123,
        "notional_value_dollars": "<string>",
        "previous_yes_bid": 123,
        "previous_yes_bid_dollars": "<string>",
        "previous_yes_ask": 123,
        "previous_yes_ask_dollars": "<string>",
        "previous_price": 123,
        "previous_price_dollars": "<string>",
        "liquidity": 123,
        "liquidity_dollars": "<string>",
        "settlement_value": 123,
        "settlement_value_dollars": "<string>",
        "expiration_value": "<string>",
        "category": "<string>",
        "risk_limit_cents": 123,
        "fee_waiver_expiration_time": "2023-11-07T05:31:56Z",
        "early_close_condition": "<string>",
        "tick_size": 123,
        "strike_type": "greater",
        "floor_strike": 123,
        "cap_strike": 123,
        "functional_strike": "<string>",
        "custom_strike": {},
        "rules_primary": "<string>",
        "rules_secondary": "<string>",
        "mve_collection_ticker": "<string>",
        "mve_selected_legs": [\
          {\
            "event_ticker": "<string>",\
            "market_ticker": "<string>",\
            "side": "<string>"\
          }\
        ],
        "primary_participant_key": "<string>",
        "price_level_structure": "<string>",
        "price_ranges": [\
          {\
            "start": "<string>",\
            "end": "<string>",\
            "step": "<string>"\
          }\
        ]
      }
    }

#### Path Parameters

[​](https://docs.kalshi.com/api-reference/market/get-market#parameter-ticker)

ticker

string

required

Market ticker

#### Response

200

application/json

Market retrieved successfully

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market)

market

object

required

Show child attributes

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-ticker)

market.ticker

string

required

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-event-ticker)

market.event\_ticker

string

required

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-market-type)

market.market\_type

enum<string>

required

Identifies the type of market

Available options:

`binary`,

`scalar`

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-title)

market.title

string

required

deprecated

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-subtitle)

market.subtitle

string

required

deprecated

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-yes-sub-title)

market.yes\_sub\_title

string

required

Shortened title for the yes side of this market

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-no-sub-title)

market.no\_sub\_title

string

required

Shortened title for the no side of this market

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-open-time)

market.open\_time

string<date-time>

required

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-close-time)

market.close\_time

string<date-time>

required

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-expiration-time)

market.expiration\_time

string<date-time>

required

deprecated

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-latest-expiration-time)

market.latest\_expiration\_time

string<date-time>

required

Latest possible time for this market to expire

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-settlement-timer-seconds)

market.settlement\_timer\_seconds

integer

required

The amount of time after determination that the market settles

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-status)

market.status

enum<string>

required

Current status of the market. 'unopened' means the market has not started trading yet, 'open' means it is currently tradeable, 'closed' means trading has ended, and 'settled' means the final result has been determined and positions settled.

Available options:

`unopened`,

`open`,

`closed`,

`settled`

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-response-price-units)

market.response\_price\_units

enum<string>

required

The units used to express all price related fields

Available options:

`cents`

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-yes-bid)

market.yes\_bid

number

required

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-yes-bid-dollars)

market.yes\_bid\_dollars

string

required

Price for the highest YES buy offer on this market in dollars

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-yes-ask)

market.yes\_ask

number

required

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-yes-ask-dollars)

market.yes\_ask\_dollars

string

required

Price for the lowest YES sell offer on this market in dollars

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-no-bid)

market.no\_bid

number

required

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-no-bid-dollars)

market.no\_bid\_dollars

string

required

Price for the highest NO buy offer on this market in dollars

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-no-ask)

market.no\_ask

number

required

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-no-ask-dollars)

market.no\_ask\_dollars

string

required

Price for the lowest NO sell offer on this market in dollars

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-last-price)

market.last\_price

number

required

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-last-price-dollars)

market.last\_price\_dollars

string

required

Price for the last traded YES contract on this market in dollars

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-volume)

market.volume

integer

required

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-volume-24h)

market.volume\_24h

integer

required

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-result)

market.result

enum<string> | null

required

Available options:

`yes`,

`no`,

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-can-close-early)

market.can\_close\_early

boolean

required

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-open-interest)

market.open\_interest

integer

required

Number of contracts bought on this market disconsidering netting

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-notional-value)

market.notional\_value

integer

required

The total value of a single contract at settlement in cents

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-notional-value-dollars)

market.notional\_value\_dollars

string

required

The total value of a single contract at settlement in dollars

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-previous-yes-bid)

market.previous\_yes\_bid

integer

required

Price for the highest YES buy offer on this market a day ago in cents

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-previous-yes-bid-dollars)

market.previous\_yes\_bid\_dollars

string

required

Price for the highest YES buy offer on this market a day ago in dollars

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-previous-yes-ask)

market.previous\_yes\_ask

integer

required

Price for the lowest YES sell offer on this market a day ago in cents

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-previous-yes-ask-dollars)

market.previous\_yes\_ask\_dollars

string

required

Price for the lowest YES sell offer on this market a day ago in dollars

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-previous-price)

market.previous\_price

integer

required

Price for the last traded YES contract on this market a day ago in cents

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-previous-price-dollars)

market.previous\_price\_dollars

string

required

Price for the last traded YES contract on this market a day ago in dollars

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-liquidity)

market.liquidity

integer

required

Value for current offers in this market in cents

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-liquidity-dollars)

market.liquidity\_dollars

string

required

Value for current offers in this market in dollars

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-expiration-value)

market.expiration\_value

string

required

The value that was considered for the settlement

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-category)

market.category

string

required

deprecated

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-risk-limit-cents)

market.risk\_limit\_cents

integer

required

deprecated

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-tick-size)

market.tick\_size

integer

required

The minimum price movement in the market

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-rules-primary)

market.rules\_primary

string

required

A plain language description of the most important market terms

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-rules-secondary)

market.rules\_secondary

string

required

A plain language description of secondary market terms

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-price-level-structure)

market.price\_level\_structure

string

required

Price level structure for this market, defining price ranges and tick sizes

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-price-ranges)

market.price\_ranges

object\[\]

required

Valid price ranges for orders on this market

Show child attributes

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-expected-expiration-time)

market.expected\_expiration\_time

string<date-time> | null

Time when this market is expected to expire

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-settlement-value)

market.settlement\_value

integer | null

The settlement value of the YES/LONG side of the contract in cents. Only filled after determination

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-settlement-value-dollars)

market.settlement\_value\_dollars

string | null

The settlement value of the YES/LONG side of the contract in dollars. Only filled after determination

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-fee-waiver-expiration-time)

market.fee\_waiver\_expiration\_time

string<date-time> | null

Time when this market's fee waiver expires

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-early-close-condition)

market.early\_close\_condition

string | null

The condition under which the market can close early

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-strike-type)

market.strike\_type

enum<string> | null

Strike type defines how the market strike is defined and evaluated

Available options:

`greater`,

`greater_or_equal`,

`less`,

`less_or_equal`,

`between`,

`functional`,

`custom`,

`structured`

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-floor-strike)

market.floor\_strike

number | null

Minimum expiration value that leads to a YES settlement

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-cap-strike)

market.cap\_strike

number | null

Maximum expiration value that leads to a YES settlement

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-functional-strike)

market.functional\_strike

string | null

Mapping from expiration values to settlement values

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-custom-strike)

market.custom\_strike

object | null

Expiration value for each target that leads to a YES settlement

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-mve-collection-ticker)

market.mve\_collection\_ticker

string | null

The ticker of the multivariate event collection

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-mve-selected-legs)

market.mve\_selected\_legs

object\[\] | null

Show child attributes

[​](https://docs.kalshi.com/api-reference/market/get-market#response-market-primary-participant-key)

market.primary\_participant\_key

string | null

[Get Markets](https://docs.kalshi.com/api-reference/market/get-markets)
[Get Event Candlesticks](https://docs.kalshi.com/api-reference/events/get-event-candlesticks)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.