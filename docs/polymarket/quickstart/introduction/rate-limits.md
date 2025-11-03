---
url: https://docs.polymarket.com/quickstart/introduction/rate-limits
title: API Rate Limits - Polymarket Documentation
scraped_at: 2025-11-03T15:04:25.632062
---

[Skip to main content](https://docs.polymarket.com/quickstart/introduction/rate-limits#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

Ctrl K

Search...

Navigation

Developer Quickstart

API Rate Limits

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

On this page

*   [How Rate Limiting Works](https://docs.polymarket.com/quickstart/introduction/rate-limits#how-rate-limiting-works)
    
*   [General Rate Limits](https://docs.polymarket.com/quickstart/introduction/rate-limits#general-rate-limits)
    
*   [Data API Rate Limits](https://docs.polymarket.com/quickstart/introduction/rate-limits#data-api-rate-limits)
    
*   [GAMMA API Rate Limits](https://docs.polymarket.com/quickstart/introduction/rate-limits#gamma-api-rate-limits)
    
*   [CLOB API Rate Limits](https://docs.polymarket.com/quickstart/introduction/rate-limits#clob-api-rate-limits)
    
*   [General CLOB Endpoints](https://docs.polymarket.com/quickstart/introduction/rate-limits#general-clob-endpoints)
    
*   [CLOB Market Data](https://docs.polymarket.com/quickstart/introduction/rate-limits#clob-market-data)
    
*   [CLOB Ledger Endpoints](https://docs.polymarket.com/quickstart/introduction/rate-limits#clob-ledger-endpoints)
    
*   [CLOB Markets & Pricing](https://docs.polymarket.com/quickstart/introduction/rate-limits#clob-markets-%26-pricing)
    
*   [CLOB Authentication](https://docs.polymarket.com/quickstart/introduction/rate-limits#clob-authentication)
    
*   [CLOB Trading Endpoints](https://docs.polymarket.com/quickstart/introduction/rate-limits#clob-trading-endpoints)
    
*   [Other API Rate Limits](https://docs.polymarket.com/quickstart/introduction/rate-limits#other-api-rate-limits)
    

[​](https://docs.polymarket.com/quickstart/introduction/rate-limits#how-rate-limiting-works)

How Rate Limiting Works
-----------------------------------------------------------------------------------------------------------------------

All rate limits are enforced using Cloudflare’s throttling system. When you exceed the maximum configured rate for any endpoint, requests are throttled rather than immediately rejected. This means:

*   **Throttling**: Requests over the limit are delayed/queued rather than dropped
*   **Burst Allowances**: Some endpoints allow short bursts above the sustained rate
*   **Time Windows**: Limits reset based on sliding time windows (e.g., per 10 seconds, per minute)

[​](https://docs.polymarket.com/quickstart/introduction/rate-limits#general-rate-limits)

General Rate Limits
---------------------------------------------------------------------------------------------------------------

| Endpoint | Limit | Notes |
| --- | --- | --- |
| General Rate Limiting | 5000 requests / 10s | Throttle requests over the maximum configured rate |
| ”OK” Endpoint | 50 requests / 10s | Throttle requests over the maximum configured rate |

[​](https://docs.polymarket.com/quickstart/introduction/rate-limits#data-api-rate-limits)

Data API Rate Limits
-----------------------------------------------------------------------------------------------------------------

| Endpoint | Limit | Notes |
| --- | --- | --- |
| Data API (General) | 200 requests / 10s | Throttle requests over the maximum configured rate |
| Data API (Alternative) | 1200 requests / 1 minute | 10 minutes block on violation |
| Data API `/trades` | 75 requests / 10s | Throttle requests over the maximum configured rate |
| Data API “OK” Endpoint | 10 requests / 10s | Throttle requests over the maximum configured rate |

[​](https://docs.polymarket.com/quickstart/introduction/rate-limits#gamma-api-rate-limits)

GAMMA API Rate Limits
-------------------------------------------------------------------------------------------------------------------

| Endpoint | Limit | Notes |
| --- | --- | --- |
| GAMMA (General) | 750 requests / 10s | Throttle requests over the maximum configured rate |
| GAMMA Get Comments | 100 requests / 10s | Throttle requests over the maximum configured rate |
| GAMMA `/events` | 100 requests / 10s | Throttle requests over the maximum configured rate |
| GAMMA `/markets` | 125 requests / 10s | Throttle requests over the maximum configured rate |
| GAMMA `/markets` /events listing | 100 requests / 10s | Throttle requests over the maximum configured rate |
| GAMMA Tags | 100 requests / 10s | Throttle requests over the maximum configured rate |
| GAMMA Search | 300 requests / 10s | Throttle requests over the maximum configured rate |

[​](https://docs.polymarket.com/quickstart/introduction/rate-limits#clob-api-rate-limits)

CLOB API Rate Limits
-----------------------------------------------------------------------------------------------------------------

### 

[​](https://docs.polymarket.com/quickstart/introduction/rate-limits#general-clob-endpoints)

General CLOB Endpoints

| Endpoint | Limit | Notes |
| --- | --- | --- |
| CLOB (General) | 5000 requests / 10s | Throttle requests over the maximum configured rate |
| CLOB GET Balance Allowance | 125 requests / 10s | Throttle requests over the maximum configured rate |
| CLOB UPDATE Balance Allowance | 20 requests / 10s | Throttle requests over the maximum configured rate |

### 

[​](https://docs.polymarket.com/quickstart/introduction/rate-limits#clob-market-data)

CLOB Market Data

| Endpoint | Limit | Notes |
| --- | --- | --- |
| CLOB `/book` | 200 requests / 10s | Throttle requests over the maximum configured rate |
| CLOB `/books` | 80 requests / 10s | Throttle requests over the maximum configured rate |
| CLOB `/price` | 200 requests / 10s | Throttle requests over the maximum configured rate |
| CLOB `/prices` | 80 requests / 10s | Throttle requests over the maximum configured rate |
| CLOB `/midprice` | 200 requests / 10s | Throttle requests over the maximum configured rate |
| CLOB `/midprices` | 80 requests / 10s | Throttle requests over the maximum configured rate |

### 

[​](https://docs.polymarket.com/quickstart/introduction/rate-limits#clob-ledger-endpoints)

CLOB Ledger Endpoints

| Endpoint | Limit | Notes |
| --- | --- | --- |
| CLOB Ledger (`/trades` `/orders` `/notifications` `/order`) | 300 requests / 10s | Throttle requests over the maximum configured rate |
| CLOB Ledger `/data/orders` | 150 requests / 10s | Throttle requests over the maximum configured rate |
| CLOB Ledger `/data/trades` | 150 requests / 10s | Throttle requests over the maximum configured rate |
| CLOB `/notifications` | 125 requests / 10s | Throttle requests over the maximum configured rate |

### 

[​](https://docs.polymarket.com/quickstart/introduction/rate-limits#clob-markets-%26-pricing)

CLOB Markets & Pricing

| Endpoint | Limit | Notes |
| --- | --- | --- |
| CLOB Price History | 100 requests / 10s | Throttle requests over the maximum configured rate |
| CLOB Markets | 250 requests / 10s | Throttle requests over the maximum configured rate |
| CLOB Market Tick Size | 50 requests / 10s | Throttle requests over the maximum configured rate |
| CLOB `markets/0x` | 50 requests / 10s | Throttle requests over the maximum configured rate |
| CLOB `/markets` listing | 100 requests / 10s | Throttle requests over the maximum configured rate |

### 

[​](https://docs.polymarket.com/quickstart/introduction/rate-limits#clob-authentication)

CLOB Authentication

| Endpoint | Limit | Notes |
| --- | --- | --- |
| CLOB API Keys | 50 requests / 10s | Throttle requests over the maximum configured rate |

### 

[​](https://docs.polymarket.com/quickstart/introduction/rate-limits#clob-trading-endpoints)

CLOB Trading Endpoints

| Endpoint | Limit | Notes |
| --- | --- | --- |
| CLOB POST `/order` | 2400 requests / 10s (240/s) | BURST - Throttle requests over the maximum configured rate |
| CLOB POST `/order` | 24000 requests / 10 minutes (40/s) | Throttle requests over the maximum configured rate |
| CLOB DELETE `/order` | 2400 requests / 10s (240/s) | BURST - Throttle requests over the maximum configured rate |
| CLOB DELETE `/order` | 24000 requests / 10 minutes (40/s) | Throttle requests over the maximum configured rate |
| CLOB POST `/orders` | 800 requests / 10s (80/s) | BURST - Throttle requests over the maximum configured rate |
| CLOB POST `/orders` | 12000 requests / 10 minutes (20/s) | Throttle requests over the maximum configured rate |
| CLOB DELETE `/orders` | 800 requests / 10s (80/s) | BURST - Throttle requests over the maximum configured rate |
| CLOB DELETE `/orders` | 12000 requests / 10 minutes (20/s) | Throttle requests over the maximum configured rate |
| CLOB DELETE `/cancel-all` | 200 requests / 10s (20/s) | BURST - Throttle requests over the maximum configured rate |
| CLOB DELETE `/cancel-all` | 3000 requests / 10 minutes (5/s) | Throttle requests over the maximum configured rate |
| CLOB DELETE `/cancel-market-orders` | 800 requests / 10s (80/s) | BURST - Throttle requests over the maximum configured rate |
| CLOB DELETE `/cancel-market-orders` | 12000 requests / 10 minutes (20/s) | Throttle requests over the maximum configured rate |

[​](https://docs.polymarket.com/quickstart/introduction/rate-limits#other-api-rate-limits)

Other API Rate Limits
-------------------------------------------------------------------------------------------------------------------

| Endpoint | Limit | Notes |
| --- | --- | --- |
| RELAYER `/submit` | 15 requests / 1 minute | Throttle requests over the maximum configured rate |
| User PNL API | 100 requests / 10s | Throttle requests over the maximum configured rate |

[Glossary](https://docs.polymarket.com/quickstart/introduction/definitions)
[Endpoints](https://docs.polymarket.com/developers/CLOB/endpoints)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.