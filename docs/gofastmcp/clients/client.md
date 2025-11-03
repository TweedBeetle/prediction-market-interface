---
url: https://gofastmcp.com/clients/client
title: The FastMCP Client - FastMCP
description: Programmatic client for interacting with MCP servers through a well-typed, Pythonic interface.
scraped_at: 2025-11-03T18:41:58.407558
---

[Skip to main content](https://gofastmcp.com/clients/client#content-area)

Join the [FastMCP community](https://discord.gg/uu8dJCgttd)
!

[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)

Search...

Navigation

Essentials

The FastMCP Client

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
    
    *   [Overview](https://gofastmcp.com/clients/client)
        
    *   [Transports](https://gofastmcp.com/clients/transports)
        
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

*   [Creating a Client](https://gofastmcp.com/clients/client#creating-a-client)
    
*   [Client-Transport Architecture](https://gofastmcp.com/clients/client#client-transport-architecture)
    
*   [Transport Inference](https://gofastmcp.com/clients/client#transport-inference)
    
*   [Configuration-Based Clients](https://gofastmcp.com/clients/client#configuration-based-clients)
    
*   [Configuration Format](https://gofastmcp.com/clients/client#configuration-format)
    
*   [Multi-Server Example](https://gofastmcp.com/clients/client#multi-server-example)
    
*   [Connection Lifecycle](https://gofastmcp.com/clients/client#connection-lifecycle)
    
*   [Operations](https://gofastmcp.com/clients/client#operations)
    
*   [Tools](https://gofastmcp.com/clients/client#tools)
    
*   [Resources](https://gofastmcp.com/clients/client#resources)
    
*   [Prompts](https://gofastmcp.com/clients/client#prompts)
    
*   [Server Connectivity](https://gofastmcp.com/clients/client#server-connectivity)
    
*   [Client Configuration](https://gofastmcp.com/clients/client#client-configuration)
    
*   [Callback Handlers](https://gofastmcp.com/clients/client#callback-handlers)
    
*   [Transport Configuration](https://gofastmcp.com/clients/client#transport-configuration)
    
*   [Next Steps](https://gofastmcp.com/clients/client#next-steps)
    
*   [Core Operations](https://gofastmcp.com/clients/client#core-operations)
    
*   [Advanced Features](https://gofastmcp.com/clients/client#advanced-features)
    
*   [Connection Details](https://gofastmcp.com/clients/client#connection-details)
    

`` New in version: `2.0.0` `` The central piece of MCP client applications is the `fastmcp.Client` class. This class provides a **programmatic interface** for interacting with any Model Context Protocol (MCP) server, handling protocol details and connection management automatically. The FastMCP Client is designed for deterministic, controlled interactions rather than autonomous behavior, making it ideal for:

*   **Testing MCP servers** during development
*   **Building deterministic applications** that need reliable MCP interactions
*   **Creating the foundation for agentic or LLM-based clients** with structured, type-safe operations

All client operations require using the `async with` context manager for proper connection lifecycle management.

This is not an agentic client - it requires explicit function calls and provides direct control over all MCP operations. Use it as a building block for higher-level systems.

[​](https://gofastmcp.com/clients/client#creating-a-client)

Creating a Client
--------------------------------------------------------------------------------

Creating a client is straightforward. You provide a server source and the client automatically infers the appropriate transport mechanism.

Copy

    import asyncio
    from fastmcp import Client, FastMCP
    
    # In-memory server (ideal for testing)
    server = FastMCP("TestServer")
    client = Client(server)
    
    # HTTP server
    client = Client("https://example.com/mcp")
    
    # Local Python script
    client = Client("my_mcp_server.py")
    
    async def main():
        async with client:
            # Basic server interaction
            await client.ping()
            
            # List available operations
            tools = await client.list_tools()
            resources = await client.list_resources()
            prompts = await client.list_prompts()
            
            # Execute operations
            result = await client.call_tool("example_tool", {"param": "value"})
            print(result)
    
    asyncio.run(main())
    

[​](https://gofastmcp.com/clients/client#client-transport-architecture)

Client-Transport Architecture
--------------------------------------------------------------------------------------------------------

The FastMCP Client separates concerns between protocol and connection:

*   **`Client`**: Handles MCP protocol operations (tools, resources, prompts) and manages callbacks
*   **`Transport`**: Establishes and maintains the connection (WebSockets, HTTP, Stdio, in-memory)

### 

[​](https://gofastmcp.com/clients/client#transport-inference)

Transport Inference

The client automatically infers the appropriate transport based on the input:

1.  **`FastMCP` instance** → In-memory transport (perfect for testing)
2.  **File path ending in `.py`** → Python Stdio transport
3.  **File path ending in `.js`** → Node.js Stdio transport
4.  **URL starting with `http://` or `https://`** → HTTP transport
5.  **`MCPConfig` dictionary** → Multi-server client

Copy

    from fastmcp import Client, FastMCP
    
    # Examples of transport inference
    client_memory = Client(FastMCP("TestServer"))
    client_script = Client("./server.py") 
    client_http = Client("https://api.example.com/mcp")
    

For testing and development, always prefer the in-memory transport by passing a `FastMCP` server directly to the client. This eliminates network complexity and separate processes.

[​](https://gofastmcp.com/clients/client#configuration-based-clients)

Configuration-Based Clients
----------------------------------------------------------------------------------------------------

`` New in version: `2.4.0` `` Create clients from MCP configuration dictionaries, which can include multiple servers. While there is no official standard for MCP configuration format, FastMCP follows established conventions used by tools like Claude Desktop.

### 

[​](https://gofastmcp.com/clients/client#configuration-format)

Configuration Format

Copy

    config = {
        "mcpServers": {
            "server_name": {
                # Remote HTTP/SSE server
                "transport": "http",  # or "sse" 
                "url": "https://api.example.com/mcp",
                "headers": {"Authorization": "Bearer token"},
                "auth": "oauth"  # or bearer token string
            },
            "local_server": {
                # Local stdio server
                "transport": "stdio",
                "command": "python",
                "args": ["./server.py", "--verbose"],
                "env": {"DEBUG": "true"},
                "cwd": "/path/to/server",
            }
        }
    }
    

### 

[​](https://gofastmcp.com/clients/client#multi-server-example)

Multi-Server Example

Copy

    config = {
        "mcpServers": {
            "weather": {"url": "https://weather-api.example.com/mcp"},
            "assistant": {"command": "python", "args": ["./assistant_server.py"]}
        }
    }
    
    client = Client(config)
    
    async with client:
        # Tools are prefixed with server names
        weather_data = await client.call_tool("weather_get_forecast", {"city": "London"})
        response = await client.call_tool("assistant_answer_question", {"question": "What's the capital of France?"})
        
        # Resources use prefixed URIs
        icons = await client.read_resource("weather://weather/icons/sunny")
        templates = await client.read_resource("resource://assistant/templates/list")
    

[​](https://gofastmcp.com/clients/client#connection-lifecycle)

Connection Lifecycle
--------------------------------------------------------------------------------------

The client operates asynchronously and uses context managers for connection management:

Copy

    async def example():
        client = Client("my_mcp_server.py")
        
        # Connection established here
        async with client:
            print(f"Connected: {client.is_connected()}")
            
            # Make multiple calls within the same session
            tools = await client.list_tools()
            result = await client.call_tool("greet", {"name": "World"})
            
        # Connection closed automatically here
        print(f"Connected: {client.is_connected()}")
    

[​](https://gofastmcp.com/clients/client#operations)

Operations
------------------------------------------------------------------

FastMCP clients can interact with several types of server components:

### 

[​](https://gofastmcp.com/clients/client#tools)

Tools

Tools are server-side functions that the client can execute with arguments.

Copy

    async with client:
        # List available tools
        tools = await client.list_tools()
        
        # Execute a tool
        result = await client.call_tool("multiply", {"a": 5, "b": 3})
        print(result.data)  # 15
    

See [Tools](https://gofastmcp.com/clients/tools)
 for detailed documentation.

### 

[​](https://gofastmcp.com/clients/client#resources)

Resources

Resources are data sources that the client can read, either static or templated.

Copy

    async with client:
        # List available resources
        resources = await client.list_resources()
        
        # Read a resource
        content = await client.read_resource("file:///config/settings.json")
        print(content[0].text)
    

See [Resources](https://gofastmcp.com/clients/resources)
 for detailed documentation.

### 

[​](https://gofastmcp.com/clients/client#prompts)

Prompts

Prompts are reusable message templates that can accept arguments.

Copy

    async with client:
        # List available prompts
        prompts = await client.list_prompts()
        
        # Get a rendered prompt
        messages = await client.get_prompt("analyze_data", {"data": [1, 2, 3]})
        print(messages.messages)
    

See [Prompts](https://gofastmcp.com/clients/prompts)
 for detailed documentation.

### 

[​](https://gofastmcp.com/clients/client#server-connectivity)

Server Connectivity

Use `ping()` to verify the server is reachable:

Copy

    async with client:
        await client.ping()
        print("Server is reachable")
    

[​](https://gofastmcp.com/clients/client#client-configuration)

Client Configuration
--------------------------------------------------------------------------------------

Clients can be configured with additional handlers and settings for specialized use cases.

### 

[​](https://gofastmcp.com/clients/client#callback-handlers)

Callback Handlers

The client supports several callback handlers for advanced server interactions:

Copy

    from fastmcp import Client
    from fastmcp.client.logging import LogMessage
    
    async def log_handler(message: LogMessage):
        print(f"Server log: {message.data}")
    
    async def progress_handler(progress: float, total: float | None, message: str | None):
        print(f"Progress: {progress}/{total} - {message}")
    
    async def sampling_handler(messages, params, context):
        # Integrate with your LLM service here
        return "Generated response"
    
    client = Client(
        "my_mcp_server.py",
        log_handler=log_handler,
        progress_handler=progress_handler,
        sampling_handler=sampling_handler,
        timeout=30.0
    )
    

The `Client` constructor accepts several configuration options:

*   `transport`: Transport instance or source for automatic inference
*   `log_handler`: Handle server log messages
*   `progress_handler`: Monitor long-running operations
*   `sampling_handler`: Respond to server LLM requests
*   `roots`: Provide local context to servers
*   `timeout`: Default timeout for requests (in seconds)

### 

[​](https://gofastmcp.com/clients/client#transport-configuration)

Transport Configuration

For detailed transport configuration (headers, authentication, environment variables), see the [Transports](https://gofastmcp.com/clients/transports)
 documentation.

[​](https://gofastmcp.com/clients/client#next-steps)

Next Steps
------------------------------------------------------------------

Explore the detailed documentation for each operation type:

### 

[​](https://gofastmcp.com/clients/client#core-operations)

Core Operations

*   **[Tools](https://gofastmcp.com/clients/tools)
    ** - Execute server-side functions and handle results
*   **[Resources](https://gofastmcp.com/clients/resources)
    ** - Access static and templated resources
*   **[Prompts](https://gofastmcp.com/clients/prompts)
    ** - Work with message templates and argument serialization

### 

[​](https://gofastmcp.com/clients/client#advanced-features)

Advanced Features

*   **[Logging](https://gofastmcp.com/clients/logging)
    ** - Handle server log messages
*   **[Progress](https://gofastmcp.com/clients/progress)
    ** - Monitor long-running operations
*   **[Sampling](https://gofastmcp.com/clients/sampling)
    ** - Respond to server LLM requests
*   **[Roots](https://gofastmcp.com/clients/roots)
    ** - Provide local context to servers

### 

[​](https://gofastmcp.com/clients/client#connection-details)

Connection Details

*   **[Transports](https://gofastmcp.com/clients/transports)
    ** - Configure connection methods and parameters
*   **[Authentication](https://gofastmcp.com/clients/auth/oauth)
    ** - Set up OAuth and bearer token authentication

The FastMCP Client is designed as a foundational tool. Use it directly for deterministic operations, or build higher-level agentic systems on top of its reliable, type-safe interface.

[Project Configuration\
\
Previous](https://gofastmcp.com/deployment/server-configuration)
[Client Transports\
\
Next](https://gofastmcp.com/clients/transports)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.