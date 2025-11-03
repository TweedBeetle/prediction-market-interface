---
url: https://gofastmcp.com/clients/auth/bearer
title: Bearer Token Authentication - FastMCP
description: Authenticate your FastMCP client with a Bearer token.
scraped_at: 2025-11-03T18:41:58.153974
---

[Skip to main content](https://gofastmcp.com/clients/auth/bearer#content-area)

Join the [FastMCP community](https://discord.gg/uu8dJCgttd)
!

[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)

Search...

Navigation

Authentication

Bearer Token Authentication

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

*   [Client Usage](https://gofastmcp.com/clients/auth/bearer#client-usage)
    
*   [BearerAuth Helper](https://gofastmcp.com/clients/auth/bearer#bearerauth-helper)
    
*   [Custom Headers](https://gofastmcp.com/clients/auth/bearer#custom-headers)
    

`` New in version: `2.6.0` ``

Bearer Token authentication is only relevant for HTTP-based transports.

You can configure your FastMCP client to use **bearer authentication** by supplying a valid access token. This is most appropriate for service accounts, long-lived API keys, CI/CD, applications where authentication is managed separately, or other non-interactive authentication methods. A Bearer token is a JSON Web Token (JWT) that is used to authenticate a request. It is most commonly used in the `Authorization` header of an HTTP request, using the `Bearer` scheme:

Copy

    Authorization: Bearer <token>
    

[​](https://gofastmcp.com/clients/auth/bearer#client-usage)

Client Usage
---------------------------------------------------------------------------

The most straightforward way to use a pre-existing Bearer token is to provide it as a string to the `auth` parameter of the `fastmcp.Client` or transport instance. FastMCP will automatically format it correctly for the `Authorization` header and bearer scheme.

If you’re using a string token, do not include the `Bearer` prefix. FastMCP will add it for you.

Copy

    from fastmcp import Client
    
    async with Client(
        "https://fastmcp.cloud/mcp", 
        auth="<your-token>",
    ) as client:
        await client.ping()
    

You can also supply a Bearer token to a transport instance, such as `StreamableHttpTransport` or `SSETransport`:

Copy

    from fastmcp import Client
    from fastmcp.client.transports import StreamableHttpTransport
    
    transport = StreamableHttpTransport(
        "http://fastmcp.cloud/mcp", 
        auth="<your-token>",
    )
    
    async with Client(transport) as client:
        await client.ping()
    

[​](https://gofastmcp.com/clients/auth/bearer#bearerauth-helper)

`BearerAuth` Helper
---------------------------------------------------------------------------------------

If you prefer to be more explicit and not rely on FastMCP to transform your string token, you can use the `BearerAuth` class yourself, which implements the `httpx.Auth` interface.

Copy

    from fastmcp import Client
    from fastmcp.client.auth import BearerAuth
    
    async with Client(
        "https://fastmcp.cloud/mcp", 
        auth=BearerAuth(token="<your-token>"),
    ) as client:
        await client.ping()
    

[​](https://gofastmcp.com/clients/auth/bearer#custom-headers)

Custom Headers
-------------------------------------------------------------------------------

If the MCP server expects a custom header or token scheme, you can manually set the client’s `headers` instead of using the `auth` parameter by setting them on your transport:

Copy

    from fastmcp import Client
    from fastmcp.client.transports import StreamableHttpTransport
    
    async with Client(
        transport=StreamableHttpTransport(
            "https://fastmcp.cloud/mcp", 
            headers={"X-API-Key": "<your-token>"},
        ),
    ) as client:
        await client.ping()
    

[OAuth Authentication\
\
Previous](https://gofastmcp.com/clients/auth/oauth)
[Auth0 OAuth 🤝 FastMCP\
\
Next](https://gofastmcp.com/integrations/auth0)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.