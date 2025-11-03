---
url: https://docs.polymarket.com/developers/CLOB/trades/trades
title: Get Trades - Polymarket Documentation
scraped_at: 2025-11-03T15:03:59.950304
---

[Skip to main content](https://docs.polymarket.com/developers/CLOB/trades/trades#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

Ctrl K

Search...

Navigation

Trades

Get Trades

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

Python

Typescript

Copy

Ask AI

from py_clob_client.clob_types import TradeParams
    
    resp = client.get_trades(
        TradeParams(
            maker_address=client.get_address(),
            market="0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",
        ),
    )
    print(resp)
    print("Done!")

This endpoint requires a L2 Header.

Get trades for the authenticated user based on the provided filters. **HTTP REQUEST** `GET /<clob-endpoint>/data/trades`

### 

[​](https://docs.polymarket.com/developers/CLOB/trades/trades#request-parameters)

Request Parameters

| Name | Required | Type | Description |
| --- | --- | --- | --- |
| id  | no  | string | id of trade to fetch |
| taker | no  | string | address to get trades for where it is included as a taker |
| maker | no  | string | address to get trades for where it is included as a maker |
| market | no  | string | market for which to get the trades (condition ID) |
| before | no  | string | unix timestamp representing the cutoff up to which trades that happened before then can be included |
| after | no  | string | unix timestamp representing the cutoff for which trades that happened after can be included |

### 

[​](https://docs.polymarket.com/developers/CLOB/trades/trades#response-format)

Response Format

| Name | Type | Description |
| --- | --- | --- |
| null | Trade\[\] | list of trades filtered by query parameters |

A `Trade` object is of the form:

| Name | Type | Description |
| --- | --- | --- |
| id  | string | trade id |
| taker\_order\_id | string | hash of taker order (market order) that catalyzed the trade |
| market | string | market id (condition id) |
| asset\_id | string | asset id (token id) of taker order (market order) |
| side | string | buy or sell |
| size | string | size |
| fee\_rate\_bps | string | the fees paid for the taker order expressed in basic points |
| price | string | limit price of taker order |
| status | string | trade status (see above) |
| match\_time | string | time at which the trade was matched |
| last\_update | string | timestamp of last status update |
| outcome | string | human readable outcome of the trade |
| maker\_address | string | funder address of the taker of the trade |
| owner | string | api key of taker of the trade |
| transaction\_hash | string | hash of the transaction where the trade was executed |
| bucket\_index | integer | index of bucket for trade in case trade is executed in multiple transactions |
| maker\_orders | MakerOrder\[\] | list of the maker trades the taker trade was filled against |
| type | string | side of the trade: TAKER or MAKER |

A `MakerOrder` object is of the form:

| Name | Type | Description |
| --- | --- | --- |
| order\_id | string | id of maker order |
| maker\_address | string | maker address of the order |
| owner | string | api key of the owner of the order |
| matched\_amount | string | size of maker order consumed with this trade |
| fee\_rate\_bps | string | the fees paid for the taker order expressed in basic points |
| price | string | price of maker order |
| asset\_id | string | token/asset id |
| outcome | string | human readable outcome of the maker order |
| side | string | the side of the maker order. Can be `buy` or `sell` |

[Trades Overview](https://docs.polymarket.com/developers/CLOB/trades/trades-overview)
[WSS Overview](https://docs.polymarket.com/developers/CLOB/websocket/wss-overview)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.