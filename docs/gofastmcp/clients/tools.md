---
url: https://gofastmcp.com/clients/tools
title: Tool Operations - FastMCP
description: Discover and execute server-side tools with the FastMCP client.
scraped_at: 2025-11-03T18:42:02.701799
---

[Skip to main content](https://gofastmcp.com/clients/tools#content-area)

Join the [FastMCP community](https://discord.gg/uu8dJCgttd)
!

[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)

Search...

Navigation

Core Operations

Tool Operations

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
    
    *   [Tools](https://gofastmcp.com/clients/tools)
        
    *   [Resources](https://gofastmcp.com/clients/resources)
        
    *   [Prompts](https://gofastmcp.com/clients/prompts)
        
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

*   [Discovering Tools](https://gofastmcp.com/clients/tools#discovering-tools)
    
*   [Filtering by Tags](https://gofastmcp.com/clients/tools#filtering-by-tags)
    
*   [Executing Tools](https://gofastmcp.com/clients/tools#executing-tools)
    
*   [Basic Execution](https://gofastmcp.com/clients/tools#basic-execution)
    
*   [Advanced Execution Options](https://gofastmcp.com/clients/tools#advanced-execution-options)
    
*   [Handling Results](https://gofastmcp.com/clients/tools#handling-results)
    
*   [CallToolResult Properties](https://gofastmcp.com/clients/tools#calltoolresult-properties)
    
*   [Structured Data Access](https://gofastmcp.com/clients/tools#structured-data-access)
    
*   [Fallback Behavior](https://gofastmcp.com/clients/tools#fallback-behavior)
    
*   [Primitive Type Unwrapping](https://gofastmcp.com/clients/tools#primitive-type-unwrapping)
    
*   [Error Handling](https://gofastmcp.com/clients/tools#error-handling)
    
*   [Exception-Based Error Handling](https://gofastmcp.com/clients/tools#exception-based-error-handling)
    
*   [Manual Error Checking](https://gofastmcp.com/clients/tools#manual-error-checking)
    
*   [Raw MCP Protocol Access](https://gofastmcp.com/clients/tools#raw-mcp-protocol-access)
    
*   [Argument Handling](https://gofastmcp.com/clients/tools#argument-handling)
    

`` New in version: `2.0.0` `` Tools are executable functions exposed by MCP servers. The FastMCP client provides methods to discover available tools and execute them with arguments.

[​](https://gofastmcp.com/clients/tools#discovering-tools)

Discovering Tools
-------------------------------------------------------------------------------

Use `list_tools()` to retrieve all tools available on the server:

Copy

    async with client:
        tools = await client.list_tools()
        # tools -> list[mcp.types.Tool]
        
        for tool in tools:
            print(f"Tool: {tool.name}")
            print(f"Description: {tool.description}")
            if tool.inputSchema:
                print(f"Parameters: {tool.inputSchema}")
            # Access tags and other metadata
            if hasattr(tool, 'meta') and tool.meta:
                fastmcp_meta = tool.meta.get('_fastmcp', {})
                print(f"Tags: {fastmcp_meta.get('tags', [])}")
    

### 

[​](https://gofastmcp.com/clients/tools#filtering-by-tags)

Filtering by Tags

`` New in version: `2.11.0` `` You can use the `meta` field to filter tools based on their tags:

Copy

    async with client:
        tools = await client.list_tools()
        
        # Filter tools by tag
        analysis_tools = [\
            tool for tool in tools \
            if hasattr(tool, 'meta') and tool.meta and\
               tool.meta.get('_fastmcp', {}) and\
               'analysis' in tool.meta.get('_fastmcp', {}).get('tags', [])\
        ]
        
        print(f"Found {len(analysis_tools)} analysis tools")
    

The `meta` field is part of the standard MCP specification. FastMCP servers include tags and other metadata within a `_fastmcp` namespace (e.g., `meta._fastmcp.tags`) to avoid conflicts with user-defined metadata. This behavior can be controlled with the server’s `include_fastmcp_meta` setting - when disabled, the `_fastmcp` namespace won’t be included. Other MCP server implementations may not provide this metadata structure.

[​](https://gofastmcp.com/clients/tools#executing-tools)

Executing Tools
---------------------------------------------------------------------------

### 

[​](https://gofastmcp.com/clients/tools#basic-execution)

Basic Execution

Execute a tool using `call_tool()` with the tool name and arguments:

Copy

    async with client:
        # Simple tool call
        result = await client.call_tool("add", {"a": 5, "b": 3})
        # result -> CallToolResult with structured and unstructured data
        
        # Access structured data (automatically deserialized)
        print(result.data)  # 8 (int) or {"result": 8} for primitive types
        
        # Access traditional content blocks  
        print(result.content[0].text)  # "8" (TextContent)
    

### 

[​](https://gofastmcp.com/clients/tools#advanced-execution-options)

Advanced Execution Options

The `call_tool()` method supports additional parameters for timeout control and progress monitoring:

Copy

    async with client:
        # With timeout (aborts if execution takes longer than 2 seconds)
        result = await client.call_tool(
            "long_running_task", 
            {"param": "value"}, 
            timeout=2.0
        )
        
        # With progress handler (to track execution progress)
        result = await client.call_tool(
            "long_running_task",
            {"param": "value"},
            progress_handler=my_progress_handler
        )
    

**Parameters:**

*   `name`: The tool name (string)
*   `arguments`: Dictionary of arguments to pass to the tool (optional)
*   `timeout`: Maximum execution time in seconds (optional, overrides client-level timeout)
*   `progress_handler`: Progress callback function (optional, overrides client-level handler)

[​](https://gofastmcp.com/clients/tools#handling-results)

Handling Results
-----------------------------------------------------------------------------

`` New in version: `2.10.0` `` Tool execution returns a `CallToolResult` object with both structured and traditional content. FastMCP’s standout feature is the `.data` property, which doesn’t just provide raw JSON but actually hydrates complete Python objects including complex types like datetimes, UUIDs, and custom classes.

### 

[​](https://gofastmcp.com/clients/tools#calltoolresult-properties)

CallToolResult Properties

CallToolResult Properties
-------------------------

[​](https://gofastmcp.com/clients/tools#param-data)

.data

Any

**FastMCP exclusive**: Fully hydrated Python objects with complex type support (datetimes, UUIDs, custom classes). Goes beyond JSON to provide complete object reconstruction from output schemas.

[​](https://gofastmcp.com/clients/tools#param-content)

.content

list\[mcp.types.ContentBlock\]

Standard MCP content blocks (`TextContent`, `ImageContent`, `AudioContent`, etc.) available from all MCP servers.

[​](https://gofastmcp.com/clients/tools#param-structured-content)

.structured\_content

dict\[str, Any\] | None

Standard MCP structured JSON data as sent by the server, available from all MCP servers that support structured outputs.

[​](https://gofastmcp.com/clients/tools#param-is-error)

.is\_error

bool

Boolean indicating if the tool execution failed.

### 

[​](https://gofastmcp.com/clients/tools#structured-data-access)

Structured Data Access

FastMCP’s `.data` property provides fully hydrated Python objects, not just JSON dictionaries. This includes complex type reconstruction:

Copy

    from datetime import datetime
    from uuid import UUID
    
    async with client:
        result = await client.call_tool("get_weather", {"city": "London"})
        
        # FastMCP reconstructs complete Python objects from the server's output schema
        weather = result.data  # Server-defined WeatherReport object
        print(f"Temperature: {weather.temperature}°C at {weather.timestamp}")
        print(f"Station: {weather.station_id}")
        print(f"Humidity: {weather.humidity}%")
        
        # The timestamp is a real datetime object, not a string!
        assert isinstance(weather.timestamp, datetime)
        assert isinstance(weather.station_id, UUID)
        
        # Compare with raw structured JSON (standard MCP)
        print(f"Raw JSON: {result.structured_content}")
        # {"temperature": 20, "timestamp": "2024-01-15T14:30:00Z", "station_id": "123e4567-..."}
        
        # Traditional content blocks (standard MCP)  
        print(f"Text content: {result.content[0].text}")
    

### 

[​](https://gofastmcp.com/clients/tools#fallback-behavior)

Fallback Behavior

For tools without output schemas or when deserialization fails, `.data` will be `None`:

Copy

    async with client:
        result = await client.call_tool("legacy_tool", {"param": "value"})
        
        if result.data is not None:
            # Structured output available and successfully deserialized
            print(f"Structured: {result.data}")
        else:
            # No structured output or deserialization failed - use content blocks
            for content in result.content:
                if hasattr(content, 'text'):
                    print(f"Text result: {content.text}")
                elif hasattr(content, 'data'):
                    print(f"Binary data: {len(content.data)} bytes")
    

### 

[​](https://gofastmcp.com/clients/tools#primitive-type-unwrapping)

Primitive Type Unwrapping

FastMCP servers automatically wrap non-object results (like `int`, `str`, `bool`) in a `{"result": value}` structure to create valid structured outputs. FastMCP clients understand this convention and automatically unwrap the value in `.data` for convenience, so you get the original primitive value instead of a wrapper object.

Copy

    async with client:
        result = await client.call_tool("calculate_sum", {"a": 5, "b": 3})
        
        # FastMCP client automatically unwraps for convenience
        print(result.data)  # 8 (int) - the original value
        
        # Raw structured content shows the server-side wrapping
        print(result.structured_content)  # {"result": 8}
        
        # Other MCP clients would need to manually access ["result"]
        # value = result.structured_content["result"]  # Not needed with FastMCP!
    

[​](https://gofastmcp.com/clients/tools#error-handling)

Error Handling
-------------------------------------------------------------------------

### 

[​](https://gofastmcp.com/clients/tools#exception-based-error-handling)

Exception-Based Error Handling

By default, `call_tool()` raises a `ToolError` if the tool execution fails:

Copy

    from fastmcp.exceptions import ToolError
    
    async with client:
        try:
            result = await client.call_tool("potentially_failing_tool", {"param": "value"})
            print("Tool succeeded:", result.data)
        except ToolError as e:
            print(f"Tool failed: {e}")
    

### 

[​](https://gofastmcp.com/clients/tools#manual-error-checking)

Manual Error Checking

You can disable automatic error raising and manually check the result:

Copy

    async with client:
        result = await client.call_tool(
            "potentially_failing_tool", 
            {"param": "value"}, 
            raise_on_error=False
        )
        
        if result.is_error:
            print(f"Tool failed: {result.content[0].text}")
        else:
            print(f"Tool succeeded: {result.data}")
    

### 

[​](https://gofastmcp.com/clients/tools#raw-mcp-protocol-access)

Raw MCP Protocol Access

For complete control, use `call_tool_mcp()` which returns the raw MCP protocol object:

Copy

    async with client:
        result = await client.call_tool_mcp("potentially_failing_tool", {"param": "value"})
        # result -> mcp.types.CallToolResult
        
        if result.isError:
            print(f"Tool failed: {result.content}")
        else:
            print(f"Tool succeeded: {result.content}")
            # Note: No automatic deserialization with call_tool_mcp()
    

[​](https://gofastmcp.com/clients/tools#argument-handling)

Argument Handling
-------------------------------------------------------------------------------

Arguments are passed as a dictionary to the tool:

Copy

    async with client:
        # Simple arguments
        result = await client.call_tool("greet", {"name": "World"})
        
        # Complex arguments
        result = await client.call_tool("process_data", {
            "config": {"format": "json", "validate": True},
            "items": [1, 2, 3, 4, 5],
            "metadata": {"source": "api", "version": "1.0"}
        })
    

For multi-server clients, tool names are automatically prefixed with the server name (e.g., `weather_get_forecast` for a tool named `get_forecast` on the `weather` server).

[Client Transports\
\
Previous](https://gofastmcp.com/clients/transports)
[Resource Operations\
\
Next](https://gofastmcp.com/clients/resources)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.