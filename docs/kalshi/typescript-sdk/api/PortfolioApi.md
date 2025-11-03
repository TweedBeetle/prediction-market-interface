---
url: https://docs.kalshi.com/typescript-sdk/api/PortfolioApi
title: Portfolio - API Documentation
description: TypeScript SDK methods for Portfolio operations
scraped_at: 2025-11-03T14:46:47.543417
---

[Skip to main content](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

API Classes

Portfolio

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

On this page

*   [amendOrder](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#amendorder)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#example)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#parameters)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#return-type)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#authorization)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-request-headers)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-response-details)
    
*   [batchCancelOrders](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#batchcancelorders)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#example-2)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#parameters-2)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#return-type-2)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#authorization-2)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-request-headers-2)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-response-details-2)
    
*   [batchCreateOrders](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#batchcreateorders)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#example-3)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#parameters-3)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#return-type-3)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#authorization-3)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-request-headers-3)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-response-details-3)
    
*   [cancelOrder](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#cancelorder)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#example-4)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#parameters-4)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#return-type-4)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#authorization-4)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-request-headers-4)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-response-details-4)
    
*   [createOrder](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#createorder)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#example-5)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#parameters-5)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#return-type-5)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#authorization-5)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-request-headers-5)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-response-details-5)
    
*   [createOrderGroup](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#createordergroup)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#example-6)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#parameters-6)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#return-type-6)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#authorization-6)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-request-headers-6)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-response-details-6)
    
*   [decreaseOrder](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#decreaseorder)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#example-7)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#parameters-7)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#return-type-7)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#authorization-7)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-request-headers-7)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-response-details-7)
    
*   [deleteOrderGroup](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#deleteordergroup)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#example-8)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#parameters-8)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#return-type-8)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#authorization-8)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-request-headers-8)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-response-details-8)
    
*   [getBalance](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#getbalance)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#example-9)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#parameters-9)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#return-type-9)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#authorization-9)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-request-headers-9)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-response-details-9)
    
*   [getFills](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#getfills)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#example-10)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#parameters-10)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#return-type-10)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#authorization-10)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-request-headers-10)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-response-details-10)
    
*   [getOrder](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#getorder)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#example-11)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#parameters-11)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#return-type-11)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#authorization-11)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-request-headers-11)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-response-details-11)
    
*   [getOrderGroup](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#getordergroup)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#example-12)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#parameters-12)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#return-type-12)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#authorization-12)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-request-headers-12)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-response-details-12)
    
*   [getOrderGroups](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#getordergroups)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#example-13)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#parameters-13)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#return-type-13)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#authorization-13)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-request-headers-13)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-response-details-13)
    
*   [getOrderQueuePosition](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#getorderqueueposition)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#example-14)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#parameters-14)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#return-type-14)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#authorization-14)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-request-headers-14)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-response-details-14)
    
*   [getOrders](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#getorders)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#example-15)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#parameters-15)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#return-type-15)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#authorization-15)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-request-headers-15)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-response-details-15)
    
*   [getPositions](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#getpositions)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#example-16)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#parameters-16)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#return-type-16)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#authorization-16)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-request-headers-16)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-response-details-16)
    
*   [getQueuePositions](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#getqueuepositions)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#example-17)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#parameters-17)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#return-type-17)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#authorization-17)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-request-headers-17)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-response-details-17)
    
*   [getSettlements](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#getsettlements)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#example-18)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#parameters-18)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#return-type-18)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#authorization-18)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-request-headers-18)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-response-details-18)
    
*   [getTotalRestingOrderValue](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#gettotalrestingordervalue)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#example-19)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#parameters-19)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#return-type-19)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#authorization-19)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-request-headers-19)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-response-details-19)
    
*   [resetOrderGroup](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#resetordergroup)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#example-20)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#parameters-20)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#return-type-20)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#authorization-20)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-request-headers-20)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-response-details-20)
    

All URIs are relative to _[https://api.elections.kalshi.com/trade-api/v2](https://api.elections.kalshi.com/trade-api/v2)
_

| Method | HTTP request | Description |
| --- | --- | --- |
| [**amendOrder**](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#amendorder) | **POST** /portfolio/orders//amend | Amend Order |
| [**batchCancelOrders**](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#batchcancelorders) | **DELETE** /portfolio/orders/batched | Batch Cancel Orders |
| [**batchCreateOrders**](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#batchcreateorders) | **POST** /portfolio/orders/batched | Batch Create Orders |
| [**cancelOrder**](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#cancelorder) | **DELETE** /portfolio/orders/ | Cancel Order |
| [**createOrder**](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#createorder) | **POST** /portfolio/orders | Create Order |
| [**createOrderGroup**](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#createordergroup) | **POST** /portfolio/order\_groups/create | Create Order Group |
| [**decreaseOrder**](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#decreaseorder) | **POST** /portfolio/orders//decrease | Decrease Order |
| [**deleteOrderGroup**](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#deleteordergroup) | **DELETE** /portfolio/order\_groups/ | Delete Order Group |
| [**getBalance**](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#getbalance) | **GET** /portfolio/balance | Get Balance |
| [**getFills**](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#getfills) | **GET** /portfolio/fills | Get Fills |
| [**getOrder**](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#getorder) | **GET** /portfolio/orders/ | Get Order |
| [**getOrderGroup**](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#getordergroup) | **GET** /portfolio/order\_groups/ | Get Order Group |
| [**getOrderGroups**](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#getordergroups) | **GET** /portfolio/order\_groups | Get Order Groups |
| [**getOrderQueuePosition**](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#getorderqueueposition) | **GET** /portfolio/orders//queue\_position | Get Order Queue Position |
| [**getOrders**](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#getorders) | **GET** /portfolio/orders | Get Orders |
| [**getPositions**](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#getpositions) | **GET** /portfolio/positions | Get Positions |
| [**getQueuePositions**](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#getqueuepositions) | **POST** /portfolio/orders/queue\_positions | Get Queue Positions |
| [**getSettlements**](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#getsettlements) | **GET** /portfolio/settlements | Get Settlements |
| [**getTotalRestingOrderValue**](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#gettotalrestingordervalue) | **GET** /portfolio/summary/total\_resting\_order\_value | Get Total Resting Order Value |
| [**resetOrderGroup**](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#resetordergroup) | **PUT** /portfolio/order\_groups//reset | Reset Order Group |

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#amendorder)

**amendOrder**
=========================================================================================

> AmendOrderResponse amendOrder(amendOrderRequest)

Amend an existing order

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#example)

Example

Copy

Ask AI

    import {
        PortfolioApi,
        Configuration,
        AmendOrderRequest
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new PortfolioApi(configuration);
    
    let orderId: string; //Order ID (default to undefined)
    let amendOrderRequest: AmendOrderRequest; //
    
    const { status, data } = await apiInstance.amendOrder(
        orderId,
        amendOrderRequest
    );
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#parameters)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **amendOrderRequest** | **AmendOrderRequest** |     |     |
| **orderId** | \[**string**\] | Order ID | defaults to undefined |

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#return-type)

Return type

**AmendOrderResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#authorization)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-request-headers)

HTTP request headers

*   **Content-Type**: application/json
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-response-details)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **200** | Order amended successfully | \-  |
| **400** | Bad request - invalid input | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **404** | Resource not found | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#batchcancelorders)

**batchCancelOrders**
=======================================================================================================

> BatchCancelOrdersResponse batchCancelOrders(batchCancelOrdersRequest)

Cancel multiple orders in a single request

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#example-2)

Example

Copy

Ask AI

    import {
        PortfolioApi,
        Configuration,
        BatchCancelOrdersRequest
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new PortfolioApi(configuration);
    
    let batchCancelOrdersRequest: BatchCancelOrdersRequest; //
    
    const { status, data } = await apiInstance.batchCancelOrders(
        batchCancelOrdersRequest
    );
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#parameters-2)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **batchCancelOrdersRequest** | **BatchCancelOrdersRequest** |     |     |

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#return-type-2)

Return type

**BatchCancelOrdersResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#authorization-2)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-request-headers-2)

HTTP request headers

*   **Content-Type**: application/json
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-response-details-2)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **200** | Batch order cancellation completed | \-  |
| **400** | Bad request - invalid input | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#batchcreateorders)

**batchCreateOrders**
=======================================================================================================

> BatchCreateOrdersResponse batchCreateOrders(batchCreateOrdersRequest)

Create multiple orders in a single request

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#example-3)

Example

Copy

Ask AI

    import {
        PortfolioApi,
        Configuration,
        BatchCreateOrdersRequest
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new PortfolioApi(configuration);
    
    let batchCreateOrdersRequest: BatchCreateOrdersRequest; //
    
    const { status, data } = await apiInstance.batchCreateOrders(
        batchCreateOrdersRequest
    );
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#parameters-3)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **batchCreateOrdersRequest** | **BatchCreateOrdersRequest** |     |     |

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#return-type-3)

Return type

**BatchCreateOrdersResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#authorization-3)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-request-headers-3)

HTTP request headers

*   **Content-Type**: application/json
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-response-details-3)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **200** | Batch order creation completed | \-  |
| **400** | Bad request - invalid input | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#cancelorder)

**cancelOrder**
===========================================================================================

> CancelOrderResponse cancelOrder()

Cancel an order

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#example-4)

Example

Copy

Ask AI

    import {
        PortfolioApi,
        Configuration
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new PortfolioApi(configuration);
    
    let orderId: string; //Order ID (default to undefined)
    
    const { status, data } = await apiInstance.cancelOrder(
        orderId
    );
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#parameters-4)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **orderId** | \[**string**\] | Order ID | defaults to undefined |

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#return-type-4)

Return type

**CancelOrderResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#authorization-4)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-request-headers-4)

HTTP request headers

*   **Content-Type**: Not defined
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-response-details-4)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **200** | Order cancelled successfully | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **404** | Resource not found | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#createorder)

**createOrder**
===========================================================================================

> CreateOrderResponse createOrder(createOrderRequest)

Create a new order

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#example-5)

Example

Copy

Ask AI

    import {
        PortfolioApi,
        Configuration,
        CreateOrderRequest
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new PortfolioApi(configuration);
    
    let createOrderRequest: CreateOrderRequest; //
    
    const { status, data } = await apiInstance.createOrder(
        createOrderRequest
    );
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#parameters-5)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **createOrderRequest** | **CreateOrderRequest** |     |     |

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#return-type-5)

Return type

**CreateOrderResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#authorization-5)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-request-headers-5)

HTTP request headers

*   **Content-Type**: application/json
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-response-details-5)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **201** | Order created successfully | \-  |
| **400** | Bad request - invalid input | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **429** | Too Many Requests - rate limit exceeded | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#createordergroup)

**createOrderGroup**
=====================================================================================================

> CreateOrderGroupResponse createOrderGroup(createOrderGroupRequest)

Create a new order group

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#example-6)

Example

Copy

Ask AI

    import {
        PortfolioApi,
        Configuration,
        CreateOrderGroupRequest
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new PortfolioApi(configuration);
    
    let createOrderGroupRequest: CreateOrderGroupRequest; //
    
    const { status, data } = await apiInstance.createOrderGroup(
        createOrderGroupRequest
    );
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#parameters-6)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **createOrderGroupRequest** | **CreateOrderGroupRequest** |     |     |

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#return-type-6)

Return type

**CreateOrderGroupResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#authorization-6)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-request-headers-6)

HTTP request headers

*   **Content-Type**: application/json
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-response-details-6)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **201** | Order group created successfully | \-  |
| **400** | Bad request - invalid input | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#decreaseorder)

**decreaseOrder**
===============================================================================================

> DecreaseOrderResponse decreaseOrder(decreaseOrderRequest)

Decrease the size of an existing order

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#example-7)

Example

Copy

Ask AI

    import {
        PortfolioApi,
        Configuration,
        DecreaseOrderRequest
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new PortfolioApi(configuration);
    
    let orderId: string; //Order ID (default to undefined)
    let decreaseOrderRequest: DecreaseOrderRequest; //
    
    const { status, data } = await apiInstance.decreaseOrder(
        orderId,
        decreaseOrderRequest
    );
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#parameters-7)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **decreaseOrderRequest** | **DecreaseOrderRequest** |     |     |
| **orderId** | \[**string**\] | Order ID | defaults to undefined |

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#return-type-7)

Return type

**DecreaseOrderResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#authorization-7)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-request-headers-7)

HTTP request headers

*   **Content-Type**: application/json
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-response-details-7)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **200** | Order decreased successfully | \-  |
| **400** | Bad request - invalid input | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **404** | Resource not found | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#deleteordergroup)

**deleteOrderGroup**
=====================================================================================================

> deleteOrderGroup()

Delete an order group

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#example-8)

Example

Copy

Ask AI

    import {
        PortfolioApi,
        Configuration
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new PortfolioApi(configuration);
    
    let orderGroupId: string; //Order group ID (default to undefined)
    
    const { status, data } = await apiInstance.deleteOrderGroup(
        orderGroupId
    );
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#parameters-8)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **orderGroupId** | \[**string**\] | Order group ID | defaults to undefined |

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#return-type-8)

Return type

void (empty response body)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#authorization-8)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-request-headers-8)

HTTP request headers

*   **Content-Type**: Not defined
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-response-details-8)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **204** | Order group deleted successfully | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **404** | Resource not found | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#getbalance)

**getBalance**
=========================================================================================

> GetBalanceResponse getBalance()

Get the user’s current balance

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#example-9)

Example

Copy

Ask AI

    import {
        PortfolioApi,
        Configuration
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new PortfolioApi(configuration);
    
    const { status, data } = await apiInstance.getBalance();
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#parameters-9)

Parameters

This endpoint does not have any parameters.

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#return-type-9)

Return type

**GetBalanceResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#authorization-9)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-request-headers-9)

HTTP request headers

*   **Content-Type**: Not defined
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-response-details-9)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **200** | Balance retrieved successfully | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#getfills)

**getFills**
=====================================================================================

> GetFillsResponse getFills()

Get fills for the logged-in user. A fill represents a partial or complete execution of an order. When an order matches with another order in the orderbook, a fill is created for each side of the trade.

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#example-10)

Example

Copy

Ask AI

    import {
        PortfolioApi,
        Configuration
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new PortfolioApi(configuration);
    
    let ticker: string; //Filter by market ticker (optional) (default to undefined)
    let orderId: string; //Filter by order ID (optional) (default to undefined)
    let minTs: number; //Filter items after this Unix timestamp (optional) (default to undefined)
    let maxTs: number; //Filter items before this Unix timestamp (optional) (default to undefined)
    let limit: number; //Number of results per page. Defaults to 100. Maximum value is 200. (optional) (default to 100)
    let cursor: string; //Pagination cursor. Use the cursor value returned from the previous response to get the next page of results. Leave empty for the first page. (optional) (default to undefined)
    
    const { status, data } = await apiInstance.getFills(
        ticker,
        orderId,
        minTs,
        maxTs,
        limit,
        cursor
    );
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#parameters-10)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **ticker** | \[**string**\] | Filter by market ticker | (optional) defaults to undefined |
| **orderId** | \[**string**\] | Filter by order ID | (optional) defaults to undefined |
| **minTs** | \[**number**\] | Filter items after this Unix timestamp | (optional) defaults to undefined |
| **maxTs** | \[**number**\] | Filter items before this Unix timestamp | (optional) defaults to undefined |
| **limit** | \[**number**\] | Number of results per page. Defaults to 100. Maximum value is 200. | (optional) defaults to 100 |
| **cursor** | \[**string**\] | Pagination cursor. Use the cursor value returned from the previous response to get the next page of results. Leave empty for the first page. | (optional) defaults to undefined |

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#return-type-10)

Return type

**GetFillsResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#authorization-10)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-request-headers-10)

HTTP request headers

*   **Content-Type**: Not defined
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-response-details-10)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **200** | Fills retrieved successfully | \-  |
| **400** | Bad request - invalid input | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#getorder)

**getOrder**
=====================================================================================

> GetOrderResponse getOrder()

Get a single order by ID

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#example-11)

Example

Copy

Ask AI

    import {
        PortfolioApi,
        Configuration
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new PortfolioApi(configuration);
    
    let orderId: string; //Order ID (default to undefined)
    
    const { status, data } = await apiInstance.getOrder(
        orderId
    );
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#parameters-11)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **orderId** | \[**string**\] | Order ID | defaults to undefined |

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#return-type-11)

Return type

**GetOrderResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#authorization-11)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-request-headers-11)

HTTP request headers

*   **Content-Type**: Not defined
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-response-details-11)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **200** | Order retrieved successfully | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **404** | Resource not found | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#getordergroup)

**getOrderGroup**
===============================================================================================

> GetOrderGroupResponse getOrderGroup()

Get details of a specific order group

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#example-12)

Example

Copy

Ask AI

    import {
        PortfolioApi,
        Configuration
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new PortfolioApi(configuration);
    
    let orderGroupId: string; //Order group ID (default to undefined)
    
    const { status, data } = await apiInstance.getOrderGroup(
        orderGroupId
    );
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#parameters-12)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **orderGroupId** | \[**string**\] | Order group ID | defaults to undefined |

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#return-type-12)

Return type

**GetOrderGroupResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#authorization-12)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-request-headers-12)

HTTP request headers

*   **Content-Type**: Not defined
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-response-details-12)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **200** | Order group retrieved successfully | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **404** | Resource not found | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#getordergroups)

**getOrderGroups**
=================================================================================================

> GetOrderGroupsResponse getOrderGroups()

Get order groups for the logged-in user

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#example-13)

Example

Copy

Ask AI

    import {
        PortfolioApi,
        Configuration
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new PortfolioApi(configuration);
    
    let status: string; //Filter by status. Possible values depend on the endpoint. (optional) (default to undefined)
    let limit: number; //Number of results per page. Defaults to 100. Maximum value is 200. (optional) (default to 100)
    let cursor: string; //Pagination cursor. Use the cursor value returned from the previous response to get the next page of results. Leave empty for the first page. (optional) (default to undefined)
    
    const { status, data } = await apiInstance.getOrderGroups(
        status,
        limit,
        cursor
    );
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#parameters-13)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **status** | \[**string**\] | Filter by status. Possible values depend on the endpoint. | (optional) defaults to undefined |
| **limit** | \[**number**\] | Number of results per page. Defaults to 100. Maximum value is 200. | (optional) defaults to 100 |
| **cursor** | \[**string**\] | Pagination cursor. Use the cursor value returned from the previous response to get the next page of results. Leave empty for the first page. | (optional) defaults to undefined |

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#return-type-13)

Return type

**GetOrderGroupsResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#authorization-13)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-request-headers-13)

HTTP request headers

*   **Content-Type**: Not defined
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-response-details-13)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **200** | Order groups retrieved successfully | \-  |
| **400** | Bad request - invalid input | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#getorderqueueposition)

**getOrderQueuePosition**
===============================================================================================================

> GetOrderQueuePositionResponse getOrderQueuePosition()

Get the queue position for an order

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#example-14)

Example

Copy

Ask AI

    import {
        PortfolioApi,
        Configuration
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new PortfolioApi(configuration);
    
    let orderId: string; //Order ID (default to undefined)
    
    const { status, data } = await apiInstance.getOrderQueuePosition(
        orderId
    );
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#parameters-14)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **orderId** | \[**string**\] | Order ID | defaults to undefined |

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#return-type-14)

Return type

**GetOrderQueuePositionResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#authorization-14)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-request-headers-14)

HTTP request headers

*   **Content-Type**: Not defined
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-response-details-14)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **200** | Queue position retrieved successfully | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **404** | Resource not found | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#getorders)

**getOrders**
=======================================================================================

> GetOrdersResponse getOrders()

Get orders for the logged-in user

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#example-15)

Example

Copy

Ask AI

    import {
        PortfolioApi,
        Configuration
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new PortfolioApi(configuration);
    
    let ticker: string; //Filter by market ticker (optional) (default to undefined)
    let eventTicker: string; //Filter by event ticker (optional) (default to undefined)
    let minTs: number; //Filter items after this Unix timestamp (optional) (default to undefined)
    let maxTs: number; //Filter items before this Unix timestamp (optional) (default to undefined)
    let status: string; //Filter by status. Possible values depend on the endpoint. (optional) (default to undefined)
    let limit: number; //Number of results per page. Defaults to 100. Maximum value is 200. (optional) (default to 100)
    let cursor: string; //Pagination cursor. Use the cursor value returned from the previous response to get the next page of results. Leave empty for the first page. (optional) (default to undefined)
    
    const { status, data } = await apiInstance.getOrders(
        ticker,
        eventTicker,
        minTs,
        maxTs,
        status,
        limit,
        cursor
    );
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#parameters-15)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **ticker** | \[**string**\] | Filter by market ticker | (optional) defaults to undefined |
| **eventTicker** | \[**string**\] | Filter by event ticker | (optional) defaults to undefined |
| **minTs** | \[**number**\] | Filter items after this Unix timestamp | (optional) defaults to undefined |
| **maxTs** | \[**number**\] | Filter items before this Unix timestamp | (optional) defaults to undefined |
| **status** | \[**string**\] | Filter by status. Possible values depend on the endpoint. | (optional) defaults to undefined |
| **limit** | \[**number**\] | Number of results per page. Defaults to 100. Maximum value is 200. | (optional) defaults to 100 |
| **cursor** | \[**string**\] | Pagination cursor. Use the cursor value returned from the previous response to get the next page of results. Leave empty for the first page. | (optional) defaults to undefined |

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#return-type-15)

Return type

**GetOrdersResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#authorization-15)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-request-headers-15)

HTTP request headers

*   **Content-Type**: Not defined
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-response-details-15)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **200** | Orders retrieved successfully | \-  |
| **400** | Bad request - invalid input | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#getpositions)

**getPositions**
=============================================================================================

> GetPositionsResponse getPositions()

Get positions for the logged-in user

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#example-16)

Example

Copy

Ask AI

    import {
        PortfolioApi,
        Configuration
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new PortfolioApi(configuration);
    
    let ticker: string; //Filter by market ticker (optional) (default to undefined)
    let eventTicker: string; //Filter by event ticker (optional) (default to undefined)
    let countDown: number; //Filter positions by minimum count down value (optional) (default to undefined)
    let countUp: number; //Filter positions by minimum count up value (optional) (default to undefined)
    let limit: number; //Number of results per page. Defaults to 100. Maximum value is 200. (optional) (default to 100)
    let cursor: string; //Pagination cursor. Use the cursor value returned from the previous response to get the next page of results. Leave empty for the first page. (optional) (default to undefined)
    
    const { status, data } = await apiInstance.getPositions(
        ticker,
        eventTicker,
        countDown,
        countUp,
        limit,
        cursor
    );
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#parameters-16)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **ticker** | \[**string**\] | Filter by market ticker | (optional) defaults to undefined |
| **eventTicker** | \[**string**\] | Filter by event ticker | (optional) defaults to undefined |
| **countDown** | \[**number**\] | Filter positions by minimum count down value | (optional) defaults to undefined |
| **countUp** | \[**number**\] | Filter positions by minimum count up value | (optional) defaults to undefined |
| **limit** | \[**number**\] | Number of results per page. Defaults to 100. Maximum value is 200. | (optional) defaults to 100 |
| **cursor** | \[**string**\] | Pagination cursor. Use the cursor value returned from the previous response to get the next page of results. Leave empty for the first page. | (optional) defaults to undefined |

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#return-type-16)

Return type

**GetPositionsResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#authorization-16)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-request-headers-16)

HTTP request headers

*   **Content-Type**: Not defined
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-response-details-16)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **200** | Positions retrieved successfully | \-  |
| **400** | Bad request - invalid input | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#getqueuepositions)

**getQueuePositions**
=======================================================================================================

> GetQueuePositionsResponse getQueuePositions(getQueuePositionsRequest)

Get queue positions for multiple orders

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#example-17)

Example

Copy

Ask AI

    import {
        PortfolioApi,
        Configuration,
        GetQueuePositionsRequest
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new PortfolioApi(configuration);
    
    let getQueuePositionsRequest: GetQueuePositionsRequest; //
    
    const { status, data } = await apiInstance.getQueuePositions(
        getQueuePositionsRequest
    );
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#parameters-17)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **getQueuePositionsRequest** | **GetQueuePositionsRequest** |     |     |

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#return-type-17)

Return type

**GetQueuePositionsResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#authorization-17)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-request-headers-17)

HTTP request headers

*   **Content-Type**: application/json
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-response-details-17)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **200** | Queue positions retrieved successfully | \-  |
| **400** | Bad request - invalid input | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#getsettlements)

**getSettlements**
=================================================================================================

> GetSettlementsResponse getSettlements()

Get settlements for the logged-in user

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#example-18)

Example

Copy

Ask AI

    import {
        PortfolioApi,
        Configuration
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new PortfolioApi(configuration);
    
    let limit: number; //Number of results per page. Defaults to 100. Maximum value is 200. (optional) (default to 100)
    let cursor: string; //Pagination cursor. Use the cursor value returned from the previous response to get the next page of results. Leave empty for the first page. (optional) (default to undefined)
    
    const { status, data } = await apiInstance.getSettlements(
        limit,
        cursor
    );
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#parameters-18)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **limit** | \[**number**\] | Number of results per page. Defaults to 100. Maximum value is 200. | (optional) defaults to 100 |
| **cursor** | \[**string**\] | Pagination cursor. Use the cursor value returned from the previous response to get the next page of results. Leave empty for the first page. | (optional) defaults to undefined |

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#return-type-18)

Return type

**GetSettlementsResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#authorization-18)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-request-headers-18)

HTTP request headers

*   **Content-Type**: Not defined
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-response-details-18)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **200** | Settlements retrieved successfully | \-  |
| **400** | Bad request - invalid input | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#gettotalrestingordervalue)

**getTotalRestingOrderValue**
=======================================================================================================================

> GetTotalRestingOrderValueResponse getTotalRestingOrderValue()

Get the total value of all resting orders

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#example-19)

Example

Copy

Ask AI

    import {
        PortfolioApi,
        Configuration
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new PortfolioApi(configuration);
    
    const { status, data } = await apiInstance.getTotalRestingOrderValue();
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#parameters-19)

Parameters

This endpoint does not have any parameters.

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#return-type-19)

Return type

**GetTotalRestingOrderValueResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#authorization-19)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-request-headers-19)

HTTP request headers

*   **Content-Type**: Not defined
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-response-details-19)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **200** | Total resting order value retrieved successfully | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#resetordergroup)

**resetOrderGroup**
===================================================================================================

> resetOrderGroup()

Reset an order group

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#example-20)

Example

Copy

Ask AI

    import {
        PortfolioApi,
        Configuration
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new PortfolioApi(configuration);
    
    let orderGroupId: string; //Order group ID (default to undefined)
    
    const { status, data } = await apiInstance.resetOrderGroup(
        orderGroupId
    );
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#parameters-20)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **orderGroupId** | \[**string**\] | Order group ID | defaults to undefined |

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#return-type-20)

Return type

void (empty response body)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#authorization-20)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-request-headers-20)

HTTP request headers

*   **Content-Type**: Not defined
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#http-response-details-20)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **204** | Order group reset successfully | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **404** | Resource not found | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[TypeScript SDK Quick Start](https://docs.kalshi.com/sdks/typescript/quickstart)
[Markets](https://docs.kalshi.com/typescript-sdk/api/MarketsApi)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.