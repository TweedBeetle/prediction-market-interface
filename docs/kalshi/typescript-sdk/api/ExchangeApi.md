---
url: https://docs.kalshi.com/typescript-sdk/api/ExchangeApi
title: Exchange - API Documentation
description: TypeScript SDK methods for Exchange operations
scraped_at: 2025-11-03T14:46:46.616121
---

[Skip to main content](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

API Classes

Exchange

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

On this page

*   [getExchangeAnnouncements](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#getexchangeannouncements)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#example)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#parameters)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#return-type)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#authorization)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#http-request-headers)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#http-response-details)
    
*   [getExchangeSchedule](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#getexchangeschedule)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#example-2)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#parameters-2)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#return-type-2)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#authorization-2)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#http-request-headers-2)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#http-response-details-2)
    
*   [getExchangeStatus](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#getexchangestatus)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#example-3)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#parameters-3)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#return-type-3)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#authorization-3)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#http-request-headers-3)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#http-response-details-3)
    
*   [getUserDataTimestamp](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#getuserdatatimestamp)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#example-4)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#parameters-4)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#return-type-4)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#authorization-4)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#http-request-headers-4)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#http-response-details-4)
    

All URIs are relative to _[https://api.elections.kalshi.com/trade-api/v2](https://api.elections.kalshi.com/trade-api/v2)
_

| Method | HTTP request | Description |
| --- | --- | --- |
| [**getExchangeAnnouncements**](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#getexchangeannouncements) | **GET** /exchange/announcements | Get Exchange Announcements |
| [**getExchangeSchedule**](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#getexchangeschedule) | **GET** /exchange/schedule | Get Exchange Schedule |
| [**getExchangeStatus**](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#getexchangestatus) | **GET** /exchange/status | Get Exchange Status |
| [**getUserDataTimestamp**](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#getuserdatatimestamp) | **GET** /exchange/user\_data\_timestamp | Get User Data Timestamp |

[​](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#getexchangeannouncements)

**getExchangeAnnouncements**
====================================================================================================================

> GetExchangeAnnouncementsResponse getExchangeAnnouncements()

Get all exchange-wide announcements

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#example)

Example

Copy

Ask AI

    import {
        ExchangeApi,
        Configuration
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new ExchangeApi(configuration);
    
    const { status, data } = await apiInstance.getExchangeAnnouncements();
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#parameters)

Parameters

This endpoint does not have any parameters.

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#return-type)

Return type

**GetExchangeAnnouncementsResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#authorization)

Authorization

No authorization required

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#http-request-headers)

HTTP request headers

*   **Content-Type**: Not defined
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#http-response-details)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **200** | Announcements retrieved successfully | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[​](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#getexchangeschedule)

**getExchangeSchedule**
==========================================================================================================

> GetExchangeScheduleResponse getExchangeSchedule()

Get the exchange schedule

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#example-2)

Example

Copy

Ask AI

    import {
        ExchangeApi,
        Configuration
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new ExchangeApi(configuration);
    
    const { status, data } = await apiInstance.getExchangeSchedule();
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#parameters-2)

Parameters

This endpoint does not have any parameters.

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#return-type-2)

Return type

**GetExchangeScheduleResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#authorization-2)

Authorization

No authorization required

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#http-request-headers-2)

HTTP request headers

*   **Content-Type**: Not defined
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#http-response-details-2)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **200** | Schedule retrieved successfully | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[​](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#getexchangestatus)

**getExchangeStatus**
======================================================================================================

> ExchangeStatus getExchangeStatus()

Get the exchange status

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#example-3)

Example

Copy

Ask AI

    import {
        ExchangeApi,
        Configuration
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new ExchangeApi(configuration);
    
    const { status, data } = await apiInstance.getExchangeStatus();
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#parameters-3)

Parameters

This endpoint does not have any parameters.

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#return-type-3)

Return type

**ExchangeStatus**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#authorization-3)

Authorization

No authorization required

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#http-request-headers-3)

HTTP request headers

*   **Content-Type**: Not defined
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#http-response-details-3)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **200** | Status retrieved successfully | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[​](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#getuserdatatimestamp)

**getUserDataTimestamp**
============================================================================================================

> GetUserDataTimestampResponse getUserDataTimestamp()

There is typically a short delay before exchange events are reflected in the API endpoints. Whenever possible, combine API responses to PUT/POST/DELETE requests with websocket data to obtain the most accurate view of the exchange state. This endpoint provides an approximate indication of when the data from the following endpoints was last validated: GetBalance, GetOrder(s), GetFills, GetPositions

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#example-4)

Example

Copy

Ask AI

    import {
        ExchangeApi,
        Configuration
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new ExchangeApi(configuration);
    
    const { status, data } = await apiInstance.getUserDataTimestamp();
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#parameters-4)

Parameters

This endpoint does not have any parameters.

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#return-type-4)

Return type

**GetUserDataTimestampResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#authorization-4)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#http-request-headers-4)

HTTP request headers

*   **Content-Type**: Not defined
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#http-response-details-4)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **200** | Timestamp retrieved successfully | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[StructuredTargets](https://docs.kalshi.com/typescript-sdk/api/StructuredTargetsApi)
[ApiKeys](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.