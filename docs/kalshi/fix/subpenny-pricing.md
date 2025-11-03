---
url: https://docs.kalshi.com/fix/subpenny-pricing
title: Subpenny Pricing - API Documentation
description: Dollar-based pricing format for subpenny precision
scraped_at: 2025-11-03T14:46:36.036770
---

[Skip to main content](https://docs.kalshi.com/fix/subpenny-pricing#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

Subpenny Pricing

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

On this page

*   [Technical Specification](https://docs.kalshi.com/fix/subpenny-pricing#technical-specification)
    
*   [Sample Messages](https://docs.kalshi.com/fix/subpenny-pricing#sample-messages)
    

[​](https://docs.kalshi.com/fix/subpenny-pricing#technical-specification)

Technical Specification
----------------------------------------------------------------------------------------------------

To enable subpenny precision, include tag **21005** in your Logon message:

| Tag | Name | Description | Value |
| --- | --- | --- | --- |
| 21005 | UseDollars | Enable dollar-based price format | Y   |

Overview:

*   **Legacy Format (Cents)**: Prices given in whole cents. E.g. 72 cents = `72`.
*   **New Format (Dollars)**: Prices normalized to dollars with fixed precision (up to 4 decimal places).

Examples:

| Cents | FIX Decimal | String Representation |
| --- | --- | --- |
| 1.23¢ | Decimal(123, -4) | 0.0123 |
| 72.5¢ | Decimal(7250, -4) | 0.725 |
| 99¢ | Decimal(9900, -4) | 0.99 |

Affected Tags:

| Tag | Field Name | Description |
| --- | --- | --- |
| 6   | AvgPx | Average price of fills |
| 31  | LastPx | Price of last fill |
| 44  | Price | Order limit price |
| 132 | BidPx | Quote bid price |
| 133 | OfferPx | Quote ask price |

[​](https://docs.kalshi.com/fix/subpenny-pricing#sample-messages)

Sample Messages
------------------------------------------------------------------------------------

logon

Copy

Ask AI

    8=FIXT.1.1|9=300|35=A|34=1|52=20250926-21:54:07.001|
    96=QhA8659Mhygcm+xE/wb1m...|21005=Y|
                                ^^ Enable dollar format
    

new order single

Copy

Ask AI

    8=FIXT.1.1|9=200|35=D|34=2|52=20250926-21:54:16.040|
    38=100.0|40=2|44=0.7500|54=1|60=20250926-21:54:16.040|
                  ^^ price
    10=092|
    

execution report

Copy

Ask AI

    8=FIXT.1.1|9=400|35=8|34=4|52=20250926-21:54:16.159|
    6=0.6600|14=100|31=0.7000|32=60|38=100.0000|39=2|44=0.7500|
    ^^ avgPx        ^^ lastPx                        ^^ price
    

[Error Handling](https://docs.kalshi.com/fix/error-handling)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.