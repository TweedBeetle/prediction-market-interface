---
url: https://gofastmcp.com/integrations/gemini
title: Gemini SDK 🤝 FastMCP - FastMCP
description: Connect FastMCP servers to the Google Gemini SDK
scraped_at: 2025-11-03T18:42:15.564004
---

[Skip to main content](https://gofastmcp.com/integrations/gemini#content-area)

Join the [FastMCP community](https://discord.gg/uu8dJCgttd)
!

[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)

Search...

Navigation

AI SDKs

Gemini SDK 🤝 FastMCP

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
    
    *   [Anthropic API](https://gofastmcp.com/integrations/anthropic)
        
    *   [Gemini SDK](https://gofastmcp.com/integrations/gemini)
        
    *   [OpenAI API](https://gofastmcp.com/integrations/openai)
        
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

*   [Gemini Python SDK](https://gofastmcp.com/integrations/gemini#gemini-python-sdk)
    
*   [Create a Server](https://gofastmcp.com/integrations/gemini#create-a-server)
    
*   [Call the Server](https://gofastmcp.com/integrations/gemini#call-the-server)
    
*   [Remote & Authenticated Servers](https://gofastmcp.com/integrations/gemini#remote-%26-authenticated-servers)
    

Google’s Gemini API includes built-in support for MCP servers in their Python and JavaScript SDKs, allowing you to connect directly to MCP servers and use their tools seamlessly with Gemini models.

[​](https://gofastmcp.com/integrations/gemini#gemini-python-sdk)

Gemini Python SDK
-------------------------------------------------------------------------------------

Google’s [Gemini Python SDK](https://ai.google.dev/gemini-api/docs)
 can use FastMCP clients directly.

Google’s MCP integration is currently experimental and available in the Python and JavaScript SDKs. The API automatically calls MCP tools when needed and can connect to both local and remote MCP servers.

Currently, Gemini’s MCP support only accesses **tools** from MCP servers—it queries the `list_tools` endpoint and exposes those functions to the AI. Other MCP features like resources and prompts are not currently supported.

### 

[​](https://gofastmcp.com/integrations/gemini#create-a-server)

Create a Server

First, create a FastMCP server with the tools you want to expose. For this example, we’ll create a server with a single tool that rolls dice.

server.py

Copy

    import random
    from fastmcp import FastMCP
    
    mcp = FastMCP(name="Dice Roller")
    
    @mcp.tool
    def roll_dice(n_dice: int) -> list[int]:
        """Roll `n_dice` 6-sided dice and return the results."""
        return [random.randint(1, 6) for _ in range(n_dice)]
    
    if __name__ == "__main__":
        mcp.run()
    

### 

[​](https://gofastmcp.com/integrations/gemini#call-the-server)

Call the Server

To use the Gemini API with MCP, you’ll need to install the Google Generative AI SDK:

Copy

    pip install google-genai
    

You’ll also need to authenticate with Google. You can do this by setting the `GEMINI_API_KEY` environment variable. Consult the Gemini SDK documentation for more information.

Copy

    export GEMINI_API_KEY="your-api-key"
    

Gemini’s SDK interacts directly with the MCP client session. To call the server, you’ll need to instantiate a FastMCP client, enter its connection context, and pass the client session to the Gemini SDK.

Copy

    from fastmcp import Client
    from google import genai
    import asyncio
    
    mcp_client = Client("server.py")
    gemini_client = genai.Client()
    
    async def main():    
        async with mcp_client:
            response = await gemini_client.aio.models.generate_content(
                model="gemini-2.0-flash",
                contents="Roll 3 dice!",
                config=genai.types.GenerateContentConfig(
                    temperature=0,
                    tools=[mcp_client.session],  # Pass the FastMCP client session
                ),
            )
            print(response.text)
    
    if __name__ == "__main__":
        asyncio.run(main())
    

If you run this code, you’ll see output like:

Copy

    Okay, I rolled 3 dice and got a 5, 4, and 1.
    

### 

[​](https://gofastmcp.com/integrations/gemini#remote-%26-authenticated-servers)

Remote & Authenticated Servers

In the above example, we connected to our local server using `stdio` transport. Because we’re using a FastMCP client, you can also connect to any local or remote MCP server, using any [transport](https://gofastmcp.com/clients/transports)
 or [auth](https://gofastmcp.com/clients/auth)
 method supported by FastMCP, simply by changing the client configuration. For example, to connect to a remote, authenticated server, you can use the following client:

Copy

    from fastmcp import Client
    from fastmcp.client.auth import BearerAuth
    
    mcp_client = Client(
        "https://my-server.com/mcp/",
        auth=BearerAuth("<your-token>"),
    )
    

The rest of the code remains the same.

[Anthropic API 🤝 FastMCP\
\
Previous](https://gofastmcp.com/integrations/anthropic)
[OpenAI API 🤝 FastMCP\
\
Next](https://gofastmcp.com/integrations/openai)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.