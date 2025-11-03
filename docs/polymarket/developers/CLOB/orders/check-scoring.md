---
url: https://docs.polymarket.com/developers/CLOB/orders/check-scoring
title: Check Order Reward Scoring - Polymarket Documentation
description: Check if an order is eligble or scoring for Rewards purposes
scraped_at: 2025-11-03T15:03:57.644885
---

[Skip to main content](https://docs.polymarket.com/developers/CLOB/orders/check-scoring#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

Ctrl K

Search...

Navigation

Order Manipulation

Check Order Reward Scoring

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

Python

Typescript

Copy

Ask AI

scoring = client.is_order_scoring(
        OrderScoringParams(
            orderId="0x..."
        )
    )
    print(scoring)
    
    scoring = client.are_orders_scoring(
        OrdersScoringParams(
            orderIds=["0x..."]
        )
    )
    print(scoring)

This endpoint requires a L2 Header.

Returns a boolean value where it is indicated if an order is scoring or not. **HTTP REQUEST** `GET /<clob-endpoint>/order-scoring?order_id={...}`

### 

[​](https://docs.polymarket.com/developers/CLOB/orders/check-scoring#request-parameters)

Request Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| orderId | yes | string | id of order to get information about |

### 

[​](https://docs.polymarket.com/developers/CLOB/orders/check-scoring#response-format)

Response Format

| Name | Type | Description |
| --- | --- | --- |
| null | OrdersScoring | order scoring data |

An `OrdersScoring` object is of the form:

| Name | Type | Description |
| --- | --- | --- |
| scoring | boolean | indicates if the order is scoring or not |

[​](https://docs.polymarket.com/developers/CLOB/orders/check-scoring#check-if-some-orders-are-scoring)

Check if some orders are scoring
==========================================================================================================================================

> This endpoint requires a L2 Header.

Returns to a dictionary with boolean value where it is indicated if an order is scoring or not. **HTTP REQUEST** `POST /<clob-endpoint>/orders-scoring`

### 

[​](https://docs.polymarket.com/developers/CLOB/orders/check-scoring#request-parameters-2)

Request Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| orderIds | yes | string\[\] | ids of the orders to get information about |

### 

[​](https://docs.polymarket.com/developers/CLOB/orders/check-scoring#response-format-2)

Response Format

| Name | Type | Description |
| --- | --- | --- |
| null | OrdersScoring | orders scoring data |

An `OrdersScoring` object is a dictionary that indicates the order by if it score.

[Get Active Orders](https://docs.polymarket.com/developers/CLOB/orders/get-active-order)
[Cancel Orders(s)](https://docs.polymarket.com/developers/CLOB/orders/cancel-orders)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.