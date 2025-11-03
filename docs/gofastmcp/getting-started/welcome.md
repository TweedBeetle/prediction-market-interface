---
url: https://gofastmcp.com/getting-started/welcome
title: Welcome to FastMCP 2.0! - FastMCP
description: The fast, Pythonic way to build MCP servers and clients.
scraped_at: 2025-11-03T18:42:09.262606
---

[Skip to main content](https://gofastmcp.com/getting-started/welcome#content-area)

Join the [FastMCP community](https://discord.gg/uu8dJCgttd)
!

[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)

Search...

Navigation

Get Started

Welcome to FastMCP 2.0!

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

*   [Beyond Basic MCP](https://gofastmcp.com/getting-started/welcome#beyond-basic-mcp)
    
*   [What is MCP?](https://gofastmcp.com/getting-started/welcome#what-is-mcp%3F)
    
*   [Why FastMCP?](https://gofastmcp.com/getting-started/welcome#why-fastmcp%3F)
    
*   [LLM-Friendly Docs](https://gofastmcp.com/getting-started/welcome#llm-friendly-docs)
    
*   [MCP Server](https://gofastmcp.com/getting-started/welcome#mcp-server)
    
*   [Text Formats](https://gofastmcp.com/getting-started/welcome#text-formats)
    

!['F' logo on a watercolor background](https://mintcdn.com/fastmcp/xdeorzy2A8w9kCCa/assets/brand/f-watercolor-waves.png?w=2500&fit=max&auto=format&n=xdeorzy2A8w9kCCa&q=85&s=6f84b20c8d1f1ab62bc4e88b47d70e6f) !['F' logo on a watercolor background](https://mintcdn.com/fastmcp/xdeorzy2A8w9kCCa/assets/brand/f-watercolor-waves-dark.png?w=2500&fit=max&auto=format&n=xdeorzy2A8w9kCCa&q=85&s=495974191566b1091e25280ec90ab6a0) **FastMCP is the standard framework for building MCP applications.** The [Model Context Protocol](https://modelcontextprotocol.io/)
 (MCP) provides a standardized way to connect LLMs to tools and data, and FastMCP makes it production-ready with clean, Pythonic code:

Copy

    from fastmcp import FastMCP
    
    mcp = FastMCP("Demo 🚀")
    
    @mcp.tool
    def add(a: int, b: int) -> int:
        """Add two numbers"""
        return a + b
    
    if __name__ == "__main__":
        mcp.run()
    

[​](https://gofastmcp.com/getting-started/welcome#beyond-basic-mcp)

Beyond Basic MCP
---------------------------------------------------------------------------------------

FastMCP pioneered Python MCP development, and FastMCP 1.0 was incorporated into the [official MCP SDK](https://github.com/modelcontextprotocol/python-sdk)
 in 2024. **This is FastMCP 2.0,** the actively maintained version that extends far beyond basic protocol implementation. While the SDK provides core functionality, FastMCP 2.0 delivers everything needed for production: advanced MCP patterns (server composition, proxying, OpenAPI/FastAPI generation, tool transformation), enterprise auth (Google, GitHub, Azure, Auth0, WorkOS, and more), deployment tools, testing frameworks, and comprehensive client libraries. Ready to build? Start with our [installation guide](https://gofastmcp.com/getting-started/installation)
 or jump straight to the [quickstart](https://gofastmcp.com/getting-started/quickstart)
. FastMCP is made with 💙 by [Prefect](https://www.prefect.io/)
.

[​](https://gofastmcp.com/getting-started/welcome#what-is-mcp%3F)

What is MCP?
---------------------------------------------------------------------------------

The Model Context Protocol lets you build servers that expose data and functionality to LLM applications in a secure, standardized way. It is often described as “the USB-C port for AI”, providing a uniform way to connect LLMs to resources they can use. It may be easier to think of it as an API, but specifically designed for LLM interactions. MCP servers can:

*   Expose data through `Resources` (think of these sort of like GET endpoints; they are used to load information into the LLM’s context)
*   Provide functionality through `Tools` (sort of like POST endpoints; they are used to execute code or otherwise produce a side effect)
*   Define interaction patterns through `Prompts` (reusable templates for LLM interactions)
*   And more!

FastMCP provides a high-level, Pythonic interface for building, managing, and interacting with these servers.

[​](https://gofastmcp.com/getting-started/welcome#why-fastmcp%3F)

Why FastMCP?
---------------------------------------------------------------------------------

FastMCP handles all the complex protocol details so you can focus on building. In most cases, decorating a Python function is all you need — FastMCP handles the rest. 🚀 **Fast**: High-level interface means less code and faster development 🍀 **Simple**: Build MCP servers with minimal boilerplate 🐍 **Pythonic**: Feels natural to Python developers 🔍 **Complete**: Everything for production — enterprise auth (Google, GitHub, Azure, Auth0, WorkOS), deployment tools, testing frameworks, client libraries, and more FastMCP provides the shortest path from idea to production. Deploy locally, to the cloud with [FastMCP Cloud](https://fastmcp.cloud/)
 (free for personal servers), or to your own infrastructure.

**This documentation reflects FastMCP’s `main` branch**, meaning it always reflects the latest development version. Features are generally marked with version badges (e.g. `New in version: 2.13.1`) to indicate when they were introduced. Note that this may include features that are not yet released.

[​](https://gofastmcp.com/getting-started/welcome#llm-friendly-docs)

LLM-Friendly Docs
-----------------------------------------------------------------------------------------

The FastMCP documentation is available in multiple LLM-friendly formats:

### 

[​](https://gofastmcp.com/getting-started/welcome#mcp-server)

MCP Server

The FastMCP docs are accessible via MCP! The server URL is `https://gofastmcp.com/mcp`. In fact, you can use FastMCP to search the FastMCP docs:

Copy

    import asyncio
    from fastmcp import Client
    
    async def main():
        async with Client("https://gofastmcp.com/mcp") as client:
            result = await client.call_tool(
                name="SearchFastMcp", 
                arguments={"query": "deploy a FastMCP server"}
            )
        print(result)
    
    asyncio.run(main())
    

### 

[​](https://gofastmcp.com/getting-started/welcome#text-formats)

Text Formats

The docs are also available in [llms.txt format](https://llmstxt.org/)
:

*   [llms.txt](https://gofastmcp.com/llms.txt)
     - A sitemap listing all documentation pages
*   [llms-full.txt](https://gofastmcp.com/llms-full.txt)
     - The entire documentation in one file (may exceed context windows)

Any page can be accessed as markdown by appending `.md` to the URL. For example, this page becomes `https://gofastmcp.com/getting-started/welcome.md`. You can also copy any page as markdown by pressing “Cmd+C” (or “Ctrl+C” on Windows) on your keyboard.

[Installation\
\
Next](https://gofastmcp.com/getting-started/installation)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.