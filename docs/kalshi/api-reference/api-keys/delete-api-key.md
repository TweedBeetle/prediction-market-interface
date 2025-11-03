---
url: https://docs.kalshi.com/api-reference/api-keys/delete-api-key
title: Delete API Key - API Documentation
description:  Endpoint for deleting an existing API key.  This endpoint permanently deletes an API key. Once deleted, the key can no longer be used for authentication. This action cannot be undone.
scraped_at: 2025-11-03T14:46:05.045826
---

[Skip to main content](https://docs.kalshi.com/api-reference/api-keys/delete-api-key#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

api-keys

Delete API Key

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Delete API Key

cURL

Copy

Ask AI

    curl --request DELETE \
      --url https://api.elections.kalshi.com/trade-api/v2/api_keys/{api_key} \
      --header 'KALSHI-ACCESS-KEY: <api-key>' \
      --header 'KALSHI-ACCESS-SIGNATURE: <api-key>' \
      --header 'KALSHI-ACCESS-TIMESTAMP: <api-key>'

DELETE

/

api\_keys

/

{api\_key}

Try it

Delete API Key

cURL

Copy

Ask AI

    curl --request DELETE \
      --url https://api.elections.kalshi.com/trade-api/v2/api_keys/{api_key} \
      --header 'KALSHI-ACCESS-KEY: <api-key>' \
      --header 'KALSHI-ACCESS-SIGNATURE: <api-key>' \
      --header 'KALSHI-ACCESS-TIMESTAMP: <api-key>'

#### Authorizations

[​](https://docs.kalshi.com/api-reference/api-keys/delete-api-key#authorization-kalshi-access-key)

KALSHI-ACCESS-KEY

string

header

required

Your API key ID

[​](https://docs.kalshi.com/api-reference/api-keys/delete-api-key#authorization-kalshi-access-signature)

KALSHI-ACCESS-SIGNATURE

string

header

required

RSA-PSS signature of the request

[​](https://docs.kalshi.com/api-reference/api-keys/delete-api-key#authorization-kalshi-access-timestamp)

KALSHI-ACCESS-TIMESTAMP

string

header

required

Request timestamp in milliseconds

#### Path Parameters

[​](https://docs.kalshi.com/api-reference/api-keys/delete-api-key#parameter-api-key)

api\_key

string

required

API key ID to delete

#### Response

204

API key successfully deleted

[Generate API Key](https://docs.kalshi.com/api-reference/api-keys/generate-api-key)
[Get Tags for Series Categories](https://docs.kalshi.com/api-reference/search/get-tags-for-series-categories)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.