---
url: https://gofastmcp.com/getting-started/installation
title: Installation - FastMCP
scraped_at: 2025-11-03T18:42:09.522288
---

[Skip to main content](https://gofastmcp.com/getting-started/installation#content-area)

Join the [FastMCP community](https://discord.gg/uu8dJCgttd)
!

[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)

Search...

Navigation

Get Started

Installation

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

*   [Install FastMCP](https://gofastmcp.com/getting-started/installation#install-fastmcp)
    
*   [Verify Installation](https://gofastmcp.com/getting-started/installation#verify-installation)
    
*   [Upgrading from the Official MCP SDK](https://gofastmcp.com/getting-started/installation#upgrading-from-the-official-mcp-sdk)
    
*   [Versioning Policy](https://gofastmcp.com/getting-started/installation#versioning-policy)
    
*   [Contributing to FastMCP](https://gofastmcp.com/getting-started/installation#contributing-to-fastmcp)
    

[​](https://gofastmcp.com/getting-started/installation#install-fastmcp)

Install FastMCP
------------------------------------------------------------------------------------------

We recommend using [uv](https://docs.astral.sh/uv/getting-started/installation/)
 to install and manage FastMCP. If you plan to use FastMCP in your project, you can add it as a dependency with:

Copy

    uv add fastmcp
    

Alternatively, you can install it directly with `pip` or `uv pip`:

uv

pip

Copy

    uv pip install fastmcp
    

### 

[​](https://gofastmcp.com/getting-started/installation#verify-installation)

Verify Installation

To verify that FastMCP is installed correctly, you can run the following command:

Copy

    fastmcp version
    

You should see output like the following:

Copy

    $ fastmcp version
    
    FastMCP version:                           2.11.3
    MCP version:                               1.12.4
    Python version:                            3.12.2
    Platform:            macOS-15.3.1-arm64-arm-64bit
    FastMCP root path:            ~/Developer/fastmcp
    

[​](https://gofastmcp.com/getting-started/installation#upgrading-from-the-official-mcp-sdk)

Upgrading from the Official MCP SDK
----------------------------------------------------------------------------------------------------------------------------------

Upgrading from the official MCP SDK’s FastMCP 1.0 to FastMCP 2.0 is generally straightforward. The core server API is highly compatible, and in many cases, changing your import statement from `from mcp.server.fastmcp import FastMCP` to `from fastmcp import FastMCP` will be sufficient.

Copy

    # Before
    # from mcp.server.fastmcp import FastMCP
    
    # After
    from fastmcp import FastMCP
    
    mcp = FastMCP("My MCP Server")
    

Prior to `fastmcp==2.3.0` and `mcp==1.8.0`, the 2.x API always mirrored the official 1.0 API. However, as the projects diverge, this can not be guaranteed. You may see deprecation warnings if you attempt to use 1.0 APIs in FastMCP 2.x. Please refer to this documentation for details on new capabilities.

[​](https://gofastmcp.com/getting-started/installation#versioning-policy)

Versioning Policy
----------------------------------------------------------------------------------------------

FastMCP follows semantic versioning with pragmatic adaptations for the rapidly evolving MCP ecosystem. Breaking changes may occur in minor versions (e.g., 2.3.x to 2.4.0) when necessary to stay current with the MCP Protocol. For production use, always pin to exact versions:

Copy

    fastmcp==2.11.0  # Good
    fastmcp>=2.11.0  # Bad - will install breaking changes
    

See the full [versioning and release policy](https://gofastmcp.com/development/releases#versioning-policy)
 for details on our public API, deprecation practices, and breaking change philosophy.

[​](https://gofastmcp.com/getting-started/installation#contributing-to-fastmcp)

Contributing to FastMCP
----------------------------------------------------------------------------------------------------------

Interested in contributing to FastMCP? See the [Contributing Guide](https://gofastmcp.com/development/contributing)
 for details on:

*   Setting up your development environment
*   Running tests and pre-commit hooks
*   Submitting issues and pull requests
*   Code standards and review process

[Welcome to FastMCP 2.0!\
\
Previous](https://gofastmcp.com/getting-started/welcome)
[Quickstart\
\
Next](https://gofastmcp.com/getting-started/quickstart)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.