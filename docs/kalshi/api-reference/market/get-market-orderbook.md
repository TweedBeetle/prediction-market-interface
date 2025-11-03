---
url: https://docs.kalshi.com/api-reference/market/get-market-orderbook
title: Get Market Orderbook - API Documentation
description:  Endpoint for getting the current order book for a specific market.  The order book shows all active bid orders for both yes and no sides of a binary market. It returns yes bids and no bids only (no asks are returned). This is because in binary markets, a bid for yes at price X is equivalent to an ask for no at price (100-X). For example, a yes bid at 7¢ is the same as a no ask at 93¢, with identical contract sizes.  Each side shows price levels with their corresponding quantities and order counts, organized from best to worst prices.
scraped_at: 2025-11-03T14:46:19.829177
---

[Skip to main content](https://docs.kalshi.com/api-reference/market/get-market-orderbook#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

market

Get Market Orderbook

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Get Market Orderbook

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/markets/{ticker}/orderbook \
      --header 'KALSHI-ACCESS-KEY: <api-key>' \
      --header 'KALSHI-ACCESS-SIGNATURE: <api-key>' \
      --header 'KALSHI-ACCESS-TIMESTAMP: <api-key>'

200

401

404

500

Copy

Ask AI

    {
      "orderbook": {
        "yes": [\
          [\
            123\
          ]\
        ],
        "no": [\
          [\
            123\
          ]\
        ],
        "yes_dollars": [\
          [\
            "<any>"\
          ]\
        ],
        "no_dollars": [\
          [\
            "<any>"\
          ]\
        ]
      }
    }

GET

/

markets

/

{ticker}

/

orderbook

Try it

Get Market Orderbook

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/markets/{ticker}/orderbook \
      --header 'KALSHI-ACCESS-KEY: <api-key>' \
      --header 'KALSHI-ACCESS-SIGNATURE: <api-key>' \
      --header 'KALSHI-ACCESS-TIMESTAMP: <api-key>'

200

401

404

500

Copy

Ask AI

    {
      "orderbook": {
        "yes": [\
          [\
            123\
          ]\
        ],
        "no": [\
          [\
            123\
          ]\
        ],
        "yes_dollars": [\
          [\
            "<any>"\
          ]\
        ],
        "no_dollars": [\
          [\
            "<any>"\
          ]\
        ]
      }
    }

#### Authorizations

[​](https://docs.kalshi.com/api-reference/market/get-market-orderbook#authorization-kalshi-access-key)

KALSHI-ACCESS-KEY

string

header

required

Your API key ID

[​](https://docs.kalshi.com/api-reference/market/get-market-orderbook#authorization-kalshi-access-signature)

KALSHI-ACCESS-SIGNATURE

string

header

required

RSA-PSS signature of the request

[​](https://docs.kalshi.com/api-reference/market/get-market-orderbook#authorization-kalshi-access-timestamp)

KALSHI-ACCESS-TIMESTAMP

string

header

required

Request timestamp in milliseconds

#### Path Parameters

[​](https://docs.kalshi.com/api-reference/market/get-market-orderbook#parameter-ticker)

ticker

string

required

Market ticker

#### Query Parameters

[​](https://docs.kalshi.com/api-reference/market/get-market-orderbook#parameter-depth)

depth

integer

default:0

Depth of the orderbook to retrieve (0 or negative means all levels, 1-100 for specific depth)

Required range: `0 <= x <= 100`

#### Response

200

application/json

Orderbook retrieved successfully

[​](https://docs.kalshi.com/api-reference/market/get-market-orderbook#response-orderbook)

orderbook

object

required

Show child attributes

[Get Trades](https://docs.kalshi.com/api-reference/market/get-trades)
[Get Series](https://docs.kalshi.com/api-reference/market/get-series)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.