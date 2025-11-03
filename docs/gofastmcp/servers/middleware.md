---
url: https://gofastmcp.com/servers/middleware
title: MCP Middleware - FastMCP
description: Add cross-cutting functionality to your MCP server with middleware that can inspect, modify, and respond to all MCP requests and responses.
scraped_at: 2025-11-03T18:43:18.028981
---

[Skip to main content](https://gofastmcp.com/servers/middleware#content-area)

Join the [FastMCP community](https://discord.gg/uu8dJCgttd)
!

[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)

Search...

Navigation

Advanced Features

MCP Middleware

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

*   [What is MCP Middleware?](https://gofastmcp.com/servers/middleware#what-is-mcp-middleware%3F)
    
*   [How Middleware Works](https://gofastmcp.com/servers/middleware#how-middleware-works)
    
*   [Middleware Hooks](https://gofastmcp.com/servers/middleware#middleware-hooks)
    
*   [Hook Hierarchy and Execution Order](https://gofastmcp.com/servers/middleware#hook-hierarchy-and-execution-order)
    
*   [Available Hooks](https://gofastmcp.com/servers/middleware#available-hooks)
    
*   [Component Access in Middleware](https://gofastmcp.com/servers/middleware#component-access-in-middleware)
    
*   [Listing Operations vs Execution Operations](https://gofastmcp.com/servers/middleware#listing-operations-vs-execution-operations)
    
*   [Accessing Component Metadata During Execution](https://gofastmcp.com/servers/middleware#accessing-component-metadata-during-execution)
    
*   [Working with Listing Results](https://gofastmcp.com/servers/middleware#working-with-listing-results)
    
*   [Tool Call Denial](https://gofastmcp.com/servers/middleware#tool-call-denial)
    
*   [Tool Call Modification](https://gofastmcp.com/servers/middleware#tool-call-modification)
    
*   [Anatomy of a Hook](https://gofastmcp.com/servers/middleware#anatomy-of-a-hook)
    
*   [Hook Parameters](https://gofastmcp.com/servers/middleware#hook-parameters)
    
*   [Control Flow](https://gofastmcp.com/servers/middleware#control-flow)
    
*   [State Management](https://gofastmcp.com/servers/middleware#state-management)
    
*   [Creating Middleware](https://gofastmcp.com/servers/middleware#creating-middleware)
    
*   [Adding Middleware to Your Server](https://gofastmcp.com/servers/middleware#adding-middleware-to-your-server)
    
*   [Single Middleware](https://gofastmcp.com/servers/middleware#single-middleware)
    
*   [Multiple Middleware](https://gofastmcp.com/servers/middleware#multiple-middleware)
    
*   [Server Composition and Middleware](https://gofastmcp.com/servers/middleware#server-composition-and-middleware)
    
*   [Built-in Middleware Examples](https://gofastmcp.com/servers/middleware#built-in-middleware-examples)
    
*   [Timing Middleware](https://gofastmcp.com/servers/middleware#timing-middleware)
    
*   [Tool Injection Middleware](https://gofastmcp.com/servers/middleware#tool-injection-middleware)
    
*   [Prompt Tool Middleware](https://gofastmcp.com/servers/middleware#prompt-tool-middleware)
    
*   [Resource Tool Middleware](https://gofastmcp.com/servers/middleware#resource-tool-middleware)
    
*   [Caching Middleware](https://gofastmcp.com/servers/middleware#caching-middleware)
    
*   [Storage Backends](https://gofastmcp.com/servers/middleware#storage-backends)
    
*   [Cache Statistics](https://gofastmcp.com/servers/middleware#cache-statistics)
    
*   [Logging Middleware](https://gofastmcp.com/servers/middleware#logging-middleware)
    
*   [Rate Limiting Middleware](https://gofastmcp.com/servers/middleware#rate-limiting-middleware)
    
*   [Error Handling Middleware](https://gofastmcp.com/servers/middleware#error-handling-middleware)
    
*   [Combining Middleware](https://gofastmcp.com/servers/middleware#combining-middleware)
    
*   [Custom Middleware Example](https://gofastmcp.com/servers/middleware#custom-middleware-example)
    

`` New in version: `2.9.0` `` MCP middleware is a powerful concept that allows you to add cross-cutting functionality to your FastMCP server. Unlike traditional web middleware, MCP middleware is designed specifically for the Model Context Protocol, providing hooks for different types of MCP operations like tool calls, resource reads, and prompt requests.

MCP middleware is a FastMCP-specific concept and is not part of the official MCP protocol specification. This middleware system is designed to work with FastMCP servers and may not be compatible with other MCP implementations.

MCP middleware is a brand new concept and may be subject to breaking changes in future versions.

[​](https://gofastmcp.com/servers/middleware#what-is-mcp-middleware%3F)

What is MCP Middleware?
--------------------------------------------------------------------------------------------------

MCP middleware lets you intercept and modify MCP requests and responses as they flow through your server. Think of it as a pipeline where each piece of middleware can inspect what’s happening, make changes, and then pass control to the next middleware in the chain. Common use cases for MCP middleware include:

*   **Authentication and Authorization**: Verify client permissions before executing operations
*   **Logging and Monitoring**: Track usage patterns and performance metrics
*   **Rate Limiting**: Control request frequency per client or operation type
*   **Request/Response Transformation**: Modify data before it reaches tools or after it leaves
*   **Caching**: Store frequently requested data to improve performance
*   **Error Handling**: Provide consistent error responses across your server

[​](https://gofastmcp.com/servers/middleware#how-middleware-works)

How Middleware Works
------------------------------------------------------------------------------------------

FastMCP middleware operates on a pipeline model. When a request comes in, it flows through your middleware in the order they were added to the server. Each middleware can:

1.  **Inspect the incoming request** and its context
2.  **Modify the request** before passing it to the next middleware or handler
3.  **Execute the next middleware/handler** in the chain by calling `call_next()`
4.  **Inspect and modify the response** before returning it
5.  **Handle errors** that occur during processing

The key insight is that middleware forms a chain where each piece decides whether to continue processing or stop the chain entirely. If you’re familiar with ASGI middleware, the basic structure of FastMCP middleware will feel familiar. At its core, middleware is a callable class that receives a context object containing information about the current JSON-RPC message and a handler function to continue the middleware chain. It’s important to understand that MCP operates on the [JSON-RPC specification](https://spec.modelcontextprotocol.io/specification/basic/transports/)
. While FastMCP presents requests and responses in a familiar way, these are fundamentally JSON-RPC messages, not HTTP request/response pairs like you might be used to in web applications. FastMCP middleware works with all [transport types](https://gofastmcp.com/clients/transports)
, including local stdio transport and HTTP transports, though not all middleware implementations are compatible across all transports (e.g., middleware that inspects HTTP headers won’t work with stdio transport). The most fundamental way to implement middleware is by overriding the `__call__` method on the `Middleware` base class:

Copy

    from fastmcp.server.middleware import Middleware, MiddlewareContext
    
    class RawMiddleware(Middleware):
        async def __call__(self, context: MiddlewareContext, call_next):
            # This method receives ALL messages regardless of type
            print(f"Raw middleware processing: {context.method}")
            result = await call_next(context)
            print(f"Raw middleware completed: {context.method}")
            return result
    

This gives you complete control over every message that flows through your server, but requires you to handle all message types manually.

[​](https://gofastmcp.com/servers/middleware#middleware-hooks)

Middleware Hooks
----------------------------------------------------------------------------------

To make it easier for users to target specific types of messages, FastMCP middleware provides a variety of specialized hooks. Instead of implementing the raw `__call__` method, you can override specific hook methods that are called only for certain types of operations, allowing you to target exactly the level of specificity you need for your middleware logic.

### 

[​](https://gofastmcp.com/servers/middleware#hook-hierarchy-and-execution-order)

Hook Hierarchy and Execution Order

FastMCP provides multiple hooks that are called with varying levels of specificity. Understanding this hierarchy is crucial for effective middleware design. When a request comes in, **multiple hooks may be called for the same request**, going from general to specific:

1.  **`on_message`** - Called for ALL MCP messages (both requests and notifications)
2.  **`on_request` or `on_notification`** - Called based on the message type
3.  **Operation-specific hooks** - Called for specific MCP operations like `on_call_tool`

For example, when a client calls a tool, your middleware will receive **multiple hook calls**:

1.  `on_message` and `on_request` for any initial tool discovery operations (list\_tools)
2.  `on_message` (because it’s any MCP message) for the tool call itself
3.  `on_request` (because tool calls expect responses) for the tool call itself
4.  `on_call_tool` (because it’s specifically a tool execution) for the tool call itself

Note that the MCP SDK may perform additional operations like listing tools for caching purposes, which will trigger additional middleware calls beyond just the direct tool execution. This hierarchy allows you to target your middleware logic with the right level of specificity. Use `on_message` for broad concerns like logging, `on_request` for authentication, and `on_call_tool` for tool-specific logic like performance monitoring.

### 

[​](https://gofastmcp.com/servers/middleware#available-hooks)

Available Hooks

`` New in version: `2.9.0` ``

*   `on_message`: Called for all MCP messages (requests and notifications)
*   `on_request`: Called specifically for MCP requests (that expect responses)
*   `on_notification`: Called specifically for MCP notifications (fire-and-forget)
*   `on_call_tool`: Called when tools are being executed
*   `on_read_resource`: Called when resources are being read
*   `on_get_prompt`: Called when prompts are being retrieved
*   `on_list_tools`: Called when listing available tools
*   `on_list_resources`: Called when listing available resources
*   `on_list_resource_templates`: Called when listing resource templates
*   `on_list_prompts`: Called when listing available prompts

`` New in version: `2.13.0` ``

*   `on_initialize`: Called when a client connects and initializes the session (returns `None`)

The `on_initialize` hook receives the client’s initialization request but **returns `None`** rather than a result. The initialization response is handled internally by the MCP protocol and cannot be modified by middleware. This hook is useful for client detection, logging connections, or initializing session state, but not for modifying the initialization handshake itself.

[​](https://gofastmcp.com/servers/middleware#component-access-in-middleware)

Component Access in Middleware
--------------------------------------------------------------------------------------------------------------

Understanding how to access component information (tools, resources, prompts) in middleware is crucial for building powerful middleware functionality. The access patterns differ significantly between listing operations and execution operations.

### 

[​](https://gofastmcp.com/servers/middleware#listing-operations-vs-execution-operations)

Listing Operations vs Execution Operations

FastMCP middleware handles two types of operations differently: **Listing Operations** (`on_list_tools`, `on_list_resources`, `on_list_prompts`, etc.):

*   Middleware receives **FastMCP component objects** with full metadata
*   These objects include FastMCP-specific properties like `tags` that can be accessed directly from the component
*   The result contains complete component information before it’s converted to MCP format
*   Tags are included in the component’s `meta` field in the listing response returned to MCP clients

**Execution Operations** (`on_call_tool`, `on_read_resource`, `on_get_prompt`):

*   Middleware runs **before** the component is executed
*   The middleware result is either the execution result or an error if the component wasn’t found
*   Component metadata isn’t directly available in the hook parameters

### 

[​](https://gofastmcp.com/servers/middleware#accessing-component-metadata-during-execution)

Accessing Component Metadata During Execution

If you need to check component properties (like tags) during execution operations, use the FastMCP server instance available through the context:

Copy

    from fastmcp.server.middleware import Middleware, MiddlewareContext
    from fastmcp.exceptions import ToolError
    
    class TagBasedMiddleware(Middleware):
        async def on_call_tool(self, context: MiddlewareContext, call_next):
            # Access the tool object to check its metadata
            if context.fastmcp_context:
                try:
                    tool = await context.fastmcp_context.fastmcp.get_tool(context.message.name)
                    
                    # Check if this tool has a "private" tag
                    if "private" in tool.tags:
                        raise ToolError("Access denied: private tool")
                        
                    # Check if tool is enabled
                    if not tool.enabled:
                        raise ToolError("Tool is currently disabled")
                        
                except Exception:
                    # Tool not found or other error - let execution continue
                    # and handle the error naturally
                    pass
            
            return await call_next(context)
    

The same pattern works for resources and prompts:

Copy

    from fastmcp.server.middleware import Middleware, MiddlewareContext
    from fastmcp.exceptions import ResourceError, PromptError
    
    class ComponentAccessMiddleware(Middleware):
        async def on_read_resource(self, context: MiddlewareContext, call_next):
            if context.fastmcp_context:
                try:
                    resource = await context.fastmcp_context.fastmcp.get_resource(context.message.uri)
                    if "restricted" in resource.tags:
                        raise ResourceError("Access denied: restricted resource")
                except Exception:
                    pass
            return await call_next(context)
        
        async def on_get_prompt(self, context: MiddlewareContext, call_next):
            if context.fastmcp_context:
                try:
                    prompt = await context.fastmcp_context.fastmcp.get_prompt(context.message.name)
                    if not prompt.enabled:
                        raise PromptError("Prompt is currently disabled")
                except Exception:
                    pass
            return await call_next(context)
    

### 

[​](https://gofastmcp.com/servers/middleware#working-with-listing-results)

Working with Listing Results

For listing operations, the middleware `call_next` function returns a list of FastMCP components prior to being converted to MCP format. You can filter or modify this list and return it to the client. For example:

Copy

    from fastmcp.server.middleware import Middleware, MiddlewareContext
    
    class ListingFilterMiddleware(Middleware):
        async def on_list_tools(self, context: MiddlewareContext, call_next):
            result = await call_next(context)
            
            # Filter out tools with "private" tag
            filtered_tools = [\
                tool for tool in result \
                if "private" not in tool.tags\
            ]
            
            # Return modified list
            return filtered_tools
    

This filtering happens before the components are converted to MCP format and returned to the client. Tags are accessible both during filtering and are included in the component’s `meta` field in the final listing response.

When filtering components in listing operations, ensure you also prevent execution of filtered components in the corresponding execution hooks (`on_call_tool`, `on_read_resource`, `on_get_prompt`) to maintain consistency.

### 

[​](https://gofastmcp.com/servers/middleware#tool-call-denial)

Tool Call Denial

You can deny access to specific tools by raising a `ToolError` in your middleware. This is the correct way to block tool execution, as it integrates properly with the FastMCP error handling system.

Copy

    from fastmcp.server.middleware import Middleware, MiddlewareContext
    from fastmcp.exceptions import ToolError
    
    class AuthMiddleware(Middleware):
        async def on_call_tool(self, context: MiddlewareContext, call_next):
            tool_name = context.message.name
            
            # Deny access to restricted tools
            if tool_name.lower() in ["delete", "admin_config"]:
                raise ToolError("Access denied: tool requires admin privileges")
            
            # Allow other tools to proceed
            return await call_next(context)
    

When denying tool calls, always raise `ToolError` rather than returning `ToolResult` objects or other values. `ToolError` ensures proper error propagation through the middleware chain and converts to the correct MCP error response format.

### 

[​](https://gofastmcp.com/servers/middleware#tool-call-modification)

Tool Call Modification

For execution operations like tool calls, you can modify arguments before execution or transform results afterward:

Copy

    from fastmcp.server.middleware import Middleware, MiddlewareContext
    
    class ToolCallMiddleware(Middleware):
        async def on_call_tool(self, context: MiddlewareContext, call_next):
            # Modify arguments before execution
            if context.message.name == "calculate":
                # Ensure positive inputs
                if context.message.arguments.get("value", 0) < 0:
                    context.message.arguments["value"] = abs(context.message.arguments["value"])
            
            result = await call_next(context)
            
            # Transform result after execution
            if context.message.name == "get_data":
                # Add metadata to result
                if result.structured_content:
                    result.structured_content["processed_at"] = "2024-01-01T00:00:00Z"
            
            return result
    

For more complex tool rewriting scenarios, consider using [Tool Transformation](https://gofastmcp.com/patterns/tool-transformation)
 patterns which provide a more structured approach to creating modified tool variants.

### 

[​](https://gofastmcp.com/servers/middleware#anatomy-of-a-hook)

Anatomy of a Hook

Every middleware hook follows the same pattern. Let’s examine the `on_message` hook to understand the structure:

Copy

    async def on_message(self, context: MiddlewareContext, call_next):
        # 1. Pre-processing: Inspect and optionally modify the request
        print(f"Processing {context.method}")
        
        # 2. Chain continuation: Call the next middleware/handler
        result = await call_next(context)
        
        # 3. Post-processing: Inspect and optionally modify the response
        print(f"Completed {context.method}")
        
        # 4. Return the result (potentially modified)
        return result
    

### 

[​](https://gofastmcp.com/servers/middleware#hook-parameters)

Hook Parameters

Every hook receives two parameters:

1.  **`context: MiddlewareContext`** - Contains information about the current request:
    *   `context.method` - The MCP method name (e.g., “tools/call”)
    *   `context.source` - Where the request came from (“client” or “server”)
    *   `context.type` - Message type (“request” or “notification”)
    *   `context.message` - The MCP message data
    *   `context.timestamp` - When the request was received
    *   `context.fastmcp_context` - FastMCP Context object (if available)
2.  **`call_next`** - A function that continues the middleware chain. You **must** call this to proceed, unless you want to stop processing entirely.

### 

[​](https://gofastmcp.com/servers/middleware#control-flow)

Control Flow

You have complete control over the request flow:

*   **Continue processing**: Call `await call_next(context)` to proceed
*   **Modify the request**: Change the context before calling `call_next`
*   **Modify the response**: Change the result after calling `call_next`
*   **Stop the chain**: Don’t call `call_next` (rarely needed)
*   **Handle errors**: Wrap `call_next` in try/catch blocks

#### 

[​](https://gofastmcp.com/servers/middleware#state-management)

State Management

`` New in version: `2.11.0` `` In addition to modifying the request and response, you can also store state data that your tools can (optionally) access later. To do so, use the FastMCP Context to either `set_state` or `get_state` as appropriate. For more information, see the [Context State Management](https://gofastmcp.com/servers/context#state-management)
 docs.

[​](https://gofastmcp.com/servers/middleware#creating-middleware)

Creating Middleware
----------------------------------------------------------------------------------------

FastMCP middleware is implemented by subclassing the `Middleware` base class and overriding the hooks you need. You only need to implement the hooks that are relevant to your use case.

Copy

    from fastmcp import FastMCP
    from fastmcp.server.middleware import Middleware, MiddlewareContext
    
    class LoggingMiddleware(Middleware):
        """Middleware that logs all MCP operations."""
        
        async def on_message(self, context: MiddlewareContext, call_next):
            """Called for all MCP messages."""
            print(f"Processing {context.method} from {context.source}")
            
            result = await call_next(context)
            
            print(f"Completed {context.method}")
            return result
    
    # Add middleware to your server
    mcp = FastMCP("MyServer")
    mcp.add_middleware(LoggingMiddleware())
    

This creates a basic logging middleware that will print information about every request that flows through your server.

[​](https://gofastmcp.com/servers/middleware#adding-middleware-to-your-server)

Adding Middleware to Your Server
------------------------------------------------------------------------------------------------------------------

### 

[​](https://gofastmcp.com/servers/middleware#single-middleware)

Single Middleware

Adding middleware to your server is straightforward:

Copy

    mcp = FastMCP("MyServer")
    mcp.add_middleware(LoggingMiddleware())
    

### 

[​](https://gofastmcp.com/servers/middleware#multiple-middleware)

Multiple Middleware

Middleware executes in the order it’s added to the server. The first middleware added runs first on the way in, and last on the way out:

Copy

    mcp = FastMCP("MyServer")
    
    mcp.add_middleware(AuthenticationMiddleware("secret-token"))
    mcp.add_middleware(PerformanceMiddleware())
    mcp.add_middleware(LoggingMiddleware())
    

This creates the following execution flow:

1.  AuthenticationMiddleware (pre-processing)
2.  PerformanceMiddleware (pre-processing)
3.  LoggingMiddleware (pre-processing)
4.  Actual tool/resource handler
5.  LoggingMiddleware (post-processing)
6.  PerformanceMiddleware (post-processing)
7.  AuthenticationMiddleware (post-processing)

[​](https://gofastmcp.com/servers/middleware#server-composition-and-middleware)

Server Composition and Middleware
--------------------------------------------------------------------------------------------------------------------

When using [Server Composition](https://gofastmcp.com/servers/composition)
 with `mount` or `import_server`, middleware behavior follows these rules:

1.  **Parent server middleware** runs for all requests, including those routed to mounted servers
2.  **Mounted server middleware** only runs for requests handled by that specific server
3.  **Middleware order** is preserved within each server

This allows you to create layered middleware architectures where parent servers handle cross-cutting concerns like authentication, while child servers focus on domain-specific middleware.

Copy

    # Parent server with middleware
    parent = FastMCP("Parent")
    parent.add_middleware(AuthenticationMiddleware("token"))
    
    # Child server with its own middleware  
    child = FastMCP("Child")
    child.add_middleware(LoggingMiddleware())
    
    @child.tool
    def child_tool() -> str:
        return "from child"
    
    # Mount the child server
    parent.mount(child, prefix="child")
    

When a client calls “child\_tool”, the request will flow through the parent’s authentication middleware first, then route to the child server where it will go through the child’s logging middleware.

[​](https://gofastmcp.com/servers/middleware#built-in-middleware-examples)

Built-in Middleware Examples
----------------------------------------------------------------------------------------------------------

FastMCP includes several middleware implementations that demonstrate best practices and provide immediately useful functionality. Let’s explore how each type works by building simplified versions, then see how to use the full implementations.

### 

[​](https://gofastmcp.com/servers/middleware#timing-middleware)

Timing Middleware

Performance monitoring is essential for understanding your server’s behavior and identifying bottlenecks. FastMCP includes timing middleware at `fastmcp.server.middleware.timing`. Here’s an example of how it works:

Copy

    import time
    from fastmcp.server.middleware import Middleware, MiddlewareContext
    
    class SimpleTimingMiddleware(Middleware):
        async def on_request(self, context: MiddlewareContext, call_next):
            start_time = time.perf_counter()
            
            try:
                result = await call_next(context)
                duration_ms = (time.perf_counter() - start_time) * 1000
                print(f"Request {context.method} completed in {duration_ms:.2f}ms")
                return result
            except Exception as e:
                duration_ms = (time.perf_counter() - start_time) * 1000
                print(f"Request {context.method} failed after {duration_ms:.2f}ms: {e}")
                raise
    

To use the full version with proper logging and configuration:

Copy

    from fastmcp.server.middleware.timing import (
        TimingMiddleware, 
        DetailedTimingMiddleware
    )
    
    # Basic timing for all requests
    mcp.add_middleware(TimingMiddleware())
    
    # Detailed per-operation timing (tools, resources, prompts)
    mcp.add_middleware(DetailedTimingMiddleware())
    

The built-in versions include custom logger support, proper formatting, and **DetailedTimingMiddleware** provides operation-specific hooks like `on_call_tool` and `on_read_resource` for granular timing.

### 

[​](https://gofastmcp.com/servers/middleware#tool-injection-middleware)

Tool Injection Middleware

Tool injection middleware is a middleware that injects tools into the server during the request lifecycle:

Copy

    from fastmcp.server.middleware.tool_injection import ToolInjectionMiddleware
    
    def my_tool_fn(a: int, b: int) -> int:
        return a + b
    
    my_tool = Tool.from_function(fn=my_tool_fn, name="my_tool")
    
    mcp.add_middleware(ToolInjectionMiddleware(tools=[my_tool]))
    

### 

[​](https://gofastmcp.com/servers/middleware#prompt-tool-middleware)

Prompt Tool Middleware

Prompt tool middleware is a compatibility middleware for clients that are unable to list or get prompts. It provides two tools: `list_prompts` and `get_prompt` which allow clients to list and get prompts respectively using only tool calls.

Copy

    from fastmcp.server.middleware.tool_injection import PromptToolMiddleware
    
    mcp.add_middleware(PromptToolMiddleware())
    

### 

[​](https://gofastmcp.com/servers/middleware#resource-tool-middleware)

Resource Tool Middleware

Resource tool middleware is a compatibility middleware for clients that are unable to list or read resources. It provides two tools: `list_resources` and `read_resource` which allow clients to list and read resources respectively using only tool calls.

Copy

    from fastmcp.server.middleware.tool_injection import ResourceToolMiddleware
    
    mcp.add_middleware(ResourceToolMiddleware())
    

### 

[​](https://gofastmcp.com/servers/middleware#caching-middleware)

Caching Middleware

Caching middleware is essential for improving performance and reducing server load. FastMCP provides caching middleware at `fastmcp.server.middleware.caching`. Here’s how to use the full version:

Copy

    from fastmcp.server.middleware.caching import ResponseCachingMiddleware
    
    mcp.add_middleware(ResponseCachingMiddleware())
    

Out of the box, it caches call/list tool, resources, and prompts to an in-memory cache with TTL-based expiration. Cache entries expire based on their TTL; there is no event-based cache invalidation. List calls are stored under global keys—when sharing a storage backend across multiple servers, consider namespacing collections to prevent conflicts. See [Storage Backends](https://gofastmcp.com/servers/storage-backends)
 for advanced configuration options. Each method can be configured individually, for example, caching list tools for 30 seconds, limiting caching to specific tools, and disabling caching for resource reads:

Copy

    from fastmcp.server.middleware.caching import ResponseCachingMiddleware, CallToolSettings, ListToolsSettings, ReadResourceSettings
    
    mcp.add_middleware(ResponseCachingMiddleware(
        list_tools_settings=ListToolsSettings(
            ttl=30,
        ),
        call_tool_settings=CallToolSettings(
            included_tools=["tool1"],
        ),
        read_resource_settings=ReadResourceSettings(
            enabled=False
        )
    ))
    

#### 

[​](https://gofastmcp.com/servers/middleware#storage-backends)

Storage Backends

By default, caching uses in-memory storage, which is fast but doesn’t persist across restarts. For production or persistent caching across server restarts, configure a different storage backend. See [Storage Backends](https://gofastmcp.com/servers/storage-backends)
 for complete options including disk, Redis, DynamoDB, and custom implementations. Disk-based caching example:

Copy

    from fastmcp.server.middleware.caching import ResponseCachingMiddleware
    from key_value.aio.stores.disk import DiskStore
    
    mcp.add_middleware(ResponseCachingMiddleware(
        cache_storage=DiskStore(directory="cache"),
    ))
    

Redis for distributed deployments:

Copy

    from fastmcp.server.middleware.caching import ResponseCachingMiddleware
    from key_value.aio.stores.redis import RedisStore
    
    mcp.add_middleware(ResponseCachingMiddleware(
        cache_storage=RedisStore(host="redis.example.com", port=6379),
    ))
    

#### 

[​](https://gofastmcp.com/servers/middleware#cache-statistics)

Cache Statistics

The caching middleware collects operation statistics (hits, misses, etc.) through the underlying storage layer. Access statistics from the middleware instance:

Copy

    from fastmcp.server.middleware.caching import ResponseCachingMiddleware
    
    middleware = ResponseCachingMiddleware()
    mcp.add_middleware(middleware)
    
    # Later, retrieve statistics
    stats = middleware.statistics()
    print(f"Total cache operations: {stats}")
    

### 

[​](https://gofastmcp.com/servers/middleware#logging-middleware)

Logging Middleware

Request and response logging is crucial for debugging, monitoring, and understanding usage patterns in your MCP server. FastMCP provides comprehensive logging middleware at `fastmcp.server.middleware.logging`. Here’s an example of how it works:

Copy

    from fastmcp.server.middleware import Middleware, MiddlewareContext
    
    class SimpleLoggingMiddleware(Middleware):
        async def on_message(self, context: MiddlewareContext, call_next):
            print(f"Processing {context.method} from {context.source}")
            
            try:
                result = await call_next(context)
                print(f"Completed {context.method}")
                return result
            except Exception as e:
                print(f"Failed {context.method}: {e}")
                raise
    

To use the full versions with advanced features:

Copy

    from fastmcp.server.middleware.logging import (
        LoggingMiddleware, 
        StructuredLoggingMiddleware
    )
    
    # Human-readable logging with payload support
    mcp.add_middleware(LoggingMiddleware(
        include_payloads=True,
        max_payload_length=1000
    ))
    
    # JSON-structured logging for log aggregation tools
    mcp.add_middleware(StructuredLoggingMiddleware(include_payloads=True))
    

The built-in versions include payload logging, structured JSON output, custom logger support, payload size limits, and operation-specific hooks for granular control.

### 

[​](https://gofastmcp.com/servers/middleware#rate-limiting-middleware)

Rate Limiting Middleware

Rate limiting is essential for protecting your server from abuse, ensuring fair resource usage, and maintaining performance under load. FastMCP includes sophisticated rate limiting middleware at `fastmcp.server.middleware.rate_limiting`. Here’s an example of how it works:

Copy

    import time
    from collections import defaultdict
    from fastmcp.server.middleware import Middleware, MiddlewareContext
    from mcp import McpError
    from mcp.types import ErrorData
    
    class SimpleRateLimitMiddleware(Middleware):
        def __init__(self, requests_per_minute: int = 60):
            self.requests_per_minute = requests_per_minute
            self.client_requests = defaultdict(list)
        
        async def on_request(self, context: MiddlewareContext, call_next):
            current_time = time.time()
            client_id = "default"  # In practice, extract from headers or context
            
            # Clean old requests and check limit
            cutoff_time = current_time - 60
            self.client_requests[client_id] = [\
                req_time for req_time in self.client_requests[client_id]\
                if req_time > cutoff_time\
            ]
            
            if len(self.client_requests[client_id]) >= self.requests_per_minute:
                raise McpError(ErrorData(code=-32000, message="Rate limit exceeded"))
            
            self.client_requests[client_id].append(current_time)
            return await call_next(context)
    

To use the full versions with advanced algorithms:

Copy

    from fastmcp.server.middleware.rate_limiting import (
        RateLimitingMiddleware, 
        SlidingWindowRateLimitingMiddleware
    )
    
    # Token bucket rate limiting (allows controlled bursts)
    mcp.add_middleware(RateLimitingMiddleware(
        max_requests_per_second=10.0,
        burst_capacity=20
    ))
    
    # Sliding window rate limiting (precise time-based control)
    mcp.add_middleware(SlidingWindowRateLimitingMiddleware(
        max_requests=100,
        window_minutes=1
    ))
    

The built-in versions include token bucket algorithms, per-client identification, global rate limiting, and async-safe implementations with configurable client identification functions.

### 

[​](https://gofastmcp.com/servers/middleware#error-handling-middleware)

Error Handling Middleware

Consistent error handling and recovery is critical for robust MCP servers. FastMCP provides comprehensive error handling middleware at `fastmcp.server.middleware.error_handling`. Here’s an example of how it works:

Copy

    import logging
    from fastmcp.server.middleware import Middleware, MiddlewareContext
    
    class SimpleErrorHandlingMiddleware(Middleware):
        def __init__(self):
            self.logger = logging.getLogger("errors")
            self.error_counts = {}
        
        async def on_message(self, context: MiddlewareContext, call_next):
            try:
                return await call_next(context)
            except Exception as error:
                # Log the error and track statistics
                error_key = f"{type(error).__name__}:{context.method}"
                self.error_counts[error_key] = self.error_counts.get(error_key, 0) + 1
                
                self.logger.error(f"Error in {context.method}: {type(error).__name__}: {error}")
                raise
    

To use the full versions with advanced features:

Copy

    from fastmcp.server.middleware.error_handling import (
        ErrorHandlingMiddleware, 
        RetryMiddleware
    )
    
    # Comprehensive error logging and transformation
    mcp.add_middleware(ErrorHandlingMiddleware(
        include_traceback=True,
        transform_errors=True,
        error_callback=my_error_callback
    ))
    
    # Automatic retry with exponential backoff
    mcp.add_middleware(RetryMiddleware(
        max_retries=3,
        retry_exceptions=(ConnectionError, TimeoutError)
    ))
    

The built-in versions include error transformation, custom callbacks, configurable retry logic, and proper MCP error formatting.

### 

[​](https://gofastmcp.com/servers/middleware#combining-middleware)

Combining Middleware

These middleware work together seamlessly:

Copy

    from fastmcp import FastMCP
    from fastmcp.server.middleware.timing import TimingMiddleware
    from fastmcp.server.middleware.logging import LoggingMiddleware
    from fastmcp.server.middleware.rate_limiting import RateLimitingMiddleware
    from fastmcp.server.middleware.error_handling import ErrorHandlingMiddleware
    
    mcp = FastMCP("Production Server")
    
    # Add middleware in logical order
    mcp.add_middleware(ErrorHandlingMiddleware())  # Handle errors first
    mcp.add_middleware(RateLimitingMiddleware(max_requests_per_second=50))
    mcp.add_middleware(TimingMiddleware())  # Time actual execution
    mcp.add_middleware(LoggingMiddleware())  # Log everything
    
    @mcp.tool
    def my_tool(data: str) -> str:
        return f"Processed: {data}"
    

This configuration provides comprehensive monitoring, protection, and observability for your MCP server.

### 

[​](https://gofastmcp.com/servers/middleware#custom-middleware-example)

Custom Middleware Example

You can also create custom middleware by extending the base class:

Copy

    from fastmcp.server.middleware import Middleware, MiddlewareContext
    
    class CustomHeaderMiddleware(Middleware):
        async def on_request(self, context: MiddlewareContext, call_next):
            # Add custom logic here
            print(f"Processing {context.method}")
            
            result = await call_next(context)
            
            print(f"Completed {context.method}")
            return result
    
    mcp.add_middleware(CustomHeaderMiddleware())
    

[Client Logging\
\
Previous](https://gofastmcp.com/servers/logging)
[Progress Reporting\
\
Next](https://gofastmcp.com/servers/progress)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.