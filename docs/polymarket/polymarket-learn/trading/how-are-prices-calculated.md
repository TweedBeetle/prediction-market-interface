---
url: https://docs.polymarket.com/polymarket-learn/trading/how-are-prices-calculated
title: How Are Prices Calculated? - Polymarket Documentation
description: The prices probabilities displayed on Polymarket are the midpoint of the bid-ask spread in the orderbook.
scraped_at: 2025-11-03T15:04:22.370164
---

[Skip to main content](https://docs.polymarket.com/polymarket-learn/trading/how-are-prices-calculated#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

Ctrl K

Search...

Navigation

Markets

How Are Prices Calculated?

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

On this page

*   [Initial Price](https://docs.polymarket.com/polymarket-learn/trading/how-are-prices-calculated#initial-price)
    
*   [Future Price](https://docs.polymarket.com/polymarket-learn/trading/how-are-prices-calculated#future-price)
    
*   [Prices = Probabilities](https://docs.polymarket.com/polymarket-learn/trading/how-are-prices-calculated#prices-%3D-probabilities)
    

[​](https://docs.polymarket.com/polymarket-learn/trading/how-are-prices-calculated#initial-price)

Initial Price
------------------------------------------------------------------------------------------------------------------

*   When a market is created, there are initially zero shares and no pre-defined prices or odds.
*   Market makers (a fancy term for traders placing limit orders) interested in buying YES or NO shares can place [Limit Orders](https://docs.polymarket.com/polymarket-learn/trading/limit-orders)
     at the price they’re willing to pay
*   When offers for the YES and NO side equal $1.00, the order is “matched” and that $1.00 is converted into 1 YES and 1 NO share, each going to their respective buyers.

For example, if you place a limit order at $0.60 for YES, that order is matched when someone places a NO order at $0.40. _This becomes the initial market price._

[​](https://docs.polymarket.com/polymarket-learn/trading/how-are-prices-calculated#future-price)

Future Price
----------------------------------------------------------------------------------------------------------------

The prices displayed on Polymarket are the midpoint of the bid-ask spread in the orderbook — unless that spread is over $0.10, in which case the last traded price is used. Like the stock market, prices on Polymarket are a function of realtime supply & demand.

### 

[​](https://docs.polymarket.com/polymarket-learn/trading/how-are-prices-calculated#prices-%3D-probabilities)

Prices = Probabilities

In the market below, the probability of 37% is the midpoint between the 34¢ bid and 40¢ ask. If the bid-ask spread is wider than 10¢, the probability is shown as the last traded price.

![](https://polymarket-upload.s3.us-east-2.amazonaws.com/how_are_prices_calculated.png)

You may not be able to buy shares at the displayed probability / price because there is a bid-ask spread. In the above example, a trader wanting to buy shares would pay 40¢ for up to 4,200 shares, after which the price would rise to 43¢.

[How Are Markets Created?](https://docs.polymarket.com/polymarket-learn/markets/how-are-markets-created)
[How Are Prediction Markets Resolved?](https://docs.polymarket.com/polymarket-learn/markets/how-are-markets-resolved)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.