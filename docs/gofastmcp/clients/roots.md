---
url: https://gofastmcp.com/clients/roots
title: Client Roots - FastMCP
description: Provide local context and resource boundaries to MCP servers.
scraped_at: 2025-11-03T18:42:02.698695
---

[Skip to main content](https://gofastmcp.com/clients/roots#content-area)

Join the [FastMCP community](https://discord.gg/uu8dJCgttd)
!

[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)

Search...

Navigation

Advanced Features

Client Roots

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
    
    *   [Elicitation](https://gofastmcp.com/clients/elicitation)
        
    *   [Logging](https://gofastmcp.com/clients/logging)
        
    *   [Progress](https://gofastmcp.com/clients/progress)
        
    *   [Sampling](https://gofastmcp.com/clients/sampling)
        
    *   [Messages](https://gofastmcp.com/clients/messages)
        
    *   [Roots](https://gofastmcp.com/clients/roots)
        
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

*   [Setting Static Roots](https://gofastmcp.com/clients/roots#setting-static-roots)
    

`` New in version: `2.0.0` `` Roots are a way for clients to inform servers about the resources they have access to. Servers can use this information to adjust behavior or provide more relevant responses.

[​](https://gofastmcp.com/clients/roots#setting-static-roots)

Setting Static Roots
-------------------------------------------------------------------------------------

Provide a list of roots when creating the client:

Static Roots

Dynamic Roots Callback

Copy

    from fastmcp import Client
    
    client = Client(
        "my_mcp_server.py", 
        roots=["/path/to/root1", "/path/to/root2"]
    )
    

[Message Handling\
\
Previous](https://gofastmcp.com/clients/messages)
[OAuth Authentication\
\
Next](https://gofastmcp.com/clients/auth/oauth)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.