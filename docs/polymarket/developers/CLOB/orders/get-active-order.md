---
url: https://docs.polymarket.com/developers/CLOB/orders/get-active-order
title: Get Active Orders - Polymarket Documentation
scraped_at: 2025-11-03T15:03:58.189819
---

[Skip to main content](https://docs.polymarket.com/developers/CLOB/orders/get-active-order#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

Ctrl K

Search...

Navigation

Order Manipulation

Get Active Orders

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

Python

Typescript

Copy

Ask AI

from py_clob_client.clob_types import OpenOrderParams
    
    resp = client.get_orders(
        OpenOrderParams(
            market="0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",
        )
    )
    print(resp)
    print("Done!")

This endpoint requires a L2 Header.

Get active order(s) for a specific market. **HTTP REQUEST** `GET /<clob-endpoint>/data/orders`

### 

[​](https://docs.polymarket.com/developers/CLOB/orders/get-active-order#request-parameters)

Request Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| id  | no  | string | id of order to get information about |
| market | no  | string | condition id of market |
| asset\_id | no  | string | id of the asset/token |

### 

[​](https://docs.polymarket.com/developers/CLOB/orders/get-active-order#response-format)

Response Format

| Name | Type | Description |
| --- | --- | --- |
| null | OpenOrder\[\] | list of open orders filtered by the query parameters |

[Get Order](https://docs.polymarket.com/developers/CLOB/orders/get-order)
[Check Order Reward Scoring](https://docs.polymarket.com/developers/CLOB/orders/check-scoring)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.