---
url: https://docs.polymarket.com/changelog/changelog
title: Polymarket Changelog - Polymarket Documentation
description: Welcome to the Polymarket Changelog. Here you will find any important changes to Polymarket, including but not limited to CLOB, API, UI and Mobile Applications.
scraped_at: 2025-11-03T15:03:55.361064
---

[Skip to main content](https://docs.polymarket.com/changelog/changelog#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

Ctrl K

Search...

Navigation

Main Changes

Polymarket Changelog

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

On this page

*   [Sept 24, 2025](https://docs.polymarket.com/changelog/changelog#sept-24%2C-2025)
    
*   [September 15, 2025](https://docs.polymarket.com/changelog/changelog#september-15%2C-2025)
    
*   [August 26, 2025](https://docs.polymarket.com/changelog/changelog#august-26%2C-2025)
    
*   [August 21, 2025](https://docs.polymarket.com/changelog/changelog#august-21%2C-2025)
    
*   [July 23, 2025](https://docs.polymarket.com/changelog/changelog#july-23%2C-2025)
    
*   [June 3, 2025](https://docs.polymarket.com/changelog/changelog#june-3%2C-2025)
    
*   [June 3, 2025](https://docs.polymarket.com/changelog/changelog#june-3%2C-2025-2)
    
*   [May 28, 2025](https://docs.polymarket.com/changelog/changelog#may-28%2C-2025)
    
*   [May 28, 2025](https://docs.polymarket.com/changelog/changelog#may-28%2C-2025-2)
    
*   [May 15, 2025](https://docs.polymarket.com/changelog/changelog#may-15%2C-2025)
    

[​](https://docs.polymarket.com/changelog/changelog#sept-24%2C-2025)

Sept 24, 2025

Polymarket Real-Time Data Socket (RTDS) official release

*   **Crypto Price Feeds**: Access real-time cryptocurrency prices from two sources (Binance & Chainlink)
*   **Comment Streaming**: Real-time updates for comment events including new comments, replies, and reactions
*   **Dynamic Subscriptions**: Add, remove, and modify subscriptions without reconnecting
*   **TypeScript Client**: Official TypeScript client available at [real-time-data-client](https://github.com/Polymarket/real-time-data-client)
     For complete documentation, see [RTDS Overview](https://docs.polymarket.com/developers/RTDS/RTDS-overview)
    .

[​](https://docs.polymarket.com/changelog/changelog#september-15%2C-2025)

September 15, 2025

WSS price\_change event update

*   There has been a significant change to the structure of the price change message. This update will be applied at 11PM UTC September 15, 2025. We apologize for the short notice
    *   Please see the [migration guide](https://docs.polymarket.com/developers/CLOB/websocket/market-channel-migration-guide)
         for details.

[​](https://docs.polymarket.com/changelog/changelog#august-26%2C-2025)

August 26, 2025

Updated /trades and /activity endpoints

*   Reduced maximum values for query parameters on Data-API /trades and /activity:
    *   `limit`: 500
    *   `offset`: 1,000

[​](https://docs.polymarket.com/changelog/changelog#august-21%2C-2025)

August 21, 2025

Batch Orders Increase

*   The batch orders limit has been increased from from 5 -> 15. Read more about the batch orders functionality [here](https://docs.polymarket.com/developers/CLOB/orders/create-order-batch)
    .

[​](https://docs.polymarket.com/changelog/changelog#july-23%2C-2025)

July 23, 2025

Get Book(s) update

*   We’re adding new fields to the `get-book` and `get-books` CLOB endpoints to include key market metadata that previously required separate queries.
    *   `min_order_size`
        *   type: string
        *   description: Minimum allowed order size.
    *   `neg_risk`
        *   type: boolean
        *   description: Boolean indicating whether the market is neg\_risk.
    *   `tick_size`
        *   type: string
        *   description: Minimum allowed order size.

[​](https://docs.polymarket.com/changelog/changelog#june-3%2C-2025)

June 3, 2025

New Batch Orders Endpoint

*   We’re excited to roll out a highly requested feature: **order batching**. With this new endpoint, users can now submit up to five trades in a single request. To help you get started, we’ve included sample code demonstrating how to use it. Please see [Place Multiple Orders (Batching)](https://docs.polymarket.com/developers/CLOB/orders/create-order-batch)
     for more details.

[​](https://docs.polymarket.com/changelog/changelog#june-3%2C-2025-2)

June 3, 2025

Change to /data/trades

*   We’re adding a new `side` field to the `MakerOrder` portion of the trade object. This field will indicate whether the maker order is a `buy` or `sell`, helping to clarify trade events where the maker side was previously ambiguous. For more details, refer to the MakerOrder object on the [Get Trades](https://docs.polymarket.com/developers/CLOB/trades/trades)
     page.

[​](https://docs.polymarket.com/changelog/changelog#may-28%2C-2025)

May 28, 2025

Websocket Changes

*   The 100 token subscription limit has been removed for the Markets channel. You can now subscribe to as many token IDs as needed for your use case.
*   New Subscribe Field `initial_dump`
    *   Optional field to indicate whether you want to receive the initial order book state when subscribing to a token or list of tokens.
    *   `default: true`

[​](https://docs.polymarket.com/changelog/changelog#may-28%2C-2025-2)

May 28, 2025

New FAK Order Type

We’re excited to introduce a new order type soon to be available to all users: Fill and Kill (FAK). FAK orders behave similarly to the well-known Fill or Kil(FOK) orders, but with a key difference:

*   FAK will fill as many shares as possible immediately at your specified price, and any remaining unfilled portion will be canceled.
*   Unlike FOK, which requires the entire order to fill instantly or be canceled, FAK is more flexible and aims to capture partial fills if possible.

[​](https://docs.polymarket.com/changelog/changelog#may-15%2C-2025)

May 15, 2025

Increased API Rate Limits

All API users will enjoy increased rate limits for the CLOB endpoints.

*   CLOB - /books (website) (300req - 10s / Throttle requests over the maximum configured rate)
*   CLOB - /books (50 req - 10s / Throttle requests over the maximum configured rate)
*   CLOB - /price (100req - 10s / Throttle requests over the maximum configured rate)
*   CLOB markets/0x (50req / 10s - Throttle requests over the maximum configured rate)
*   CLOB POST /order - 500 every 10s (50/s) - (BURST) - Throttle requests over the maximum configured rateed
*   CLOB POST /order - 3000 every 10 minutes (5/s) - Throttle requests over the maximum configured rate
*   CLOB DELETE /order - 500 every 10s (50/s) - (BURST) - Throttle requests over the maximum configured rate
*   DELETE /order - 3000 every 10 minutes (5/s) - Throttle requests over the maximum configured rate

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.