---
url: https://docs.polymarket.com/developers/CLOB/orders/onchain-order-info
title: Onchain Order Info - Polymarket Documentation
scraped_at: 2025-11-03T15:03:59.667270
---

[Skip to main content](https://docs.polymarket.com/developers/CLOB/orders/onchain-order-info#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

Ctrl K

Search...

Navigation

Order Manipulation

Onchain Order Info

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

On this page

*   [How do I interpret the OrderFilled onchain event?](https://docs.polymarket.com/developers/CLOB/orders/onchain-order-info#how-do-i-interpret-the-orderfilled-onchain-event%3F)
    

[​](https://docs.polymarket.com/developers/CLOB/orders/onchain-order-info#how-do-i-interpret-the-orderfilled-onchain-event%3F)

How do I interpret the OrderFilled onchain event?
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Given an OrderFilled event:

*   `orderHash`: a unique hash for the Order being filled
*   `maker`: the user generating the order and the source of funds for the order
*   `taker`: the user filling the order OR the Exchange contract if the order fills multiple limit orders
*   `makerAssetId`: id of the asset that is given out. If 0, indicates that the Order is a BUY, giving USDC in exchange for Outcome tokens. Else, indicates that the Order is a SELL, giving Outcome tokens in exchange for USDC.
*   `takerAssetId`: id of the asset that is received. If 0, indicates that the Order is a SELL, receiving USDC in exchange for Outcome tokens. Else, indicates that the Order is a BUY, receiving Outcome tokens in exchange for USDC.
*   `makerAmountFilled`: the amount of the asset that is given out.
*   `takerAmountFilled`: the amount of the asset that is received.
*   `fee`: the fees paid by the order maker

[Cancel Orders(s)](https://docs.polymarket.com/developers/CLOB/orders/cancel-orders)
[Trades Overview](https://docs.polymarket.com/developers/CLOB/trades/trades-overview)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.