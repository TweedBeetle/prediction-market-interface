---
url: https://gofastmcp.com/clients/sampling
title: LLM Sampling - FastMCP
description: Handle server-initiated LLM sampling requests.
scraped_at: 2025-11-03T18:42:02.701143
---

[Skip to main content](https://gofastmcp.com/clients/sampling#content-area)

Join the [FastMCP community](https://discord.gg/uu8dJCgttd)
!

[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)

Search...

Navigation

Advanced Features

LLM Sampling

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
    
    *   [Elicitation](https://gofastmcp.com/clients/elicitation)
        
    *   [Logging](https://gofastmcp.com/clients/logging)
        
    *   [Progress](https://gofastmcp.com/clients/progress)
        
    *   [Sampling](https://gofastmcp.com/clients/sampling)
        
    *   [Messages](https://gofastmcp.com/clients/messages)
        
    *   [Roots](https://gofastmcp.com/clients/roots)
        
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

*   [Sampling Handler](https://gofastmcp.com/clients/sampling#sampling-handler)
    
*   [Handler Parameters](https://gofastmcp.com/clients/sampling#handler-parameters)
    
*   [Basic Example](https://gofastmcp.com/clients/sampling#basic-example)
    

`` New in version: `2.0.0` `` MCP servers can request LLM completions from clients. The client handles these requests through a sampling handler callback.

[​](https://gofastmcp.com/clients/sampling#sampling-handler)

Sampling Handler
--------------------------------------------------------------------------------

Provide a `sampling_handler` function when creating the client:

Copy

    from fastmcp import Client
    from fastmcp.client.sampling import (
        SamplingMessage,
        SamplingParams,
        RequestContext,
    )
    
    async def sampling_handler(
        messages: list[SamplingMessage],
        params: SamplingParams,
        context: RequestContext
    ) -> str:
        # Your LLM integration logic here
        # Extract text from messages and generate a response
        return "Generated response based on the messages"
    
    client = Client(
        "my_mcp_server.py",
        sampling_handler=sampling_handler,
    )
    

### 

[​](https://gofastmcp.com/clients/sampling#handler-parameters)

Handler Parameters

The sampling handler receives three parameters:

Sampling Handler Parameters
---------------------------

[​](https://gofastmcp.com/clients/sampling#param-sampling-message)

SamplingMessage

Sampling Message Object

Show attributes

[​](https://gofastmcp.com/clients/sampling#param-role)

role

Literal\["user", "assistant"\]

The role of the message.

[​](https://gofastmcp.com/clients/sampling#param-content)

content

TextContent | ImageContent | AudioContent

The content of the message.TextContent is most common, and has a `.text` attribute.

[​](https://gofastmcp.com/clients/sampling#param-sampling-params)

SamplingParams

Sampling Parameters Object

Show attributes

[​](https://gofastmcp.com/clients/sampling#param-messages)

messages

list\[SamplingMessage\]

The messages to sample from

[​](https://gofastmcp.com/clients/sampling#param-model-preferences)

modelPreferences

ModelPreferences | None

The server’s preferences for which model to select. The client MAY ignore these preferences.

Show attributes

[​](https://gofastmcp.com/clients/sampling#param-hints)

hints

list\[ModelHint\] | None

The hints to use for model selection.

[​](https://gofastmcp.com/clients/sampling#param-cost-priority)

costPriority

float | None

The cost priority for model selection.

[​](https://gofastmcp.com/clients/sampling#param-speed-priority)

speedPriority

float | None

The speed priority for model selection.

[​](https://gofastmcp.com/clients/sampling#param-intelligence-priority)

intelligencePriority

float | None

The intelligence priority for model selection.

[​](https://gofastmcp.com/clients/sampling#param-system-prompt)

systemPrompt

str | None

An optional system prompt the server wants to use for sampling.

[​](https://gofastmcp.com/clients/sampling#param-include-context)

includeContext

IncludeContext | None

A request to include context from one or more MCP servers (including the caller), to be attached to the prompt.

[​](https://gofastmcp.com/clients/sampling#param-temperature)

temperature

float | None

The sampling temperature.

[​](https://gofastmcp.com/clients/sampling#param-max-tokens)

maxTokens

int

The maximum number of tokens to sample.

[​](https://gofastmcp.com/clients/sampling#param-stop-sequences)

stopSequences

list\[str\] | None

The stop sequences to use for sampling.

[​](https://gofastmcp.com/clients/sampling#param-metadata)

metadata

dict\[str, Any\] | None

Optional metadata to pass through to the LLM provider.

[​](https://gofastmcp.com/clients/sampling#param-request-context)

RequestContext

Request Context Object

Show attributes

[​](https://gofastmcp.com/clients/sampling#param-request-id)

request\_id

RequestId

Unique identifier for the MCP request

[​](https://gofastmcp.com/clients/sampling#basic-example)

Basic Example
--------------------------------------------------------------------------

Copy

    from fastmcp import Client
    from fastmcp.client.sampling import SamplingMessage, SamplingParams, RequestContext
    
    async def basic_sampling_handler(
        messages: list[SamplingMessage],
        params: SamplingParams,
        context: RequestContext
    ) -> str:
        # Extract message content
        conversation = []
        for message in messages:
            content = message.content.text if hasattr(message.content, 'text') else str(message.content)
            conversation.append(f"{message.role}: {content}")
    
        # Use the system prompt if provided
        system_prompt = params.systemPrompt or "You are a helpful assistant."
    
        # Here you would integrate with your preferred LLM service
        # This is just a placeholder response
        return f"Response based on conversation: {' | '.join(conversation)}"
    
    client = Client(
        "my_mcp_server.py",
        sampling_handler=basic_sampling_handler
    )
    

If the client doesn’t provide a sampling handler, servers can optionally configure a fallback handler. See [Server Sampling](https://gofastmcp.com/servers/sampling#sampling-fallback-handler)
 for details.

[Progress Monitoring\
\
Previous](https://gofastmcp.com/clients/progress)
[Message Handling\
\
Next](https://gofastmcp.com/clients/messages)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.