---
url: https://gofastmcp.com/servers/icons
title: Icons - FastMCP
description: Add visual icons to your servers, tools, resources, and prompts
scraped_at: 2025-11-03T18:43:17.307793
---

[Skip to main content](https://gofastmcp.com/servers/icons#content-area)

Join the [FastMCP community](https://discord.gg/uu8dJCgttd)
!

[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)

Search...

Navigation

Advanced Features

Icons

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
    
    *   [Composition](https://gofastmcp.com/servers/composition)
        
    *   [Context](https://gofastmcp.com/servers/context)
        
    *   [Elicitation](https://gofastmcp.com/servers/elicitation)
        
    *   [Icons\
        \
        NEW](https://gofastmcp.com/servers/icons)
        
    *   [Logging](https://gofastmcp.com/servers/logging)
        
    *   [Middleware\
        \
        NEW](https://gofastmcp.com/servers/middleware)
        
    *   [Progress](https://gofastmcp.com/servers/progress)
        
    *   [Proxy Servers](https://gofastmcp.com/servers/proxy)
        
    *   [Sampling](https://gofastmcp.com/servers/sampling)
        
    *   [Storage Backends\
        \
        NEW](https://gofastmcp.com/servers/storage-backends)
        
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

*   [Icon Format](https://gofastmcp.com/servers/icons#icon-format)
    
*   [Server Icons](https://gofastmcp.com/servers/icons#server-icons)
    
*   [Component Icons](https://gofastmcp.com/servers/icons#component-icons)
    
*   [Tool Icons](https://gofastmcp.com/servers/icons#tool-icons)
    
*   [Resource Icons](https://gofastmcp.com/servers/icons#resource-icons)
    
*   [Resource Template Icons](https://gofastmcp.com/servers/icons#resource-template-icons)
    
*   [Prompt Icons](https://gofastmcp.com/servers/icons#prompt-icons)
    
*   [Using Data URIs](https://gofastmcp.com/servers/icons#using-data-uris)
    

`` New in version: `2.14.0` `` Icons provide visual representations for your MCP servers and components, helping client applications present better user interfaces. When displayed in MCP clients, icons help users quickly identify and navigate your server’s capabilities.

[​](https://gofastmcp.com/servers/icons#icon-format)

Icon Format
-------------------------------------------------------------------

Icons use the standard MCP Icon type from the MCP protocol specification. Each icon specifies:

*   **src**: URL or data URI pointing to the icon image
*   **mimeType** (optional): MIME type of the image (e.g., “image/png”, “image/svg+xml”)
*   **sizes** (optional): Array of size descriptors (e.g., \[“48x48”\], \[“any”\])

Copy

    from mcp.types import Icon
    
    icon = Icon(
        src="https://example.com/icon.png",
        mimeType="image/png",
        sizes=["48x48"]
    )
    

[​](https://gofastmcp.com/servers/icons#server-icons)

Server Icons
---------------------------------------------------------------------

Add icons and a website URL to your server for display in client applications:

Copy

    from fastmcp import FastMCP
    from mcp.types import Icon
    
    mcp = FastMCP(
        name="WeatherService",
        website_url="https://weather.example.com",
        icons=[\
            Icon(\
                src="https://weather.example.com/icon-48.png",\
                mimeType="image/png",\
                sizes=["48x48"]\
            ),\
            Icon(\
                src="https://weather.example.com/icon-96.png",\
                mimeType="image/png",\
                sizes=["96x96"]\
            ),\
        ]
    )
    

Server icons appear in MCP client interfaces to help users identify your server among others they may have installed.

[​](https://gofastmcp.com/servers/icons#component-icons)

Component Icons
---------------------------------------------------------------------------

Icons can be added to individual tools, resources, resource templates, and prompts:

### 

[​](https://gofastmcp.com/servers/icons#tool-icons)

Tool Icons

Copy

    from mcp.types import Icon
    
    @mcp.tool(
        icons=[Icon(src="https://example.com/calculator-icon.png")]
    )
    def calculate_sum(a: int, b: int) -> int:
        """Add two numbers together."""
        return a + b
    

### 

[​](https://gofastmcp.com/servers/icons#resource-icons)

Resource Icons

Copy

    @mcp.resource(
        "config://settings",
        icons=[Icon(src="https://example.com/config-icon.png")]
    )
    def get_settings() -> dict:
        """Retrieve application settings."""
        return {"theme": "dark", "language": "en"}
    

### 

[​](https://gofastmcp.com/servers/icons#resource-template-icons)

Resource Template Icons

Copy

    @mcp.resource(
        "user://{user_id}/profile",
        icons=[Icon(src="https://example.com/user-icon.png")]
    )
    def get_user_profile(user_id: str) -> dict:
        """Get a user's profile."""
        return {"id": user_id, "name": f"User {user_id}"}
    

### 

[​](https://gofastmcp.com/servers/icons#prompt-icons)

Prompt Icons

Copy

    @mcp.prompt(
        icons=[Icon(src="https://example.com/prompt-icon.png")]
    )
    def analyze_code(code: str):
        """Create a prompt for code analysis."""
        return f"Please analyze this code:\n\n{code}"
    

[​](https://gofastmcp.com/servers/icons#using-data-uris)

Using Data URIs
---------------------------------------------------------------------------

For small icons or when you want to embed the icon directly, use data URIs:

Copy

    from mcp.types import Icon
    from fastmcp.utilities.types import Image
    
    # SVG icon as data URI
    svg_icon = Icon(
        src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCI+PHBhdGggZD0iTTEyIDJDNi40OCAyIDIgNi40OCAyIDEyczQuNDggMTAgMTAgMTAgMTAtNC40OCAxMC0xMFMxNy41MiAyIDEyIDJ6Ii8+PC9zdmc+",
        mimeType="image/svg+xml"
    )
    
    @mcp.tool(icons=[svg_icon])
    def my_tool() -> str:
        """A tool with an embedded SVG icon."""
        return "result"
    
    # Generating a data URI from a local image file.
    img = Image(path="./assets/brand/favicon.png")
    icon = Icon(src=img.to_data_uri())
    
    @mcp.tool(icons=[icon])
    def file_icon_tool() -> str:
        """A tool with an icon generated from a local file."""
        return "result"
    

[User Elicitation\
\
Previous](https://gofastmcp.com/servers/elicitation)
[Client Logging\
\
Next](https://gofastmcp.com/servers/logging)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.