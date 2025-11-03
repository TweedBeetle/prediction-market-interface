---
url: https://docs.polymarket.com/developers/builders/builder-intro
title: Builder Program Introduction - Polymarket Documentation
description: Learn about Polymarket's Builder Program and how to integrate your platform
scraped_at: 2025-11-03T15:04:07.475645
---

[Skip to main content](https://docs.polymarket.com/developers/builders/builder-intro#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

Ctrl K

Search...

Navigation

Polymarket Builders Program

Builder Program Introduction

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

On this page

*   [What is a Builder?](https://docs.polymarket.com/developers/builders/builder-intro#what-is-a-builder%3F)
    
*   [Builder Program Benefits](https://docs.polymarket.com/developers/builders/builder-intro#builder-program-benefits)
    
*   [1\. Polygon Relayer Access](https://docs.polymarket.com/developers/builders/builder-intro#1-polygon-relayer-access)
    
*   [2\. Trading Attribution](https://docs.polymarket.com/developers/builders/builder-intro#2-trading-attribution)
    
*   [Getting Started](https://docs.polymarket.com/developers/builders/builder-intro#getting-started)
    

[​](https://docs.polymarket.com/developers/builders/builder-intro#what-is-a-builder%3F)

What is a Builder?
-------------------------------------------------------------------------------------------------------------

In the context of Polymarket, a “builder” refers to a person, group, or organization that routes orders from their customers to Polymarket. For example, if you’ve created a unique front end that allows your users to place trades on Polymarket via your system, then this guide is for you.

[​](https://docs.polymarket.com/developers/builders/builder-intro#builder-program-benefits)

Builder Program Benefits
-----------------------------------------------------------------------------------------------------------------------

The Builders Program currently provides two main benefits:

### 

[​](https://docs.polymarket.com/developers/builders/builder-intro#1-polygon-relayer-access)

1\. Polygon Relayer Access

We expose our Polygon relayer to builders, allowing you to route on-chain transactions through our infrastructure. This means:

*   **Polymarket pays for gas fees** on your behalf (when using our Safe Wallets)
*   You can deploy _Safe Wallets_ for your users and customers

### 

[​](https://docs.polymarket.com/developers/builders/builder-intro#2-trading-attribution)

2\. Trading Attribution

When posting orders to our CLOB exchange, you can add custom headers that identify you as a builder. This enables Polymarket to clearly attribute orders coming from your platform. High volume builders will be showcased in our upcoming _Builder Leaderboard_ allowing Builders to compete for grants from Polymarket.

[​](https://docs.polymarket.com/developers/builders/builder-intro#getting-started)

Getting Started
-----------------------------------------------------------------------------------------------------

Explore the following guides to integrate with the Builders Program:

*   [Order Attribution](https://docs.polymarket.com/developers/builders/order-attribution)
     - Learn how to attribute customer orders to your builder account
*   [Relayer Client](https://docs.polymarket.com/developers/builders/relayer-client)
     - Use the Polygon relayer for gasless transactions and Safe wallet deployment
*   [Builder Signing Server](https://docs.polymarket.com/developers/builders/builder-signing-server)
     - Set up a secure server for remote signing of builder headers

[Endpoints](https://docs.polymarket.com/developers/CLOB/endpoints)
[Order Attribution](https://docs.polymarket.com/developers/builders/order-attribution)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.