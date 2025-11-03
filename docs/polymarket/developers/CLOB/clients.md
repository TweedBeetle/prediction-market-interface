---
url: https://docs.polymarket.com/developers/CLOB/clients
title: Clients - Polymarket Documentation
scraped_at: 2025-11-03T15:03:55.868666
---

[Skip to main content](https://docs.polymarket.com/developers/CLOB/clients#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

Ctrl K

Search...

Navigation

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

On this page

*   [Order Utils](https://docs.polymarket.com/developers/CLOB/clients#order-utils)
    

Polymarket has implemented reference clients that allow programmatic use of the API below:

*   [clob-client](https://github.com/Polymarket/clob-client)
     (Typescript)
*   [py-clob-client](https://github.com/Polymarket/py-clob-client)
     (Python)

python\_initialization

typescript\_initialization

Copy

Ask AI

    pip install py-clob-client
    
    from py_clob_client.client import ClobClient
    
    host: str = ""
    key: str = ""
    chain_id: int = 137
    
    ### Initialization of a client that trades directly from an EOA
    client = ClobClient(host, key=key, chain_id=chain_id)
    
    ### Initialization of a client using a Polymarket Proxy associated with an Email/Magic account
    client = ClobClient(host, key=key, chain_id=chain_id, signature_type=1, funder=POLYMARKET_PROXY_ADDRESS)
    
    ### Initialization of a client using a Polymarket Proxy associated with a Browser Wallet(Metamask, Coinbase Wallet, etc)
    client = ClobClient(host, key=key, chain_id=chain_id, signature_type=2, funder=POLYMARKET_PROXY_ADDRESS)
    
    

* * *

[​](https://docs.polymarket.com/developers/CLOB/clients#order-utils)

Order Utils
-----------------------------------------------------------------------------------

Polymarket has implemented utility libraries to programmatically sign and generate orders:

*   [clob-order-utils](https://github.com/Polymarket/clob-order-utils)
     (Typescript)
*   [python-order-utils](https://github.com/Polymarket/python-order-utils)
     (Python)
*   [go-order-utils](https://github.com/Polymarket/go-order-utils)
     (Golang)

[Status](https://docs.polymarket.com/developers/CLOB/status)
[Authentication](https://docs.polymarket.com/developers/CLOB/authentication)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.