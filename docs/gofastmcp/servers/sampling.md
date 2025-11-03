---
url: https://gofastmcp.com/servers/sampling
title: LLM Sampling - FastMCP
description: Request LLM text generation from the client or a configured provider through the MCP context.
scraped_at: 2025-11-03T18:43:22.579436
---

[Skip to main content](https://gofastmcp.com/servers/sampling#content-area)

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

*   [Why Use LLM Sampling?](https://gofastmcp.com/servers/sampling#why-use-llm-sampling%3F)
    
*   [Basic Usage](https://gofastmcp.com/servers/sampling#basic-usage)
    
*   [Method Signature](https://gofastmcp.com/servers/sampling#method-signature)
    
*   [Simple Text Generation](https://gofastmcp.com/servers/sampling#simple-text-generation)
    
*   [Basic Prompting](https://gofastmcp.com/servers/sampling#basic-prompting)
    
*   [System Prompt](https://gofastmcp.com/servers/sampling#system-prompt)
    
*   [Model Preferences](https://gofastmcp.com/servers/sampling#model-preferences)
    
*   [Complex Message Structures](https://gofastmcp.com/servers/sampling#complex-message-structures)
    
*   [Sampling Fallback Handler](https://gofastmcp.com/servers/sampling#sampling-fallback-handler)
    
*   [Fallback Mode (Default)](https://gofastmcp.com/servers/sampling#fallback-mode-default)
    
*   [Always Mode](https://gofastmcp.com/servers/sampling#always-mode)
    
*   [Client Requirements](https://gofastmcp.com/servers/sampling#client-requirements)
    

`` New in version: `2.0.0` `` LLM sampling allows MCP tools to request LLM text generation based on provided messages. By default, sampling requests are sent to the client’s LLM, but you can also configure a fallback handler or always use a specific LLM provider. This is useful when tools need to leverage LLM capabilities to process data, generate responses, or perform text-based analysis.

[​](https://gofastmcp.com/servers/sampling#why-use-llm-sampling%3F)

Why Use LLM Sampling?
--------------------------------------------------------------------------------------------

LLM sampling enables tools to:

*   **Leverage AI capabilities**: Use the client’s LLM for text generation and analysis
*   **Offload complex reasoning**: Let the LLM handle tasks requiring natural language understanding
*   **Generate dynamic content**: Create responses, summaries, or transformations based on data
*   **Maintain context**: Use the same LLM instance that the user is already interacting with

### 

[​](https://gofastmcp.com/servers/sampling#basic-usage)

Basic Usage

Use `ctx.sample()` to request text generation from the client’s LLM:

Copy

    from fastmcp import FastMCP, Context
    
    mcp = FastMCP("SamplingDemo")
    
    @mcp.tool
    async def analyze_sentiment(text: str, ctx: Context) -> dict:
        """Analyze the sentiment of text using the client's LLM."""
        prompt = f"""Analyze the sentiment of the following text as positive, negative, or neutral. 
        Just output a single word - 'positive', 'negative', or 'neutral'.
        
        Text to analyze: {text}"""
        
        # Request LLM analysis
        response = await ctx.sample(prompt)
        
        # Process the LLM's response
        sentiment = response.text.strip().lower()
        
        # Map to standard sentiment values
        if "positive" in sentiment:
            sentiment = "positive"
        elif "negative" in sentiment:
            sentiment = "negative"
        else:
            sentiment = "neutral"
        
        return {"text": text, "sentiment": sentiment}
    

[​](https://gofastmcp.com/servers/sampling#method-signature)

Method Signature
--------------------------------------------------------------------------------

Context Sampling Method
-----------------------

[​](https://gofastmcp.com/servers/sampling#param-ctx-sample)

ctx.sample

async method

Request text generation from the client’s LLM

Show Parameters

[​](https://gofastmcp.com/servers/sampling#param-messages)

messages

str | list\[str | SamplingMessage\]

A string or list of strings/message objects to send to the LLM

[​](https://gofastmcp.com/servers/sampling#param-system-prompt)

system\_prompt

str | None

default:"None"

Optional system prompt to guide the LLM’s behavior

[​](https://gofastmcp.com/servers/sampling#param-temperature)

temperature

float | None

default:"None"

Optional sampling temperature (controls randomness, typically 0.0-1.0)

[​](https://gofastmcp.com/servers/sampling#param-max-tokens)

max\_tokens

int | None

default:"512"

Optional maximum number of tokens to generate

[​](https://gofastmcp.com/servers/sampling#param-model-preferences)

model\_preferences

ModelPreferences | str | list\[str\] | None

default:"None"

Optional model selection preferences (e.g., model hint string, list of hints, or ModelPreferences object)

Show Response

[​](https://gofastmcp.com/servers/sampling#param-response)

response

TextContent | ImageContent

The LLM’s response content (typically TextContent with a .text attribute)

[​](https://gofastmcp.com/servers/sampling#simple-text-generation)

Simple Text Generation
--------------------------------------------------------------------------------------------

### 

[​](https://gofastmcp.com/servers/sampling#basic-prompting)

Basic Prompting

Generate text with simple string prompts:

Copy

    @mcp.tool
    async def generate_summary(content: str, ctx: Context) -> str:
        """Generate a summary of the provided content."""
        prompt = f"Please provide a concise summary of the following content:\n\n{content}"
        
        response = await ctx.sample(prompt)
        return response.text
    

### 

[​](https://gofastmcp.com/servers/sampling#system-prompt)

System Prompt

Use system prompts to guide the LLM’s behavior:

Copy

    @mcp.tool
    async def generate_code_example(concept: str, ctx: Context) -> str:
        """Generate a Python code example for a given concept."""
        response = await ctx.sample(
            messages=f"Write a simple Python code example demonstrating '{concept}'.",
            system_prompt="You are an expert Python programmer. Provide concise, working code examples without explanations.",
            temperature=0.7,
            max_tokens=300
        )
        
        code_example = response.text
        return f"```python\n{code_example}\n```"
    

### 

[​](https://gofastmcp.com/servers/sampling#model-preferences)

Model Preferences

Specify model preferences for different use cases:

Copy

    @mcp.tool
    async def creative_writing(topic: str, ctx: Context) -> str:
        """Generate creative content using a specific model."""
        response = await ctx.sample(
            messages=f"Write a creative short story about {topic}",
            model_preferences="claude-3-sonnet",  # Prefer a specific model
            include_context="thisServer",  # Use the server's context
            temperature=0.9,  # High creativity
            max_tokens=1000
        )
        
        return response.text
    
    @mcp.tool
    async def technical_analysis(data: str, ctx: Context) -> str:
        """Perform technical analysis with a reasoning-focused model."""
        response = await ctx.sample(
            messages=f"Analyze this technical data and provide insights: {data}",
            model_preferences=["claude-3-opus", "gpt-4"],  # Prefer reasoning models
            temperature=0.2,  # Low randomness for consistency
            max_tokens=800
        )
        
        return response.text
    

### 

[​](https://gofastmcp.com/servers/sampling#complex-message-structures)

Complex Message Structures

Use structured messages for more complex interactions:

Copy

    from fastmcp.client.sampling import SamplingMessage
    
    @mcp.tool
    async def multi_turn_analysis(user_query: str, context_data: str, ctx: Context) -> str:
        """Perform analysis using multi-turn conversation structure."""
        messages = [\
            SamplingMessage(role="user", content=f"I have this data: {context_data}"),\
            SamplingMessage(role="assistant", content="I can see your data. What would you like me to analyze?"),\
            SamplingMessage(role="user", content=user_query)\
        ]
        
        response = await ctx.sample(
            messages=messages,
            system_prompt="You are a data analyst. Provide detailed insights based on the conversation context.",
            temperature=0.3
        )
        
        return response.text
    

[​](https://gofastmcp.com/servers/sampling#sampling-fallback-handler)

Sampling Fallback Handler
--------------------------------------------------------------------------------------------------

Client support for sampling is optional. If the client does not support sampling, the server will report an error indicating that the client does not support sampling. However, you can provide a `sampling_handler` to the FastMCP server, which sends sampling requests directly to an LLM provider instead of routing through the client. The `sampling_handler_behavior` parameter controls when this handler is used:

*   **`"fallback"`** (default): Uses the handler only when the client doesn’t support sampling. Requests go to the client first, falling back to the handler if needed.
*   **`"always"`**: Always uses the handler, bypassing the client entirely. Useful when you want full control over the LLM used for sampling.

Sampling handlers can be implemented using any LLM provider, but a sample implementation for OpenAI is provided as a Contrib module. Sampling lacks the full capabilities of typical LLM completions. For this reason, the OpenAI sampling handler, pointed at a third-party provider’s OpenAI-compatible API, is often sufficient to implement a sampling handler.

### 

[​](https://gofastmcp.com/servers/sampling#fallback-mode-default)

Fallback Mode (Default)

Uses the handler only when the client doesn’t support sampling:

Copy

    import asyncio
    import os
    
    from mcp.types import ContentBlock
    from openai import OpenAI
    
    from fastmcp import FastMCP
    from fastmcp.experimental.sampling.handlers.openai import OpenAISamplingHandler
    from fastmcp.server.context import Context
    
    
    async def async_main():
        server = FastMCP(
            name="OpenAI Sampling Fallback Example",
            sampling_handler=OpenAISamplingHandler(
                default_model="gpt-4o-mini",
                client=OpenAI(
                    api_key=os.getenv("API_KEY"),
                    base_url=os.getenv("BASE_URL"),
                ),
            ),
            sampling_handler_behavior="fallback",  # Default - only use when client doesn't support sampling
        )
    
        @server.tool
        async def test_sample_fallback(ctx: Context) -> ContentBlock:
            # Will use client's LLM if available, otherwise falls back to the handler
            return await ctx.sample(
                messages=["hello world!"],
            )
    
        await server.run_http_async()
    
    
    if __name__ == "__main__":
        asyncio.run(async_main())
    

### 

[​](https://gofastmcp.com/servers/sampling#always-mode)

Always Mode

Always uses the handler, bypassing the client:

Copy

    server = FastMCP(
        name="Server-Controlled Sampling",
        sampling_handler=OpenAISamplingHandler(
            default_model="gpt-4o-mini",
            client=OpenAI(api_key=os.getenv("API_KEY")),
        ),
        sampling_handler_behavior="always",  # Always use the handler, never the client
    )
    
    @server.tool
    async def analyze_data(data: str, ctx: Context) -> str:
        # Will ALWAYS use the server's configured LLM, not the client's
        result = await ctx.sample(
            messages=f"Analyze this data: {data}",
            system_prompt="You are a data analyst.",
        )
        return result.text
    

[​](https://gofastmcp.com/servers/sampling#client-requirements)

Client Requirements
--------------------------------------------------------------------------------------

By default, LLM sampling requires client support:

*   Clients must implement sampling handlers to process requests (see [Client Sampling](https://gofastmcp.com/clients/sampling)
    )
*   If the client doesn’t support sampling and no fallback handler is configured, `ctx.sample()` will raise an error
*   Configure a `sampling_handler` with `sampling_handler_behavior="fallback"` to automatically handle clients that don’t support sampling
*   Use `sampling_handler_behavior="always"` to completely bypass the client and control which LLM is used

[Proxy Servers\
\
Previous](https://gofastmcp.com/servers/proxy)
[Storage Backends\
\
Next](https://gofastmcp.com/servers/storage-backends)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.