---
url: https://docs.kalshi.com/python-sdk/api/MultivariateCollectionsApi
title: MultivariateCollections - API Documentation
description: Python SDK methods for MultivariateCollections operations
scraped_at: 2025-11-03T14:46:41.586845
---

[Skip to main content](https://docs.kalshi.com/python-sdk/api/MultivariateCollectionsApi#content-area)

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

*   [get\_multivariate\_event\_collection](https://docs.kalshi.com/python-sdk/api/MultivariateCollectionsApi#get-multivariate-event-collection)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/MultivariateCollectionsApi#example)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/MultivariateCollectionsApi#parameters)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/MultivariateCollectionsApi#return-type)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/MultivariateCollectionsApi#http-response-details)
    
*   [get\_multivariate\_event\_collections](https://docs.kalshi.com/python-sdk/api/MultivariateCollectionsApi#get-multivariate-event-collections)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/MultivariateCollectionsApi#example-2)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/MultivariateCollectionsApi#parameters-2)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/MultivariateCollectionsApi#return-type-2)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/MultivariateCollectionsApi#http-response-details-2)
    
*   [lookup\_multivariate\_event\_collection\_bundle](https://docs.kalshi.com/python-sdk/api/MultivariateCollectionsApi#lookup-multivariate-event-collection-bundle)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/MultivariateCollectionsApi#example-3)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/MultivariateCollectionsApi#parameters-3)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/MultivariateCollectionsApi#return-type-3)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/MultivariateCollectionsApi#http-response-details-3)
    

All URIs are relative to _[https://api.elections.kalshi.com/trade-api/v2](https://api.elections.kalshi.com/trade-api/v2)
_

| Method | HTTP request | Description |
| --- | --- | --- |
| [**get\_multivariate\_event\_collection**](https://docs.kalshi.com/python-sdk/api/MultivariateCollectionsApi#get-multivariate-event-collection) | **GET** /multivariate\_event\_collections/ | Get Multivariate Event Collection |
| [**get\_multivariate\_event\_collections**](https://docs.kalshi.com/python-sdk/api/MultivariateCollectionsApi#get-multivariate-event-collections) | **GET** /multivariate\_event\_collections | Get Multivariate Event Collections |
| [**lookup\_multivariate\_event\_collection\_bundle**](https://docs.kalshi.com/python-sdk/api/MultivariateCollectionsApi#lookup-multivariate-event-collection-bundle) | **POST** /multivariate\_event\_collections//lookup | Lookup Multivariate Event Collection Bundle |

[​](https://docs.kalshi.com/python-sdk/api/MultivariateCollectionsApi#get-multivariate-event-collection)

**get\_multivariate\_event\_collection**
====================================================================================================================================================

> GetMultivariateEventCollectionResponse get\_multivariate\_event\_collection(collection\_ticker)

Get Multivariate Event Collection Get a single multivariate event collection by ticker

### 

[​](https://docs.kalshi.com/python-sdk/api/MultivariateCollectionsApi#example)

Example

Copy

Ask AI

    import kalshi_python
    from kalshi_python.models.get_multivariate_event_collection_response import GetMultivariateEventCollectionResponse
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
    
    collection_ticker = 'collection_ticker_example' # str | Collection ticker
    
    try:
        # Get Multivariate Event Collection
        api_response = client.get_multivariate_event_collection(collection_ticker)
        print("The response of MultivariateCollectionsApi->get_multivariate_event_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MultivariateCollectionsApi->get_multivariate_event_collection: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/MultivariateCollectionsApi#parameters)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **collection\_ticker** | **str** | Collection ticker |     |

### 

[​](https://docs.kalshi.com/python-sdk/api/MultivariateCollectionsApi#return-type)

Return type

[**GetMultivariateEventCollectionResponse**](https://docs.kalshi.com/python-sdk/models/GetMultivariateEventCollectionResponse)

### 

[​](https://docs.kalshi.com/python-sdk/api/MultivariateCollectionsApi#http-response-details)

HTTP response details

| Status code | Description |
| --- | --- |
| **200** | Collection retrieved successfully |
| **401** | Unauthorized - authentication required |
| **404** | Resource not found |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/MultivariateCollectionsApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[​](https://docs.kalshi.com/python-sdk/api/MultivariateCollectionsApi#get-multivariate-event-collections)

**get\_multivariate\_event\_collections**
======================================================================================================================================================

> GetMultivariateEventCollectionsResponse get\_multivariate\_event\_collections(status=status)

Get Multivariate Event Collections Get all multivariate event collections

### 

[​](https://docs.kalshi.com/python-sdk/api/MultivariateCollectionsApi#example-2)

Example

Copy

Ask AI

    import kalshi_python
    from kalshi_python.models.get_multivariate_event_collections_response import GetMultivariateEventCollectionsResponse
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
    
    status = 'status_example' # str | Filter by multivariate collection status (optional)
    
    try:
        # Get Multivariate Event Collections
        api_response = client.get_multivariate_event_collections(status=status)
        print("The response of MultivariateCollectionsApi->get_multivariate_event_collections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MultivariateCollectionsApi->get_multivariate_event_collections: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/MultivariateCollectionsApi#parameters-2)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **status** | **str** | Filter by multivariate collection status | \[optional\] |

### 

[​](https://docs.kalshi.com/python-sdk/api/MultivariateCollectionsApi#return-type-2)

Return type

[**GetMultivariateEventCollectionsResponse**](https://docs.kalshi.com/python-sdk/models/GetMultivariateEventCollectionsResponse)

### 

[​](https://docs.kalshi.com/python-sdk/api/MultivariateCollectionsApi#http-response-details-2)

HTTP response details

| Status code | Description |
| --- | --- |
| **200** | Collections retrieved successfully |
| **401** | Unauthorized - authentication required |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/MultivariateCollectionsApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[​](https://docs.kalshi.com/python-sdk/api/MultivariateCollectionsApi#lookup-multivariate-event-collection-bundle)

**lookup\_multivariate\_event\_collection\_bundle**
=========================================================================================================================================================================

> LookupBundleResponse lookup\_multivariate\_event\_collection\_bundle(collection\_ticker, lookup\_bundle\_request)

Lookup Multivariate Event Collection Bundle Lookup a bundle in a multivariate event collection

### 

[​](https://docs.kalshi.com/python-sdk/api/MultivariateCollectionsApi#example-3)

Example

Copy

Ask AI

    import kalshi_python
    from kalshi_python.models.lookup_bundle_request import LookupBundleRequest
    from kalshi_python.models.lookup_bundle_response import LookupBundleResponse
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
    
    collection_ticker = 'collection_ticker_example' # str | Collection ticker
    
    lookup_bundle_request = kalshi_python.LookupBundleRequest() # LookupBundleRequest |
    
    try:
        # Lookup Multivariate Event Collection Bundle
        api_response = client.lookup_multivariate_event_collection_bundle(collection_ticker, lookup_bundle_request)
        print("The response of MultivariateCollectionsApi->lookup_multivariate_event_collection_bundle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MultivariateCollectionsApi->lookup_multivariate_event_collection_bundle: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/MultivariateCollectionsApi#parameters-3)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **collection\_ticker** | **str** | Collection ticker |     |
| **lookup\_bundle\_request** | [**LookupBundleRequest**](https://docs.kalshi.com/python-sdk/models/LookupBundleRequest) |     |     |

### 

[​](https://docs.kalshi.com/python-sdk/api/MultivariateCollectionsApi#return-type-3)

Return type

[**LookupBundleResponse**](https://docs.kalshi.com/python-sdk/models/LookupBundleResponse)

### 

[​](https://docs.kalshi.com/python-sdk/api/MultivariateCollectionsApi#http-response-details-3)

HTTP response details

| Status code | Description |
| --- | --- |
| **200** | Bundle lookup successful |
| **400** | Bad request - invalid input |
| **401** | Unauthorized - authentication required |
| **404** | Resource not found |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/MultivariateCollectionsApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[Milestones](https://docs.kalshi.com/python-sdk/api/MilestonesApi)
[StructuredTargets](https://docs.kalshi.com/python-sdk/api/StructuredTargetsApi)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.