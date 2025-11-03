---
url: https://docs.kalshi.com/fix/rfq-messages
title: RFQ Messages - API Documentation
description: Request for Quote functionality for market makers
scraped_at: 2025-11-03T14:46:34.995692
---

[Skip to main content](https://docs.kalshi.com/fix/rfq-messages#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

RFQ Messages

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

On this page

*   [RFQ (Request for Quote) Messages](https://docs.kalshi.com/fix/rfq-messages#rfq-request-for-quote-messages)
    
*   [Overview](https://docs.kalshi.com/fix/rfq-messages#overview)
    
*   [Message Flow](https://docs.kalshi.com/fix/rfq-messages#message-flow)
    
*   [QuoteRequest (35=R)](https://docs.kalshi.com/fix/rfq-messages#quoterequest-35%3Dr)
    
*   [Quote (35=S)](https://docs.kalshi.com/fix/rfq-messages#quote-35%3Ds)
    
*   [QuoteStatusReport (35=AI)](https://docs.kalshi.com/fix/rfq-messages#quotestatusreport-35%3Dai)
    
*   [Quote Status Values (297)](https://docs.kalshi.com/fix/rfq-messages#quote-status-values-297)
    
*   [QuoteCancel (35=Z)](https://docs.kalshi.com/fix/rfq-messages#quotecancel-35%3Dz)
    
*   [QuoteCancelStatus (35=U9)](https://docs.kalshi.com/fix/rfq-messages#quotecancelstatus-35%3Du9)
    
*   [QuoteConfirm (35=U7)](https://docs.kalshi.com/fix/rfq-messages#quoteconfirm-35%3Du7)
    
*   [QuoteConfirmStatus (35=U8)](https://docs.kalshi.com/fix/rfq-messages#quoteconfirmstatus-35%3Du8)
    
*   [QuoteRequestReject (35=AG)](https://docs.kalshi.com/fix/rfq-messages#quoterequestreject-35%3Dag)
    
*   [Best Practices](https://docs.kalshi.com/fix/rfq-messages#best-practices)
    
*   [For Market Makers](https://docs.kalshi.com/fix/rfq-messages#for-market-makers)
    
*   [Error Handling](https://docs.kalshi.com/fix/rfq-messages#error-handling)
    
*   [Example Workflow](https://docs.kalshi.com/fix/rfq-messages#example-workflow)
    
*   [Integration Notes](https://docs.kalshi.com/fix/rfq-messages#integration-notes)
    

[​](https://docs.kalshi.com/fix/rfq-messages#rfq-request-for-quote-messages)

RFQ (Request for Quote) Messages
================================================================================================================

[​](https://docs.kalshi.com/fix/rfq-messages#overview)

Overview
------------------------------------------------------------------

The RFQ session allows market makers to respond to quote requests from users. The workflow involves:

1.  Exchange sends QuoteRequest to market makers
2.  Market makers respond with Quote
3.  Requester can accept the quote
4.  Market maker confirms execution

RFQ sessions use the KalshiRFQ endpoint with retransmission support.

[​](https://docs.kalshi.com/fix/rfq-messages#message-flow)

Message Flow
--------------------------------------------------------------------------

[​](https://docs.kalshi.com/fix/rfq-messages#quoterequest-35%3Dr)

QuoteRequest (35=R)
----------------------------------------------------------------------------------------

This message is sent by Kalshi Exchange back to clients to inform of new quote requests.

| Tag | Name | Type | Required | Description |
| --- | --- | --- | --- | --- |
| 131 | QuoteReqId | UUID | Y   | Unique quote request ID |
| 146 | NoRelatedSym | Integer | Y   | Number of symbols. Currently, only 1 is supported. |
| 38  | OrderQty | Integer | Y   | Number of contracts |
| 152 | CashOrderQty | Decimal | N   | Target cost of the quote in dollars. |
| 55  | Symbol | String | Y   | Market ticker |
| 453 | NoPartyIDs | Integer | N   | Number of parties. Currently, only 1 is supported. |
| 448 | PartyId | UUID | N   | Pseudonymous identifier for requester |
| 20180 | MultivariateCollectionTicker | String | N   | Collection ticker for multivariate markets |
| 20181 | NoMultivariateSelectedLegs | Integer | N   | Number of selected legs for multivariate markets. Repeating group containing the following 3 fields. |
| 20182 | MultivariateSelectedEventTicker | String | N   | Event ticker for the selected leg |
| 20183 | MultivariateSelectedMarketTicker | String | N   | Market ticker for the selected leg |
| 20184 | MultivariateSelectedMarketSide | String | N   | Side for the selected leg (“yes” or “no”) |

[​](https://docs.kalshi.com/fix/rfq-messages#quote-35%3Ds)

Quote (35=S)
--------------------------------------------------------------------------

Used to submit a quote in response to a quote request. If a new Quote is created when an existing quote for the same market already exists for the user, the exchange will cancel the existing quote.

| Tag | Name | Type | Required | Description |
| --- | --- | --- | --- | --- |
| 117 | QuoteId | UUID | Y   | Unique quote identifier |
| 131 | QuoteReqId | UUID | Y   | Quote request for which the quote is in response to. |
| 55  | Symbol | String | Y   | Market ticker |
| 132 | BidPx | Integer | Y   | Yes price in cents. Only integer part considered (1-99) |
| 133 | OfferPx | Integer | Y   | No price in cents. Only integer part considered (1-99) |

Either BidPx or OfferPx can be zero, but not both. Zero indicates no quote for that side.

[​](https://docs.kalshi.com/fix/rfq-messages#quotestatusreport-35%3Dai)

QuoteStatusReport (35=AI)
----------------------------------------------------------------------------------------------------

A QuoteStatusReport is sent by the exchange:

1.  In response to a Quote. Status will be PENDING if processed, or REJECTED if rejected
2.  When the requester accepts the quote. Status will be ACCEPTED. Quoter should reply with QuoteConfirm within 30 seconds
3.  In response to a QuoteCancel. Status will be CANCELLED

| Tag | Name | Type | Required | Description |
| --- | --- | --- | --- | --- |
| 117 | QuoteId | String | Y   | Quote identifier (empty if rejected) |
| 131 | QuoteReqId | String | Y   | Request reference |
| 297 | QuoteStatus | Integer | Y   | Current status |
| 38  | OrderQty | Integer | C   | Number of contracts. Not present if REJECTED |
| 132 | BidPx | Integer | C   | Yes price in cents. Only integer part considered. Not present if REJECTED |
| 133 | OfferPx | Integer | C   | No price in cents. Only integer part considered. Not present if REJECTED |
| 54  | AcceptedSide | Char | C   | Side accepted (1=Yes, 2=No). Only present if ACCEPTED |
| 58  | Text | String | C   | Rejection reason. Only present if REJECTED |

### 

[​](https://docs.kalshi.com/fix/rfq-messages#quote-status-values-297)

Quote Status Values (297)

*   **ACCEPTED<0>**: Requester accepted the quote
*   **REJECTED<5>**: Exchange rejected the quote
*   **PENDING<10>**: Quote processed, awaiting action
*   **CANCELLED<17>**: Quote cancelled

[​](https://docs.kalshi.com/fix/rfq-messages#quotecancel-35%3Dz)

QuoteCancel (35=Z)
--------------------------------------------------------------------------------------

Market maker cancels an active quote.

| Tag | Name | Type | Required | Description |
| --- | --- | --- | --- | --- |
| 117 | QuoteId | String | Y   | Quote to cancel |

Exchange responds with QuoteStatusReport (Status=CANCELLED).

[​](https://docs.kalshi.com/fix/rfq-messages#quotecancelstatus-35%3Du9)

QuoteCancelStatus (35=U9)
----------------------------------------------------------------------------------------------------

Response to QuoteCancel from exchange.

| Tag | Name | Type | Required | Description |
| --- | --- | --- | --- | --- |
| 117 | QuoteId | String | Y   | Quote identifier |
| 298 | QuoteCancelStatus | Integer | Y   | CANCELED(0) or REJECTED(1) |
| 58  | RejectReason | String | C   | Present if QuoteCancelStatus is REJECTED |

[​](https://docs.kalshi.com/fix/rfq-messages#quoteconfirm-35%3Du7)

QuoteConfirm (35=U7)
------------------------------------------------------------------------------------------

Market maker confirms willingness to execute after quote acceptance.

| Tag | Name | Type | Required | Description |
| --- | --- | --- | --- | --- |
| 117 | QuoteId | String | Y   | Accepted quote ID |

Quote must be confirmed within 30 seconds of acceptance or it will be voided.

[​](https://docs.kalshi.com/fix/rfq-messages#quoteconfirmstatus-35%3Du8)

QuoteConfirmStatus (35=U8)
------------------------------------------------------------------------------------------------------

Exchange response to quote confirmation.

| Tag | Name | Type | Required | Description |
| --- | --- | --- | --- | --- |
| 117 | QuoteId | String | Y   | Quote identifier |
| 297 | QuoteConfirmStatus | Integer | Y   | ACCEPTED(0) or REJECTED(1) |
| 58  | RejectReason | String | C   | Present if QuoteConfirmStatus is REJECTED |

[​](https://docs.kalshi.com/fix/rfq-messages#quoterequestreject-35%3Dag)

QuoteRequestReject (35=AG)
------------------------------------------------------------------------------------------------------

Exchange notifies that a quote request was cancelled.

| Tag | Name | Type | Required | Description |
| --- | --- | --- | --- | --- |
| 58  | Text | String | Y   | Reason the quote has been cancelled |
| 131 | QuoteReqId | String | Y   | Request identifier |
| 658 | QuoteRequestRejectReason | Integer | Y   | OTHER(99) |

Market makers do not send QuoteRequestReject when ignoring a request.

[​](https://docs.kalshi.com/fix/rfq-messages#best-practices)

Best Practices
------------------------------------------------------------------------------

### 

[​](https://docs.kalshi.com/fix/rfq-messages#for-market-makers)

For Market Makers

1.  **Response Time**
    *   Respond to quote requests promptly
    *   Confirm accepted quotes within 30 seconds
    *   Cancel stale quotes proactively
2.  **Quote Management**
    *   Track active quotes locally
    *   Handle quote replacements properly
    *   Monitor for acceptance notifications
3.  **Risk Management**
    *   Validate prices before quoting
    *   Implement position limits
    *   Handle partial quotes (one-sided)

### 

[​](https://docs.kalshi.com/fix/rfq-messages#error-handling)

Error Handling

1.  **Rejection Scenarios**
    *   Invalid price range
    *   Symbol not found
    *   Technical issues
2.  **Timeout Handling**
    *   30-second confirmation window
    *   Automatic quote expiration
    *   Network disconnection recovery

[​](https://docs.kalshi.com/fix/rfq-messages#example-workflow)

Example Workflow
----------------------------------------------------------------------------------

QuoteRequest from Exchange

Quote Response

Quote Accepted

Quote Confirmation

Copy

Ask AI

    8=FIXT.1.1|35=R|131=req-123|146=1|38=100|55=HIGHNY-23DEC31|453=1|448=anon-456|
    

[​](https://docs.kalshi.com/fix/rfq-messages#integration-notes)

Integration Notes
------------------------------------------------------------------------------------

*   RFQ session requires separate connection
*   Uses KalshiRFQ endpoint
*   Independent of order entry session

[Order Group Messages](https://docs.kalshi.com/fix/order-groups)
[Drop Copy Session](https://docs.kalshi.com/fix/drop-copy)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.