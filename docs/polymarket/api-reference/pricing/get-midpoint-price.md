---
url: https://docs.polymarket.com/api-reference/pricing/get-midpoint-price
title: Get midpoint price - Polymarket Documentation
description: Retrieves the midpoint price for a specific token
scraped_at: 2025-11-03T15:03:48.043754
---

[Skip to main content](https://docs.polymarket.com/api-reference/pricing/get-midpoint-price#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

Ctrl K

Search...

Navigation

Pricing

Get midpoint price

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

Get midpoint price

cURL

Copy

Ask AI

    curl --request GET \
      --url https://clob.polymarket.com/midpoint

200

400

404

500

Copy

Ask AI

    {
      "mid": "1800.75"
    }

GET

/

midpoint

Try it

Get midpoint price

cURL

Copy

Ask AI

    curl --request GET \
      --url https://clob.polymarket.com/midpoint

200

400

404

500

Copy

Ask AI

    {
      "mid": "1800.75"
    }

#### Query Parameters

[​](https://docs.polymarket.com/api-reference/pricing/get-midpoint-price#parameter-token-id)

token\_id

string

required

The unique identifier for the token

#### Response

200

application/json

Successful response

[​](https://docs.polymarket.com/api-reference/pricing/get-midpoint-price#response-mid)

mid

string

required

The midpoint price (as string to maintain precision)

Example:

`"1800.75"`

[Get multiple market prices by request](https://docs.polymarket.com/api-reference/pricing/get-multiple-market-prices-by-request)
[Get price history for a traded token](https://docs.polymarket.com/api-reference/pricing/get-price-history-for-a-traded-token)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.