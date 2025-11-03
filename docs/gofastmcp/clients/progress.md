---
url: https://gofastmcp.com/clients/progress
title: Progress Monitoring - FastMCP
description: Handle progress notifications from long-running server operations.
scraped_at: 2025-11-03T18:41:58.408652
---

[Skip to main content](https://gofastmcp.com/clients/progress#content-area)

Join the [FastMCP community](https://discord.gg/uu8dJCgttd)
!

[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)

Search...

Navigation

Advanced Features

Progress Monitoring

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

*   [Progress Handler](https://gofastmcp.com/clients/progress#progress-handler)
    
*   [Handler Parameters](https://gofastmcp.com/clients/progress#handler-parameters)
    
*   [Per-Call Progress Handler](https://gofastmcp.com/clients/progress#per-call-progress-handler)
    

`` New in version: `2.3.5` `` MCP servers can report progress during long-running operations. The client can receive these updates through a progress handler.

[​](https://gofastmcp.com/clients/progress#progress-handler)

Progress Handler
--------------------------------------------------------------------------------

Set a progress handler when creating the client:

Copy

    from fastmcp import Client
    
    async def my_progress_handler(
        progress: float, 
        total: float | None, 
        message: str | None
    ) -> None:
        if total is not None:
            percentage = (progress / total) * 100
            print(f"Progress: {percentage:.1f}% - {message or ''}")
        else:
            print(f"Progress: {progress} - {message or ''}")
    
    client = Client(
        "my_mcp_server.py",
        progress_handler=my_progress_handler
    )
    

### 

[​](https://gofastmcp.com/clients/progress#handler-parameters)

Handler Parameters

The progress handler receives three parameters:

Progress Handler Parameters
---------------------------

[​](https://gofastmcp.com/clients/progress#param-progress)

progress

float

Current progress value

[​](https://gofastmcp.com/clients/progress#param-total)

total

float | None

Expected total value (may be None)

[​](https://gofastmcp.com/clients/progress#param-message)

message

str | None

Optional status message (may be None)

[​](https://gofastmcp.com/clients/progress#per-call-progress-handler)

Per-Call Progress Handler
--------------------------------------------------------------------------------------------------

Override the progress handler for specific tool calls:

Copy

    async with client:
        # Override with specific progress handler for this call
        result = await client.call_tool(
            "long_running_task", 
            {"param": "value"}, 
            progress_handler=my_progress_handler
        )
    

[Server Logging\
\
Previous](https://gofastmcp.com/clients/logging)
[LLM Sampling\
\
Next](https://gofastmcp.com/clients/sampling)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.