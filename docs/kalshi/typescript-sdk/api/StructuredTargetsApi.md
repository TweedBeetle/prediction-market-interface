---
url: https://docs.kalshi.com/typescript-sdk/api/StructuredTargetsApi
title: StructuredTargets - API Documentation
description: TypeScript SDK methods for StructuredTargets operations
scraped_at: 2025-11-03T14:46:47.321023
---

[Skip to main content](https://docs.kalshi.com/typescript-sdk/api/StructuredTargetsApi#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

API Classes

StructuredTargets

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

On this page

*   [getStructuredTarget](https://docs.kalshi.com/typescript-sdk/api/StructuredTargetsApi#getstructuredtarget)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/StructuredTargetsApi#example)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/StructuredTargetsApi#parameters)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/StructuredTargetsApi#return-type)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/StructuredTargetsApi#authorization)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/StructuredTargetsApi#http-request-headers)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/StructuredTargetsApi#http-response-details)
    
*   [getStructuredTargets](https://docs.kalshi.com/typescript-sdk/api/StructuredTargetsApi#getstructuredtargets)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/StructuredTargetsApi#example-2)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/StructuredTargetsApi#parameters-2)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/StructuredTargetsApi#return-type-2)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/StructuredTargetsApi#authorization-2)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/StructuredTargetsApi#http-request-headers-2)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/StructuredTargetsApi#http-response-details-2)
    

All URIs are relative to _[https://api.elections.kalshi.com/trade-api/v2](https://api.elections.kalshi.com/trade-api/v2)
_

| Method | HTTP request | Description |
| --- | --- | --- |
| [**getStructuredTarget**](https://docs.kalshi.com/typescript-sdk/api/StructuredTargetsApi#getstructuredtarget) | **GET** /structured\_targets/ | Get Structured Target |
| [**getStructuredTargets**](https://docs.kalshi.com/typescript-sdk/api/StructuredTargetsApi#getstructuredtargets) | **GET** /structured\_targets | Get Structured Targets |

[​](https://docs.kalshi.com/typescript-sdk/api/StructuredTargetsApi#getstructuredtarget)

**getStructuredTarget**
===================================================================================================================

> GetStructuredTargetResponse getStructuredTarget()

Get a single structured target by ID

### 

[​](https://docs.kalshi.com/typescript-sdk/api/StructuredTargetsApi#example)

Example

Copy

Ask AI

    import {
        StructuredTargetsApi,
        Configuration
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new StructuredTargetsApi(configuration);
    
    let structuredTargetId: string; //Structured target ID (default to undefined)
    
    const { status, data } = await apiInstance.getStructuredTarget(
        structuredTargetId
    );
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/StructuredTargetsApi#parameters)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **structuredTargetId** | \[**string**\] | Structured target ID | defaults to undefined |

### 

[​](https://docs.kalshi.com/typescript-sdk/api/StructuredTargetsApi#return-type)

Return type

**GetStructuredTargetResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/StructuredTargetsApi#authorization)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/StructuredTargetsApi#http-request-headers)

HTTP request headers

*   **Content-Type**: Not defined
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/StructuredTargetsApi#http-response-details)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **200** | Structured target retrieved successfully | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **404** | Resource not found | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/StructuredTargetsApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[​](https://docs.kalshi.com/typescript-sdk/api/StructuredTargetsApi#getstructuredtargets)

**getStructuredTargets**
=====================================================================================================================

> GetStructuredTargetsResponse getStructuredTargets()

Get all structured targets

### 

[​](https://docs.kalshi.com/typescript-sdk/api/StructuredTargetsApi#example-2)

Example

Copy

Ask AI

    import {
        StructuredTargetsApi,
        Configuration
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new StructuredTargetsApi(configuration);
    
    let status: string; //Filter by structured target status (optional) (default to undefined)
    let pageSize: number; //Number of items per page (minimum 100, default 100) (optional) (default to 100)
    
    const { status, data } = await apiInstance.getStructuredTargets(
        status,
        pageSize
    );
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/StructuredTargetsApi#parameters-2)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **status** | \[**string**\] | Filter by structured target status | (optional) defaults to undefined |
| **pageSize** | \[**number**\] | Number of items per page (minimum 100, default 100) | (optional) defaults to 100 |

### 

[​](https://docs.kalshi.com/typescript-sdk/api/StructuredTargetsApi#return-type-2)

Return type

**GetStructuredTargetsResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/StructuredTargetsApi#authorization-2)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/StructuredTargetsApi#http-request-headers-2)

HTTP request headers

*   **Content-Type**: Not defined
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/StructuredTargetsApi#http-response-details-2)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **200** | Structured targets retrieved successfully | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/StructuredTargetsApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[MultivariateCollections](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi)
[Exchange](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.