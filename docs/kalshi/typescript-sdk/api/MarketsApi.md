---
url: https://docs.kalshi.com/typescript-sdk/api/MarketsApi
title: Markets - API Documentation
description: TypeScript SDK methods for Markets operations
scraped_at: 2025-11-03T14:46:47.620185
---

[Skip to main content](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

API Classes

Markets

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

On this page

*   [getMarket](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#getmarket)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#example)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#parameters)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#return-type)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#authorization)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#http-request-headers)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#http-response-details)
    
*   [getMarketCandlesticks](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#getmarketcandlesticks)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#example-2)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#parameters-2)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#return-type-2)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#authorization-2)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#http-request-headers-2)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#http-response-details-2)
    
*   [getMarketOrderbook](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#getmarketorderbook)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#example-3)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#parameters-3)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#return-type-3)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#authorization-3)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#http-request-headers-3)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#http-response-details-3)
    
*   [getMarkets](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#getmarkets)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#example-4)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#parameters-4)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#return-type-4)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#authorization-4)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#http-request-headers-4)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#http-response-details-4)
    
*   [getTrades](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#gettrades)
    
*   [Example](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#example-5)
    
*   [Parameters](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#parameters-5)
    
*   [Return type](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#return-type-5)
    
*   [Authorization](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#authorization-5)
    
*   [HTTP request headers](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#http-request-headers-5)
    
*   [HTTP response details](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#http-response-details-5)
    

All URIs are relative to _[https://api.elections.kalshi.com/trade-api/v2](https://api.elections.kalshi.com/trade-api/v2)
_

| Method | HTTP request | Description |
| --- | --- | --- |
| [**getMarket**](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#getmarket) | **GET** /markets/ | Get Market |
| [**getMarketCandlesticks**](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#getmarketcandlesticks) | **GET** /series//markets//candlesticks | Get Market Candlesticks |
| [**getMarketOrderbook**](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#getmarketorderbook) | **GET** /markets//orderbook | Get Market Orderbook |
| [**getMarkets**](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#getmarkets) | **GET** /markets | Get Markets |
| [**getTrades**](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#gettrades) | **GET** /markets/trades | Get Trades |

[​](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#getmarket)

**getMarket**
=====================================================================================

> GetMarketResponse getMarket()

Get a single market by its ticker. A market represents a specific binary outcome within an event that users can trade on (e.g., “Will candidate X win?”). Markets have yes/no positions, current prices, volume, and settlement rules.

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#example)

Example

Copy

Ask AI

    import {
        MarketsApi,
        Configuration
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new MarketsApi(configuration);
    
    let ticker: string; //Market ticker (default to undefined)
    
    const { status, data } = await apiInstance.getMarket(
        ticker
    );
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#parameters)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **ticker** | \[**string**\] | Market ticker | defaults to undefined |

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#return-type)

Return type

**GetMarketResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#authorization)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#http-request-headers)

HTTP request headers

*   **Content-Type**: Not defined
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#http-response-details)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **200** | Market retrieved successfully | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **404** | Resource not found | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[​](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#getmarketcandlesticks)

**getMarketCandlesticks**
=============================================================================================================

> GetMarketCandlesticksResponse getMarketCandlesticks()

Get candlestick data for a market within a series

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#example-2)

Example

Copy

Ask AI

    import {
        MarketsApi,
        Configuration
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new MarketsApi(configuration);
    
    let ticker: string; //The series ticker (default to undefined)
    let marketTicker: string; //The market ticker (default to undefined)
    let startTs: number; //Start timestamp for the range (optional) (default to undefined)
    let endTs: number; //End timestamp for the range (optional) (default to undefined)
    let periodInterval: string; //Period interval for candlesticks (e.g., 1m, 5m, 1h, 1d) (optional) (default to undefined)
    
    const { status, data } = await apiInstance.getMarketCandlesticks(
        ticker,
        marketTicker,
        startTs,
        endTs,
        periodInterval
    );
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#parameters-2)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **ticker** | \[**string**\] | The series ticker | defaults to undefined |
| **marketTicker** | \[**string**\] | The market ticker | defaults to undefined |
| **startTs** | \[**number**\] | Start timestamp for the range | (optional) defaults to undefined |
| **endTs** | \[**number**\] | End timestamp for the range | (optional) defaults to undefined |
| **periodInterval** | \[**string**\] | Period interval for candlesticks (e.g., 1m, 5m, 1h, 1d) | (optional) defaults to undefined |

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#return-type-2)

Return type

**GetMarketCandlesticksResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#authorization-2)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#http-request-headers-2)

HTTP request headers

*   **Content-Type**: Not defined
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#http-response-details-2)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **200** | Candlesticks retrieved successfully | \-  |
| **400** | Bad request - invalid input | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **404** | Resource not found | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[​](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#getmarketorderbook)

**getMarketOrderbook**
=======================================================================================================

> GetMarketOrderbookResponse getMarketOrderbook()

Get the orderbook for a market

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#example-3)

Example

Copy

Ask AI

    import {
        MarketsApi,
        Configuration
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new MarketsApi(configuration);
    
    let ticker: string; //Market ticker (default to undefined)
    let depth: number; //Depth of the orderbook to retrieve (optional) (default to 10)
    
    const { status, data } = await apiInstance.getMarketOrderbook(
        ticker,
        depth
    );
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#parameters-3)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **ticker** | \[**string**\] | Market ticker | defaults to undefined |
| **depth** | \[**number**\] | Depth of the orderbook to retrieve | (optional) defaults to 10 |

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#return-type-3)

Return type

**GetMarketOrderbookResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#authorization-3)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#http-request-headers-3)

HTTP request headers

*   **Content-Type**: Not defined
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#http-response-details-3)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **200** | Orderbook retrieved successfully | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **404** | Resource not found | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[​](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#getmarkets)

**getMarkets**
=======================================================================================

> GetMarketsResponse getMarkets()

List and discover markets on Kalshi. A market represents a specific binary outcome within an event that users can trade on (e.g., “Will candidate X win?”). Markets have yes/no positions, current prices, volume, and settlement rules. This endpoint returns a paginated response. Use the ‘limit’ parameter to control page size (1-1000, defaults to 100). The response includes a ‘cursor’ field - pass this value in the ‘cursor’ parameter of your next request to get the next page. An empty cursor indicates no more pages are available.

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#example-4)

Example

Copy

Ask AI

    import {
        MarketsApi,
        Configuration
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new MarketsApi(configuration);
    
    let limit: number; //Number of results per page. Defaults to 100. Maximum value is 1000. (optional) (default to 100)
    let cursor: string; //Pagination cursor. Use the cursor value returned from the previous response to get the next page of results. Leave empty for the first page. (optional) (default to undefined)
    let eventTicker: string; //Filter by event ticker (optional) (default to undefined)
    let seriesTicker: string; //Filter by series ticker (optional) (default to undefined)
    let maxCloseTs: number; //Filter items that close before this Unix timestamp (optional) (default to undefined)
    let minCloseTs: number; //Filter items that close after this Unix timestamp (optional) (default to undefined)
    let status: string; //Filter by market status. Comma-separated list. Possible values are \'initialized\', \'open\', \'closed\', \'settled\', \'determined\'. Note that the API accepts \'open\' for filtering but returns \'active\' in the response. Leave empty to return markets with any status. (optional) (default to undefined)
    let tickers: string; //Filter by specific market tickers. Comma-separated list of market tickers to retrieve. (optional) (default to undefined)
    
    const { status, data } = await apiInstance.getMarkets(
        limit,
        cursor,
        eventTicker,
        seriesTicker,
        maxCloseTs,
        minCloseTs,
        status,
        tickers
    );
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#parameters-4)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **limit** | \[**number**\] | Number of results per page. Defaults to 100. Maximum value is 1000. | (optional) defaults to 100 |
| **cursor** | \[**string**\] | Pagination cursor. Use the cursor value returned from the previous response to get the next page of results. Leave empty for the first page. | (optional) defaults to undefined |
| **eventTicker** | \[**string**\] | Filter by event ticker | (optional) defaults to undefined |
| **seriesTicker** | \[**string**\] | Filter by series ticker | (optional) defaults to undefined |
| **maxCloseTs** | \[**number**\] | Filter items that close before this Unix timestamp | (optional) defaults to undefined |
| **minCloseTs** | \[**number**\] | Filter items that close after this Unix timestamp | (optional) defaults to undefined |
| **status** | \[**string**\] | Filter by market status. Comma-separated list. Possible values are &#39;initialized&#39;, &#39;open&#39;, &#39;closed&#39;, &#39;settled&#39;, &#39;determined&#39;. Note that the API accepts &#39;open&#39; for filtering but returns &#39;active&#39; in the response. Leave empty to return markets with any status. | (optional) defaults to undefined |
| **tickers** | \[**string**\] | Filter by specific market tickers. Comma-separated list of market tickers to retrieve. | (optional) defaults to undefined |

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#return-type-4)

Return type

**GetMarketsResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#authorization-4)

Authorization

[bearerAuth](https://docs.kalshi.com/typescript-sdk/README.md#bearerAuth)

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#http-request-headers-4)

HTTP request headers

*   **Content-Type**: Not defined
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#http-response-details-4)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **200** | Markets retrieved successfully | \-  |
| **400** | Bad request - invalid input | \-  |
| **401** | Unauthorized - authentication required | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[​](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#gettrades)

**getTrades**
=====================================================================================

> GetTradesResponse getTrades()

Get all trades for all markets. A trade represents a completed transaction between two users on a specific market. Each trade includes the market ticker, price, quantity, and timestamp information. This endpoint returns a paginated response. Use the ‘limit’ parameter to control page size (1-1000, defaults to 100). The response includes a ‘cursor’ field - pass this value in the ‘cursor’ parameter of your next request to get the next page. An empty cursor indicates no more pages are available.

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#example-5)

Example

Copy

Ask AI

    import {
        MarketsApi,
        Configuration
    } from 'kalshi-typescript';
    
    const configuration = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: '/path/to/private-key.pem'  // or privateKeyPem: 'PEM string'
    });
    const apiInstance = new MarketsApi(configuration);
    
    let limit: number; //Number of results per page. Defaults to 100. Maximum value is 1000. (optional) (default to 100)
    let cursor: string; //Pagination cursor. Use the cursor value returned from the previous response to get the next page of results. Leave empty for the first page. (optional) (default to undefined)
    let ticker: string; //Filter by market ticker (optional) (default to undefined)
    let minTs: number; //Filter items after this Unix timestamp (optional) (default to undefined)
    let maxTs: number; //Filter items before this Unix timestamp (optional) (default to undefined)
    
    const { status, data } = await apiInstance.getTrades(
        limit,
        cursor,
        ticker,
        minTs,
        maxTs
    );
    

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#parameters-5)

Parameters

| Name | Type | Description | Notes |
| --- | --- | --- | --- |
| **limit** | \[**number**\] | Number of results per page. Defaults to 100. Maximum value is 1000. | (optional) defaults to 100 |
| **cursor** | \[**string**\] | Pagination cursor. Use the cursor value returned from the previous response to get the next page of results. Leave empty for the first page. | (optional) defaults to undefined |
| **ticker** | \[**string**\] | Filter by market ticker | (optional) defaults to undefined |
| **minTs** | \[**number**\] | Filter items after this Unix timestamp | (optional) defaults to undefined |
| **maxTs** | \[**number**\] | Filter items before this Unix timestamp | (optional) defaults to undefined |

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#return-type-5)

Return type

**GetTradesResponse**

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#authorization-5)

Authorization

No authorization required

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#http-request-headers-5)

HTTP request headers

*   **Content-Type**: Not defined
*   **Accept**: application/json

### 

[​](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#http-response-details-5)

HTTP response details

| Status code | Description | Response headers |
| --- | --- | --- |
| **200** | Trades retrieved successfully | \-  |
| **400** | Bad request - invalid input | \-  |
| **500** | Internal server error | \-  |

[\[Back to top\]](https://docs.kalshi.com/typescript-sdk/api/MarketsApi#)
 [\[Back to API list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-api-endpoints)
 [\[Back to Model list\]](https://docs.kalshi.com/typescript-sdk/README.md#documentation-for-models)
 [\[Back to README\]](https://docs.kalshi.com/typescript-sdk/README.md)

[Portfolio](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi)
[Communications](https://docs.kalshi.com/typescript-sdk/api/CommunicationsApi)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.