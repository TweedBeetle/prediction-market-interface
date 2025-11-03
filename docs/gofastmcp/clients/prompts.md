---
url: https://gofastmcp.com/clients/prompts
title: Prompts - FastMCP
description: Use server-side prompt templates with automatic argument serialization.
scraped_at: 2025-11-03T18:41:58.406914
---

[Skip to main content](https://gofastmcp.com/clients/prompts#content-area)

Join the [FastMCP community](https://discord.gg/uu8dJCgttd)
!

[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)

Search...

Navigation

Core Operations

Prompts

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

*   [Listing Prompts](https://gofastmcp.com/clients/prompts#listing-prompts)
    
*   [Filtering by Tags](https://gofastmcp.com/clients/prompts#filtering-by-tags)
    
*   [Using Prompts](https://gofastmcp.com/clients/prompts#using-prompts)
    
*   [Basic Usage](https://gofastmcp.com/clients/prompts#basic-usage)
    
*   [Prompts with Arguments](https://gofastmcp.com/clients/prompts#prompts-with-arguments)
    
*   [Automatic Argument Serialization](https://gofastmcp.com/clients/prompts#automatic-argument-serialization)
    
*   [Serialization Examples](https://gofastmcp.com/clients/prompts#serialization-examples)
    
*   [Working with Prompt Results](https://gofastmcp.com/clients/prompts#working-with-prompt-results)
    
*   [Raw MCP Protocol Access](https://gofastmcp.com/clients/prompts#raw-mcp-protocol-access)
    
*   [Multi-Server Clients](https://gofastmcp.com/clients/prompts#multi-server-clients)
    
*   [Common Prompt Patterns](https://gofastmcp.com/clients/prompts#common-prompt-patterns)
    
*   [System Messages](https://gofastmcp.com/clients/prompts#system-messages)
    
*   [Conversation Templates](https://gofastmcp.com/clients/prompts#conversation-templates)
    

`` New in version: `2.0.0` `` Prompts are reusable message templates exposed by MCP servers. They can accept arguments to generate personalized message sequences for LLM interactions.

[​](https://gofastmcp.com/clients/prompts#listing-prompts)

Listing Prompts
-----------------------------------------------------------------------------

Use `list_prompts()` to retrieve all available prompt templates:

Copy

    async with client:
        prompts = await client.list_prompts()
        # prompts -> list[mcp.types.Prompt]
        
        for prompt in prompts:
            print(f"Prompt: {prompt.name}")
            print(f"Description: {prompt.description}")
            if prompt.arguments:
                print(f"Arguments: {[arg.name for arg in prompt.arguments]}")
            # Access tags and other metadata
            if hasattr(prompt, '_meta') and prompt._meta:
                fastmcp_meta = prompt._meta.get('_fastmcp', {})
                print(f"Tags: {fastmcp_meta.get('tags', [])}")
    

### 

[​](https://gofastmcp.com/clients/prompts#filtering-by-tags)

Filtering by Tags

`` New in version: `2.11.0` `` You can use the `meta` field to filter prompts based on their tags:

Copy

    async with client:
        prompts = await client.list_prompts()
        
        # Filter prompts by tag
        analysis_prompts = [\
            prompt for prompt in prompts \
            if hasattr(prompt, '_meta') and prompt._meta and\
               prompt._meta.get('_fastmcp', {}) and\
               'analysis' in prompt._meta.get('_fastmcp', {}).get('tags', [])\
        ]
        
        print(f"Found {len(analysis_prompts)} analysis prompts")
    

The `_meta` field is part of the standard MCP specification. FastMCP servers include tags and other metadata within a `_fastmcp` namespace (e.g., `_meta._fastmcp.tags`) to avoid conflicts with user-defined metadata. This behavior can be controlled with the server’s `include_fastmcp_meta` setting - when disabled, the `_fastmcp` namespace won’t be included. Other MCP server implementations may not provide this metadata structure.

[​](https://gofastmcp.com/clients/prompts#using-prompts)

Using Prompts
-------------------------------------------------------------------------

### 

[​](https://gofastmcp.com/clients/prompts#basic-usage)

Basic Usage

Request a rendered prompt using `get_prompt()` with the prompt name and arguments:

Copy

    async with client:
        # Simple prompt without arguments
        result = await client.get_prompt("welcome_message")
        # result -> mcp.types.GetPromptResult
        
        # Access the generated messages
        for message in result.messages:
            print(f"Role: {message.role}")
            print(f"Content: {message.content}")
    

### 

[​](https://gofastmcp.com/clients/prompts#prompts-with-arguments)

Prompts with Arguments

Pass arguments as a dictionary to customize the prompt:

Copy

    async with client:
        # Prompt with simple arguments
        result = await client.get_prompt("user_greeting", {
            "name": "Alice",
            "role": "administrator"
        })
        
        # Access the personalized messages
        for message in result.messages:
            print(f"Generated message: {message.content}")
    

[​](https://gofastmcp.com/clients/prompts#automatic-argument-serialization)

Automatic Argument Serialization
---------------------------------------------------------------------------------------------------------------

`` New in version: `2.9.0` `` FastMCP automatically serializes complex arguments to JSON strings as required by the MCP specification. This allows you to pass typed objects directly:

Copy

    from dataclasses import dataclass
    
    @dataclass
    class UserData:
        name: str
        age: int
    
    async with client:
        # Complex arguments are automatically serialized
        result = await client.get_prompt("analyze_user", {
            "user": UserData(name="Alice", age=30),     # Automatically serialized to JSON
            "preferences": {"theme": "dark"},           # Dict serialized to JSON string
            "scores": [85, 92, 78],                     # List serialized to JSON string
            "simple_name": "Bob"                        # Strings passed through unchanged
        })
    

The client handles serialization using `pydantic_core.to_json()` for consistent formatting. FastMCP servers can automatically deserialize these JSON strings back to the expected types.

### 

[​](https://gofastmcp.com/clients/prompts#serialization-examples)

Serialization Examples

Copy

    async with client:
        result = await client.get_prompt("data_analysis", {
            # These will be automatically serialized to JSON strings:
            "config": {
                "format": "csv",
                "include_headers": True,
                "delimiter": ","
            },
            "filters": [\
                {"field": "age", "operator": ">", "value": 18},\
                {"field": "status", "operator": "==", "value": "active"}\
            ],
            # This remains a string:
            "report_title": "Monthly Analytics Report"
        })
    

[​](https://gofastmcp.com/clients/prompts#working-with-prompt-results)

Working with Prompt Results
-----------------------------------------------------------------------------------------------------

The `get_prompt()` method returns a `GetPromptResult` object containing a list of messages:

Copy

    async with client:
        result = await client.get_prompt("conversation_starter", {"topic": "climate"})
        
        # Access individual messages
        for i, message in enumerate(result.messages):
            print(f"Message {i + 1}:")
            print(f"  Role: {message.role}")
            print(f"  Content: {message.content.text if hasattr(message.content, 'text') else message.content}")
    

[​](https://gofastmcp.com/clients/prompts#raw-mcp-protocol-access)

Raw MCP Protocol Access
---------------------------------------------------------------------------------------------

For access to the complete MCP protocol objects, use the `*_mcp` methods:

Copy

    async with client:
        # Raw MCP method returns full protocol object
        prompts_result = await client.list_prompts_mcp()
        # prompts_result -> mcp.types.ListPromptsResult
        
        prompt_result = await client.get_prompt_mcp("example_prompt", {"arg": "value"})
        # prompt_result -> mcp.types.GetPromptResult
    

[​](https://gofastmcp.com/clients/prompts#multi-server-clients)

Multi-Server Clients
---------------------------------------------------------------------------------------

When using multi-server clients, prompts are accessible without prefixing (unlike tools):

Copy

    async with client:  # Multi-server client
        # Prompts from any server are directly accessible
        result1 = await client.get_prompt("weather_prompt", {"city": "London"})
        result2 = await client.get_prompt("assistant_prompt", {"query": "help"})
    

[​](https://gofastmcp.com/clients/prompts#common-prompt-patterns)

Common Prompt Patterns
-------------------------------------------------------------------------------------------

### 

[​](https://gofastmcp.com/clients/prompts#system-messages)

System Messages

Many prompts generate system messages for LLM configuration:

Copy

    async with client:
        result = await client.get_prompt("system_configuration", {
            "role": "helpful assistant",
            "expertise": "python programming"
        })
        
        # Typically returns messages with role="system"
        system_message = result.messages[0]
        print(f"System prompt: {system_message.content}")
    

### 

[​](https://gofastmcp.com/clients/prompts#conversation-templates)

Conversation Templates

Prompts can generate multi-turn conversation templates:

Copy

    async with client:
        result = await client.get_prompt("interview_template", {
            "candidate_name": "Alice",
            "position": "Senior Developer"
        })
        
        # Multiple messages for a conversation flow
        for message in result.messages:
            print(f"{message.role}: {message.content}")
    

Prompt arguments and their expected types depend on the specific prompt implementation. Check the server’s documentation or use `list_prompts()` to see available arguments for each prompt.

[Resource Operations\
\
Previous](https://gofastmcp.com/clients/resources)
[User Elicitation\
\
Next](https://gofastmcp.com/clients/elicitation)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.