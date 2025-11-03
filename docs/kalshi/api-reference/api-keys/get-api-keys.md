---
url: https://docs.kalshi.com/api-reference/api-keys/get-api-keys
title: Get API Keys - API Documentation
description:  Endpoint for retrieving all API keys associated with the authenticated user.  API keys allow programmatic access to the platform without requiring username/password authentication. Each key has a unique identifier and name.
scraped_at: 2025-11-03T14:46:05.045117
---

[Skip to main content](https://docs.kalshi.com/api-reference/api-keys/get-api-keys#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

api-keys

Get API Keys

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Get API Keys

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/api_keys \
      --header 'KALSHI-ACCESS-KEY: <api-key>' \
      --header 'KALSHI-ACCESS-SIGNATURE: <api-key>' \
      --header 'KALSHI-ACCESS-TIMESTAMP: <api-key>'

200

401

500

Copy

Ask AI

    {
      "api_keys": [\
        {\
          "api_key_id": "<string>",\
          "name": "<string>"\
        }\
      ]
    }

GET

/

api\_keys

Try it

Get API Keys

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/api_keys \
      --header 'KALSHI-ACCESS-KEY: <api-key>' \
      --header 'KALSHI-ACCESS-SIGNATURE: <api-key>' \
      --header 'KALSHI-ACCESS-TIMESTAMP: <api-key>'

200

401

500

Copy

Ask AI

    {
      "api_keys": [\
        {\
          "api_key_id": "<string>",\
          "name": "<string>"\
        }\
      ]
    }

#### Authorizations

[​](https://docs.kalshi.com/api-reference/api-keys/get-api-keys#authorization-kalshi-access-key)

KALSHI-ACCESS-KEY

string

header

required

Your API key ID

[​](https://docs.kalshi.com/api-reference/api-keys/get-api-keys#authorization-kalshi-access-signature)

KALSHI-ACCESS-SIGNATURE

string

header

required

RSA-PSS signature of the request

[​](https://docs.kalshi.com/api-reference/api-keys/get-api-keys#authorization-kalshi-access-timestamp)

KALSHI-ACCESS-TIMESTAMP

string

header

required

Request timestamp in milliseconds

#### Response

200

application/json

List of API keys retrieved successfully

[​](https://docs.kalshi.com/api-reference/api-keys/get-api-keys#response-api-keys)

api\_keys

object\[\]

required

List of all API keys associated with the user

Show child attributes

[Get Order Queue Position](https://docs.kalshi.com/api-reference/portfolio/get-order-queue-position)
[Create API Key](https://docs.kalshi.com/api-reference/api-keys/create-api-key)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.