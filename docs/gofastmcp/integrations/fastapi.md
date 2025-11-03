---
url: https://gofastmcp.com/integrations/fastapi
title: FastAPI 🤝 FastMCP - FastMCP
description: Integrate FastMCP with FastAPI applications
scraped_at: 2025-11-03T18:42:14.053084
---

[Skip to main content](https://gofastmcp.com/integrations/fastapi#content-area)

Join the [FastMCP community](https://discord.gg/uu8dJCgttd)
!

[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)

Search...

Navigation

API Integration

FastAPI 🤝 FastMCP

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

*   [Example FastAPI Application](https://gofastmcp.com/integrations/fastapi#example-fastapi-application)
    
*   [Generating an MCP Server](https://gofastmcp.com/integrations/fastapi#generating-an-mcp-server)
    
*   [Basic Conversion](https://gofastmcp.com/integrations/fastapi#basic-conversion)
    
*   [Adding Components](https://gofastmcp.com/integrations/fastapi#adding-components)
    
*   [Interacting with the MCP Server](https://gofastmcp.com/integrations/fastapi#interacting-with-the-mcp-server)
    
*   [Custom Route Mapping](https://gofastmcp.com/integrations/fastapi#custom-route-mapping)
    
*   [Authentication and Headers](https://gofastmcp.com/integrations/fastapi#authentication-and-headers)
    
*   [Mounting an MCP Server](https://gofastmcp.com/integrations/fastapi#mounting-an-mcp-server)
    
*   [Basic Mounting](https://gofastmcp.com/integrations/fastapi#basic-mounting)
    
*   [Offering an LLM-Friendly API](https://gofastmcp.com/integrations/fastapi#offering-an-llm-friendly-api)
    
*   [Key Considerations](https://gofastmcp.com/integrations/fastapi#key-considerations)
    
*   [Operation IDs](https://gofastmcp.com/integrations/fastapi#operation-ids)
    
*   [Lifespan Management](https://gofastmcp.com/integrations/fastapi#lifespan-management)
    
*   [CORS Middleware](https://gofastmcp.com/integrations/fastapi#cors-middleware)
    
*   [Combining Lifespans](https://gofastmcp.com/integrations/fastapi#combining-lifespans)
    
*   [Performance Tips](https://gofastmcp.com/integrations/fastapi#performance-tips)
    

**New in 2.11**: FastMCP is introducing a next-generation OpenAPI parser. The new parser has greatly improved performance and compatibility, and is also easier to maintain. To enable it, set the environment variable `FASTMCP_EXPERIMENTAL_ENABLE_NEW_OPENAPI_PARSER=true`.The new parser is largely API-compatible with the existing implementation and will become the default in a future version. We encourage all users to test it and report any issues before it becomes the default.

FastMCP provides two powerful ways to integrate with FastAPI applications:

1.  **[Generate an MCP server FROM your FastAPI app](https://gofastmcp.com/integrations/fastapi#generating-an-mcp-server)
    ** - Convert existing API endpoints into MCP tools
2.  **[Mount an MCP server INTO your FastAPI app](https://gofastmcp.com/integrations/fastapi#mounting-an-mcp-server)
    ** - Add MCP functionality to your web application

Generating MCP servers from OpenAPI is a great way to get started with FastMCP, but in practice LLMs achieve **significantly better performance** with well-designed and curated MCP servers than with auto-converted OpenAPI servers. This is especially true for complex APIs with many endpoints and parameters.We recommend using the FastAPI integration for bootstrapping and prototyping, not for mirroring your API to LLM clients. See the post [Stop Converting Your REST APIs to MCP](https://www.jlowin.dev/blog/stop-converting-rest-apis-to-mcp)
 for more details.

FastMCP does _not_ include FastAPI as a dependency; you must install it separately to use this integration.

[​](https://gofastmcp.com/integrations/fastapi#example-fastapi-application)

Example FastAPI Application
----------------------------------------------------------------------------------------------------------

Throughout this guide, we’ll use this e-commerce API as our example (click the `Copy` button to copy it for use with other code blocks):

Copy

    # Copy this FastAPI server into other code blocks in this guide
    
    from fastapi import FastAPI, HTTPException
    from pydantic import BaseModel
    
    # Models
    class Product(BaseModel):
        name: str
        price: float
        category: str
        description: str | None = None
    
    class ProductResponse(BaseModel):
        id: int
        name: str
        price: float
        category: str
        description: str | None = None
    
    # Create FastAPI app
    app = FastAPI(title="E-commerce API", version="1.0.0")
    
    # In-memory database
    products_db = {
        1: ProductResponse(
            id=1, name="Laptop", price=999.99, category="Electronics"
        ),
        2: ProductResponse(
            id=2, name="Mouse", price=29.99, category="Electronics"
        ),
        3: ProductResponse(
            id=3, name="Desk Chair", price=299.99, category="Furniture"
        ),
    }
    next_id = 4
    
    @app.get("/products", response_model=list[ProductResponse])
    def list_products(
        category: str | None = None,
        max_price: float | None = None,
    ) -> list[ProductResponse]:
        """List all products with optional filtering."""
        products = list(products_db.values())
        if category:
            products = [p for p in products if p.category == category]
        if max_price:
            products = [p for p in products if p.price <= max_price]
        return products
    
    @app.get("/products/{product_id}", response_model=ProductResponse)
    def get_product(product_id: int):
        """Get a specific product by ID."""
        if product_id not in products_db:
            raise HTTPException(status_code=404, detail="Product not found")
        return products_db[product_id]
    
    @app.post("/products", response_model=ProductResponse)
    def create_product(product: Product):
        """Create a new product."""
        global next_id
        product_response = ProductResponse(id=next_id, **product.model_dump())
        products_db[next_id] = product_response
        next_id += 1
        return product_response
    
    @app.put("/products/{product_id}", response_model=ProductResponse)
    def update_product(product_id: int, product: Product):
        """Update an existing product."""
        if product_id not in products_db:
            raise HTTPException(status_code=404, detail="Product not found")
        products_db[product_id] = ProductResponse(
            id=product_id,
            **product.model_dump(),
        )
        return products_db[product_id]
    
    @app.delete("/products/{product_id}")
    def delete_product(product_id: int):
        """Delete a product."""
        if product_id not in products_db:
            raise HTTPException(status_code=404, detail="Product not found")
        del products_db[product_id]
        return {"message": "Product deleted"}
    

See all 83 lines

All subsequent code examples in this guide assume you have the above FastAPI application code already defined. Each example builds upon this base application, `app`.

[​](https://gofastmcp.com/integrations/fastapi#generating-an-mcp-server)

Generating an MCP Server
----------------------------------------------------------------------------------------------------

`` New in version: `2.0.0` `` One of the most common ways to bootstrap an MCP server is to generate it from an existing FastAPI application. FastMCP will expose your FastAPI endpoints as MCP components (tools, by default) in order to expose your API to LLM clients.

### 

[​](https://gofastmcp.com/integrations/fastapi#basic-conversion)

Basic Conversion

Convert the FastAPI app to an MCP server with a single line:

Copy

    # Assumes the FastAPI app from above is already defined
    from fastmcp import FastMCP
    
    # Convert to MCP server
    mcp = FastMCP.from_fastapi(app=app)
    
    if __name__ == "__main__":
        mcp.run()
    

### 

[​](https://gofastmcp.com/integrations/fastapi#adding-components)

Adding Components

Your converted MCP server is a full FastMCP instance, meaning you can add new tools, resources, and other components to it just like you would with any other FastMCP instance.

Copy

    # Assumes the FastAPI app from above is already defined
    from fastmcp import FastMCP
    
    # Convert to MCP server
    mcp = FastMCP.from_fastapi(app=app)
    
    # Add a new tool
    @mcp.tool
    def get_product(product_id: int) -> ProductResponse:
        """Get a product by ID."""
        return products_db[product_id]
    
    # Run the MCP server
    if __name__ == "__main__":
        mcp.run()
    

### 

[​](https://gofastmcp.com/integrations/fastapi#interacting-with-the-mcp-server)

Interacting with the MCP Server

Once you’ve converted your FastAPI app to an MCP server, you can interact with it using the FastMCP client to test functionality before deploying it to an LLM-based application.

Copy

    # Assumes the FastAPI app from above is already defined
    from fastmcp import FastMCP
    from fastmcp.client import Client
    import asyncio
    
    # Convert to MCP server
    mcp = FastMCP.from_fastapi(app=app)
    
    async def demo():
        async with Client(mcp) as client:
            # List available tools
            tools = await client.list_tools()
            print(f"Available tools: {[t.name for t in tools]}")
            
            # Create a product
            result = await client.call_tool(
                "create_product_products_post",
                {
                    "name": "Wireless Keyboard",
                    "price": 79.99,
                    "category": "Electronics",
                    "description": "Bluetooth mechanical keyboard"
                }
            )
            print(f"Created product: {result.data}")
            
            # List electronics under $100
            result = await client.call_tool(
                "list_products_products_get",
                {"category": "Electronics", "max_price": 100}
            )
            print(f"Affordable electronics: {result.data}")
    
    if __name__ == "__main__":
        asyncio.run(demo())
    

### 

[​](https://gofastmcp.com/integrations/fastapi#custom-route-mapping)

Custom Route Mapping

Because FastMCP’s FastAPI integration is based on its [OpenAPI integration](https://gofastmcp.com/integrations/openapi)
, you can customize how endpoints are converted to MCP components in exactly the same way. For example, here we use a `RouteMap` to map all GET requests to MCP resources, and all POST/PUT/DELETE requests to MCP tools:

Copy

    # Assumes the FastAPI app from above is already defined
    from fastmcp import FastMCP
    from fastmcp.server.openapi import RouteMap, MCPType
    
    # If using experimental parser, import from experimental module:
    # from fastmcp.experimental.server.openapi import RouteMap, MCPType
    
    # Custom mapping rules
    mcp = FastMCP.from_fastapi(
        app=app,
        route_maps=[\
            # GET with path params → ResourceTemplates\
            RouteMap(\
                methods=["GET"], \
                pattern=r".*\{.*\}.*", \
                mcp_type=MCPType.RESOURCE_TEMPLATE\
            ),\
            # Other GETs → Resources\
            RouteMap(\
                methods=["GET"], \
                pattern=r".*", \
                mcp_type=MCPType.RESOURCE\
            ),\
            # POST/PUT/DELETE → Tools (default)\
        ],
    )
    
    # Now:
    # - GET /products → Resource
    # - GET /products/{id} → ResourceTemplate
    # - POST/PUT/DELETE → Tools
    

To learn more about customizing the conversion process, see the [OpenAPI Integration guide](https://gofastmcp.com/integrations/openapi)
.

### 

[​](https://gofastmcp.com/integrations/fastapi#authentication-and-headers)

Authentication and Headers

You can configure headers and other client options via the `httpx_client_kwargs` parameter. For example, to add authentication to your FastAPI app, you can pass a `headers` dictionary to the `httpx_client_kwargs` parameter:

Copy

    # Assumes the FastAPI app from above is already defined
    from fastmcp import FastMCP
    
    # Add authentication to your FastAPI app
    from fastapi import Depends, Header
    from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
    
    security = HTTPBearer()
    
    def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
        if credentials.credentials != "secret-token":
            raise HTTPException(status_code=401, detail="Invalid authentication")
        return credentials.credentials
    
    # Add a protected endpoint
    @app.get("/admin/stats", dependencies=[Depends(verify_token)])
    def get_admin_stats():
        return {
            "total_products": len(products_db),
            "categories": list(set(p.category for p in products_db.values()))
        }
    
    # Create MCP server with authentication headers
    mcp = FastMCP.from_fastapi(
        app=app,
        httpx_client_kwargs={
            "headers": {
                "Authorization": "Bearer secret-token",
            }
        }
    )
    

[​](https://gofastmcp.com/integrations/fastapi#mounting-an-mcp-server)

Mounting an MCP Server
------------------------------------------------------------------------------------------------

`` New in version: `2.3.1` `` In addition to generating servers, FastMCP can facilitate adding MCP servers to your existing FastAPI application. You can do this by mounting the MCP ASGI application.

### 

[​](https://gofastmcp.com/integrations/fastapi#basic-mounting)

Basic Mounting

To mount an MCP server, you can use the `http_app` method on your FastMCP instance. This will return an ASGI application that can be mounted to your FastAPI application.

Copy

    from fastmcp import FastMCP
    from fastapi import FastAPI
    
    # Create MCP server
    mcp = FastMCP("Analytics Tools")
    
    @mcp.tool
    def analyze_pricing(category: str) -> dict:
        """Analyze pricing for a category."""
        products = [p for p in products_db.values() if p.category == category]
        if not products:
            return {"error": f"No products in {category}"}
        
        prices = [p.price for p in products]
        return {
            "category": category,
            "avg_price": round(sum(prices) / len(prices), 2),
            "min": min(prices),
            "max": max(prices),
        }
    
    # Create ASGI app from MCP server
    mcp_app = mcp.http_app(path='/mcp')
    
    # Key: Pass lifespan to FastAPI
    app = FastAPI(title="E-commerce API", lifespan=mcp_app.lifespan)
    
    # Mount the MCP server
    app.mount("/analytics", mcp_app)
    
    # Now: API at /products/*, MCP at /analytics/mcp/
    

[​](https://gofastmcp.com/integrations/fastapi#offering-an-llm-friendly-api)

Offering an LLM-Friendly API
------------------------------------------------------------------------------------------------------------

A common pattern is to generate an MCP server from your FastAPI app and serve both interfaces from the same application. This provides an LLM-optimized interface alongside your regular API:

Copy

    # Assumes the FastAPI app from above is already defined
    from fastmcp import FastMCP
    from fastapi import FastAPI
    
    # 1. Generate MCP server from your API
    mcp = FastMCP.from_fastapi(app=app, name="E-commerce MCP")
    
    # 2. Create the MCP's ASGI app
    mcp_app = mcp.http_app(path='/mcp')
    
    # 3. Create a new FastAPI app that combines both sets of routes
    combined_app = FastAPI(
        title="E-commerce API with MCP",
        routes=[\
            *mcp_app.routes,  # MCP routes\
            *app.routes,      # Original API routes\
        ],
        lifespan=mcp_app.lifespan,
    )
    
    # Now you have:
    # - Regular API: http://localhost:8000/products
    # - LLM-friendly MCP: http://localhost:8000/mcp
    # Both served from the same FastAPI application!
    

This approach lets you maintain a single codebase while offering both traditional REST endpoints and MCP-compatible endpoints for LLM clients.

[​](https://gofastmcp.com/integrations/fastapi#key-considerations)

Key Considerations
----------------------------------------------------------------------------------------

### 

[​](https://gofastmcp.com/integrations/fastapi#operation-ids)

Operation IDs

FastAPI operation IDs become MCP component names. Always specify meaningful operation IDs:

Copy

    # Good - explicit operation_id
    @app.get("/users/{user_id}", operation_id="get_user_by_id")
    def get_user(user_id: int):
        return {"id": user_id}
    
    # Less ideal - auto-generated name
    @app.get("/users/{user_id}")
    def get_user(user_id: int):
        return {"id": user_id}
    

### 

[​](https://gofastmcp.com/integrations/fastapi#lifespan-management)

Lifespan Management

When mounting MCP servers, always pass the lifespan context:

Copy

    # Correct - lifespan passed
    mcp_app = mcp.http_app(path='/mcp')
    app = FastAPI(lifespan=mcp_app.lifespan)
    app.mount("/mcp", mcp_app)
    
    # Incorrect - missing lifespan
    app = FastAPI()
    app.mount("/mcp", mcp.http_app())  # Session manager won't initialize
    

If you’re mounting an authenticated MCP server under a path prefix, see [Mounting Authenticated Servers](https://gofastmcp.com/deployment/http#mounting-authenticated-servers)
 for important OAuth routing considerations.

### 

[​](https://gofastmcp.com/integrations/fastapi#cors-middleware)

CORS Middleware

If your FastAPI app uses `CORSMiddleware` and you’re mounting an OAuth-protected FastMCP server, avoid adding application-wide CORS middleware. FastMCP and the MCP SDK already handle CORS for OAuth routes, and layering CORS middleware can cause conflicts (such as 404 errors on `.well-known` routes or OPTIONS requests). If you need CORS on your own FastAPI routes, use the sub-app pattern: mount your API and FastMCP as separate apps, each with their own middleware, rather than adding top-level `CORSMiddleware` to the combined application.

### 

[​](https://gofastmcp.com/integrations/fastapi#combining-lifespans)

Combining Lifespans

If your FastAPI app already has a lifespan (for database connections, startup tasks, etc.), you can’t simply replace it with the MCP lifespan. Instead, you need to create a new lifespan function that manages both contexts. This ensures that both your app’s initialization logic and the MCP server’s session manager run properly:

Copy

    from contextlib import asynccontextmanager
    from fastapi import FastAPI
    from fastmcp import FastMCP
    
    # Your existing lifespan
    @asynccontextmanager
    async def app_lifespan(app: FastAPI):
        # Startup
        print("Starting up the app...")
        # Initialize database, cache, etc.
        yield
        # Shutdown
        print("Shutting down the app...")
    
    # Create MCP server
    mcp = FastMCP("Tools")
    mcp_app = mcp.http_app(path='/mcp')
    
    # Combine both lifespans
    @asynccontextmanager
    async def combined_lifespan(app: FastAPI):
        # Run both lifespans
        async with app_lifespan(app):
            async with mcp_app.lifespan(app):
                yield
    
    # Use the combined lifespan
    app = FastAPI(lifespan=combined_lifespan)
    app.mount("/mcp", mcp_app)
    

This pattern ensures both your app’s initialization logic and the MCP server’s session manager are properly managed. The key is using nested `async with` statements - the inner context (MCP) will be initialized after the outer context (your app), and cleaned up before it. This maintains the correct initialization and cleanup order for all your resources.

### 

[​](https://gofastmcp.com/integrations/fastapi#performance-tips)

Performance Tips

1.  **Use in-memory transport for testing** - Pass MCP servers directly to clients
2.  **Design purpose-built MCP tools** - Better than auto-converting complex APIs
3.  **Keep tool parameters simple** - LLMs perform better with focused interfaces

For more details on configuration options, see the [OpenAPI Integration guide](https://gofastmcp.com/integrations/openapi)
.

[OpenAI API 🤝 FastMCP\
\
Previous](https://gofastmcp.com/integrations/openai)
[OpenAPI 🤝 FastMCP\
\
Next](https://gofastmcp.com/integrations/openapi)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.