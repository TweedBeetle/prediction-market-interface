---
url: https://docs.kalshi.com/fix/connectivity
title: Connectivity - API Documentation
description: Connection setup and endpoints for Kalshi FIX API
scraped_at: 2025-11-03T14:46:33.655251
---

[Skip to main content](https://docs.kalshi.com/fix/connectivity#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

Connectivity

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

On this page

*   [FIX API Connectivity](https://docs.kalshi.com/fix/connectivity#fix-api-connectivity)
    
*   [Endpoints](https://docs.kalshi.com/fix/connectivity#endpoints)
    
*   [Rate Limits](https://docs.kalshi.com/fix/connectivity#rate-limits)
    
*   [Order Entry Session](https://docs.kalshi.com/fix/connectivity#order-entry-session)
    
*   [TCP SSL Configuration](https://docs.kalshi.com/fix/connectivity#tcp-ssl-configuration)
    
*   [SSL/TLS Requirements](https://docs.kalshi.com/fix/connectivity#ssl%2Ftls-requirements)
    
*   [Message Retransmission](https://docs.kalshi.com/fix/connectivity#message-retransmission)
    
*   [Supported Endpoints](https://docs.kalshi.com/fix/connectivity#supported-endpoints)
    
*   [Unsupported Message Types](https://docs.kalshi.com/fix/connectivity#unsupported-message-types)
    
*   [Alternative Recovery](https://docs.kalshi.com/fix/connectivity#alternative-recovery)
    
*   [Session Configuration](https://docs.kalshi.com/fix/connectivity#session-configuration)
    
*   [Required Settings](https://docs.kalshi.com/fix/connectivity#required-settings)
    
*   [Session Identification](https://docs.kalshi.com/fix/connectivity#session-identification)
    
*   [Best Practices](https://docs.kalshi.com/fix/connectivity#best-practices)
    
*   [Troubleshooting](https://docs.kalshi.com/fix/connectivity#troubleshooting)
    
*   [Common Connection Issues](https://docs.kalshi.com/fix/connectivity#common-connection-issues)
    

[​](https://docs.kalshi.com/fix/connectivity#fix-api-connectivity)

FIX API Connectivity
==========================================================================================

[​](https://docs.kalshi.com/fix/connectivity#endpoints)

Endpoints
--------------------------------------------------------------------

Before logging onto a FIX session, clients must establish a secure connection to the FIX gateway.

*   Production
    
*   Demo
    

**Host:** `fix.elections.kalshi.com`

| Purpose | Port | TargetCompID |
| --- | --- | --- |
| Order Entry (without retransmission) | 8228 | KalshiNR |
| Order Entry (with retransmission) | 8230 | KalshiRT |
| Drop Copy | 8229 | KalshiDC |
| Post Trade | 8231 | KalshiPT |
| RFQ | 8232 | KalshiRFQ |

Sessions are potentially dropped during trading closed hours for maintenance. For now, this is on Thursdays from 3 AM to 5 AM ET. All users are required to restart their sessions during this time and reset sequence numbers to 0.

[​](https://docs.kalshi.com/fix/connectivity#rate-limits)

Rate Limits
------------------------------------------------------------------------

### 

[​](https://docs.kalshi.com/fix/connectivity#order-entry-session)

Order Entry Session

*   **Limit**: Your account-level rate limits are applicable
*   **Scope**: Application messages only (from client to server)
*   **Excluded**: Session layer messages

Session layer messages excluded from rate limits:

*   Logon (35=A)
*   Logout (35=5)
*   Heartbeat (35=0)
*   TestRequest (35=1)

[​](https://docs.kalshi.com/fix/connectivity#tcp-ssl-configuration)

TCP SSL Configuration
--------------------------------------------------------------------------------------------

### 

[​](https://docs.kalshi.com/fix/connectivity#ssl%2Ftls-requirements)

SSL/TLS Requirements

If your FIX implementation does not support establishing a native TCP SSL connection, you must set up a local proxy such as stunnel to establish a secure connection to our FIX gateway.

Kalshi will provide the certificate for pinning on the initiator side when providing your API key.

[​](https://docs.kalshi.com/fix/connectivity#message-retransmission)

Message Retransmission
----------------------------------------------------------------------------------------------

### 

[​](https://docs.kalshi.com/fix/connectivity#supported-endpoints)

Supported Endpoints

Message retransmission is currently only supported on:

*   Order Entry with retransmission (KalshiRT)
*   RFQ session (KalshiRFQ)

### 

[​](https://docs.kalshi.com/fix/connectivity#unsupported-message-types)

Unsupported Message Types

For endpoints without retransmission support:

*   ResendRequest (35=2) - Not supported
*   SequenceReset (35=4) - Not supported

For sessions without retransmission support, `ResetSeqNumFlag&lt;141&gt;` in the Logon message must always be `true` or the Logon will be rejected.

### 

[​](https://docs.kalshi.com/fix/connectivity#alternative-recovery)

Alternative Recovery

The drop copy session endpoint provides an alternative way for clients to query for missed execution reports without using the retransmission protocol.

[​](https://docs.kalshi.com/fix/connectivity#session-configuration)

Session Configuration
--------------------------------------------------------------------------------------------

### 

[​](https://docs.kalshi.com/fix/connectivity#required-settings)

Required Settings

*   **Session Profile**: FIXT.1.1 (required for Application Version Independence)
*   **Application Version**: FIX50SP2 (FIX 5.0 SP2)
*   **SenderCompID**: Your FIX API Key (UUID format)
*   **TargetCompID**: See endpoints table above

### 

[​](https://docs.kalshi.com/fix/connectivity#session-identification)

Session Identification

*   Session identification uses: `SessionID = TargetCompID + SenderCompID`
*   Only one FIX connection is allowed per FIX API Key

Each API key can only be used for a single connection at a time. If you need to establish multiple concurrent connections (e.g., for both order entry and drop copy), you must create separate API keys for each connection.

[​](https://docs.kalshi.com/fix/connectivity#best-practices)

Best Practices
------------------------------------------------------------------------------

1.  **Connection Management**
    *   Implement automatic reconnection logic for the daily maintenance window
    *   Monitor heartbeat intervals (default 30 seconds)
    *   Handle connection drops gracefully
2.  **Sequence Number Management**
    *   Reset sequence numbers to 0 after daily maintenance
    *   For non-retransmission endpoints, always use `ResetSeqNumFlag=Y`
3.  **Security**
    *   Store private keys securely
    *   Never share private keys, even with Kalshi employees
    *   Use certificate pinning when provided

[​](https://docs.kalshi.com/fix/connectivity#troubleshooting)

Troubleshooting
--------------------------------------------------------------------------------

### 

[​](https://docs.kalshi.com/fix/connectivity#common-connection-issues)

Common Connection Issues

SSL/TLS Connection Failed

*   Verify certificate configuration
*   Check if stunnel or similar proxy is needed

Logon Rejected

*   Verify SenderCompID matches your FIX API key
*   Check TargetCompID matches the port number
*   Ensure ResetSeqNumFlag is set correctly for non-retransmission endpoints

[FIX API Overview](https://docs.kalshi.com/fix)
[Session Management](https://docs.kalshi.com/fix/session-management)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.