---
url: https://docs.kalshi.com/sdks/typescript/quickstart
title: TypeScript SDK Quick Start - API Documentation
description: Get started with the Kalshi TypeScript SDK
scraped_at: 2025-11-03T14:46:42.527633
---

[Skip to main content](https://docs.kalshi.com/sdks/typescript/quickstart#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

TypeScript

TypeScript SDK Quick Start

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

On this page

*   [Installation](https://docs.kalshi.com/sdks/typescript/quickstart#installation)
    
*   [Quick Start](https://docs.kalshi.com/sdks/typescript/quickstart#quick-start)
    
*   [Authentication](https://docs.kalshi.com/sdks/typescript/quickstart#authentication)
    
*   [Source Code](https://docs.kalshi.com/sdks/typescript/quickstart#source-code)
    

[​](https://docs.kalshi.com/sdks/typescript/quickstart#installation)

Installation
------------------------------------------------------------------------------------

Copy

Ask AI

    npm install kalshi-typescript
    

[​](https://docs.kalshi.com/sdks/typescript/quickstart#quick-start)

Quick Start
----------------------------------------------------------------------------------

Copy

Ask AI

    import { Configuration, PortfolioApi } from 'kalshi-typescript';
    
    // Configure the SDK
    const config = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: 'path/to/your/private-key.pem', // or use privateKeyPem
        basePath: 'https://api.elections.kalshi.com/trade-api/v2'
    });
    
    // Create API instance
    const portfolioApi = new PortfolioApi(config);
    
    // Make API calls
    const balance = await portfolioApi.getBalance();
    console.log(`Balance: $${(balance.data.balance || 0) / 100}`);
    

[​](https://docs.kalshi.com/sdks/typescript/quickstart#authentication)

Authentication
----------------------------------------------------------------------------------------

The SDK uses RSA-PSS signing for authentication. You can provide your private key either as a file path or as a PEM string:

Copy

Ask AI

    // Using file path
    const config = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPath: 'path/to/private-key.pem',
        basePath: 'https://api.elections.kalshi.com/trade-api/v2'
    });
    
    // Using PEM string
    const config = new Configuration({
        apiKey: 'your-api-key-id',
        privateKeyPem: '-----BEGIN RSA PRIVATE KEY-----\n...\n-----END RSA PRIVATE KEY-----',
        basePath: 'https://api.elections.kalshi.com/trade-api/v2'
    });
    

[​](https://docs.kalshi.com/sdks/typescript/quickstart#source-code)

Source Code
----------------------------------------------------------------------------------

*   NPM: [kalshi-typescript](https://www.npmjs.com/package/kalshi-typescript)
    

[ApiKeys](https://docs.kalshi.com/python-sdk/api/ApiKeysApi)
[Portfolio](https://docs.kalshi.com/typescript-sdk/api/PortfolioApi)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.