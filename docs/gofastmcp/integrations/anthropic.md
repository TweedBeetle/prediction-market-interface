---
url: https://gofastmcp.com/integrations/anthropic
title: Anthropic API 🤝 FastMCP - FastMCP
description: Connect FastMCP servers to the Anthropic API
scraped_at: 2025-11-03T18:42:09.773529
---

[Skip to main content](https://gofastmcp.com/integrations/anthropic#content-area)

Join the [FastMCP community](https://discord.gg/uu8dJCgttd)
!

[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)

Search...

Navigation

AI SDKs

Anthropic API 🤝 FastMCP

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

*   [Create a Server](https://gofastmcp.com/integrations/anthropic#create-a-server)
    
*   [Deploy the Server](https://gofastmcp.com/integrations/anthropic#deploy-the-server)
    
*   [Call the Server](https://gofastmcp.com/integrations/anthropic#call-the-server)
    
*   [Authentication](https://gofastmcp.com/integrations/anthropic#authentication)
    
*   [Server Authentication](https://gofastmcp.com/integrations/anthropic#server-authentication)
    
*   [Client Authentication](https://gofastmcp.com/integrations/anthropic#client-authentication)
    

Anthropic’s [Messages API](https://docs.anthropic.com/en/api/messages)
 supports MCP servers as remote tool sources. This tutorial will show you how to create a FastMCP server and deploy it to a public URL, then how to call it from the Messages API.

Currently, the MCP connector only accesses **tools** from MCP servers—it queries the `list_tools` endpoint and exposes those functions to Claude. Other MCP features like resources and prompts are not currently supported. You can read more about the MCP connector in the [Anthropic documentation](https://docs.anthropic.com/en/docs/agents-and-tools/mcp-connector)
.

[​](https://gofastmcp.com/integrations/anthropic#create-a-server)

Create a Server
------------------------------------------------------------------------------------

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
        mcp.run(transport="http", port=8000)
    

[​](https://gofastmcp.com/integrations/anthropic#deploy-the-server)

Deploy the Server
----------------------------------------------------------------------------------------

Your server must be deployed to a public URL in order for Anthropic to access it. The MCP connector supports both SSE and Streamable HTTP transports. For development, you can use tools like `ngrok` to temporarily expose a locally-running server to the internet. We’ll do that for this example (you may need to install `ngrok` and create a free account), but you can use any other method to deploy your server. Assuming you saved the above code as `server.py`, you can run the following two commands in two separate terminals to deploy your server and expose it to the internet:

FastMCP server

ngrok

Copy

    python server.py
    

This exposes your unauthenticated server to the internet. Only run this command in a safe environment if you understand the risks.

[​](https://gofastmcp.com/integrations/anthropic#call-the-server)

Call the Server
------------------------------------------------------------------------------------

To use the Messages API with MCP servers, you’ll need to install the Anthropic Python SDK (not included with FastMCP):

Copy

    pip install anthropic
    

You’ll also need to authenticate with Anthropic. You can do this by setting the `ANTHROPIC_API_KEY` environment variable. Consult the Anthropic SDK documentation for more information.

Copy

    export ANTHROPIC_API_KEY="your-api-key"
    

Here is an example of how to call your server from Python. Note that you’ll need to replace `https://your-server-url.com` with the actual URL of your server. In addition, we use `/mcp/` as the endpoint because we deployed a streamable-HTTP server with the default path; you may need to use a different endpoint if you customized your server’s deployment. **At this time you must also include the `extra_headers` parameter with the `anthropic-beta` header.**

Copy

    import anthropic
    from rich import print
    
    # Your server URL (replace with your actual URL)
    url = 'https://your-server-url.com'
    
    client = anthropic.Anthropic()
    
    response = client.beta.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        messages=[{"role": "user", "content": "Roll a few dice!"}],
        mcp_servers=[\
            {\
                "type": "url",\
                "url": f"{url}/mcp/",\
                "name": "dice-server",\
            }\
        ],
        extra_headers={
            "anthropic-beta": "mcp-client-2025-04-04"
        }
    )
    
    print(response.content)
    

If you run this code, you’ll see something like the following output:

Copy

    I'll roll some dice for you! Let me use the dice rolling tool.
    
    I rolled 3 dice and got: 4, 2, 6
    
    The results were 4, 2, and 6. Would you like me to roll again or roll a different number of dice?
    

[​](https://gofastmcp.com/integrations/anthropic#authentication)

Authentication
----------------------------------------------------------------------------------

`` New in version: `2.6.0` `` The MCP connector supports OAuth authentication through authorization tokens, which means you can secure your server while still allowing Anthropic to access it.

### 

[​](https://gofastmcp.com/integrations/anthropic#server-authentication)

Server Authentication

The simplest way to add authentication to the server is to use a bearer token scheme. For this example, we’ll quickly generate our own tokens with FastMCP’s `RSAKeyPair` utility, but this may not be appropriate for production use. For more details, see the complete server-side [Token Verification](https://gofastmcp.com/servers/auth/token-verification)
 documentation. We’ll start by creating an RSA key pair to sign and verify tokens.

Copy

    from fastmcp.server.auth.providers.jwt import RSAKeyPair
    
    key_pair = RSAKeyPair.generate()
    access_token = key_pair.create_token(audience="dice-server")
    

FastMCP’s `RSAKeyPair` utility is for development and testing only.

Next, we’ll create a `JWTVerifier` to authenticate the server.

Copy

    from fastmcp import FastMCP
    from fastmcp.server.auth import JWTVerifier
    
    auth = JWTVerifier(
        public_key=key_pair.public_key,
        audience="dice-server",
    )
    
    mcp = FastMCP(name="Dice Roller", auth=auth)
    

Here is a complete example that you can copy/paste. For simplicity and the purposes of this example only, it will print the token to the console. **Do NOT do this in production!**

server.py

Copy

    from fastmcp import FastMCP
    from fastmcp.server.auth import JWTVerifier
    from fastmcp.server.auth.providers.jwt import RSAKeyPair
    import random
    
    key_pair = RSAKeyPair.generate()
    access_token = key_pair.create_token(audience="dice-server")
    
    auth = JWTVerifier(
        public_key=key_pair.public_key,
        audience="dice-server",
    )
    
    mcp = FastMCP(name="Dice Roller", auth=auth)
    
    @mcp.tool
    def roll_dice(n_dice: int) -> list[int]:
        """Roll `n_dice` 6-sided dice and return the results."""
        return [random.randint(1, 6) for _ in range(n_dice)]
    
    if __name__ == "__main__":
        print(f"\n---\n\n🔑 Dice Roller access token:\n\n{access_token}\n\n---\n")
        mcp.run(transport="http", port=8000)
    

See all 23 lines

### 

[​](https://gofastmcp.com/integrations/anthropic#client-authentication)

Client Authentication

If you try to call the authenticated server with the same Anthropic code we wrote earlier, you’ll get an error indicating that the server rejected the request because it’s not authenticated.

Copy

    Error code: 400 - {
        "type": "error", 
        "error": {
            "type": "invalid_request_error", 
            "message": "MCP server 'dice-server' requires authentication. Please provide an authorization_token.",
        },
    }
    

To authenticate the client, you can pass the token using the `authorization_token` parameter in your MCP server configuration:

Copy

    import anthropic
    from rich import print
    
    # Your server URL (replace with your actual URL)
    url = 'https://your-server-url.com'
    
    # Your access token (replace with your actual token)
    access_token = 'your-access-token'
    
    client = anthropic.Anthropic()
    
    response = client.beta.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        messages=[{"role": "user", "content": "Roll a few dice!"}],
        mcp_servers=[\
            {\
                "type": "url",\
                "url": f"{url}/mcp/",\
                "name": "dice-server",\
                "authorization_token": access_token\
            }\
        ],
        extra_headers={
            "anthropic-beta": "mcp-client-2025-04-04"
        }
    )
    
    print(response.content)
    

You should now see the dice roll results in the output.

[MCP JSON Configuration 🤝 FastMCP\
\
Previous](https://gofastmcp.com/integrations/mcp-json-configuration)
[Gemini SDK 🤝 FastMCP\
\
Next](https://gofastmcp.com/integrations/gemini)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.