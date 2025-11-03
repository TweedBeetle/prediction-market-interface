---
url: https://gofastmcp.com/integrations/descope
title: Descope 🤝 FastMCP - FastMCP
description: Secure your FastMCP server with Descope
scraped_at: 2025-11-03T18:42:15.529152
---

[Skip to main content](https://gofastmcp.com/integrations/descope#content-area)

Join the [FastMCP community](https://discord.gg/uu8dJCgttd)
!

[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)

Search...

Navigation

Authentication

Descope 🤝 FastMCP

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

*   [Configuration](https://gofastmcp.com/integrations/descope#configuration)
    
*   [Prerequisites](https://gofastmcp.com/integrations/descope#prerequisites)
    
*   [Step 1: Configure Descope](https://gofastmcp.com/integrations/descope#step-1%3A-configure-descope)
    
*   [Step 2: Environment Setup](https://gofastmcp.com/integrations/descope#step-2%3A-environment-setup)
    
*   [Step 3: FastMCP Configuration](https://gofastmcp.com/integrations/descope#step-3%3A-fastmcp-configuration)
    
*   [Testing](https://gofastmcp.com/integrations/descope#testing)
    
*   [Environment Variables](https://gofastmcp.com/integrations/descope#environment-variables)
    
*   [Provider Selection](https://gofastmcp.com/integrations/descope#provider-selection)
    
*   [Descope-Specific Configuration](https://gofastmcp.com/integrations/descope#descope-specific-configuration)
    

`` New in version: `2.12.4` `` This guide shows you how to secure your FastMCP server using [**Descope**](https://www.descope.com/)
, a complete authentication and user management solution. This integration uses the [**Remote OAuth**](https://gofastmcp.com/servers/auth/remote-oauth)
 pattern, where Descope handles user login and your FastMCP server validates the tokens.

[​](https://gofastmcp.com/integrations/descope#configuration)

Configuration
------------------------------------------------------------------------------

### 

[​](https://gofastmcp.com/integrations/descope#prerequisites)

Prerequisites

Before you begin, you will need:

1.  To [sign up](https://www.descope.com/sign-up)
     for a Free Forever Descope account
2.  Your **Project ID** from the [Descope Console](https://app.descope.com/settings/project)
    
3.  Your FastMCP server’s URL (can be localhost for development, e.g., `http://localhost:3000`)

### 

[​](https://gofastmcp.com/integrations/descope#step-1%3A-configure-descope)

Step 1: Configure Descope

1

Enable Dynamic Client Registration

1.  Go to the [Inbound Apps page](https://app.descope.com/apps/inbound)
     of the Descope Console
2.  Click **DCR Settings**
3.  Enable **Dynamic Client Registration (DCR)**
4.  Define allowed scopes

DCR is required for FastMCP clients to automatically register with your authentication server.

2

Note Your Project ID

Save your Project ID from [Project Settings](https://app.descope.com/settings/project)
:

Copy

    Project ID: P2abc...123
    

### 

[​](https://gofastmcp.com/integrations/descope#step-2%3A-environment-setup)

Step 2: Environment Setup

Create a `.env` file with your Descope configuration:

Copy

    DESCOPE_PROJECT_ID=P2abc...123      # Your Descope Project ID
    DESCOPE_BASE_URL=https://api.descope.com   # Descope API URL
    SERVER_URL=http://localhost:3000     # Your server's base URL
    

You can find your project’s Descope Base URL in the [Multi-Region Support Guide](https://docs.descope.com/management/project-settings/multi-regional)
.

### 

[​](https://gofastmcp.com/integrations/descope#step-3%3A-fastmcp-configuration)

Step 3: FastMCP Configuration

Create your FastMCP server file and use the DescopeProvider to handle all the OAuth integration automatically:

server.py

Copy

    from fastmcp import FastMCP
    from fastmcp.server.auth.providers.descope import DescopeProvider
    
    # The DescopeProvider automatically discovers Descope endpoints
    # and configures JWT token validation
    auth_provider = DescopeProvider(
        project_id=DESCOPE_PROJECT_ID,        # Your Descope Project ID
        base_url=SERVER_URL,                  # Your server's public URL
        descope_base_url=DESCOPE_BASE_URL,    # Descope API base URL
    )
    
    # Create FastMCP server with auth
    mcp = FastMCP(name="My Descope Protected Server", auth=auth_provider)
    
    

[​](https://gofastmcp.com/integrations/descope#testing)

Testing
------------------------------------------------------------------

To test your server, you can use the `fastmcp` CLI to run it locally. Assuming you’ve saved the above code to `server.py` (after replacing the `project_id`, `base_url`, and `descope_base_url` with your actual values!), you can run the following command:

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
    

[​](https://gofastmcp.com/integrations/descope#environment-variables)

Environment Variables
----------------------------------------------------------------------------------------------

For production deployments, use environment variables instead of hardcoding credentials.

### 

[​](https://gofastmcp.com/integrations/descope#provider-selection)

Provider Selection

Setting this environment variable allows the Descope provider to be used automatically without explicitly instantiating it in code.

[​](https://gofastmcp.com/integrations/descope#param-fastmcp-server-auth)

FASTMCP\_SERVER\_AUTH

default:"Not set"

Set to `fastmcp.server.auth.providers.descope.DescopeProvider` to use Descope authentication.

### 

[​](https://gofastmcp.com/integrations/descope#descope-specific-configuration)

Descope-Specific Configuration

These environment variables provide default values for the Descope provider, whether it’s instantiated manually or configured via `FASTMCP_SERVER_AUTH`.

[​](https://gofastmcp.com/integrations/descope#param-fastmcp-server-auth-descopeprovider-project-id)

FASTMCP\_SERVER\_AUTH\_DESCOPEPROVIDER\_PROJECT\_ID

required

Your Descope Project ID from the [Descope Console](https://app.descope.com/settings/project)

[​](https://gofastmcp.com/integrations/descope#param-fastmcp-server-auth-descopeprovider-base-url)

FASTMCP\_SERVER\_AUTH\_DESCOPEPROVIDER\_BASE\_URL

required

Public URL of your FastMCP server (e.g., `https://your-server.com` or `http://localhost:8000` for development)

[​](https://gofastmcp.com/integrations/descope#param-fastmcp-server-auth-descopeprovider-descope-base-url)

FASTMCP\_SERVER\_AUTH\_DESCOPEPROVIDER\_DESCOPE\_BASE\_URL

default:"https://api.descope.com"

Descope API base URL for your [region/environment](https://docs.descope.com/management/project-settings/multi-regional)

Example `.env` file:

Copy

    # Use the Descope provider
    FASTMCP_SERVER_AUTH=fastmcp.server.auth.providers.descope.DescopeProvider
    
    # Descope configuration
    FASTMCP_SERVER_AUTH_DESCOPEPROVIDER_PROJECT_ID=P2abc...123
    FASTMCP_SERVER_AUTH_DESCOPEPROVIDER_BASE_URL=https://your-server.com
    FASTMCP_SERVER_AUTH_DESCOPEPROVIDER_DESCOPE_BASE_URL=https://api.descope.com
    

With environment variables set, your server code simplifies to:

server.py

Copy

    from fastmcp import FastMCP
    
    # Authentication is automatically configured from environment
    mcp = FastMCP(name="My Descope Protected Server")
    

[Azure (Microsoft Entra ID) OAuth 🤝 FastMCP\
\
Previous](https://gofastmcp.com/integrations/azure)
[GitHub OAuth 🤝 FastMCP\
\
Next](https://gofastmcp.com/integrations/github)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.