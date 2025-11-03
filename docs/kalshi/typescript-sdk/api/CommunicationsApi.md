---
url: https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi
title: Communications - API Documentation
description: TypeScript SDK methods for Communications operations
scraped_at: 2025-11-03T14:46:46.137417
---

[Skip to main content](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

API Classes

Communications

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

On this page

*   [acceptQuote](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#acceptquote)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#example)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#parameters)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#return-type)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#authorization)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#http-request-headers)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#http-response-details)
    
*   [confirmQuote](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#confirmquote)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#example-2)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#parameters-2)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#return-type-2)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#authorization-2)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#http-request-headers-2)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#http-response-details-2)
    
*   [createQuote](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#createquote)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#example-3)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#parameters-3)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#return-type-3)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#authorization-3)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#http-request-headers-3)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#http-response-details-3)
    
*   [createRFQ](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#createrfq)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#example-4)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#parameters-4)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#return-type-4)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#authorization-4)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#http-request-headers-4)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#http-response-details-4)
    
*   [deleteQuote](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#deletequote)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#example-5)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#parameters-5)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#return-type-5)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#authorization-5)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#http-request-headers-5)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#http-response-details-5)
    
*   [deleteRFQ](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#deleterfq)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#example-6)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#parameters-6)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#return-type-6)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#authorization-6)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#http-request-headers-6)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#http-response-details-6)
    
*   [getCommunicationsID](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#getcommunicationsid)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#example-7)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#parameters-7)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#return-type-7)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#authorization-7)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#http-request-headers-7)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#http-response-details-7)
    
*   [getQuote](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#getquote)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#example-8)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#parameters-8)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#return-type-8)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#authorization-8)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#http-request-headers-8)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#http-response-details-8)
    
*   [getQuotes](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#getquotes)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#example-9)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#parameters-9)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#return-type-9)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#authorization-9)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#http-request-headers-9)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#http-response-details-9)
    
*   [getRFQ](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#getrfq)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#example-10)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#parameters-10)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#return-type-10)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#authorization-10)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#http-request-headers-10)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#http-response-details-10)
    
*   [getRFQs](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#getrfqs)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#example-11)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#parameters-11)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#return-type-11)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#authorization-11)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#http-request-headers-11)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#http-response-details-11)
    

All URIs are relative to _[https://api.elections.kalshi.com/trade-api/v2](https://api.elections.kalshi.com/trade-api/v2)
_

| Method | HTTP request | Description |
| --- | --- | --- |
| [**acceptQuote**](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#acceptquote) | **PUT** /communications/quotes//accept | Accept Quote |
| [**confirmQuote**](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#confirmquote) | **PUT** /communications/quotes//confirm | Confirm Quote |
| [**createQuote**](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#createquote) | **POST** /communications/quotes | Create Quote |
| [**createRFQ**](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#createrfq) | **POST** /communications/rfqs | Create RFQ |
| [**deleteQuote**](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#deletequote) | **DELETE** /communications/quotes/ | Delete Quote |
| [**deleteRFQ**](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#deleterfq) | **DELETE** /communications/rfqs/ | Delete RFQ |
| [**getCommunicationsID**](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#getcommunicationsid) | **GET** /communications/id | Get Communications ID |
| [**getQuote**](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#getquote) | **GET** /communications/quotes/ | Get Quote |
| [**getQuotes**](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#getquotes) | **GET** /communications/quotes | Get Quotes |
| [**getRFQ**](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#getrfq) | **GET** /communications/rfqs/ | Get RFQ |
| [**getRFQs**](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#getrfqs) | **GET** /communications/rfqs | Get RFQs |

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#acceptquote)

**acceptQuote**
================================================================================================

> acceptQuote(acceptQuoteRequest)

Accept a quote. This will require the quoter to confirm

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#example)

Example

Copy

Ask AI

    import {
        CommunicationsApi,
        Configuration,
        AcceptQuoteRequest
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new CommunicationsApi(configuration);
    
    let quoteId: string; //Quote ID (default to undefined)
    let acceptQuoteRequest: AcceptQuoteRequest; //
    
    const { status, data } = await apiInstance.acceptQuote(
        quoteId,
        acceptQuoteRequest
    );
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#parameters)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **acceptQuoteRequest** | **AcceptQuoteRequest** |     |     |
| **quoteId** | \[**string**\] | Quote ID | defaults to undefined |

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#return-type)

Return type

void (empty response body)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#authorization)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#http-request-headers)

HTTP request headers

*   **Content-Type**: application/json
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#http-response-details)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **204** | Quote accepted successfully | \-  |
| **400** | Bad request - invalid input | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **404** | Resource not found | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#confirmquote)

**confirmQuote**
==================================================================================================

> confirmQuote()

Confirm a quote. This will start a timer for order execution

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#example-2)

Example

Copy

Ask AI

    import {
        CommunicationsApi,
        Configuration
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new CommunicationsApi(configuration);
    
    let quoteId: string; //Quote ID (default to undefined)
    
    const { status, data } = await apiInstance.confirmQuote(
        quoteId
    );
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#parameters-2)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **quoteId** | \[**string**\] | Quote ID | defaults to undefined |

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#return-type-2)

Return type

void (empty response body)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#authorization-2)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#http-request-headers-2)

HTTP request headers

*   **Content-Type**: Not defined
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#http-response-details-2)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **204** | Quote confirmed successfully | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **404** | Resource not found | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#createquote)

**createQuote**
================================================================================================

> CreateQuoteResponse createQuote(createQuoteRequest)

Create a quote in response to an RFQ

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#example-3)

Example

Copy

Ask AI

    import {
        CommunicationsApi,
        Configuration,
        CreateQuoteRequest
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new CommunicationsApi(configuration);
    
    let createQuoteRequest: CreateQuoteRequest; //
    
    const { status, data } = await apiInstance.createQuote(
        createQuoteRequest
    );
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#parameters-3)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **createQuoteRequest** | **CreateQuoteRequest** |     |     |

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#return-type-3)

Return type

**CreateQuoteResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#authorization-3)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#http-request-headers-3)

HTTP request headers

*   **Content-Type**: application/json
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#http-response-details-3)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **201** | Quote created successfully | \-  |
| **400** | Bad request - invalid input | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#createrfq)

**createRFQ**
============================================================================================

> CreateRFQResponse createRFQ(createRFQRequest)

Create a new RFQ

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#example-4)

Example

Copy

Ask AI

    import {
        CommunicationsApi,
        Configuration,
        CreateRFQRequest
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new CommunicationsApi(configuration);
    
    let createRFQRequest: CreateRFQRequest; //
    
    const { status, data } = await apiInstance.createRFQ(
        createRFQRequest
    );
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#parameters-4)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **createRFQRequest** | **CreateRFQRequest** |     |     |

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#return-type-4)

Return type

**CreateRFQResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#authorization-4)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#http-request-headers-4)

HTTP request headers

*   **Content-Type**: application/json
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#http-response-details-4)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **201** | RFQ created successfully | \-  |
| **400** | Bad request - invalid input | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#deletequote)

**deleteQuote**
================================================================================================

> deleteQuote()

Delete a quote, which means it can no longer be accepted

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#example-5)

Example

Copy

Ask AI

    import {
        CommunicationsApi,
        Configuration
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new CommunicationsApi(configuration);
    
    let quoteId: string; //Quote ID (default to undefined)
    
    const { status, data } = await apiInstance.deleteQuote(
        quoteId
    );
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#parameters-5)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **quoteId** | \[**string**\] | Quote ID | defaults to undefined |

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#return-type-5)

Return type

void (empty response body)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#authorization-5)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#http-request-headers-5)

HTTP request headers

*   **Content-Type**: Not defined
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#http-response-details-5)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **204** | Quote deleted successfully | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **404** | Resource not found | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#deleterfq)

**deleteRFQ**
============================================================================================

> deleteRFQ()

Delete an RFQ by ID

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#example-6)

Example

Copy

Ask AI

    import {
        CommunicationsApi,
        Configuration
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new CommunicationsApi(configuration);
    
    let rfqId: string; //RFQ ID (default to undefined)
    
    const { status, data } = await apiInstance.deleteRFQ(
        rfqId
    );
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#parameters-6)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **rfqId** | \[**string**\] | RFQ ID | defaults to undefined |

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#return-type-6)

Return type

void (empty response body)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#authorization-6)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#http-request-headers-6)

HTTP request headers

*   **Content-Type**: Not defined
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#http-response-details-6)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **204** | RFQ deleted successfully | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **404** | Resource not found | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#getcommunicationsid)

**getCommunicationsID**
================================================================================================================

> GetCommunicationsIDResponse getCommunicationsID()

Get the communications ID of the logged-in user

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#example-7)

Example

Copy

Ask AI

    import {
        CommunicationsApi,
        Configuration
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new CommunicationsApi(configuration);
    
    const { status, data } = await apiInstance.getCommunicationsID();
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#parameters-7)

Parameters

This endpoint does not have any parameters.

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#return-type-7)

Return type

**GetCommunicationsIDResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#authorization-7)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#http-request-headers-7)

HTTP request headers

*   **Content-Type**: Not defined
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#http-response-details-7)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **200** | Communications ID retrieved successfully | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#getquote)

**getQuote**
==========================================================================================

> GetQuoteResponse getQuote()

Get a particular quote by ID

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#example-8)

Example

Copy

Ask AI

    import {
        CommunicationsApi,
        Configuration
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new CommunicationsApi(configuration);
    
    let quoteId: string; //Quote ID (default to undefined)
    
    const { status, data } = await apiInstance.getQuote(
        quoteId
    );
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#parameters-8)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **quoteId** | \[**string**\] | Quote ID | defaults to undefined |

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#return-type-8)

Return type

**GetQuoteResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#authorization-8)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#http-request-headers-8)

HTTP request headers

*   **Content-Type**: Not defined
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#http-response-details-8)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **200** | Quote retrieved successfully | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **404** | Resource not found | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#getquotes)

**getQuotes**
============================================================================================

> GetQuotesResponse getQuotes()

Retrieve all quotes

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#example-9)

Example

Copy

Ask AI

    import {
        CommunicationsApi,
        Configuration
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new CommunicationsApi(configuration);
    
    const { status, data } = await apiInstance.getQuotes();
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#parameters-9)

Parameters

This endpoint does not have any parameters.

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#return-type-9)

Return type

**GetQuotesResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#authorization-9)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#http-request-headers-9)

HTTP request headers

*   **Content-Type**: Not defined
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#http-response-details-9)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **200** | Quotes retrieved successfully | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#getrfq)

**getRFQ**
======================================================================================

> GetRFQResponse getRFQ()

Get a single RFQ by ID

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#example-10)

Example

Copy

Ask AI

    import {
        CommunicationsApi,
        Configuration
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new CommunicationsApi(configuration);
    
    let rfqId: string; //RFQ ID (default to undefined)
    
    const { status, data } = await apiInstance.getRFQ(
        rfqId
    );
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#parameters-10)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **rfqId** | \[**string**\] | RFQ ID | defaults to undefined |

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#return-type-10)

Return type

**GetRFQResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#authorization-10)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#http-request-headers-10)

HTTP request headers

*   **Content-Type**: Not defined
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#http-response-details-10)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **200** | RFQ retrieved successfully | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **404** | Resource not found | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#getrfqs)

**getRFQs**
========================================================================================

> GetRFQsResponse getRFQs()

Retrieve all RFQs

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#example-11)

Example

Copy

Ask AI

    import {
        CommunicationsApi,
        Configuration
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new CommunicationsApi(configuration);
    
    const { status, data } = await apiInstance.getRFQs();
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#parameters-11)

Parameters

This endpoint does not have any parameters.

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#return-type-11)

Return type

**GetRFQsResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#authorization-11)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#http-request-headers-11)

HTTP request headers

*   **Content-Type**: Not defined
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#http-response-details-11)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **200** | RFQs retrieved successfully | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[Markets](https://docs.kalshi.com/typescript-sdk/api/MarketsApi)
[Events](https://docs.kalshi.com/typescript-sdk/api/EventsApi)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.