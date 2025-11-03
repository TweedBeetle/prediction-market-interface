---
url: https://docs.kalshi.com/python-sdk/api/StructuredTargetsApi
title: StructuredTargets - API Documentation
description: Python SDK methods for StructuredTargets operations
scraped_at: 2025-11-03T14:46:41.823615
---

[Skip to main content](https://docs.kalshi.com/python-sdk/api/StructuredTargetsApi#content-area)

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

*   [get\_structured\_target](https://docs.kalshi.com/python-sdk/api/StructuredTargetsApi#get-structured-target)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/StructuredTargetsApi#example)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/StructuredTargetsApi#parameters)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/StructuredTargetsApi#return-type)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/StructuredTargetsApi#http-response-details)
    
*   [get\_structured\_targets](https://docs.kalshi.com/python-sdk/api/StructuredTargetsApi#get-structured-targets)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/StructuredTargetsApi#example-2)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/StructuredTargetsApi#parameters-2)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/StructuredTargetsApi#return-type-2)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/StructuredTargetsApi#http-response-details-2)
    

All URIs are relative to _[https://api.elections.kalshi.com/trade-api/v2](https://api.elections.kalshi.com/trade-api/v2)
_

| Method | HTTP request | Description |
| --- | --- | --- |
| [**get\_structured\_target**](https://docs.kalshi.com/python-sdk/api/StructuredTargetsApi#get-structured-target) | **GET** /structured\_targets/ | Get Structured Target |
| [**get\_structured\_targets**](https://docs.kalshi.com/python-sdk/api/StructuredTargetsApi#get-structured-targets) | **GET** /structured\_targets | Get Structured Targets |

[​](https://docs.kalshi.com/python-sdk/api/StructuredTargetsApi#get-structured-target)

**get\_structured\_target**
=====================================================================================================================

> GetStructuredTargetResponse get\_structured\_target(structured\_target\_id)

Get Structured Target Get a single structured target by ID

### 

[​](https://docs.kalshi.com/python-sdk/api/StructuredTargetsApi#example)

Example

Copy

Ask AI

    import kalshi_python
    from kalshi_python.models.get_structured_target_response import GetStructuredTargetResponse
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
    
    structured_target_id = 'structured_target_id_example' # str | Structured target ID
    
    try:
        # Get Structured Target
        api_response = client.get_structured_target(structured_target_id)
        print("The response of StructuredTargetsApi->get_structured_target:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StructuredTargetsApi->get_structured_target: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/StructuredTargetsApi#parameters)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **structured\_target\_id** | **str** | Structured target ID |     |

### 

[​](https://docs.kalshi.com/python-sdk/api/StructuredTargetsApi#return-type)

Return type

[**GetStructuredTargetResponse**](https://docs.kalshi.com/python-sdk/models/GetStructuredTargetResponse)

### 

[​](https://docs.kalshi.com/python-sdk/api/StructuredTargetsApi#http-response-details)

HTTP response details

| Status code | Description |
| --- | --- |
| **200** | Structured target retrieved successfully |
| **401** | Unauthorized - authentication required |
| **404** | Resource not found |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/StructuredTargetsApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[​](https://docs.kalshi.com/python-sdk/api/StructuredTargetsApi#get-structured-targets)

**get\_structured\_targets**
=======================================================================================================================

> GetStructuredTargetsResponse get\_structured\_targets(status=status, page\_size=page\_size)

Get Structured Targets Get all structured targets

### 

[​](https://docs.kalshi.com/python-sdk/api/StructuredTargetsApi#example-2)

Example

Copy

Ask AI

    import kalshi_python
    from kalshi_python.models.get_structured_targets_response import GetStructuredTargetsResponse
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
    
    status = 'status_example' # str | Filter by structured target status (optional)
    
    page_size = 100 # int | Number of items per page (minimum 100, default 100) (optional) (default to 100)
    
    try:
        # Get Structured Targets
        api_response = client.get_structured_targets(status=status, page_size=page_size)
        print("The response of StructuredTargetsApi->get_structured_targets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StructuredTargetsApi->get_structured_targets: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/StructuredTargetsApi#parameters-2)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **status** | **str** | Filter by structured target status | \[optional\] |
| **page\_size** | **int** | Number of items per page (minimum 100, default 100) | \[optional\] \[default to 100\] |

### 

[​](https://docs.kalshi.com/python-sdk/api/StructuredTargetsApi#return-type-2)

Return type

[**GetStructuredTargetsResponse**](https://docs.kalshi.com/python-sdk/models/GetStructuredTargetsResponse)

### 

[​](https://docs.kalshi.com/python-sdk/api/StructuredTargetsApi#http-response-details-2)

HTTP response details

| Status code | Description |
| --- | --- |
| **200** | Structured targets retrieved successfully |
| **401** | Unauthorized - authentication required |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/StructuredTargetsApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[MultivariateCollections](https://docs.kalshi.com/python-sdk/api/MultivariateCollectionsApi)
[Exchange](https://docs.kalshi.com/python-sdk/api/ExchangeApi)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.