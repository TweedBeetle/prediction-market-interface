---
url: https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi
title: ApiKeys - API Documentation
description: TypeScript SDK methods for ApiKeys operations
scraped_at: 2025-11-03T14:46:46.571068
---

[Skip to main content](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

API Classes

ApiKeys

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

On this page

*   [createApiKey](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#createapikey)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#example)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#parameters)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#return-type)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#authorization)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#http-request-headers)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#http-response-details)
    
*   [deleteApiKey](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#deleteapikey)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#example-2)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#parameters-2)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#return-type-2)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#authorization-2)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#http-request-headers-2)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#http-response-details-2)
    
*   [generateApiKey](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#generateapikey)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#example-3)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#parameters-3)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#return-type-3)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#authorization-3)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#http-request-headers-3)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#http-response-details-3)
    
*   [getApiKeys](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#getapikeys)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#example-4)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#parameters-4)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#return-type-4)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#authorization-4)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#http-request-headers-4)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#http-response-details-4)
    

All URIs are relative to _[https://api.elections.kalshi.com/trade-api/v2](https://api.elections.kalshi.com/trade-api/v2)
_

| Method | HTTP request | Description |
| --- | --- | --- |
| [**createApiKey**](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#createapikey) | **POST** /api\_keys | Create API Key |
| [**deleteApiKey**](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#deleteapikey) | **DELETE** /api\_keys/ | Delete API Key |
| [**generateApiKey**](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#generateapikey) | **POST** /api\_keys/generate | Generate API Key |
| [**getApiKeys**](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#getapikeys) | **GET** /api\_keys | Get API Keys |

[​](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#createapikey)

**createApiKey**
===========================================================================================

> CreateApiKeyResponse createApiKey(createApiKeyRequest)

Create a new API key with a user-provided public key. This endpoint allows users with Premier or Market Maker API usage levels to create API keys by providing their own RSA public key. The platform will use this public key to verify signatures on API requests.

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#example)

Example

Copy

Ask AI

    import {
        ApiKeysApi,
        Configuration,
        CreateApiKeyRequest
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new ApiKeysApi(configuration);
    
    let createApiKeyRequest: CreateApiKeyRequest; //
    
    const { status, data } = await apiInstance.createApiKey(
        createApiKeyRequest
    );
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#parameters)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **createApiKeyRequest** | **CreateApiKeyRequest** |     |     |

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#return-type)

Return type

**CreateApiKeyResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#authorization)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#http-request-headers)

HTTP request headers

*   **Content-Type**: application/json
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#http-response-details)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **201** | API key created successfully | \-  |
| **400** | Bad request - invalid input | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **403** | Forbidden - insufficient permissions | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[​](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#deleteapikey)

**deleteApiKey**
===========================================================================================

> deleteApiKey()

Delete an existing API key. This endpoint permanently deletes an API key. Once deleted, the key can no longer be used for authentication. This action cannot be undone.

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#example-2)

Example

Copy

Ask AI

    import {
        ApiKeysApi,
        Configuration
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new ApiKeysApi(configuration);
    
    let apiKey: string; //API key ID to delete (default to undefined)
    
    const { status, data } = await apiInstance.deleteApiKey(
        apiKey
    );
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#parameters-2)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **apiKey** | \[**string**\] | API key ID to delete | defaults to undefined |

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#return-type-2)

Return type

void (empty response body)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#authorization-2)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#http-request-headers-2)

HTTP request headers

*   **Content-Type**: Not defined
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#http-response-details-2)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **204** | API key successfully deleted | \-  |
| **400** | Bad request - invalid input | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **404** | Resource not found | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[​](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#generateapikey)

**generateApiKey**
===============================================================================================

> GenerateApiKeyResponse generateApiKey(generateApiKeyRequest)

Generate a new API key with an automatically created key pair. This endpoint generates both a public and private RSA key pair. The public key is stored on the platform, while the private key is returned to the user and must be stored securely. The private key cannot be retrieved again.

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#example-3)

Example

Copy

Ask AI

    import {
        ApiKeysApi,
        Configuration,
        GenerateApiKeyRequest
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new ApiKeysApi(configuration);
    
    let generateApiKeyRequest: GenerateApiKeyRequest; //
    
    const { status, data } = await apiInstance.generateApiKey(
        generateApiKeyRequest
    );
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#parameters-3)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **generateApiKeyRequest** | **GenerateApiKeyRequest** |     |     |

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#return-type-3)

Return type

**GenerateApiKeyResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#authorization-3)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#http-request-headers-3)

HTTP request headers

*   **Content-Type**: application/json
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#http-response-details-3)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **201** | API key generated successfully | \-  |
| **400** | Bad request - invalid input | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[​](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#getapikeys)

**getApiKeys**
=======================================================================================

> GetApiKeysResponse getApiKeys()

Retrieve all API keys associated with the authenticated user. API keys allow programmatic access to the platform without requiring username/password authentication. Each key has a unique identifier and name.

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#example-4)

Example

Copy

Ask AI

    import {
        ApiKeysApi,
        Configuration
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new ApiKeysApi(configuration);
    
    const { status, data } = await apiInstance.getApiKeys();
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#parameters-4)

Parameters

This endpoint does not have any parameters.

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#return-type-4)

Return type

**GetApiKeysResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#authorization-4)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#http-request-headers-4)

HTTP request headers

*   **Content-Type**: Not defined
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#http-response-details-4)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **200** | List of API keys retrieved successfully | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/ApiKeysApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[Exchange](https://docs.kalshi.com/typescript-sdk/api/ExchangeApi)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.