---
url: https://gofastmcp.com/servers/server
title: The FastMCP Server - FastMCP
description: The core FastMCP server class for building MCP applications with tools, resources, and prompts.
scraped_at: 2025-11-03T18:43:22.594749
---

[Skip to main content](https://gofastmcp.com/servers/server#content-area)

Join the [FastMCP community](https://discord.gg/uu8dJCgttd)
!

[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)

Search...

Navigation

Servers

The FastMCP Server

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

*   [Creating a Server](https://gofastmcp.com/servers/server#creating-a-server)
    
*   [Components](https://gofastmcp.com/servers/server#components)
    
*   [Tools](https://gofastmcp.com/servers/server#tools)
    
*   [Resources](https://gofastmcp.com/servers/server#resources)
    
*   [Resource Templates](https://gofastmcp.com/servers/server#resource-templates)
    
*   [Prompts](https://gofastmcp.com/servers/server#prompts)
    
*   [Tag-Based Filtering](https://gofastmcp.com/servers/server#tag-based-filtering)
    
*   [Running the Server](https://gofastmcp.com/servers/server#running-the-server)
    
*   [Custom Routes](https://gofastmcp.com/servers/server#custom-routes)
    
*   [Composing Servers](https://gofastmcp.com/servers/server#composing-servers)
    
*   [Proxying Servers](https://gofastmcp.com/servers/server#proxying-servers)
    
*   [OpenAPI Integration](https://gofastmcp.com/servers/server#openapi-integration)
    
*   [Server Configuration](https://gofastmcp.com/servers/server#server-configuration)
    
*   [Server-Specific Configuration](https://gofastmcp.com/servers/server#server-specific-configuration)
    
*   [Global Settings](https://gofastmcp.com/servers/server#global-settings)
    
*   [Transport-Specific Configuration](https://gofastmcp.com/servers/server#transport-specific-configuration)
    
*   [Setting Global Configuration](https://gofastmcp.com/servers/server#setting-global-configuration)
    
*   [Custom Tool Serialization](https://gofastmcp.com/servers/server#custom-tool-serialization)
    

The central piece of a FastMCP application is the `FastMCP` server class. This class acts as the main container for your application’s tools, resources, and prompts, and manages communication with MCP clients.

[​](https://gofastmcp.com/servers/server#creating-a-server)

Creating a Server
--------------------------------------------------------------------------------

Instantiating a server is straightforward. You typically provide a name for your server, which helps identify it in client applications or logs.

Copy

    from fastmcp import FastMCP
    
    # Create a basic server instance
    mcp = FastMCP(name="MyAssistantServer")
    
    # You can also add instructions for how to interact with the server
    mcp_with_instructions = FastMCP(
        name="HelpfulAssistant",
        instructions="""
            This server provides data analysis tools.
            Call get_average() to analyze numerical data.
        """,
    )
    

The `FastMCP` constructor accepts several arguments:

FastMCP Constructor Parameters
------------------------------

[​](https://gofastmcp.com/servers/server#param-name)

name

str

default:"FastMCP"

A human-readable name for your server

[​](https://gofastmcp.com/servers/server#param-instructions)

instructions

str | None

Description of how to interact with this server. These instructions help clients understand the server’s purpose and available functionality

[​](https://gofastmcp.com/servers/server#param-version)

version

str | None

Version string for your server. If not provided, defaults to the FastMCP library version

[​](https://gofastmcp.com/servers/server#param-website-url)

website\_url

str | None

`` New in version: `2.14.0` ``URL to a website with more information about your server. Displayed in client applications

[​](https://gofastmcp.com/servers/server#param-icons)

icons

list\[Icon\] | None

`` New in version: `2.14.0` ``List of icon representations for your server. Icons help users visually identify your server in client applications. See [Icons](https://gofastmcp.com/servers/icons)
 for detailed examples

[​](https://gofastmcp.com/servers/server#param-auth)

auth

OAuthProvider | TokenVerifier | None

Authentication provider for securing HTTP-based transports. See [Authentication](https://gofastmcp.com/servers/auth/authentication)
 for configuration options

[​](https://gofastmcp.com/servers/server#param-lifespan)

lifespan

AsyncContextManager | None

An async context manager function for server startup and shutdown logic

[​](https://gofastmcp.com/servers/server#param-tools)

tools

list\[Tool | Callable\] | None

A list of tools (or functions to convert to tools) to add to the server. In some cases, providing tools programmatically may be more convenient than using the `@mcp.tool` decorator

[​](https://gofastmcp.com/servers/server#param-include-tags)

include\_tags

set\[str\] | None

Only expose components with at least one matching tag

[​](https://gofastmcp.com/servers/server#param-exclude-tags)

exclude\_tags

set\[str\] | None

Hide components with any matching tag

[​](https://gofastmcp.com/servers/server#param-on-duplicate-tools)

on\_duplicate\_tools

Literal\["error", "warn", "replace"\]

default:"error"

How to handle duplicate tool registrations

[​](https://gofastmcp.com/servers/server#param-on-duplicate-resources)

on\_duplicate\_resources

Literal\["error", "warn", "replace"\]

default:"warn"

How to handle duplicate resource registrations

[​](https://gofastmcp.com/servers/server#param-on-duplicate-prompts)

on\_duplicate\_prompts

Literal\["error", "warn", "replace"\]

default:"replace"

How to handle duplicate prompt registrations

[​](https://gofastmcp.com/servers/server#param-strict-input-validation)

strict\_input\_validation

bool

default:"False"

`` New in version: `2.13.0` ``Controls how tool input parameters are validated. When `False` (default), FastMCP uses Pydantic’s flexible validation that coerces compatible inputs (e.g., `"10"` → `10` for int parameters). When `True`, uses the MCP SDK’s JSON Schema validation to validate inputs against the exact schema before passing them to your function, rejecting any type mismatches. The default mode improves compatibility with LLM clients while maintaining type safety. See [Input Validation Modes](https://gofastmcp.com/servers/tools#input-validation-modes)
 for details

[​](https://gofastmcp.com/servers/server#param-include-fastmcp-meta)

include\_fastmcp\_meta

bool

default:"True"

`` New in version: `2.11.0` ``Whether to include FastMCP metadata in component responses. When `True`, component tags and other FastMCP-specific metadata are included in the `_fastmcp` namespace within each component’s `meta` field. When `False`, this metadata is omitted, resulting in cleaner integration with external systems. Can be overridden globally via `FASTMCP_INCLUDE_FASTMCP_META` environment variable

[​](https://gofastmcp.com/servers/server#components)

Components
------------------------------------------------------------------

FastMCP servers expose several types of components to the client:

### 

[​](https://gofastmcp.com/servers/server#tools)

Tools

Tools are functions that the client can call to perform actions or access external systems.

Copy

    @mcp.tool
    def multiply(a: float, b: float) -> float:
        """Multiplies two numbers together."""
        return a * b
    

See [Tools](https://gofastmcp.com/servers/tools)
 for detailed documentation.

### 

[​](https://gofastmcp.com/servers/server#resources)

Resources

Resources expose data sources that the client can read.

Copy

    @mcp.resource("data://config")
    def get_config() -> dict:
        """Provides the application configuration."""
        return {"theme": "dark", "version": "1.0"}
    

See [Resources & Templates](https://gofastmcp.com/servers/resources)
 for detailed documentation.

### 

[​](https://gofastmcp.com/servers/server#resource-templates)

Resource Templates

Resource templates are parameterized resources that allow the client to request specific data.

Copy

    @mcp.resource("users://{user_id}/profile")
    def get_user_profile(user_id: int) -> dict:
        """Retrieves a user's profile by ID."""
        # The {user_id} in the URI is extracted and passed to this function
        return {"id": user_id, "name": f"User {user_id}", "status": "active"}
    

See [Resources & Templates](https://gofastmcp.com/servers/resources)
 for detailed documentation.

### 

[​](https://gofastmcp.com/servers/server#prompts)

Prompts

Prompts are reusable message templates for guiding the LLM.

Copy

    @mcp.prompt
    def analyze_data(data_points: list[float]) -> str:
        """Creates a prompt asking for analysis of numerical data."""
        formatted_data = ", ".join(str(point) for point in data_points)
        return f"Please analyze these data points: {formatted_data}"
    

See [Prompts](https://gofastmcp.com/servers/prompts)
 for detailed documentation.

[​](https://gofastmcp.com/servers/server#tag-based-filtering)

Tag-Based Filtering
------------------------------------------------------------------------------------

`` New in version: `2.8.0` `` FastMCP supports tag-based filtering to selectively expose components based on configurable include/exclude tag sets. This is useful for creating different views of your server for different environments or users. Components can be tagged when defined using the `tags` parameter:

Copy

    @mcp.tool(tags={"public", "utility"})
    def public_tool() -> str:
        return "This tool is public"
    
    @mcp.tool(tags={"internal", "admin"})
    def admin_tool() -> str:
        return "This tool is for admins only"
    

The filtering logic works as follows:

*   **Include tags**: If specified, only components with at least one matching tag are exposed
*   **Exclude tags**: Components with any matching tag are filtered out
*   **Precedence**: Exclude tags always take priority over include tags

To ensure a component is never exposed, you can set `enabled=False` on the component itself. To learn more, see the component-specific documentation.

You configure tag-based filtering when creating your server:

Copy

    # Only expose components tagged with "public"
    mcp = FastMCP(include_tags={"public"})
    
    # Hide components tagged as "internal" or "deprecated"  
    mcp = FastMCP(exclude_tags={"internal", "deprecated"})
    
    # Combine both: show admin tools but hide deprecated ones
    mcp = FastMCP(include_tags={"admin"}, exclude_tags={"deprecated"})
    

This filtering applies to all component types (tools, resources, resource templates, and prompts) and affects both listing and access.

[​](https://gofastmcp.com/servers/server#running-the-server)

Running the Server
----------------------------------------------------------------------------------

FastMCP servers need a transport mechanism to communicate with clients. You typically start your server by calling the `mcp.run()` method on your `FastMCP` instance, often within an `if __name__ == "__main__":` block in your main server script. This pattern ensures compatibility with various MCP clients.

Copy

    # my_server.py
    from fastmcp import FastMCP
    
    mcp = FastMCP(name="MyServer")
    
    @mcp.tool
    def greet(name: str) -> str:
        """Greet a user by name."""
        return f"Hello, {name}!"
    
    if __name__ == "__main__":
        # This runs the server, defaulting to STDIO transport
        mcp.run()
        
        # To use a different transport, e.g., HTTP:
        # mcp.run(transport="http", host="127.0.0.1", port=9000)
    

FastMCP supports several transport options:

*   STDIO (default, for local tools)
*   HTTP (recommended for web services, uses Streamable HTTP protocol)
*   SSE (legacy web transport, deprecated)

The server can also be run using the FastMCP CLI. For detailed information on each transport, how to configure them (host, port, paths), and when to use which, please refer to the [**Running Your FastMCP Server**](https://gofastmcp.com/deployment/running-server)
 guide.

[​](https://gofastmcp.com/servers/server#custom-routes)

Custom Routes
------------------------------------------------------------------------

When running your server with HTTP transport, you can add custom web routes alongside your MCP endpoint using the `@custom_route` decorator. This is useful for simple endpoints like health checks that need to be served alongside your MCP server:

Copy

    from fastmcp import FastMCP
    from starlette.requests import Request
    from starlette.responses import PlainTextResponse
    
    mcp = FastMCP("MyServer")
    
    @mcp.custom_route("/health", methods=["GET"])
    async def health_check(request: Request) -> PlainTextResponse:
        return PlainTextResponse("OK")
    
    if __name__ == "__main__":
        mcp.run(transport="http")  # Health check at http://localhost:8000/health
    

Custom routes are served alongside your MCP endpoint and are useful for:

*   Health check endpoints for monitoring
*   Simple status or info endpoints
*   Basic webhooks or callbacks

For more complex web applications, consider [mounting your MCP server into a FastAPI or Starlette app](https://gofastmcp.com/deployment/http#integration-with-web-frameworks)
.

[​](https://gofastmcp.com/servers/server#composing-servers)

Composing Servers
--------------------------------------------------------------------------------

`` New in version: `2.2.0` `` FastMCP supports composing multiple servers together using `import_server` (static copy) and `mount` (live link). This allows you to organize large applications into modular components or reuse existing servers. See the [Server Composition](https://gofastmcp.com/servers/composition)
 guide for full details, best practices, and examples.

Copy

    # Example: Importing a subserver
    from fastmcp import FastMCP
    import asyncio
    
    main = FastMCP(name="Main")
    sub = FastMCP(name="Sub")
    
    @sub.tool
    def hello(): 
        return "hi"
    
    # Mount directly
    main.mount(sub, prefix="sub")
    

[​](https://gofastmcp.com/servers/server#proxying-servers)

Proxying Servers
------------------------------------------------------------------------------

`` New in version: `2.0.0` `` FastMCP can act as a proxy for any MCP server (local or remote) using `FastMCP.as_proxy`, letting you bridge transports or add a frontend to existing servers. For example, you can expose a remote SSE server locally via stdio, or vice versa. Proxies automatically handle concurrent operations safely by creating fresh sessions for each request when using disconnected clients. See the [Proxying Servers](https://gofastmcp.com/servers/proxy)
 guide for details and advanced usage.

Copy

    from fastmcp import FastMCP, Client
    
    backend = Client("http://example.com/mcp/sse")
    proxy = FastMCP.as_proxy(backend, name="ProxyServer")
    # Now use the proxy like any FastMCP server
    

[​](https://gofastmcp.com/servers/server#openapi-integration)

OpenAPI Integration
------------------------------------------------------------------------------------

`` New in version: `2.0.0` `` FastMCP can automatically generate servers from OpenAPI specifications or existing FastAPI applications using `FastMCP.from_openapi()` and `FastMCP.from_fastapi()`. This allows you to instantly convert existing APIs into MCP servers without manual tool creation. See the [FastAPI Integration](https://gofastmcp.com/integrations/fastapi)
 and [OpenAPI Integration](https://gofastmcp.com/integrations/openapi)
 guides for detailed examples and configuration options.

Copy

    import httpx
    from fastmcp import FastMCP
    
    # From OpenAPI spec
    spec = httpx.get("https://api.example.com/openapi.json").json()
    mcp = FastMCP.from_openapi(openapi_spec=spec, client=httpx.AsyncClient())
    
    # From FastAPI app
    from fastapi import FastAPI
    app = FastAPI()
    mcp = FastMCP.from_fastapi(app=app)
    

[​](https://gofastmcp.com/servers/server#server-configuration)

Server Configuration
--------------------------------------------------------------------------------------

Servers can be configured using a combination of initialization arguments, global settings, and transport-specific settings.

### 

[​](https://gofastmcp.com/servers/server#server-specific-configuration)

Server-Specific Configuration

Server-specific settings are passed when creating the `FastMCP` instance and control server behavior:

Copy

    from fastmcp import FastMCP
    
    # Configure server-specific settings
    mcp = FastMCP(
        name="ConfiguredServer",
        include_tags={"public", "api"},              # Only expose these tagged components
        exclude_tags={"internal", "deprecated"},     # Hide these tagged components
        on_duplicate_tools="error",                  # Handle duplicate registrations
        on_duplicate_resources="warn",
        on_duplicate_prompts="replace",
        include_fastmcp_meta=False,                  # Disable FastMCP metadata for cleaner integration
    )
    

### 

[​](https://gofastmcp.com/servers/server#global-settings)

Global Settings

Global settings affect all FastMCP servers and can be configured via environment variables (prefixed with `FASTMCP_`) or in a `.env` file:

Copy

    import fastmcp
    
    # Access global settings
    print(fastmcp.settings.log_level)        # Default: "INFO"
    print(fastmcp.settings.mask_error_details)  # Default: False
    print(fastmcp.settings.resource_prefix_format)  # Default: "path"
    print(fastmcp.settings.strict_input_validation)  # Default: False
    print(fastmcp.settings.include_fastmcp_meta)   # Default: True
    

Common global settings include:

*   **`log_level`**: Logging level (“DEBUG”, “INFO”, “WARNING”, “ERROR”, “CRITICAL”), set with `FASTMCP_LOG_LEVEL`
*   **`mask_error_details`**: Whether to hide detailed error information from clients, set with `FASTMCP_MASK_ERROR_DETAILS`
*   **`resource_prefix_format`**: How to format resource prefixes (“path” or “protocol”), set with `FASTMCP_RESOURCE_PREFIX_FORMAT`
*   **`strict_input_validation`**: Controls tool input validation mode (default: False for flexible coercion), set with `FASTMCP_STRICT_INPUT_VALIDATION`. See [Input Validation Modes](https://gofastmcp.com/servers/tools#input-validation-modes)
    
*   **`include_fastmcp_meta`**: Whether to include FastMCP metadata in component responses (default: True), set with `FASTMCP_INCLUDE_FASTMCP_META`
*   **`env_file`**: Path to the environment file to load settings from (default: “.env”), set with `FASTMCP_ENV_FILE`. Useful when your project uses a `.env` file with syntax incompatible with python-dotenv

### 

[​](https://gofastmcp.com/servers/server#transport-specific-configuration)

Transport-Specific Configuration

Transport settings are provided when running the server and control network behavior:

Copy

    # Configure transport when running
    mcp.run(
        transport="http",
        host="0.0.0.0",           # Bind to all interfaces
        port=9000,                # Custom port
        log_level="DEBUG",        # Override global log level
    )
    
    # Or for async usage
    await mcp.run_async(
        transport="http", 
        host="127.0.0.1",
        port=8080,
    )
    

### 

[​](https://gofastmcp.com/servers/server#setting-global-configuration)

Setting Global Configuration

Global FastMCP settings can be configured via environment variables (prefixed with `FASTMCP_`):

Copy

    # Configure global FastMCP behavior
    export FASTMCP_LOG_LEVEL=DEBUG
    export FASTMCP_MASK_ERROR_DETAILS=True
    export FASTMCP_RESOURCE_PREFIX_FORMAT=protocol
    export FASTMCP_STRICT_INPUT_VALIDATION=False
    export FASTMCP_INCLUDE_FASTMCP_META=False
    

### 

[​](https://gofastmcp.com/servers/server#custom-tool-serialization)

Custom Tool Serialization

`` New in version: `2.2.7` `` By default, FastMCP serializes tool return values to JSON when they need to be converted to text. You can customize this behavior by providing a `tool_serializer` function when creating your server:

Copy

    import yaml
    from fastmcp import FastMCP
    
    # Define a custom serializer that formats dictionaries as YAML
    def yaml_serializer(data):
        return yaml.dump(data, sort_keys=False)
    
    # Create a server with the custom serializer
    mcp = FastMCP(name="MyServer", tool_serializer=yaml_serializer)
    
    @mcp.tool
    def get_config():
        """Returns configuration in YAML format."""
        return {"api_key": "abc123", "debug": True, "rate_limit": 100}
    

The serializer function takes any data object and returns a string representation. This is applied to **all non-string return values** from your tools. Tools that already return strings bypass the serializer. This customization is useful when you want to:

*   Format data in a specific way (like YAML or custom formats)
*   Control specific serialization options (like indentation or sorting)
*   Add metadata or transform data before sending it to clients

If the serializer function raises an exception, the tool will fall back to the default JSON serialization to avoid breaking the server.

[FastMCP Updates\
\
Previous](https://gofastmcp.com/updates)
[Tools\
\
Next](https://gofastmcp.com/servers/tools)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.