---
url: https://docs.polymarket.com/developers/subgraph/overview
title: Overview - Polymarket Documentation
scraped_at: 2025-11-03T15:04:11.292968
---

[Skip to main content](https://docs.polymarket.com/developers/subgraph/overview#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

Ctrl K

Search...

Navigation

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

On this page

*   [Subgraph Overview](https://docs.polymarket.com/developers/subgraph/overview#subgraph-overview)
    
*   [Source](https://docs.polymarket.com/developers/subgraph/overview#source)
    
*   [Hosted Version](https://docs.polymarket.com/developers/subgraph/overview#hosted-version)
    

[​](https://docs.polymarket.com/developers/subgraph/overview#subgraph-overview)

Subgraph Overview
----------------------------------------------------------------------------------------------------

Polymarket has written and open sourced a subgraph that provides, via a GraphQL query interface, useful aggregate calculations and event indexing for things like volume, user position, market and liquidity data. The subgraph updates in real time to be able to be mixed, and match core data from the primary Polymarket interface, providing positional data, activity history and more. The subgraph can be hosted by anyone but is also hosted and made publicly available by a 3rd party provider, Goldsky.

[​](https://docs.polymarket.com/developers/subgraph/overview#source)

Source
------------------------------------------------------------------------------

The Polymarket subgraph is entirely open source and can be found on the Polymarket Github. **[Subgraph Github Repository](https://github.com/Polymarket/polymarket-subgraph)
**

> Note: The available models/schemas can be found in the `schema.graphql` file.

[​](https://docs.polymarket.com/developers/subgraph/overview#hosted-version)

Hosted Version
----------------------------------------------------------------------------------------------

The subgraphs are hosted on goldsky, each with an accompanying GraphQL playground:

*   Orders subgraph: [https://api.goldsky.com/api/public/project\_cl6mb8i9h0003e201j6li0diw/subgraphs/orderbook-subgraph/0.0.1/gn](https://api.goldsky.com/api/public/project_cl6mb8i9h0003e201j6li0diw/subgraphs/orderbook-subgraph/0.0.1/gn)
    
*   Positions subgraph: [https://api.goldsky.com/api/public/project\_cl6mb8i9h0003e201j6li0diw/subgraphs/positions-subgraph/0.0.7/gn](https://api.goldsky.com/api/public/project_cl6mb8i9h0003e201j6li0diw/subgraphs/positions-subgraph/0.0.7/gn)
    
*   Activity subgraph: [https://api.goldsky.com/api/public/project\_cl6mb8i9h0003e201j6li0diw/subgraphs/activity-subgraph/0.0.4/gn](https://api.goldsky.com/api/public/project_cl6mb8i9h0003e201j6li0diw/subgraphs/activity-subgraph/0.0.4/gn)
    
*   Open Interest subgraph: [https://api.goldsky.com/api/public/project\_cl6mb8i9h0003e201j6li0diw/subgraphs/oi-subgraph/0.0.6/gn](https://api.goldsky.com/api/public/project_cl6mb8i9h0003e201j6li0diw/subgraphs/oi-subgraph/0.0.6/gn)
    
*   PNL subgraph: [https://api.goldsky.com/api/public/project\_cl6mb8i9h0003e201j6li0diw/subgraphs/pnl-subgraph/0.0.14/gn](https://api.goldsky.com/api/public/project_cl6mb8i9h0003e201j6li0diw/subgraphs/pnl-subgraph/0.0.14/gn)
    

[Get live volume for an event](https://docs.polymarket.com/api-reference/misc/get-live-volume-for-an-event)
[Resolution](https://docs.polymarket.com/developers/resolution/UMA)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.