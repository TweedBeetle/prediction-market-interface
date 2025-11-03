---
url: https://gofastmcp.com/integrations/auth0
title: Auth0 OAuth 🤝 FastMCP - FastMCP
description: Secure your FastMCP server with Auth0 OAuth
scraped_at: 2025-11-03T18:42:09.029572
---

[Skip to main content](https://gofastmcp.com/integrations/auth0#content-area)

Join the [FastMCP community](https://discord.gg/uu8dJCgttd)
!

[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)

Search...

Navigation

Authentication

Auth0 OAuth 🤝 FastMCP

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

*   [Configuration](https://gofastmcp.com/integrations/auth0#configuration)
    
*   [Prerequisites](https://gofastmcp.com/integrations/auth0#prerequisites)
    
*   [Step 1: Create an Auth0 Application](https://gofastmcp.com/integrations/auth0#step-1%3A-create-an-auth0-application)
    
*   [Step 2: FastMCP Configuration](https://gofastmcp.com/integrations/auth0#step-2%3A-fastmcp-configuration)
    
*   [Testing](https://gofastmcp.com/integrations/auth0#testing)
    
*   [Running the Server](https://gofastmcp.com/integrations/auth0#running-the-server)
    
*   [Testing with a Client](https://gofastmcp.com/integrations/auth0#testing-with-a-client)
    
*   [Production Configuration](https://gofastmcp.com/integrations/auth0#production-configuration)
    
*   [Environment Variables](https://gofastmcp.com/integrations/auth0#environment-variables)
    
*   [Provider Selection](https://gofastmcp.com/integrations/auth0#provider-selection)
    
*   [Auth0-Specific Configuration](https://gofastmcp.com/integrations/auth0#auth0-specific-configuration)
    

`` New in version: `2.12.4` `` This guide shows you how to secure your FastMCP server using **Auth0 OAuth**. While Auth0 does have support for Dynamic Client Registration, it is not enabled by default so this integration uses the [**OIDC Proxy**](https://gofastmcp.com/servers/auth/oidc-proxy)
 pattern to bridge Auth0’s dynamic OIDC configuration with MCP’s authentication requirements.

[​](https://gofastmcp.com/integrations/auth0#configuration)

Configuration
----------------------------------------------------------------------------

### 

[​](https://gofastmcp.com/integrations/auth0#prerequisites)

Prerequisites

Before you begin, you will need:

1.  An **[Auth0 Account](https://auth0.com/)
    ** with access to create Applications
2.  Your FastMCP server’s URL (can be localhost for development, e.g., `http://localhost:8000`)

### 

[​](https://gofastmcp.com/integrations/auth0#step-1%3A-create-an-auth0-application)

Step 1: Create an Auth0 Application

Create an Application in your Auth0 settings to get the credentials needed for authentication:

1

Navigate to Applications

Go to **Applications → Applications** in your Auth0 account.Click **”+ Create Application”** to create a new application.

2

Create Your Application

*   **Name**: Choose a name users will recognize (e.g., “My FastMCP Server”)
*   **Choose an application type**: Choose “Single Page Web Applications”
*   Click **Create** to create the application

3

Configure Your Application

Select the “Settings” tab for your application, then find the “Application URIs” section.

*   **Allowed Callback URLs**: Your server URL + `/auth/callback` (e.g., `http://localhost:8000/auth/callback`)
*   Click **Save** to save your changes

The callback URL must match exactly. The default path is `/auth/callback`, but you can customize it using the `redirect_path` parameter.

If you want to use a custom callback path (e.g., `/auth/auth0/callback`), make sure to set the same path in both your Auth0 Application settings and the `redirect_path` parameter when configuring the Auth0Provider.

4

Save Your Credentials

After creating the app, in the “Basic Information” section you’ll see:

*   **Client ID**: A public identifier like `tv2ObNgaZAWWhhycr7Bz1LU2mxlnsmsB`
*   **Client Secret**: A private hidden value that should always be stored securely

Store these credentials securely. Never commit them to version control. Use environment variables or a secrets manager in production.

5

Select Your Audience

Go to **Applications → APIs** in your Auth0 account.

*   Find the API that you want to use for your application
*   **API Audience**: A URL that uniquely identifies the API

Store this along with of the credentials above. Never commit this to version control. Use environment variables or a secrets manager in production.

### 

[​](https://gofastmcp.com/integrations/auth0#step-2%3A-fastmcp-configuration)

Step 2: FastMCP Configuration

Create your FastMCP server using the `Auth0Provider`.

server.py

Copy

    from fastmcp import FastMCP
    from fastmcp.server.auth.providers.auth0 import Auth0Provider
    
    # The Auth0Provider utilizes Auth0 OIDC configuration
    auth_provider = Auth0Provider(
        config_url="https://.../.well-known/openid-configuration",  # Your Auth0 configuration URL
        client_id="tv2ObNgaZAWWhhycr7Bz1LU2mxlnsmsB",               # Your Auth0 application Client ID
        client_secret="vPYqbjemq...",                               # Your Auth0 application Client Secret
        audience="https://...",                                     # Your Auth0 API audience
        base_url="http://localhost:8000",                           # Must match your application configuration
        # redirect_path="/auth/callback"                            # Default value, customize if needed
    )
    
    mcp = FastMCP(name="Auth0 Secured App", auth=auth_provider)
    
    # Add a protected tool to test authentication
    @mcp.tool
    async def get_token_info() -> dict:
        """Returns information about the Auth0 token."""
        from fastmcp.server.dependencies import get_access_token
    
        token = get_access_token()
    
        return {
            "issuer": token.claims.get("iss"),
            "audience": token.claims.get("aud"),
            "scope": token.claims.get("scope")
        }
    

[​](https://gofastmcp.com/integrations/auth0#testing)

Testing
----------------------------------------------------------------

### 

[​](https://gofastmcp.com/integrations/auth0#running-the-server)

Running the Server

Start your FastMCP server with HTTP transport to enable OAuth flows:

Copy

    fastmcp run server.py --transport http --port 8000
    

Your server is now running and protected by Auth0 authentication.

### 

[​](https://gofastmcp.com/integrations/auth0#testing-with-a-client)

Testing with a Client

Create a test client that authenticates with your Auth0-protected server:

test\_client.py

Copy

    from fastmcp import Client
    import asyncio
    
    async def main():
        # The client will automatically handle Auth0 OAuth flows
        async with Client("http://localhost:8000/mcp", auth="oauth") as client:
            # First-time connection will open Auth0 login in your browser
            print("✓ Authenticated with Auth0!")
    
            # Test the protected tool
            result = await client.call_tool("get_token_info")
            print(f"Auth0 audience: {result['audience']}")
    
    if __name__ == "__main__":
        asyncio.run(main())
    

When you run the client for the first time:

1.  Your browser will open to Auth0’s authorization page
2.  After you authorize the app, you’ll be redirected back
3.  The client receives the token and can make authenticated requests

[​](https://gofastmcp.com/integrations/auth0#production-configuration)

Production Configuration
--------------------------------------------------------------------------------------------------

`` New in version: `2.13.0` `` For production deployments with persistent token management across server restarts, configure `jwt_signing_key`, and `client_storage`:

server.py

Copy

    import os
    from fastmcp import FastMCP
    from fastmcp.server.auth.providers.auth0 import Auth0Provider
    from key_value.aio.stores.redis import RedisStore
    from key_value.aio.wrappers.encryption import FernetEncryptionWrapper
    from cryptography.fernet import Fernet
    
    # Production setup with encrypted persistent token storage
    auth_provider = Auth0Provider(
        config_url="https://.../.well-known/openid-configuration",
        client_id="tv2ObNgaZAWWhhycr7Bz1LU2mxlnsmsB",
        client_secret="vPYqbjemq...",
        audience="https://...",
        base_url="https://your-production-domain.com",
    
        # Production token management
        jwt_signing_key=os.environ["JWT_SIGNING_KEY"],
        client_storage=FernetEncryptionWrapper(
            key_value=RedisStore(
                host=os.environ["REDIS_HOST"],
                port=int(os.environ["REDIS_PORT"])
            ),
            fernet=Fernet(os.environ["STORAGE_ENCRYPTION_KEY"])
        )
    )
    
    mcp = FastMCP(name="Production Auth0 App", auth=auth_provider)
    

Parameters (`jwt_signing_key` and `client_storage`) work together to ensure tokens and client registrations survive server restarts. **Wrap your storage in `FernetEncryptionWrapper` to encrypt sensitive OAuth tokens at rest** - without it, tokens are stored in plaintext. Store secrets in environment variables and use a persistent storage backend like Redis for distributed deployments.For complete details on these parameters, see the [OAuth Proxy documentation](https://gofastmcp.com/servers/auth/oauth-proxy#configuration-parameters)
.

The client caches tokens locally, so you won’t need to re-authenticate for subsequent runs unless the token expires or you explicitly clear the cache.

[​](https://gofastmcp.com/integrations/auth0#environment-variables)

Environment Variables
--------------------------------------------------------------------------------------------

For production deployments, use environment variables instead of hardcoding credentials.

### 

[​](https://gofastmcp.com/integrations/auth0#provider-selection)

Provider Selection

Setting this environment variable allows the Auth0 provider to be used automatically without explicitly instantiating it in code.

[​](https://gofastmcp.com/integrations/auth0#param-fastmcp-server-auth)

FASTMCP\_SERVER\_AUTH

default:"Not set"

Set to `fastmcp.server.auth.providers.auth0.Auth0Provider` to use Auth0 authentication.

### 

[​](https://gofastmcp.com/integrations/auth0#auth0-specific-configuration)

Auth0-Specific Configuration

These environment variables provide default values for the Auth0 provider, whether it’s instantiated manually or configured via `FASTMCP_SERVER_AUTH`.

[​](https://gofastmcp.com/integrations/auth0#param-fastmcp-server-auth-auth-0-config-url)

FASTMCP\_SERVER\_AUTH\_AUTH0\_CONFIG\_URL

required

Your Auth0 Application Configuration URL (e.g., `https://.../.well-known/openid-configuration`)

[​](https://gofastmcp.com/integrations/auth0#param-fastmcp-server-auth-auth-0-client-id)

FASTMCP\_SERVER\_AUTH\_AUTH0\_CLIENT\_ID

required

Your Auth0 Application Client ID (e.g., `tv2ObNgaZAWWhhycr7Bz1LU2mxlnsmsB`)

[​](https://gofastmcp.com/integrations/auth0#param-fastmcp-server-auth-auth-0-client-secret)

FASTMCP\_SERVER\_AUTH\_AUTH0\_CLIENT\_SECRET

required

Your Auth0 Application Client Secret (e.g., `vPYqbjemq...`)

[​](https://gofastmcp.com/integrations/auth0#param-fastmcp-server-auth-auth-0-audience)

FASTMCP\_SERVER\_AUTH\_AUTH0\_AUDIENCE

required

Your Auth0 API Audience

[​](https://gofastmcp.com/integrations/auth0#param-fastmcp-server-auth-auth-0-base-url)

FASTMCP\_SERVER\_AUTH\_AUTH0\_BASE\_URL

required

Public URL where OAuth endpoints will be accessible (includes any mount path)

[​](https://gofastmcp.com/integrations/auth0#param-fastmcp-server-auth-auth-0-issuer-url)

FASTMCP\_SERVER\_AUTH\_AUTH0\_ISSUER\_URL

default:"Uses BASE\_URL"

Issuer URL for OAuth metadata (defaults to `BASE_URL`). Set to root-level URL when mounting under a path prefix to avoid 404 logs. See [HTTP Deployment guide](https://gofastmcp.com/deployment/http#mounting-authenticated-servers)
 for details.

[​](https://gofastmcp.com/integrations/auth0#param-fastmcp-server-auth-auth-0-redirect-path)

FASTMCP\_SERVER\_AUTH\_AUTH0\_REDIRECT\_PATH

default:"/auth/callback"

Redirect path configured in your Auth0 Application

[​](https://gofastmcp.com/integrations/auth0#param-fastmcp-server-auth-auth-0-required-scopes)

FASTMCP\_SERVER\_AUTH\_AUTH0\_REQUIRED\_SCOPES

default:"\[\\"openid\\"\]"

Comma-, space-, or JSON-separated list of required AUth0 scopes (e.g., `openid email` or `["openid","email"]`)

Example `.env` file:

Copy

    # Use the Auth0 provider
    FASTMCP_SERVER_AUTH=fastmcp.server.auth.providers.auth0.Auth0Provider
    
    # Auth0 configuration and credentials
    FASTMCP_SERVER_AUTH_AUTH0_CONFIG_URL=https://.../.well-known/openid-configuration
    FASTMCP_SERVER_AUTH_AUTH0_CLIENT_ID=tv2ObNgaZAWWhhycr7Bz1LU2mxlnsmsB
    FASTMCP_SERVER_AUTH_AUTH0_CLIENT_SECRET=vPYqbjemq...
    FASTMCP_SERVER_AUTH_AUTH0_AUDIENCE=https://...
    FASTMCP_SERVER_AUTH_AUTH0_BASE_URL=https://your-server.com
    FASTMCP_SERVER_AUTH_AUTH0_REQUIRED_SCOPES=openid,email
    

With environment variables set, your server code simplifies to:

server.py

Copy

    from fastmcp import FastMCP
    
    # Authentication is automatically configured from environment
    mcp = FastMCP(name="Auth0 Secured App")
    
    @mcp.tool
    async def search_logs() -> list[str]:
        """Search the service logs."""
        # Your tool implementation here
        pass
    

[Bearer Token Authentication\
\
Previous](https://gofastmcp.com/clients/auth/bearer)
[AuthKit 🤝 FastMCP\
\
Next](https://gofastmcp.com/integrations/authkit)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.