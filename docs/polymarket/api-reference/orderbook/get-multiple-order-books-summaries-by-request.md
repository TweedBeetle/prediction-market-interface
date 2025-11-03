---
url: https://docs.polymarket.com/api-reference/orderbook/get-multiple-order-books-summaries-by-request
title: Get multiple order books summaries by request - Polymarket Documentation
description: Retrieves order book summaries for specified tokens via POST request
scraped_at: 2025-11-03T15:03:46.818622
---

[Skip to main content](https://docs.polymarket.com/api-reference/orderbook/get-multiple-order-books-summaries-by-request#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

Ctrl K

Search...

Navigation

Orderbook

Get multiple order books summaries by request

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

Get multiple order books summaries by request

cURL

Copy

Ask AI

    curl --request POST \
      --url https://clob.polymarket.com/books \
      --header 'Content-Type: application/json' \
      --data '[\
      {\
        "token_id": "1234567890"\
      },\
      {\
        "token_id": "0987654321"\
      }\
    ]'

200

example

Copy

Ask AI

    [  {    "market": "0x1b6f76e5b8587ee896c35847e12d11e75290a8c3934c5952e8a9d6e4c6f03cfa",    "asset_id": "1234567890",    "timestamp": "2023-10-01T12:00:00Z",    "hash": "0xabc123def456...",    "bids": [      {        "price": "1800.50",        "size": "10.5"      }    ],    "asks": [      {        "price": "1800.50",        "size": "10.5"      }    ],    "min_order_size": "0.001",    "tick_size": "0.01",    "neg_risk": false  }]

POST

/

books

Try it

Get multiple order books summaries by request

cURL

Copy

Ask AI

    curl --request POST \
      --url https://clob.polymarket.com/books \
      --header 'Content-Type: application/json' \
      --data '[\
      {\
        "token_id": "1234567890"\
      },\
      {\
        "token_id": "0987654321"\
      }\
    ]'

200

example

Copy

Ask AI

    [  {    "market": "0x1b6f76e5b8587ee896c35847e12d11e75290a8c3934c5952e8a9d6e4c6f03cfa",    "asset_id": "1234567890",    "timestamp": "2023-10-01T12:00:00Z",    "hash": "0xabc123def456...",    "bids": [      {        "price": "1800.50",        "size": "10.5"      }    ],    "asks": [      {        "price": "1800.50",        "size": "10.5"      }    ],    "min_order_size": "0.001",    "tick_size": "0.01",    "neg_risk": false  }]

#### Body

application/json · object\[\]

[​](https://docs.polymarket.com/api-reference/orderbook/get-multiple-order-books-summaries-by-request#body-token-id)

token\_id

string

required

The unique identifier for the token

Example:

`"1234567890"`

[​](https://docs.polymarket.com/api-reference/orderbook/get-multiple-order-books-summaries-by-request#body-side)

side

enum<string>

Optional side parameter for certain operations

Available options:

`BUY`,

`SELL`

Example:

`"BUY"`

#### Response

200

application/json

Successful response

[​](https://docs.polymarket.com/api-reference/orderbook/get-multiple-order-books-summaries-by-request#response-market)

market

string

required

Market identifier

Example:

`"0x1b6f76e5b8587ee896c35847e12d11e75290a8c3934c5952e8a9d6e4c6f03cfa"`

[​](https://docs.polymarket.com/api-reference/orderbook/get-multiple-order-books-summaries-by-request#response-asset-id)

asset\_id

string

required

Asset identifier

Example:

`"1234567890"`

[​](https://docs.polymarket.com/api-reference/orderbook/get-multiple-order-books-summaries-by-request#response-timestamp)

timestamp

string<date-time>

required

Timestamp of the order book snapshot

Example:

`"2023-10-01T12:00:00Z"`

[​](https://docs.polymarket.com/api-reference/orderbook/get-multiple-order-books-summaries-by-request#response-hash)

hash

string

required

Hash of the order book state

Example:

`"0xabc123def456..."`

[​](https://docs.polymarket.com/api-reference/orderbook/get-multiple-order-books-summaries-by-request#response-bids)

bids

object\[\]

required

Array of bid levels

Show child attributes

[​](https://docs.polymarket.com/api-reference/orderbook/get-multiple-order-books-summaries-by-request#response-asks)

asks

object\[\]

required

Array of ask levels

Show child attributes

[​](https://docs.polymarket.com/api-reference/orderbook/get-multiple-order-books-summaries-by-request#response-min-order-size)

min\_order\_size

string

required

Minimum order size for this market

Example:

`"0.001"`

[​](https://docs.polymarket.com/api-reference/orderbook/get-multiple-order-books-summaries-by-request#response-tick-size)

tick\_size

string

required

Minimum price increment

Example:

`"0.01"`

[​](https://docs.polymarket.com/api-reference/orderbook/get-multiple-order-books-summaries-by-request#response-neg-risk)

neg\_risk

boolean

required

Whether negative risk is enabled

Example:

`false`

[Get order book summary](https://docs.polymarket.com/api-reference/orderbook/get-order-book-summary)
[Get market price](https://docs.polymarket.com/api-reference/pricing/get-market-price)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.