---
url: https://docs.kalshi.com/api-reference/exchange/get-user-data-timestamp
title: Get User Data Timestamp - API Documentation
description:  There is typically a short delay before exchange events are reflected in the API endpoints. Whenever possible, combine API responses to PUT/POST/DELETE requests with websocket data to obtain the most accurate view of the exchange state. This endpoint provides an approximate indication of when the data from the following endpoints was last validated: GetBalance, GetOrder(s), GetFills, GetPositions
scraped_at: 2025-11-03T14:46:16.269482
---

[Skip to main content](https://docs.kalshi.com/api-reference/exchange/get-user-data-timestamp#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

exchange

Get User Data Timestamp

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

Get User Data Timestamp

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/exchange/user_data_timestamp

200

500

Copy

Ask AI

    {
      "as_of_time": "2023-11-07T05:31:56Z"
    }

GET

/

exchange

/

user\_data\_timestamp

Try it

Get User Data Timestamp

cURL

Copy

Ask AI

    curl --request GET \
      --url https://api.elections.kalshi.com/trade-api/v2/exchange/user_data_timestamp

200

500

Copy

Ask AI

    {
      "as_of_time": "2023-11-07T05:31:56Z"
    }

#### Response

200

application/json

User data timestamp retrieved successfully

[​](https://docs.kalshi.com/api-reference/exchange/get-user-data-timestamp#response-as-of-time)

as\_of\_time

string<date-time>

required

Timestamp when user data was last updated.

[Get Exchange Schedule](https://docs.kalshi.com/api-reference/exchange/get-exchange-schedule)
[Get Balance](https://docs.kalshi.com/api-reference/portfolio/get-balance)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.