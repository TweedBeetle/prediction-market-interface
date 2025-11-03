---
url: https://docs.kalshi.com/getting_started/rate_limits
title: Rate Limits and Tiers - API Documentation
description: Understanding API rate limits and access tiers
scraped_at: 2025-11-03T14:46:38.069627
---

[Skip to main content](https://docs.kalshi.com/getting_started/rate_limits#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

Rate Limits and Tiers

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

On this page

*   [Access tiers](https://docs.kalshi.com/getting_started/rate_limits#access-tiers)
    

[​](https://docs.kalshi.com/getting_started/rate_limits#access-tiers)

Access tiers
-------------------------------------------------------------------------------------

| Tier | Read | Write |
| --- | --- | --- |
| Basic | 20 per second | 10 per second |
| Advanced | 30 per second | 30 per second |
| Premier | 100 per second | 100 per second |
| Prime | 400 per second | 400 per second |

Qualification for tiers:

*   Basic: Completing signup
*   Advanced: Completing [https://kalshi.typeform.com/advanced-api](https://kalshi.typeform.com/advanced-api)
    
*   Premier: 3.75% of exchange traded volume in a given month
*   Prime: 7.5% of exchange traded volume in a given month

In addition to the volume targets, technical competency is a requirement for Premier/Prime access. Before providing access to the Premier/Prime tiers, the Exchange will establish that the trader/trading entity has the following requirements met:

*   Knowledge of common security practices for API usage
*   Proficiency in setting up monitoring for API usage, and ability to monitor API usage in near real-time
*   Understanding and implementation of rate limiting and throttling mechanisms imposed by the API, and the ability to self-limit load
*   Awareness of legal and compliance aspects related to API usage

Only the following APIs fall under the write limit, for the batch APIs, each item in the batch is considered 1 transaction with the sole exception of BatchCancelOrders, where each cancel counts as 0.2 transactions:

*   [BatchCreateOrders](https://docs.kalshi.com/api-reference/portfolio/batch-create-orders)
    
*   [BatchCancelOrders](https://docs.kalshi.com/api-reference/portfolio/batch-cancel-orders)
    
*   [CreateOrder](https://docs.kalshi.com/api-reference/portfolio/create-order)
    
*   [CancelOrder](https://docs.kalshi.com/api-reference/portfolio/cancel-order)
    
*   [AmendOrder](https://docs.kalshi.com/api-reference/portfolio/amend-order)
    
*   [DecreaseOrder](https://docs.kalshi.com/api-reference/portfolio/decrease-order)
    

We reserve the right to downgrade your API rate limit tier from Prime and Premier when you have shown lack of activity in the previous period.

[API Keys](https://docs.kalshi.com/getting_started/api_keys)
[Understanding Pagination](https://docs.kalshi.com/getting_started/pagination)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.