---
url: https://docs.kalshi.com/fix
title: FIX API Overview - API Documentation
description: Financial Information eXchange (FIX) protocol implementation for Kalshi
scraped_at: 2025-11-03T14:46:33.491137
---

[Skip to main content](https://docs.kalshi.com/fix#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

FIX API Overview

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

On this page

*   [Kalshi FIX API Specifications](https://docs.kalshi.com/fix#kalshi-fix-api-specifications)
    
*   [Introduction](https://docs.kalshi.com/fix#introduction)
    
*   [Key Features](https://docs.kalshi.com/fix#key-features)
    
*   [Getting Started](https://docs.kalshi.com/fix#getting-started)
    
*   [Support](https://docs.kalshi.com/fix#support)
    

[​](https://docs.kalshi.com/fix#kalshi-fix-api-specifications)

Kalshi FIX API Specifications
===============================================================================================

**Version**: 1.0.13 **Last Updated**: 2025-10-01

[​](https://docs.kalshi.com/fix#introduction)

Introduction
-------------------------------------------------------------

FIX (Financial Information eXchange) is a standard protocol that can be used to enter orders, submit cancel requests, and receive fills. Kalshi’s implementation follows the standards as closely as possible, with any divergences highlighted in this documentation. Please contact [institutional@kalshi.com](mailto:institutional@kalshi.com)
 to inquire about FIX access.

[​](https://docs.kalshi.com/fix#key-features)

Key Features
-------------------------------------------------------------

[Session Management\
------------------\
\
Logon, logout, heartbeat, and session control messages](https://docs.kalshi.com/fix/session-management)
[Order Entry\
-----------\
\
Submit, modify, and cancel orders through standard FIX messages](https://docs.kalshi.com/fix/order-entry)
[Market Settlement\
-----------------\
\
Market settlement and payout updates](https://docs.kalshi.com/fix/market-settlement)
[RFQ Support\
-----------\
\
Request for Quote functionality for market makers](https://docs.kalshi.com/fix/rfq-messages)
[Drop Copy\
---------\
\
Separate session for order event recovery](https://docs.kalshi.com/fix/drop-copy)
[Order Groups\
------------\
\
Automatic order cancellation with contracts limits](https://docs.kalshi.com/fix/order-groups)

[​](https://docs.kalshi.com/fix#getting-started)

Getting Started
-------------------------------------------------------------------

1

Generate RSA Keys

Create a 2048 bit RSA PKCS#8 key pair for authentication

2

Create API Key

Upload your public key to the Kalshi platform to receive your FIX API key

3

Configure Connection

Set up your FIX client with the appropriate endpoints and credentials

4

Start Trading

Send a Logon message and begin submitting orders

[​](https://docs.kalshi.com/fix#support)

Support
---------------------------------------------------

For technical support or questions about the FIX API, please contact the Kalshi trading support team.

[Connectivity](https://docs.kalshi.com/fix/connectivity)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.