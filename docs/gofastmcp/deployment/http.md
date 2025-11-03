---
url: https://gofastmcp.com/deployment/http
title: HTTP Deployment - FastMCP
description: Deploy your FastMCP server over HTTP for remote access
scraped_at: 2025-11-03T18:42:03.447585
---

[Skip to main content](https://gofastmcp.com/deployment/http#content-area)

Join the [FastMCP community](https://discord.gg/uu8dJCgttd)
!

[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)

Search...

Navigation

Deployment

HTTP Deployment

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
    
    *   [Running Your Server](https://gofastmcp.com/deployment/running-server)
        
    *   [HTTP Deployment\
        \
        NEW](https://gofastmcp.com/deployment/http)
        
    *   [FastMCP Cloud\
        \
        NEW](https://gofastmcp.com/deployment/fastmcp-cloud)
        
    *   [Project Configuration](https://gofastmcp.com/deployment/server-configuration)
        

##### Clients

*   Essentials
    
*   Core Operations
    
*   Advanced Features
    
*   Authentication
    

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

*   [Choosing Your Approach](https://gofastmcp.com/deployment/http#choosing-your-approach)
    
*   [Direct HTTP Server](https://gofastmcp.com/deployment/http#direct-http-server)
    
*   [ASGI Application](https://gofastmcp.com/deployment/http#asgi-application)
    
*   [Configuring Your Server](https://gofastmcp.com/deployment/http#configuring-your-server)
    
*   [Custom Path](https://gofastmcp.com/deployment/http#custom-path)
    
*   [Authentication](https://gofastmcp.com/deployment/http#authentication)
    
*   [Health Checks](https://gofastmcp.com/deployment/http#health-checks)
    
*   [Custom Middleware](https://gofastmcp.com/deployment/http#custom-middleware)
    
*   [CORS for Browser-Based Clients](https://gofastmcp.com/deployment/http#cors-for-browser-based-clients)
    
*   [Integration with Web Frameworks](https://gofastmcp.com/deployment/http#integration-with-web-frameworks)
    
*   [Mounting in Starlette](https://gofastmcp.com/deployment/http#mounting-in-starlette)
    
*   [Nested Mounts](https://gofastmcp.com/deployment/http#nested-mounts)
    
*   [FastAPI Integration](https://gofastmcp.com/deployment/http#fastapi-integration)
    
*   [Mounting Authenticated Servers](https://gofastmcp.com/deployment/http#mounting-authenticated-servers)
    
*   [Route Types](https://gofastmcp.com/deployment/http#route-types)
    
*   [Configuration Parameters](https://gofastmcp.com/deployment/http#configuration-parameters)
    
*   [Mounting Strategy](https://gofastmcp.com/deployment/http#mounting-strategy)
    
*   [Complete Example](https://gofastmcp.com/deployment/http#complete-example)
    
*   [Production Deployment](https://gofastmcp.com/deployment/http#production-deployment)
    
*   [Running with Uvicorn](https://gofastmcp.com/deployment/http#running-with-uvicorn)
    
*   [Environment Variables](https://gofastmcp.com/deployment/http#environment-variables)
    
*   [OAuth Token Security](https://gofastmcp.com/deployment/http#oauth-token-security)
    
*   [Testing Your Deployment](https://gofastmcp.com/deployment/http#testing-your-deployment)
    
*   [Hosting Your Server](https://gofastmcp.com/deployment/http#hosting-your-server)
    

STDIO transport is perfect for local development and desktop applications. But to unlock the full potential of MCP—centralized services, multi-client access, and network availability—you need remote HTTP deployment.

This guide walks you through deploying your FastMCP server as a remote MCP service that’s accessible via a URL. Once deployed, your MCP server will be available over the network, allowing multiple clients to connect simultaneously and enabling integration with cloud-based LLM applications. This guide focuses specifically on remote MCP deployment, not local STDIO servers.

[​](https://gofastmcp.com/deployment/http#choosing-your-approach)

Choosing Your Approach
-------------------------------------------------------------------------------------------

FastMCP provides two ways to deploy your server as an HTTP service. Understanding the trade-offs helps you choose the right approach for your needs. The **direct HTTP server** approach is simpler and perfect for getting started quickly. You modify your server’s `run()` method to use HTTP transport, and FastMCP handles all the web server configuration. This approach works well for standalone deployments where you want your MCP server to be the only service running on a port. The **ASGI application** approach gives you more control and flexibility. Instead of running the server directly, you create an ASGI application that can be served by Uvicorn. This approach is better when you need advanced server features like multiple workers, custom middleware, or when you’re integrating with existing web applications.

### 

[​](https://gofastmcp.com/deployment/http#direct-http-server)

Direct HTTP Server

The simplest way to get your MCP server online is to use the built-in `run()` method with HTTP transport. This approach handles all the server configuration for you and is ideal when you want a standalone MCP server without additional complexity.

server.py

Copy

    from fastmcp import FastMCP
    
    mcp = FastMCP("My Server")
    
    @mcp.tool
    def process_data(input: str) -> str:
        """Process data on the server"""
        return f"Processed: {input}"
    
    if __name__ == "__main__":
        mcp.run(transport="http", host="0.0.0.0", port=8000)
    

Run your server with a simple Python command:

Copy

    python server.py
    

Your server is now accessible at `http://localhost:8000/mcp` (or use your server’s actual IP address for remote access). This approach is ideal when you want to get online quickly with minimal configuration. It’s perfect for internal tools, development environments, or simple deployments where you don’t need advanced server features. The built-in server handles all the HTTP details, letting you focus on your MCP implementation.

### 

[​](https://gofastmcp.com/deployment/http#asgi-application)

ASGI Application

For production deployments, you’ll often want more control over how your server runs. FastMCP can create a standard ASGI application that works with any ASGI server like Uvicorn, Gunicorn, or Hypercorn. This approach is particularly useful when you need to configure advanced server options, run multiple workers, or integrate with existing infrastructure.

app.py

Copy

    from fastmcp import FastMCP
    
    mcp = FastMCP("My Server")
    
    @mcp.tool
    def process_data(input: str) -> str:
        """Process data on the server"""
        return f"Processed: {input}"
    
    # Create ASGI application
    app = mcp.http_app()
    

Run with any ASGI server - here’s an example with Uvicorn:

Copy

    uvicorn app:app --host 0.0.0.0 --port 8000
    

Your server is accessible at the same URL: `http://localhost:8000/mcp` (or use your server’s actual IP address for remote access). The ASGI approach shines in production environments where you need reliability and performance. You can run multiple worker processes to handle concurrent requests, add custom middleware for logging or monitoring, integrate with existing deployment pipelines, or mount your MCP server as part of a larger application.

[​](https://gofastmcp.com/deployment/http#configuring-your-server)

Configuring Your Server
---------------------------------------------------------------------------------------------

### 

[​](https://gofastmcp.com/deployment/http#custom-path)

Custom Path

By default, your MCP server is accessible at `/mcp/` on your domain. You can customize this path to fit your URL structure or avoid conflicts with existing endpoints. This is particularly useful when integrating MCP into an existing application or following specific API conventions.

Copy

    # Option 1: With mcp.run()
    mcp.run(transport="http", host="0.0.0.0", port=8000, path="/api/mcp/")
    
    # Option 2: With ASGI app
    app = mcp.http_app(path="/api/mcp/")
    

Now your server is accessible at `http://localhost:8000/api/mcp/`.

### 

[​](https://gofastmcp.com/deployment/http#authentication)

Authentication

Authentication is **highly recommended** for remote MCP servers. Some LLM clients require authentication for remote servers and will refuse to connect without it.

FastMCP supports multiple authentication methods to secure your remote server. See the [Authentication Overview](https://gofastmcp.com/servers/auth/authentication)
 for complete configuration options including Bearer tokens, JWT, and OAuth. If you’re mounting an authenticated server under a path prefix, see [Mounting Authenticated Servers](https://gofastmcp.com/deployment/http#mounting-authenticated-servers)
 below for important routing considerations.

### 

[​](https://gofastmcp.com/deployment/http#health-checks)

Health Checks

Health check endpoints are essential for monitoring your deployed server and ensuring it’s responding correctly. FastMCP allows you to add custom routes alongside your MCP endpoints, making it easy to implement health checks that work with both deployment approaches.

Copy

    from starlette.responses import JSONResponse
    
    @mcp.custom_route("/health", methods=["GET"])
    async def health_check(request):
        return JSONResponse({"status": "healthy", "service": "mcp-server"})
    

This health endpoint will be available at `http://localhost:8000/health` and can be used by load balancers, monitoring systems, or deployment platforms to verify your server is running.

### 

[​](https://gofastmcp.com/deployment/http#custom-middleware)

Custom Middleware

`` New in version: `2.3.2` `` Add custom Starlette middleware to your FastMCP ASGI apps:

Copy

    from fastmcp import FastMCP
    from starlette.middleware import Middleware
    from starlette.middleware.cors import CORSMiddleware
    
    # Create your FastMCP server
    mcp = FastMCP("MyServer")
    
    # Define middleware
    middleware = [\
        Middleware(\
            CORSMiddleware,\
            allow_origins=["*"],\
            allow_methods=["*"],\
            allow_headers=["*"],\
        )\
    ]
    
    # Create ASGI app with middleware
    http_app = mcp.http_app(middleware=middleware)
    

### 

[​](https://gofastmcp.com/deployment/http#cors-for-browser-based-clients)

CORS for Browser-Based Clients

Most MCP clients, including those that you access through a browser like ChatGPT or Claude, don’t need CORS configuration. Only enable CORS if you’re working with an MCP client that connects directly from a browser, such as debugging tools or inspectors.

CORS (Cross-Origin Resource Sharing) is needed when JavaScript running in a web browser connects directly to your MCP server. This is different from using an LLM through a browser—in that case, the browser connects to the LLM service, and the LLM service connects to your MCP server (no CORS needed). Browser-based MCP clients that need CORS include:

*   **MCP Inspector** - Browser-based debugging tool for testing MCP servers
*   **Custom browser-based MCP clients** - If you’re building a web app that directly connects to MCP servers

For these scenarios, add CORS middleware with the specific headers required for MCP protocol:

Copy

    from fastmcp import FastMCP
    from starlette.middleware import Middleware
    from starlette.middleware.cors import CORSMiddleware
    
    mcp = FastMCP("MyServer")
    
    # Configure CORS for browser-based clients
    middleware = [\
        Middleware(\
            CORSMiddleware,\
            allow_origins=["*"],  # Allow all origins; use specific origins for security\
            allow_methods=["GET", "POST", "DELETE", "OPTIONS"],\
            allow_headers=[\
                "mcp-protocol-version",\
                "mcp-session-id",\
                "Authorization",\
                "Content-Type",\
            ],\
            expose_headers=["mcp-session-id"],\
        )\
    ]
    
    app = mcp.http_app(middleware=middleware)
    

**Key configuration details:**

*   **`allow_origins`**: Specify exact origins (e.g., `["http://localhost:3000"]`) rather than `["*"]` for production deployments
*   **`allow_headers`**: Must include `mcp-protocol-version`, `mcp-session-id`, and `Authorization` (for authenticated servers)
*   **`expose_headers`**: Must include `mcp-session-id` so JavaScript can read the session ID from responses and send it in subsequent requests

Without `expose_headers=["mcp-session-id"]`, browsers will receive the session ID but JavaScript won’t be able to access it, causing session management to fail.

**Production Security**: Never use `allow_origins=["*"]` in production. Specify the exact origins of your browser-based clients. Using wildcards exposes your server to unauthorized access from any website.

[​](https://gofastmcp.com/deployment/http#integration-with-web-frameworks)

Integration with Web Frameworks
-------------------------------------------------------------------------------------------------------------

If you already have a web application running, you can add MCP capabilities by mounting a FastMCP server as a sub-application. This allows you to expose MCP tools alongside your existing API endpoints, sharing the same domain and infrastructure. The MCP server becomes just another route in your application, making it easy to manage and deploy.

### 

[​](https://gofastmcp.com/deployment/http#mounting-in-starlette)

Mounting in Starlette

Mount your FastMCP server in a Starlette application:

Copy

    from fastmcp import FastMCP
    from starlette.applications import Starlette
    from starlette.routing import Mount
    
    # Create your FastMCP server
    mcp = FastMCP("MyServer")
    
    @mcp.tool
    def analyze(data: str) -> dict:
        return {"result": f"Analyzed: {data}"}
    
    # Create the ASGI app
    mcp_app = mcp.http_app(path='/mcp')
    
    # Create a Starlette app and mount the MCP server
    app = Starlette(
        routes=[\
            Mount("/mcp-server", app=mcp_app),\
            # Add other routes as needed\
        ],
        lifespan=mcp_app.lifespan,
    )
    

The MCP endpoint will be available at `/mcp-server/mcp/` of the resulting Starlette app.

For Streamable HTTP transport, you **must** pass the lifespan context from the FastMCP app to the resulting Starlette app, as nested lifespans are not recognized. Otherwise, the FastMCP server’s session manager will not be properly initialized.

#### 

[​](https://gofastmcp.com/deployment/http#nested-mounts)

Nested Mounts

You can create complex routing structures by nesting mounts:

Copy

    from fastmcp import FastMCP
    from starlette.applications import Starlette
    from starlette.routing import Mount
    
    # Create your FastMCP server
    mcp = FastMCP("MyServer")
    
    # Create the ASGI app
    mcp_app = mcp.http_app(path='/mcp')
    
    # Create nested application structure
    inner_app = Starlette(routes=[Mount("/inner", app=mcp_app)])
    app = Starlette(
        routes=[Mount("/outer", app=inner_app)],
        lifespan=mcp_app.lifespan,
    )
    

In this setup, the MCP server is accessible at the `/outer/inner/mcp/` path.

### 

[​](https://gofastmcp.com/deployment/http#fastapi-integration)

FastAPI Integration

For FastAPI-specific integration patterns including both mounting MCP servers into FastAPI apps and generating MCP servers from FastAPI apps, see the [FastAPI Integration guide](https://gofastmcp.com/integrations/fastapi)
. Here’s a quick example showing how to add MCP to an existing FastAPI application:

Copy

    from fastapi import FastAPI
    from fastmcp import FastMCP
    
    # Your existing API
    api = FastAPI()
    
    @api.get("/api/status")
    def status():
        return {"status": "ok"}
    
    # Create your MCP server
    mcp = FastMCP("API Tools")
    
    @mcp.tool
    def query_database(query: str) -> dict:
        """Run a database query"""
        return {"result": "data"}
    
    # Mount MCP at /mcp
    api.mount("/mcp", mcp.http_app())
    
    # Run with: uvicorn app:api --host 0.0.0.0 --port 8000
    

Your existing API remains at `http://localhost:8000/api` while MCP is available at `http://localhost:8000/mcp`.

[​](https://gofastmcp.com/deployment/http#mounting-authenticated-servers)

Mounting Authenticated Servers
-----------------------------------------------------------------------------------------------------------

`` New in version: `2.13.0` ``

This section only applies if you’re **mounting an OAuth-protected FastMCP server under a path prefix** (like `/api`) inside another application using `Mount()`.If you’re deploying your FastMCP server at root level without any `Mount()` prefix, the well-known routes are automatically included in `mcp.http_app()` and you don’t need to do anything special.

OAuth specifications (RFC 8414 and RFC 9728) require discovery metadata to be accessible at well-known paths under the root level of your domain. When you mount an OAuth-protected FastMCP server under a path prefix like `/api`, this creates a routing challenge: your operational OAuth endpoints move under the prefix, but discovery endpoints must remain at the root.

**Common Mistakes to Avoid:**

1.  **Forgetting to mount `.well-known` routes at root** - FastMCP cannot do this automatically when your server is mounted under a path prefix. You must explicitly mount well-known routes at the root level.
2.  **Including mount prefix in both base\_url AND mcp\_path** - The mount prefix (like `/api`) should only be in `base_url`, not in `mcp_path`. Otherwise you’ll get double paths. ✅ **Correct:**
    
    Copy
    
        base_url = "http://localhost:8000/api"
        mcp_path = "/mcp"
        # Result: /api/mcp
        
    
    ❌ **Wrong:**
    
    Copy
    
        base_url = "http://localhost:8000/api"
        mcp_path = "/api/mcp"
        # Result: /api/api/mcp (double prefix!)
        
    
3.  **Not setting issuer\_url when mounting** - Without `issuer_url` set to root level, OAuth discovery will attempt path-scoped discovery first (which will 404), adding unnecessary error logs.

Follow the configuration instructions below to set up mounting correctly.

**CORS Middleware Conflicts:**If you’re integrating FastMCP into an existing application with its own CORS middleware, be aware that layering CORS middleware can cause conflicts (such as 404 errors on `.well-known` routes or OPTIONS requests).FastMCP and the MCP SDK already handle CORS for OAuth routes. If you need CORS on your own application routes, consider using the sub-app pattern: mount FastMCP and your routes as separate apps, each with their own middleware, rather than adding application-wide CORS middleware.

### 

[​](https://gofastmcp.com/deployment/http#route-types)

Route Types

OAuth-protected MCP servers expose two categories of routes: **Operational routes** handle the OAuth flow and MCP protocol:

*   `/authorize` - OAuth authorization endpoint
*   `/token` - Token exchange endpoint
*   `/auth/callback` - OAuth callback handler
*   `/mcp` - MCP protocol endpoint

**Discovery routes** provide metadata for OAuth clients:

*   `/.well-known/oauth-authorization-server` - Authorization server metadata
*   `/.well-known/oauth-protected-resource/*` - Protected resource metadata

When you mount your MCP app under a prefix, operational routes move with it, but discovery routes must stay at root level for RFC compliance.

### 

[​](https://gofastmcp.com/deployment/http#configuration-parameters)

Configuration Parameters

Three parameters control where routes are located and how they combine: **`base_url`** tells clients where to find operational endpoints. This includes any Starlette `Mount()` path prefix (e.g., `/api`):

Copy

    base_url="http://localhost:8000/api"  # Includes mount prefix
    

**`mcp_path`** is the internal FastMCP endpoint path, which gets appended to `base_url`:

Copy

    mcp_path="/mcp"  # Internal MCP path, NOT the mount prefix
    

**`issuer_url`** tells clients where to find discovery metadata. This should point to the root level of your server where well-known routes are mounted:

Copy

    issuer_url="http://localhost:8000"  # Root level, no prefix
    

**Key Invariant:** `base_url + mcp_path = actual externally-accessible MCP URL` Example:

*   `base_url`: `http://localhost:8000/api` (mount prefix `/api`)
*   `mcp_path`: `/mcp` (internal path)
*   Result: `http://localhost:8000/api/mcp` (final MCP endpoint)

Note that the mount prefix (`/api` from `Mount("/api", ...)`) goes in `base_url`, while `mcp_path` is just the internal MCP route. Don’t include the mount prefix in both places or you’ll get `/api/api/mcp`.

### 

[​](https://gofastmcp.com/deployment/http#mounting-strategy)

Mounting Strategy

When mounting an OAuth-protected server under a path prefix, declare your URLs upfront to make the relationships clear:

Copy

    from fastmcp import FastMCP
    from fastmcp.server.auth.providers.github import GitHubProvider
    from starlette.applications import Starlette
    from starlette.routing import Mount
    
    # Define the routing structure
    ROOT_URL = "http://localhost:8000"
    MOUNT_PREFIX = "/api"
    MCP_PATH = "/mcp"
    

Create the auth provider with both `issuer_url` and `base_url`:

Copy

    auth = GitHubProvider(
        client_id="your-client-id",
        client_secret="your-client-secret",
        issuer_url=ROOT_URL,  # Discovery metadata at root
        base_url=f"{ROOT_URL}{MOUNT_PREFIX}",  # Operational endpoints under prefix
    )
    

Create the MCP app, which generates operational routes at the specified path:

Copy

    mcp = FastMCP("Protected Server", auth=auth)
    mcp_app = mcp.http_app(path=MCP_PATH)
    

Retrieve the discovery routes from the auth provider. The `mcp_path` argument should match the path used when creating the MCP app:

Copy

    well_known_routes = auth.get_well_known_routes(mcp_path=MCP_PATH)
    

Finally, mount everything in the Starlette app with discovery routes at root and the MCP app under the prefix:

Copy

    app = Starlette(
        routes=[\
            *well_known_routes,  # Discovery routes at root level\
            Mount(MOUNT_PREFIX, app=mcp_app),  # Operational routes under prefix\
        ],
        lifespan=mcp_app.lifespan,
    )
    

This configuration produces the following URL structure:

*   MCP endpoint: `http://localhost:8000/api/mcp`
*   OAuth authorization: `http://localhost:8000/api/authorize`
*   OAuth callback: `http://localhost:8000/api/auth/callback`
*   Authorization server metadata: `http://localhost:8000/.well-known/oauth-authorization-server`
*   Protected resource metadata: `http://localhost:8000/.well-known/oauth-protected-resource/api/mcp`

### 

[​](https://gofastmcp.com/deployment/http#complete-example)

Complete Example

Here’s a complete working example showing all the pieces together:

Copy

    from fastmcp import FastMCP
    from fastmcp.server.auth.providers.github import GitHubProvider
    from starlette.applications import Starlette
    from starlette.routing import Mount
    import uvicorn
    
    # Define routing structure
    ROOT_URL = "http://localhost:8000"
    MOUNT_PREFIX = "/api"
    MCP_PATH = "/mcp"
    
    # Create OAuth provider
    auth = GitHubProvider(
        client_id="your-client-id",
        client_secret="your-client-secret",
        issuer_url=ROOT_URL,
        base_url=f"{ROOT_URL}{MOUNT_PREFIX}",
    )
    
    # Create MCP server
    mcp = FastMCP("Protected Server", auth=auth)
    
    @mcp.tool
    def analyze(data: str) -> dict:
        return {"result": f"Analyzed: {data}"}
    
    # Create MCP app
    mcp_app = mcp.http_app(path=MCP_PATH)
    
    # Get discovery routes for root level
    well_known_routes = auth.get_well_known_routes(mcp_path=MCP_PATH)
    
    # Assemble the application
    app = Starlette(
        routes=[\
            *well_known_routes,\
            Mount(MOUNT_PREFIX, app=mcp_app),\
        ],
        lifespan=mcp_app.lifespan,
    )
    
    if __name__ == "__main__":
        uvicorn.run(app, host="0.0.0.0", port=8000)
    

For more details on OAuth authentication, see the [Authentication guide](https://gofastmcp.com/servers/auth)
.

[​](https://gofastmcp.com/deployment/http#production-deployment)

Production Deployment
-----------------------------------------------------------------------------------------

### 

[​](https://gofastmcp.com/deployment/http#running-with-uvicorn)

Running with Uvicorn

When deploying to production, you’ll want to optimize your server for performance and reliability. Uvicorn provides several options to improve your server’s capabilities:

Copy

    # Run with basic configuration
    uvicorn app:app --host 0.0.0.0 --port 8000
    
    # Run with multiple workers for production
    uvicorn app:app --host 0.0.0.0 --port 8000 --workers 4
    

### 

[​](https://gofastmcp.com/deployment/http#environment-variables)

Environment Variables

Production deployments should never hardcode sensitive information like API keys or authentication tokens. Instead, use environment variables to configure your server at runtime. This keeps your code secure and makes it easy to deploy the same code to different environments with different configurations. Here’s an example using bearer token authentication (though OAuth is recommended for production):

Copy

    import os
    from fastmcp import FastMCP
    from fastmcp.server.auth import BearerTokenAuth
    
    # Read configuration from environment
    auth_token = os.environ.get("MCP_AUTH_TOKEN")
    if auth_token:
        auth = BearerTokenAuth(token=auth_token)
        mcp = FastMCP("Production Server", auth=auth)
    else:
        mcp = FastMCP("Production Server")
    
    app = mcp.http_app()
    

Deploy with your secrets safely stored in environment variables:

Copy

    MCP_AUTH_TOKEN=secret uvicorn app:app --host 0.0.0.0 --port 8000
    

### 

[​](https://gofastmcp.com/deployment/http#oauth-token-security)

OAuth Token Security

`` New in version: `2.13.0` `` If you’re using the [OAuth Proxy](https://gofastmcp.com/servers/auth/oauth-proxy)
, FastMCP issues its own JWT tokens to clients instead of forwarding upstream provider tokens. This maintains proper OAuth 2.0 token boundaries. **Default Behavior (Development Only):** By default, FastMCP automatically manages cryptographic keys:

*   **Mac/Windows**: Keys are generated and stored in your system keyring, surviving server restarts. Suitable **only** for development and local testing.
*   **Linux**: Keys are ephemeral (random salt at startup), so tokens are invalidated on restart.

This automatic approach is convenient for development but not suitable for production deployments. **For Production:** Production requires explicit key management to ensure tokens survive restarts and can be shared across multiple server instances. This requires the following two things working together:

1.  **Explicit JWT signing key** for signing tokens issued to clients
2.  **Persistent network-accessible storage** for upstream tokens (wrapped in `FernetEncryptionWrapper` to encrypt sensitive data at rest)

**Configuration:** Add two parameters to your auth provider:

Copy

    from key_value.aio.stores.redis import RedisStore
    from key_value.aio.wrappers.encryption import FernetEncryptionWrapper
    from cryptography.fernet import Fernet
    
    auth = GitHubProvider(
        client_id=os.environ["GITHUB_CLIENT_ID"],
        client_secret=os.environ["GITHUB_CLIENT_SECRET"],
        jwt_signing_key=os.environ["JWT_SIGNING_KEY"],
        client_storage=FernetEncryptionWrapper(
            key_value=RedisStore(host="redis.example.com", port=6379),
            fernet=Fernet(os.environ["STORAGE_ENCRYPTION_KEY"])
        ),
        base_url="https://your-server.com"  # use HTTPS
    )
    

Both parameters are required for production. Without an explicit signing key, keys are signed using a key derived from the client\_secret, which will cause invalidation upon rotation of the client secret. Without persistent storage, tokens are local to the server and won’t be trusted across hosts. **Wrap your storage backend in `FernetEncryptionWrapper` to encrypt sensitive OAuth tokens at rest** - without encryption, tokens are stored in plaintext. For more details on the token architecture and key management, see [OAuth Proxy Key and Storage Management](https://gofastmcp.com/servers/auth/oauth-proxy#key-and-storage-management)
.

[​](https://gofastmcp.com/deployment/http#testing-your-deployment)

Testing Your Deployment
---------------------------------------------------------------------------------------------

Once your server is deployed, you’ll need to verify it’s accessible and functioning correctly. For comprehensive testing strategies including connectivity tests, client testing, and authentication testing, see the [Testing Your Server](https://gofastmcp.com/development/tests)
 guide.

[​](https://gofastmcp.com/deployment/http#hosting-your-server)

Hosting Your Server
-------------------------------------------------------------------------------------

This guide has shown you how to create an HTTP-accessible MCP server, but you’ll still need a hosting provider to make it available on the internet. Your FastMCP server can run anywhere that supports Python web applications:

*   **Cloud VMs** (AWS EC2, Google Compute Engine, Azure VMs)
*   **Container platforms** (Cloud Run, Container Instances, ECS)
*   **Platform-as-a-Service** (Railway, Render, Vercel)
*   **Edge platforms** (Cloudflare Workers)
*   **Kubernetes clusters** (self-managed or managed)

The key requirements are Python 3.10+ support and the ability to expose an HTTP port. Most providers will require you to package your server (requirements.txt, Dockerfile, etc.) according to their deployment format. For managed, zero-configuration deployment, see [FastMCP Cloud](https://gofastmcp.com/deployment/fastmcp-cloud)
.

[Running Your Server\
\
Previous](https://gofastmcp.com/deployment/running-server)
[FastMCP Cloud\
\
Next](https://gofastmcp.com/deployment/fastmcp-cloud)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.