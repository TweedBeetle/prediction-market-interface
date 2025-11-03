---
url: https://docs.kalshi.com/python-sdk/api/SeriesApi
title: Series - API Documentation
description: Python SDK methods for Series operations
scraped_at: 2025-11-03T14:46:41.541059
---

[Skip to main content](https://docs.kalshi.com/python-sdk/api/SeriesApi#content-area)

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

*   [get\_series](https://docs.kalshi.com/python-sdk/api/SeriesApi#get-series)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/SeriesApi#example)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/SeriesApi#parameters)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/SeriesApi#return-type)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/SeriesApi#http-response-details)
    
*   [get\_series\_by\_ticker](https://docs.kalshi.com/python-sdk/api/SeriesApi#get-series-by-ticker)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/SeriesApi#example-2)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/SeriesApi#parameters-2)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/SeriesApi#return-type-2)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/SeriesApi#http-response-details-2)
    

All URIs are relative to _[https://api.elections.kalshi.com/trade-api/v2](https://api.elections.kalshi.com/trade-api/v2)
_

| Method | HTTP request | Description |
| --- | --- | --- |
| [**get\_series**](https://docs.kalshi.com/python-sdk/api/SeriesApi#get-series) | **GET** /series | Get Series |
| [**get\_series\_by\_ticker**](https://docs.kalshi.com/python-sdk/api/SeriesApi#get-series-by-ticker) | **GET** /series/ | Get Series by Ticker |

[​](https://docs.kalshi.com/python-sdk/api/SeriesApi#get-series)

**get\_series**
===================================================================================

> GetSeriesResponse get\_series(status=status)

Get Series Get all market series

### 

[​](https://docs.kalshi.com/python-sdk/api/SeriesApi#example)

Example

Copy

Ask AI

    import kalshi_python
    from kalshi_python.models.get_series_response import GetSeriesResponse
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
    
    status = 'status_example' # str | Filter by series status (optional)
    
    try:
        # Get Series
        api_response = client.get_series(status=status)
        print("The response of SeriesApi->get_series:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeriesApi->get_series: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/SeriesApi#parameters)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **status** | **str** | Filter by series status | \[optional\] |

### 

[​](https://docs.kalshi.com/python-sdk/api/SeriesApi#return-type)

Return type

[**GetSeriesResponse**](https://docs.kalshi.com/python-sdk/models/GetSeriesResponse)

### 

[​](https://docs.kalshi.com/python-sdk/api/SeriesApi#http-response-details)

HTTP response details

| Status code | Description |
| --- | --- |
| **200** | Series retrieved successfully |
| **401** | Unauthorized - authentication required |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/SeriesApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[​](https://docs.kalshi.com/python-sdk/api/SeriesApi#get-series-by-ticker)

**get\_series\_by\_ticker**
=========================================================================================================

> GetSeriesByTickerResponse get\_series\_by\_ticker(ticker)

Get Series by Ticker Get a single series by its ticker

### 

[​](https://docs.kalshi.com/python-sdk/api/SeriesApi#example-2)

Example

Copy

Ask AI

    import kalshi_python
    from kalshi_python.models.get_series_by_ticker_response import GetSeriesByTickerResponse
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
    
    ticker = 'ticker_example' # str | The series ticker
    
    try:
        # Get Series by Ticker
        api_response = client.get_series_by_ticker(ticker)
        print("The response of SeriesApi->get_series_by_ticker:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SeriesApi->get_series_by_ticker: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/SeriesApi#parameters-2)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **ticker** | **str** | The series ticker |     |

### 

[​](https://docs.kalshi.com/python-sdk/api/SeriesApi#return-type-2)

Return type

[**GetSeriesByTickerResponse**](https://docs.kalshi.com/python-sdk/models/GetSeriesByTickerResponse)

### 

[​](https://docs.kalshi.com/python-sdk/api/SeriesApi#http-response-details-2)

HTTP response details

| Status code | Description |
| --- | --- |
| **200** | Series retrieved successfully |
| **401** | Unauthorized - authentication required |
| **404** | Resource not found |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/SeriesApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[Events](https://docs.kalshi.com/python-sdk/api/EventsApi)
[Milestones](https://docs.kalshi.com/python-sdk/api/MilestonesApi)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.