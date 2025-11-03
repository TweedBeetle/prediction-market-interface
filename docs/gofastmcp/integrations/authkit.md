---
url: https://gofastmcp.com/integrations/authkit
title: AuthKit 🤝 FastMCP - FastMCP
description: Secure your FastMCP server with AuthKit by WorkOS
scraped_at: 2025-11-03T18:42:09.774196
---

[Skip to main content](https://gofastmcp.com/integrations/authkit#content-area)

Join the [FastMCP community](https://discord.gg/uu8dJCgttd)
!

[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)

Search...

Navigation

Authentication

AuthKit 🤝 FastMCP

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
    

##### Integrations

*   Authentication
    
    *   [Auth0\
        \
        NEW](https://gofastmcp.com/integrations/auth0)
        
    *   [AuthKit\
        \
        NEW](https://gofastmcp.com/integrations/authkit)
        
    *   [AWS Cognito\
        \
        NEW](https://gofastmcp.com/integrations/aws-cognito)
        
    *   [Azure (Entra ID)\
        \
        NEW](https://gofastmcp.com/integrations/azure)
        
    *   [Descope\
        \
        NEW](https://gofastmcp.com/integrations/descope)
        
    *   [GitHub\
        \
        NEW](https://gofastmcp.com/integrations/github)
        
    *   [Scalekit\
        \
        NEW](https://gofastmcp.com/integrations/scalekit)
        
    *   [Google\
        \
        NEW](https://gofastmcp.com/integrations/google)
        
    *   [WorkOS\
        \
        NEW](https://gofastmcp.com/integrations/workos)
        
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

*   [Configuration](https://gofastmcp.com/integrations/authkit#configuration)
    
*   [Prerequisites](https://gofastmcp.com/integrations/authkit#prerequisites)
    
*   [Step 1: AuthKit Configuration](https://gofastmcp.com/integrations/authkit#step-1%3A-authkit-configuration)
    
*   [Step 2: FastMCP Configuration](https://gofastmcp.com/integrations/authkit#step-2%3A-fastmcp-configuration)
    
*   [Testing](https://gofastmcp.com/integrations/authkit#testing)
    
*   [Environment Variables](https://gofastmcp.com/integrations/authkit#environment-variables)
    
*   [Provider Selection](https://gofastmcp.com/integrations/authkit#provider-selection)
    
*   [AuthKit-Specific Configuration](https://gofastmcp.com/integrations/authkit#authkit-specific-configuration)
    

`` New in version: `2.11.0` `` This guide shows you how to secure your FastMCP server using WorkOS’s **AuthKit**, a complete authentication and user management solution. This integration uses the [**Remote OAuth**](https://gofastmcp.com/servers/auth/remote-oauth)
 pattern, where AuthKit handles user login and your FastMCP server validates the tokens.

[​](https://gofastmcp.com/integrations/authkit#configuration)

Configuration
------------------------------------------------------------------------------

### 

[​](https://gofastmcp.com/integrations/authkit#prerequisites)

Prerequisites

Before you begin, you will need:

1.  A **[WorkOS Account](https://workos.com/)
    ** and a new **Project**.
2.  An **[AuthKit](https://www.authkit.com/)
    ** instance configured within your WorkOS project.
3.  Your FastMCP server’s URL (can be localhost for development, e.g., `http://localhost:8000`).

### 

[​](https://gofastmcp.com/integrations/authkit#step-1%3A-authkit-configuration)

Step 1: AuthKit Configuration

In your WorkOS Dashboard, enable AuthKit and configure the following settings:

1

Enable Dynamic Client Registration

Go to **Applications → Configuration** and enable **Dynamic Client Registration**. This allows MCP clients register with your application automatically.![Enable Dynamic Client Registration](https://mintcdn.com/fastmcp/hUosZw7ujHZFemrG/integrations/images/authkit/enable_dcr.png?w=2500&fit=max&auto=format&n=hUosZw7ujHZFemrG&q=85&s=a4e1627dd14ee7c1c2ad6b6628dc8520)

2

Note Your AuthKit Domain

Find your **AuthKit Domain** on the configuration page. It will look like `https://your-project-12345.authkit.app`. You’ll need this for your FastMCP server configuration.

### 

[​](https://gofastmcp.com/integrations/authkit#step-2%3A-fastmcp-configuration)

Step 2: FastMCP Configuration

Create your FastMCP server file and use the `AuthKitProvider` to handle all the OAuth integration automatically:

server.py

Copy

    from fastmcp import FastMCP
    from fastmcp.server.auth.providers.workos import AuthKitProvider
    
    # The AuthKitProvider automatically discovers WorkOS endpoints
    # and configures JWT token validation
    auth_provider = AuthKitProvider(
        authkit_domain="https://your-project-12345.authkit.app",
        base_url="http://localhost:8000"  # Use your actual server URL
    )
    
    mcp = FastMCP(name="AuthKit Secured App", auth=auth_provider)
    

[​](https://gofastmcp.com/integrations/authkit#testing)

Testing
------------------------------------------------------------------

To test your server, you can use the `fastmcp` CLI to run it locally. Assuming you’ve saved the above code to `server.py` (after replacing the `authkit_domain` and `base_url` with your actual values!), you can run the following command:

Copy

    fastmcp run server.py --transport http --port 8000
    

Now, you can use a FastMCP client to test that you can reach your server after authenticating:

Copy

    from fastmcp import Client
    import asyncio
    
    async def main():
        async with Client("http://localhost:8000/mcp", auth="oauth") as client:
            assert await client.ping()
    
    if __name__ == "__main__":
        asyncio.run(main())
    

[​](https://gofastmcp.com/integrations/authkit#environment-variables)

Environment Variables
----------------------------------------------------------------------------------------------

`` New in version: `2.12.1` `` For production deployments, use environment variables instead of hardcoding credentials.

### 

[​](https://gofastmcp.com/integrations/authkit#provider-selection)

Provider Selection

Setting this environment variable allows the AuthKit provider to be used automatically without explicitly instantiating it in code.

[​](https://gofastmcp.com/integrations/authkit#param-fastmcp-server-auth)

FASTMCP\_SERVER\_AUTH

default:"Not set"

Set to `fastmcp.server.auth.providers.workos.AuthKitProvider` to use AuthKit authentication.

### 

[​](https://gofastmcp.com/integrations/authkit#authkit-specific-configuration)

AuthKit-Specific Configuration

These environment variables provide default values for the AuthKit provider, whether it’s instantiated manually or configured via `FASTMCP_SERVER_AUTH`.

[​](https://gofastmcp.com/integrations/authkit#param-fastmcp-server-auth-authkitprovider-authkit-domain)

FASTMCP\_SERVER\_AUTH\_AUTHKITPROVIDER\_AUTHKIT\_DOMAIN

required

Your AuthKit domain (e.g., `https://your-project-12345.authkit.app`)

[​](https://gofastmcp.com/integrations/authkit#param-fastmcp-server-auth-authkitprovider-base-url)

FASTMCP\_SERVER\_AUTH\_AUTHKITPROVIDER\_BASE\_URL

required

Public URL of your FastMCP server (e.g., `https://your-server.com` or `http://localhost:8000` for development)

[​](https://gofastmcp.com/integrations/authkit#param-fastmcp-server-auth-authkitprovider-required-scopes)

FASTMCP\_SERVER\_AUTH\_AUTHKITPROVIDER\_REQUIRED\_SCOPES

default:"\[\]"

Comma-, space-, or JSON-separated list of required OAuth scopes (e.g., `openid profile email` or `["openid", "profile", "email"]`)

Example `.env` file:

Copy

    # Use the AuthKit provider
    FASTMCP_SERVER_AUTH=fastmcp.server.auth.providers.workos.AuthKitProvider
    
    # AuthKit configuration
    FASTMCP_SERVER_AUTH_AUTHKITPROVIDER_AUTHKIT_DOMAIN=https://your-project-12345.authkit.app
    FASTMCP_SERVER_AUTH_AUTHKITPROVIDER_BASE_URL=https://your-server.com
    FASTMCP_SERVER_AUTH_AUTHKITPROVIDER_REQUIRED_SCOPES=openid,profile,email
    

With environment variables set, your server code simplifies to:

server.py

Copy

    from fastmcp import FastMCP
    
    # Authentication is automatically configured from environment
    mcp = FastMCP(name="AuthKit Secured App")
    

[Auth0 OAuth 🤝 FastMCP\
\
Previous](https://gofastmcp.com/integrations/auth0)
[AWS Cognito OAuth 🤝 FastMCP\
\
Next](https://gofastmcp.com/integrations/aws-cognito)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

![Enable Dynamic Client Registration](https://mintcdn.com/fastmcp/hUosZw7ujHZFemrG/integrations/images/authkit/enable_dcr.png?w=2500&fit=max&auto=format&n=hUosZw7ujHZFemrG&q=85&s=a4e1627dd14ee7c1c2ad6b6628dc8520)