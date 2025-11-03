---
url: https://gofastmcp.com/integrations/github
title: GitHub OAuth 🤝 FastMCP - FastMCP
description: Secure your FastMCP server with GitHub OAuth
scraped_at: 2025-11-03T18:42:15.564404
---

[Skip to main content](https://gofastmcp.com/integrations/github#content-area)

Join the [FastMCP community](https://discord.gg/uu8dJCgttd)
!

[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)

Search...

Navigation

Authentication

GitHub OAuth 🤝 FastMCP

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

*   [Configuration](https://gofastmcp.com/integrations/github#configuration)
    
*   [Prerequisites](https://gofastmcp.com/integrations/github#prerequisites)
    
*   [Step 1: Create a GitHub OAuth App](https://gofastmcp.com/integrations/github#step-1%3A-create-a-github-oauth-app)
    
*   [Step 2: FastMCP Configuration](https://gofastmcp.com/integrations/github#step-2%3A-fastmcp-configuration)
    
*   [Testing](https://gofastmcp.com/integrations/github#testing)
    
*   [Running the Server](https://gofastmcp.com/integrations/github#running-the-server)
    
*   [Testing with a Client](https://gofastmcp.com/integrations/github#testing-with-a-client)
    
*   [Production Configuration](https://gofastmcp.com/integrations/github#production-configuration)
    
*   [Environment Variables](https://gofastmcp.com/integrations/github#environment-variables)
    
*   [Provider Selection](https://gofastmcp.com/integrations/github#provider-selection)
    
*   [GitHub-Specific Configuration](https://gofastmcp.com/integrations/github#github-specific-configuration)
    

`` New in version: `2.12.0` `` This guide shows you how to secure your FastMCP server using **GitHub OAuth**. Since GitHub doesn’t support Dynamic Client Registration, this integration uses the [**OAuth Proxy**](https://gofastmcp.com/servers/auth/oauth-proxy)
 pattern to bridge GitHub’s traditional OAuth with MCP’s authentication requirements.

[​](https://gofastmcp.com/integrations/github#configuration)

Configuration
-----------------------------------------------------------------------------

### 

[​](https://gofastmcp.com/integrations/github#prerequisites)

Prerequisites

Before you begin, you will need:

1.  A **[GitHub Account](https://github.com/)
    ** with access to create OAuth Apps
2.  Your FastMCP server’s URL (can be localhost for development, e.g., `http://localhost:8000`)

### 

[​](https://gofastmcp.com/integrations/github#step-1%3A-create-a-github-oauth-app)

Step 1: Create a GitHub OAuth App

Create an OAuth App in your GitHub settings to get the credentials needed for authentication:

1

Navigate to OAuth Apps

Go to **Settings → Developer settings → OAuth Apps** in your GitHub account, or visit [github.com/settings/developers](https://github.com/settings/developers)
.Click **“New OAuth App”** to create a new application.

2

Configure Your OAuth App

Fill in the application details:

*   **Application name**: Choose a name users will recognize (e.g., “My FastMCP Server”)
*   **Homepage URL**: Your application’s homepage or documentation URL
*   **Authorization callback URL**: Your server URL + `/auth/callback` (e.g., `http://localhost:8000/auth/callback`)

The callback URL must match exactly. The default path is `/auth/callback`, but you can customize it using the `redirect_path` parameter. For local development, GitHub allows `http://localhost` URLs. For production, you must use HTTPS.

If you want to use a custom callback path (e.g., `/auth/github/callback`), make sure to set the same path in both your GitHub OAuth App settings and the `redirect_path` parameter when configuring the GitHubProvider.

3

Save Your Credentials

After creating the app, you’ll see:

*   **Client ID**: A public identifier like `Ov23liAbcDefGhiJkLmN`
*   **Client Secret**: Click “Generate a new client secret” and save the value securely

Store these credentials securely. Never commit them to version control. Use environment variables or a secrets manager in production.

### 

[​](https://gofastmcp.com/integrations/github#step-2%3A-fastmcp-configuration)

Step 2: FastMCP Configuration

Create your FastMCP server using the `GitHubProvider`, which handles GitHub’s OAuth quirks automatically:

server.py

Copy

    from fastmcp import FastMCP
    from fastmcp.server.auth.providers.github import GitHubProvider
    
    # The GitHubProvider handles GitHub's token format and validation
    auth_provider = GitHubProvider(
        client_id="Ov23liAbcDefGhiJkLmN",  # Your GitHub OAuth App Client ID
        client_secret="github_pat_...",     # Your GitHub OAuth App Client Secret
        base_url="http://localhost:8000",   # Must match your OAuth App configuration
        # redirect_path="/auth/callback"   # Default value, customize if needed
    )
    
    mcp = FastMCP(name="GitHub Secured App", auth=auth_provider)
    
    # Add a protected tool to test authentication
    @mcp.tool
    async def get_user_info() -> dict:
        """Returns information about the authenticated GitHub user."""
        from fastmcp.server.dependencies import get_access_token
        
        token = get_access_token()
        # The GitHubProvider stores user data in token claims
        return {
            "github_user": token.claims.get("login"),
            "name": token.claims.get("name"),
            "email": token.claims.get("email")
        }
    

[​](https://gofastmcp.com/integrations/github#testing)

Testing
-----------------------------------------------------------------

### 

[​](https://gofastmcp.com/integrations/github#running-the-server)

Running the Server

Start your FastMCP server with HTTP transport to enable OAuth flows:

Copy

    fastmcp run server.py --transport http --port 8000
    

Your server is now running and protected by GitHub OAuth authentication.

### 

[​](https://gofastmcp.com/integrations/github#testing-with-a-client)

Testing with a Client

Create a test client that authenticates with your GitHub-protected server:

test\_client.py

Copy

    from fastmcp import Client
    import asyncio
    
    async def main():
        # The client will automatically handle GitHub OAuth
        async with Client("http://localhost:8000/mcp", auth="oauth") as client:
            # First-time connection will open GitHub login in your browser
            print("✓ Authenticated with GitHub!")
            
            # Test the protected tool
            result = await client.call_tool("get_user_info")
            print(f"GitHub user: {result['github_user']}")
    
    if __name__ == "__main__":
        asyncio.run(main())
    

When you run the client for the first time:

1.  Your browser will open to GitHub’s authorization page
2.  After you authorize the app, you’ll be redirected back
3.  The client receives the token and can make authenticated requests

The client caches tokens locally, so you won’t need to re-authenticate for subsequent runs unless the token expires or you explicitly clear the cache.

[​](https://gofastmcp.com/integrations/github#production-configuration)

Production Configuration
---------------------------------------------------------------------------------------------------

`` New in version: `2.13.0` `` For production deployments with persistent token management across server restarts, configure `jwt_signing_key` and `client_storage`:

server.py

Copy

    import os
    from fastmcp import FastMCP
    from fastmcp.server.auth.providers.github import GitHubProvider
    from key_value.aio.stores.redis import RedisStore
    from key_value.aio.wrappers.encryption import FernetEncryptionWrapper
    from cryptography.fernet import Fernet
    
    # Production setup with encrypted persistent token storage
    auth_provider = GitHubProvider(
        client_id="Ov23liAbcDefGhiJkLmN",
        client_secret="github_pat_...",
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
    
    mcp = FastMCP(name="Production GitHub App", auth=auth_provider)
    

Parameters (`jwt_signing_key` and `client_storage`) work together to ensure tokens and client registrations survive server restarts. **Wrap your storage in `FernetEncryptionWrapper` to encrypt sensitive OAuth tokens at rest** - without it, tokens are stored in plaintext. Store secrets in environment variables and use a persistent storage backend like Redis for distributed deployments.For complete details on these parameters, see the [OAuth Proxy documentation](https://gofastmcp.com/servers/auth/oauth-proxy#configuration-parameters)
.

[​](https://gofastmcp.com/integrations/github#environment-variables)

Environment Variables
---------------------------------------------------------------------------------------------

`` New in version: `2.12.1` `` For production deployments, use environment variables instead of hardcoding credentials.

### 

[​](https://gofastmcp.com/integrations/github#provider-selection)

Provider Selection

Setting this environment variable allows the GitHub provider to be used automatically without explicitly instantiating it in code.

[​](https://gofastmcp.com/integrations/github#param-fastmcp-server-auth)

FASTMCP\_SERVER\_AUTH

default:"Not set"

Set to `fastmcp.server.auth.providers.github.GitHubProvider` to use GitHub authentication.

### 

[​](https://gofastmcp.com/integrations/github#github-specific-configuration)

GitHub-Specific Configuration

These environment variables provide default values for the GitHub provider, whether it’s instantiated manually or configured via `FASTMCP_SERVER_AUTH`.

[​](https://gofastmcp.com/integrations/github#param-fastmcp-server-auth-github-client-id)

FASTMCP\_SERVER\_AUTH\_GITHUB\_CLIENT\_ID

required

Your GitHub OAuth App Client ID (e.g., `Ov23liAbcDefGhiJkLmN`)

[​](https://gofastmcp.com/integrations/github#param-fastmcp-server-auth-github-client-secret)

FASTMCP\_SERVER\_AUTH\_GITHUB\_CLIENT\_SECRET

required

Your GitHub OAuth App Client Secret

[​](https://gofastmcp.com/integrations/github#param-fastmcp-server-auth-github-base-url)

FASTMCP\_SERVER\_AUTH\_GITHUB\_BASE\_URL

default:"http://localhost:8000"

Public URL where OAuth endpoints will be accessible (includes any mount path)

[​](https://gofastmcp.com/integrations/github#param-fastmcp-server-auth-github-issuer-url)

FASTMCP\_SERVER\_AUTH\_GITHUB\_ISSUER\_URL

default:"Uses BASE\_URL"

Issuer URL for OAuth metadata (defaults to `BASE_URL`). Set to root-level URL when mounting under a path prefix to avoid 404 logs. See [HTTP Deployment guide](https://gofastmcp.com/deployment/http#mounting-authenticated-servers)
 for details.

[​](https://gofastmcp.com/integrations/github#param-fastmcp-server-auth-github-redirect-path)

FASTMCP\_SERVER\_AUTH\_GITHUB\_REDIRECT\_PATH

default:"/auth/callback"

Redirect path configured in your GitHub OAuth App

[​](https://gofastmcp.com/integrations/github#param-fastmcp-server-auth-github-required-scopes)

FASTMCP\_SERVER\_AUTH\_GITHUB\_REQUIRED\_SCOPES

default:"\[\\"user\\"\]"

Comma-, space-, or JSON-separated list of required GitHub scopes (e.g., `user repo` or `["user","repo"]`)

[​](https://gofastmcp.com/integrations/github#param-fastmcp-server-auth-github-timeout-seconds)

FASTMCP\_SERVER\_AUTH\_GITHUB\_TIMEOUT\_SECONDS

default:"10"

HTTP request timeout for GitHub API calls

Example `.env` file:

Copy

    # Use the GitHub provider
    FASTMCP_SERVER_AUTH=fastmcp.server.auth.providers.github.GitHubProvider
    
    # GitHub OAuth credentials
    FASTMCP_SERVER_AUTH_GITHUB_CLIENT_ID=Ov23liAbcDefGhiJkLmN
    FASTMCP_SERVER_AUTH_GITHUB_CLIENT_SECRET=github_pat_...
    FASTMCP_SERVER_AUTH_GITHUB_BASE_URL=https://your-server.com
    FASTMCP_SERVER_AUTH_GITHUB_REQUIRED_SCOPES=user,repo
    

With environment variables set, your server code simplifies to:

server.py

Copy

    from fastmcp import FastMCP
    
    # Authentication is automatically configured from environment
    mcp = FastMCP(name="GitHub Secured App")
    
    @mcp.tool
    async def list_repos() -> list[str]:
        """List the authenticated user's repositories."""
        # Your tool implementation here
        pass
    

[Descope 🤝 FastMCP\
\
Previous](https://gofastmcp.com/integrations/descope)
[Scalekit 🤝 FastMCP\
\
Next](https://gofastmcp.com/integrations/scalekit)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.