---
url: https://gofastmcp.com/development/upgrade-guide
title: Upgrade Guide - FastMCP
description: Migration instructions for upgrading between FastMCP versions
scraped_at: 2025-11-03T18:42:04.229303
---

[Skip to main content](https://gofastmcp.com/development/upgrade-guide#content-area)

Join the [FastMCP community](https://discord.gg/uu8dJCgttd)
!

[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)

Search...

Navigation

Development

Upgrade Guide

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

*   [v2.13.0](https://gofastmcp.com/development/upgrade-guide#v2-13-0)
    
*   [OAuth Token Key Management](https://gofastmcp.com/development/upgrade-guide#oauth-token-key-management)
    

This guide provides migration instructions for breaking changes and major updates when upgrading between FastMCP versions.

[​](https://gofastmcp.com/development/upgrade-guide#v2-13-0)

v2.13.0
-----------------------------------------------------------------------

### 

[​](https://gofastmcp.com/development/upgrade-guide#oauth-token-key-management)

OAuth Token Key Management

The OAuth proxy now issues its own JWT tokens to clients instead of forwarding upstream provider tokens. This improves security by maintaining proper token audience boundaries. **What changed:** The OAuth proxy now implements a token factory pattern - it receives tokens from your OAuth provider (GitHub, Google, etc.), encrypts and stores them, then issues its own FastMCP JWT tokens to clients. This requires cryptographic keys for JWT signing and token encryption. **Default behavior (development):** By default, FastMCP automatically manages keys based on your platform:

*   **Mac/Windows**: Keys are auto-managed via system keyring, surviving server restarts with zero configuration. Suitable **only** for development and local testing.
*   **Linux**: Keys are ephemeral (random salt at startup, regenerated on each restart).

This works fine for development and testing where re-authentication after restart is acceptable. **For production:** Production deployments must provide explicit keys and use persistent storage. Add these three things:

Copy

    auth = GitHubProvider(
        client_id=os.environ["GITHUB_CLIENT_ID"],
        client_secret=os.environ["GITHUB_CLIENT_SECRET"],
        base_url="https://your-server.com",
    
        # Explicit keys (required for production)
        jwt_signing_key=os.environ["JWT_SIGNING_KEY"],
    
        # Persistent network storage (required for production)
        client_storage=RedisStore(host="redis.example.com", port=6379)
    )
    

**More information:**

*   [OAuth Token Security](https://gofastmcp.com/deployment/http#oauth-token-security)
     - Complete production setup guide
*   [Key and Storage Management](https://gofastmcp.com/servers/auth/oauth-proxy#key-and-storage-management)
     - Detailed explanation of defaults and production requirements
*   [OAuth Proxy Parameters](https://gofastmcp.com/servers/auth/oauth-proxy#configuration-parameters)
     - Parameter documentation

[Releases\
\
Previous](https://gofastmcp.com/development/releases)
[Changelog\
\
Next](https://gofastmcp.com/changelog)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.