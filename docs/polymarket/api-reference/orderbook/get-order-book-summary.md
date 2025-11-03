---
url: https://docs.polymarket.com/api-reference/orderbook/get-order-book-summary
title: Get order book summary - Polymarket Documentation
description: Retrieves the order book summary for a specific token
scraped_at: 2025-11-03T15:03:47.074013
---

[Skip to main content](https://docs.polymarket.com/api-reference/orderbook/get-order-book-summary#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

Ctrl K

Search...

Navigation

Orderbook

Get order book summary

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

Get order book summary

cURL

Copy

Ask AI

    curl --request GET \
      --url https://clob.polymarket.com/book

200

400

404

500

Copy

Ask AI

    {
      "market": "0x1b6f76e5b8587ee896c35847e12d11e75290a8c3934c5952e8a9d6e4c6f03cfa",
      "asset_id": "1234567890",
      "timestamp": "2023-10-01T12:00:00Z",
      "hash": "0xabc123def456...",
      "bids": [\
        {\
          "price": "1800.50",\
          "size": "10.5"\
        }\
      ],
      "asks": [\
        {\
          "price": "1800.50",\
          "size": "10.5"\
        }\
      ],
      "min_order_size": "0.001",
      "tick_size": "0.01",
      "neg_risk": false
    }

GET

/

book

Try it

Get order book summary

cURL

Copy

Ask AI

    curl --request GET \
      --url https://clob.polymarket.com/book

200

400

404

500

Copy

Ask AI

    {
      "market": "0x1b6f76e5b8587ee896c35847e12d11e75290a8c3934c5952e8a9d6e4c6f03cfa",
      "asset_id": "1234567890",
      "timestamp": "2023-10-01T12:00:00Z",
      "hash": "0xabc123def456...",
      "bids": [\
        {\
          "price": "1800.50",\
          "size": "10.5"\
        }\
      ],
      "asks": [\
        {\
          "price": "1800.50",\
          "size": "10.5"\
        }\
      ],
      "min_order_size": "0.001",
      "tick_size": "0.01",
      "neg_risk": false
    }

#### Query Parameters

[​](https://docs.polymarket.com/api-reference/orderbook/get-order-book-summary#parameter-token-id)

token\_id

string

required

The unique identifier for the token

#### Response

200

application/json

Successful response

[​](https://docs.polymarket.com/api-reference/orderbook/get-order-book-summary#response-market)

market

string

required

Market identifier

Example:

`"0x1b6f76e5b8587ee896c35847e12d11e75290a8c3934c5952e8a9d6e4c6f03cfa"`

[​](https://docs.polymarket.com/api-reference/orderbook/get-order-book-summary#response-asset-id)

asset\_id

string

required

Asset identifier

Example:

`"1234567890"`

[​](https://docs.polymarket.com/api-reference/orderbook/get-order-book-summary#response-timestamp)

timestamp

string<date-time>

required

Timestamp of the order book snapshot

Example:

`"2023-10-01T12:00:00Z"`

[​](https://docs.polymarket.com/api-reference/orderbook/get-order-book-summary#response-hash)

hash

string

required

Hash of the order book state

Example:

`"0xabc123def456..."`

[​](https://docs.polymarket.com/api-reference/orderbook/get-order-book-summary#response-bids)

bids

object\[\]

required

Array of bid levels

Show child attributes

[​](https://docs.polymarket.com/api-reference/orderbook/get-order-book-summary#response-asks)

asks

object\[\]

required

Array of ask levels

Show child attributes

[​](https://docs.polymarket.com/api-reference/orderbook/get-order-book-summary#response-min-order-size)

min\_order\_size

string

required

Minimum order size for this market

Example:

`"0.001"`

[​](https://docs.polymarket.com/api-reference/orderbook/get-order-book-summary#response-tick-size)

tick\_size

string

required

Minimum price increment

Example:

`"0.01"`

[​](https://docs.polymarket.com/api-reference/orderbook/get-order-book-summary#response-neg-risk)

neg\_risk

boolean

required

Whether negative risk is enabled

Example:

`false`

[Authentication](https://docs.polymarket.com/developers/CLOB/authentication)
[Get multiple order books summaries by request](https://docs.polymarket.com/api-reference/orderbook/get-multiple-order-books-summaries-by-request)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.