---
url: https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi
title: MultivariateCollections - API Documentation
description: TypeScript SDK methods for MultivariateCollections operations
scraped_at: 2025-11-03T14:46:46.420565
---

[Skip to main content](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

API Classes

MultivariateCollections

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

On this page

*   [getMultivariateEventCollection](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#getmultivariateeventcollection)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#example)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#parameters)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#return-type)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#authorization)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#http-request-headers)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#http-response-details)
    
*   [getMultivariateEventCollections](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#getmultivariateeventcollections)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#example-2)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#parameters-2)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#return-type-2)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#authorization-2)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#http-request-headers-2)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#http-response-details-2)
    
*   [lookupMultivariateEventCollectionBundle](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#lookupmultivariateeventcollectionbundle)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#example-3)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#parameters-3)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#return-type-3)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#authorization-3)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#http-request-headers-3)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#http-response-details-3)
    

All URIs are relative to _[https://api.elections.kalshi.com/trade-api/v2](https://api.elections.kalshi.com/trade-api/v2)
_

| Method | HTTP request | Description |
| --- | --- | --- |
| [**getMultivariateEventCollection**](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#getmultivariateeventcollection) | **GET** /multivariate\_event\_collections/ | Get Multivariate Event Collection |
| [**getMultivariateEventCollections**](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#getmultivariateeventcollections) | **GET** /multivariate\_event\_collections | Get Multivariate Event Collections |
| [**lookupMultivariateEventCollectionBundle**](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#lookupmultivariateeventcollectionbundle) | **POST** /multivariate\_event\_collections//lookup | Lookup Multivariate Event Collection Bundle |

[​](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#getmultivariateeventcollection)

**getMultivariateEventCollection**
===============================================================================================================================================

> GetMultivariateEventCollectionResponse getMultivariateEventCollection()

Get a single multivariate event collection by ticker

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#example)

Example

Copy

Ask AI

    import {
        MultivariateCollectionsApi,
        Configuration
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new MultivariateCollectionsApi(configuration);
    
    let collectionTicker: string; //Collection ticker (default to undefined)
    
    const { status, data } = await apiInstance.getMultivariateEventCollection(
        collectionTicker
    );
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#parameters)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **collectionTicker** | \[**string**\] | Collection ticker | defaults to undefined |

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#return-type)

Return type

**GetMultivariateEventCollectionResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#authorization)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#http-request-headers)

HTTP request headers

*   **Content-Type**: Not defined
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#http-response-details)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **200** | Collection retrieved successfully | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **404** | Resource not found | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[​](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#getmultivariateeventcollections)

**getMultivariateEventCollections**
=================================================================================================================================================

> GetMultivariateEventCollectionsResponse getMultivariateEventCollections()

Get all multivariate event collections

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#example-2)

Example

Copy

Ask AI

    import {
        MultivariateCollectionsApi,
        Configuration
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new MultivariateCollectionsApi(configuration);
    
    let status: string; //Filter by multivariate collection status (optional) (default to undefined)
    
    const { status, data } = await apiInstance.getMultivariateEventCollections(
        status
    );
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#parameters-2)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **status** | \[**string**\] | Filter by multivariate collection status | (optional) defaults to undefined |

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#return-type-2)

Return type

**GetMultivariateEventCollectionsResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#authorization-2)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#http-request-headers-2)

HTTP request headers

*   **Content-Type**: Not defined
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#http-response-details-2)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **200** | Collections retrieved successfully | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[​](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#lookupmultivariateeventcollectionbundle)

**lookupMultivariateEventCollectionBundle**
=================================================================================================================================================================

> LookupBundleResponse lookupMultivariateEventCollectionBundle(lookupBundleRequest)

Lookup a bundle in a multivariate event collection

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#example-3)

Example

Copy

Ask AI

    import {
        MultivariateCollectionsApi,
        Configuration,
        LookupBundleRequest
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new MultivariateCollectionsApi(configuration);
    
    let collectionTicker: string; //Collection ticker (default to undefined)
    let lookupBundleRequest: LookupBundleRequest; //
    
    const { status, data } = await apiInstance.lookupMultivariateEventCollectionBundle(
        collectionTicker,
        lookupBundleRequest
    );
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#parameters-3)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **lookupBundleRequest** | **LookupBundleRequest** |     |     |
| **collectionTicker** | \[**string**\] | Collection ticker | defaults to undefined |

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#return-type-3)

Return type

**LookupBundleResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#authorization-3)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#http-request-headers-3)

HTTP request headers

*   **Content-Type**: application/json
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#http-response-details-3)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **200** | Bundle lookup successful | \-  |
| **400** | Bad request - invalid input | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **404** | Resource not found | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[Milestones](https://docs.kalshi.com/typescript-sdk/api/MilestonesApi)
[StructuredTargets](https://docs.kalshi.com/typescript-sdk/api/StructuredTargetsApi)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.