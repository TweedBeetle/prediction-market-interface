---
url: https://docs.polymarket.com/developers/CLOB/orders/get-order
title: Get Order - Polymarket Documentation
description: Get information about an existing order
scraped_at: 2025-11-03T15:03:58.911826
---

[Skip to main content](https://docs.polymarket.com/developers/CLOB/orders/get-order#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

Ctrl K

Search...

Navigation

Order Manipulation

Get Order

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

Python

Typescript

Copy

Ask AI

order = clob_client.get_order("0xb816482a5187a3d3db49cbaf6fe3ddf24f53e6c712b5a4bf5e01d0ec7b11dabc")
    print(order)

This endpoint requires a L2 Header.

Get single order by id. **HTTP REQUEST** `GET /<clob-endpoint>/data/order/<order_hash>`

### 

[​](https://docs.polymarket.com/developers/CLOB/orders/get-order#request-parameters)

Request Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| id  | no  | string | id of order to get information about |

### 

[​](https://docs.polymarket.com/developers/CLOB/orders/get-order#response-format)

Response Format

| Name | Type | Description |
| --- | --- | --- |
| order | OpenOrder | order if it exists |

An `OpenOrder` object is of the form:

| Name | Type | Description |
| --- | --- | --- |
| associate\_trades | string\[\] | any Trade id the order has been partially included in |
| id  | string | order id |
| status | string | order current status |
| market | string | market id (condition id) |
| original\_size | string | original order size at placement |
| outcome | string | human readable outcome the order is for |
| maker\_address | string | maker address (funder) |
| owner | string | api key |
| price | string | price |
| side | string | buy or sell |
| size\_matched | string | size of order that has been matched/filled |
| asset\_id | string | token id |
| expiration | string | unix timestamp when the order expired, 0 if it does not expire |
| type | string | order type (GTC, FOK, GTD) |
| created\_at | string | unix timestamp when the order was created |

[Place Multiple Orders (Batching)](https://docs.polymarket.com/developers/CLOB/orders/create-order-batch)
[Get Active Orders](https://docs.polymarket.com/developers/CLOB/orders/get-active-order)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.