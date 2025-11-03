---
url: https://docs.kalshi.com/fix/session-management
title: Session Management - API Documentation
description: Managing FIX sessions including logon, logout, and message sequencing
scraped_at: 2025-11-03T14:46:35.755858
---

[Skip to main content](https://docs.kalshi.com/fix/session-management#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

Session Management

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

On this page

*   [Session Management](https://docs.kalshi.com/fix/session-management#session-management)
    
*   [Creating FIX API Keys](https://docs.kalshi.com/fix/session-management#creating-fix-api-keys)
    
*   [Generate RSA Key Pair](https://docs.kalshi.com/fix/session-management#generate-rsa-key-pair)
    
*   [Create API Key](https://docs.kalshi.com/fix/session-management#create-api-key)
    
*   [Logon Process](https://docs.kalshi.com/fix/session-management#logon-process)
    
*   [Logon Message (35=A)](https://docs.kalshi.com/fix/session-management#logon-message-35%3Da)
    
*   [Required Fields](https://docs.kalshi.com/fix/session-management#required-fields)
    
*   [Optional Fields](https://docs.kalshi.com/fix/session-management#optional-fields)
    
*   [Signature Generation](https://docs.kalshi.com/fix/session-management#signature-generation)
    
*   [Session Maintenance](https://docs.kalshi.com/fix/session-management#session-maintenance)
    
*   [Heartbeat Protocol](https://docs.kalshi.com/fix/session-management#heartbeat-protocol)
    
*   [Message Sequence Numbers](https://docs.kalshi.com/fix/session-management#message-sequence-numbers)
    
*   [Sequence Number Rules](https://docs.kalshi.com/fix/session-management#sequence-number-rules)
    
*   [Reconnection Procedure](https://docs.kalshi.com/fix/session-management#reconnection-procedure)
    
*   [ResendRequest (35=2)](https://docs.kalshi.com/fix/session-management#resendrequest-35%3D2)
    
*   [Limitations](https://docs.kalshi.com/fix/session-management#limitations)
    
*   [Error Handling](https://docs.kalshi.com/fix/session-management#error-handling)
    
*   [Reject (35=3)](https://docs.kalshi.com/fix/session-management#reject-35%3D3)
    
*   [BusinessMessageReject (35=j)](https://docs.kalshi.com/fix/session-management#businessmessagereject-35%3Dj)
    
*   [Session Termination](https://docs.kalshi.com/fix/session-management#session-termination)
    
*   [Logout (35=5)](https://docs.kalshi.com/fix/session-management#logout-35%3D5)
    
*   [Message Headers](https://docs.kalshi.com/fix/session-management#message-headers)
    
*   [Message Trailers](https://docs.kalshi.com/fix/session-management#message-trailers)
    
*   [Best Practices](https://docs.kalshi.com/fix/session-management#best-practices)
    

[​](https://docs.kalshi.com/fix/session-management#session-management)

Session Management
============================================================================================

[​](https://docs.kalshi.com/fix/session-management#creating-fix-api-keys)

Creating FIX API Keys
--------------------------------------------------------------------------------------------------

### 

[​](https://docs.kalshi.com/fix/session-management#generate-rsa-key-pair)

Generate RSA Key Pair

First, generate a 2048 bit RSA PKCS#8 key pair:

Copy

Ask AI

    openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:2048 -out kalshi-fix.key
    openssl rsa -in kalshi-fix.key -pubout -out kalshi-fix.pub
    

This creates two files:

*   **kalshi-fix.key**: Your private key (keep secure, never share)
*   **kalshi-fix.pub**: Your public key (share with Kalshi)

### 

[​](https://docs.kalshi.com/fix/session-management#create-api-key)

Create API Key

1.  Navigate to [https://demo.kalshi.co/account/profile](https://demo.kalshi.co/account/profile)
    
2.  Click the “Create key” button
3.  Name your API Key
4.  Copy and paste the contents of `kalshi-fix.pub` into the “RSA public key” field
5.  Click “Create”
6.  Copy the generated FIX API Key (UUID format)

Store your private key securely. It is equivalent to your username + password and should never be sent to anyone, including Kalshi employees.

[​](https://docs.kalshi.com/fix/session-management#logon-process)

Logon Process
----------------------------------------------------------------------------------

### 

[​](https://docs.kalshi.com/fix/session-management#logon-message-35%3Da)

Logon Message (35=A)

The initiator must send a Logon message to establish a session. The acceptor will either:

*   Respond with a Logon message acknowledging successful logon
*   Respond with a Logout (35=5) message if the logon fails

### 

[​](https://docs.kalshi.com/fix/session-management#required-fields)

Required Fields

| Tag | Name | Description | Value |
| --- | --- | --- | --- |
| 98  | EncryptMethod | Method of encryption | None<0> |
| 96  | RawData | Client logon message signature | Base64 encoded signature |
| 1137 | DefaultApplVerID | Default application version | FIX50SP2<9> |

### 

[​](https://docs.kalshi.com/fix/session-management#optional-fields)

Optional Fields

| Tag | Name | Description | Default |
| --- | --- | --- | --- |
| 108 | HeartbeatInt | Heartbeat <0> interval (seconds) | 30  |
| 8013 | CancelOrdersOnDisconnect | Cancel orders on any disconnection (including graceful logout) | N   |
| 20126 | ListenerSession | Listen-only session (KalshiNR/RT only, requires SkipPendingExecReports=Y) | N   |
| 20127 | ReceiveSettlementReports | Receive settlement reports (KalshiRT only) | N   |
| 20200 | MessageRetentionPeriod | How long session messages will be store for retransmission (KalshiRT and KalshiRFQ only) | 3   |
| 21003 | SkipPendingExecReports | Skip PENDING\_{NEW\|REPLACE\|CANCEL} execution reports | N   |

### 

[​](https://docs.kalshi.com/fix/session-management#signature-generation)

Signature Generation

The RawData field must contain a PSS RSA signature of the pre-hash string:

Copy

Ask AI

    PreHashString = SendingTime + SOH + MsgType + SOH + MsgSeqNum + SOH + SenderCompID + SOH + TargetCompID
    

Python

Copy

Ask AI

    from base64 import b64encode
    from Cryptodome.Signature import pss
    from Cryptodome.Hash import SHA256
    from Cryptodome.PublicKey import RSA
    
    # Load private key
    private_key = RSA.import_key(open('kalshi-fix.key').read().encode('utf-8'))
    
    # Build message string
    sending_time = "20230809-05:28:18.035"
    msg_type = "A"
    msg_seq_num = "1"
    sender_comp_id = "your-fix-api-key-uuid"
    target_comp_id = "Kalshi"  # Or appropriate TargetCompID
    
    msg_string = chr(1).join([\
        sending_time, msg_type, msg_seq_num,\
        sender_comp_id, target_comp_id\
    ])
    
    # Generate signature
    msg_hash = SHA256.new(msg_string.encode('utf-8'))
    signature = pss.new(private_key).sign(msg_hash)
    raw_data_value = b64encode(signature).decode('utf-8')
    

[​](https://docs.kalshi.com/fix/session-management#session-maintenance)

Session Maintenance
----------------------------------------------------------------------------------------------

### 

[​](https://docs.kalshi.com/fix/session-management#heartbeat-protocol)

Heartbeat Protocol

*   Default interval: 30 seconds
*   Both sides must respond to TestRequest messages
*   Connection terminates if heartbeat response not received within interval

### 

[​](https://docs.kalshi.com/fix/session-management#message-sequence-numbers)

Message Sequence Numbers

#### 

[​](https://docs.kalshi.com/fix/session-management#sequence-number-rules)

Sequence Number Rules

1.  Must be unique and increase by one for each message
2.  Empty MsgSeqNum results in session termination
3.  Lower than expected = serious failure, connection terminated
4.  Higher than expected = recoverable with ResendRequest (if supported)

### 

[​](https://docs.kalshi.com/fix/session-management#reconnection-procedure)

Reconnection Procedure

For unexpected sequence numbers:

1.  Document the issue with logs for out-of-band communication
2.  Check order status via REST API or UI
3.  Establish new session with reset sequence numbers

[​](https://docs.kalshi.com/fix/session-management#resendrequest-35%3D2)

ResendRequest (35=2)
------------------------------------------------------------------------------------------------

Only available on Order Entry with Retransmission (KalshiRT) sessions.

### 

[​](https://docs.kalshi.com/fix/session-management#limitations)

Limitations

*   Lookback window limited to 3 hours (or up to 24 hours if MessageRetentionPeriod was set on Logon request)
*   If you provide a BeginSeqNo that is beyond the lookback window, you will receive a Reject message

| Tag | Name | Description |
| --- | --- | --- |
| 7   | BeginSeqNo | Lower bound (inclusive) |
| 16  | EndSeqNo | Upper bound (inclusive) |

[​](https://docs.kalshi.com/fix/session-management#error-handling)

Error Handling
------------------------------------------------------------------------------------

### 

[​](https://docs.kalshi.com/fix/session-management#reject-35%3D3)

Reject (35=3)

Sent when a message cannot be processed due to session-level rule violations.

| Tag | Name | Description | Required |
| --- | --- | --- | --- |
| 45  | RefSeqNum | Sequence number of rejected message | Yes |
| 58  | Text | Human-readable error description | No  |
| 371 | RefTagID | Tag number that caused reject | No  |
| 372 | RefMsgType | MsgType of referenced message | No  |
| 373 | SessionRejectReason | Rejection reason code | No  |

Reject indicates serious errors that may result from faulty logic. Log and investigate these errors.

### 

[​](https://docs.kalshi.com/fix/session-management#businessmessagereject-35%3Dj)

BusinessMessageReject (35=j)

Sent for business logic violations rather than session-level errors.

| Tag | Name | Description | Required |
| --- | --- | --- | --- |
| 45  | RefSeqNum | Sequence number of rejected message | Yes |
| 58  | Text | Human-readable error description | No  |
| 371 | RefTagID | Tag number that caused reject | No  |
| 372 | RefMsgType | MsgType of referenced message | No  |
| 379 | BusinessRejectRefID | Business-level ID of rejected message | No  |
| 380 | BusinessRejectReason | Business rejection reason code | Yes |

[​](https://docs.kalshi.com/fix/session-management#session-termination)

Session Termination
----------------------------------------------------------------------------------------------

### 

[​](https://docs.kalshi.com/fix/session-management#logout-35%3D5)

Logout (35=5)

Graceful session termination:

1.  Initiator sends Logout message
2.  Acceptor responds with Logout (empty Text field)
3.  Transport layer connection terminated

| Tag | Name | Description |
| --- | --- | --- |
| 58  | Text | Error description (if any) |

If `CancelOrdersOnDisconnect=Y`, all orders are canceled even on graceful logout.

[​](https://docs.kalshi.com/fix/session-management#message-headers)

Message Headers
--------------------------------------------------------------------------------------

All messages must include standard FIX headers:

| Tag | Name | Description | Requirements |
| --- | --- | --- | --- |
| 8   | BeginString | Protocol version | FIXT.1.1 (must be first) |
| 9   | BodyLength | Message length in bytes | Must be second |
| 34  | MsgSeqNum | Message sequence number | Unique, incrementing |
| 35  | MsgType | Message type | Must be third |
| 52  | SendingTime | UTC timestamp | Within 120 seconds of server time |
| 1137 | ApplVerID | Application version | Only FIX50SP2<9> is accepted |

### 

[​](https://docs.kalshi.com/fix/session-management#message-trailers)

Message Trailers

| Tag | Name | Description |     |
| --- | --- | --- | --- |
| 10  | CheckSum | Standard FIX checksum | Must be last field |

CheckSum is calculated by summing ASCII values of all characters (except checksum field) modulo 256.

[​](https://docs.kalshi.com/fix/session-management#best-practices)

Best Practices
------------------------------------------------------------------------------------

1.  **Session Configuration**
    *   Use unique ClOrdIDs across all message types
    *   Implement proper heartbeat handling
    *   Monitor sequence numbers carefully
2.  **Error Recovery**
    *   Implement automatic reconnection logic
    *   Store order state locally for recovery
    *   Use drop copy session for missed messages
3.  **Security**
    *   Rotate API keys periodically
    *   Monitor for unauthorized access
    *   Use secure storage for private keys

[Connectivity](https://docs.kalshi.com/fix/connectivity)
[Order Entry Messages](https://docs.kalshi.com/fix/order-entry)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.