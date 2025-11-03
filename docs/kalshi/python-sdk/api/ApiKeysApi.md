---
url: https://docs.kalshi.com/python-sdk/api/ApiKeysApi
title: ApiKeys - API Documentation
description: Python SDK methods for ApiKeys operations
scraped_at: 2025-11-03T14:46:40.333083
---

[Skip to main content](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#content-area)

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

*   [create\_api\_key](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#create-api-key)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#example)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#parameters)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#return-type)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#http-response-details)
    
*   [delete\_api\_key](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#delete-api-key)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#example-2)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#parameters-2)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#return-type-2)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#http-response-details-2)
    
*   [generate\_api\_key](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#generate-api-key)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#example-3)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#parameters-3)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#return-type-3)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#http-response-details-3)
    
*   [get\_api\_keys](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#get-api-keys)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#example-4)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#parameters-4)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#return-type-4)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#http-response-details-4)
    

All URIs are relative to _[https://api.elections.kalshi.com/trade-api/v2](https://api.elections.kalshi.com/trade-api/v2)
_

| Method | HTTP request | Description |
| --- | --- | --- |
| [**create\_api\_key**](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#create-api-key) | **POST** /api\_keys | Create API Key |
| [**delete\_api\_key**](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#delete-api-key) | **DELETE** /api\_keys/ | Delete API Key |
| [**generate\_api\_key**](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#generate-api-key) | **POST** /api\_keys/generate | Generate API Key |
| [**get\_api\_keys**](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#get-api-keys) | **GET** /api\_keys | Get API Keys |

[​](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#create-api-key)

**create\_api\_key**
=============================================================================================

> CreateApiKeyResponse create\_api\_key(create\_api\_key\_request)

Create API Key Create a new API key with a user-provided public key. This endpoint allows users with Premier or Market Maker API usage levels to create API keys by providing their own RSA public key. The platform will use this public key to verify signatures on API requests.

### 

[​](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#example)

Example

Copy

Ask AI

    import kalshi_python
    from kalshi_python.models.create_api_key_request import CreateApiKeyRequest
    from kalshi_python.models.create_api_key_response import CreateApiKeyResponse
    from kalshi_python.rest import ApiException
    from pprint import pprint
    
    # Defining the host is optional and defaults to https://api.elections.kalshi.com/trade-api/v2
    # See configuration.py for a list of all supported configuration parameters.
    configuration = kalshi_python.Configuration(
        host = "https://api.elections.kalshi.com/trade-api/v2"
    )
    
    # Read private key from file
    with open('path/to/private_key.pem', 'r') as f:
        private_key = f.read()
    
    # Configure API key authentication
    configuration.api_key_id = "your-api-key-id"
    configuration.private_key_pem = private_key
    
    # Initialize the Kalshi client
    client = kalshi_python.KalshiClient(configuration)
    
    create_api_key_request = kalshi_python.CreateApiKeyRequest() # CreateApiKeyRequest |
    
    try:
        # Create API Key
        api_response = client.create_api_key(create_api_key_request)
        print("The response of ApiKeysApi->create_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeysApi->create_api_key: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#parameters)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **create\_api\_key\_request** | [**CreateApiKeyRequest**](https://docs.kalshi.com/python-sdk/models/CreateApiKeyRequest) |     |     |

### 

[​](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#return-type)

Return type

[**CreateApiKeyResponse**](https://docs.kalshi.com/python-sdk/models/CreateApiKeyResponse)

### 

[​](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#http-response-details)

HTTP response details

| Status code | Description |
| --- | --- |
| **201** | API key created successfully |
| **400** | Bad request - invalid input |
| **401** | Unauthorized - authentication required |
| **403** | Forbidden - insufficient permissions |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[​](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#delete-api-key)

**delete\_api\_key**
=============================================================================================

> delete\_api\_key(api\_key)

Delete API Key Delete an existing API key. This endpoint permanently deletes an API key. Once deleted, the key can no longer be used for authentication. This action cannot be undone.

### 

[​](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#example-2)

Example

Copy

Ask AI

    import kalshi_python
    from kalshi_python.rest import ApiException
    from pprint import pprint
    
    # Defining the host is optional and defaults to https://api.elections.kalshi.com/trade-api/v2
    # See configuration.py for a list of all supported configuration parameters.
    configuration = kalshi_python.Configuration(
        host = "https://api.elections.kalshi.com/trade-api/v2"
    )
    
    # Read private key from file
    with open('path/to/private_key.pem', 'r') as f:
        private_key = f.read()
    
    # Configure API key authentication
    configuration.api_key_id = "your-api-key-id"
    configuration.private_key_pem = private_key
    
    # Initialize the Kalshi client
    client = kalshi_python.KalshiClient(configuration)
    
    api_key = 'api_key_example' # str | API key ID to delete
    
    try:
        # Delete API Key
        client.delete_api_key(api_key)
    except Exception as e:
        print("Exception when calling ApiKeysApi->delete_api_key: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#parameters-2)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **api\_key** | **str** | API key ID to delete |     |

### 

[​](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#return-type-2)

Return type

void (empty response body)

### 

[​](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#http-response-details-2)

HTTP response details

| Status code | Description |
| --- | --- |
| **204** | API key successfully deleted |
| **400** | Bad request - invalid input |
| **401** | Unauthorized - authentication required |
| **404** | Resource not found |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[​](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#generate-api-key)

**generate\_api\_key**
=================================================================================================

> GenerateApiKeyResponse generate\_api\_key(generate\_api\_key\_request)

Generate API Key Generate a new API key with an automatically created key pair. This endpoint generates both a public and private RSA key pair. The public key is stored on the platform, while the private key is returned to the user and must be stored securely. The private key cannot be retrieved again.

### 

[​](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#example-3)

Example

Copy

Ask AI

    import kalshi_python
    from kalshi_python.models.generate_api_key_request import GenerateApiKeyRequest
    from kalshi_python.models.generate_api_key_response import GenerateApiKeyResponse
    from kalshi_python.rest import ApiException
    from pprint import pprint
    
    # Defining the host is optional and defaults to https://api.elections.kalshi.com/trade-api/v2
    # See configuration.py for a list of all supported configuration parameters.
    configuration = kalshi_python.Configuration(
        host = "https://api.elections.kalshi.com/trade-api/v2"
    )
    
    # Read private key from file
    with open('path/to/private_key.pem', 'r') as f:
        private_key = f.read()
    
    # Configure API key authentication
    configuration.api_key_id = "your-api-key-id"
    configuration.private_key_pem = private_key
    
    # Initialize the Kalshi client
    client = kalshi_python.KalshiClient(configuration)
    
    generate_api_key_request = kalshi_python.GenerateApiKeyRequest() # GenerateApiKeyRequest |
    
    try:
        # Generate API Key
        api_response = client.generate_api_key(generate_api_key_request)
        print("The response of ApiKeysApi->generate_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeysApi->generate_api_key: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#parameters-3)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **generate\_api\_key\_request** | [**GenerateApiKeyRequest**](https://docs.kalshi.com/python-sdk/models/GenerateApiKeyRequest) |     |     |

### 

[​](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#return-type-3)

Return type

[**GenerateApiKeyResponse**](https://docs.kalshi.com/python-sdk/models/GenerateApiKeyResponse)

### 

[​](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#http-response-details-3)

HTTP response details

| Status code | Description |
| --- | --- |
| **201** | API key generated successfully |
| **400** | Bad request - invalid input |
| **401** | Unauthorized - authentication required |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[​](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#get-api-keys)

**get\_api\_keys**
=========================================================================================

> GetApiKeysResponse get\_api\_keys()

Get API Keys Retrieve all API keys associated with the authenticated user. API keys allow programmatic access to the platform without requiring username/password authentication. Each key has a unique identifier and name.

### 

[​](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#example-4)

Example

Copy

Ask AI

    import kalshi_python
    from kalshi_python.models.get_api_keys_response import GetApiKeysResponse
    from kalshi_python.rest import ApiException
    from pprint import pprint
    
    # Defining the host is optional and defaults to https://api.elections.kalshi.com/trade-api/v2
    # See configuration.py for a list of all supported configuration parameters.
    configuration = kalshi_python.Configuration(
        host = "https://api.elections.kalshi.com/trade-api/v2"
    )
    
    # Read private key from file
    with open('path/to/private_key.pem', 'r') as f:
        private_key = f.read()
    
    # Configure API key authentication
    configuration.api_key_id = "your-api-key-id"
    configuration.private_key_pem = private_key
    
    # Initialize the Kalshi client
    client = kalshi_python.KalshiClient(configuration)
    
    try:
        # Get API Keys
        api_response = client.get_api_keys()
        print("The response of ApiKeysApi->get_api_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiKeysApi->get_api_keys: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#parameters-4)

Parameters

This endpoint does not need any parameter.

### 

[​](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#return-type-4)

Return type

[**GetApiKeysResponse**](https://docs.kalshi.com/python-sdk/models/GetApiKeysResponse)

### 

[​](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#http-response-details-4)

HTTP response details

| Status code | Description |
| --- | --- |
| **200** | List of API keys retrieved successfully |
| **401** | Unauthorized - authentication required |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/ApiKeysApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[Exchange](https://docs.kalshi.com/python-sdk/api/ExchangeApi)
[TypeScript SDK Quick Start](https://docs.kalshi.com/sdks/typescript/quickstart)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.