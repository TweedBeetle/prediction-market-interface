---
url: https://docs.kalshi.com/getting_started/pagination
title: Understanding Pagination - API Documentation
description: Learn how to navigate through large datasets using cursor-based pagination
scraped_at: 2025-11-03T14:46:36.786677
---

[Skip to main content](https://docs.kalshi.com/getting_started/pagination#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

Understanding Pagination

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

On this page

*   [How Pagination Works](https://docs.kalshi.com/getting_started/pagination#how-pagination-works)
    
*   [Using Cursors](https://docs.kalshi.com/getting_started/pagination#using-cursors)
    
*   [Example: Paginating Through Markets](https://docs.kalshi.com/getting_started/pagination#example%3A-paginating-through-markets)
    
*   [Pagination Parameters](https://docs.kalshi.com/getting_started/pagination#pagination-parameters)
    
*   [Best Practices](https://docs.kalshi.com/getting_started/pagination#best-practices)
    
*   [Endpoints Supporting Pagination](https://docs.kalshi.com/getting_started/pagination#endpoints-supporting-pagination)
    
*   [Common Patterns](https://docs.kalshi.com/getting_started/pagination#common-patterns)
    
*   [Fetching Recent Items](https://docs.kalshi.com/getting_started/pagination#fetching-recent-items)
    
*   [Filtering While Paginating](https://docs.kalshi.com/getting_started/pagination#filtering-while-paginating)
    
*   [Detecting New Items](https://docs.kalshi.com/getting_started/pagination#detecting-new-items)
    
*   [Next Steps](https://docs.kalshi.com/getting_started/pagination#next-steps)
    

The Kalshi API uses cursor-based pagination to help you efficiently navigate through large datasets. This guide explains how pagination works and provides examples for handling paginated responses.

[​](https://docs.kalshi.com/getting_started/pagination#how-pagination-works)

How Pagination Works
----------------------------------------------------------------------------------------------------

When making requests to list endpoints (like `/markets`, `/events`, or `/series`), the API returns results in pages to keep response sizes manageable. Each page contains:

*   **Data array**: The actual items for the current page (markets, events, etc.)
*   **Cursor field**: A token that points to the next page of results
*   **Limit**: The maximum number of items per page (default: 100)

[​](https://docs.kalshi.com/getting_started/pagination#using-cursors)

Using Cursors
--------------------------------------------------------------------------------------

To paginate through results:

1.  Make your initial request without a cursor
2.  Check if the response includes a `cursor` field
3.  If a cursor exists, make another request with `?cursor={cursor_value}`
4.  Continue until the cursor is `null` (no more pages)

[​](https://docs.kalshi.com/getting_started/pagination#example%3A-paginating-through-markets)

Example: Paginating Through Markets
------------------------------------------------------------------------------------------------------------------------------------

Python

JavaScript

Copy

Ask AI

    import requests
    
    def get_all_markets(series_ticker):
        """Fetch all markets for a series, handling pagination"""
        all_markets = []
        cursor = None
        base_url = "https://api.elections.kalshi.com/trade-api/v2/markets"
    
        while True:
            # Build URL with cursor if we have one
            url = f"{base_url}?series_ticker={series_ticker}&limit=100"
            if cursor:
                url += f"&cursor={cursor}"
    
            response = requests.get(url)
            data = response.json()
    
            # Add markets from this page
            all_markets.extend(data['markets'])
    
            # Check if there are more pages
            cursor = data.get('cursor')
            if not cursor:
                break
    
            print(f"Fetched {len(data['markets'])} markets, total: {len(all_markets)}")
    
        return all_markets
    
    # Example usage
    markets = get_all_markets("KXHIGHNY")
    print(f"Total markets found: {len(markets)}")
    

[​](https://docs.kalshi.com/getting_started/pagination#pagination-parameters)

Pagination Parameters
------------------------------------------------------------------------------------------------------

Most list endpoints support these pagination parameters:

*   **`cursor`**: Token from previous response to get the next page
*   **`limit`**: Number of items per page (typically 1-100, default: 100)

[​](https://docs.kalshi.com/getting_started/pagination#best-practices)

Best Practices
----------------------------------------------------------------------------------------

1.  **Handle rate limits**: When paginating through large datasets, be mindful of [rate limits](https://docs.kalshi.com/getting_started/rate_limits)
    
2.  **Set appropriate limits**: Use smaller page sizes if you only need a few items
3.  **Cache results**: Store paginated data locally to avoid repeated API calls
4.  **Check for changes**: Data can change between requests, so consider implementing refresh logic

[​](https://docs.kalshi.com/getting_started/pagination#endpoints-supporting-pagination)

Endpoints Supporting Pagination
--------------------------------------------------------------------------------------------------------------------------

The following endpoints support cursor-based pagination:

*   [Get Markets](https://docs.kalshi.com/api-reference/market/get-markets)
     - `/markets`
*   [Get Events](https://docs.kalshi.com/api-reference/market/get-events)
     - `/events`
*   [Get Series](https://docs.kalshi.com/api-reference/market/get-series)
     - `/series`
*   [Get Trades](https://docs.kalshi.com/api-reference/market/get-trades)
     - `/markets/trades`
*   [Get Portfolio History](https://docs.kalshi.com/api-reference/portfolio/get-portfolio-history)
     - `/portfolio/history`
*   [Get Fills](https://docs.kalshi.com/api-reference/portfolio/get-fills)
     - `/portfolio/fills`
*   [Get Orders](https://docs.kalshi.com/api-reference/portfolio/get-orders)
     - `/portfolio/orders`

[​](https://docs.kalshi.com/getting_started/pagination#common-patterns)

Common Patterns
------------------------------------------------------------------------------------------

### 

[​](https://docs.kalshi.com/getting_started/pagination#fetching-recent-items)

Fetching Recent Items

If you only need recent items, you can limit results without pagination:

Copy

Ask AI

    # Get just the 10 most recent markets
    url = "https://api.elections.kalshi.com/trade-api/v2/markets?limit=10&status=open"
    

### 

[​](https://docs.kalshi.com/getting_started/pagination#filtering-while-paginating)

Filtering While Paginating

You can combine filters with pagination:

Copy

Ask AI

    # Get all open markets for a series
    url = f"{base_url}?series_ticker={ticker}&status=open&limit=100&cursor={cursor}"
    

### 

[​](https://docs.kalshi.com/getting_started/pagination#detecting-new-items)

Detecting New Items

To check for new items since your last fetch:

1.  Store the first item’s ID or timestamp from your previous fetch
2.  Paginate through results until you find that item
3.  Everything before it is new

[​](https://docs.kalshi.com/getting_started/pagination#next-steps)

Next Steps
--------------------------------------------------------------------------------

Now that you understand pagination, you can efficiently work with large datasets in the Kalshi API. For more details on specific endpoints, check the [API Reference](https://docs.kalshi.com/api-reference)
.

[Rate Limits and Tiers](https://docs.kalshi.com/getting_started/rate_limits)
[Orderbook Responses](https://docs.kalshi.com/getting_started/orderbook_responses)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.