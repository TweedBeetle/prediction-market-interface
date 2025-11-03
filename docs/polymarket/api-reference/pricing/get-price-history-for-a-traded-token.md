---
url: https://docs.polymarket.com/api-reference/pricing/get-price-history-for-a-traded-token
title: Get price history for a traded token - Polymarket Documentation
description: Fetches historical price data for a specified market token
scraped_at: 2025-11-03T15:03:49.087919
---

[Skip to main content](https://docs.polymarket.com/api-reference/pricing/get-price-history-for-a-traded-token#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

Ctrl K

Search...

Navigation

Pricing

Get price history for a traded token

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

Get price history for a traded token

cURL

Copy

Ask AI

    curl --request GET \
      --url https://clob.polymarket.com/prices-history

200

400

404

500

Copy

Ask AI

    {
      "history": [\
        {\
          "t": 1697875200,\
          "p": 1800.75\
        }\
      ]
    }

GET

/

prices-history

Try it

Get price history for a traded token

cURL

Copy

Ask AI

    curl --request GET \
      --url https://clob.polymarket.com/prices-history

200

400

404

500

Copy

Ask AI

    {
      "history": [\
        {\
          "t": 1697875200,\
          "p": 1800.75\
        }\
      ]
    }

#### Query Parameters

[​](https://docs.polymarket.com/api-reference/pricing/get-price-history-for-a-traded-token#parameter-market)

market

string

required

The CLOB token ID for which to fetch price history

[​](https://docs.polymarket.com/api-reference/pricing/get-price-history-for-a-traded-token#parameter-start-ts)

startTs

number

The start time, a Unix timestamp in UTC

[​](https://docs.polymarket.com/api-reference/pricing/get-price-history-for-a-traded-token#parameter-end-ts)

endTs

number

The end time, a Unix timestamp in UTC

[​](https://docs.polymarket.com/api-reference/pricing/get-price-history-for-a-traded-token#parameter-interval)

interval

enum<string>

A string representing a duration ending at the current time. Mutually exclusive with startTs and endTs

Available options:

`1m`,

`1w`,

`1d`,

`6h`,

`1h`,

`max`

[​](https://docs.polymarket.com/api-reference/pricing/get-price-history-for-a-traded-token#parameter-fidelity)

fidelity

number

The resolution of the data, in minutes

#### Response

200

application/json

A list of timestamp/price pairs

[​](https://docs.polymarket.com/api-reference/pricing/get-price-history-for-a-traded-token#response-history)

history

object\[\]

required

Show child attributes

[Get midpoint price](https://docs.polymarket.com/api-reference/pricing/get-midpoint-price)
[Get bid-ask spreads](https://docs.polymarket.com/api-reference/spreads/get-bid-ask-spreads)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.