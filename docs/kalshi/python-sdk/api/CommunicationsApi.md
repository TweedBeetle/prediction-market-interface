---
url: https://docs.kalshi.com/python-sdk/api/CommunicationsApi
title: Communications - API Documentation
description: Python SDK methods for Communications operations
scraped_at: 2025-11-03T14:46:40.334157
---

[Skip to main content](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#content-area)

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

*   [accept\_quote](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#accept-quote)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#example)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#parameters)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#return-type)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#http-response-details)
    
*   [confirm\_quote](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#confirm-quote)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#example-2)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#parameters-2)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#return-type-2)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#http-response-details-2)
    
*   [create\_quote](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#create-quote)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#example-3)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#parameters-3)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#return-type-3)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#http-response-details-3)
    
*   [create\_rfq](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#create-rfq)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#example-4)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#parameters-4)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#return-type-4)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#http-response-details-4)
    
*   [delete\_quote](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#delete-quote)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#example-5)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#parameters-5)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#return-type-5)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#http-response-details-5)
    
*   [delete\_rfq](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#delete-rfq)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#example-6)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#parameters-6)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#return-type-6)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#http-response-details-6)
    
*   [get\_communications\_id](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#get-communications-id)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#example-7)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#parameters-7)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#return-type-7)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#http-response-details-7)
    
*   [get\_quote](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#get-quote)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#example-8)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#parameters-8)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#return-type-8)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#http-response-details-8)
    
*   [get\_quotes](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#get-quotes)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#example-9)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#parameters-9)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#return-type-9)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#http-response-details-9)
    
*   [get\_rfq](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#get-rfq)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#example-10)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#parameters-10)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#return-type-10)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#http-response-details-10)
    
*   [get\_rfqs](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#get-rfqs)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#example-11)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#parameters-11)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#return-type-11)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#http-response-details-11)
    

All URIs are relative to _[https://api.elections.kalshi.com/trade-api/v2](https://api.elections.kalshi.com/trade-api/v2)
_

| Method | HTTP request | Description |
| --- | --- | --- |
| [**accept\_quote**](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#accept-quote) | **PUT** /communications/quotes//accept | Accept Quote |
| [**confirm\_quote**](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#confirm-quote) | **PUT** /communications/quotes//confirm | Confirm Quote |
| [**create\_quote**](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#create-quote) | **POST** /communications/quotes | Create Quote |
| [**create\_rfq**](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#create-rfq) | **POST** /communications/rfqs | Create RFQ |
| [**delete\_quote**](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#delete-quote) | **DELETE** /communications/quotes/ | Delete Quote |
| [**delete\_rfq**](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#delete-rfq) | **DELETE** /communications/rfqs/ | Delete RFQ |
| [**get\_communications\_id**](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#get-communications-id) | **GET** /communications/id | Get Communications ID |
| [**get\_quote**](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#get-quote) | **GET** /communications/quotes/ | Get Quote |
| [**get\_quotes**](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#get-quotes) | **GET** /communications/quotes | Get Quotes |
| [**get\_rfq**](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#get-rfq) | **GET** /communications/rfqs/ | Get RFQ |
| [**get\_rfqs**](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#get-rfqs) | **GET** /communications/rfqs | Get RFQs |

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#accept-quote)

**accept\_quote**
===============================================================================================

> accept\_quote(quote\_id, accept\_quote\_request)

Accept Quote Accept a quote. This will require the quoter to confirm

### 

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#example)

Example

Copy

Ask AI

    import kalshi_python
    from kalshi_python.models.accept_quote_request import AcceptQuoteRequest
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
    
    quote_id = 'quote_id_example' # str | Quote ID
    
    accept_quote_request = kalshi_python.AcceptQuoteRequest() # AcceptQuoteRequest |
    
    try:
        # Accept Quote
        client.accept_quote(quote_id, accept_quote_request)
    except Exception as e:
        print("Exception when calling CommunicationsApi->accept_quote: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#parameters)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **quote\_id** | **str** | Quote ID |     |
| **accept\_quote\_request** | [**AcceptQuoteRequest**](https://docs.kalshi.com/python-sdk/models/AcceptQuoteRequest) |     |     |

### 

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#return-type)

Return type

void (empty response body)

### 

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#http-response-details)

HTTP response details

| Status code | Description |
| --- | --- |
| **204** | Quote accepted successfully |
| **400** | Bad request - invalid input |
| **401** | Unauthorized - authentication required |
| **404** | Resource not found |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#confirm-quote)

**confirm\_quote**
=================================================================================================

> confirm\_quote(quote\_id)

Confirm Quote Confirm a quote. This will start a timer for order execution

### 

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#example-2)

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
    
    quote_id = 'quote_id_example' # str | Quote ID
    
    try:
        # Confirm Quote
        client.confirm_quote(quote_id)
    except Exception as e:
        print("Exception when calling CommunicationsApi->confirm_quote: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#parameters-2)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **quote\_id** | **str** | Quote ID |     |

### 

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#return-type-2)

Return type

void (empty response body)

### 

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#http-response-details-2)

HTTP response details

| Status code | Description |
| --- | --- |
| **204** | Quote confirmed successfully |
| **401** | Unauthorized - authentication required |
| **404** | Resource not found |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#create-quote)

**create\_quote**
===============================================================================================

> CreateQuoteResponse create\_quote(create\_quote\_request)

Create Quote Create a quote in response to an RFQ

### 

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#example-3)

Example

Copy

Ask AI

    import kalshi_python
    from kalshi_python.models.create_quote_request import CreateQuoteRequest
    from kalshi_python.models.create_quote_response import CreateQuoteResponse
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
    
    create_quote_request = kalshi_python.CreateQuoteRequest() # CreateQuoteRequest |
    
    try:
        # Create Quote
        api_response = client.create_quote(create_quote_request)
        print("The response of CommunicationsApi->create_quote:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunicationsApi->create_quote: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#parameters-3)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **create\_quote\_request** | [**CreateQuoteRequest**](https://docs.kalshi.com/python-sdk/models/CreateQuoteRequest) |     |     |

### 

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#return-type-3)

Return type

[**CreateQuoteResponse**](https://docs.kalshi.com/python-sdk/models/CreateQuoteResponse)

### 

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#http-response-details-3)

HTTP response details

| Status code | Description |
| --- | --- |
| **201** | Quote created successfully |
| **400** | Bad request - invalid input |
| **401** | Unauthorized - authentication required |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#create-rfq)

**create\_rfq**
===========================================================================================

> CreateRFQResponse create\_rfq(create\_rfq\_request)

Create RFQ Create a new RFQ

### 

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#example-4)

Example

Copy

Ask AI

    import kalshi_python
    from kalshi_python.models.create_rfq_request import CreateRFQRequest
    from kalshi_python.models.create_rfq_response import CreateRFQResponse
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
    
    create_rfq_request = kalshi_python.CreateRFQRequest() # CreateRFQRequest |
    
    try:
        # Create RFQ
        api_response = client.create_rfq(create_rfq_request)
        print("The response of CommunicationsApi->create_rfq:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunicationsApi->create_rfq: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#parameters-4)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **create\_rfq\_request** | [**CreateRFQRequest**](https://docs.kalshi.com/python-sdk/models/CreateRFQRequest) |     |     |

### 

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#return-type-4)

Return type

[**CreateRFQResponse**](https://docs.kalshi.com/python-sdk/models/CreateRFQResponse)

### 

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#http-response-details-4)

HTTP response details

| Status code | Description |
| --- | --- |
| **201** | RFQ created successfully |
| **400** | Bad request - invalid input |
| **401** | Unauthorized - authentication required |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#delete-quote)

**delete\_quote**
===============================================================================================

> delete\_quote(quote\_id)

Delete Quote Delete a quote, which means it can no longer be accepted

### 

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#example-5)

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
    
    quote_id = 'quote_id_example' # str | Quote ID
    
    try:
        # Delete Quote
        client.delete_quote(quote_id)
    except Exception as e:
        print("Exception when calling CommunicationsApi->delete_quote: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#parameters-5)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **quote\_id** | **str** | Quote ID |     |

### 

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#return-type-5)

Return type

void (empty response body)

### 

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#http-response-details-5)

HTTP response details

| Status code | Description |
| --- | --- |
| **204** | Quote deleted successfully |
| **401** | Unauthorized - authentication required |
| **404** | Resource not found |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#delete-rfq)

**delete\_rfq**
===========================================================================================

> delete\_rfq(rfq\_id)

Delete RFQ Delete an RFQ by ID

### 

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#example-6)

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
    
    rfq_id = 'rfq_id_example' # str | RFQ ID
    
    try:
        # Delete RFQ
        client.delete_rfq(rfq_id)
    except Exception as e:
        print("Exception when calling CommunicationsApi->delete_rfq: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#parameters-6)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **rfq\_id** | **str** | RFQ ID |     |

### 

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#return-type-6)

Return type

void (empty response body)

### 

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#http-response-details-6)

HTTP response details

| Status code | Description |
| --- | --- |
| **204** | RFQ deleted successfully |
| **401** | Unauthorized - authentication required |
| **404** | Resource not found |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#get-communications-id)

**get\_communications\_id**
==================================================================================================================

> GetCommunicationsIDResponse get\_communications\_id()

Get Communications ID Get the communications ID of the logged-in user

### 

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#example-7)

Example

Copy

Ask AI

    import kalshi_python
    from kalshi_python.models.get_communications_id_response import GetCommunicationsIDResponse
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
        # Get Communications ID
        api_response = client.get_communications_id()
        print("The response of CommunicationsApi->get_communications_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunicationsApi->get_communications_id: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#parameters-7)

Parameters

This endpoint does not need any parameter.

### 

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#return-type-7)

Return type

[**GetCommunicationsIDResponse**](https://docs.kalshi.com/python-sdk/models/GetCommunicationsIDResponse)

### 

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#http-response-details-7)

HTTP response details

| Status code | Description |
| --- | --- |
| **200** | Communications ID retrieved successfully |
| **401** | Unauthorized - authentication required |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#get-quote)

**get\_quote**
=========================================================================================

> GetQuoteResponse get\_quote(quote\_id)

Get Quote Get a particular quote by ID

### 

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#example-8)

Example

Copy

Ask AI

    import kalshi_python
    from kalshi_python.models.get_quote_response import GetQuoteResponse
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
    
    quote_id = 'quote_id_example' # str | Quote ID
    
    try:
        # Get Quote
        api_response = client.get_quote(quote_id)
        print("The response of CommunicationsApi->get_quote:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunicationsApi->get_quote: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#parameters-8)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **quote\_id** | **str** | Quote ID |     |

### 

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#return-type-8)

Return type

[**GetQuoteResponse**](https://docs.kalshi.com/python-sdk/models/GetQuoteResponse)

### 

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#http-response-details-8)

HTTP response details

| Status code | Description |
| --- | --- |
| **200** | Quote retrieved successfully |
| **401** | Unauthorized - authentication required |
| **404** | Resource not found |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#get-quotes)

**get\_quotes**
===========================================================================================

> GetQuotesResponse get\_quotes()

Get Quotes Retrieve all quotes

### 

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#example-9)

Example

Copy

Ask AI

    import kalshi_python
    from kalshi_python.models.get_quotes_response import GetQuotesResponse
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
        # Get Quotes
        api_response = client.get_quotes()
        print("The response of CommunicationsApi->get_quotes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunicationsApi->get_quotes: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#parameters-9)

Parameters

This endpoint does not need any parameter.

### 

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#return-type-9)

Return type

[**GetQuotesResponse**](https://docs.kalshi.com/python-sdk/models/GetQuotesResponse)

### 

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#http-response-details-9)

HTTP response details

| Status code | Description |
| --- | --- |
| **200** | Quotes retrieved successfully |
| **401** | Unauthorized - authentication required |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#get-rfq)

**get\_rfq**
=====================================================================================

> GetRFQResponse get\_rfq(rfq\_id)

Get RFQ Get a single RFQ by ID

### 

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#example-10)

Example

Copy

Ask AI

    import kalshi_python
    from kalshi_python.models.get_rfq_response import GetRFQResponse
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
    
    rfq_id = 'rfq_id_example' # str | RFQ ID
    
    try:
        # Get RFQ
        api_response = client.get_rfq(rfq_id)
        print("The response of CommunicationsApi->get_rfq:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunicationsApi->get_rfq: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#parameters-10)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **rfq\_id** | **str** | RFQ ID |     |

### 

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#return-type-10)

Return type

[**GetRFQResponse**](https://docs.kalshi.com/python-sdk/models/GetRFQResponse)

### 

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#http-response-details-10)

HTTP response details

| Status code | Description |
| --- | --- |
| **200** | RFQ retrieved successfully |
| **401** | Unauthorized - authentication required |
| **404** | Resource not found |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#get-rfqs)

**get\_rfqs**
=======================================================================================

> GetRFQsResponse get\_rfqs()

Get RFQs Retrieve all RFQs

### 

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#example-11)

Example

Copy

Ask AI

    import kalshi_python
    from kalshi_python.models.get_rfqs_response import GetRFQsResponse
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
        # Get RFQs
        api_response = client.get_rfqs()
        print("The response of CommunicationsApi->get_rfqs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommunicationsApi->get_rfqs: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#parameters-11)

Parameters

This endpoint does not need any parameter.

### 

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#return-type-11)

Return type

[**GetRFQsResponse**](https://docs.kalshi.com/python-sdk/models/GetRFQsResponse)

### 

[​](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#http-response-details-11)

HTTP response details

| Status code | Description |
| --- | --- |
| **200** | RFQs retrieved successfully |
| **401** | Unauthorized - authentication required |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/CommunicationsApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[Markets](https://docs.kalshi.com/python-sdk/api/MarketsApi)
[Events](https://docs.kalshi.com/python-sdk/api/EventsApi)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.