---
url: https://gofastmcp.com/servers/progress
title: Progress Reporting - FastMCP
description: Update clients on the progress of long-running operations through the MCP context.
scraped_at: 2025-11-03T18:43:18.029720
---

[Skip to main content](https://gofastmcp.com/servers/progress#content-area)

Join the [FastMCP community](https://discord.gg/uu8dJCgttd)
!

[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)

Search...

Navigation

Advanced Features

Progress Reporting

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

*   [Why Use Progress Reporting?](https://gofastmcp.com/servers/progress#why-use-progress-reporting%3F)
    
*   [Basic Usage](https://gofastmcp.com/servers/progress#basic-usage)
    
*   [Method Signature](https://gofastmcp.com/servers/progress#method-signature)
    
*   [Progress Patterns](https://gofastmcp.com/servers/progress#progress-patterns)
    
*   [Percentage-Based Progress](https://gofastmcp.com/servers/progress#percentage-based-progress)
    
*   [Absolute Progress](https://gofastmcp.com/servers/progress#absolute-progress)
    
*   [Indeterminate Progress](https://gofastmcp.com/servers/progress#indeterminate-progress)
    
*   [Multi-Stage Operations](https://gofastmcp.com/servers/progress#multi-stage-operations)
    
*   [Client Requirements](https://gofastmcp.com/servers/progress#client-requirements)
    

Progress reporting allows MCP tools to notify clients about the progress of long-running operations. This enables clients to display progress indicators and provide better user experience during time-consuming tasks.

[​](https://gofastmcp.com/servers/progress#why-use-progress-reporting%3F)

Why Use Progress Reporting?
--------------------------------------------------------------------------------------------------------

Progress reporting is valuable for:

*   **User experience**: Keep users informed about long-running operations
*   **Progress indicators**: Enable clients to show progress bars or percentages
*   **Timeout prevention**: Demonstrate that operations are actively progressing
*   **Debugging**: Track execution progress for performance analysis

### 

[​](https://gofastmcp.com/servers/progress#basic-usage)

Basic Usage

Use `ctx.report_progress()` to send progress updates to the client:

Copy

    from fastmcp import FastMCP, Context
    import asyncio
    
    mcp = FastMCP("ProgressDemo")
    
    @mcp.tool
    async def process_items(items: list[str], ctx: Context) -> dict:
        """Process a list of items with progress updates."""
        total = len(items)
        results = []
        
        for i, item in enumerate(items):
            # Report progress as we process each item
            await ctx.report_progress(progress=i, total=total)
            
            # Simulate processing time
            await asyncio.sleep(0.1)
            results.append(item.upper())
        
        # Report 100% completion
        await ctx.report_progress(progress=total, total=total)
        
        return {"processed": len(results), "results": results}
    

[​](https://gofastmcp.com/servers/progress#method-signature)

Method Signature
--------------------------------------------------------------------------------

Context Progress Method
-----------------------

[​](https://gofastmcp.com/servers/progress#param-ctx-report-progress)

ctx.report\_progress

async method

Report progress to the client for long-running operations

Show Parameters

[​](https://gofastmcp.com/servers/progress#param-progress)

progress

float

Current progress value (e.g., 24, 0.75, 1500)

[​](https://gofastmcp.com/servers/progress#param-total)

total

float | None

default:"None"

Optional total value (e.g., 100, 1.0, 2000). When provided, clients may interpret this as enabling percentage calculation.

[​](https://gofastmcp.com/servers/progress#progress-patterns)

Progress Patterns
----------------------------------------------------------------------------------

### 

[​](https://gofastmcp.com/servers/progress#percentage-based-progress)

Percentage-Based Progress

Report progress as a percentage (0-100):

Copy

    @mcp.tool
    async def download_file(url: str, ctx: Context) -> str:
        """Download a file with percentage progress."""
        total_size = 1000  # KB
        downloaded = 0
        
        while downloaded < total_size:
            # Download chunk
            chunk_size = min(50, total_size - downloaded)
            downloaded += chunk_size
            
            # Report percentage progress
            percentage = (downloaded / total_size) * 100
            await ctx.report_progress(progress=percentage, total=100)
            
            await asyncio.sleep(0.1)  # Simulate download time
        
        return f"Downloaded file from {url}"
    

### 

[​](https://gofastmcp.com/servers/progress#absolute-progress)

Absolute Progress

Report progress with absolute values:

Copy

    @mcp.tool
    async def backup_database(ctx: Context) -> str:
        """Backup database tables with absolute progress."""
        tables = ["users", "orders", "products", "inventory", "logs"]
        
        for i, table in enumerate(tables):
            await ctx.info(f"Backing up table: {table}")
            
            # Report absolute progress
            await ctx.report_progress(progress=i + 1, total=len(tables))
            
            # Simulate backup time
            await asyncio.sleep(0.5)
        
        return "Database backup completed"
    

### 

[​](https://gofastmcp.com/servers/progress#indeterminate-progress)

Indeterminate Progress

Report progress without a known total for operations where the endpoint is unknown:

Copy

    @mcp.tool
    async def scan_directory(directory: str, ctx: Context) -> dict:
        """Scan directory with indeterminate progress."""
        files_found = 0
        
        # Simulate directory scanning
        for i in range(10):  # Unknown number of files
            files_found += 1
            
            # Report progress without total for indeterminate operations
            await ctx.report_progress(progress=files_found)
            
            await asyncio.sleep(0.2)
        
        return {"files_found": files_found, "directory": directory}
    

### 

[​](https://gofastmcp.com/servers/progress#multi-stage-operations)

Multi-Stage Operations

Break complex operations into stages with progress for each:

Copy

    @mcp.tool
    async def data_migration(source: str, destination: str, ctx: Context) -> str:
        """Migrate data with multi-stage progress reporting."""
        
        # Stage 1: Validation (0-25%)
        await ctx.info("Validating source data")
        for i in range(5):
            await ctx.report_progress(progress=i * 5, total=100)
            await asyncio.sleep(0.1)
        
        # Stage 2: Export (25-60%)
        await ctx.info("Exporting data from source")
        for i in range(7):
            progress = 25 + (i * 5)
            await ctx.report_progress(progress=progress, total=100)
            await asyncio.sleep(0.1)
        
        # Stage 3: Transform (60-80%)
        await ctx.info("Transforming data format")
        for i in range(4):
            progress = 60 + (i * 5)
            await ctx.report_progress(progress=progress, total=100)
            await asyncio.sleep(0.1)
        
        # Stage 4: Import (80-100%)
        await ctx.info("Importing to destination")
        for i in range(4):
            progress = 80 + (i * 5)
            await ctx.report_progress(progress=progress, total=100)
            await asyncio.sleep(0.1)
        
        # Final completion
        await ctx.report_progress(progress=100, total=100)
        
        return f"Migration from {source} to {destination} completed"
    

[​](https://gofastmcp.com/servers/progress#client-requirements)

Client Requirements
--------------------------------------------------------------------------------------

Progress reporting requires clients to support progress handling:

*   Clients must send a `progressToken` in the initial request to receive progress updates
*   If no progress token is provided, progress calls will have no effect (they won’t error)
*   See [Client Progress](https://gofastmcp.com/clients/progress)
     for details on implementing client-side progress handling

[MCP Middleware\
\
Previous](https://gofastmcp.com/servers/middleware)
[Proxy Servers\
\
Next](https://gofastmcp.com/servers/proxy)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.