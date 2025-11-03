---
url: https://gofastmcp.com/clients/auth/oauth
title: OAuth Authentication - FastMCP
description: Authenticate your FastMCP client via OAuth 2.1.
scraped_at: 2025-11-03T18:41:57.906056
---

[Skip to main content](https://gofastmcp.com/clients/auth/oauth#content-area)

Join the [FastMCP community](https://discord.gg/uu8dJCgttd)
!

[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)

Search...

Navigation

Authentication

OAuth Authentication

Search the docs...

Ctrl K

Documentation

##### Get Started

*   [Welcome!](https://gofastmcp.com/getting-started/welcome)
    
*   [Installation](https://gofastmcp.com/getting-started/installation)
    
*   [Quickstart](https://gofastmcp.com/getting-started/quickstart)
    
*   [Updates\
    \
    NEW](https://gofastmcp.com/updates)
    

##### Servers

*   [Overview](https://gofastmcp.com/servers/server)
    
*   Core Components
    
*   Advanced Features
    
*   Authentication
    
*   Deployment
    

##### Clients

*   Essentials
    
*   Core Operations
    
*   Advanced Features
    
*   Authentication
    
    *   [OAuth\
        \
        NEW](https://gofastmcp.com/clients/auth/oauth)
        
    *   [Bearer Auth](https://gofastmcp.com/clients/auth/bearer)
        

##### Integrations

*   Authentication
    
*   Authorization
    
*   AI Assistants
    
*   AI SDKs
    
*   API Integration
    

##### Patterns

*   [Tool Transformation](https://gofastmcp.com/patterns/tool-transformation)
    
*   [Decorating Methods](https://gofastmcp.com/patterns/decorating-methods)
    
*   [CLI](https://gofastmcp.com/patterns/cli)
    
*   [Contrib Modules](https://gofastmcp.com/patterns/contrib)
    
*   [Testing](https://gofastmcp.com/patterns/testing)
    

##### Development

*   [Contributing](https://gofastmcp.com/development/contributing)
    
*   [Tests](https://gofastmcp.com/development/tests)
    
*   [Releases](https://gofastmcp.com/development/releases)
    
*   [Upgrade Guide\
    \
    NEW](https://gofastmcp.com/development/upgrade-guide)
    
*   [Changelog](https://gofastmcp.com/changelog)
    

On this page

*   [Client Usage](https://gofastmcp.com/clients/auth/oauth#client-usage)
    
*   [Default Configuration](https://gofastmcp.com/clients/auth/oauth#default-configuration)
    
*   [OAuth Helper](https://gofastmcp.com/clients/auth/oauth#oauth-helper)
    
*   [OAuth Parameters](https://gofastmcp.com/clients/auth/oauth#oauth-parameters)
    
*   [OAuth Flow](https://gofastmcp.com/clients/auth/oauth#oauth-flow)
    
*   [Token Storage](https://gofastmcp.com/clients/auth/oauth#token-storage)
    

`` New in version: `2.6.0` ``

OAuth authentication is only relevant for HTTP-based transports and requires user interaction via a web browser.

When your FastMCP client needs to access an MCP server protected by OAuth 2.1, and the process requires user interaction (like logging in and granting consent), you should use the Authorization Code Flow. FastMCP provides the `fastmcp.client.auth.OAuth` helper to simplify this entire process. This flow is common for user-facing applications where the application acts on behalf of the user.

[​](https://gofastmcp.com/clients/auth/oauth#client-usage)

Client Usage
--------------------------------------------------------------------------

### 

[​](https://gofastmcp.com/clients/auth/oauth#default-configuration)

Default Configuration

The simplest way to use OAuth is to pass the string `"oauth"` to the `auth` parameter of the `Client` or transport instance. FastMCP will automatically configure the client to use OAuth with default settings:

Copy

    from fastmcp import Client
    
    # Uses default OAuth settings
    async with Client("https://fastmcp.cloud/mcp", auth="oauth") as client:
        await client.ping()
    

### 

[​](https://gofastmcp.com/clients/auth/oauth#oauth-helper)

`OAuth` Helper

To fully configure the OAuth flow, use the `OAuth` helper and pass it to the `auth` parameter of the `Client` or transport instance. `OAuth` manages the complexities of the OAuth 2.1 Authorization Code Grant with PKCE (Proof Key for Code Exchange) for enhanced security, and implements the full `httpx.Auth` interface.

Copy

    from fastmcp import Client
    from fastmcp.client.auth import OAuth
    
    oauth = OAuth(mcp_url="https://fastmcp.cloud/mcp")
    
    async with Client("https://fastmcp.cloud/mcp", auth=oauth) as client:
        await client.ping()
    

#### 

[​](https://gofastmcp.com/clients/auth/oauth#oauth-parameters)

`OAuth` Parameters

*   **`mcp_url`** (`str`): The full URL of the target MCP server endpoint. Used to discover OAuth server metadata
*   **`scopes`** (`str | list[str]`, optional): OAuth scopes to request. Can be space-separated string or list of strings
*   **`client_name`** (`str`, optional): Client name for dynamic registration. Defaults to `"FastMCP Client"`
*   **`token_storage`** (`AsyncKeyValue`, optional): Storage backend for persisting OAuth tokens. Defaults to in-memory storage (tokens lost on restart). See [Token Storage](https://gofastmcp.com/clients/auth/oauth#token-storage)
     for encrypted storage options
*   **`additional_client_metadata`** (`dict[str, Any]`, optional): Extra metadata for client registration
*   **`callback_port`** (`int`, optional): Fixed port for OAuth callback server. If not specified, uses a random available port

[​](https://gofastmcp.com/clients/auth/oauth#oauth-flow)

OAuth Flow
----------------------------------------------------------------------

The OAuth flow is triggered when you use a FastMCP `Client` configured to use OAuth.

1

Token Check

The client first checks the configured `token_storage` backend for existing, valid tokens for the target server. If one is found, it will be used to authenticate the client.

2

OAuth Server Discovery

If no valid tokens exist, the client attempts to discover the OAuth server’s endpoints using a well-known URI (e.g., `/.well-known/oauth-authorization-server`) based on the `mcp_url`.

3

Dynamic Client Registration

If the OAuth server supports it and the client isn’t already registered (or credentials aren’t cached), the client performs dynamic client registration according to RFC 7591.

4

Local Callback Server

A temporary local HTTP server is started on an available port (or the port specified via `callback_port`). This server’s address (e.g., `http://127.0.0.1:<port>/callback`) acts as the `redirect_uri` for the OAuth flow.

5

Browser Interaction

The user’s default web browser is automatically opened, directing them to the OAuth server’s authorization endpoint. The user logs in and grants (or denies) the requested `scopes`.

6

Authorization Code & Token Exchange

Upon approval, the OAuth server redirects the user’s browser to the local callback server with an `authorization_code`. The client captures this code and exchanges it with the OAuth server’s token endpoint for an `access_token` (and often a `refresh_token`) using PKCE for security.

7

Token Caching

The obtained tokens are saved to the configured `token_storage` backend for future use, eliminating the need for repeated browser interactions.

8

Authenticated Requests

The access token is automatically included in the `Authorization` header for requests to the MCP server.

9

Refresh Token

If the access token expires, the client will automatically use the refresh token to get a new access token.

[​](https://gofastmcp.com/clients/auth/oauth#token-storage)

Token Storage
----------------------------------------------------------------------------

`` New in version: `2.13.0` `` By default, tokens are stored in memory and lost when your application restarts. For persistent storage, pass an `AsyncKeyValue`\-compatible storage backend to the `token_storage` parameter.

**Security Consideration**: Use encrypted storage for production. MCP clients can accumulate OAuth credentials for many servers over time, and a compromised token store could expose access to multiple services.

Copy

    from fastmcp import Client
    from fastmcp.client.auth import OAuth
    from key_value.aio.stores.disk import DiskStore
    from key_value.aio.wrappers.encryption import FernetEncryptionWrapper
    from cryptography.fernet import Fernet
    import os
    
    # Create encrypted disk storage
    encrypted_storage = FernetEncryptionWrapper(
        key_value=DiskStore(directory="~/.fastmcp/oauth-tokens"),
        fernet=Fernet(os.environ["OAUTH_STORAGE_ENCRYPTION_KEY"])
    )
    
    oauth = OAuth(
        mcp_url="https://fastmcp.cloud/mcp",
        token_storage=encrypted_storage
    )
    
    async with Client("https://fastmcp.cloud/mcp", auth=oauth) as client:
        await client.ping()
    

You can use any `AsyncKeyValue`\-compatible backend from the [key-value library](https://github.com/strawgate/py-key-value)
 including Redis, DynamoDB, and more. Wrap your storage in `FernetEncryptionWrapper` for encryption.

When selecting a storage backend, review the [py-key-value documentation](https://github.com/strawgate/py-key-value)
 to understand the maturity level and limitations of your chosen backend. Some backends may be in preview or have constraints that affect production suitability.

[Client Roots\
\
Previous](https://gofastmcp.com/clients/roots)
[Bearer Token Authentication\
\
Next](https://gofastmcp.com/clients/auth/bearer)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.