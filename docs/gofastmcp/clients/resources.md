---
url: https://gofastmcp.com/clients/resources
title: Resource Operations - FastMCP
description: Access static and templated resources from MCP servers.
scraped_at: 2025-11-03T18:42:02.700181
---

[Skip to main content](https://gofastmcp.com/clients/resources#content-area)

Join the [FastMCP community](https://discord.gg/uu8dJCgttd)
!

[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)

Search...

Navigation

Core Operations

Resource Operations

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
    
    *   [Tools](https://gofastmcp.com/clients/tools)
        
    *   [Resources](https://gofastmcp.com/clients/resources)
        
    *   [Prompts](https://gofastmcp.com/clients/prompts)
        
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

*   [Types of Resources](https://gofastmcp.com/clients/resources#types-of-resources)
    
*   [Listing Resources](https://gofastmcp.com/clients/resources#listing-resources)
    
*   [Static Resources](https://gofastmcp.com/clients/resources#static-resources)
    
*   [Resource Templates](https://gofastmcp.com/clients/resources#resource-templates)
    
*   [Filtering by Tags](https://gofastmcp.com/clients/resources#filtering-by-tags)
    
*   [Reading Resources](https://gofastmcp.com/clients/resources#reading-resources)
    
*   [Static Resources](https://gofastmcp.com/clients/resources#static-resources-2)
    
*   [Resource Templates](https://gofastmcp.com/clients/resources#resource-templates-2)
    
*   [Content Types](https://gofastmcp.com/clients/resources#content-types)
    
*   [Text Resources](https://gofastmcp.com/clients/resources#text-resources)
    
*   [Binary Resources](https://gofastmcp.com/clients/resources#binary-resources)
    
*   [Working with Multi-Server Clients](https://gofastmcp.com/clients/resources#working-with-multi-server-clients)
    
*   [Raw MCP Protocol Access](https://gofastmcp.com/clients/resources#raw-mcp-protocol-access)
    
*   [Common Resource URI Patterns](https://gofastmcp.com/clients/resources#common-resource-uri-patterns)
    

`` New in version: `2.0.0` `` Resources are data sources exposed by MCP servers. They can be static files or dynamic templates that generate content based on parameters.

[​](https://gofastmcp.com/clients/resources#types-of-resources)

Types of Resources
-------------------------------------------------------------------------------------

MCP servers expose two types of resources:

*   **Static Resources**: Fixed content accessible via URI (e.g., configuration files, documentation)
*   **Resource Templates**: Dynamic resources that accept parameters to generate content (e.g., API endpoints, database queries)

[​](https://gofastmcp.com/clients/resources#listing-resources)

Listing Resources
-----------------------------------------------------------------------------------

### 

[​](https://gofastmcp.com/clients/resources#static-resources)

Static Resources

Use `list_resources()` to retrieve all static resources available on the server:

Copy

    async with client:
        resources = await client.list_resources()
        # resources -> list[mcp.types.Resource]
        
        for resource in resources:
            print(f"Resource URI: {resource.uri}")
            print(f"Name: {resource.name}")
            print(f"Description: {resource.description}")
            print(f"MIME Type: {resource.mimeType}")
            # Access tags and other metadata
            if hasattr(resource, '_meta') and resource._meta:
                fastmcp_meta = resource._meta.get('_fastmcp', {})
                print(f"Tags: {fastmcp_meta.get('tags', [])}")
    

### 

[​](https://gofastmcp.com/clients/resources#resource-templates)

Resource Templates

Use `list_resource_templates()` to retrieve available resource templates:

Copy

    async with client:
        templates = await client.list_resource_templates()
        # templates -> list[mcp.types.ResourceTemplate]
        
        for template in templates:
            print(f"Template URI: {template.uriTemplate}")
            print(f"Name: {template.name}")
            print(f"Description: {template.description}")
            # Access tags and other metadata
            if hasattr(template, '_meta') and template._meta:
                fastmcp_meta = template._meta.get('_fastmcp', {})
                print(f"Tags: {fastmcp_meta.get('tags', [])}")
    

### 

[​](https://gofastmcp.com/clients/resources#filtering-by-tags)

Filtering by Tags

`` New in version: `2.11.0` `` You can use the `meta` field to filter resources based on their tags:

Copy

    async with client:
        resources = await client.list_resources()
        
        # Filter resources by tag
        config_resources = [\
            resource for resource in resources \
            if hasattr(resource, '_meta') and resource._meta and\
               resource._meta.get('_fastmcp', {}) and\
               'config' in resource._meta.get('_fastmcp', {}).get('tags', [])\
        ]
        
        print(f"Found {len(config_resources)} config resources")
    

The `_meta` field is part of the standard MCP specification. FastMCP servers include tags and other metadata within a `_fastmcp` namespace (e.g., `_meta._fastmcp.tags`) to avoid conflicts with user-defined metadata. This behavior can be controlled with the server’s `include_fastmcp_meta` setting - when disabled, the `_fastmcp` namespace won’t be included. Other MCP server implementations may not provide this metadata structure.

[​](https://gofastmcp.com/clients/resources#reading-resources)

Reading Resources
-----------------------------------------------------------------------------------

### 

[​](https://gofastmcp.com/clients/resources#static-resources-2)

Static Resources

Read a static resource using its URI:

Copy

    async with client:
        # Read a static resource
        content = await client.read_resource("file:///path/to/README.md")
        # content -> list[mcp.types.TextResourceContents | mcp.types.BlobResourceContents]
        
        # Access text content
        if hasattr(content[0], 'text'):
            print(content[0].text)
        
        # Access binary content
        if hasattr(content[0], 'blob'):
            print(f"Binary data: {len(content[0].blob)} bytes")
    

### 

[​](https://gofastmcp.com/clients/resources#resource-templates-2)

Resource Templates

Read from a resource template by providing the URI with parameters:

Copy

    async with client:
        # Read a resource generated from a template
        # For example, a template like "weather://{{city}}/current"
        weather_content = await client.read_resource("weather://london/current")
        
        # Access the generated content
        print(weather_content[0].text)  # Assuming text JSON response
    

[​](https://gofastmcp.com/clients/resources#content-types)

Content Types
---------------------------------------------------------------------------

Resources can return different content types:

### 

[​](https://gofastmcp.com/clients/resources#text-resources)

Text Resources

Copy

    async with client:
        content = await client.read_resource("resource://config/settings.json")
        
        for item in content:
            if hasattr(item, 'text'):
                print(f"Text content: {item.text}")
                print(f"MIME type: {item.mimeType}")
    

### 

[​](https://gofastmcp.com/clients/resources#binary-resources)

Binary Resources

Copy

    async with client:
        content = await client.read_resource("resource://images/logo.png")
        
        for item in content:
            if hasattr(item, 'blob'):
                print(f"Binary content: {len(item.blob)} bytes")
                print(f"MIME type: {item.mimeType}")
                
                # Save to file
                with open("downloaded_logo.png", "wb") as f:
                    f.write(item.blob)
    

[​](https://gofastmcp.com/clients/resources#working-with-multi-server-clients)

Working with Multi-Server Clients
-------------------------------------------------------------------------------------------------------------------

When using multi-server clients, resource URIs are automatically prefixed with the server name:

Copy

    async with client:  # Multi-server client
        # Access resources from different servers
        weather_icons = await client.read_resource("weather://weather/icons/sunny")
        templates = await client.read_resource("resource://assistant/templates/list")
        
        print(f"Weather icon: {weather_icons[0].blob}")
        print(f"Templates: {templates[0].text}")
    

[​](https://gofastmcp.com/clients/resources#raw-mcp-protocol-access)

Raw MCP Protocol Access
-----------------------------------------------------------------------------------------------

For access to the complete MCP protocol objects, use the `*_mcp` methods:

Copy

    async with client:
        # Raw MCP methods return full protocol objects
        resources_result = await client.list_resources_mcp()
        # resources_result -> mcp.types.ListResourcesResult
        
        templates_result = await client.list_resource_templates_mcp()
        # templates_result -> mcp.types.ListResourceTemplatesResult
        
        content_result = await client.read_resource_mcp("resource://example")
        # content_result -> mcp.types.ReadResourceResult
    

[​](https://gofastmcp.com/clients/resources#common-resource-uri-patterns)

Common Resource URI Patterns
---------------------------------------------------------------------------------------------------------

Different MCP servers may use various URI schemes:

Copy

    # File system resources
    "file:///path/to/file.txt"
    
    # Custom protocol resources  
    "weather://london/current"
    "database://users/123"
    
    # Generic resource protocol
    "resource://config/settings"
    "resource://templates/email"
    

Resource URIs and their formats depend on the specific MCP server implementation. Check the server’s documentation for available resources and their URI patterns.

[Tool Operations\
\
Previous](https://gofastmcp.com/clients/tools)
[Prompts\
\
Next](https://gofastmcp.com/clients/prompts)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.