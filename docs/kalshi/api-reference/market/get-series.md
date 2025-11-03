---
url: https://docs.kalshi.com/api-reference/market/get-series
title: Get Series - API Documentation
description:  Endpoint for getting data about a specific series by its ticker.  A series represents a template for recurring events that follow the same format and rules (e.g., "Monthly Jobs Report", "Weekly Initial Jobless Claims", "Daily Weather in NYC"). Series define the structure, settlement sources, and metadata that will be applied to each recurring event instance within that series.
scraped_at: 2025-11-03T14:46:19.834209
---

[Skip to main content](https://docs.kalshi.com/api-reference/market/get-series#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

market

Get Series

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Get Series

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/series/{series_ticker}

200

400

500

Copy

Ask AI

    {
      "series": {
        "ticker": "<string>",
        "frequency": "<string>",
        "title": "<string>",
        "category": "<string>",
        "tags": [\
          "<string>"\
        ],
        "settlement_sources": [\
          {\
            "name": "<string>",\
            "url": "<string>"\
          }\
        ],
        "contract_url": "<string>",
        "contract_terms_url": "<string>",
        "product_metadata": {},
        "fee_type": "quadratic",
        "fee_multiplier": 123,
        "additional_prohibitions": [\
          "<string>"\
        ]
      }
    }

GET

/

series

/

{series\_ticker}

Try it

Get Series

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/series/{series_ticker}

200

400

500

Copy

Ask AI

    {
      "series": {
        "ticker": "<string>",
        "frequency": "<string>",
        "title": "<string>",
        "category": "<string>",
        "tags": [\
          "<string>"\
        ],
        "settlement_sources": [\
          {\
            "name": "<string>",\
            "url": "<string>"\
          }\
        ],
        "contract_url": "<string>",
        "contract_terms_url": "<string>",
        "product_metadata": {},
        "fee_type": "quadratic",
        "fee_multiplier": 123,
        "additional_prohibitions": [\
          "<string>"\
        ]
      }
    }

#### Path Parameters

[​](https://docs.kalshi.com/api-reference/market/get-series#parameter-series-ticker)

series\_ticker

string

required

The ticker of the series to retrieve

#### Response

200

application/json

Series retrieved successfully

[​](https://docs.kalshi.com/api-reference/market/get-series#response-series)

series

object

required

Show child attributes

[​](https://docs.kalshi.com/api-reference/market/get-series#response-series-ticker)

series.ticker

string

required

Ticker that identifies this series.

[​](https://docs.kalshi.com/api-reference/market/get-series#response-series-frequency)

series.frequency

string

required

Description of the frequency of the series. There is no fixed value set here, but will be something human-readable like weekly, daily, one-off.

[​](https://docs.kalshi.com/api-reference/market/get-series#response-series-title)

series.title

string

required

Title describing the series. For full context use you should use this field with the title field of the events belonging to this series.

[​](https://docs.kalshi.com/api-reference/market/get-series#response-series-category)

series.category

string

required

Category specifies the category which this series belongs to.

[​](https://docs.kalshi.com/api-reference/market/get-series#response-series-tags)

series.tags

string\[\]

required

Tags specifies the subjects that this series relates to, multiple series from different categories can have the same tags.

[​](https://docs.kalshi.com/api-reference/market/get-series#response-series-settlement-sources)

series.settlement\_sources

object\[\]

required

SettlementSources specifies the official sources used for the determination of markets within the series. Methodology is defined in the rulebook.

Show child attributes

[​](https://docs.kalshi.com/api-reference/market/get-series#response-series-contract-url)

series.contract\_url

string

required

ContractUrl provides a direct link to the original filing of the contract which underlies the series.

[​](https://docs.kalshi.com/api-reference/market/get-series#response-series-contract-terms-url)

series.contract\_terms\_url

string

required

ContractTermsUrl is the URL to the current terms of the contract underlying the series.

[​](https://docs.kalshi.com/api-reference/market/get-series#response-series-fee-type)

series.fee\_type

enum<string>

required

FeeType is a string representing the series' fee structure. Fee structures can be found at [https://kalshi.com/docs/kalshi-fee-schedule.pdf](https://kalshi.com/docs/kalshi-fee-schedule.pdf)
. 'quadratic' is described by the General Trading Fees Table, 'quadratic\_with\_maker\_fees' is described by the General Trading Fees Table with maker fees described in the Maker Fees section, 'flat' is described by the Specific Trading Fees Table.

Available options:

`quadratic`,

`quadratic_with_maker_fees`,

`flat`

[​](https://docs.kalshi.com/api-reference/market/get-series#response-series-fee-multiplier)

series.fee\_multiplier

number

required

FeeMultiplier is a floating point multiplier applied to the fee calculations.

[​](https://docs.kalshi.com/api-reference/market/get-series#response-series-additional-prohibitions)

series.additional\_prohibitions

string\[\]

required

AdditionalProhibitions is a list of additional trading prohibitions for this series.

[​](https://docs.kalshi.com/api-reference/market/get-series#response-series-product-metadata)

series.product\_metadata

object | null

Internal product metadata of the series.

[Get Market Orderbook](https://docs.kalshi.com/api-reference/market/get-market-orderbook)
[Get Series List](https://docs.kalshi.com/api-reference/market/get-series-list)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.