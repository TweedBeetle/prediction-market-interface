---
url: https://gofastmcp.com/integrations/eunomia-authorization
title: Eunomia Authorization 🤝 FastMCP - FastMCP
description: Add policy-based authorization to your FastMCP servers with Eunomia
scraped_at: 2025-11-03T18:42:15.545953
---

[Skip to main content](https://gofastmcp.com/integrations/eunomia-authorization#content-area)

Join the [FastMCP community](https://discord.gg/uu8dJCgttd)
!

[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)

Search...

Navigation

Authorization

Eunomia Authorization 🤝 FastMCP

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
    
    *   [Eunomia Auth](https://gofastmcp.com/integrations/eunomia-authorization)
        
    *   [Permit.io](https://gofastmcp.com/integrations/permit)
        
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

*   [How it Works](https://gofastmcp.com/integrations/eunomia-authorization#how-it-works)
    
*   [Listing Operations](https://gofastmcp.com/integrations/eunomia-authorization#listing-operations)
    
*   [Execution Operations](https://gofastmcp.com/integrations/eunomia-authorization#execution-operations)
    
*   [Add Authorization to Your Server](https://gofastmcp.com/integrations/eunomia-authorization#add-authorization-to-your-server)
    
*   [Create a Server with Authorization](https://gofastmcp.com/integrations/eunomia-authorization#create-a-server-with-authorization)
    
*   [Configure Access Policies](https://gofastmcp.com/integrations/eunomia-authorization#configure-access-policies)
    
*   [Run the Server](https://gofastmcp.com/integrations/eunomia-authorization#run-the-server)
    

Add **policy-based authorization** to your FastMCP servers with one-line code addition with the **[Eunomia](https://github.com/whataboutyou-ai/eunomia)
 authorization middleware**. Control which tools, resources and prompts MCP clients can view and execute on your server. Define dynamic JSON-based policies and obtain a comprehensive audit log of all access attempts and violations.

[​](https://gofastmcp.com/integrations/eunomia-authorization#how-it-works)

How it Works
------------------------------------------------------------------------------------------

Exploiting FastMCP’s [Middleware](https://gofastmcp.com/servers/middleware)
, the Eunomia middleware intercepts all MCP requests to your server and automatically maps MCP methods to authorization checks.

### 

[​](https://gofastmcp.com/integrations/eunomia-authorization#listing-operations)

Listing Operations

The middleware behaves as a filter for listing operations (`tools/list`, `resources/list`, `prompts/list`), hiding to the client components that are not authorized by the defined policies.

Eunomia ServerFastMCP ServerEunomia MiddlewareMCP ClientEunomia ServerFastMCP ServerEunomia MiddlewareMCP ClientMCP Listing Request (e.g., tools/list)MCP Listing RequestMCP Listing ResponseAuthorization ChecksAuthorization DecisionsFiltered MCP Listing Response

### 

[​](https://gofastmcp.com/integrations/eunomia-authorization#execution-operations)

Execution Operations

The middleware behaves as a firewall for execution operations (`tools/call`, `resources/read`, `prompts/get`), blocking operations that are not authorized by the defined policies.

Eunomia ServerFastMCP ServerEunomia MiddlewareMCP ClientEunomia ServerFastMCP ServerEunomia MiddlewareMCP ClientMCP Execution Request (e.g., tools/call)Authorization CheckAuthorization DecisionMCP Unauthorized Error (if denied)MCP Execution Request (if allowed)MCP Execution Response (if allowed)MCP Execution Response (if allowed)

[​](https://gofastmcp.com/integrations/eunomia-authorization#add-authorization-to-your-server)

Add Authorization to Your Server
----------------------------------------------------------------------------------------------------------------------------------

Eunomia is an AI-specific authorization server that handles policy decisions. The server runs embedded within your MCP server by default for a zero-effort configuration, but can alternatively be run remotely for centralized policy decisions.

### 

[​](https://gofastmcp.com/integrations/eunomia-authorization#create-a-server-with-authorization)

Create a Server with Authorization

First, install the `eunomia-mcp` package:

Copy

    pip install eunomia-mcp
    

Then create a FastMCP server and add the Eunomia middleware in one line:

server.py

Copy

    from fastmcp import FastMCP
    from eunomia_mcp import create_eunomia_middleware
    
    # Create your FastMCP server
    mcp = FastMCP("Secure MCP Server 🔒")
    
    @mcp.tool()
    def add(a: int, b: int) -> int:
        """Add two numbers"""
        return a + b
    
    # Add middleware to your server
    middleware = create_eunomia_middleware(policy_file="mcp_policies.json")
    mcp.add_middleware(middleware)
    
    if __name__ == "__main__":
        mcp.run()
    

### 

[​](https://gofastmcp.com/integrations/eunomia-authorization#configure-access-policies)

Configure Access Policies

Use the `eunomia-mcp` CLI in your terminal to manage your authorization policies:

Copy

    # Create a default policy file
    eunomia-mcp init
    
    # Or create a policy file customized for your FastMCP server
    eunomia-mcp init --custom-mcp "app.server:mcp"
    

This creates `mcp_policies.json` file that you can further edit to your access control needs.

Copy

    # Once edited, validate your policy file
    eunomia-mcp validate mcp_policies.json
    

### 

[​](https://gofastmcp.com/integrations/eunomia-authorization#run-the-server)

Run the Server

Start your FastMCP server normally:

Copy

    python server.py
    

The middleware will now intercept all MCP requests and check them against your policies. Requests include agent identification through headers like `X-Agent-ID`, `X-User-ID`, `User-Agent`, or `Authorization` and an automatic mapping of MCP methods to authorization resources and actions.

For detailed policy configuration, custom authentication, and remote deployments, visit the [Eunomia MCP Middleware repository](https://github.com/whataboutyou-ai/eunomia/tree/main/pkgs/extensions/mcp)
.

[WorkOS 🤝 FastMCP\
\
Previous](https://gofastmcp.com/integrations/workos)
[Permit.io Authorization 🤝 FastMCP\
\
Next](https://gofastmcp.com/integrations/permit)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.