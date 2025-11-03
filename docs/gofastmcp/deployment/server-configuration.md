---
url: https://gofastmcp.com/deployment/server-configuration
title: Project Configuration - FastMCP
description: Use fastmcp.json for portable, declarative project configuration
scraped_at: 2025-11-03T18:42:03.471195
---

[Skip to main content](https://gofastmcp.com/deployment/server-configuration#content-area)

Join the [FastMCP community](https://discord.gg/uu8dJCgttd)
!

[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)

Search...

Navigation

Deployment

Project Configuration

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
    
    *   [Running Your Server](https://gofastmcp.com/deployment/running-server)
        
    *   [HTTP Deployment\
        \
        NEW](https://gofastmcp.com/deployment/http)
        
    *   [FastMCP Cloud\
        \
        NEW](https://gofastmcp.com/deployment/fastmcp-cloud)
        
    *   [Project Configuration](https://gofastmcp.com/deployment/server-configuration)
        

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

*   [Overview](https://gofastmcp.com/deployment/server-configuration#overview)
    
*   [File Structure](https://gofastmcp.com/deployment/server-configuration#file-structure)
    
*   [JSON Schema Support](https://gofastmcp.com/deployment/server-configuration#json-schema-support)
    
*   [Source Configuration](https://gofastmcp.com/deployment/server-configuration#source-configuration)
    
*   [Environment Configuration](https://gofastmcp.com/deployment/server-configuration#environment-configuration)
    
*   [Deployment Configuration](https://gofastmcp.com/deployment/server-configuration#deployment-configuration)
    
*   [Environment Variable Interpolation](https://gofastmcp.com/deployment/server-configuration#environment-variable-interpolation)
    
*   [Usage with CLI Commands](https://gofastmcp.com/deployment/server-configuration#usage-with-cli-commands)
    
*   [Pre-building Environments](https://gofastmcp.com/deployment/server-configuration#pre-building-environments)
    
*   [Using an Existing Environment](https://gofastmcp.com/deployment/server-configuration#using-an-existing-environment)
    
*   [Using an Existing Source](https://gofastmcp.com/deployment/server-configuration#using-an-existing-source)
    
*   [CLI Override Behavior](https://gofastmcp.com/deployment/server-configuration#cli-override-behavior)
    
*   [Custom Naming Patterns](https://gofastmcp.com/deployment/server-configuration#custom-naming-patterns)
    
*   [Examples](https://gofastmcp.com/deployment/server-configuration#examples)
    
*   [Migrating from CLI Arguments](https://gofastmcp.com/deployment/server-configuration#migrating-from-cli-arguments)
    

`` New in version: `2.12.0` `` FastMCP supports declarative configuration through `fastmcp.json` files. This is the canonical and preferred way to configure FastMCP projects, providing a single source of truth for server settings, dependencies, and deployment options that replaces complex command-line arguments. The `fastmcp.json` file is designed to be a portable description of your server configuration that can be shared across environments and teams. When running from a `fastmcp.json` file, you can override any configuration values using CLI arguments.

[​](https://gofastmcp.com/deployment/server-configuration#overview)

Overview
-------------------------------------------------------------------------------

The `fastmcp.json` configuration file allows you to define all aspects of your FastMCP server in a structured, shareable format. Instead of remembering command-line arguments or writing shell scripts, you declare your server’s configuration once and use it everywhere. When you have a `fastmcp.json` file, running your server becomes as simple as:

Copy

    # Run the server using the configuration
    fastmcp run fastmcp.json
    
    # Or if fastmcp.json exists in the current directory
    fastmcp run
    

This configuration approach ensures reproducible deployments across different environments, from local development to production servers. It works seamlessly with Claude Desktop, VS Code extensions, and any MCP-compatible client.

[​](https://gofastmcp.com/deployment/server-configuration#file-structure)

File Structure
-------------------------------------------------------------------------------------------

The `fastmcp.json` configuration answers three fundamental questions about your server:

*   **Source** = WHERE does your server code live?
*   **Environment** = WHAT environment setup does it require?
*   **Deployment** = HOW should the server run?

This conceptual model helps you understand the purpose of each configuration section and organize your settings effectively. The configuration file maps directly to these three concerns:

Copy

    {
      "$schema": "https://gofastmcp.com/public/schemas/fastmcp.json/v1.json",
      "source": {
        // WHERE: Location of your server code
        "type": "filesystem",  // Optional, defaults to "filesystem"
        "path": "server.py",
        "entrypoint": "mcp"
      },
      "environment": {
        // WHAT: Environment setup and dependencies
        "type": "uv",  // Optional, defaults to "uv"
        "python": ">=3.10",
        "dependencies": ["pandas", "numpy"]
      },
      "deployment": {
        // HOW: Runtime configuration
        "transport": "stdio",
        "log_level": "INFO"
      }
    }
    

Only the `source` field is required. The `environment` and `deployment` sections are optional and provide additional configuration when needed.

### 

[​](https://gofastmcp.com/deployment/server-configuration#json-schema-support)

JSON Schema Support

FastMCP provides JSON schemas for IDE autocomplete and validation. Add the schema reference to your `fastmcp.json` for enhanced developer experience:

Copy

    {
      "$schema": "https://gofastmcp.com/public/schemas/fastmcp.json/v1.json",
      "source": {
        "path": "server.py",
        "entrypoint": "mcp"
      }
    }
    

Two schema URLs are available:

*   **Version-specific**: `https://gofastmcp.com/public/schemas/fastmcp.json/v1.json`
*   **Latest version**: `https://gofastmcp.com/public/schemas/fastmcp.json/latest.json`

Modern IDEs like VS Code will automatically provide autocomplete suggestions, validation, and inline documentation when the schema is specified.

### 

[​](https://gofastmcp.com/deployment/server-configuration#source-configuration)

Source Configuration

The source configuration determines **WHERE** your server code lives. It tells FastMCP how to find and load your server, whether it’s a local Python file, a remote repository, or hosted in the cloud. This section is required and forms the foundation of your configuration.

Source
------

[​](https://gofastmcp.com/deployment/server-configuration#param-source)

source

object

required

The server source configuration that determines where your server code lives.

[​](https://gofastmcp.com/deployment/server-configuration#param-type)

type

string

default:"filesystem"

The source type identifier that determines which implementation to use. Currently supports `"filesystem"` for local files. Future releases will add support for `"git"` and `"cloud"` source types.

Show FileSystemSource

When `type` is `"filesystem"` (or omitted), the source points to a local Python file containing your FastMCP server:

[​](https://gofastmcp.com/deployment/server-configuration#param-path)

path

string

required

Path to the Python file containing your FastMCP server.

[​](https://gofastmcp.com/deployment/server-configuration#param-entrypoint)

entrypoint

string

Name of the server instance or factory function within the module:

*   Can be a FastMCP server instance (e.g., `mcp = FastMCP("MyServer")`)
*   Can be a function with no arguments that returns a FastMCP server
*   If not specified, FastMCP searches for common names: `mcp`, `server`, or `app`

**Example:**

Copy

    "source": {
      "type": "filesystem",
      "path": "src/server.py",
      "entrypoint": "mcp"
    }
    

Note: File paths are resolved relative to the configuration file’s location.

**Future Source Types**Future releases will support additional source types:

*   **Git repositories** (`type: "git"`) for loading server code directly from version control
*   **FastMCP Cloud** (`type: "cloud"`) for hosted servers with automatic scaling and management

### 

[​](https://gofastmcp.com/deployment/server-configuration#environment-configuration)

Environment Configuration

The environment configuration determines **WHAT** environment setup your server requires. It controls the build-time setup of your Python environment, ensuring your server runs with the exact Python version and dependencies it requires. This section creates isolated, reproducible environments across different systems. FastMCP uses an extensible environment system with a base `Environment` class that can be implemented by different environment providers. Currently, FastMCP supports the `UVEnvironment` for Python environment management using `uv`’s powerful dependency resolver.

Environment
-----------

[​](https://gofastmcp.com/deployment/server-configuration#param-environment)

environment

object

Optional environment configuration. When specified, FastMCP uses the appropriate environment implementation to set up your server’s runtime.

[​](https://gofastmcp.com/deployment/server-configuration#param-type-1)

type

string

default:"uv"

The environment type identifier that determines which implementation to use. Currently supports `"uv"` for Python environments managed by uv. If omitted, defaults to `"uv"`.

Show UVEnvironment

When `type` is `"uv"` (or omitted), the environment uses uv to manage Python dependencies:

[​](https://gofastmcp.com/deployment/server-configuration#param-python)

python

string

Python version constraint. Examples:

*   Exact version: `"3.12"`
*   Minimum version: `">=3.10"`
*   Version range: `">=3.10,<3.13"`

[​](https://gofastmcp.com/deployment/server-configuration#param-dependencies)

dependencies

list\[str\]

List of pip packages with optional version specifiers (PEP 508 format).

Copy

    "dependencies": ["pandas>=2.0", "requests", "httpx"]
    

[​](https://gofastmcp.com/deployment/server-configuration#param-requirements)

requirements

string

Path to a requirements.txt file, resolved relative to the config file location.

Copy

    "requirements": "requirements.txt"
    

[​](https://gofastmcp.com/deployment/server-configuration#param-project)

project

string

Path to a project directory containing pyproject.toml for uv project management.

Copy

    "project": "."
    

[​](https://gofastmcp.com/deployment/server-configuration#param-editable)

editable

list\[string\]

List of paths to packages to install in editable/development mode. Useful for local development when you want changes to be reflected immediately. Supports multiple packages for monorepo setups or shared libraries.

Copy

    "editable": ["."]
    

Or with multiple packages:

Copy

    "editable": [".", "../shared-lib", "/path/to/another-package"]
    

**Example:**

Copy

    "environment": {
      "type": "uv",
      "python": ">=3.10",
      "dependencies": ["pandas", "numpy"],
      "editable": ["."]
    }
    

Note: When any UVEnvironment field is specified, FastMCP automatically creates an isolated environment using `uv` before running your server.

When environment configuration is provided, FastMCP:

1.  Detects the environment type (defaults to `"uv"` if not specified)
2.  Creates an isolated environment using the appropriate provider
3.  Installs the specified dependencies
4.  Runs your server in this clean environment

This build-time setup ensures your server always has the dependencies it needs, without polluting your system Python or conflicting with other projects.

**Future Environment Types**Similar to source types, future releases may support additional environment types for different runtime requirements, such as Docker containers or language-specific environments beyond Python.

### 

[​](https://gofastmcp.com/deployment/server-configuration#deployment-configuration)

Deployment Configuration

The deployment configuration controls **HOW** your server runs. It defines the runtime behavior including network settings, environment variables, and execution context. These settings determine how your server operates when it executes, from transport protocols to logging levels. Environment variables are included in this section because they’re runtime configuration that affects how your server behaves when it executes, not how its environment is built. The deployment configuration is applied every time your server starts, controlling its operational characteristics.

Deployment Fields
-----------------

[​](https://gofastmcp.com/deployment/server-configuration#param-deployment)

deployment

object

Optional runtime configuration for the server.Show Deployment Fields

[​](https://gofastmcp.com/deployment/server-configuration#param-transport)

transport

string

default:"stdio"

Protocol for client communication:

*   `"stdio"`: Standard input/output for desktop clients
*   `"http"`: Network-accessible HTTP server
*   `"sse"`: Server-sent events

[​](https://gofastmcp.com/deployment/server-configuration#param-host)

host

string

default:"127.0.0.1"

Network interface to bind (HTTP transport only):

*   `"127.0.0.1"`: Local connections only
*   `"0.0.0.0"`: All network interfaces

[​](https://gofastmcp.com/deployment/server-configuration#param-port)

port

integer

default:"3000"

Port number for HTTP transport.

[​](https://gofastmcp.com/deployment/server-configuration#param-path-1)

path

string

default:"/mcp/"

URL path for the MCP endpoint when using HTTP transport.

[​](https://gofastmcp.com/deployment/server-configuration#param-log-level)

log\_level

string

default:"INFO"

Server logging verbosity. Options:

*   `"DEBUG"`: Detailed debugging information
*   `"INFO"`: General informational messages
*   `"WARNING"`: Warning messages
*   `"ERROR"`: Error messages only
*   `"CRITICAL"`: Critical errors only

[​](https://gofastmcp.com/deployment/server-configuration#param-env)

env

object

Environment variables to set when running the server. Supports `${VAR_NAME}` syntax for runtime interpolation.

Copy

    "env": {
      "API_KEY": "secret-key",
      "DATABASE_URL": "postgres://${DB_USER}@${DB_HOST}/mydb"
    }
    

[​](https://gofastmcp.com/deployment/server-configuration#param-cwd)

cwd

string

Working directory for the server process. Relative paths are resolved from the config file location.

[​](https://gofastmcp.com/deployment/server-configuration#param-args)

args

list\[str\]

Command-line arguments to pass to the server, passed after `--` to the server’s argument parser.

Copy

    "args": ["--config", "server-config.json"]

#### 

[​](https://gofastmcp.com/deployment/server-configuration#environment-variable-interpolation)

Environment Variable Interpolation

The `env` field in deployment configuration supports runtime interpolation of environment variables using `${VAR_NAME}` syntax. This enables dynamic configuration based on your deployment environment:

Copy

    {
      "deployment": {
        "env": {
          "API_URL": "https://api.${ENVIRONMENT}.example.com",
          "DATABASE_URL": "postgres://${DB_USER}:${DB_PASS}@${DB_HOST}/myapp",
          "CACHE_KEY": "myapp_${ENVIRONMENT}_${VERSION}"
        }
      }
    }
    

When the server starts, FastMCP replaces `${ENVIRONMENT}`, `${DB_USER}`, etc. with values from your system’s environment variables. If a variable doesn’t exist, the placeholder is preserved as-is. **Example**: If your system has `ENVIRONMENT=production` and `DB_HOST=db.example.com`:

Copy

    // Configuration
    {
      "deployment": {
        "env": {
          "API_URL": "https://api.${ENVIRONMENT}.example.com",
          "DB_HOST": "${DB_HOST}"
        }
      }
    }
    
    // Result at runtime
    {
      "API_URL": "https://api.production.example.com",
      "DB_HOST": "db.example.com"
    }
    

This feature is particularly useful for:

*   Deploying the same configuration across development, staging, and production
*   Keeping sensitive values out of configuration files
*   Building dynamic URLs and connection strings
*   Creating environment-specific prefixes or suffixes

[​](https://gofastmcp.com/deployment/server-configuration#usage-with-cli-commands)

Usage with CLI Commands
-------------------------------------------------------------------------------------------------------------

FastMCP automatically detects and uses a file specifically named `fastmcp.json` in the current directory, making server execution simple and consistent. Files with FastMCP configuration format but different names are not auto-detected and must be specified explicitly:

Copy

    # Auto-detect fastmcp.json in current directory
    cd my-project
    fastmcp run  # No arguments needed!
    
    # Or specify a configuration file explicitly
    fastmcp run prod.fastmcp.json
    
    # Skip environment setup when already in a uv environment
    fastmcp run fastmcp.json --skip-env
    
    # Skip source preparation when source is already prepared
    fastmcp run fastmcp.json --skip-source
    
    # Skip both environment and source preparation
    fastmcp run fastmcp.json --skip-env --skip-source
    

### 

[​](https://gofastmcp.com/deployment/server-configuration#pre-building-environments)

Pre-building Environments

You can use `fastmcp project prepare` to create a persistent uv project with all dependencies pre-installed:

Copy

    # Create a persistent environment
    fastmcp project prepare fastmcp.json --output-dir ./env
    
    # Use the pre-built environment to run the server
    fastmcp run fastmcp.json --project ./env
    

This pattern separates environment setup (slow) from server execution (fast), useful for deployment scenarios.

### 

[​](https://gofastmcp.com/deployment/server-configuration#using-an-existing-environment)

Using an Existing Environment

By default, FastMCP creates an isolated environment with `uv` based on your configuration. When you already have a suitable Python environment, use the `--skip-env` flag to skip environment creation:

Copy

    fastmcp run fastmcp.json --skip-env
    

**When you already have an environment:**

*   You’re in an activated virtual environment with all dependencies installed
*   You’re inside a Docker container with pre-installed dependencies
*   You’re in a CI/CD pipeline that pre-builds the environment
*   You’re using a system-wide installation with all required packages
*   You’re in a uv-managed environment (prevents infinite recursion)

This flag tells FastMCP: “I already have everything installed, just run the server.”

### 

[​](https://gofastmcp.com/deployment/server-configuration#using-an-existing-source)

Using an Existing Source

When working with source types that require preparation (future support for git repositories or cloud sources), use the `--skip-source` flag when you already have the source code available:

Copy

    fastmcp run fastmcp.json --skip-source
    

**When you already have the source:**

*   You’ve previously cloned a git repository and don’t need to re-fetch
*   You have a cached copy of a cloud-hosted server
*   You’re in a CI/CD pipeline where source checkout is a separate step
*   You’re iterating locally on already-downloaded code

This flag tells FastMCP: “I already have the source code, skip any download/clone steps.” Note: For filesystem sources (local Python files), this flag has no effect since they don’t require preparation. The configuration file works with all FastMCP commands:

*   **`run`** - Start the server in production mode
*   **`dev`** - Launch with the Inspector UI for development
*   **`inspect`** - View server capabilities and configuration
*   **`install`** - Install to Claude Desktop, Cursor, or other MCP clients

When no file argument is provided, FastMCP searches the current directory for `fastmcp.json`. This means you can simply navigate to your project directory and run `fastmcp run` to start your server with all its configured settings.

### 

[​](https://gofastmcp.com/deployment/server-configuration#cli-override-behavior)

CLI Override Behavior

Command-line arguments take precedence over configuration file values, allowing ad-hoc adjustments without modifying the file:

Copy

    # Config specifies port 3000, CLI overrides to 8080
    fastmcp run fastmcp.json --port 8080
    
    # Config specifies stdio, CLI overrides to HTTP
    fastmcp run fastmcp.json --transport http
    
    # Add extra dependencies not in config
    fastmcp run fastmcp.json --with requests --with httpx
    

This precedence order enables:

*   Quick testing of different settings
*   Environment-specific overrides in deployment scripts
*   Debugging with increased log levels
*   Temporary configuration changes

### 

[​](https://gofastmcp.com/deployment/server-configuration#custom-naming-patterns)

Custom Naming Patterns

You can use different configuration files for different environments:

*   `fastmcp.json` - Default configuration
*   `dev.fastmcp.json` - Development settings
*   `prod.fastmcp.json` - Production settings
*   `test_fastmcp.json` - Test configuration

Any file with “fastmcp.json” in the name is recognized as a configuration file.

[​](https://gofastmcp.com/deployment/server-configuration#examples)

Examples
-------------------------------------------------------------------------------

*   Basic Configuration
    
*   Development Configuration
    
*   Production Configuration
    
*   Data Science Server
    
*   Multi-Environment Setup
    

A minimal configuration for a simple server:

Copy

    {
      "$schema": "https://gofastmcp.com/public/schemas/fastmcp.json/v1.json",
      "source": {
        "path": "server.py",
        "entrypoint": "mcp"
      }
    }
    

This configuration explicitly specifies the server entrypoint (`mcp`), making it clear which server instance or factory function to use. Uses all defaults: STDIO transport, no special dependencies, standard logging.

[​](https://gofastmcp.com/deployment/server-configuration#migrating-from-cli-arguments)

Migrating from CLI Arguments
-----------------------------------------------------------------------------------------------------------------------

If you’re currently using command-line arguments or shell scripts, migrating to `fastmcp.json` simplifies your workflow. Here’s how common CLI patterns map to configuration: **CLI Command**:

Copy

    uv run --with pandas --with requests \
      fastmcp run server.py \
      --transport http \
      --port 8000 \
      --log-level INFO
    

**Equivalent fastmcp.json**:

Copy

    {
      "$schema": "https://gofastmcp.com/public/schemas/fastmcp.json/v1.json",
      "source": {
        "path": "server.py",
        "entrypoint": "mcp"
      },
      "environment": {
        "dependencies": ["pandas", "requests"]
      },
      "deployment": {
        "transport": "http",
        "port": 8000,
        "log_level": "INFO"
      }
    }
    

Now simply run:

Copy

    fastmcp run  # Automatically finds and uses fastmcp.json
    

The configuration file approach provides better documentation, easier sharing, and consistent execution across different environments while maintaining the flexibility to override settings when needed.

[FastMCP Cloud\
\
Previous](https://gofastmcp.com/deployment/fastmcp-cloud)
[The FastMCP Client\
\
Next](https://gofastmcp.com/clients/client)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.