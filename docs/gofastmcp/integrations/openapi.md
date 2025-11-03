---
url: https://gofastmcp.com/integrations/openapi
title: OpenAPI 🤝 FastMCP - FastMCP
description: Generate MCP servers from any OpenAPI specification
scraped_at: 2025-11-03T18:42:20.608327
---

[Skip to main content](https://gofastmcp.com/integrations/openapi#content-area)

Join the [FastMCP community](https://discord.gg/uu8dJCgttd)
!

[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)

Search...

Navigation

API Integration

OpenAPI 🤝 FastMCP

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
    
    *   [FastAPI](https://gofastmcp.com/integrations/fastapi)
        
    *   [OpenAPI](https://gofastmcp.com/integrations/openapi)
        

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

*   [Create a Server](https://gofastmcp.com/integrations/openapi#create-a-server)
    
*   [Authentication](https://gofastmcp.com/integrations/openapi#authentication)
    
*   [Route Mapping](https://gofastmcp.com/integrations/openapi#route-mapping)
    
*   [Custom Route Maps](https://gofastmcp.com/integrations/openapi#custom-route-maps)
    
*   [Excluding Routes](https://gofastmcp.com/integrations/openapi#excluding-routes)
    
*   [Advanced Route Mapping](https://gofastmcp.com/integrations/openapi#advanced-route-mapping)
    
*   [Customization](https://gofastmcp.com/integrations/openapi#customization)
    
*   [Component Names](https://gofastmcp.com/integrations/openapi#component-names)
    
*   [Tags](https://gofastmcp.com/integrations/openapi#tags)
    
*   [RouteMap Tags](https://gofastmcp.com/integrations/openapi#routemap-tags)
    
*   [Global Tags](https://gofastmcp.com/integrations/openapi#global-tags)
    
*   [OpenAPI Tags in Client Meta](https://gofastmcp.com/integrations/openapi#openapi-tags-in-client-meta)
    
*   [Advanced Customization](https://gofastmcp.com/integrations/openapi#advanced-customization)
    
*   [Request Parameter Handling](https://gofastmcp.com/integrations/openapi#request-parameter-handling)
    
*   [Query Parameters](https://gofastmcp.com/integrations/openapi#query-parameters)
    
*   [Path Parameters](https://gofastmcp.com/integrations/openapi#path-parameters)
    
*   [Array Parameters](https://gofastmcp.com/integrations/openapi#array-parameters)
    
*   [Headers](https://gofastmcp.com/integrations/openapi#headers)
    

`` New in version: `2.0.0` ``

**New in 2.11**: FastMCP is introducing a next-generation OpenAPI parser. The new parser has greatly improved performance and compatibility, and is also easier to maintain. To enable it, set the environment variable `FASTMCP_EXPERIMENTAL_ENABLE_NEW_OPENAPI_PARSER=true`.The new parser is largely API-compatible with the existing implementation and will become the default in a future version. We encourage all users to test it and report any issues before it becomes the default.

FastMCP can automatically generate an MCP server from any OpenAPI specification, allowing AI models to interact with existing APIs through the MCP protocol. Instead of manually creating tools and resources, you provide an OpenAPI spec and FastMCP intelligently converts API endpoints into the appropriate MCP components.

Generating MCP servers from OpenAPI is a great way to get started with FastMCP, but in practice LLMs achieve **significantly better performance** with well-designed and curated MCP servers than with auto-converted OpenAPI servers. This is especially true for complex APIs with many endpoints and parameters.We recommend using the FastAPI integration for bootstrapping and prototyping, not for mirroring your API to LLM clients. See the post [Stop Converting Your REST APIs to MCP](https://www.jlowin.dev/blog/stop-converting-rest-apis-to-mcp)
 for more details.

[​](https://gofastmcp.com/integrations/openapi#create-a-server)

Create a Server
----------------------------------------------------------------------------------

To convert an OpenAPI specification to an MCP server, use the `FastMCP.from_openapi()` class method:

server.py

Copy

    import httpx
    from fastmcp import FastMCP
    
    # Create an HTTP client for your API
    client = httpx.AsyncClient(base_url="https://api.example.com")
    
    # Load your OpenAPI spec 
    openapi_spec = httpx.get("https://api.example.com/openapi.json").json()
    
    # Create the MCP server
    mcp = FastMCP.from_openapi(
        openapi_spec=openapi_spec,
        client=client,
        name="My API Server"
    )
    
    if __name__ == "__main__":
        mcp.run()
    

### 

[​](https://gofastmcp.com/integrations/openapi#authentication)

Authentication

If your API requires authentication, configure it on the HTTP client:

Copy

    import httpx
    from fastmcp import FastMCP
    
    # Bearer token authentication
    api_client = httpx.AsyncClient(
        base_url="https://api.example.com",
        headers={"Authorization": "Bearer YOUR_TOKEN"}
    )
    
    # Create MCP server with authenticated client
    mcp = FastMCP.from_openapi(
        openapi_spec=spec, 
        client=api_client,
        timeout=30.0  # 30 second timeout for all requests
    )
    

[​](https://gofastmcp.com/integrations/openapi#route-mapping)

Route Mapping
------------------------------------------------------------------------------

By default, FastMCP converts **every endpoint** in your OpenAPI specification into an MCP **Tool**. This provides a simple, predictable starting point that ensures all your API’s functionality is immediately available to the vast majority of LLM clients which only support MCP tools. While this is a pragmatic default for maximum compatibility, you can easily customize this behavior. Internally, FastMCP uses an ordered list of `RouteMap` objects to determine how to map OpenAPI routes to various MCP component types. Each `RouteMap` specifies a combination of methods, patterns, and tags, as well as a corresponding MCP component type. Each OpenAPI route is checked against each `RouteMap` in order, and the first one that matches every criteria is used to determine its converted MCP type. A special type, `EXCLUDE`, can be used to exclude routes from the MCP server entirely.

*   **Methods**: HTTP methods to match (e.g. `["GET", "POST"]` or `"*"` for all)
*   **Pattern**: Regex pattern to match the route path (e.g. `r"^/users/.*"` or `r".*"` for all)
*   **Tags**: A set of OpenAPI tags that must all be present. An empty set (`{}`) means no tag filtering, so the route matches regardless of its tags.
*   **MCP type**: What MCP component type to create (`TOOL`, `RESOURCE`, `RESOURCE_TEMPLATE`, or `EXCLUDE`)
*   **MCP tags**: A set of custom tags to add to components created from matching routes

Here is FastMCP’s default rule:

Copy

    from fastmcp.server.openapi import RouteMap, MCPType
    
    DEFAULT_ROUTE_MAPPINGS = [\
        # All routes become tools\
        RouteMap(mcp_type=MCPType.TOOL),\
    ]
    

**Experimental Parser**: If you’re using the new parser (enabled via `FASTMCP_EXPERIMENTAL_ENABLE_NEW_OPENAPI_PARSER=true`), import from the experimental module instead:

Copy

    from fastmcp.experimental.server.openapi import RouteMap, MCPType
    

The API is identical, but the implementation provides better performance and serverless compatibility.

### 

[​](https://gofastmcp.com/integrations/openapi#custom-route-maps)

Custom Route Maps

When creating your FastMCP server, you can customize routing behavior by providing your own list of `RouteMap` objects. Your custom maps are processed before the default route maps, and routes will be assigned to the first matching custom map. For example, prior to FastMCP 2.8.0, GET requests were automatically mapped to `Resource` and `ResourceTemplate` components based on whether they had path parameters. (This was changed solely for client compatibility reasons.) You can restore this behavior by providing custom route maps:

Copy

    from fastmcp import FastMCP
    from fastmcp.server.openapi import RouteMap, MCPType
    
    # Restore pre-2.8.0 semantic mapping
    semantic_maps = [\
        # GET requests with path parameters become ResourceTemplates\
        RouteMap(methods=["GET"], pattern=r".*\{.*\}.*", mcp_type=MCPType.RESOURCE_TEMPLATE),\
        # All other GET requests become Resources\
        RouteMap(methods=["GET"], pattern=r".*", mcp_type=MCPType.RESOURCE),\
    ]
    
    mcp = FastMCP.from_openapi(
        openapi_spec=spec,
        client=client,
        route_maps=semantic_maps,
    )
    

With these maps, `GET` requests are handled semantically, and all other methods (`POST`, `PUT`, etc.) will fall through to the default rule and become `Tool`s. Here is a more complete example that uses custom route maps to convert all `GET` endpoints under `/analytics/` to tools while excluding all admin endpoints and all routes tagged “internal”. All other routes will be handled by the default rules:

Copy

    from fastmcp import FastMCP
    from fastmcp.server.openapi import RouteMap, MCPType
    
    mcp = FastMCP.from_openapi(
        openapi_spec=spec,
        client=client,
        route_maps=[\
            # Analytics `GET` endpoints are tools\
            RouteMap(\
                methods=["GET"], \
                pattern=r"^/analytics/.*", \
                mcp_type=MCPType.TOOL,\
            ),\
    \
            # Exclude all admin endpoints\
            RouteMap(\
                pattern=r"^/admin/.*", \
                mcp_type=MCPType.EXCLUDE,\
            ),\
    \
            # Exclude all routes tagged "internal"\
            RouteMap(\
                tags={"internal"},\
                mcp_type=MCPType.EXCLUDE,\
            ),\
        ],
    )
    

The default route maps are always applied after your custom maps, so you do not have to create route maps for every possible route.

### 

[​](https://gofastmcp.com/integrations/openapi#excluding-routes)

Excluding Routes

To exclude routes from the MCP server, use a route map to assign them to `MCPType.EXCLUDE`. You can use this to remove sensitive or internal routes by targeting them specifically:

Copy

    from fastmcp import FastMCP
    from fastmcp.server.openapi import RouteMap, MCPType
    
    mcp = FastMCP.from_openapi(
        openapi_spec=spec,
        client=client,
        route_maps=[\
            RouteMap(pattern=r"^/admin/.*", mcp_type=MCPType.EXCLUDE),\
            RouteMap(tags={"internal"}, mcp_type=MCPType.EXCLUDE),\
        ],
    )
    

Or you can use a catch-all rule to exclude everything that your maps don’t handle explicitly:

Copy

    from fastmcp import FastMCP
    from fastmcp.server.openapi import RouteMap, MCPType
    
    mcp = FastMCP.from_openapi(
        openapi_spec=spec,
        client=client,
        route_maps=[\
            # custom mapping logic goes here\
            # ... your specific route maps ...\
            # exclude all remaining routes\
            RouteMap(mcp_type=MCPType.EXCLUDE),\
        ],
    )
    

Using a catch-all exclusion rule will prevent the default route mappings from being applied, since it will match every remaining route. This is useful if you want to explicitly allow-list certain routes.

### 

[​](https://gofastmcp.com/integrations/openapi#advanced-route-mapping)

Advanced Route Mapping

`` New in version: `2.5.0` `` For advanced use cases that require more complex logic, you can provide a `route_map_fn` callable. After the route map logic is applied, this function is called on each matched route and its assigned MCP component type. It can optionally return a different component type to override the mapped assignment. If it returns `None`, the assigned type is used. In addition to more precise targeting of methods, patterns, and tags, this function can access any additional OpenAPI metadata about the route.

The `route_map_fn` is called on all routes, even those that matched `MCPType.EXCLUDE` in your custom maps. This gives you an opportunity to customize the mapping or even override an exclusion.

Copy

    from fastmcp import FastMCP
    from fastmcp.server.openapi import RouteMap, MCPType, HTTPRoute
    
    def custom_route_mapper(route: HTTPRoute, mcp_type: MCPType) -> MCPType | None:
        """Advanced route type mapping."""
        # Convert all admin routes to tools regardless of HTTP method
        if "/admin/" in route.path:
            return MCPType.TOOL
    
        elif "internal" in route.tags:
            return MCPType.EXCLUDE
        
        # Convert user detail routes to templates even if they're POST
        elif route.path.startswith("/users/") and route.method == "POST":
            return MCPType.RESOURCE_TEMPLATE
        
        # Use defaults for all other routes
        return None
    
    mcp = FastMCP.from_openapi(
        openapi_spec=spec,
        client=client,
        route_map_fn=custom_route_mapper,
    )
    

[​](https://gofastmcp.com/integrations/openapi#customization)

Customization
------------------------------------------------------------------------------

### 

[​](https://gofastmcp.com/integrations/openapi#component-names)

Component Names

`` New in version: `2.5.0` `` FastMCP automatically generates names for MCP components based on the OpenAPI specification. By default, it uses the `operationId` from your OpenAPI spec, up to the first double underscore (`__`). All component names are automatically:

*   **Slugified**: Spaces and special characters are converted to underscores or removed
*   **Truncated**: Limited to 56 characters maximum to ensure compatibility
*   **Unique**: If multiple components have the same name, a number is automatically appended to make them unique

For more control over component names, you can provide an `mcp_names` dictionary that maps `operationId` values to your desired names. The `operationId` must be exactly as it appears in the OpenAPI spec. The provided name will always be slugified and truncated.

Copy

    mcp = FastMCP.from_openapi(
        openapi_spec=spec,
        client=client,
        mcp_names={
            "list_users__with_pagination": "user_list",
            "create_user__admin_required": "create_user", 
            "get_user_details__admin_required": "user_detail",
        }
    )
    

Any `operationId` not found in `mcp_names` will use the default strategy (operationId up to the first `__`).

### 

[​](https://gofastmcp.com/integrations/openapi#tags)

Tags

`` New in version: `2.8.0` `` FastMCP provides several ways to add tags to your MCP components, allowing you to categorize and organize them for better discoverability and filtering. Tags are combined from multiple sources to create the final set of tags on each component.

#### 

[​](https://gofastmcp.com/integrations/openapi#routemap-tags)

RouteMap Tags

You can add custom tags to components created from specific routes using the `mcp_tags` parameter in `RouteMap`. These tags will be applied to all components created from routes that match that particular route map.

Copy

    from fastmcp.server.openapi import RouteMap, MCPType
    
    mcp = FastMCP.from_openapi(
        openapi_spec=spec,
        client=client,
        route_maps=[\
            # Add custom tags to all POST endpoints\
            RouteMap(\
                methods=["POST"],\
                pattern=r".*",\
                mcp_type=MCPType.TOOL,\
                mcp_tags={"write-operation", "api-mutation"}\
            ),\
            \
            # Add different tags to detail view endpoints\
            RouteMap(\
                methods=["GET"],\
                pattern=r".*\{.*\}.*",\
                mcp_type=MCPType.RESOURCE_TEMPLATE,\
                mcp_tags={"detail-view", "parameterized"}\
            ),\
            \
            # Add tags to list endpoints\
            RouteMap(\
                methods=["GET"],\
                pattern=r".*",\
                mcp_type=MCPType.RESOURCE,\
                mcp_tags={"list-data", "collection"}\
            ),\
        ],
    )
    

#### 

[​](https://gofastmcp.com/integrations/openapi#global-tags)

Global Tags

You can add tags to **all** components by providing a `tags` parameter when creating your MCP server. These global tags will be applied to every component created from your OpenAPI specification.

Copy

    mcp = FastMCP.from_openapi(
        openapi_spec=spec,
        client=client,
        tags={"api-v2", "production", "external"}
    )
    

#### 

[​](https://gofastmcp.com/integrations/openapi#openapi-tags-in-client-meta)

OpenAPI Tags in Client Meta

FastMCP automatically includes OpenAPI tags from your specification in the component’s metadata. These tags are available to MCP clients through the `_meta._fastmcp.tags` field, allowing clients to filter and organize components based on the original OpenAPI tagging:

OpenAPI spec with tags

Access OpenAPI tags in MCP client

Copy

    {
      "paths": {
        "/users": {
          "get": {
            "tags": ["users", "public"],
            "operationId": "list_users",
            "summary": "List all users"
          }
        }
      }
    }
    

This makes it easy for clients to understand and organize API endpoints based on their original OpenAPI categorization.

### 

[​](https://gofastmcp.com/integrations/openapi#advanced-customization)

Advanced Customization

`` New in version: `2.5.0` `` By default, FastMCP creates MCP components using a variety of metadata from the OpenAPI spec, such as incorporating the OpenAPI description into the MCP component description. At times you may want to modify those MCP components in a variety of ways, such as adding LLM-specific instructions or tags. For fine-grained customization, you can provide a `mcp_component_fn` when creating the MCP server. After each MCP component has been created, this function is called on it and has the opportunity to modify it in-place.

Your `mcp_component_fn` is expected to modify the component in-place, not to return a new component. The result of the function is ignored.

Copy

    from fastmcp.server.openapi import (
        HTTPRoute, 
        OpenAPITool, 
        OpenAPIResource, 
        OpenAPIResourceTemplate,
    )
    
    # If using experimental parser, import from experimental module:
    # from fastmcp.experimental.server.openapi import (
    #     HTTPRoute,
    #     OpenAPITool,
    #     OpenAPIResource,
    #     OpenAPIResourceTemplate,
    # )
    
    def customize_components(
        route: HTTPRoute, 
        component: OpenAPITool | OpenAPIResource | OpenAPIResourceTemplate,
    ) -> None:
        # Add custom tags to all components
        component.tags.add("openapi")
        
        # Customize based on component type
        if isinstance(component, OpenAPITool):
            component.description = f"🔧 {component.description} (via API)"
        
        if isinstance(component, OpenAPIResource):
            component.description = f"📊 {component.description}"
            component.tags.add("data")
    
    mcp = FastMCP.from_openapi(
        openapi_spec=spec,
        client=client,
        mcp_component_fn=customize_components,
    )
    

[​](https://gofastmcp.com/integrations/openapi#request-parameter-handling)

Request Parameter Handling
--------------------------------------------------------------------------------------------------------

FastMCP intelligently handles different types of parameters in OpenAPI requests:

### 

[​](https://gofastmcp.com/integrations/openapi#query-parameters)

Query Parameters

By default, FastMCP only includes query parameters that have non-empty values. Parameters with `None` values or empty strings are automatically filtered out.

Copy

    # When calling this tool...
    await client.call_tool("search_products", {
        "category": "electronics",  # ✅ Included
        "min_price": 100,           # ✅ Included  
        "max_price": None,          # ❌ Excluded
        "brand": "",                # ❌ Excluded
    })
    
    # The HTTP request will be: GET /products?category=electronics&min_price=100
    

### 

[​](https://gofastmcp.com/integrations/openapi#path-parameters)

Path Parameters

Path parameters are typically required by REST APIs. FastMCP:

*   Filters out `None` values
*   Validates that all required path parameters are provided
*   Raises clear errors for missing required parameters

Copy

    # ✅ This works
    await client.call_tool("get_user", {"user_id": 123})
    
    # ❌ This raises: "Missing required path parameters: {'user_id'}"
    await client.call_tool("get_user", {"user_id": None})
    

### 

[​](https://gofastmcp.com/integrations/openapi#array-parameters)

Array Parameters

FastMCP handles array parameters according to OpenAPI specifications:

*   **Query arrays**: Serialized based on the `explode` parameter (default: `True`)
*   **Path arrays**: Serialized as comma-separated values (OpenAPI ‘simple’ style)

Copy

    # Query array with explode=true (default)
    # ?tags=red&tags=blue&tags=green
    
    # Query array with explode=false  
    # ?tags=red,blue,green
    
    # Path array (always comma-separated)
    # /items/red,blue,green
    

### 

[​](https://gofastmcp.com/integrations/openapi#headers)

Headers

Header parameters are automatically converted to strings and included in the HTTP request.

[FastAPI 🤝 FastMCP\
\
Previous](https://gofastmcp.com/integrations/fastapi)
[Tool Transformation\
\
Next](https://gofastmcp.com/patterns/tool-transformation)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.