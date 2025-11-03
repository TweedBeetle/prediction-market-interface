---
url: https://docs.polymarket.com/quickstart/websocket/WSS-Quickstart
title: WSS Quickstart - Polymarket Documentation
scraped_at: 2025-11-03T15:04:26.663122
---

[Skip to main content](https://docs.polymarket.com/quickstart/websocket/WSS-Quickstart#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

Ctrl K

Search...

Navigation

Websocket

WSS Quickstart

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

On this page

*   [Getting your API Keys](https://docs.polymarket.com/quickstart/websocket/WSS-Quickstart#getting-your-api-keys)
    
*   [Using those keys to connect to the Market or User Websocket](https://docs.polymarket.com/quickstart/websocket/WSS-Quickstart#using-those-keys-to-connect-to-the-market-or-user-websocket)
    

The following code samples and explanation will show you how to subsribe to the Marker and User channels of the Websocket. You’ll need your API keys to do this so we’ll start with that.

[​](https://docs.polymarket.com/quickstart/websocket/WSS-Quickstart#getting-your-api-keys)

Getting your API Keys
-------------------------------------------------------------------------------------------------------------------

DeriveAPIKeys-Python

DeriveAPIKeys-TS

Copy

Ask AI

    from py_clob_client.client import ClobClient
    
    host: str = "https://clob.polymarket.com"
    key: str = "" #This is your Private Key. If using email login export from https://reveal.magic.link/polymarket otherwise export from your Web3 Application
    chain_id: int = 137 #No need to adjust this
    POLYMARKET_PROXY_ADDRESS: str = '' #This is the address you deposit/send USDC to to FUND your Polymarket account.
    
    #Select from the following 3 initialization options to matches your login method, and remove any unused lines so only one client is initialized.
    
    ### Initialization of a client using a Polymarket Proxy associated with an Email/Magic account. If you login with your email use this example.
    client = ClobClient(host, key=key, chain_id=chain_id, signature_type=1, funder=POLYMARKET_PROXY_ADDRESS)
    
    ### Initialization of a client using a Polymarket Proxy associated with a Browser Wallet(Metamask, Coinbase Wallet, etc)
    client = ClobClient(host, key=key, chain_id=chain_id, signature_type=2, funder=POLYMARKET_PROXY_ADDRESS)
    
    ### Initialization of a client that trades directly from an EOA. 
    client = ClobClient(host, key=key, chain_id=chain_id)
    
    print( client.derive_api_key() )
    
    

See all 20 lines

[​](https://docs.polymarket.com/quickstart/websocket/WSS-Quickstart#using-those-keys-to-connect-to-the-market-or-user-websocket)

Using those keys to connect to the Market or User Websocket
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

WSS-Connection

Copy

Ask AI

    from websocket import WebSocketApp
    import json
    import time
    import threading
    
    MARKET_CHANNEL = "market"
    USER_CHANNEL = "user"
    
    
    class WebSocketOrderBook:
        def __init__(self, channel_type, url, data, auth, message_callback, verbose):
            self.channel_type = channel_type
            self.url = url
            self.data = data
            self.auth = auth
            self.message_callback = message_callback
            self.verbose = verbose
            furl = url + "/ws/" + channel_type
            self.ws = WebSocketApp(
                furl,
                on_message=self.on_message,
                on_error=self.on_error,
                on_close=self.on_close,
                on_open=self.on_open,
            )
            self.orderbooks = {}
    
        def on_message(self, ws, message):
            print(message)
            pass
    
        def on_error(self, ws, error):
            print("Error: ", error)
            exit(1)
    
        def on_close(self, ws, close_status_code, close_msg):
            print("closing")
            exit(0)
    
        def on_open(self, ws):
            if self.channel_type == MARKET_CHANNEL:
                ws.send(json.dumps({"assets_ids": self.data, "type": MARKET_CHANNEL}))
            elif self.channel_type == USER_CHANNEL and self.auth:
                ws.send(
                    json.dumps(
                        {"markets": self.data, "type": USER_CHANNEL, "auth": self.auth}
                    )
                )
            else:
                exit(1)
    
            thr = threading.Thread(target=self.ping, args=(ws,))
            thr.start()
    
        def ping(self, ws):
            while True:
                ws.send("PING")
                time.sleep(10)
    
        def run(self):
            self.ws.run_forever()
    
    
    if __name__ == "__main__":
        url = "wss://ws-subscriptions-clob.polymarket.com"
        #Complete these by exporting them from your initialized client. 
        api_key = ""
        api_secret = ""
        api_passphrase = ""
    
        asset_ids = [\
            "109681959945973300464568698402968596289258214226684818748321941747028805721376",\
        ]
        condition_ids = [] # no really need to filter by this one
    
        auth = {"apiKey": api_key, "secret": api_secret, "passphrase": api_passphrase}
    
        market_connection = WebSocketOrderBook(
            MARKET_CHANNEL, url, asset_ids, auth, None, True
        )
        user_connection = WebSocketOrderBook(
            USER_CHANNEL, url, condition_ids, auth, None, True
        )
    
        market_connection.run()
        # user_connection.run()
    

See all 86 lines

[WSS Overview](https://docs.polymarket.com/developers/CLOB/websocket/wss-overview)
[WSS Authentication](https://docs.polymarket.com/developers/CLOB/websocket/wss-auth)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.