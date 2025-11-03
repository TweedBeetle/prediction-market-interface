---
url: https://gofastmcp.com/integrations/claude-code
title: Claude Code 🤝 FastMCP - FastMCP
description: Install and use FastMCP servers in Claude Code
scraped_at: 2025-11-03T18:42:15.544478
---

[Skip to main content](https://gofastmcp.com/integrations/claude-code#content-area)

Join the [FastMCP community](https://discord.gg/uu8dJCgttd)
!

[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)

Search...

Navigation

AI Assistants

Claude Code 🤝 FastMCP

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
    
    *   [ChatGPT\
        \
        NEW](https://gofastmcp.com/integrations/chatgpt)
        
    *   [Claude Code](https://gofastmcp.com/integrations/claude-code)
        
    *   [Claude Desktop](https://gofastmcp.com/integrations/claude-desktop)
        
    *   [Cursor](https://gofastmcp.com/integrations/cursor)
        
    *   [Gemini CLI\
        \
        NEW](https://gofastmcp.com/integrations/gemini-cli)
        
    *   [MCP.json](https://gofastmcp.com/integrations/mcp-json-configuration)
        
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

*   [Requirements](https://gofastmcp.com/integrations/claude-code#requirements)
    
*   [Create a Server](https://gofastmcp.com/integrations/claude-code#create-a-server)
    
*   [Install the Server](https://gofastmcp.com/integrations/claude-code#install-the-server)
    
*   [FastMCP CLI](https://gofastmcp.com/integrations/claude-code#fastmcp-cli)
    
*   [Dependencies](https://gofastmcp.com/integrations/claude-code#dependencies)
    
*   [Python Version and Project Configuration](https://gofastmcp.com/integrations/claude-code#python-version-and-project-configuration)
    
*   [Environment Variables](https://gofastmcp.com/integrations/claude-code#environment-variables)
    
*   [Manual Configuration](https://gofastmcp.com/integrations/claude-code#manual-configuration)
    
*   [Using the Server](https://gofastmcp.com/integrations/claude-code#using-the-server)
    

**This integration focuses on running local FastMCP server files with STDIO transport.** For remote servers running with HTTP or SSE transport, use your client's native configuration - FastMCP's integrations focus on simplifying the complex local setup with dependencies and `uv` commands.

Claude Code supports MCP servers through multiple transport methods including STDIO, SSE, and HTTP, allowing you to extend Claude’s capabilities with custom tools, resources, and prompts from your FastMCP servers.

[​](https://gofastmcp.com/integrations/claude-code#requirements)

Requirements
--------------------------------------------------------------------------------

This integration uses STDIO transport to run your FastMCP server locally. For remote deployments, you can run your FastMCP server with HTTP or SSE transport and configure it directly using Claude Code’s built-in MCP management commands.

[​](https://gofastmcp.com/integrations/claude-code#create-a-server)

Create a Server
--------------------------------------------------------------------------------------

The examples in this guide will use the following simple dice-rolling server, saved as `server.py`.

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
    

[​](https://gofastmcp.com/integrations/claude-code#install-the-server)

Install the Server
--------------------------------------------------------------------------------------------

### 

[​](https://gofastmcp.com/integrations/claude-code#fastmcp-cli)

FastMCP CLI

`` New in version: `2.10.3` `` The easiest way to install a FastMCP server in Claude Code is using the `fastmcp install claude-code` command. This automatically handles the configuration, dependency management, and calls Claude Code’s built-in MCP management system.

Copy

    fastmcp install claude-code server.py
    

The install command supports the same `file.py:object` notation as the `run` command. If no object is specified, it will automatically look for a FastMCP server object named `mcp`, `server`, or `app` in your file:

Copy

    # These are equivalent if your server object is named 'mcp'
    fastmcp install claude-code server.py
    fastmcp install claude-code server.py:mcp
    
    # Use explicit object name if your server has a different name
    fastmcp install claude-code server.py:my_custom_server
    

The command will automatically configure the server with Claude Code’s `claude mcp add` command.

#### 

[​](https://gofastmcp.com/integrations/claude-code#dependencies)

Dependencies

FastMCP provides flexible dependency management options for your Claude Code servers: **Individual packages**: Use the `--with` flag to specify packages your server needs. You can use this flag multiple times:

Copy

    fastmcp install claude-code server.py --with pandas --with requests
    

**Requirements file**: If you maintain a `requirements.txt` file with all your dependencies, use `--with-requirements` to install them:

Copy

    fastmcp install claude-code server.py --with-requirements requirements.txt
    

**Editable packages**: For local packages under development, use `--with-editable` to install them in editable mode:

Copy

    fastmcp install claude-code server.py --with-editable ./my-local-package
    

Alternatively, you can use a `fastmcp.json` configuration file (recommended):

fastmcp.json

Copy

    {
      "$schema": "https://gofastmcp.com/public/schemas/fastmcp.json/v1.json",
      "source": {
        "path": "server.py",
        "entrypoint": "mcp"
      },
      "environment": {
        "dependencies": ["pandas", "requests"]
      }
    }
    

#### 

[​](https://gofastmcp.com/integrations/claude-code#python-version-and-project-configuration)

Python Version and Project Configuration

Control the Python environment for your server with these options: **Python version**: Use `--python` to specify which Python version your server requires. This ensures compatibility when your server needs specific Python features:

Copy

    fastmcp install claude-code server.py --python 3.11
    

**Project directory**: Use `--project` to run your server within a specific project context. This tells `uv` to use the project’s configuration files and virtual environment:

Copy

    fastmcp install claude-code server.py --project /path/to/my-project
    

#### 

[​](https://gofastmcp.com/integrations/claude-code#environment-variables)

Environment Variables

If your server needs environment variables (like API keys), you must include them:

Copy

    fastmcp install claude-code server.py --server-name "Weather Server" \
      --env API_KEY=your-api-key \
      --env DEBUG=true
    

Or load them from a `.env` file:

Copy

    fastmcp install claude-code server.py --server-name "Weather Server" --env-file .env
    

**Claude Code must be installed**. The integration looks for the Claude Code CLI at the default installation location (`~/.claude/local/claude`) and uses the `claude mcp add` command to register servers.

### 

[​](https://gofastmcp.com/integrations/claude-code#manual-configuration)

Manual Configuration

For more control over the configuration, you can manually use Claude Code’s built-in MCP management commands. This gives you direct control over how your server is launched:

Copy

    # Add a server with custom configuration
    claude mcp add dice-roller -- uv run --with fastmcp fastmcp run server.py
    
    # Add with environment variables
    claude mcp add weather-server -e API_KEY=secret -e DEBUG=true -- uv run --with fastmcp fastmcp run server.py
    
    # Add with specific scope (local, user, or project)
    claude mcp add my-server --scope user -- uv run --with fastmcp fastmcp run server.py
    

You can also manually specify Python versions and project directories in your Claude Code commands:

Copy

    # With specific Python version
    claude mcp add ml-server -- uv run --python 3.11 --with fastmcp fastmcp run server.py
    
    # Within a project directory
    claude mcp add project-server -- uv run --project /path/to/project --with fastmcp fastmcp run server.py
    

[​](https://gofastmcp.com/integrations/claude-code#using-the-server)

Using the Server
----------------------------------------------------------------------------------------

Once your server is installed, you can start using your FastMCP server with Claude Code. Try asking Claude something like:

> “Roll some dice for me”

Claude will automatically detect your `roll_dice` tool and use it to fulfill your request, returning something like:

> I’ll roll some dice for you! Here are your results: \[4, 2, 6\] You rolled three dice and got a 4, a 2, and a 6!

Claude Code can now access all the tools, resources, and prompts you’ve defined in your FastMCP server. If your server provides resources, you can reference them with `@` mentions using the format `@server:protocol://resource/path`. If your server provides prompts, you can use them as slash commands with `/mcp__servername__promptname`.

[ChatGPT 🤝 FastMCP\
\
Previous](https://gofastmcp.com/integrations/chatgpt)
[Claude Desktop 🤝 FastMCP\
\
Next](https://gofastmcp.com/integrations/claude-desktop)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.