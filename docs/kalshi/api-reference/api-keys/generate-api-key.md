---
url: https://docs.kalshi.com/api-reference/api-keys/generate-api-key
title: Generate API Key - API Documentation
description:  Endpoint for generating a new API key with an automatically created key pair.  This endpoint generates both a public and private RSA key pair. The public key is stored on the platform, while the private key is returned to the user and must be stored securely. The private key cannot be retrieved again.
scraped_at: 2025-11-03T14:46:05.025733
---

[Skip to main content](https://docs.kalshi.com/api-reference/api-keys/generate-api-key#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

api-keys

Generate API Key

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Generate API Key

cURL

Copy

Ask AI

    curl --request POST \
      --url https://api.elections.kalshi.com/trade-api/v2/api_keys/generate \
      --header 'Content-Type: application/json' \
      --header 'KALSHI-ACCESS-KEY: <api-key>' \
      --header 'KALSHI-ACCESS-SIGNATURE: <api-key>' \
      --header 'KALSHI-ACCESS-TIMESTAMP: <api-key>' \
      --data '{
      "name": "<string>"
    }'

201

400

401

500

Copy

Ask AI

    {
      "api_key_id": "<string>",
      "private_key": "<string>"
    }

POST

/

api\_keys

/

generate

Try it

Generate API Key

cURL

Copy

Ask AI

    curl --request POST \
      --url https://api.elections.kalshi.com/trade-api/v2/api_keys/generate \
      --header 'Content-Type: application/json' \
      --header 'KALSHI-ACCESS-KEY: <api-key>' \
      --header 'KALSHI-ACCESS-SIGNATURE: <api-key>' \
      --header 'KALSHI-ACCESS-TIMESTAMP: <api-key>' \
      --data '{
      "name": "<string>"
    }'

201

400

401

500

Copy

Ask AI

    {
      "api_key_id": "<string>",
      "private_key": "<string>"
    }

#### Authorizations

[​](https://docs.kalshi.com/api-reference/api-keys/generate-api-key#authorization-kalshi-access-key)

KALSHI-ACCESS-KEY

string

header

required

Your API key ID

[​](https://docs.kalshi.com/api-reference/api-keys/generate-api-key#authorization-kalshi-access-signature)

KALSHI-ACCESS-SIGNATURE

string

header

required

RSA-PSS signature of the request

[​](https://docs.kalshi.com/api-reference/api-keys/generate-api-key#authorization-kalshi-access-timestamp)

KALSHI-ACCESS-TIMESTAMP

string

header

required

Request timestamp in milliseconds

#### Body

application/json

[​](https://docs.kalshi.com/api-reference/api-keys/generate-api-key#body-name)

name

string

required

Name for the API key. This helps identify the key's purpose

#### Response

201

application/json

API key generated successfully

[​](https://docs.kalshi.com/api-reference/api-keys/generate-api-key#response-api-key-id)

api\_key\_id

string

required

Unique identifier for the newly generated API key

[​](https://docs.kalshi.com/api-reference/api-keys/generate-api-key#response-private-key)

private\_key

string

required

RSA private key in PEM format. This must be stored securely and cannot be retrieved again after this response

[Create API Key](https://docs.kalshi.com/api-reference/api-keys/create-api-key)
[Delete API Key](https://docs.kalshi.com/api-reference/api-keys/delete-api-key)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.