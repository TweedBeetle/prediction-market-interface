---
url: https://gofastmcp.com/integrations/mcp-json-configuration
title: MCP JSON Configuration 🤝 FastMCP - FastMCP
description: Generate standard MCP configuration files for any compatible client
scraped_at: 2025-11-03T18:42:16.070686
---

[Skip to main content](https://gofastmcp.com/integrations/mcp-json-configuration#content-area)

Join the [FastMCP community](https://discord.gg/uu8dJCgttd)
!

[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)

Search...

Navigation

AI Assistants

MCP JSON Configuration 🤝 FastMCP

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

*   [MCP JSON Configuration Standard](https://gofastmcp.com/integrations/mcp-json-configuration#mcp-json-configuration-standard)
    
*   [Configuration Structure](https://gofastmcp.com/integrations/mcp-json-configuration#configuration-structure)
    
*   [Server Configuration Fields](https://gofastmcp.com/integrations/mcp-json-configuration#server-configuration-fields)
    
*   [command (required)](https://gofastmcp.com/integrations/mcp-json-configuration#command-required)
    
*   [args (optional)](https://gofastmcp.com/integrations/mcp-json-configuration#args-optional)
    
*   [env (optional)](https://gofastmcp.com/integrations/mcp-json-configuration#env-optional)
    
*   [Client Adoption](https://gofastmcp.com/integrations/mcp-json-configuration#client-adoption)
    
*   [Overview](https://gofastmcp.com/integrations/mcp-json-configuration#overview)
    
*   [Basic Usage](https://gofastmcp.com/integrations/mcp-json-configuration#basic-usage)
    
*   [Configuration Options](https://gofastmcp.com/integrations/mcp-json-configuration#configuration-options)
    
*   [Server Naming](https://gofastmcp.com/integrations/mcp-json-configuration#server-naming)
    
*   [Dependencies](https://gofastmcp.com/integrations/mcp-json-configuration#dependencies)
    
*   [Environment Variables](https://gofastmcp.com/integrations/mcp-json-configuration#environment-variables)
    
*   [Python Version and Project Directory](https://gofastmcp.com/integrations/mcp-json-configuration#python-version-and-project-directory)
    
*   [Server Object Selection](https://gofastmcp.com/integrations/mcp-json-configuration#server-object-selection)
    
*   [Clipboard Integration](https://gofastmcp.com/integrations/mcp-json-configuration#clipboard-integration)
    
*   [Usage Examples](https://gofastmcp.com/integrations/mcp-json-configuration#usage-examples)
    
*   [Basic Server](https://gofastmcp.com/integrations/mcp-json-configuration#basic-server)
    
*   [Production Server with Dependencies](https://gofastmcp.com/integrations/mcp-json-configuration#production-server-with-dependencies)
    
*   [Advanced Configuration](https://gofastmcp.com/integrations/mcp-json-configuration#advanced-configuration)
    
*   [Pipeline Usage](https://gofastmcp.com/integrations/mcp-json-configuration#pipeline-usage)
    
*   [Integration with MCP Clients](https://gofastmcp.com/integrations/mcp-json-configuration#integration-with-mcp-clients)
    
*   [Claude Desktop](https://gofastmcp.com/integrations/mcp-json-configuration#claude-desktop)
    
*   [Cursor](https://gofastmcp.com/integrations/mcp-json-configuration#cursor)
    
*   [VS Code](https://gofastmcp.com/integrations/mcp-json-configuration#vs-code)
    
*   [Custom Applications](https://gofastmcp.com/integrations/mcp-json-configuration#custom-applications)
    
*   [Configuration Format](https://gofastmcp.com/integrations/mcp-json-configuration#configuration-format)
    
*   [Requirements](https://gofastmcp.com/integrations/mcp-json-configuration#requirements)
    

`` New in version: `2.10.3` `` FastMCP can generate standard MCP JSON configuration files that work with any MCP-compatible client including Claude Desktop, VS Code, Cursor, and other applications that support the Model Context Protocol.

[​](https://gofastmcp.com/integrations/mcp-json-configuration#mcp-json-configuration-standard)

MCP JSON Configuration Standard
---------------------------------------------------------------------------------------------------------------------------------

The MCP JSON configuration format is an **emergent standard** that has developed across the MCP ecosystem. This format defines how MCP clients should configure and launch MCP servers, providing a consistent way to specify server commands, arguments, and environment variables.

### 

[​](https://gofastmcp.com/integrations/mcp-json-configuration#configuration-structure)

Configuration Structure

The standard uses a `mcpServers` object where each key represents a server name and the value contains the server’s configuration:

Copy

    {
      "mcpServers": {
        "server-name": {
          "command": "executable",
          "args": ["arg1", "arg2"],
          "env": {
            "VAR": "value"
          }
        }
      }
    }
    

### 

[​](https://gofastmcp.com/integrations/mcp-json-configuration#server-configuration-fields)

Server Configuration Fields

#### 

[​](https://gofastmcp.com/integrations/mcp-json-configuration#command-required)

`command` (required)

The executable command to run the MCP server. This should be an absolute path or a command available in the system PATH.

Copy

    {
      "command": "python"
    }
    

#### 

[​](https://gofastmcp.com/integrations/mcp-json-configuration#args-optional)

`args` (optional)

An array of command-line arguments passed to the server executable. Arguments are passed in order.

Copy

    {
      "args": ["server.py", "--verbose", "--port", "8080"]
    }
    

#### 

[​](https://gofastmcp.com/integrations/mcp-json-configuration#env-optional)

`env` (optional)

An object containing environment variables to set when launching the server. All values must be strings.

Copy

    {
      "env": {
        "API_KEY": "secret-key",
        "DEBUG": "true",
        "PORT": "8080"
      }
    }
    

### 

[​](https://gofastmcp.com/integrations/mcp-json-configuration#client-adoption)

Client Adoption

This format is widely adopted across the MCP ecosystem:

*   **Claude Desktop**: Uses `~/.claude/claude_desktop_config.json`
*   **Cursor**: Uses `~/.cursor/mcp.json`
*   **VS Code**: Uses workspace `.vscode/mcp.json`
*   **Other clients**: Many MCP-compatible applications follow this standard

[​](https://gofastmcp.com/integrations/mcp-json-configuration#overview)

Overview
-----------------------------------------------------------------------------------

**For the best experience, use FastMCP’s first-class integrations:** [`fastmcp install claude-code`](https://gofastmcp.com/integrations/claude-code)
, [`fastmcp install claude-desktop`](https://gofastmcp.com/integrations/claude-desktop)
, or [`fastmcp install cursor`](https://gofastmcp.com/integrations/cursor)
. Use MCP JSON generation for advanced use cases and unsupported clients.

The `fastmcp install mcp-json` command generates configuration in the standard `mcpServers` format used across the MCP ecosystem. This is useful when:

*   **Working with unsupported clients** - Any MCP client not directly integrated with FastMCP
*   **CI/CD environments** - Automated configuration generation for deployments
*   **Configuration sharing** - Easy distribution of server setups to team members
*   **Custom tooling** - Integration with your own MCP management tools
*   **Manual setup** - When you prefer to manually configure your MCP client

[​](https://gofastmcp.com/integrations/mcp-json-configuration#basic-usage)

Basic Usage
-----------------------------------------------------------------------------------------

Generate configuration and output to stdout (useful for piping):

Copy

    fastmcp install mcp-json server.py
    

This outputs the server configuration JSON with the server name as the root key:

Copy

    {
      "My Server": {
        "command": "uv",
        "args": [\
          "run",\
          "--with",\
          "fastmcp", \
          "fastmcp",\
          "run",\
          "/absolute/path/to/server.py"\
        ]
      }
    }
    

To use this in a client configuration file, add it to the `mcpServers` object in your client’s configuration:

Copy

    {
      "mcpServers": {
        "My Server": {
          "command": "uv",
          "args": [\
            "run",\
            "--with",\
            "fastmcp", \
            "fastmcp",\
            "run",\
            "/absolute/path/to/server.py"\
          ]
        }
      }
    }
    

When using `--python`, `--project`, or `--with-requirements`, the generated configuration will include these options in the `uv run` command, ensuring your server runs with the correct Python version and dependencies.

Different MCP clients may have specific configuration requirements or formatting needs. Always consult your client’s documentation to ensure proper integration.

[​](https://gofastmcp.com/integrations/mcp-json-configuration#configuration-options)

Configuration Options
-------------------------------------------------------------------------------------------------------------

### 

[​](https://gofastmcp.com/integrations/mcp-json-configuration#server-naming)

Server Naming

Copy

    # Use server's built-in name (from FastMCP constructor)
    fastmcp install mcp-json server.py
    
    # Override with custom name
    fastmcp install mcp-json server.py --name "Custom Server Name"
    

### 

[​](https://gofastmcp.com/integrations/mcp-json-configuration#dependencies)

Dependencies

Add Python packages your server needs:

Copy

    # Single package
    fastmcp install mcp-json server.py --with pandas
    
    # Multiple packages  
    fastmcp install mcp-json server.py --with pandas --with requests --with httpx
    
    # Editable local package
    fastmcp install mcp-json server.py --with-editable ./my-package
    
    # From requirements file
    fastmcp install mcp-json server.py --with-requirements requirements.txt
    

You can also use a `fastmcp.json` configuration file (recommended):

fastmcp.json

Copy

    {
      "$schema": "https://gofastmcp.com/public/schemas/fastmcp.json/v1.json",
      "source": {
        "path": "server.py",
        "entrypoint": "mcp"
      },
      "environment": {
        "dependencies": ["pandas", "matplotlib", "seaborn"]
      }
    }
    

Then simply install with:

Copy

    fastmcp install mcp-json fastmcp.json
    

### 

[​](https://gofastmcp.com/integrations/mcp-json-configuration#environment-variables)

Environment Variables

Copy

    # Individual environment variables
    fastmcp install mcp-json server.py \
      --env API_KEY=your-secret-key \
      --env DEBUG=true
    
    # Load from .env file
    fastmcp install mcp-json server.py --env-file .env
    

### 

[​](https://gofastmcp.com/integrations/mcp-json-configuration#python-version-and-project-directory)

Python Version and Project Directory

Specify Python version or run within a specific project:

Copy

    # Use specific Python version
    fastmcp install mcp-json server.py --python 3.11
    
    # Run within a project directory
    fastmcp install mcp-json server.py --project /path/to/project
    

### 

[​](https://gofastmcp.com/integrations/mcp-json-configuration#server-object-selection)

Server Object Selection

Use the same `file.py:object` notation as other FastMCP commands:

Copy

    # Auto-detects server object (looks for 'mcp', 'server', or 'app')
    fastmcp install mcp-json server.py
    
    # Explicit server object
    fastmcp install mcp-json server.py:my_custom_server
    

[​](https://gofastmcp.com/integrations/mcp-json-configuration#clipboard-integration)

Clipboard Integration
-------------------------------------------------------------------------------------------------------------

Copy configuration directly to your clipboard for easy pasting:

Copy

    fastmcp install mcp-json server.py --copy
    

The `--copy` flag requires the `pyperclip` Python package. If not installed, you’ll see an error message with installation instructions.

[​](https://gofastmcp.com/integrations/mcp-json-configuration#usage-examples)

Usage Examples
-----------------------------------------------------------------------------------------------

### 

[​](https://gofastmcp.com/integrations/mcp-json-configuration#basic-server)

Basic Server

Copy

    fastmcp install mcp-json dice_server.py
    

Output:

Copy

    {
      "Dice Server": {
        "command": "uv",
        "args": [\
          "run",\
          "--with",\
          "fastmcp",\
          "fastmcp", \
          "run",\
          "/home/user/dice_server.py"\
        ]
      }
    }
    

### 

[​](https://gofastmcp.com/integrations/mcp-json-configuration#production-server-with-dependencies)

Production Server with Dependencies

Copy

    fastmcp install mcp-json api_server.py \
      --name "Production API Server" \
      --with requests \
      --with python-dotenv \
      --env API_BASE_URL=https://api.example.com \
      --env TIMEOUT=30
    

### 

[​](https://gofastmcp.com/integrations/mcp-json-configuration#advanced-configuration)

Advanced Configuration

Copy

    fastmcp install mcp-json ml_server.py \
      --name "ML Analysis Server" \
      --python 3.11 \
      --with-requirements requirements.txt \
      --project /home/user/ml-project \
      --env GPU_DEVICE=0
    

Output:

Copy

    {
      "Production API Server": {
        "command": "uv",
        "args": [\
          "run",\
          "--with",\
          "fastmcp",\
          "--with",\
          "python-dotenv", \
          "--with",\
          "requests",\
          "fastmcp",\
          "run", \
          "/home/user/api_server.py"\
        ],
        "env": {
          "API_BASE_URL": "https://api.example.com",
          "TIMEOUT": "30"
        }
      }
    }
    

The advanced configuration example generates:

Copy

    {
      "ML Analysis Server": {
        "command": "uv",
        "args": [\
          "run",\
          "--python",\
          "3.11",\
          "--project",\
          "/home/user/ml-project",\
          "--with",\
          "fastmcp",\
          "--with-requirements",\
          "requirements.txt",\
          "fastmcp",\
          "run",\
          "/home/user/ml_server.py"\
        ],
        "env": {
          "GPU_DEVICE": "0"
        }
      }
    }
    

### 

[​](https://gofastmcp.com/integrations/mcp-json-configuration#pipeline-usage)

Pipeline Usage

Save configuration to file:

Copy

    fastmcp install mcp-json server.py > mcp-config.json
    

Use in shell scripts:

Copy

    #!/bin/bash
    CONFIG=$(fastmcp install mcp-json server.py --name "CI Server")
    echo "$CONFIG" | jq '."CI Server".command'
    # Output: "uv"
    

[​](https://gofastmcp.com/integrations/mcp-json-configuration#integration-with-mcp-clients)

Integration with MCP Clients
---------------------------------------------------------------------------------------------------------------------------

The generated configuration works with any MCP-compatible application:

### 

[​](https://gofastmcp.com/integrations/mcp-json-configuration#claude-desktop)

Claude Desktop

**Prefer [`fastmcp install claude-desktop`](https://gofastmcp.com/integrations/claude-desktop)
** for automatic installation. Use MCP JSON for advanced configuration needs.

Copy the `mcpServers` object into `~/.claude/claude_desktop_config.json`

### 

[​](https://gofastmcp.com/integrations/mcp-json-configuration#cursor)

Cursor

**Prefer [`fastmcp install cursor`](https://gofastmcp.com/integrations/cursor)
** for automatic installation. Use MCP JSON for advanced configuration needs.

Add to `~/.cursor/mcp.json`

### 

[​](https://gofastmcp.com/integrations/mcp-json-configuration#vs-code)

VS Code

Add to your workspace’s `.vscode/mcp.json` file

### 

[​](https://gofastmcp.com/integrations/mcp-json-configuration#custom-applications)

Custom Applications

Use the JSON configuration with any application that supports the MCP protocol

[​](https://gofastmcp.com/integrations/mcp-json-configuration#configuration-format)

Configuration Format
-----------------------------------------------------------------------------------------------------------

The generated configuration outputs a server object with the server name as the root key:

Copy

    {
      "<server-name>": {
        "command": "<executable>",
        "args": ["<arg1>", "<arg2>", "..."],
        "env": {
          "<ENV_VAR>": "<value>"
        }
      }
    }
    

To use this in an MCP client, add it to the client’s `mcpServers` configuration object. **Fields:**

*   `command`: The executable to run (always `uv` for FastMCP servers)
*   `args`: Command-line arguments including dependencies and server path
*   `env`: Environment variables (only included if specified)

**All file paths in the generated configuration are absolute paths**. This ensures the configuration works regardless of the working directory when the MCP client starts the server.

[​](https://gofastmcp.com/integrations/mcp-json-configuration#requirements)

Requirements
-------------------------------------------------------------------------------------------

*   **uv**: Must be installed and available in your system PATH
*   **pyperclip** (optional): Required only for `--copy` functionality

Install uv if not already available:

Copy

    # macOS
    brew install uv
    
    # Linux/Windows  
    curl -LsSf https://astral.sh/uv/install.sh | sh
    

[Gemini CLI 🤝 FastMCP\
\
Previous](https://gofastmcp.com/integrations/gemini-cli)
[Anthropic API 🤝 FastMCP\
\
Next](https://gofastmcp.com/integrations/anthropic)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.