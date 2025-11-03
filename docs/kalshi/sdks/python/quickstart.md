---
url: https://docs.kalshi.com/sdks/python/quickstart
title: Python SDK Quick Start - API Documentation
description: Get started with the Kalshi Python SDK
scraped_at: 2025-11-03T14:46:42.360179
---

[Skip to main content](https://docs.kalshi.com/sdks/python/quickstart#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

Python

Python SDK Quick Start

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

On this page

*   [Installation](https://docs.kalshi.com/sdks/python/quickstart#installation)
    
*   [Quick Start](https://docs.kalshi.com/sdks/python/quickstart#quick-start)
    
*   [Source Code](https://docs.kalshi.com/sdks/python/quickstart#source-code)
    

[​](https://docs.kalshi.com/sdks/python/quickstart#installation)

Installation
--------------------------------------------------------------------------------

Copy

Ask AI

    pip install kalshi-python
    

[​](https://docs.kalshi.com/sdks/python/quickstart#quick-start)

Quick Start
------------------------------------------------------------------------------

Copy

Ask AI

    from kalshi_python import Configuration, KalshiClient
    
    # Configure the client
    config = Configuration(
        host="https://api.elections.kalshi.com/trade-api/v2"
    )
    
    # For authenticated requests
    # Read private key from file
    with open("path/to/private_key.pem", "r") as f:
        private_key = f.read()
    
    config.api_key_id = "your-api-key-id"
    config.private_key_pem = private_key
    
    # Initialize the client
    client = KalshiClient(config)
    
    # Make API calls
    balance = client.get_balance()
    print(f"Balance: ${balance.balance / 100:.2f}")
    

[​](https://docs.kalshi.com/sdks/python/quickstart#source-code)

Source Code
------------------------------------------------------------------------------

*   PyPI: [https://pypi.org/project/kalshi-python/](https://pypi.org/project/kalshi-python/)
    

[Kalshi SDKs](https://docs.kalshi.com/sdks/overview)
[Portfolio](https://docs.kalshi.com/python-sdk/api/PortfolioApi)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.