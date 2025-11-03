---
url: https://gofastmcp.com/clients/messages
title: Message Handling - FastMCP
description: Handle MCP messages, requests, and notifications with custom message handlers.
scraped_at: 2025-11-03T18:41:58.150639
---

[Skip to main content](https://gofastmcp.com/clients/messages#content-area)

Join the [FastMCP community](https://discord.gg/uu8dJCgttd)
!

[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)

Search...

Navigation

Advanced Features

Message Handling

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

*   [Function-Based Handler](https://gofastmcp.com/clients/messages#function-based-handler)
    
*   [Message Handler Class](https://gofastmcp.com/clients/messages#message-handler-class)
    
*   [Available Handler Methods](https://gofastmcp.com/clients/messages#available-handler-methods)
    
*   [Example: Handling Tool Changes](https://gofastmcp.com/clients/messages#example%3A-handling-tool-changes)
    
*   [Handling Requests](https://gofastmcp.com/clients/messages#handling-requests)
    

`` New in version: `2.9.1` `` MCP clients can receive various types of messages from servers, including requests that need responses and notifications that don’t. The message handler provides a unified way to process all these messages.

[​](https://gofastmcp.com/clients/messages#function-based-handler)

Function-Based Handler
--------------------------------------------------------------------------------------------

The simplest way to handle messages is with a function that receives all messages:

Copy

    from fastmcp import Client
    
    async def message_handler(message):
        """Handle all MCP messages from the server."""
        if hasattr(message, 'root'):
            method = message.root.method
            print(f"Received: {method}")
            
            # Handle specific notifications
            if method == "notifications/tools/list_changed":
                print("Tools have changed - might want to refresh tool cache")
            elif method == "notifications/resources/list_changed":
                print("Resources have changed")
    
    client = Client(
        "my_mcp_server.py",
        message_handler=message_handler,
    )
    

[​](https://gofastmcp.com/clients/messages#message-handler-class)

Message Handler Class
------------------------------------------------------------------------------------------

For fine-grained targeting, FastMCP provides a `MessageHandler` class you can subclass to take advantage of specific hooks:

Copy

    from fastmcp import Client
    from fastmcp.client.messages import MessageHandler
    import mcp.types
    
    class MyMessageHandler(MessageHandler):
        async def on_tool_list_changed(
            self, notification: mcp.types.ToolListChangedNotification
        ) -> None:
            """Handle tool list changes specifically."""
            print("Tool list changed - refreshing available tools")
    
    client = Client(
        "my_mcp_server.py",
        message_handler=MyMessageHandler(),
    )
    

### 

[​](https://gofastmcp.com/clients/messages#available-handler-methods)

Available Handler Methods

All handler methods receive a single argument - the specific message type:

Message Handler Methods
-----------------------

[​](https://gofastmcp.com/clients/messages#param-on-message-message)

on\_message(message)

Any MCP message

Called for ALL messages (requests and notifications)

[​](https://gofastmcp.com/clients/messages#param-on-request-request)

on\_request(request)

mcp.types.ClientRequest

Called for requests that expect responses

[​](https://gofastmcp.com/clients/messages#param-on-notification-notification)

on\_notification(notification)

mcp.types.ServerNotification

Called for notifications (fire-and-forget)

[​](https://gofastmcp.com/clients/messages#param-on-tool-list-changed-notification)

on\_tool\_list\_changed(notification)

mcp.types.ToolListChangedNotification

Called when the server’s tool list changes

[​](https://gofastmcp.com/clients/messages#param-on-resource-list-changed-notification)

on\_resource\_list\_changed(notification)

mcp.types.ResourceListChangedNotification

Called when the server’s resource list changes

[​](https://gofastmcp.com/clients/messages#param-on-prompt-list-changed-notification)

on\_prompt\_list\_changed(notification)

mcp.types.PromptListChangedNotification

Called when the server’s prompt list changes

[​](https://gofastmcp.com/clients/messages#param-on-progress-notification)

on\_progress(notification)

mcp.types.ProgressNotification

Called for progress updates during long-running operations

[​](https://gofastmcp.com/clients/messages#param-on-logging-message-notification)

on\_logging\_message(notification)

mcp.types.LoggingMessageNotification

Called for log messages from the server

[​](https://gofastmcp.com/clients/messages#example%3A-handling-tool-changes)

Example: Handling Tool Changes
--------------------------------------------------------------------------------------------------------------

Here’s a practical example of handling tool list changes:

Copy

    from fastmcp.client.messages import MessageHandler
    import mcp.types
    
    class ToolCacheHandler(MessageHandler):
        def __init__(self):
            self.cached_tools = []
        
        async def on_tool_list_changed(
            self, notification: mcp.types.ToolListChangedNotification
        ) -> None:
            """Clear tool cache when tools change."""
            print("Tools changed - clearing cache")
            self.cached_tools = []  # Force refresh on next access
    
    client = Client("server.py", message_handler=ToolCacheHandler())
    

[​](https://gofastmcp.com/clients/messages#handling-requests)

Handling Requests
----------------------------------------------------------------------------------

While the message handler receives server-initiated requests, for most use cases you should use the dedicated callback parameters instead:

*   **Sampling requests**: Use [`sampling_handler`](https://gofastmcp.com/clients/sampling)
    
*   **Progress requests**: Use [`progress_handler`](https://gofastmcp.com/clients/progress)
    
*   **Log requests**: Use [`log_handler`](https://gofastmcp.com/clients/logging)
    

The message handler is primarily for monitoring and handling notifications rather than responding to requests.

[LLM Sampling\
\
Previous](https://gofastmcp.com/clients/sampling)
[Client Roots\
\
Next](https://gofastmcp.com/clients/roots)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.