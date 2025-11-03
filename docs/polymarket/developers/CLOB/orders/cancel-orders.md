---
url: https://docs.polymarket.com/developers/CLOB/orders/cancel-orders
title: Cancel Orders(s) - Polymarket Documentation
description: Multiple endpoints to cancel a single order, multiple orders, all orders or all orders from a single market.
scraped_at: 2025-11-03T15:03:58.125307
---

[Skip to main content](https://docs.polymarket.com/developers/CLOB/orders/cancel-orders#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

Ctrl K

Search...

Navigation

Order Manipulation

Cancel Orders(s)

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

On this page

*   [Cancel an single Order](https://docs.polymarket.com/developers/CLOB/orders/cancel-orders#cancel-an-single-order)
    
*   [Request Payload Parameters](https://docs.polymarket.com/developers/CLOB/orders/cancel-orders#request-payload-parameters)
    
*   [Response Format](https://docs.polymarket.com/developers/CLOB/orders/cancel-orders#response-format)
    
*   [Cancel Multiple Orders](https://docs.polymarket.com/developers/CLOB/orders/cancel-orders#cancel-multiple-orders)
    
*   [Request Payload Parameters](https://docs.polymarket.com/developers/CLOB/orders/cancel-orders#request-payload-parameters-2)
    
*   [Response Format](https://docs.polymarket.com/developers/CLOB/orders/cancel-orders#response-format-2)
    
*   [Cancel ALL Orders](https://docs.polymarket.com/developers/CLOB/orders/cancel-orders#cancel-all-orders)
    
*   [Response Format](https://docs.polymarket.com/developers/CLOB/orders/cancel-orders#response-format-3)
    
*   [Cancel orders from market](https://docs.polymarket.com/developers/CLOB/orders/cancel-orders#cancel-orders-from-market)
    
*   [Request Payload Parameters](https://docs.polymarket.com/developers/CLOB/orders/cancel-orders#request-payload-parameters-3)
    
*   [Response Format](https://docs.polymarket.com/developers/CLOB/orders/cancel-orders#response-format-4)
    

[​](https://docs.polymarket.com/developers/CLOB/orders/cancel-orders#cancel-an-single-order)

Cancel an single Order
======================================================================================================================

This endpoint requires a L2 Header.

Cancel an order. **HTTP REQUEST** `DELETE /<clob-endpoint>/order`

### 

[​](https://docs.polymarket.com/developers/CLOB/orders/cancel-orders#request-payload-parameters)

Request Payload Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| orderID | yes | string | ID of order to cancel |

### 

[​](https://docs.polymarket.com/developers/CLOB/orders/cancel-orders#response-format)

Response Format

| Name | Type | Description |
| --- | --- | --- |
| canceled | string\[\] | list of canceled orders |
| not\_canceled |     | a order id -> reason map that explains why that order couldn’t be canceled |

Python

Typescript

Copy

Ask AI

    resp = client.cancel(order_id="0x38a73eed1e6d177545e9ab027abddfb7e08dbe975fa777123b1752d203d6ac88")
    print(resp)
    

[​](https://docs.polymarket.com/developers/CLOB/orders/cancel-orders#cancel-multiple-orders)

Cancel Multiple Orders
======================================================================================================================

This endpoint requires a L2 Header.

**HTTP REQUEST** `DELETE /<clob-endpoint>/orders`

### 

[​](https://docs.polymarket.com/developers/CLOB/orders/cancel-orders#request-payload-parameters-2)

Request Payload Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| null | yes | string\[\] | IDs of the orders to cancel |

### 

[​](https://docs.polymarket.com/developers/CLOB/orders/cancel-orders#response-format-2)

Response Format

| Name | Type | Description |
| --- | --- | --- |
| canceled | string\[\] | list of canceled orders |
| not\_canceled |     | a order id -> reason map that explains why that order couldn’t be canceled |

Python

Typescript

Copy

Ask AI

    resp = client.cancel_orders(["0x38a73eed1e6d177545e9ab027abddfb7e08dbe975fa777123b1752d203d6ac88", "0xaaaa..."])
    print(resp)
    

[​](https://docs.polymarket.com/developers/CLOB/orders/cancel-orders#cancel-all-orders)

Cancel ALL Orders
============================================================================================================

This endpoint requires a L2 Header.

Cancel all open orders posted by a user. **HTTP REQUEST** `DELETE /<clob-endpoint>/cancel-all`

### 

[​](https://docs.polymarket.com/developers/CLOB/orders/cancel-orders#response-format-3)

Response Format

| Name | Type | Description |
| --- | --- | --- |
| canceled | string\[\] | list of canceled orders |
| not\_canceled |     | a order id -> reason map that explains why that order couldn’t be canceled |

Python

Typescript

Copy

Ask AI

    resp = client.cancel_all()
    print(resp)
    print("Done!")
    

[​](https://docs.polymarket.com/developers/CLOB/orders/cancel-orders#cancel-orders-from-market)

Cancel orders from market
============================================================================================================================

This endpoint requires a L2 Header.

Cancel orders from market. **HTTP REQUEST** `DELETE /<clob-endpoint>/cancel-market-orders`

### 

[​](https://docs.polymarket.com/developers/CLOB/orders/cancel-orders#request-payload-parameters-3)

Request Payload Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| market | no  | string | condition id of the market |
| asset\_id | no  | string | id of the asset/token |

### 

[​](https://docs.polymarket.com/developers/CLOB/orders/cancel-orders#response-format-4)

Response Format

| Name | Type | Description |
| --- | --- | --- |
| canceled | string\[\] | list of canceled orders |
| not\_canceled |     | a order id -> reason map that explains why that order couldn’t be canceled |

Python

Typescript

Copy

Ask AI

    resp = client.cancel_market_orders(market="0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af", asset_id="52114319501245915516055106046884209969926127482827954674443846427813813222426")
    print(resp)
    
    

[Check Order Reward Scoring](https://docs.polymarket.com/developers/CLOB/orders/check-scoring)
[Onchain Order Info](https://docs.polymarket.com/developers/CLOB/orders/onchain-order-info)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.