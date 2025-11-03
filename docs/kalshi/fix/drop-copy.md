---
url: https://docs.kalshi.com/fix/drop-copy
title: Drop Copy Session - API Documentation
description: Recover missed execution reports and query historical order events
scraped_at: 2025-11-03T14:46:33.687171
---

[Skip to main content](https://docs.kalshi.com/fix/drop-copy#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

Drop Copy Session

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

On this page

*   [Drop Copy Session](https://docs.kalshi.com/fix/drop-copy#drop-copy-session)
    
*   [Overview](https://docs.kalshi.com/fix/drop-copy#overview)
    
*   [Connection Details](https://docs.kalshi.com/fix/drop-copy#connection-details)
    
*   [EventResendRequest (35=U1)](https://docs.kalshi.com/fix/drop-copy#eventresendrequest-35%3Du1)
    
*   [Fields](https://docs.kalshi.com/fix/drop-copy#fields)
    
*   [Limitations](https://docs.kalshi.com/fix/drop-copy#limitations)
    
*   [Example Request](https://docs.kalshi.com/fix/drop-copy#example-request)
    
*   [EventResendComplete (35=U2)](https://docs.kalshi.com/fix/drop-copy#eventresendcomplete-35%3Du2)
    
*   [Fields](https://docs.kalshi.com/fix/drop-copy#fields-2)
    
*   [EventResendReject (35=U3)](https://docs.kalshi.com/fix/drop-copy#eventresendreject-35%3Du3)
    
*   [Fields](https://docs.kalshi.com/fix/drop-copy#fields-3)
    
*   [Rejection Reasons (21004)](https://docs.kalshi.com/fix/drop-copy#rejection-reasons-21004)
    
*   [Usage Patterns](https://docs.kalshi.com/fix/drop-copy#usage-patterns)
    
*   [Recovery After Disconnect](https://docs.kalshi.com/fix/drop-copy#recovery-after-disconnect)
    
*   [Best Practices](https://docs.kalshi.com/fix/drop-copy#best-practices)
    
*   [1\. ExecID Management](https://docs.kalshi.com/fix/drop-copy#1-execid-management)
    
*   [2\. Rate Limiting](https://docs.kalshi.com/fix/drop-copy#2-rate-limiting)
    
*   [3\. Deduplication](https://docs.kalshi.com/fix/drop-copy#3-deduplication)
    
*   [4\. Error Recovery](https://docs.kalshi.com/fix/drop-copy#4-error-recovery)
    
*   [Comparison with Retransmission](https://docs.kalshi.com/fix/drop-copy#comparison-with-retransmission)
    

[​](https://docs.kalshi.com/fix/drop-copy#drop-copy-session)

Drop Copy Session
=================================================================================

[​](https://docs.kalshi.com/fix/drop-copy#overview)

Overview
---------------------------------------------------------------

The drop copy session provides an alternative method to query for missed execution reports without using the FIX retransmission protocol. This is particularly useful for:

*   Recovering from connection failures
*   Auditing order activity
*   Building backup systems
*   Compliance recording

Kalshi’s DropCopy format utilizes a request-response message type, if you are interested in a session that “follows along” the execution report activity of your trading session, consider using a KalshiRT session with the ListenerFlag parameter.

[​](https://docs.kalshi.com/fix/drop-copy#connection-details)

Connection Details
-----------------------------------------------------------------------------------

| Environment | URL | Port | TargetCompID |
| --- | --- | --- | --- |
| Production | fix.elections.kalshi.com | 8229 | KalshiDC |
| Demo | fix.demo.kalshi.co | 8229 | KalshiDC |

[​](https://docs.kalshi.com/fix/drop-copy#eventresendrequest-35%3Du1)

EventResendRequest (35=U1)
---------------------------------------------------------------------------------------------------

Request execution reports within a specified ExecID range.

### 

[​](https://docs.kalshi.com/fix/drop-copy#fields)

Fields

| Tag | Name | Description | Required |
| --- | --- | --- | --- |
| 21001 | BeginExecID | Starting ExecID (inclusive) | Yes |
| 21002 | EndExecID | Ending ExecID (inclusive) | No  |

If EndExecID is not provided, it defaults to the latest ExecID in your history.

### 

[​](https://docs.kalshi.com/fix/drop-copy#limitations)

Limitations

*   **Lookback Window**: Last 3 hours only
*   **Message Types**: Only ExecutionReport (35=8) supported
*   **Excluded Messages**:
    *   Rejects (no valid ExecID)
    *   Pending new orders (ExecID = “-1;-1”)

### 

[​](https://docs.kalshi.com/fix/drop-copy#example-request)

Example Request

Copy

Ask AI

    8=FIXT.1.1|35=U1|21001=12345;67890|21002=12350;67895|
    

[​](https://docs.kalshi.com/fix/drop-copy#eventresendcomplete-35%3Du2)

EventResendComplete (35=U2)
-----------------------------------------------------------------------------------------------------

Sent after all requested events have been resent.

### 

[​](https://docs.kalshi.com/fix/drop-copy#fields-2)

Fields

| Tag | Name | Description | Required |
| --- | --- | --- | --- |
| 45  | RefSeqNum | MsgSeqNum of the EventResendRequest | Yes |
| 21003 | ResentEventCount | Total number of events resent | Yes |

[​](https://docs.kalshi.com/fix/drop-copy#eventresendreject-35%3Du3)

EventResendReject (35=U3)
-------------------------------------------------------------------------------------------------

Sent when a resend request cannot be fulfilled.

### 

[​](https://docs.kalshi.com/fix/drop-copy#fields-3)

Fields

| Tag | Name | Description | Required |
| --- | --- | --- | --- |
| 45  | RefSeqNum | MsgSeqNum of the EventResendRequest | Yes |
| 21004 | EventResendRejectReason | Rejection code | Yes |

### 

[​](https://docs.kalshi.com/fix/drop-copy#rejection-reasons-21004)

Rejection Reasons (21004)

| Code | Description |
| --- | --- |
| 1   | Too many resend requests |
| 2   | Server error |
| 3   | BeginExecID is too small (outside window) |
| 4   | EndExecID is too large |

[​](https://docs.kalshi.com/fix/drop-copy#usage-patterns)

Usage Patterns
---------------------------------------------------------------------------

### 

[​](https://docs.kalshi.com/fix/drop-copy#recovery-after-disconnect)

Recovery After Disconnect

1

Track Last ExecID

Store the last processed ExecID before disconnect

2

Reconnect to Drop Copy

Establish new drop copy session

3

Request Missing Events

Send EventResendRequest starting from last ExecID

4

Process Resent Events

Handle execution reports with new sequence numbers

[​](https://docs.kalshi.com/fix/drop-copy#best-practices)

Best Practices
---------------------------------------------------------------------------

### 

[​](https://docs.kalshi.com/fix/drop-copy#1-execid-management)

1\. ExecID Management

*   Store ExecIDs persistently
*   Handle the two-part format correctly (e.g., “12345;67890”)
*   Implement proper ID comparison logic

### 

[​](https://docs.kalshi.com/fix/drop-copy#2-rate-limiting)

2\. Rate Limiting

*   Avoid excessive resend requests
*   Implement exponential backoff on failures
*   Batch requests when possible

### 

[​](https://docs.kalshi.com/fix/drop-copy#3-deduplication)

3\. Deduplication

*   Events may arrive via both primary and drop copy sessions
*   Implement deduplication based on ExecID
*   Handle out-of-order delivery

### 

[​](https://docs.kalshi.com/fix/drop-copy#4-error-recovery)

4\. Error Recovery

*   Handle all rejection codes appropriately
*   Implement retry logic with delays
*   Alert on persistent failures

[​](https://docs.kalshi.com/fix/drop-copy#comparison-with-retransmission)

Comparison with Retransmission
-----------------------------------------------------------------------------------------------------------

| Feature | Drop Copy | Retransmission |
| --- | --- | --- |
| Session Type | Separate | Same as order entry |
| Sequence Numbers | Independent | Original preserved |
| Lookback Window | 3 hours | 3 hours |
| Message Types | ExecutionReport only | All types |
| Use Case | Recovery/Audit | Real-time gaps |

All resent messages will have new FIX sequence numbers in the drop copy session, different from their original sequence numbers in the order entry session.

[RFQ Messages](https://docs.kalshi.com/fix/rfq-messages)
[Market Settlement](https://docs.kalshi.com/fix/market-settlement)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.