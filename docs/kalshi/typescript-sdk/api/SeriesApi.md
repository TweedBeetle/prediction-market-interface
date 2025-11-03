---
url: https://docs.kalshi.com/typescript-sdk/api/SeriesApi
title: Series - API Documentation
description: TypeScript SDK methods for Series operations
scraped_at: 2025-11-03T14:46:47.416066
---

[Skip to main content](https://docs.kalshi.com/typescript-sdk/api/SeriesApi#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

API Classes

Series

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

On this page

*   [getSeries](https://docs.kalshi.com/typescript-sdk/api/SeriesApi#getseries)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/SeriesApi#example)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/SeriesApi#parameters)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/SeriesApi#return-type)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/SeriesApi#authorization)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/SeriesApi#http-request-headers)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/SeriesApi#http-response-details)
    
*   [getSeriesByTicker](https://docs.kalshi.com/typescript-sdk/api/SeriesApi#getseriesbyticker)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/SeriesApi#example-2)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/SeriesApi#parameters-2)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/SeriesApi#return-type-2)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/SeriesApi#authorization-2)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/SeriesApi#http-request-headers-2)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/SeriesApi#http-response-details-2)
    

All URIs are relative to _[https://api.elections.kalshi.com/trade-api/v2](https://api.elections.kalshi.com/trade-api/v2)
_

| Method | HTTP request | Description |
| --- | --- | --- |
| [**getSeries**](https://docs.kalshi.com/typescript-sdk/api/SeriesApi#getseries) | **GET** /series | Get Series |
| [**getSeriesByTicker**](https://docs.kalshi.com/typescript-sdk/api/SeriesApi#getseriesbyticker) | **GET** /series/ | Get Series by Ticker |

[​](https://docs.kalshi.com/typescript-sdk/api/SeriesApi#getseries)

**getSeries**
====================================================================================

> GetSeriesResponse getSeries()

Get all market series

### 

[​](https://docs.kalshi.com/typescript-sdk/api/SeriesApi#example)

Example

Copy

Ask AI

    import {
        SeriesApi,
        Configuration
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new SeriesApi(configuration);
    
    let status: string; //Filter by series status (optional) (default to undefined)
    
    const { status, data } = await apiInstance.getSeries(
        status
    );
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/SeriesApi#parameters)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **status** | \[**string**\] | Filter by series status | (optional) defaults to undefined |

### 

[​](https://docs.kalshi.com/typescript-sdk/api/SeriesApi#return-type)

Return type

**GetSeriesResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/SeriesApi#authorization)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/SeriesApi#http-request-headers)

HTTP request headers

*   **Content-Type**: Not defined
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/SeriesApi#http-response-details)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **200** | Series retrieved successfully | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/SeriesApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[​](https://docs.kalshi.com/typescript-sdk/api/SeriesApi#getseriesbyticker)

**getSeriesByTicker**
====================================================================================================

> GetSeriesByTickerResponse getSeriesByTicker()

Get a single series by its ticker

### 

[​](https://docs.kalshi.com/typescript-sdk/api/SeriesApi#example-2)

Example

Copy

Ask AI

    import {
        SeriesApi,
        Configuration
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new SeriesApi(configuration);
    
    let ticker: string; //The series ticker (default to undefined)
    
    const { status, data } = await apiInstance.getSeriesByTicker(
        ticker
    );
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/SeriesApi#parameters-2)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **ticker** | \[**string**\] | The series ticker | defaults to undefined |

### 

[​](https://docs.kalshi.com/typescript-sdk/api/SeriesApi#return-type-2)

Return type

**GetSeriesByTickerResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/SeriesApi#authorization-2)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/SeriesApi#http-request-headers-2)

HTTP request headers

*   **Content-Type**: Not defined
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/SeriesApi#http-response-details-2)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **200** | Series retrieved successfully | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **404** | Resource not found | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/SeriesApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[Events](https://docs.kalshi.com/typescript-sdk/api/EventsApi)
[Milestones](https://docs.kalshi.com/typescript-sdk/api/MilestonesApi)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.