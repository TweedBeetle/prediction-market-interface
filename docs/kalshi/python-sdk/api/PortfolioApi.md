---
url: https://docs.kalshi.com/python-sdk/api/PortfolioApi
title: Portfolio - API Documentation
description: Python SDK methods for Portfolio operations
scraped_at: 2025-11-03T14:46:42.086682
---

[Skip to main content](https://docs.kalshi.com/python-sdk/api/PortfolioApi#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

API Classes

Portfolio

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

On this page

*   [amend\_order](https://docs.kalshi.com/python-sdk/api/PortfolioApi#amend-order)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/PortfolioApi#example)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/PortfolioApi#parameters)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/PortfolioApi#return-type)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/PortfolioApi#http-response-details)
    
*   [batch\_cancel\_orders](https://docs.kalshi.com/python-sdk/api/PortfolioApi#batch-cancel-orders)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/PortfolioApi#example-2)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/PortfolioApi#parameters-2)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/PortfolioApi#return-type-2)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/PortfolioApi#http-response-details-2)
    
*   [batch\_create\_orders](https://docs.kalshi.com/python-sdk/api/PortfolioApi#batch-create-orders)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/PortfolioApi#example-3)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/PortfolioApi#parameters-3)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/PortfolioApi#return-type-3)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/PortfolioApi#http-response-details-3)
    
*   [cancel\_order](https://docs.kalshi.com/python-sdk/api/PortfolioApi#cancel-order)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/PortfolioApi#example-4)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/PortfolioApi#parameters-4)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/PortfolioApi#return-type-4)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/PortfolioApi#http-response-details-4)
    
*   [create\_order](https://docs.kalshi.com/python-sdk/api/PortfolioApi#create-order)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/PortfolioApi#example-5)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/PortfolioApi#parameters-5)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/PortfolioApi#return-type-5)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/PortfolioApi#http-response-details-5)
    
*   [create\_order\_group](https://docs.kalshi.com/python-sdk/api/PortfolioApi#create-order-group)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/PortfolioApi#example-6)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/PortfolioApi#parameters-6)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/PortfolioApi#return-type-6)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/PortfolioApi#http-response-details-6)
    
*   [decrease\_order](https://docs.kalshi.com/python-sdk/api/PortfolioApi#decrease-order)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/PortfolioApi#example-7)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/PortfolioApi#parameters-7)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/PortfolioApi#return-type-7)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/PortfolioApi#http-response-details-7)
    
*   [delete\_order\_group](https://docs.kalshi.com/python-sdk/api/PortfolioApi#delete-order-group)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/PortfolioApi#example-8)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/PortfolioApi#parameters-8)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/PortfolioApi#return-type-8)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/PortfolioApi#http-response-details-8)
    
*   [get\_balance](https://docs.kalshi.com/python-sdk/api/PortfolioApi#get-balance)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/PortfolioApi#example-9)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/PortfolioApi#parameters-9)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/PortfolioApi#return-type-9)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/PortfolioApi#http-response-details-9)
    
*   [get\_fills](https://docs.kalshi.com/python-sdk/api/PortfolioApi#get-fills)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/PortfolioApi#example-10)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/PortfolioApi#parameters-10)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/PortfolioApi#return-type-10)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/PortfolioApi#http-response-details-10)
    
*   [get\_order](https://docs.kalshi.com/python-sdk/api/PortfolioApi#get-order)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/PortfolioApi#example-11)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/PortfolioApi#parameters-11)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/PortfolioApi#return-type-11)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/PortfolioApi#http-response-details-11)
    
*   [get\_order\_group](https://docs.kalshi.com/python-sdk/api/PortfolioApi#get-order-group)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/PortfolioApi#example-12)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/PortfolioApi#parameters-12)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/PortfolioApi#return-type-12)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/PortfolioApi#http-response-details-12)
    
*   [get\_order\_groups](https://docs.kalshi.com/python-sdk/api/PortfolioApi#get-order-groups)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/PortfolioApi#example-13)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/PortfolioApi#parameters-13)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/PortfolioApi#return-type-13)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/PortfolioApi#http-response-details-13)
    
*   [get\_order\_queue\_position](https://docs.kalshi.com/python-sdk/api/PortfolioApi#get-order-queue-position)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/PortfolioApi#example-14)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/PortfolioApi#parameters-14)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/PortfolioApi#return-type-14)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/PortfolioApi#http-response-details-14)
    
*   [get\_orders](https://docs.kalshi.com/python-sdk/api/PortfolioApi#get-orders)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/PortfolioApi#example-15)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/PortfolioApi#parameters-15)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/PortfolioApi#return-type-15)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/PortfolioApi#http-response-details-15)
    
*   [get\_positions](https://docs.kalshi.com/python-sdk/api/PortfolioApi#get-positions)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/PortfolioApi#example-16)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/PortfolioApi#parameters-16)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/PortfolioApi#return-type-16)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/PortfolioApi#http-response-details-16)
    
*   [get\_queue\_positions](https://docs.kalshi.com/python-sdk/api/PortfolioApi#get-queue-positions)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/PortfolioApi#example-17)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/PortfolioApi#parameters-17)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/PortfolioApi#return-type-17)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/PortfolioApi#http-response-details-17)
    
*   [get\_settlements](https://docs.kalshi.com/python-sdk/api/PortfolioApi#get-settlements)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/PortfolioApi#example-18)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/PortfolioApi#parameters-18)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/PortfolioApi#return-type-18)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/PortfolioApi#http-response-details-18)
    
*   [get\_total\_resting\_order\_value](https://docs.kalshi.com/python-sdk/api/PortfolioApi#get-total-resting-order-value)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/PortfolioApi#example-19)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/PortfolioApi#parameters-19)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/PortfolioApi#return-type-19)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/PortfolioApi#http-response-details-19)
    
*   [reset\_order\_group](https://docs.kalshi.com/python-sdk/api/PortfolioApi#reset-order-group)
    
*   [Example](https://docs.kalshi.com/python-sdk/api/PortfolioApi#example-20)
    
*   [Parameters](https://docs.kalshi.com/python-sdk/api/PortfolioApi#parameters-20)
    
*   [Return type](https://docs.kalshi.com/python-sdk/api/PortfolioApi#return-type-20)
    
*   [HTTP response details](https://docs.kalshi.com/python-sdk/api/PortfolioApi#http-response-details-20)
    

All URIs are relative to _[https://api.elections.kalshi.com/trade-api/v2](https://api.elections.kalshi.com/trade-api/v2)
_

| Method | HTTP request | Description |
| --- | --- | --- |
| [**amend\_order**](https://docs.kalshi.com/python-sdk/api/PortfolioApi#amend-order) | **POST** /portfolio/orders//amend | Amend Order |
| [**batch\_cancel\_orders**](https://docs.kalshi.com/python-sdk/api/PortfolioApi#batch-cancel-orders) | **DELETE** /portfolio/orders/batched | Batch Cancel Orders |
| [**batch\_create\_orders**](https://docs.kalshi.com/python-sdk/api/PortfolioApi#batch-create-orders) | **POST** /portfolio/orders/batched | Batch Create Orders |
| [**cancel\_order**](https://docs.kalshi.com/python-sdk/api/PortfolioApi#cancel-order) | **DELETE** /portfolio/orders/ | Cancel Order |
| [**create\_order**](https://docs.kalshi.com/python-sdk/api/PortfolioApi#create-order) | **POST** /portfolio/orders | Create Order |
| [**create\_order\_group**](https://docs.kalshi.com/python-sdk/api/PortfolioApi#create-order-group) | **POST** /portfolio/order\_groups/create | Create Order Group |
| [**decrease\_order**](https://docs.kalshi.com/python-sdk/api/PortfolioApi#decrease-order) | **POST** /portfolio/orders//decrease | Decrease Order |
| [**delete\_order\_group**](https://docs.kalshi.com/python-sdk/api/PortfolioApi#delete-order-group) | **DELETE** /portfolio/order\_groups/ | Delete Order Group |
| [**get\_balance**](https://docs.kalshi.com/python-sdk/api/PortfolioApi#get-balance) | **GET** /portfolio/balance | Get Balance |
| [**get\_fills**](https://docs.kalshi.com/python-sdk/api/PortfolioApi#get-fills) | **GET** /portfolio/fills | Get Fills |
| [**get\_order**](https://docs.kalshi.com/python-sdk/api/PortfolioApi#get-order) | **GET** /portfolio/orders/ | Get Order |
| [**get\_order\_group**](https://docs.kalshi.com/python-sdk/api/PortfolioApi#get-order-group) | **GET** /portfolio/order\_groups/ | Get Order Group |
| [**get\_order\_groups**](https://docs.kalshi.com/python-sdk/api/PortfolioApi#get-order-groups) | **GET** /portfolio/order\_groups | Get Order Groups |
| [**get\_order\_queue\_position**](https://docs.kalshi.com/python-sdk/api/PortfolioApi#get-order-queue-position) | **GET** /portfolio/orders//queue\_position | Get Order Queue Position |
| [**get\_orders**](https://docs.kalshi.com/python-sdk/api/PortfolioApi#get-orders) | **GET** /portfolio/orders | Get Orders |
| [**get\_positions**](https://docs.kalshi.com/python-sdk/api/PortfolioApi#get-positions) | **GET** /portfolio/positions | Get Positions |
| [**get\_queue\_positions**](https://docs.kalshi.com/python-sdk/api/PortfolioApi#get-queue-positions) | **POST** /portfolio/orders/queue\_positions | Get Queue Positions |
| [**get\_settlements**](https://docs.kalshi.com/python-sdk/api/PortfolioApi#get-settlements) | **GET** /portfolio/settlements | Get Settlements |
| [**get\_total\_resting\_order\_value**](https://docs.kalshi.com/python-sdk/api/PortfolioApi#get-total-resting-order-value) | **GET** /portfolio/summary/total\_resting\_order\_value | Get Total Resting Order Value |
| [**reset\_order\_group**](https://docs.kalshi.com/python-sdk/api/PortfolioApi#reset-order-group) | **PUT** /portfolio/order\_groups//reset | Reset Order Group |

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#amend-order)

**amend\_order**
========================================================================================

> AmendOrderResponse amend\_order(order\_id, amend\_order\_request)

Amend Order Amend an existing order

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#example)

Example

Copy

Ask AI

    import kalshi_python
    from kalshi_python.models.amend_order_request import AmendOrderRequest
    from kalshi_python.models.amend_order_response import AmendOrderResponse
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
    
    order_id = 'order_id_example' # str | Order ID
    
    amend_order_request = kalshi_python.AmendOrderRequest() # AmendOrderRequest |
    
    try:
        # Amend Order
        api_response = client.amend_order(order_id, amend_order_request)
        print("The response of PortfolioApi->amend_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioApi->amend_order: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#parameters)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **order\_id** | **str** | Order ID |     |
| **amend\_order\_request** | [**AmendOrderRequest**](https://docs.kalshi.com/python-sdk/models/AmendOrderRequest) |     |     |

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#return-type)

Return type

[**AmendOrderResponse**](https://docs.kalshi.com/python-sdk/models/AmendOrderResponse)

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#http-response-details)

HTTP response details

| Status code | Description |
| --- | --- |
| **200** | Order amended successfully |
| **400** | Bad request - invalid input |
| **401** | Unauthorized - authentication required |
| **404** | Resource not found |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/PortfolioApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#batch-cancel-orders)

**batch\_cancel\_orders**
=========================================================================================================

> BatchCancelOrdersResponse batch\_cancel\_orders(batch\_cancel\_orders\_request)

Batch Cancel Orders Cancel multiple orders in a single request

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#example-2)

Example

Copy

Ask AI

    import kalshi_python
    from kalshi_python.models.batch_cancel_orders_request import BatchCancelOrdersRequest
    from kalshi_python.models.batch_cancel_orders_response import BatchCancelOrdersResponse
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
    
    batch_cancel_orders_request = kalshi_python.BatchCancelOrdersRequest() # BatchCancelOrdersRequest |
    
    try:
        # Batch Cancel Orders
        api_response = client.batch_cancel_orders(batch_cancel_orders_request)
        print("The response of PortfolioApi->batch_cancel_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioApi->batch_cancel_orders: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#parameters-2)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **batch\_cancel\_orders\_request** | [**BatchCancelOrdersRequest**](https://docs.kalshi.com/python-sdk/models/BatchCancelOrdersRequest) |     |     |

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#return-type-2)

Return type

[**BatchCancelOrdersResponse**](https://docs.kalshi.com/python-sdk/models/BatchCancelOrdersResponse)

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#http-response-details-2)

HTTP response details

| Status code | Description |
| --- | --- |
| **200** | Batch order cancellation completed |
| **400** | Bad request - invalid input |
| **401** | Unauthorized - authentication required |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/PortfolioApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#batch-create-orders)

**batch\_create\_orders**
=========================================================================================================

> BatchCreateOrdersResponse batch\_create\_orders(batch\_create\_orders\_request)

Batch Create Orders Create multiple orders in a single request

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#example-3)

Example

Copy

Ask AI

    import kalshi_python
    from kalshi_python.models.batch_create_orders_request import BatchCreateOrdersRequest
    from kalshi_python.models.batch_create_orders_response import BatchCreateOrdersResponse
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
    
    batch_create_orders_request = kalshi_python.BatchCreateOrdersRequest() # BatchCreateOrdersRequest |
    
    try:
        # Batch Create Orders
        api_response = client.batch_create_orders(batch_create_orders_request)
        print("The response of PortfolioApi->batch_create_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioApi->batch_create_orders: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#parameters-3)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **batch\_create\_orders\_request** | [**BatchCreateOrdersRequest**](https://docs.kalshi.com/python-sdk/models/BatchCreateOrdersRequest) |     |     |

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#return-type-3)

Return type

[**BatchCreateOrdersResponse**](https://docs.kalshi.com/python-sdk/models/BatchCreateOrdersResponse)

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#http-response-details-3)

HTTP response details

| Status code | Description |
| --- | --- |
| **200** | Batch order creation completed |
| **400** | Bad request - invalid input |
| **401** | Unauthorized - authentication required |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/PortfolioApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#cancel-order)

**cancel\_order**
==========================================================================================

> CancelOrderResponse cancel\_order(order\_id)

Cancel Order Cancel an order

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#example-4)

Example

Copy

Ask AI

    import kalshi_python
    from kalshi_python.models.cancel_order_response import CancelOrderResponse
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
    
    order_id = 'order_id_example' # str | Order ID
    
    try:
        # Cancel Order
        api_response = client.cancel_order(order_id)
        print("The response of PortfolioApi->cancel_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioApi->cancel_order: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#parameters-4)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **order\_id** | **str** | Order ID |     |

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#return-type-4)

Return type

[**CancelOrderResponse**](https://docs.kalshi.com/python-sdk/models/CancelOrderResponse)

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#http-response-details-4)

HTTP response details

| Status code | Description |
| --- | --- |
| **200** | Order cancelled successfully |
| **401** | Unauthorized - authentication required |
| **404** | Resource not found |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/PortfolioApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#create-order)

**create\_order**
==========================================================================================

> CreateOrderResponse create\_order(create\_order\_request)

Create Order Create a new order

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#example-5)

Example

Copy

Ask AI

    import kalshi_python
    from kalshi_python.models.create_order_request import CreateOrderRequest
    from kalshi_python.models.create_order_response import CreateOrderResponse
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
    
    create_order_request = kalshi_python.CreateOrderRequest() # CreateOrderRequest |
    
    try:
        # Create Order
        api_response = client.create_order(create_order_request)
        print("The response of PortfolioApi->create_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioApi->create_order: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#parameters-5)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **create\_order\_request** | [**CreateOrderRequest**](https://docs.kalshi.com/python-sdk/models/CreateOrderRequest) |     |     |

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#return-type-5)

Return type

[**CreateOrderResponse**](https://docs.kalshi.com/python-sdk/models/CreateOrderResponse)

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#http-response-details-5)

HTTP response details

| Status code | Description |
| --- | --- |
| **201** | Order created successfully |
| **400** | Bad request - invalid input |
| **401** | Unauthorized - authentication required |
| **429** | Too Many Requests - rate limit exceeded |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/PortfolioApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#create-order-group)

**create\_order\_group**
=======================================================================================================

> CreateOrderGroupResponse create\_order\_group(create\_order\_group\_request)

Create Order Group Create a new order group

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#example-6)

Example

Copy

Ask AI

    import kalshi_python
    from kalshi_python.models.create_order_group_request import CreateOrderGroupRequest
    from kalshi_python.models.create_order_group_response import CreateOrderGroupResponse
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
    
    create_order_group_request = kalshi_python.CreateOrderGroupRequest() # CreateOrderGroupRequest |
    
    try:
        # Create Order Group
        api_response = client.create_order_group(create_order_group_request)
        print("The response of PortfolioApi->create_order_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioApi->create_order_group: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#parameters-6)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **create\_order\_group\_request** | [**CreateOrderGroupRequest**](https://docs.kalshi.com/python-sdk/models/CreateOrderGroupRequest) |     |     |

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#return-type-6)

Return type

[**CreateOrderGroupResponse**](https://docs.kalshi.com/python-sdk/models/CreateOrderGroupResponse)

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#http-response-details-6)

HTTP response details

| Status code | Description |
| --- | --- |
| **201** | Order group created successfully |
| **400** | Bad request - invalid input |
| **401** | Unauthorized - authentication required |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/PortfolioApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#decrease-order)

**decrease\_order**
==============================================================================================

> DecreaseOrderResponse decrease\_order(order\_id, decrease\_order\_request)

Decrease Order Decrease the size of an existing order

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#example-7)

Example

Copy

Ask AI

    import kalshi_python
    from kalshi_python.models.decrease_order_request import DecreaseOrderRequest
    from kalshi_python.models.decrease_order_response import DecreaseOrderResponse
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
    
    order_id = 'order_id_example' # str | Order ID
    
    decrease_order_request = kalshi_python.DecreaseOrderRequest() # DecreaseOrderRequest |
    
    try:
        # Decrease Order
        api_response = client.decrease_order(order_id, decrease_order_request)
        print("The response of PortfolioApi->decrease_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioApi->decrease_order: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#parameters-7)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **order\_id** | **str** | Order ID |     |
| **decrease\_order\_request** | [**DecreaseOrderRequest**](https://docs.kalshi.com/python-sdk/models/DecreaseOrderRequest) |     |     |

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#return-type-7)

Return type

[**DecreaseOrderResponse**](https://docs.kalshi.com/python-sdk/models/DecreaseOrderResponse)

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#http-response-details-7)

HTTP response details

| Status code | Description |
| --- | --- |
| **200** | Order decreased successfully |
| **400** | Bad request - invalid input |
| **401** | Unauthorized - authentication required |
| **404** | Resource not found |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/PortfolioApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#delete-order-group)

**delete\_order\_group**
=======================================================================================================

> delete\_order\_group(order\_group\_id)

Delete Order Group Delete an order group

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#example-8)

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
    
    order_group_id = 'order_group_id_example' # str | Order group ID
    
    try:
        # Delete Order Group
        client.delete_order_group(order_group_id)
    except Exception as e:
        print("Exception when calling PortfolioApi->delete_order_group: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#parameters-8)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **order\_group\_id** | **str** | Order group ID |     |

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#return-type-8)

Return type

void (empty response body)

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#http-response-details-8)

HTTP response details

| Status code | Description |
| --- | --- |
| **204** | Order group deleted successfully |
| **401** | Unauthorized - authentication required |
| **404** | Resource not found |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/PortfolioApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#get-balance)

**get\_balance**
========================================================================================

> GetBalanceResponse get\_balance()

Get Balance Get the user’s current balance

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#example-9)

Example

Copy

Ask AI

    import kalshi_python
    from kalshi_python.models.get_balance_response import GetBalanceResponse
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
        # Get Balance
        api_response = client.get_balance()
        print("The response of PortfolioApi->get_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioApi->get_balance: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#parameters-9)

Parameters

This endpoint does not need any parameter.

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#return-type-9)

Return type

[**GetBalanceResponse**](https://docs.kalshi.com/python-sdk/models/GetBalanceResponse)

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#http-response-details-9)

HTTP response details

| Status code | Description |
| --- | --- |
| **200** | Balance retrieved successfully |
| **401** | Unauthorized - authentication required |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/PortfolioApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#get-fills)

**get\_fills**
====================================================================================

> GetFillsResponse get\_fills(ticker=ticker, order\_id=order\_id, min\_ts=min\_ts, max\_ts=max\_ts, limit=limit, cursor=cursor)

Get Fills Get fills for the logged-in user. A fill represents a partial or complete execution of an order. When an order matches with another order in the orderbook, a fill is created for each side of the trade.

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#example-10)

Example

Copy

Ask AI

    import kalshi_python
    from kalshi_python.models.get_fills_response import GetFillsResponse
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
    
    ticker = 'ticker_example' # str | Filter by market ticker (optional)
    
    order_id = 'order_id_example' # str | Filter by order ID (optional)
    
    min_ts = 56 # int | Filter items after this Unix timestamp (optional)
    
    max_ts = 56 # int | Filter items before this Unix timestamp (optional)
    
    limit = 100 # int | Number of results per page. Defaults to 100. Maximum value is 200. (optional) (default to 100)
    
    cursor = 'cursor_example' # str | Pagination cursor. Use the cursor value returned from the previous response to get the next page of results. Leave empty for the first page. (optional)
    
    try:
        # Get Fills
        api_response = client.get_fills(ticker=ticker, order_id=order_id, min_ts=min_ts, max_ts=max_ts, limit=limit, cursor=cursor)
        print("The response of PortfolioApi->get_fills:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioApi->get_fills: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#parameters-10)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **ticker** | **str** | Filter by market ticker | \[optional\] |
| **order\_id** | **str** | Filter by order ID | \[optional\] |
| **min\_ts** | **int** | Filter items after this Unix timestamp | \[optional\] |
| **max\_ts** | **int** | Filter items before this Unix timestamp | \[optional\] |
| **limit** | **int** | Number of results per page. Defaults to 100. Maximum value is 200. | \[optional\] \[default to 100\] |
| **cursor** | **str** | Pagination cursor. Use the cursor value returned from the previous response to get the next page of results. Leave empty for the first page. | \[optional\] |

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#return-type-10)

Return type

[**GetFillsResponse**](https://docs.kalshi.com/python-sdk/models/GetFillsResponse)

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#http-response-details-10)

HTTP response details

| Status code | Description |
| --- | --- |
| **200** | Fills retrieved successfully |
| **400** | Bad request - invalid input |
| **401** | Unauthorized - authentication required |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/PortfolioApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#get-order)

**get\_order**
====================================================================================

> GetOrderResponse get\_order(order\_id)

Get Order Get a single order by ID

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#example-11)

Example

Copy

Ask AI

    import kalshi_python
    from kalshi_python.models.get_order_response import GetOrderResponse
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
    
    order_id = 'order_id_example' # str | Order ID
    
    try:
        # Get Order
        api_response = client.get_order(order_id)
        print("The response of PortfolioApi->get_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioApi->get_order: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#parameters-11)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **order\_id** | **str** | Order ID |     |

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#return-type-11)

Return type

[**GetOrderResponse**](https://docs.kalshi.com/python-sdk/models/GetOrderResponse)

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#http-response-details-11)

HTTP response details

| Status code | Description |
| --- | --- |
| **200** | Order retrieved successfully |
| **401** | Unauthorized - authentication required |
| **404** | Resource not found |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/PortfolioApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#get-order-group)

**get\_order\_group**
=================================================================================================

> GetOrderGroupResponse get\_order\_group(order\_group\_id)

Get Order Group Get details of a specific order group

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#example-12)

Example

Copy

Ask AI

    import kalshi_python
    from kalshi_python.models.get_order_group_response import GetOrderGroupResponse
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
    
    order_group_id = 'order_group_id_example' # str | Order group ID
    
    try:
        # Get Order Group
        api_response = client.get_order_group(order_group_id)
        print("The response of PortfolioApi->get_order_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioApi->get_order_group: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#parameters-12)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **order\_group\_id** | **str** | Order group ID |     |

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#return-type-12)

Return type

[**GetOrderGroupResponse**](https://docs.kalshi.com/python-sdk/models/GetOrderGroupResponse)

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#http-response-details-12)

HTTP response details

| Status code | Description |
| --- | --- |
| **200** | Order group retrieved successfully |
| **401** | Unauthorized - authentication required |
| **404** | Resource not found |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/PortfolioApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#get-order-groups)

**get\_order\_groups**
===================================================================================================

> GetOrderGroupsResponse get\_order\_groups(status=status, limit=limit, cursor=cursor)

Get Order Groups Get order groups for the logged-in user

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#example-13)

Example

Copy

Ask AI

    import kalshi_python
    from kalshi_python.models.get_order_groups_response import GetOrderGroupsResponse
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
    
    status = 'status_example' # str | Filter by status. Possible values depend on the endpoint. (optional)
    
    limit = 100 # int | Number of results per page. Defaults to 100. Maximum value is 200. (optional) (default to 100)
    
    cursor = 'cursor_example' # str | Pagination cursor. Use the cursor value returned from the previous response to get the next page of results. Leave empty for the first page. (optional)
    
    try:
        # Get Order Groups
        api_response = client.get_order_groups(status=status, limit=limit, cursor=cursor)
        print("The response of PortfolioApi->get_order_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioApi->get_order_groups: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#parameters-13)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **status** | **str** | Filter by status. Possible values depend on the endpoint. | \[optional\] |
| **limit** | **int** | Number of results per page. Defaults to 100. Maximum value is 200. | \[optional\] \[default to 100\] |
| **cursor** | **str** | Pagination cursor. Use the cursor value returned from the previous response to get the next page of results. Leave empty for the first page. | \[optional\] |

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#return-type-13)

Return type

[**GetOrderGroupsResponse**](https://docs.kalshi.com/python-sdk/models/GetOrderGroupsResponse)

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#http-response-details-13)

HTTP response details

| Status code | Description |
| --- | --- |
| **200** | Order groups retrieved successfully |
| **400** | Bad request - invalid input |
| **401** | Unauthorized - authentication required |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/PortfolioApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#get-order-queue-position)

**get\_order\_queue\_position**
====================================================================================================================

> GetOrderQueuePositionResponse get\_order\_queue\_position(order\_id)

Get Order Queue Position Get the queue position for an order

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#example-14)

Example

Copy

Ask AI

    import kalshi_python
    from kalshi_python.models.get_order_queue_position_response import GetOrderQueuePositionResponse
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
    
    order_id = 'order_id_example' # str | Order ID
    
    try:
        # Get Order Queue Position
        api_response = client.get_order_queue_position(order_id)
        print("The response of PortfolioApi->get_order_queue_position:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioApi->get_order_queue_position: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#parameters-14)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **order\_id** | **str** | Order ID |     |

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#return-type-14)

Return type

[**GetOrderQueuePositionResponse**](https://docs.kalshi.com/python-sdk/models/GetOrderQueuePositionResponse)

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#http-response-details-14)

HTTP response details

| Status code | Description |
| --- | --- |
| **200** | Queue position retrieved successfully |
| **401** | Unauthorized - authentication required |
| **404** | Resource not found |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/PortfolioApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#get-orders)

**get\_orders**
======================================================================================

> GetOrdersResponse get\_orders(ticker=ticker, event\_ticker=event\_ticker, min\_ts=min\_ts, max\_ts=max\_ts, status=status, limit=limit, cursor=cursor)

Get Orders Get orders for the logged-in user

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#example-15)

Example

Copy

Ask AI

    import kalshi_python
    from kalshi_python.models.get_orders_response import GetOrdersResponse
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
    
    ticker = 'ticker_example' # str | Filter by market ticker (optional)
    
    event_ticker = 'event_ticker_example' # str | Filter by event ticker (optional)
    
    min_ts = 56 # int | Filter items after this Unix timestamp (optional)
    
    max_ts = 56 # int | Filter items before this Unix timestamp (optional)
    
    status = 'status_example' # str | Filter by status. Possible values depend on the endpoint. (optional)
    
    limit = 100 # int | Number of results per page. Defaults to 100. Maximum value is 200. (optional) (default to 100)
    
    cursor = 'cursor_example' # str | Pagination cursor. Use the cursor value returned from the previous response to get the next page of results. Leave empty for the first page. (optional)
    
    try:
        # Get Orders
        api_response = client.get_orders(ticker=ticker, event_ticker=event_ticker, min_ts=min_ts, max_ts=max_ts, status=status, limit=limit, cursor=cursor)
        print("The response of PortfolioApi->get_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioApi->get_orders: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#parameters-15)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **ticker** | **str** | Filter by market ticker | \[optional\] |
| **event\_ticker** | **str** | Filter by event ticker | \[optional\] |
| **min\_ts** | **int** | Filter items after this Unix timestamp | \[optional\] |
| **max\_ts** | **int** | Filter items before this Unix timestamp | \[optional\] |
| **status** | **str** | Filter by status. Possible values depend on the endpoint. | \[optional\] |
| **limit** | **int** | Number of results per page. Defaults to 100. Maximum value is 200. | \[optional\] \[default to 100\] |
| **cursor** | **str** | Pagination cursor. Use the cursor value returned from the previous response to get the next page of results. Leave empty for the first page. | \[optional\] |

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#return-type-15)

Return type

[**GetOrdersResponse**](https://docs.kalshi.com/python-sdk/models/GetOrdersResponse)

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#http-response-details-15)

HTTP response details

| Status code | Description |
| --- | --- |
| **200** | Orders retrieved successfully |
| **400** | Bad request - invalid input |
| **401** | Unauthorized - authentication required |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/PortfolioApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#get-positions)

**get\_positions**
============================================================================================

> GetPositionsResponse get\_positions(ticker=ticker, event\_ticker=event\_ticker, count\_down=count\_down, count\_up=count\_up, limit=limit, cursor=cursor)

Get Positions Get positions for the logged-in user

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#example-16)

Example

Copy

Ask AI

    import kalshi_python
    from kalshi_python.models.get_positions_response import GetPositionsResponse
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
    
    ticker = 'ticker_example' # str | Filter by market ticker (optional)
    
    event_ticker = 'event_ticker_example' # str | Filter by event ticker (optional)
    
    count_down = 56 # int | Filter positions by minimum count down value (optional)
    
    count_up = 56 # int | Filter positions by minimum count up value (optional)
    
    limit = 100 # int | Number of results per page. Defaults to 100. Maximum value is 200. (optional) (default to 100)
    
    cursor = 'cursor_example' # str | Pagination cursor. Use the cursor value returned from the previous response to get the next page of results. Leave empty for the first page. (optional)
    
    try:
        # Get Positions
        api_response = client.get_positions(ticker=ticker, event_ticker=event_ticker, count_down=count_down, count_up=count_up, limit=limit, cursor=cursor)
        print("The response of PortfolioApi->get_positions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioApi->get_positions: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#parameters-16)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **ticker** | **str** | Filter by market ticker | \[optional\] |
| **event\_ticker** | **str** | Filter by event ticker | \[optional\] |
| **count\_down** | **int** | Filter positions by minimum count down value | \[optional\] |
| **count\_up** | **int** | Filter positions by minimum count up value | \[optional\] |
| **limit** | **int** | Number of results per page. Defaults to 100. Maximum value is 200. | \[optional\] \[default to 100\] |
| **cursor** | **str** | Pagination cursor. Use the cursor value returned from the previous response to get the next page of results. Leave empty for the first page. | \[optional\] |

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#return-type-16)

Return type

[**GetPositionsResponse**](https://docs.kalshi.com/python-sdk/models/GetPositionsResponse)

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#http-response-details-16)

HTTP response details

| Status code | Description |
| --- | --- |
| **200** | Positions retrieved successfully |
| **400** | Bad request - invalid input |
| **401** | Unauthorized - authentication required |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/PortfolioApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#get-queue-positions)

**get\_queue\_positions**
=========================================================================================================

> GetQueuePositionsResponse get\_queue\_positions(get\_queue\_positions\_request)

Get Queue Positions Get queue positions for multiple orders

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#example-17)

Example

Copy

Ask AI

    import kalshi_python
    from kalshi_python.models.get_queue_positions_request import GetQueuePositionsRequest
    from kalshi_python.models.get_queue_positions_response import GetQueuePositionsResponse
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
    
    get_queue_positions_request = kalshi_python.GetQueuePositionsRequest() # GetQueuePositionsRequest |
    
    try:
        # Get Queue Positions
        api_response = client.get_queue_positions(get_queue_positions_request)
        print("The response of PortfolioApi->get_queue_positions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioApi->get_queue_positions: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#parameters-17)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **get\_queue\_positions\_request** | [**GetQueuePositionsRequest**](https://docs.kalshi.com/python-sdk/models/GetQueuePositionsRequest) |     |     |

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#return-type-17)

Return type

[**GetQueuePositionsResponse**](https://docs.kalshi.com/python-sdk/models/GetQueuePositionsResponse)

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#http-response-details-17)

HTTP response details

| Status code | Description |
| --- | --- |
| **200** | Queue positions retrieved successfully |
| **400** | Bad request - invalid input |
| **401** | Unauthorized - authentication required |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/PortfolioApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#get-settlements)

**get\_settlements**
================================================================================================

> GetSettlementsResponse get\_settlements(limit=limit, cursor=cursor)

Get Settlements Get settlements for the logged-in user

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#example-18)

Example

Copy

Ask AI

    import kalshi_python
    from kalshi_python.models.get_settlements_response import GetSettlementsResponse
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
    
    limit = 100 # int | Number of results per page. Defaults to 100. Maximum value is 200. (optional) (default to 100)
    
    cursor = 'cursor_example' # str | Pagination cursor. Use the cursor value returned from the previous response to get the next page of results. Leave empty for the first page. (optional)
    
    try:
        # Get Settlements
        api_response = client.get_settlements(limit=limit, cursor=cursor)
        print("The response of PortfolioApi->get_settlements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioApi->get_settlements: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#parameters-18)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **limit** | **int** | Number of results per page. Defaults to 100. Maximum value is 200. | \[optional\] \[default to 100\] |
| **cursor** | **str** | Pagination cursor. Use the cursor value returned from the previous response to get the next page of results. Leave empty for the first page. | \[optional\] |

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#return-type-18)

Return type

[**GetSettlementsResponse**](https://docs.kalshi.com/python-sdk/models/GetSettlementsResponse)

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#http-response-details-18)

HTTP response details

| Status code | Description |
| --- | --- |
| **200** | Settlements retrieved successfully |
| **400** | Bad request - invalid input |
| **401** | Unauthorized - authentication required |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/PortfolioApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#get-total-resting-order-value)

**get\_total\_resting\_order\_value**
===============================================================================================================================

> GetTotalRestingOrderValueResponse get\_total\_resting\_order\_value()

Get Total Resting Order Value Get the total value of all resting orders

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#example-19)

Example

Copy

Ask AI

    import kalshi_python
    from kalshi_python.models.get_total_resting_order_value_response import GetTotalRestingOrderValueResponse
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
        # Get Total Resting Order Value
        api_response = client.get_total_resting_order_value()
        print("The response of PortfolioApi->get_total_resting_order_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortfolioApi->get_total_resting_order_value: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#parameters-19)

Parameters

This endpoint does not need any parameter.

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#return-type-19)

Return type

[**GetTotalRestingOrderValueResponse**](https://docs.kalshi.com/python-sdk/models/GetTotalRestingOrderValueResponse)

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#http-response-details-19)

HTTP response details

| Status code | Description |
| --- | --- |
| **200** | Total resting order value retrieved successfully |
| **401** | Unauthorized - authentication required |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/PortfolioApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#reset-order-group)

**reset\_order\_group**
=====================================================================================================

> reset\_order\_group(order\_group\_id)

Reset Order Group Reset an order group

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#example-20)

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
    
    order_group_id = 'order_group_id_example' # str | Order group ID
    
    try:
        # Reset Order Group
        client.reset_order_group(order_group_id)
    except Exception as e:
        print("Exception when calling PortfolioApi->reset_order_group: %s\n" % e)
    

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#parameters-20)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **order\_group\_id** | **str** | Order group ID |     |

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#return-type-20)

Return type

void (empty response body)

### 

[​](https://docs.kalshi.com/python-sdk/api/PortfolioApi#http-response-details-20)

HTTP response details

| Status code | Description |
| --- | --- |
| **204** | Order group reset successfully |
| **401** | Unauthorized - authentication required |
| **404** | Resource not found |
| **500** | Internal server error |

[\[Back to top\]](https://docs.kalshi.com/python-sdk/api/PortfolioApi#)
 [\[Back to API list\]](https://docs.kalshi.com/python-sdk/api)
 [\[Back to Model list\]](https://docs.kalshi.com/python-sdk/models)
 [\[Back to README\]](https://docs.kalshi.com/python-sdk)

[Python SDK Quick Start](https://docs.kalshi.com/sdks/python/quickstart)
[Markets](https://docs.kalshi.com/python-sdk/api/MarketsApi)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.