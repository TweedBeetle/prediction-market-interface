---
url: https://gofastmcp.com/servers/logging
title: Client Logging - FastMCP
description: Send log messages back to MCP clients through the context.
scraped_at: 2025-11-03T18:43:18.028558
---

[Skip to main content](https://gofastmcp.com/servers/logging#content-area)

Join the [FastMCP community](https://discord.gg/uu8dJCgttd)
!

[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)

Search...

Navigation

Advanced Features

Client Logging

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

*   [Why Use Server Logging?](https://gofastmcp.com/servers/logging#why-use-server-logging%3F)
    
*   [Basic Usage](https://gofastmcp.com/servers/logging#basic-usage)
    
*   [Structured Logging with extra](https://gofastmcp.com/servers/logging#structured-logging-with-extra)
    
*   [Server Logs](https://gofastmcp.com/servers/logging#server-logs)
    
*   [Logging Methods](https://gofastmcp.com/servers/logging#logging-methods)
    
*   [Log Levels](https://gofastmcp.com/servers/logging#log-levels)
    
*   [Debug](https://gofastmcp.com/servers/logging#debug)
    
*   [Info](https://gofastmcp.com/servers/logging#info)
    
*   [Warning](https://gofastmcp.com/servers/logging#warning)
    
*   [Error](https://gofastmcp.com/servers/logging#error)
    
*   [Client Handling](https://gofastmcp.com/servers/logging#client-handling)
    

This documentation covers **MCP client logging** - sending messages from your server to MCP clients. For standard server-side logging (e.g., writing to files, console), use `fastmcp.utilities.logging.get_logger()` or Python’s built-in `logging` module.

Server logging allows MCP tools to send debug, info, warning, and error messages back to the client. This provides visibility into function execution and helps with debugging during development and operation.

[​](https://gofastmcp.com/servers/logging#why-use-server-logging%3F)

Why Use Server Logging?
-----------------------------------------------------------------------------------------------

Server logging is essential for:

*   **Debugging**: Send detailed execution information to help diagnose issues
*   **Progress visibility**: Keep users informed about what the tool is doing
*   **Error reporting**: Communicate problems and their context to clients
*   **Audit trails**: Create records of tool execution for compliance or analysis

Unlike standard Python logging, MCP server logging sends messages directly to the client, making them visible in the client’s interface or logs.

### 

[​](https://gofastmcp.com/servers/logging#basic-usage)

Basic Usage

Use the context logging methods within any tool function:

Copy

    from fastmcp import FastMCP, Context
    
    mcp = FastMCP("LoggingDemo")
    
    @mcp.tool
    async def analyze_data(data: list[float], ctx: Context) -> dict:
        """Analyze numerical data with comprehensive logging."""
        await ctx.debug("Starting analysis of numerical data")
        await ctx.info(f"Analyzing {len(data)} data points")
        
        try:
            if not data:
                await ctx.warning("Empty data list provided")
                return {"error": "Empty data list"}
            
            result = sum(data) / len(data)
            await ctx.info(f"Analysis complete, average: {result}")
            return {"average": result, "count": len(data)}
            
        except Exception as e:
            await ctx.error(f"Analysis failed: {str(e)}")
            raise
    

[​](https://gofastmcp.com/servers/logging#structured-logging-with-extra)

Structured Logging with `extra`
-----------------------------------------------------------------------------------------------------------

All logging methods (`debug`, `info`, `warning`, `error`, `log`) now accept an `extra` parameter, which is a dictionary of arbitrary data. This allows you to send structured data to the client, which is useful for creating rich, queryable logs.

Copy

    @mcp.tool
    async def process_transaction(transaction_id: str, amount: float, ctx: Context):
        await ctx.info(
            f"Processing transaction {transaction_id}",
            extra={
                "transaction_id": transaction_id,
                "amount": amount,
                "currency": "USD"
            }
        )
        # ... processing logic ...
    

[​](https://gofastmcp.com/servers/logging#server-logs)

Server Logs
---------------------------------------------------------------------

Client Logging in the form of `ctx.log()` and its convenience methods (`debug`, `info`, `warning`, `error`) are meant for sending messages to the MCP clients. Messages sent to clients are also logged to the server’s log at `DEBUG` level. Enable debug logging on the server or enable debug logging on the `fastmcp.server.context.to_client` logger to see these messages in the server’s log.

Copy

    import logging
    
    from fastmcp.utilities.logging import get_logger
    
    to_client_logger = get_logger(name="fastmcp.server.context.to_client")
    to_client_logger.setLevel(level=logging.DEBUG)
    

[​](https://gofastmcp.com/servers/logging#logging-methods)

Logging Methods
-----------------------------------------------------------------------------

Context Logging Methods
-----------------------

[​](https://gofastmcp.com/servers/logging#param-ctx-debug)

ctx.debug

async method

Send debug-level messages for detailed execution information

Show parameters

[​](https://gofastmcp.com/servers/logging#param-message)

message

str

The debug message to send to the client

[​](https://gofastmcp.com/servers/logging#param-extra)

extra

dict | None

default:"None"

Optional dictionary for structured logging data

[​](https://gofastmcp.com/servers/logging#param-ctx-info)

ctx.info

async method

Send informational messages about normal execution

Show parameters

[​](https://gofastmcp.com/servers/logging#param-message-1)

message

str

The information message to send to the client

[​](https://gofastmcp.com/servers/logging#param-extra-1)

extra

dict | None

default:"None"

Optional dictionary for structured logging data

[​](https://gofastmcp.com/servers/logging#param-ctx-warning)

ctx.warning

async method

Send warning messages for potential issues that didn’t prevent execution

Show parameters

[​](https://gofastmcp.com/servers/logging#param-message-2)

message

str

The warning message to send to the client

[​](https://gofastmcp.com/servers/logging#param-extra-2)

extra

dict | None

default:"None"

Optional dictionary for structured logging data

[​](https://gofastmcp.com/servers/logging#param-ctx-error)

ctx.error

async method

Send error messages for problems that occurred during execution

Show parameters

[​](https://gofastmcp.com/servers/logging#param-message-3)

message

str

The error message to send to the client

[​](https://gofastmcp.com/servers/logging#param-extra-3)

extra

dict | None

default:"None"

Optional dictionary for structured logging data

[​](https://gofastmcp.com/servers/logging#param-ctx-log)

ctx.log

async method

Generic logging method with custom level and logger name

Show parameters

[​](https://gofastmcp.com/servers/logging#param-level)

level

Literal\['debug', 'info', 'warning', 'error'\]

The log level for the message

[​](https://gofastmcp.com/servers/logging#param-message-4)

message

str

The message to send to the client

[​](https://gofastmcp.com/servers/logging#param-logger-name)

logger\_name

str | None

default:"None"

Optional custom logger name for categorizing messages

[​](https://gofastmcp.com/servers/logging#param-extra-4)

extra

dict | None

default:"None"

Optional dictionary for structured logging data

[​](https://gofastmcp.com/servers/logging#log-levels)

Log Levels
-------------------------------------------------------------------

### 

[​](https://gofastmcp.com/servers/logging#debug)

Debug

Use for detailed information that’s typically only useful when diagnosing problems:

Copy

    @mcp.tool
    async def process_file(file_path: str, ctx: Context) -> str:
        """Process a file with detailed debug logging."""
        await ctx.debug(f"Starting to process file: {file_path}")
        await ctx.debug("Checking file permissions")
        
        # File processing logic
        await ctx.debug("File processing completed successfully")
        return "File processed"
    

### 

[​](https://gofastmcp.com/servers/logging#info)

Info

Use for general information about normal program execution:

Copy

    @mcp.tool
    async def backup_database(ctx: Context) -> str:
        """Backup database with progress information."""
        await ctx.info("Starting database backup")
        await ctx.info("Connecting to database")
        await ctx.info("Backup completed successfully")
        return "Database backed up"
    

### 

[​](https://gofastmcp.com/servers/logging#warning)

Warning

Use for potentially harmful situations that don’t prevent execution:

Copy

    @mcp.tool
    async def validate_config(config: dict, ctx: Context) -> dict:
        """Validate configuration with warnings for deprecated options."""
        if "old_api_key" in config:
            await ctx.warning(
                "Using deprecated 'old_api_key' field. Please use 'api_key' instead",
                extra={"deprecated_field": "old_api_key"}
            )
        
        if config.get("timeout", 30) > 300:
            await ctx.warning(
                "Timeout value is very high (>5 minutes), this may cause issues",
                extra={"timeout_value": config.get("timeout")}
            )
        
        return {"status": "valid", "warnings": "see logs"}
    

### 

[​](https://gofastmcp.com/servers/logging#error)

Error

Use for error events that might still allow the application to continue:

Copy

    @mcp.tool
    async def batch_process(items: list[str], ctx: Context) -> dict:
        """Process multiple items, logging errors for failed items."""
        successful = 0
        failed = 0
        
        for item in items:
            try:
                # Process item
                successful += 1
            except Exception as e:
                await ctx.error(
                    f"Failed to process item '{item}': {str(e)}",
                    extra={"failed_item": item}
                )
                failed += 1
        
        return {"successful": successful, "failed": failed}
    

[​](https://gofastmcp.com/servers/logging#client-handling)

Client Handling
-----------------------------------------------------------------------------

Log messages are sent to the client through the MCP protocol. How clients handle these messages depends on their implementation:

*   **Development clients**: May display logs in real-time for debugging
*   **Production clients**: May store logs for later analysis or display to users
*   **Integration clients**: May forward logs to external logging systems

See [Client Logging](https://gofastmcp.com/clients/logging)
 for details on how clients can handle server log messages.

[Icons\
\
Previous](https://gofastmcp.com/servers/icons)
[MCP Middleware\
\
Next](https://gofastmcp.com/servers/middleware)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.