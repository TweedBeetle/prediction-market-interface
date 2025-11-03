---
url: https://docs.polymarket.com/api-reference/pricing/get-market-price
title: Get market price - Polymarket Documentation
description: Retrieves the market price for a specific token and side
scraped_at: 2025-11-03T15:03:47.298384
---

[Skip to main content](https://docs.polymarket.com/api-reference/pricing/get-market-price#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

Ctrl K

Search...

Navigation

Pricing

Get market price

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

Get market price

cURL

Copy

Ask AI

    curl --request GET \
      --url https://clob.polymarket.com/price

200

example

Copy

Ask AI

    {  "price": "1800.50"}

GET

/

price

Try it

Get market price

cURL

Copy

Ask AI

    curl --request GET \
      --url https://clob.polymarket.com/price

200

example

Copy

Ask AI

    {  "price": "1800.50"}

#### Query Parameters

[​](https://docs.polymarket.com/api-reference/pricing/get-market-price#parameter-token-id)

token\_id

string

required

The unique identifier for the token

[​](https://docs.polymarket.com/api-reference/pricing/get-market-price#parameter-side)

side

enum<string>

required

The side of the market (BUY or SELL)

Available options:

`BUY`,

`SELL`

#### Response

200

application/json

Successful response

[​](https://docs.polymarket.com/api-reference/pricing/get-market-price#response-price)

price

string

required

The market price (as string to maintain precision)

Example:

`"1800.50"`

[Get multiple order books summaries by request](https://docs.polymarket.com/api-reference/orderbook/get-multiple-order-books-summaries-by-request)
[Get multiple market prices](https://docs.polymarket.com/api-reference/pricing/get-multiple-market-prices)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.