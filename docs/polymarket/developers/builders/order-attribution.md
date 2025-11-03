---
url: https://docs.polymarket.com/developers/builders/order-attribution
title: Order Attribution - Polymarket Documentation
description: Learn how to attribute customer orders to your builder account using authentication headers
scraped_at: 2025-11-03T15:04:07.758579
---

[Skip to main content](https://docs.polymarket.com/developers/builders/order-attribution#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

Ctrl K

Search...

Navigation

Polymarket Builders Program

Order Attribution

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

On this page

*   [Overview](https://docs.polymarket.com/developers/builders/order-attribution#overview)
    
*   [Builder API Credentials](https://docs.polymarket.com/developers/builders/order-attribution#builder-api-credentials)
    
*   [Signing Methods](https://docs.polymarket.com/developers/builders/order-attribution#signing-methods)
    
*   [Remote Signing (Recommended)](https://docs.polymarket.com/developers/builders/order-attribution#remote-signing-recommended)
    
*   [Local Signing](https://docs.polymarket.com/developers/builders/order-attribution#local-signing)
    
*   [Authentication Headers](https://docs.polymarket.com/developers/builders/order-attribution#authentication-headers)
    
*   [Using Our SDKs](https://docs.polymarket.com/developers/builders/order-attribution#using-our-sdks)
    
*   [Next Steps](https://docs.polymarket.com/developers/builders/order-attribution#next-steps)
    

[​](https://docs.polymarket.com/developers/builders/order-attribution#overview)

Overview
-------------------------------------------------------------------------------------------

The order attribution system allows builders to attach custom headers to their customer orders before posting them to the CLOB. These additional headers enable Polymarket to attribute orders to your specific builder account, providing visibility into which orders originate from your platform.

[​](https://docs.polymarket.com/developers/builders/order-attribution#builder-api-credentials)

Builder API Credentials
-------------------------------------------------------------------------------------------------------------------------

Each builder will receive Builder API Key Credentials that look like this:

Copy

Ask AI

    interface BuilderApiKeyCreds {
        key: string;
        secret: string;
        passphrase: string;
    }
    
    // Example structure
    const builderCreds = {
        key: "xxxxx.....",
        secret: "xxxxx.....",
        passphrase: "xxxxx....."
    };
    

**Security Notice**: Your Builder API keys must be kept secure. We provide both local and remote signing methods to help you protect these credentials.

[​](https://docs.polymarket.com/developers/builders/order-attribution#signing-methods)

Signing Methods
---------------------------------------------------------------------------------------------------------

There are two methods available for signing orders and adding attribution headers: **Remote Signing** and **Local Signing**.

### 

[​](https://docs.polymarket.com/developers/builders/order-attribution#remote-signing-recommended)

Remote Signing (Recommended)

Remote signing is the recommended approach for protecting your Builder API credentials. With this method, your credentials never leave your secure server. **How it works:**

1.  Your customer signs an order payload (ready to be sent to the CLOB)
2.  Instead of sending directly to the CLOB, the signed payload is sent to your builder signing server
3.  Your builder signing server uses your Builder API keys to cryptographically sign the entire payload and adds the authentication headers
4.  The fully signed payload (signed by both your customer and you as the builder) is then sent to the CLOB

**Implementation:** We provide a complete server implementation in the [@polymarket/builder-signing-server](https://github.com/Polymarket/builder-signing-server)
 repository.

Copy

Ask AI

    import { ClobClient } from "@polymarket/clob-client";
    import { BuilderConfig } from "@polymarket/builder-signing-sdk";
    
    // Basic remote signing configuration
    const builderConfig = new BuilderConfig({
        remoteBuilderConfig: {url: "http://localhost:3000/sign"}
    });
    
    // Or with optional authorization token for added security
    const builderConfigWithAuth = new BuilderConfig({
        remoteBuilderConfig: {url: "http://localhost:3000/sign", token: "XXXX-XXXX-XXXX"}
    });
    
    const clobClient = new ClobClient(
        host,
        chainId,
        wallet,
        creds,
        SignatureType.POLY_PROXY,
        funderAddress,
        undefined,
        false,
        builderConfig // or builderConfigWithAuth
    );
    
    // Create and post order - headers are added automatically
    const order = await clobClient.createOrder({
        price: 0.40,
        side: Side.BUY,
        size: 5,
        tokenID: "27072675915285915455116137912884489109876947142577610372904917850067886308458"
    });
    
    const response = await clobClient.postOrder(order);
    

**Remote Builder Configuration:**

Copy

Ask AI

    interface RemoteBuilderConfig {
        url: string;              // URL of your signing server
        token?: string;           // Optional authorization token
    }
    

The optional `token` parameter allows you to add an authorization header to requests sent to your signing server, providing an additional layer of security.

### 

[​](https://docs.polymarket.com/developers/builders/order-attribution#local-signing)

Local Signing

If you control the entire order placement flow (including signing for your customers), you can sign orders locally before sending them to the CLOB. **How it works:**

1.  Your system creates and signs the order on behalf of your customer
2.  Your system uses your Builder API credentials locally to add authentication headers
3.  The complete signed order with builder headers is sent directly to the CLOB

**Implementation:**

Copy

Ask AI

    import { ClobClient } from "@polymarket/clob-client";
    import { BuilderConfig, BuilderApiKeyCreds } from "@polymarket/builder-signing-sdk";
    
    // Configure with local builder credentials
    const builderCreds: BuilderApiKeyCreds = {
        key: process.env.POLY_BUILDER_API_KEY!,
        secret: process.env.POLY_BUILDER_SECRET!,
        passphrase: process.env.POLY_BUILDER_PASSPHRASE!
    };
    
    const builderConfig: BuilderConfig = {
        localBuilderCreds: builderCreds
    };
    
    const clobClient = new ClobClient(
        host,
        chainId,
        wallet,
        creds,
        SignatureType.POLY_PROXY,
        funderAddress,
        undefined,
        false,
        builderConfig
    );
    
    // Create and post order - headers are added automatically
    const order = await clobClient.createOrder({
        price: 0.40,
        side: Side.BUY,
        size: 5,
        tokenID: "27072675915285915455116137912884489109876947142577610372904917850067886308458"
    });
    
    const response = await clobClient.postOrder(order);
    

[​](https://docs.polymarket.com/developers/builders/order-attribution#authentication-headers)

Authentication Headers
-----------------------------------------------------------------------------------------------------------------------

The builder signing process adds the following headers to each order request:

*   `POLY_BUILDER_API_KEY`: Your builder API key
*   `POLY_BUILDER_TIMESTAMP`: Unix timestamp of when the signature was created
*   `POLY_BUILDER_PASSPHRASE`: Your builder passphrase
*   `POLY_BUILDER_SIGNATURE`: HMAC signature of the request

These headers are automatically generated and attached by the SDK - you don’t need to construct them manually.

[​](https://docs.polymarket.com/developers/builders/order-attribution#using-our-sdks)

Using Our SDKs
-------------------------------------------------------------------------------------------------------

**Important**: We strongly recommend using our official SDKs and server implementations. You **do not** need to implement the signing logic yourself.

We provide the following packages to handle all signing and header injection:

*   **[@polymarket/builder-signing-sdk](https://github.com/Polymarket/builder-signing-sdk)
    **: Core signing functionality
*   **[@polymarket/builder-signing-server](https://github.com/Polymarket/builder-signing-server)
    **: Production-ready remote signing server
*   **[@polymarket/clob-client](https://github.com/Polymarket/clob-client)
    **: Updated CLOB client with built-in builder support

All examples in this documentation use these official packages to ensure security and reliability.

[​](https://docs.polymarket.com/developers/builders/order-attribution#next-steps)

Next Steps
-----------------------------------------------------------------------------------------------

*   Set up your [builder signing server](https://github.com/Polymarket/builder-signing-server)
     for remote signing
*   Review the [complete examples](https://github.com/Polymarket/clob-client/tree/main/examples)
     in the CLOB client repository
*   Contact [support@polymarket.com](mailto:support@polymarket.com)
     if you need assistance

[Builder Program Introduction](https://docs.polymarket.com/developers/builders/builder-intro)
[Builder Signing Server](https://docs.polymarket.com/developers/builders/builder-signing-server)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.