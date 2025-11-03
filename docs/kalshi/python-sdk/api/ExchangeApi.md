---
url: https://docs.kalshi.com/python-sdk/api/ExchangeApi
title: Exchange - API Documentation
description: Python SDK methods for Exchange operations
scraped_at: 2025-11-03T14:46:41.344430
---

[Skip to main content](https://docs.kalshi.com/python-sdk/api/ExchangeApi#content-area)

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

*   [get\_exchange\_announcements](https://docs.kalshi.com/python-sdk/api/ExchangeApi#get-exchange-announcements)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/ExchangeApi#example)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/ExchangeApi#parameters)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/ExchangeApi#return-type)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/ExchangeApi#http-response-details)
    
*   [get\_exchange\_schedule](https://docs.kalshi.com/python-sdk/api/ExchangeApi#get-exchange-schedule)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/ExchangeApi#example-2)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/ExchangeApi#parameters-2)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/ExchangeApi#return-type-2)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/ExchangeApi#http-response-details-2)
    
*   [get\_exchange\_status](https://docs.kalshi.com/python-sdk/api/ExchangeApi#get-exchange-status)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/ExchangeApi#example-3)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/ExchangeApi#parameters-3)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/ExchangeApi#return-type-3)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/ExchangeApi#http-response-details-3)
    
*   [get\_user\_data\_timestamp](https://docs.kalshi.com/python-sdk/api/ExchangeApi#get-user-data-timestamp)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/ExchangeApi#example-4)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/ExchangeApi#parameters-4)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/ExchangeApi#return-type-4)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/ExchangeApi#http-response-details-4)
    

All URIs are relative to _[https://api.elections.kalshi.com/trade-api/v2](https://api.elections.kalshi.com/trade-api/v2)
_

| Method | HTTP request | Description |
| --- | --- | --- |
| [**get\_exchange\_announcements**](https://docs.kalshi.com/python-sdk/api/ExchangeApi#get-exchange-announcements) | **GET** /exchange/announcements | Get Exchange Announcements |
| [**get\_exchange\_schedule**](https://docs.kalshi.com/python-sdk/api/ExchangeApi#get-exchange-schedule) | **GET** /exchange/schedule | Get Exchange Schedule |
| [**get\_exchange\_status**](https://docs.kalshi.com/python-sdk/api/ExchangeApi#get-exchange-status) | **GET** /exchange/status | Get Exchange Status |
| [**get\_user\_data\_timestamp**](https://docs.kalshi.com/python-sdk/api/ExchangeApi#get-user-data-timestamp) | **GET** /exchange/user\_data\_timestamp | Get User Data Timestamp |

[​](https://docs.kalshi.com/python-sdk/api/ExchangeApi#get-exchange-announcements)

**get\_exchange\_announcements**
======================================================================================================================

> GetExchangeAnnouncementsResponse get\_exchange\_announcements()

Get Exchange Announcements Get all exchange-wide announcements

### 

[​](https://docs.kalshi.com/python-sdk/api/ExchangeApi#example)

Example

Copy

Ask AI

    import kalshi_python
    from kalshi_python.models.get_exchange_announcements_response import GetExchangeAnnouncementsResponse
    from kalshi_python.rest import ApiException
    from pprint import pprint
    
    # Defining the host is optional and defaults to https://api.elections.kalshi.com/trade-api/v2
    # See configuration.py for a list of all supported configuration parameters.
    configuration = kalshi_python.Configuration(
        host = "https://api.elections.kalshi.com/trade-api/v2"
    )
    
    
    # Initialize the Kalshi client
    client = kalshi_python.KalshiClient(configuration)
    
    try:
        # Get Exchange Announcements
        api_response = client.get_exchange_announcements()
        print("The response of ExchangeApi->get_exchange_announcements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExchangeApi->get_exchange_announcements: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/ExchangeApi#parameters)

Parameters

This endpoint does not need any parameter.

### 

[​](https://docs.kalshi.com/python-sdk/api/ExchangeApi#return-type)

Return type

[**GetExchangeAnnouncementsResponse**](https://docs.kalshi.com/python-sdk/models/GetExchangeAnnouncementsResponse)

### 

[​](https://docs.kalshi.com/python-sdk/api/ExchangeApi#http-response-details)

HTTP response details

| Status code | Description |
| --- | --- |
| **200** | Announcements retrieved successfully |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/ExchangeApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[​](https://docs.kalshi.com/python-sdk/api/ExchangeApi#get-exchange-schedule)

**get\_exchange\_schedule**
============================================================================================================

> GetExchangeScheduleResponse get\_exchange\_schedule()

Get Exchange Schedule Get the exchange schedule

### 

[​](https://docs.kalshi.com/python-sdk/api/ExchangeApi#example-2)

Example

Copy

Ask AI

    import kalshi_python
    from kalshi_python.models.get_exchange_schedule_response import GetExchangeScheduleResponse
    from kalshi_python.rest import ApiException
    from pprint import pprint
    
    # Defining the host is optional and defaults to https://api.elections.kalshi.com/trade-api/v2
    # See configuration.py for a list of all supported configuration parameters.
    configuration = kalshi_python.Configuration(
        host = "https://api.elections.kalshi.com/trade-api/v2"
    )
    
    
    # Initialize the Kalshi client
    client = kalshi_python.KalshiClient(configuration)
    
    try:
        # Get Exchange Schedule
        api_response = client.get_exchange_schedule()
        print("The response of ExchangeApi->get_exchange_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExchangeApi->get_exchange_schedule: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/ExchangeApi#parameters-2)

Parameters

This endpoint does not need any parameter.

### 

[​](https://docs.kalshi.com/python-sdk/api/ExchangeApi#return-type-2)

Return type

[**GetExchangeScheduleResponse**](https://docs.kalshi.com/python-sdk/models/GetExchangeScheduleResponse)

### 

[​](https://docs.kalshi.com/python-sdk/api/ExchangeApi#http-response-details-2)

HTTP response details

| Status code | Description |
| --- | --- |
| **200** | Schedule retrieved successfully |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/ExchangeApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[​](https://docs.kalshi.com/python-sdk/api/ExchangeApi#get-exchange-status)

**get\_exchange\_status**
========================================================================================================

> ExchangeStatus get\_exchange\_status()

Get Exchange Status Get the exchange status

### 

[​](https://docs.kalshi.com/python-sdk/api/ExchangeApi#example-3)

Example

Copy

Ask AI

    import kalshi_python
    from kalshi_python.models.exchange_status import ExchangeStatus
    from kalshi_python.rest import ApiException
    from pprint import pprint
    
    # Defining the host is optional and defaults to https://api.elections.kalshi.com/trade-api/v2
    # See configuration.py for a list of all supported configuration parameters.
    configuration = kalshi_python.Configuration(
        host = "https://api.elections.kalshi.com/trade-api/v2"
    )
    
    
    # Initialize the Kalshi client
    client = kalshi_python.KalshiClient(configuration)
    
    try:
        # Get Exchange Status
        api_response = client.get_exchange_status()
        print("The response of ExchangeApi->get_exchange_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExchangeApi->get_exchange_status: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/ExchangeApi#parameters-3)

Parameters

This endpoint does not need any parameter.

### 

[​](https://docs.kalshi.com/python-sdk/api/ExchangeApi#return-type-3)

Return type

[**ExchangeStatus**](https://docs.kalshi.com/python-sdk/models/ExchangeStatus)

### 

[​](https://docs.kalshi.com/python-sdk/api/ExchangeApi#http-response-details-3)

HTTP response details

| Status code | Description |
| --- | --- |
| **200** | Status retrieved successfully |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/ExchangeApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[​](https://docs.kalshi.com/python-sdk/api/ExchangeApi#get-user-data-timestamp)

**get\_user\_data\_timestamp**
=================================================================================================================

> GetUserDataTimestampResponse get\_user\_data\_timestamp()

Get User Data Timestamp There is typically a short delay before exchange events are reflected in the API endpoints. Whenever possible, combine API responses to PUT/POST/DELETE requests with websocket data to obtain the most accurate view of the exchange state. This endpoint provides an approximate indication of when the data from the following endpoints was last validated: GetBalance, GetOrder(s), GetFills, GetPositions

### 

[​](https://docs.kalshi.com/python-sdk/api/ExchangeApi#example-4)

Example

Copy

Ask AI

    import kalshi_python
    from kalshi_python.models.get_user_data_timestamp_response import GetUserDataTimestampResponse
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
        # Get User Data Timestamp
        api_response = client.get_user_data_timestamp()
        print("The response of ExchangeApi->get_user_data_timestamp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExchangeApi->get_user_data_timestamp: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/ExchangeApi#parameters-4)

Parameters

This endpoint does not need any parameter.

### 

[​](https://docs.kalshi.com/python-sdk/api/ExchangeApi#return-type-4)

Return type

[**GetUserDataTimestampResponse**](https://docs.kalshi.com/python-sdk/models/GetUserDataTimestampResponse)

### 

[​](https://docs.kalshi.com/python-sdk/api/ExchangeApi#http-response-details-4)

HTTP response details

| Status code | Description |
| --- | --- |
| **200** | Timestamp retrieved successfully |
| **401** | Unauthorized - authentication required |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/ExchangeApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[StructuredTargets](https://docs.kalshi.com/python-sdk/api/StructuredTargetsApi)
[ApiKeys](https://docs.kalshi.com/python-sdk/api/ApiKeysApi)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.