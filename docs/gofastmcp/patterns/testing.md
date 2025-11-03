---
url: https://gofastmcp.com/patterns/testing
title: Testing your FastMCP Server - FastMCP
description: How to test your FastMCP server.
scraped_at: 2025-11-03T18:42:21.361950
---

[Skip to main content](https://gofastmcp.com/patterns/testing#content-area)

Join the [FastMCP community](https://discord.gg/uu8dJCgttd)
!

[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)

Search...

Navigation

Patterns

Testing your FastMCP Server

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
    

The best way to ensure a reliable and maintainable FastMCP Server is to test it! The FastMCP Client combined with Pytest provides a simple and powerful way to test your FastMCP servers. Using Pytest Fixtures, you can wrap your FastMCP Server in a Client instance that makes interacting with your server fast and easy. This is especially useful when building your own MCP Servers and enables a tight development loop by allowing you to avoid using a separate tool like MCP Inspector during development:

Copy

    import pytest
    from fastmcp.client import Client
    from fastmcp.client.transports import FastMCPTransport
    
    from my_project.main import mcp
    
    @pytest.fixture
    async def main_mcp_client():
        async with Client(transport=mcp) as mcp_client:
            yield mcp_client
    
    async def test_list_tools(main_mcp_client: Client[FastMCPTransport]):
        list_tools = await main_mcp_client.list_tools()
    
        assert len(list_tools) == 5
    

We recommend the [inline-snapshot library](https://github.com/15r10nk/inline-snapshot)
 for asserting complex data structures coming from your MCP Server. This library allows you to write tests that are easy to read and understand, and are also easy to update when the data structure changes.

Copy

    from inline_snapshot import snapshot
    
    async def test_list_tools(main_mcp_client: Client[FastMCPTransport]):
        list_tools = await main_mcp_client.list_tools()
    
        assert list_tools == snapshot()
    

Simply run `pytest --inline-snapshot=fix,create` to fill in the `snapshot()` with actual data.

For values that change you can leverage the [dirty-equals](https://github.com/samuelcolvin/dirty-equals)
 library to perform flexible equality assertions on dynamic or non-deterministic values.

Using the pytest `parametrize` decorator, you can easily test your tools with a wide variety of inputs.

Copy

    import pytest
    from my_project.main import mcp
    
    from fastmcp.client import Client
    from fastmcp.client.transports import FastMCPTransport
    @pytest.fixture
    async def main_mcp_client():
        async with Client(mcp) as client:
            yield client
    
    
    @pytest.mark.parametrize(
        "first_number, second_number, expected",
        [\
            (1, 2, 3),\
            (2, 3, 5),\
            (3, 4, 7),\
        ],
    )
    async def test_add(
        first_number: int,
        second_number: int,
        expected: int,
        main_mcp_client: Client[FastMCPTransport],
    ):
        result = await main_mcp_client.call_tool(
            name="add", arguments={"x": first_number, "y": second_number}
        )
        assert result.data is not None
        assert isinstance(result.data, int)
        assert result.data == expected
    

The [FastMCP Repository contains thousands of tests](https://github.com/jlowin/fastmcp/tree/main/tests)
 for the FastMCP Client and Server. Everything from connecting to remote MCP servers, to testing tools, resources, and prompts is covered, take a look for inspiration!

[Contrib Modules\
\
Previous](https://gofastmcp.com/patterns/contrib)
[Contributing\
\
Next](https://gofastmcp.com/development/contributing)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.