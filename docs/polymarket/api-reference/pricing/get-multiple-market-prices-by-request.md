---
url: https://docs.polymarket.com/api-reference/pricing/get-multiple-market-prices-by-request
title: Get multiple market prices by request - Polymarket Documentation
description: Retrieves market prices for specified tokens and sides via POST request
scraped_at: 2025-11-03T15:03:48.589246
---

[Skip to main content](https://docs.polymarket.com/api-reference/pricing/get-multiple-market-prices-by-request#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

Ctrl K

Search...

Navigation

Pricing

Get multiple market prices by request

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

Get multiple market prices by request

cURL

Copy

Ask AI

    curl --request POST \
      --url https://clob.polymarket.com/prices \
      --header 'Content-Type: application/json' \
      --data '[\
      {\
        "token_id": "1234567890",\
        "side": "BUY"\
      },\
      {\
        "token_id": "0987654321",\
        "side": "SELL"\
      }\
    ]'

200

example

Copy

Ask AI

    {  "1234567890": {    "BUY": "1800.50",    "SELL": "1801.00"  },  "0987654321": {    "BUY": "50.25",    "SELL": "50.30"  }}

POST

/

prices

Try it

Get multiple market prices by request

cURL

Copy

Ask AI

    curl --request POST \
      --url https://clob.polymarket.com/prices \
      --header 'Content-Type: application/json' \
      --data '[\
      {\
        "token_id": "1234567890",\
        "side": "BUY"\
      },\
      {\
        "token_id": "0987654321",\
        "side": "SELL"\
      }\
    ]'

200

example

Copy

Ask AI

    {  "1234567890": {    "BUY": "1800.50",    "SELL": "1801.00"  },  "0987654321": {    "BUY": "50.25",    "SELL": "50.30"  }}

#### Body

application/json · object\[\]

[​](https://docs.polymarket.com/api-reference/pricing/get-multiple-market-prices-by-request#body-token-id)

token\_id

string

required

The unique identifier for the token

Example:

`"1234567890"`

[​](https://docs.polymarket.com/api-reference/pricing/get-multiple-market-prices-by-request#body-side)

side

enum<string>

required

The side of the market (BUY or SELL)

Available options:

`BUY`,

`SELL`

Example:

`"BUY"`

#### Response

200

application/json

Successful response

Map of token\_id to side to price

[​](https://docs.polymarket.com/api-reference/pricing/get-multiple-market-prices-by-request#response-key)

{key}

object

Show child attributes

[Get multiple market prices](https://docs.polymarket.com/api-reference/pricing/get-multiple-market-prices)
[Get midpoint price](https://docs.polymarket.com/api-reference/pricing/get-midpoint-price)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.