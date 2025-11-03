---
url: https://gofastmcp.com/integrations/chatgpt
title: ChatGPT 🤝 FastMCP - FastMCP
description: Connect FastMCP servers to ChatGPT in Chat and Deep Research modes
scraped_at: 2025-11-03T18:42:10.294385
---

[Skip to main content](https://gofastmcp.com/integrations/chatgpt#content-area)

Join the [FastMCP community](https://discord.gg/uu8dJCgttd)
!

[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)

Search...

Navigation

AI Assistants

ChatGPT 🤝 FastMCP

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

*   [Build a Server](https://gofastmcp.com/integrations/chatgpt#build-a-server)
    
*   [Deploy Your Server](https://gofastmcp.com/integrations/chatgpt#deploy-your-server)
    
*   [Chat Mode](https://gofastmcp.com/integrations/chatgpt#chat-mode)
    
*   [Add to ChatGPT](https://gofastmcp.com/integrations/chatgpt#add-to-chatgpt)
    
*   [1\. Enable Developer Mode](https://gofastmcp.com/integrations/chatgpt#1-enable-developer-mode)
    
*   [2\. Create Connector](https://gofastmcp.com/integrations/chatgpt#2-create-connector)
    
*   [3\. Use in Chat](https://gofastmcp.com/integrations/chatgpt#3-use-in-chat)
    
*   [Skip Confirmations](https://gofastmcp.com/integrations/chatgpt#skip-confirmations)
    
*   [Deep Research Mode](https://gofastmcp.com/integrations/chatgpt#deep-research-mode)
    
*   [Tool Implementation](https://gofastmcp.com/integrations/chatgpt#tool-implementation)
    
*   [Using Deep Research](https://gofastmcp.com/integrations/chatgpt#using-deep-research)
    

ChatGPT supports MCP servers through remote HTTP connections in two modes: **Chat mode** for interactive conversations and **Deep Research mode** for comprehensive information retrieval.

**Developer Mode Required for Chat Mode**: To use MCP servers in regular ChatGPT conversations, you must first enable Developer Mode in your ChatGPT settings. This feature is available for ChatGPT Pro, Team, Enterprise, and Edu users.

OpenAI’s official MCP documentation and examples are built with **FastMCP v2**! Learn more from their [MCP documentation](https://platform.openai.com/docs/mcp)
 and [Developer Mode guide](https://platform.openai.com/docs/guides/developer-mode)
.

[​](https://gofastmcp.com/integrations/chatgpt#build-a-server)

Build a Server
--------------------------------------------------------------------------------

First, let’s create a simple FastMCP server:

server.py

Copy

    from fastmcp import FastMCP
    import random
    
    mcp = FastMCP("Demo Server")
    
    @mcp.tool
    def roll_dice(sides: int = 6) -> int:
        """Roll a dice with the specified number of sides."""
        return random.randint(1, sides)
    
    if __name__ == "__main__":
        mcp.run(transport="http", port=8000)
    

### 

[​](https://gofastmcp.com/integrations/chatgpt#deploy-your-server)

Deploy Your Server

Your server must be accessible from the internet. For development, use `ngrok`:

Terminal 1

Terminal 2

Copy

    python server.py
    

Note your public URL (e.g., `https://abc123.ngrok.io`) for the next steps.

[​](https://gofastmcp.com/integrations/chatgpt#chat-mode)

Chat Mode
----------------------------------------------------------------------

Chat mode lets you use MCP tools directly in ChatGPT conversations. See [OpenAI’s Developer Mode guide](https://platform.openai.com/docs/guides/developer-mode)
 for the latest requirements.

### 

[​](https://gofastmcp.com/integrations/chatgpt#add-to-chatgpt)

Add to ChatGPT

#### 

[​](https://gofastmcp.com/integrations/chatgpt#1-enable-developer-mode)

1\. Enable Developer Mode

1.  Open ChatGPT and go to **Settings** → **Connectors**
2.  Under **Advanced**, toggle **Developer Mode** to enabled

#### 

[​](https://gofastmcp.com/integrations/chatgpt#2-create-connector)

2\. Create Connector

1.  In **Settings** → **Connectors**, click **Create**
2.  Enter:
    *   **Name**: Your server name
    *   **Server URL**: `https://your-server.ngrok.io/mcp/`
3.  Check **I trust this provider**
4.  Add authentication if needed
5.  Click **Create**

**Without Developer Mode**: If you don’t have search/fetch tools, ChatGPT will reject the server. With Developer Mode enabled, you don’t need search/fetch tools for Chat mode.

#### 

[​](https://gofastmcp.com/integrations/chatgpt#3-use-in-chat)

3\. Use in Chat

1.  Start a new chat
2.  Click the **+** button → **More** → **Developer Mode**
3.  **Enable your MCP server connector** (required - the connector must be explicitly added to each chat)
4.  Now you can use your tools:

Example usage:

*   “Roll a 20-sided dice”
*   “Roll dice” (uses default 6 sides)

The connector must be explicitly enabled in each chat session through Developer Mode. Once added, it remains active for the entire conversation.

### 

[​](https://gofastmcp.com/integrations/chatgpt#skip-confirmations)

Skip Confirmations

Use `annotations={"readOnlyHint": True}` to skip confirmation prompts for read-only tools:

Copy

    @mcp.tool(annotations={"readOnlyHint": True})
    def get_status() -> str:
        """Check system status."""
        return "All systems operational"
    
    @mcp.tool()  # No annotation - ChatGPT may ask for confirmation
    def delete_item(id: str) -> str:
        """Delete an item."""
        return f"Deleted {id}"
    

[​](https://gofastmcp.com/integrations/chatgpt#deep-research-mode)

Deep Research Mode
----------------------------------------------------------------------------------------

Deep Research mode provides systematic information retrieval with citations. See [OpenAI’s MCP documentation](https://platform.openai.com/docs/mcp)
 for the latest Deep Research specifications.

**Search and Fetch Required**: Without Developer Mode, ChatGPT will reject any server that doesn’t have both `search` and `fetch` tools. Even in Developer Mode, Deep Research only uses these two tools.

### 

[​](https://gofastmcp.com/integrations/chatgpt#tool-implementation)

Tool Implementation

Deep Research tools must follow this pattern:

Copy

    @mcp.tool()
    def search(query: str) -> dict:
        """
        Search for records matching the query.
        Must return {"ids": [list of string IDs]}
        """
        # Your search logic
        matching_ids = ["id1", "id2", "id3"]
        return {"ids": matching_ids}
    
    @mcp.tool()
    def fetch(id: str) -> dict:
        """
        Fetch a complete record by ID.
        Return the full record data for ChatGPT to analyze.
        """
        # Your fetch logic
        return {
            "id": id,
            "title": "Record Title",
            "content": "Full record content...",
            "metadata": {"author": "Jane Doe", "date": "2024"}
        }
    

### 

[​](https://gofastmcp.com/integrations/chatgpt#using-deep-research)

Using Deep Research

1.  Ensure your server is added to ChatGPT’s connectors (same as Chat mode)
2.  Start a new chat
3.  Click **+** → **Deep Research**
4.  Select your MCP server as a source
5.  Ask research questions

ChatGPT will use your `search` and `fetch` tools to find and cite relevant information.

[Permit.io Authorization 🤝 FastMCP\
\
Previous](https://gofastmcp.com/integrations/permit)
[Claude Code 🤝 FastMCP\
\
Next](https://gofastmcp.com/integrations/claude-code)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.