---
url: https://gofastmcp.com/deployment/fastmcp-cloud
title: FastMCP Cloud - FastMCP
description: The fastest way to deploy your MCP server
scraped_at: 2025-11-03T18:42:03.467978
---

[Skip to main content](https://gofastmcp.com/deployment/fastmcp-cloud#content-area)

Join the [FastMCP community](https://discord.gg/uu8dJCgttd)
!

[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)

Search...

Navigation

Deployment

FastMCP Cloud

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

*   [Prerequisites](https://gofastmcp.com/deployment/fastmcp-cloud#prerequisites)
    
*   [Getting Started](https://gofastmcp.com/deployment/fastmcp-cloud#getting-started)
    
*   [Step 1: Create a Project](https://gofastmcp.com/deployment/fastmcp-cloud#step-1%3A-create-a-project)
    
*   [Step 2: Deploy Your Server](https://gofastmcp.com/deployment/fastmcp-cloud#step-2%3A-deploy-your-server)
    
*   [Step 3: Connect to Your Server](https://gofastmcp.com/deployment/fastmcp-cloud#step-3%3A-connect-to-your-server)
    

[FastMCP Cloud](https://fastmcp.cloud/)
 is a managed platform for hosting MCP servers, built by the FastMCP team. While the FastMCP framework will always be fully open-source, we created FastMCP Cloud to solve the deployment challenges we’ve seen developers face. Our goal is to provide the absolute fastest way to make your MCP server available to LLM clients like Claude and Cursor. FastMCP Cloud is a young product and we welcome your feedback. Please join our [Discord](https://discord.com/invite/aGsSC3yDF4)
 to share your thoughts and ideas, and you can expect to see new features and improvements every week.

FastMCP Cloud supports both **FastMCP 2.0** servers and also **FastMCP 1.0** servers that were created with the official MCP Python SDK.

FastMCP Cloud is completely free while in beta!

[​](https://gofastmcp.com/deployment/fastmcp-cloud#prerequisites)

Prerequisites
----------------------------------------------------------------------------------

To use FastMCP Cloud, you’ll need a [GitHub](https://github.com/)
 account. In addition, you’ll need a GitHub repo that contains a FastMCP server instance. If you don’t want to create one yet, you can proceed to [step 1](https://gofastmcp.com/deployment/fastmcp-cloud#step-1-create-a-project)
 and use the FastMCP Cloud quickstart repo. Your repo can be public or private, but must include at least a Python file that contains a FastMCP server instance.

To ensure your file is compatible with FastMCP Cloud, you can run `fastmcp inspect <file.py:server_object>` to see what FastMCP Cloud will see when it runs your server.

If you have a `requirements.txt` or `pyproject.toml` in the repo, FastMCP Cloud will automatically detect your server’s dependencies and install them for you. Note that your file _can_ have an `if __name__ == "__main__"` block, but it will be ignored by FastMCP Cloud. For example, a minimal server file might look like:

Copy

    from fastmcp import FastMCP
    
    mcp = FastMCP("MyServer")
    
    @mcp.tool
    def hello(name: str) -> str:
        return f"Hello, {name}!"
    

[​](https://gofastmcp.com/deployment/fastmcp-cloud#getting-started)

Getting Started
--------------------------------------------------------------------------------------

There are just three steps to deploying a server to FastMCP Cloud:

### 

[​](https://gofastmcp.com/deployment/fastmcp-cloud#step-1%3A-create-a-project)

Step 1: Create a Project

Visit [fastmcp.cloud](https://fastmcp.cloud/)
 and sign in with your GitHub account. Then, create a project. Each project corresponds to a GitHub repo, and you can create one from either your own repo or using the FastMCP Cloud quickstart repo.

![FastMCP Cloud Quickstart Screen](https://mintcdn.com/fastmcp/hUosZw7ujHZFemrG/assets/images/fastmcp_cloud/quickstart.png?w=2500&fit=max&auto=format&n=hUosZw7ujHZFemrG&q=85&s=b2320ef39fff5ff3a00d5c09787fefc8)

Next, you’ll be prompted to configure your project.

![FastMCP Cloud Configuration Screen](https://mintcdn.com/fastmcp/hUosZw7ujHZFemrG/assets/images/fastmcp_cloud/create_project.png?w=2500&fit=max&auto=format&n=hUosZw7ujHZFemrG&q=85&s=51b9fa2763dc5064c1eef4f8f90af77a)

The configuration screen lets you specify:

*   **Name**: The name of your project. This will be used to generate a unique URL for your server.
*   **Entrypoint**: The Python file containing your FastMCP server (e.g., `echo.py`). This field has the same syntax as the `fastmcp run` command, for example `echo.py:my_server` to specify a specific object in the file.
*   **Authentication**: If disabled, your server is open to the public. If enabled, only other members of your FastMCP Cloud organization will be able to connect.

Note that FastMCP Cloud will automatically detect yours server’s Python dependencies from either a `requirements.txt` or `pyproject.toml` file.

### 

[​](https://gofastmcp.com/deployment/fastmcp-cloud#step-2%3A-deploy-your-server)

Step 2: Deploy Your Server

Once you configure your project, FastMCP Cloud will:

1.  Clone the repository
2.  Build your FastMCP server
3.  Deploy it to a unique URL
4.  Make it immediately available for connections

![FastMCP Cloud Deployment Screen](https://mintcdn.com/fastmcp/hUosZw7ujHZFemrG/assets/images/fastmcp_cloud/deployment.png?w=2500&fit=max&auto=format&n=hUosZw7ujHZFemrG&q=85&s=f6b3a204d808cad20b40f200e2e40d7a)

FastMCP Cloud will monitor your repo and redeploy your server whenever you push a change to the `main` branch. In addition, FastMCP Cloud will build and deploy servers for every PR your open, hosting them on unique URLs, so you can test changes before updating your production server.

### 

[​](https://gofastmcp.com/deployment/fastmcp-cloud#step-3%3A-connect-to-your-server)

Step 3: Connect to Your Server

Once your server is deployed, it will be accessible at a URL like:

Copy

    https://your-project-name.fastmcp.app/mcp
    

You should be able to connect to it as soon as you see the deployment succeed! FastMCP Cloud provides instant connection options for popular LLM clients:

![FastMCP Cloud Connection Screen](https://mintcdn.com/fastmcp/hUosZw7ujHZFemrG/assets/images/fastmcp_cloud/connect.png?w=2500&fit=max&auto=format&n=hUosZw7ujHZFemrG&q=85&s=fb9b2640011b3757a9a0cdcb4b4449c4)

[HTTP Deployment\
\
Previous](https://gofastmcp.com/deployment/http)
[Project Configuration\
\
Next](https://gofastmcp.com/deployment/server-configuration)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.

![FastMCP Cloud Quickstart Screen](https://mintcdn.com/fastmcp/hUosZw7ujHZFemrG/assets/images/fastmcp_cloud/quickstart.png?w=2500&fit=max&auto=format&n=hUosZw7ujHZFemrG&q=85&s=b2320ef39fff5ff3a00d5c09787fefc8)

![FastMCP Cloud Configuration Screen](https://mintcdn.com/fastmcp/hUosZw7ujHZFemrG/assets/images/fastmcp_cloud/create_project.png?w=2500&fit=max&auto=format&n=hUosZw7ujHZFemrG&q=85&s=51b9fa2763dc5064c1eef4f8f90af77a)

![FastMCP Cloud Deployment Screen](https://mintcdn.com/fastmcp/hUosZw7ujHZFemrG/assets/images/fastmcp_cloud/deployment.png?w=2500&fit=max&auto=format&n=hUosZw7ujHZFemrG&q=85&s=f6b3a204d808cad20b40f200e2e40d7a)

![FastMCP Cloud Connection Screen](https://mintcdn.com/fastmcp/hUosZw7ujHZFemrG/assets/images/fastmcp_cloud/connect.png?w=2500&fit=max&auto=format&n=hUosZw7ujHZFemrG&q=85&s=fb9b2640011b3757a9a0cdcb4b4449c4)