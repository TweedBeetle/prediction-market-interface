---
url: https://docs.kalshi.com/typescript-sdk/api/EventsApi
title: Events - API Documentation
description: TypeScript SDK methods for Events operations
scraped_at: 2025-11-03T14:46:47.595755
---

[Skip to main content](https://docs.kalshi.com/typescript-sdk/api/EventsApi#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

API Classes

Events

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

On this page

*   [getEvent](https://docs.kalshi.com/typescript-sdk/api/EventsApi#getevent)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/EventsApi#example)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/EventsApi#parameters)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/EventsApi#return-type)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/EventsApi#authorization)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/EventsApi#http-request-headers)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/EventsApi#http-response-details)
    
*   [getEventMetadata](https://docs.kalshi.com/typescript-sdk/api/EventsApi#geteventmetadata)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/EventsApi#example-2)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/EventsApi#parameters-2)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/EventsApi#return-type-2)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/EventsApi#authorization-2)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/EventsApi#http-request-headers-2)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/EventsApi#http-response-details-2)
    
*   [getEvents](https://docs.kalshi.com/typescript-sdk/api/EventsApi#getevents)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/EventsApi#example-3)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/EventsApi#parameters-3)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/EventsApi#return-type-3)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/EventsApi#authorization-3)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/EventsApi#http-request-headers-3)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/EventsApi#http-response-details-3)
    

All URIs are relative to _[https://api.elections.kalshi.com/trade-api/v2](https://api.elections.kalshi.com/trade-api/v2)
_

| Method | HTTP request | Description |
| --- | --- | --- |
| [**getEvent**](https://docs.kalshi.com/typescript-sdk/api/EventsApi#getevent) | **GET** /events/ | Get Event |
| [**getEventMetadata**](https://docs.kalshi.com/typescript-sdk/api/EventsApi#geteventmetadata) | **GET** /events//metadata | Get Event Metadata |
| [**getEvents**](https://docs.kalshi.com/typescript-sdk/api/EventsApi#getevents) | **GET** /events | Get Events |

[​](https://docs.kalshi.com/typescript-sdk/api/EventsApi#getevent)

**getEvent**
==================================================================================

> GetEventResponse getEvent()

Get data about an event by its ticker. An event represents a real-world occurrence that can be traded on, such as an election, sports game, or economic indicator release. Events contain one or more markets where users can place trades on different outcomes.

### 

[​](https://docs.kalshi.com/typescript-sdk/api/EventsApi#example)

Example

Copy

Ask AI

    import {
        EventsApi,
        Configuration
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new EventsApi(configuration);
    
    let eventTicker: string; //Event ticker (default to undefined)
    let withNestedMarkets: boolean; //If true, markets are included within the event object. If false (default), markets are returned as a separate top-level field in the response. (optional) (default to false)
    
    const { status, data } = await apiInstance.getEvent(
        eventTicker,
        withNestedMarkets
    );
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/EventsApi#parameters)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **eventTicker** | \[**string**\] | Event ticker | defaults to undefined |
| **withNestedMarkets** | \[**boolean**\] | If true, markets are included within the event object. If false (default), markets are returned as a separate top-level field in the response. | (optional) defaults to false |

### 

[​](https://docs.kalshi.com/typescript-sdk/api/EventsApi#return-type)

Return type

**GetEventResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/EventsApi#authorization)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/EventsApi#http-request-headers)

HTTP request headers

*   **Content-Type**: Not defined
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/EventsApi#http-response-details)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **200** | Event retrieved successfully | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **404** | Resource not found | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/EventsApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[​](https://docs.kalshi.com/typescript-sdk/api/EventsApi#geteventmetadata)

**getEventMetadata**
==================================================================================================

> GetEventMetadataResponse getEventMetadata()

Get metadata about an event by its ticker

### 

[​](https://docs.kalshi.com/typescript-sdk/api/EventsApi#example-2)

Example

Copy

Ask AI

    import {
        EventsApi,
        Configuration
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new EventsApi(configuration);
    
    let eventTicker: string; //Event ticker (default to undefined)
    
    const { status, data } = await apiInstance.getEventMetadata(
        eventTicker
    );
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/EventsApi#parameters-2)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **eventTicker** | \[**string**\] | Event ticker | defaults to undefined |

### 

[​](https://docs.kalshi.com/typescript-sdk/api/EventsApi#return-type-2)

Return type

**GetEventMetadataResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/EventsApi#authorization-2)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/EventsApi#http-request-headers-2)

HTTP request headers

*   **Content-Type**: Not defined
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/EventsApi#http-response-details-2)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **200** | Event metadata retrieved successfully | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **404** | Resource not found | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/EventsApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[​](https://docs.kalshi.com/typescript-sdk/api/EventsApi#getevents)

**getEvents**
====================================================================================

> GetEventsResponse getEvents()

Get data about all events. An event represents a real-world occurrence that can be traded on, such as an election, sports game, or economic indicator release. Events contain one or more markets where users can place trades on different outcomes. This endpoint returns a paginated response. Use the ‘limit’ parameter to control page size (1-200, defaults to 100). The response includes a ‘cursor’ field - pass this value in the ‘cursor’ parameter of your next request to get the next page. An empty cursor indicates no more pages are available.

### 

[​](https://docs.kalshi.com/typescript-sdk/api/EventsApi#example-3)

Example

Copy

Ask AI

    import {
        EventsApi,
        Configuration
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new EventsApi(configuration);
    
    let limit: number; //Number of results per page. Defaults to 100. Maximum value is 200. (optional) (default to 100)
    let cursor: string; //Pagination cursor. Use the cursor value returned from the previous response to get the next page of results. Leave empty for the first page. (optional) (default to undefined)
    let withNestedMarkets: boolean; //If true, markets are included within the event object. If false (default), markets are returned as a separate top-level field in the response. (optional) (default to false)
    let status: string; //Filter by status. Possible values depend on the endpoint. (optional) (default to undefined)
    let seriesTicker: string; //Filter by series ticker (optional) (default to undefined)
    let minCloseTs: number; //Filter items that close after this Unix timestamp (optional) (default to undefined)
    
    const { status, data } = await apiInstance.getEvents(
        limit,
        cursor,
        withNestedMarkets,
        status,
        seriesTicker,
        minCloseTs
    );
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/EventsApi#parameters-3)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **limit** | \[**number**\] | Number of results per page. Defaults to 100. Maximum value is 200. | (optional) defaults to 100 |
| **cursor** | \[**string**\] | Pagination cursor. Use the cursor value returned from the previous response to get the next page of results. Leave empty for the first page. | (optional) defaults to undefined |
| **withNestedMarkets** | \[**boolean**\] | If true, markets are included within the event object. If false (default), markets are returned as a separate top-level field in the response. | (optional) defaults to false |
| **status** | \[**string**\] | Filter by status. Possible values depend on the endpoint. | (optional) defaults to undefined |
| **seriesTicker** | \[**string**\] | Filter by series ticker | (optional) defaults to undefined |
| **minCloseTs** | \[**number**\] | Filter items that close after this Unix timestamp | (optional) defaults to undefined |

### 

[​](https://docs.kalshi.com/typescript-sdk/api/EventsApi#return-type-3)

Return type

**GetEventsResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/EventsApi#authorization-3)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/EventsApi#http-request-headers-3)

HTTP request headers

*   **Content-Type**: Not defined
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/EventsApi#http-response-details-3)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **200** | Events retrieved successfully | \-  |
| **400** | Bad request - invalid input | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/EventsApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[Communications](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi)
[Series](https://docs.kalshi.com/typescript-sdk/api/SeriesApi)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.