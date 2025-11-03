---
url: https://docs.polymarket.com/api-reference/spreads/get-bid-ask-spreads
title: Get bid-ask spreads - Polymarket Documentation
description: Retrieves bid-ask spreads for multiple tokens
scraped_at: 2025-11-03T15:03:51.586343
---

[Skip to main content](https://docs.polymarket.com/api-reference/spreads/get-bid-ask-spreads#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

Ctrl K

Search...

Navigation

Spreads

Get bid-ask spreads

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

Get bid-ask spreads

cURL

Copy

Ask AI

    curl --request POST \
      --url https://clob.polymarket.com/spreads \
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

    {  "1234567890": "0.50",  "0987654321": "0.05"}

POST

/

spreads

Try it

Get bid-ask spreads

cURL

Copy

Ask AI

    curl --request POST \
      --url https://clob.polymarket.com/spreads \
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

    {  "1234567890": "0.50",  "0987654321": "0.05"}

#### Body

application/json · object\[\]

[​](https://docs.polymarket.com/api-reference/spreads/get-bid-ask-spreads#body-token-id)

token\_id

string

required

The unique identifier for the token

Example:

`"1234567890"`

[​](https://docs.polymarket.com/api-reference/spreads/get-bid-ask-spreads#body-side)

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

Map of token\_id to spread value

[​](https://docs.polymarket.com/api-reference/spreads/get-bid-ask-spreads#response-key)

{key}

string

[Get price history for a traded token](https://docs.polymarket.com/api-reference/pricing/get-price-history-for-a-traded-token)
[Orders Overview](https://docs.polymarket.com/developers/CLOB/orders/orders)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.