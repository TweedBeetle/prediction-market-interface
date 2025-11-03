---
url: https://docs.polymarket.com/developers/builders/builder-signing-server
title: Builder Signing Server - Polymarket Documentation
description: Self-hosted server for secure remote signing of builder authentication headers
scraped_at: 2025-11-03T15:04:07.757209
---

[Skip to main content](https://docs.polymarket.com/developers/builders/builder-signing-server#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

Ctrl K

Search...

Navigation

Polymarket Builders Program

Builder Signing Server

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

On this page

*   [Overview](https://docs.polymarket.com/developers/builders/builder-signing-server#overview)
    
*   [Why Use Remote Signing?](https://docs.polymarket.com/developers/builders/builder-signing-server#why-use-remote-signing%3F)
    
*   [Installation](https://docs.polymarket.com/developers/builders/builder-signing-server#installation)
    
*   [Prerequisites](https://docs.polymarket.com/developers/builders/builder-signing-server#prerequisites)
    
*   [Clone and Install](https://docs.polymarket.com/developers/builders/builder-signing-server#clone-and-install)
    
*   [Configuration](https://docs.polymarket.com/developers/builders/builder-signing-server#configuration)
    
*   [Environment Variables](https://docs.polymarket.com/developers/builders/builder-signing-server#environment-variables)
    
*   [Port Configuration](https://docs.polymarket.com/developers/builders/builder-signing-server#port-configuration)
    
*   [Running the Server](https://docs.polymarket.com/developers/builders/builder-signing-server#running-the-server)
    
*   [Development Mode](https://docs.polymarket.com/developers/builders/builder-signing-server#development-mode)
    
*   [Production Mode](https://docs.polymarket.com/developers/builders/builder-signing-server#production-mode)
    
*   [Client Integration](https://docs.polymarket.com/developers/builders/builder-signing-server#client-integration)
    
*   [With CLOB Client](https://docs.polymarket.com/developers/builders/builder-signing-server#with-clob-client)
    
*   [With Relayer Client](https://docs.polymarket.com/developers/builders/builder-signing-server#with-relayer-client)
    
*   [Production Deployment](https://docs.polymarket.com/developers/builders/builder-signing-server#production-deployment)
    
*   [Troubleshooting](https://docs.polymarket.com/developers/builders/builder-signing-server#troubleshooting)
    
*   [Server Won’t Start](https://docs.polymarket.com/developers/builders/builder-signing-server#server-won%E2%80%99t-start)
    
*   [Port Already in Use](https://docs.polymarket.com/developers/builders/builder-signing-server#port-already-in-use)
    
*   [Invalid Signature Errors](https://docs.polymarket.com/developers/builders/builder-signing-server#invalid-signature-errors)
    
*   [Source Code](https://docs.polymarket.com/developers/builders/builder-signing-server#source-code)
    
*   [Support](https://docs.polymarket.com/developers/builders/builder-signing-server#support)
    

[​](https://docs.polymarket.com/developers/builders/builder-signing-server#overview)

Overview
------------------------------------------------------------------------------------------------

The Builder Signing Server is a self-hosted Express.js application that enables remote signing of builder authentication headers. By running this server, you can keep your Builder API credentials secure on your own infrastructure while still allowing your application to sign requests.

This server is designed to work with both the [CLOB Client](https://github.com/Polymarket/clob-client)
 for order attribution and the [Relayer Client](https://docs.polymarket.com/developers/builders/relayer-client)
 for gasless transactions.

[​](https://docs.polymarket.com/developers/builders/builder-signing-server#why-use-remote-signing%3F)

Why Use Remote Signing?
--------------------------------------------------------------------------------------------------------------------------------

Remote signing provides enhanced security by:

*   **Isolating credentials**: Your Builder API keys never leave your secure server
*   **Centralized key management**: Manage credentials in one secure location
*   **Reduced exposure**: Client applications don’t need direct access to sensitive keys

[​](https://docs.polymarket.com/developers/builders/builder-signing-server#installation)

Installation
--------------------------------------------------------------------------------------------------------

### 

[​](https://docs.polymarket.com/developers/builders/builder-signing-server#prerequisites)

Prerequisites

*   **Node.js**: v18 or higher
*   **yarn** or npm

### 

[​](https://docs.polymarket.com/developers/builders/builder-signing-server#clone-and-install)

Clone and Install

Copy

Ask AI

    # Clone the repository
    git clone https://github.com/Polymarket/builder-signing-server.git
    cd builder-signing-server
    
    # Install dependencies
    yarn install
    

[​](https://docs.polymarket.com/developers/builders/builder-signing-server#configuration)

Configuration
----------------------------------------------------------------------------------------------------------

### 

[​](https://docs.polymarket.com/developers/builders/builder-signing-server#environment-variables)

Environment Variables

Create a `.env` file in the root directory with your Builder API credentials:

Copy

Ask AI

    PORT=5001
    POLY_BUILDER_API_KEY=your_builder_api_key
    POLY_BUILDER_SECRET=your_builder_secret
    POLY_BUILDER_PASSPHRASE=your_builder_passphrase
    

**Security**: Never commit your `.env` file to version control. Add it to `.gitignore` to prevent accidental exposure of your credentials.

### 

[​](https://docs.polymarket.com/developers/builders/builder-signing-server#port-configuration)

Port Configuration

You can run the server on any port you choose. The default is `5001`, but you can change this by setting the `PORT` environment variable. Make sure to configure your client applications to use the same port:

Copy

Ask AI

    // In your client application
    const builderConfig = new BuilderConfig({
        remoteBuilderConfig: {url: "http://localhost:3000/sign"}
    });
    

[​](https://docs.polymarket.com/developers/builders/builder-signing-server#running-the-server)

Running the Server
--------------------------------------------------------------------------------------------------------------------

### 

[​](https://docs.polymarket.com/developers/builders/builder-signing-server#development-mode)

Development Mode

For development with automatic reloading:

Copy

Ask AI

    yarn start-dev
    

### 

[​](https://docs.polymarket.com/developers/builders/builder-signing-server#production-mode)

Production Mode

Build and run the compiled version:

Copy

Ask AI

    # Start the production server
    yarn start
    

The server will start and display:

Copy

Ask AI

    Builder signing server listening on :5001
    

[​](https://docs.polymarket.com/developers/builders/builder-signing-server#client-integration)

Client Integration
--------------------------------------------------------------------------------------------------------------------

### 

[​](https://docs.polymarket.com/developers/builders/builder-signing-server#with-clob-client)

With CLOB Client

Configure the CLOB client to use your signing server for order attribution:

Copy

Ask AI

    import { ClobClient } from "@polymarket/clob-client";
    import { BuilderConfig } from "@polymarket/builder-signing-sdk";
    
    const builderConfig = new BuilderConfig({
        remoteBuilderConfig: {url: "http://localhost:3000/sign"}
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
        builderConfig
    );
    
    // Orders will automatically use the signing server
    const order = await clobClient.createOrder({
        price: 0.40,
        side: Side.BUY,
        size: 5,
        tokenID: "27072675915285915455116137912884489109876947142577610372904917850067886308458"
    });
    
    const response = await clobClient.postOrder(order);
    

### 

[​](https://docs.polymarket.com/developers/builders/builder-signing-server#with-relayer-client)

With Relayer Client

Configure the relayer client to use your signing server for gasless transactions:

Copy

Ask AI

    import { RelayClient } from "@polymarket/builder-relayer-client";
    import { BuilderConfig } from "@polymarket/builder-signing-sdk";
    
    const builderConfig = new BuilderConfig({
        remoteBuilderConfig: {url: "http://localhost:3000/sign"}
    });
    
    const relayClient = new RelayClient(
        relayerUrl,
        chainId,
        wallet,
        builderConfig
    );
    
    // Transactions will automatically use the signing server
    const response = await relayClient.deploySafe();
    const result = await response.wait();
    

[​](https://docs.polymarket.com/developers/builders/builder-signing-server#production-deployment)

Production Deployment
--------------------------------------------------------------------------------------------------------------------------

[​](https://docs.polymarket.com/developers/builders/builder-signing-server#troubleshooting)

Troubleshooting
--------------------------------------------------------------------------------------------------------------

### 

[​](https://docs.polymarket.com/developers/builders/builder-signing-server#server-won%E2%80%99t-start)

Server Won’t Start

**Issue**: `Error: POLY_BUILDER_API_KEY environment variable is required` **Solution**: Ensure your `.env` file contains all required variables:

*   `POLY_BUILDER_API_KEY`
*   `POLY_BUILDER_SECRET`
*   `POLY_BUILDER_PASSPHRASE`

### 

[​](https://docs.polymarket.com/developers/builders/builder-signing-server#port-already-in-use)

Port Already in Use

**Issue**: `Error: listen EADDRINUSE: address already in use :::5001` **Solution**: Change the port in your `.env` file:

Copy

Ask AI

    PORT=5002
    

And update your client configuration accordingly.

### 

[​](https://docs.polymarket.com/developers/builders/builder-signing-server#invalid-signature-errors)

Invalid Signature Errors

**Issue**: Client receives invalid signature errors **Solution**:

1.  Verify the request body is being passed correctly as a JSON string
2.  Check that the path and method match exactly what the client is sending
3.  Ensure your server and client are using the same Builder API credentials

[​](https://docs.polymarket.com/developers/builders/builder-signing-server#source-code)

Source Code
------------------------------------------------------------------------------------------------------

The complete source code and additional examples are available on GitHub:

*   [Builder Signing Server Repository](https://github.com/Polymarket/builder-signing-server)
    
*   [Builder Signing SDK](https://github.com/Polymarket/builder-signing-sdk)
    

[​](https://docs.polymarket.com/developers/builders/builder-signing-server#support)

Support
----------------------------------------------------------------------------------------------

For assistance with the builder signing server:

*   Review the [GitHub repository](https://github.com/Polymarket/builder-signing-server)
    
*   Contact [support@polymarket.com](mailto:support@polymarket.com)
    

[Order Attribution](https://docs.polymarket.com/developers/builders/order-attribution)
[Relayer Client](https://docs.polymarket.com/developers/builders/relayer-client)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.