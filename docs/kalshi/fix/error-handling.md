---
url: https://docs.kalshi.com/fix/error-handling
title: Error Handling - API Documentation
description: Understanding and handling errors in the FIX protocol
scraped_at: 2025-11-03T14:46:33.750740
---

[Skip to main content](https://docs.kalshi.com/fix/error-handling#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

Error Handling

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

On this page

*   [Error Handling](https://docs.kalshi.com/fix/error-handling#error-handling)
    
*   [Overview](https://docs.kalshi.com/fix/error-handling#overview)
    
*   [Error Message Types](https://docs.kalshi.com/fix/error-handling#error-message-types)
    
*   [Reject (35=3)](https://docs.kalshi.com/fix/error-handling#reject-35%3D3)
    
*   [Session Reject Reasons (373)](https://docs.kalshi.com/fix/error-handling#session-reject-reasons-373)
    
*   [BusinessMessageReject (35=j)](https://docs.kalshi.com/fix/error-handling#businessmessagereject-35%3Dj)
    
*   [Business Reject Reasons (380)](https://docs.kalshi.com/fix/error-handling#business-reject-reasons-380)
    
*   [Order-Specific Rejections](https://docs.kalshi.com/fix/error-handling#order-specific-rejections)
    
*   [Order Reject Reasons (103)](https://docs.kalshi.com/fix/error-handling#order-reject-reasons-103)
    
*   [Cancel Reject Reasons (102)](https://docs.kalshi.com/fix/error-handling#cancel-reject-reasons-102)
    
*   [Common Error Scenarios](https://docs.kalshi.com/fix/error-handling#common-error-scenarios)
    
*   [Example 1: Invalid Tag](https://docs.kalshi.com/fix/error-handling#example-1%3A-invalid-tag)
    
*   [Example 2: Business Logic Error](https://docs.kalshi.com/fix/error-handling#example-2%3A-business-logic-error)
    
*   [Example 3: Order Rejection](https://docs.kalshi.com/fix/error-handling#example-3%3A-order-rejection)
    
*   [Error Handling Best Practices](https://docs.kalshi.com/fix/error-handling#error-handling-best-practices)
    
*   [1\. Comprehensive Logging](https://docs.kalshi.com/fix/error-handling#1-comprehensive-logging)
    
*   [2\. Retry Strategies](https://docs.kalshi.com/fix/error-handling#2-retry-strategies)
    
*   [3\. Graceful Degradation](https://docs.kalshi.com/fix/error-handling#3-graceful-degradation)
    
*   [Specific Error Conditions](https://docs.kalshi.com/fix/error-handling#specific-error-conditions)
    
*   [Authentication Errors](https://docs.kalshi.com/fix/error-handling#authentication-errors)
    
*   [Order Entry Errors](https://docs.kalshi.com/fix/error-handling#order-entry-errors)
    
*   [Connection Errors](https://docs.kalshi.com/fix/error-handling#connection-errors)
    
*   [Error Response Patterns](https://docs.kalshi.com/fix/error-handling#error-response-patterns)
    
*   [Synchronous Errors](https://docs.kalshi.com/fix/error-handling#synchronous-errors)
    
*   [Asynchronous Errors](https://docs.kalshi.com/fix/error-handling#asynchronous-errors)
    

[​](https://docs.kalshi.com/fix/error-handling#error-handling)

Error Handling
================================================================================

[​](https://docs.kalshi.com/fix/error-handling#overview)

Overview
--------------------------------------------------------------------

Kalshi FIX API uses standard FIX error messages with additional detail in the Text field. Errors fall into two categories:

*   **Session-level errors**: Protocol violations, handled with Reject (35=3)
*   **Business-level errors**: Application logic issues, handled with BusinessMessageReject (35=j) or specific rejection messages

[​](https://docs.kalshi.com/fix/error-handling#error-message-types)

Error Message Types
------------------------------------------------------------------------------------------

### 

[​](https://docs.kalshi.com/fix/error-handling#reject-35%3D3)

Reject (35=3)

Used for session-level protocol violations.

| Tag | Name | Description | Required |
| --- | --- | --- | --- |
| 45  | RefSeqNum | Sequence number of rejected message | Yes |
| 58  | Text | Human-readable error description | No  |
| 371 | RefTagID | Tag that caused the rejection | No  |
| 372 | RefMsgType | Message type being rejected | No  |
| 373 | SessionRejectReason | Rejection reason code | No  |

#### 

[​](https://docs.kalshi.com/fix/error-handling#session-reject-reasons-373)

Session Reject Reasons (373)

| Code | Reason | Description |
| --- | --- | --- |
| 0   | Invalid tag number | Unknown tag in message |
| 1   | Required tag missing | Mandatory field not present |
| 2   | Tag not defined for message | Tag not valid for this message type |
| 3   | Undefined tag | Tag number not in FIX specification |
| 4   | Tag without value | Empty tag value |
| 5   | Incorrect value | Invalid value for tag |
| 6   | Incorrect data format | Wrong data type |
| 7   | Decryption problem | Security issue |
| 8   | Signature problem | Authentication failure |
| 9   | CompID problem | SenderCompID/TargetCompID issue |
| 10  | SendingTime accuracy | Time outside acceptable window |
| 11  | Invalid MsgType | Unknown message type |

### 

[​](https://docs.kalshi.com/fix/error-handling#businessmessagereject-35%3Dj)

BusinessMessageReject (35=j)

Used for application-level business logic errors.

| Tag | Name | Description | Required |
| --- | --- | --- | --- |
| 45  | RefSeqNum | Sequence number of rejected message | Yes |
| 58  | Text | Human-readable error description | No  |
| 371 | RefTagID | Tag that caused the rejection | No  |
| 372 | RefMsgType | Message type being rejected | No  |
| 379 | BusinessRejectRefID | Business ID from rejected message | No  |
| 380 | BusinessRejectReason | Business rejection reason code | Yes |

#### 

[​](https://docs.kalshi.com/fix/error-handling#business-reject-reasons-380)

Business Reject Reasons (380)

| Code | Reason | Description |
| --- | --- | --- |
| 0   | Other | See Text field for details |
| 1   | Unknown ID | Referenced ID not found |
| 2   | Unknown Security | Invalid symbol |
| 3   | Unsupported Message Type | Message type not implemented |
| 4   | Application not available | System temporarily unavailable |
| 5   | Conditionally required field missing | Context-specific field missing |

[​](https://docs.kalshi.com/fix/error-handling#order-specific-rejections)

Order-Specific Rejections
------------------------------------------------------------------------------------------------------

### 

[​](https://docs.kalshi.com/fix/error-handling#order-reject-reasons-103)

Order Reject Reasons (103)

In ExecutionReport (35=8) with ExecType=Rejected:

| Code | Reason | Common Causes |
| --- | --- | --- |
| 1   | Unknown symbol | Invalid market ticker |
| 2   | Exchange closed | Outside trading hours |
| 3   | Order exceeds limit | Position or order size limit |
| 4   | Too late to enter | Market expired/closed |
| 6   | Duplicate order | ClOrdID already used |
| 11  | Unsupported order characteristic | Invalid order parameters |
| 99  | Other | See Text field |

### 

[​](https://docs.kalshi.com/fix/error-handling#cancel-reject-reasons-102)

Cancel Reject Reasons (102)

In OrderCancelReject (35=9):

| Code | Reason | Description |
| --- | --- | --- |
| 0   | Too late to cancel | Order already filled |
| 1   | Unknown order | Order ID not found |
| 99  | Other | See Text field |

[​](https://docs.kalshi.com/fix/error-handling#common-error-scenarios)

Common Error Scenarios
------------------------------------------------------------------------------------------------

### 

[​](https://docs.kalshi.com/fix/error-handling#example-1%3A-invalid-tag)

Example 1: Invalid Tag

**Scenario**: Undefined tag in NewOrderSingle

Copy

Ask AI

    // Sent
    8=FIXT.1.1|35=D|11=123|38=10|333333=test|...
    
    // Response: Reject
    8=FIXT.1.1|35=3|45=5|58=Undefined tag received|371=333333|372=D|373=3|
    

### 

[​](https://docs.kalshi.com/fix/error-handling#example-2%3A-business-logic-error)

Example 2: Business Logic Error

**Scenario**: Trading during maintenance

Copy

Ask AI

    // Sent
    8=FIXT.1.1|35=D|11=456|38=10|55=HIGHNY-23DEC31|...
    
    // Response: BusinessMessageReject
    8=FIXT.1.1|35=j|45=10|58=Kalshi exchange unavailable|372=D|380=4|
    

### 

[​](https://docs.kalshi.com/fix/error-handling#example-3%3A-order-rejection)

Example 3: Order Rejection

**Scenario**: Insufficient funds

Copy

Ask AI

    // Response: ExecutionReport
    8=FIXT.1.1|35=8|11=789|150=8|39=8|58=Insufficient funds|103=99|...
    

[​](https://docs.kalshi.com/fix/error-handling#error-handling-best-practices)

Error Handling Best Practices
--------------------------------------------------------------------------------------------------------------

### 

[​](https://docs.kalshi.com/fix/error-handling#1-comprehensive-logging)

1\. Comprehensive Logging

Copy

Ask AI

    def handle_message(msg):
        if msg.type == 'Reject':
            log.error(f"Session reject: {msg.Text} (Tag: {msg.RefTagID}, Reason: {msg.SessionRejectReason})")
        elif msg.type == 'BusinessMessageReject':
            log.error(f"Business reject: {msg.Text} (Reason: {msg.BusinessRejectReason})")
        elif msg.type == 'ExecutionReport' and msg.ExecType == 'Rejected':
            log.error(f"Order rejected: {msg.Text} (Reason: {msg.OrdRejReason})")
    

### 

[​](https://docs.kalshi.com/fix/error-handling#2-retry-strategies)

2\. Retry Strategies

| Error Type | Retry Strategy |
| --- | --- |
| Session errors | Fix protocol issue before retry |
| Rate limit | Exponential backoff |
| Exchange closed | Wait for market open |
| Insufficient funds | Check balance before retry |
| Unknown symbol | Verify symbol, don’t retry |

### 

[​](https://docs.kalshi.com/fix/error-handling#3-graceful-degradation)

3\. Graceful Degradation

1

Identify Error Type

Distinguish between recoverable and non-recoverable errors

2

Apply Appropriate Action

*   Recoverable: Implement retry with backoff
*   Non-recoverable: Alert and halt

3

Monitor and Alert

Track error rates and patterns for system health

[​](https://docs.kalshi.com/fix/error-handling#specific-error-conditions)

Specific Error Conditions
------------------------------------------------------------------------------------------------------

### 

[​](https://docs.kalshi.com/fix/error-handling#authentication-errors)

Authentication Errors

| Symptom | Likely Cause | Resolution |
| --- | --- | --- |
| Logon rejected | Invalid signature | Check RSA key and signature algorithm |
| CompID problem | Wrong API key | Verify SenderCompID matches API key |
| Time accuracy | Clock skew | Sync system time with NTP |

### 

[​](https://docs.kalshi.com/fix/error-handling#order-entry-errors)

Order Entry Errors

| Error | Check | Action |
| --- | --- | --- |
| Unknown symbol | Symbol format | Use exact ticker from market data |
| Order exceeds limit | Position limits | Query current position |
| Duplicate ClOrdID | ID generation | Ensure UUID uniqueness |
| Invalid price | Price range | Ensure (0, 100) cents with valid tick interval |

### 

[​](https://docs.kalshi.com/fix/error-handling#connection-errors)

Connection Errors

Connection errors often manifest as:

*   Heartbeat timeout
*   Sequence number gaps
*   Socket disconnection

Always implement reconnection logic with appropriate delays.

[​](https://docs.kalshi.com/fix/error-handling#error-response-patterns)

Error Response Patterns
--------------------------------------------------------------------------------------------------

### 

[​](https://docs.kalshi.com/fix/error-handling#synchronous-errors)

Synchronous Errors

Immediate response to invalid request:

Copy

Ask AI

    Request → Validation → Immediate Error Response
    

### 

[​](https://docs.kalshi.com/fix/error-handling#asynchronous-errors)

Asynchronous Errors

Delayed errors during processing:

Copy

Ask AI

    Request → Initial Accept → Processing → Later Error Report
    

[Market Settlement](https://docs.kalshi.com/fix/market-settlement)
[Subpenny Pricing](https://docs.kalshi.com/fix/subpenny-pricing)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.