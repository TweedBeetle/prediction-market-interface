---
url: https://docs.polymarket.com/developers/RTDS/RTDS-overview
title: Real Time Data Socket - Polymarket Documentation
scraped_at: 2025-11-03T15:04:06.772948
---

[Skip to main content](https://docs.polymarket.com/developers/RTDS/RTDS-overview#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

Ctrl K

Search...

Navigation

Real Time Data Stream

Real Time Data Socket

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

On this page

*   [Overview](https://docs.polymarket.com/developers/RTDS/RTDS-overview#overview)
    
*   [Connection Details](https://docs.polymarket.com/developers/RTDS/RTDS-overview#connection-details)
    
*   [Authentication](https://docs.polymarket.com/developers/RTDS/RTDS-overview#authentication)
    
*   [Connection Management](https://docs.polymarket.com/developers/RTDS/RTDS-overview#connection-management)
    
*   [Available Subscription Types](https://docs.polymarket.com/developers/RTDS/RTDS-overview#available-subscription-types)
    
*   [Message Structure](https://docs.polymarket.com/developers/RTDS/RTDS-overview#message-structure)
    
*   [Subscription Management](https://docs.polymarket.com/developers/RTDS/RTDS-overview#subscription-management)
    
*   [Subscribe to Topics](https://docs.polymarket.com/developers/RTDS/RTDS-overview#subscribe-to-topics)
    
*   [Unsubscribe from Topics](https://docs.polymarket.com/developers/RTDS/RTDS-overview#unsubscribe-from-topics)
    
*   [Error Handling](https://docs.polymarket.com/developers/RTDS/RTDS-overview#error-handling)
    

[​](https://docs.polymarket.com/developers/RTDS/RTDS-overview#overview)

Overview
-----------------------------------------------------------------------------------

The Polymarket Real-Time Data Socket (RTDS) is a WebSocket-based streaming service that provides real-time updates for various Polymarket data streams. The service allows clients to subscribe to multiple data feeds simultaneously and receive live updates as events occur on the platform.

Polymarket provides a Typescript client for interacting with this streaming service. [Download and view it’s documentation here](https://github.com/Polymarket/real-time-data-client)

### 

[​](https://docs.polymarket.com/developers/RTDS/RTDS-overview#connection-details)

Connection Details

*   **WebSocket URL**: `wss://ws-live-data.polymarket.com`
*   **Protocol**: WebSocket
*   **Data Format**: JSON

### 

[​](https://docs.polymarket.com/developers/RTDS/RTDS-overview#authentication)

Authentication

The RTDS supports two types of authentication depending on the subscription type:

1.  **CLOB Authentication**: Required for certain trading-related subscriptions
    *   `key`: API key
    *   `secret`: API secret
    *   `passphrase`: API passphrase
2.  **Gamma Authentication**: Required for user-specific data
    *   `address`: User wallet address

### 

[​](https://docs.polymarket.com/developers/RTDS/RTDS-overview#connection-management)

Connection Management

The WebSocket connection supports:

*   **Dynamic Subscriptions**: Without disconnecting from the socket users can add, remove and modify topics and filters they are subscribed to.
*   **Ping/Pong**: You should send PING messages (every 5 seconds ideally) to maintain connection

[​](https://docs.polymarket.com/developers/RTDS/RTDS-overview#available-subscription-types)

Available Subscription Types
---------------------------------------------------------------------------------------------------------------------------

Although this connection technically supports additional activity and subscription types, they are not fully supported at this time. Users are free to use them but there may be some unexpected behavior.

The RTDS currently supports the following subscription types:

1.  **[Crypto Prices](https://docs.polymarket.com/developers/RTDS/RTDS-crypto-prices)
    ** - Real-time cryptocurrency price updates
2.  **[Comments](https://docs.polymarket.com/developers/RTDS/RTDS-comments)
    ** - Comment-related events including reactions

[​](https://docs.polymarket.com/developers/RTDS/RTDS-overview#message-structure)

Message Structure
-----------------------------------------------------------------------------------------------------

All messages received from the WebSocket follow this structure:

Copy

Ask AI

    {
      "topic": "string",
      "type": "string", 
      "timestamp": "number",
      "payload": "object"
    }
    

*   `topic`: The subscription topic (e.g., “crypto\_prices”, “comments”, “activity”)
*   `type`: The message type/event (e.g., “update”, “reaction\_created”, “orders\_matched”)
*   `timestamp`: Unix timestamp in milliseconds
*   `payload`: Event-specific data object

[​](https://docs.polymarket.com/developers/RTDS/RTDS-overview#subscription-management)

Subscription Management
-----------------------------------------------------------------------------------------------------------------

### 

[​](https://docs.polymarket.com/developers/RTDS/RTDS-overview#subscribe-to-topics)

Subscribe to Topics

To subscribe to data streams, send a JSON message with this structure:

Copy

Ask AI

    {
      "action": "subscribe",
      "subscriptions": [\
        {\
          "topic": "topic_name",\
          "type": "message_type",\
          "filters": "optional_filter_string",\
          "clob_auth": {\
            "key": "api_key",\
            "secret": "api_secret", \
            "passphrase": "api_passphrase"\
          },\
          "gamma_auth": {\
            "address": "wallet_address"\
          }\
        }\
      ]
    }
    

### 

[​](https://docs.polymarket.com/developers/RTDS/RTDS-overview#unsubscribe-from-topics)

Unsubscribe from Topics

To unsubscribe from data streams, send a similar message with `"action": "unsubscribe"`.

[​](https://docs.polymarket.com/developers/RTDS/RTDS-overview#error-handling)

Error Handling
-----------------------------------------------------------------------------------------------

*   Connection errors will trigger automatic reconnection attempts
*   Invalid subscription messages may result in connection closure
*   Authentication failures will prevent successful subscription to protected topics

[Market Channel](https://docs.polymarket.com/developers/CLOB/websocket/market-channel)
[RTDS Crypto Prices](https://docs.polymarket.com/developers/RTDS/RTDS-crypto-prices)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.