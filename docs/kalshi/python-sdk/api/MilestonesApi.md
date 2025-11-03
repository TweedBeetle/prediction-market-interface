---
url: https://docs.kalshi.com/python-sdk/api/MilestonesApi
title: Milestones - API Documentation
description: Python SDK methods for Milestones operations
scraped_at: 2025-11-03T14:46:42.240338
---

[Skip to main content](https://docs.kalshi.com/python-sdk/api/MilestonesApi#content-area)

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

*   [get\_milestone](https://docs.kalshi.com/python-sdk/api/MilestonesApi#get-milestone)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/MilestonesApi#example)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/MilestonesApi#parameters)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/MilestonesApi#return-type)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/MilestonesApi#http-response-details)
    
*   [get\_milestones](https://docs.kalshi.com/python-sdk/api/MilestonesApi#get-milestones)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/MilestonesApi#example-2)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/MilestonesApi#parameters-2)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/MilestonesApi#return-type-2)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/MilestonesApi#http-response-details-2)
    

All URIs are relative to _[https://api.elections.kalshi.com/trade-api/v2](https://api.elections.kalshi.com/trade-api/v2)
_

| Method | HTTP request | Description |
| --- | --- | --- |
| [**get\_milestone**](https://docs.kalshi.com/python-sdk/api/MilestonesApi#get-milestone) | **GET** /milestones/ | Get Milestone |
| [**get\_milestones**](https://docs.kalshi.com/python-sdk/api/MilestonesApi#get-milestones) | **GET** /milestones | Get Milestones |

[​](https://docs.kalshi.com/python-sdk/api/MilestonesApi#get-milestone)

**get\_milestone**
=============================================================================================

> GetMilestoneResponse get\_milestone(milestone\_id)

Get Milestone Get a single milestone by ID

### 

[​](https://docs.kalshi.com/python-sdk/api/MilestonesApi#example)

Example

Copy

Ask AI

    import kalshi_python
    from kalshi_python.models.get_milestone_response import GetMilestoneResponse
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
    
    milestone_id = 'milestone_id_example' # str | Milestone ID
    
    try:
        # Get Milestone
        api_response = client.get_milestone(milestone_id)
        print("The response of MilestonesApi->get_milestone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MilestonesApi->get_milestone: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/MilestonesApi#parameters)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **milestone\_id** | **str** | Milestone ID |     |

### 

[​](https://docs.kalshi.com/python-sdk/api/MilestonesApi#return-type)

Return type

[**GetMilestoneResponse**](https://docs.kalshi.com/python-sdk/models/GetMilestoneResponse)

### 

[​](https://docs.kalshi.com/python-sdk/api/MilestonesApi#http-response-details)

HTTP response details

| Status code | Description |
| --- | --- |
| **200** | Milestone retrieved successfully |
| **401** | Unauthorized - authentication required |
| **404** | Resource not found |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/MilestonesApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[​](https://docs.kalshi.com/python-sdk/api/MilestonesApi#get-milestones)

**get\_milestones**
===============================================================================================

> GetMilestonesResponse get\_milestones(status=status, limit=limit)

Get Milestones Get all milestones

### 

[​](https://docs.kalshi.com/python-sdk/api/MilestonesApi#example-2)

Example

Copy

Ask AI

    import kalshi_python
    from kalshi_python.models.get_milestones_response import GetMilestonesResponse
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
    
    status = 'status_example' # str | Filter by milestone status (optional)
    
    limit = 100 # int | Number of items per page (minimum 1, maximum 500) (optional) (default to 100)
    
    try:
        # Get Milestones
        api_response = client.get_milestones(status=status, limit=limit)
        print("The response of MilestonesApi->get_milestones:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MilestonesApi->get_milestones: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/MilestonesApi#parameters-2)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **status** | **str** | Filter by milestone status | \[optional\] |
| **limit** | **int** | Number of items per page (minimum 1, maximum 500) | \[optional\] \[default to 100\] |

### 

[​](https://docs.kalshi.com/python-sdk/api/MilestonesApi#return-type-2)

Return type

[**GetMilestonesResponse**](https://docs.kalshi.com/python-sdk/models/GetMilestonesResponse)

### 

[​](https://docs.kalshi.com/python-sdk/api/MilestonesApi#http-response-details-2)

HTTP response details

| Status code | Description |
| --- | --- |
| **200** | Milestones retrieved successfully |
| **401** | Unauthorized - authentication required |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/MilestonesApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[Series](https://docs.kalshi.com/python-sdk/api/SeriesApi)
[MultivariateCollections](https://docs.kalshi.com/python-sdk/api/MultivariateCollectionsApi)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.