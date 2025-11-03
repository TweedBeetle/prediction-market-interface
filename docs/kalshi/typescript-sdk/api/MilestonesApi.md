---
url: https://docs.kalshi.com/typescript-sdk/api/MilestonesApi
title: Milestones - API Documentation
description: TypeScript SDK methods for Milestones operations
scraped_at: 2025-11-03T14:46:46.626078
---

[Skip to main content](https://docs.kalshi.com/typescript-sdk/api/MilestonesApi#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

API Classes

Milestones

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

On this page

*   [getMilestone](https://docs.kalshi.com/typescript-sdk/api/MilestonesApi#getmilestone)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/MilestonesApi#example)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/MilestonesApi#parameters)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/MilestonesApi#return-type)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/MilestonesApi#authorization)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/MilestonesApi#http-request-headers)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/MilestonesApi#http-response-details)
    
*   [getMilestones](https://docs.kalshi.com/typescript-sdk/api/MilestonesApi#getmilestones)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/MilestonesApi#example-2)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/MilestonesApi#parameters-2)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/MilestonesApi#return-type-2)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/MilestonesApi#authorization-2)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/MilestonesApi#http-request-headers-2)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/MilestonesApi#http-response-details-2)
    

All URIs are relative to _[https://api.elections.kalshi.com/trade-api/v2](https://api.elections.kalshi.com/trade-api/v2)
_

| Method | HTTP request | Description |
| --- | --- | --- |
| [**getMilestone**](https://docs.kalshi.com/typescript-sdk/api/MilestonesApi#getmilestone) | **GET** /milestones/ | Get Milestone |
| [**getMilestones**](https://docs.kalshi.com/typescript-sdk/api/MilestonesApi#getmilestones) | **GET** /milestones | Get Milestones |

[​](https://docs.kalshi.com/typescript-sdk/api/MilestonesApi#getmilestone)

**getMilestone**
==============================================================================================

> GetMilestoneResponse getMilestone()

Get a single milestone by ID

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MilestonesApi#example)

Example

Copy

Ask AI

    import {
        MilestonesApi,
        Configuration
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new MilestonesApi(configuration);
    
    let milestoneId: string; //Milestone ID (default to undefined)
    
    const { status, data } = await apiInstance.getMilestone(
        milestoneId
    );
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MilestonesApi#parameters)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **milestoneId** | \[**string**\] | Milestone ID | defaults to undefined |

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MilestonesApi#return-type)

Return type

**GetMilestoneResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MilestonesApi#authorization)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MilestonesApi#http-request-headers)

HTTP request headers

*   **Content-Type**: Not defined
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MilestonesApi#http-response-details)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **200** | Milestone retrieved successfully | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **404** | Resource not found | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/MilestonesApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[​](https://docs.kalshi.com/typescript-sdk/api/MilestonesApi#getmilestones)

**getMilestones**
================================================================================================

> GetMilestonesResponse getMilestones()

Get all milestones

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MilestonesApi#example-2)

Example

Copy

Ask AI

    import {
        MilestonesApi,
        Configuration
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new MilestonesApi(configuration);
    
    let status: string; //Filter by milestone status (optional) (default to undefined)
    let limit: number; //Number of items per page (minimum 1, maximum 500) (optional) (default to 100)
    
    const { status, data } = await apiInstance.getMilestones(
        status,
        limit
    );
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MilestonesApi#parameters-2)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **status** | \[**string**\] | Filter by milestone status | (optional) defaults to undefined |
| **limit** | \[**number**\] | Number of items per page (minimum 1, maximum 500) | (optional) defaults to 100 |

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MilestonesApi#return-type-2)

Return type

**GetMilestonesResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MilestonesApi#authorization-2)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MilestonesApi#http-request-headers-2)

HTTP request headers

*   **Content-Type**: Not defined
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MilestonesApi#http-response-details-2)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **200** | Milestones retrieved successfully | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/MilestonesApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[Series](https://docs.kalshi.com/typescript-sdk/api/SeriesApi)
[MultivariateCollections](https://docs.kalshi.com/typescript-sdk/api/MultivariateCollectionsApi)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.