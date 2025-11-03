---
url: https://docs.kalshi.com/getting_started/orderbook_responses
title: Orderbook Responses - API Documentation
description: Understanding Kalshi orderbook structure and binary prediction market mechanics
scraped_at: 2025-11-03T14:46:36.786419
---

[Skip to main content](https://docs.kalshi.com/getting_started/orderbook_responses#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

Orderbook Responses

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

On this page

*   [Getting Orderbook Data](https://docs.kalshi.com/getting_started/orderbook_responses#getting-orderbook-data)
    
*   [Request Format](https://docs.kalshi.com/getting_started/orderbook_responses#request-format)
    
*   [Example Request](https://docs.kalshi.com/getting_started/orderbook_responses#example-request)
    
*   [Response Structure](https://docs.kalshi.com/getting_started/orderbook_responses#response-structure)
    
*   [Example Response](https://docs.kalshi.com/getting_started/orderbook_responses#example-response)
    
*   [Understanding the Arrays](https://docs.kalshi.com/getting_started/orderbook_responses#understanding-the-arrays)
    
*   [Why Only Bids?](https://docs.kalshi.com/getting_started/orderbook_responses#why-only-bids%3F)
    
*   [The Reciprocal Relationship](https://docs.kalshi.com/getting_started/orderbook_responses#the-reciprocal-relationship)
    
*   [Calculating Spreads](https://docs.kalshi.com/getting_started/orderbook_responses#calculating-spreads)
    
*   [Example Calculation](https://docs.kalshi.com/getting_started/orderbook_responses#example-calculation)
    
*   [Working with Orderbook Data](https://docs.kalshi.com/getting_started/orderbook_responses#working-with-orderbook-data)
    
*   [Display Best Prices](https://docs.kalshi.com/getting_started/orderbook_responses#display-best-prices)
    
*   [Calculate Market Depth](https://docs.kalshi.com/getting_started/orderbook_responses#calculate-market-depth)
    
*   [Next Steps](https://docs.kalshi.com/getting_started/orderbook_responses#next-steps)
    

[​](https://docs.kalshi.com/getting_started/orderbook_responses#getting-orderbook-data)

Getting Orderbook Data
-----------------------------------------------------------------------------------------------------------------

The [Get Market Orderbook](https://docs.kalshi.com/api-reference/market/get-market-order-book)
 endpoint returns the current state of bids for a specific market.

### 

[​](https://docs.kalshi.com/getting_started/orderbook_responses#request-format)

Request Format

Copy

Ask AI

    GET /markets/{ticker}/orderbook
    

No authentication is required for this endpoint.

### 

[​](https://docs.kalshi.com/getting_started/orderbook_responses#example-request)

Example Request

Python

JavaScript

cURL

Copy

Ask AI

    import requests
    
    # Get orderbook for a specific market
    market_ticker = "KXHIGHNY-24JAN01-T60"
    url = f"https://api.elections.kalshi.com/trade-api/v2/markets/{market_ticker}/orderbook"
    
    response = requests.get(url)
    orderbook_data = response.json()
    

[​](https://docs.kalshi.com/getting_started/orderbook_responses#response-structure)

Response Structure
---------------------------------------------------------------------------------------------------------

The orderbook response contains two arrays of bids - one for YES positions and one for NO positions. Each bid is represented as a two-element array: `[price, quantity]`.

### 

[​](https://docs.kalshi.com/getting_started/orderbook_responses#example-response)

Example Response

Copy

Ask AI

    {
      "orderbook": {
        "yes": [\
          [1, 200],    // 200 contracts bid at 1¢\
          [15, 100],   // 100 contracts bid at 15¢\
          [20, 50],    // 50 contracts bid at 20¢\
          [25, 20],    // 20 contracts bid at 25¢\
          [30, 11],    // 11 contracts bid at 30¢\
          [31, 10],    // 10 contracts bid at 31¢\
          [32, 10],    // 10 contracts bid at 32¢\
          [33, 11],    // 11 contracts bid at 33¢\
          [34, 9],     // 9 contracts bid at 34¢\
          [35, 11],    // 11 contracts bid at 35¢\
          [41, 10],    // 10 contracts bid at 41¢\
          [42, 13]     // 13 contracts bid at 42¢\
        ],
        "no": [\
          [1, 100],    // 100 contracts bid at 1¢\
          [16, 3],     // 3 contracts bid at 16¢\
          [25, 50],    // 50 contracts bid at 25¢\
          [28, 19],    // 19 contracts bid at 28¢\
          [36, 5],     // 5 contracts bid at 36¢\
          [37, 50],    // 50 contracts bid at 37¢\
          [38, 300],   // 300 contracts bid at 38¢\
          [44, 29],    // 29 contracts bid at 44¢\
          [45, 20],    // 20 contracts bid at 45¢\
          [56, 17]     // 17 contracts bid at 56¢\
        ]
      }
    }
    

### 

[​](https://docs.kalshi.com/getting_started/orderbook_responses#understanding-the-arrays)

Understanding the Arrays

*   **First element**: Price in cents (1-99)
*   **Second element**: Number of contracts available at that price
*   Arrays are sorted by price in **ascending order**
*   The **highest** bid (best bid) is the **last** element in each array

[​](https://docs.kalshi.com/getting_started/orderbook_responses#why-only-bids%3F)

Why Only Bids?
---------------------------------------------------------------------------------------------------

**Important**: Kalshi’s orderbook only returns bids, not asks. This is because in binary prediction markets, there’s a reciprocal relationship between YES and NO positions.

In binary prediction markets, every position has a complementary opposite:

*   A **YES BID** at price X is equivalent to a **NO ASK** at price (100 - X)
*   A **NO BID** at price Y is equivalent to a **YES ASK** at price (100 - Y)

### 

[​](https://docs.kalshi.com/getting_started/orderbook_responses#the-reciprocal-relationship)

The Reciprocal Relationship

Since binary markets must sum to 100¢, these relationships always hold:

| Action | Equivalent To | Why |
| --- | --- | --- |
| YES BID at 60¢ | NO ASK at 40¢ | Willing to pay 60¢ for YES = Willing to receive 40¢ to take NO |
| NO BID at 30¢ | YES ASK at 70¢ | Willing to pay 30¢ for NO = Willing to receive 70¢ to take YES |

This reciprocal nature means that by showing only bids, the orderbook provides complete market information while avoiding redundancy.

[​](https://docs.kalshi.com/getting_started/orderbook_responses#calculating-spreads)

Calculating Spreads
-----------------------------------------------------------------------------------------------------------

To find the bid-ask spread for a market:

1.  **YES spread**:
    *   Best YES bid: Highest price in the `yes` array
    *   Best YES ask: 100 - (Highest price in the `no` array)
    *   Spread = Best YES ask - Best YES bid
2.  **NO spread**:
    *   Best NO bid: Highest price in the `no` array
    *   Best NO ask: 100 - (Highest price in the `yes` array)
    *   Spread = Best NO ask - Best NO bid

### 

[​](https://docs.kalshi.com/getting_started/orderbook_responses#example-calculation)

Example Calculation

Copy

Ask AI

    # Using the example orderbook above
    best_yes_bid = 42  # Highest YES bid (last in array)
    best_yes_ask = 100 - 56  # 100 - highest NO bid = 44
    
    spread = best_yes_ask - best_yes_bid  # 44 - 42 = 2
    
    # The spread is 2¢
    # You can buy YES at 44¢ (implied ask) and sell at 42¢ (bid)
    

[​](https://docs.kalshi.com/getting_started/orderbook_responses#working-with-orderbook-data)

Working with Orderbook Data
---------------------------------------------------------------------------------------------------------------------------

### 

[​](https://docs.kalshi.com/getting_started/orderbook_responses#display-best-prices)

Display Best Prices

Python

JavaScript

Copy

Ask AI

    def display_best_prices(orderbook_data):
        """Display the best bid prices and implied asks"""
        orderbook = orderbook_data['orderbook']
    
        # Best bids (if any exist)
        if orderbook['yes']:
            best_yes_bid = orderbook['yes'][-1][0]  # Last element is highest
            print(f"Best YES Bid: {best_yes_bid}¢")
    
        if orderbook['no']:
            best_no_bid = orderbook['no'][-1][0]  # Last element is highest
            best_yes_ask = 100 - best_no_bid
            print(f"Best YES Ask: {best_yes_ask}¢ (implied from NO bid)")
    
        print()
    
        if orderbook['no']:
            best_no_bid = orderbook['no'][-1][0]  # Last element is highest
            print(f"Best NO Bid: {best_no_bid}¢")
    
        if orderbook['yes']:
            best_yes_bid = orderbook['yes'][-1][0]  # Last element is highest
            best_no_ask = 100 - best_yes_bid
            print(f"Best NO Ask: {best_no_ask}¢ (implied from YES bid)")
    

### 

[​](https://docs.kalshi.com/getting_started/orderbook_responses#calculate-market-depth)

Calculate Market Depth

Copy

Ask AI

    def calculate_depth(orderbook_data, depth_cents=5):
        """Calculate total volume within X cents of best bid"""
        orderbook = orderbook_data['orderbook']
    
        yes_depth = 0
        no_depth = 0
    
        # YES side depth (iterate backwards from best bid)
        if orderbook['yes']:
            best_yes = orderbook['yes'][-1][0]  # Last element is highest
            for price, quantity in reversed(orderbook['yes']):
                if best_yes - price <= depth_cents:
                    yes_depth += quantity
                else:
                    break
    
        # NO side depth (iterate backwards from best bid)
        if orderbook['no']:
            best_no = orderbook['no'][-1][0]  # Last element is highest
            for price, quantity in reversed(orderbook['no']):
                if best_no - price <= depth_cents:
                    no_depth += quantity
                else:
                    break
    
        return {"yes_depth": yes_depth, "no_depth": no_depth}
    

[​](https://docs.kalshi.com/getting_started/orderbook_responses#next-steps)

Next Steps
-----------------------------------------------------------------------------------------

*   Learn about [making authenticated requests](https://docs.kalshi.com/getting_started/api_keys)
     to place orders
*   Explore [WebSocket connections](https://docs.kalshi.com/websockets/orderbook-updates)
     for real-time orderbook updates
*   Read about [market mechanics](https://kalshi.com/learn)
     on the Kalshi website

[Understanding Pagination](https://docs.kalshi.com/getting_started/pagination)
[Subpenny Pricing](https://docs.kalshi.com/getting_started/subpenny_pricing)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.