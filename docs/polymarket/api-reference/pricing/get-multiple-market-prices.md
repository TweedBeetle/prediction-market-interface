---
url: https://docs.polymarket.com/api-reference/pricing/get-multiple-market-prices
title: Get multiple market prices - Polymarket Documentation
description: Retrieves market prices for multiple tokens and sides
scraped_at: 2025-11-03T15:03:47.825685
---

[Skip to main content](https://docs.polymarket.com/api-reference/pricing/get-multiple-market-prices#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

Ctrl K

Search...

Navigation

Pricing

Get multiple market prices

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

Get multiple market prices

cURL

Copy

Ask AI

    curl --request GET \
      --url https://clob.polymarket.com/prices

200

400

500

Copy

Ask AI

    {
      "1234567890": {
        "BUY": "1800.50",
        "SELL": "1801.00"
      },
      "0987654321": {
        "BUY": "50.25",
        "SELL": "50.30"
      }
    }

GET

/

prices

Try it

Get multiple market prices

cURL

Copy

Ask AI

    curl --request GET \
      --url https://clob.polymarket.com/prices

200

400

500

Copy

Ask AI

    {
      "1234567890": {
        "BUY": "1800.50",
        "SELL": "1801.00"
      },
      "0987654321": {
        "BUY": "50.25",
        "SELL": "50.30"
      }
    }

#### Response

200

application/json

Successful response

Map of token\_id to side to price

[​](https://docs.polymarket.com/api-reference/pricing/get-multiple-market-prices#response-key)

{key}

object

Show child attributes

[​](https://docs.polymarket.com/api-reference/pricing/get-multiple-market-prices#response-key-key)

{key}.{key}

string

[Get market price](https://docs.polymarket.com/api-reference/pricing/get-market-price)
[Get multiple market prices by request](https://docs.polymarket.com/api-reference/pricing/get-multiple-market-prices-by-request)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.