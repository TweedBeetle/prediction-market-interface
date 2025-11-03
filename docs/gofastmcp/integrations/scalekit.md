---
url: https://gofastmcp.com/integrations/scalekit
title: Scalekit 🤝 FastMCP - FastMCP
description: Secure your FastMCP server with Scalekit
scraped_at: 2025-11-03T18:42:21.090783
---

[Skip to main content](https://gofastmcp.com/integrations/scalekit#content-area)

Join the [FastMCP community](https://discord.gg/uu8dJCgttd)
!

[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)

Search...

Navigation

Authentication

Scalekit 🤝 FastMCP

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

*   [Configuration](https://gofastmcp.com/integrations/scalekit#configuration)
    
*   [Prerequisites](https://gofastmcp.com/integrations/scalekit#prerequisites)
    
*   [Step 1: Configure MCP server in Scalekit environment](https://gofastmcp.com/integrations/scalekit#step-1%3A-configure-mcp-server-in-scalekit-environment)
    
*   [Step 2: Add auth to FastMCP server](https://gofastmcp.com/integrations/scalekit#step-2%3A-add-auth-to-fastmcp-server)
    
*   [Testing](https://gofastmcp.com/integrations/scalekit#testing)
    
*   [Start the MCP server](https://gofastmcp.com/integrations/scalekit#start-the-mcp-server)
    
*   [Provider selection](https://gofastmcp.com/integrations/scalekit#provider-selection)
    
*   [Scalekit-specific configuration](https://gofastmcp.com/integrations/scalekit#scalekit-specific-configuration)
    
*   [Capabilities](https://gofastmcp.com/integrations/scalekit#capabilities)
    
*   [Debugging](https://gofastmcp.com/integrations/scalekit#debugging)
    
*   [Token inspection](https://gofastmcp.com/integrations/scalekit#token-inspection)
    

`` New in version: `2.12.5` `` Install auth stack to your FastMCP server with [Scalekit](https://scalekit.com/)
 using the [Remote OAuth](https://gofastmcp.com/servers/auth/remote-oauth)
 pattern: Scalekit handles user authentication, and the MCP server validates issued tokens.

[​](https://gofastmcp.com/integrations/scalekit#configuration)

Configuration
-------------------------------------------------------------------------------

### 

[​](https://gofastmcp.com/integrations/scalekit#prerequisites)

Prerequisites

Before you begin

1.  Get a [Scalekit account](https://app.scalekit.com/)
     and grab API credentials such as **Client ID**, **Client Secret** and **Environment URL** from _Dashboard > Developers > Settings_.
2.  Have your FastMCP server’s endpoint ready (can be localhost for development, e.g., `http://localhost:8000/mcp`)

### 

[​](https://gofastmcp.com/integrations/scalekit#step-1%3A-configure-mcp-server-in-scalekit-environment)

Step 1: Configure MCP server in Scalekit environment

1

Register MCP server and set environment

In your Scalekit dashboard:

1.  Open the **MCP Servers** section, then select **Create new server**
2.  Enter server details: a name, a resource identifier, and the desired MCP client authentication settings
3.  Save, then copy the **Resource ID** (for example, res\_92015146095)

In your FastMCP project’s `.env`:

Copy

    SCALEKIT_ENVIRONMENT_URL=<YOUR_APP_ENVIRONMENT_URL>
    SCALEKIT_CLIENT_ID=<YOUR_APP_CLIENT_ID> # skc_7008EXAMPLE46
    SCALEKIT_RESOURCE_ID=<YOUR_APP_RESOURCE_ID> # res_926EXAMPLE5878
    MCP_URL=http://localhost:8000/mcp
    

### 

[​](https://gofastmcp.com/integrations/scalekit#step-2%3A-add-auth-to-fastmcp-server)

Step 2: Add auth to FastMCP server

Create your FastMCP server file and use the ScalekitProvider to handle all the OAuth integration automatically:

server.py

Copy

    from fastmcp import FastMCP
    from fastmcp.server.auth.providers.scalekit import ScalekitProvider
    
    # Discovers Scalekit endpoints and set up JWT token validation
    auth_provider = ScalekitProvider(
        environment_url=SCALEKIT_ENVIRONMENT_URL,    # Scalekit environment URL
        client_id=SCALEKIT_CLIENT_ID,                # OAuth client ID
        resource_id=SCALEKIT_RESOURCE_ID,            # Resource server ID
        mcp_url=SERVER_URL,                          # Is also aud claim
    )
    
    # Create FastMCP server with auth
    mcp = FastMCP(name="My Scalekit Protected Server", auth=auth_provider)
    
    @mcp.tool
    def auth_status() -> dict:
        """Show Scalekit authentication status."""
        # Extract user claims from the JWT
        return {
            "message": "This tool requires authentication via Scalekit",
            "authenticated": True,
            "provider": "Scalekit"
        }
    
    

[​](https://gofastmcp.com/integrations/scalekit#testing)

Testing
-------------------------------------------------------------------

### 

[​](https://gofastmcp.com/integrations/scalekit#start-the-mcp-server)

Start the MCP server

Copy

    uv run python server.py
    

Use any MCP client (for example, mcp-inspector, Claude, VS Code, or Windsurf) to connect to the running serve. Verify that authentication succeeds and requests are authorized as expected.

### 

[​](https://gofastmcp.com/integrations/scalekit#provider-selection)

Provider selection

Setting this environment variable allows the Scalekit provider to be used automatically without explicitly instantiating it in code.

[​](https://gofastmcp.com/integrations/scalekit#param-fastmcp-server-auth)

FASTMCP\_SERVER\_AUTH

default:"Not set"

Set to `fastmcp.server.auth.providers.scalekit.ScalekitProvider` to use Scalekit authentication.

### 

[​](https://gofastmcp.com/integrations/scalekit#scalekit-specific-configuration)

Scalekit-specific configuration

These environment variables provide default values for the Scalekit provider, whether it’s instantiated manually or configured via `FASTMCP_SERVER_AUTH`.

[​](https://gofastmcp.com/integrations/scalekit#param-fastmcp-server-auth-scalekitprovider-environment-url)

FASTMCP\_SERVER\_AUTH\_SCALEKITPROVIDER\_ENVIRONMENT\_URL

required

Your Scalekit environment URL from the Admin Portal (e.g., `https://your-env.scalekit.com`)

[​](https://gofastmcp.com/integrations/scalekit#param-fastmcp-server-auth-scalekitprovider-client-id)

FASTMCP\_SERVER\_AUTH\_SCALEKITPROVIDER\_CLIENT\_ID

required

Your Scalekit OAuth application client ID from the Applications section

[​](https://gofastmcp.com/integrations/scalekit#param-fastmcp-server-auth-scalekitprovider-resource-id)

FASTMCP\_SERVER\_AUTH\_SCALEKITPROVIDER\_RESOURCE\_ID

required

Your Scalekit resource server ID from the Resources section

[​](https://gofastmcp.com/integrations/scalekit#param-fastmcp-server-auth-scalekitprovider-mcp-url)

FASTMCP\_SERVER\_AUTH\_SCALEKITPROVIDER\_MCP\_URL

required

Public URL of your FastMCP server (e.g., `https://your-server.com` or `http://localhost:8000/mcp` for development)

Example `.env`:

Copy

    # Use the Scalekit provider
    FASTMCP_SERVER_AUTH=fastmcp.server.auth.providers.scalekit.ScalekitProvider
    
    # Scalekit configuration
    FASTMCP_SERVER_AUTH_SCALEKITPROVIDER_ENVIRONMENT_URL=https://your-env.scalekit.com
    FASTMCP_SERVER_AUTH_SCALEKITPROVIDER_CLIENT_ID=skc_123
    FASTMCP_SERVER_AUTH_SCALEKITPROVIDER_RESOURCE_ID=res_456
    FASTMCP_SERVER_AUTH_SCALEKITPROVIDER_MCP_URL=https://your-server.com/mcp
    

With environment variables set, your server code simplifies to:

server.py

Copy

    from fastmcp import FastMCP
    
    # Authentication is automatically configured from environment
    mcp = FastMCP(name="My Scalekit Protected Server")
    
    @mcp.tool
    def protected_action() -> str:
        """A tool that requires authentication."""
        return "Access granted via Scalekit!"
    

[​](https://gofastmcp.com/integrations/scalekit#capabilities)

Capabilities
-----------------------------------------------------------------------------

Scalekit supports OAuth 2.1 with Dynamic Client Registration for MCP clients and enterprise SSO, and provides built‑in JWT validation and security controls. **OAuth 2.1/DCR**: clients self‑register, use PKCE, and work with the Remote OAuth pattern without pre‑provisioned credentials. **Validation and SSO**: tokens are verified (keys, RS256, issuer, audience, expiry), and SAML, OIDC, OAuth 2.0, ADFS, Azure AD, and Google Workspace are supported; use HTTPS in production and review auth logs as needed.

[​](https://gofastmcp.com/integrations/scalekit#debugging)

Debugging
-----------------------------------------------------------------------

Enable detailed logging to troubleshoot authentication issues:

Copy

    import logging
    logging.basicConfig(level=logging.DEBUG)
    

### 

[​](https://gofastmcp.com/integrations/scalekit#token-inspection)

Token inspection

You can inspect JWT tokens in your tools to understand the user context:

Copy

    from fastmcp.server.context import request_ctx
    import jwt
    
    @mcp.tool
    def inspect_token() -> dict:
        """Inspect the current JWT token claims."""
        context = request_ctx.get()
    
        # Extract token from Authorization header
        if hasattr(context, 'request') and hasattr(context.request, 'headers'):
            auth_header = context.request.headers.get('authorization', '')
            if auth_header.startswith('Bearer '):
                token = auth_header[7:]
                # Decode without verification (already verified by provider)
                claims = jwt.decode(token, options={"verify_signature": False})
                return claims
    
        return {"error": "No token found"}
    

[GitHub OAuth 🤝 FastMCP\
\
Previous](https://gofastmcp.com/integrations/github)
[Google OAuth 🤝 FastMCP\
\
Next](https://gofastmcp.com/integrations/google)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.