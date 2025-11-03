# GoFast MCP Documentation

> Local mirror of https://gofastmcp.com/ documentation

## Getting Started

- [Welcome](getting-started/welcome.md)
- [Installation](getting-started/installation.md)
- [Quickstart](getting-started/quickstart.md)

## Core Concepts

### Clients

- [Client](clients/client.md)
- [Authentication](clients/auth/)
  - [Bearer Token](clients/auth/bearer.md)
  - [OAuth](clients/auth/oauth.md)
- [Messages](clients/messages.md)
- [Tools](clients/tools.md)
- [Resources](clients/resources.md)
- [Prompts](clients/prompts.md)
- [Sampling](clients/sampling.md)
- [Logging](clients/logging.md)
- [Progress](clients/progress.md)
- [Elicitation](clients/elicitation.md)
- [Roots](clients/roots.md)
- [Transports](clients/transports.md)

### Servers

- [Server](servers/server.md)
- [Authentication](servers/auth/)
  - [Authentication Overview](servers/auth/authentication.md)
  - [Full OAuth Server](servers/auth/full-oauth-server.md)
  - [OAuth Proxy](servers/auth/oauth-proxy.md)
  - [OIDC Proxy](servers/auth/oidc-proxy.md)
  - [Remote OAuth](servers/auth/remote-oauth.md)
  - [Token Verification](servers/auth/token-verification.md)
- [Tools](servers/tools.md)
- [Resources](servers/resources.md)
- [Prompts](servers/prompts.md)
- [Sampling](servers/sampling.md)
- [Context](servers/context.md)
- [Elicitation](servers/elicitation.md)
- [Logging](servers/logging.md)
- [Progress](servers/progress.md)
- [Middleware](servers/middleware.md)
- [Composition](servers/composition.md)
- [Proxy](servers/proxy.md)
- [Icons](servers/icons.md)
- [Storage Backends](servers/storage-backends.md)

## Deployment

- [Running Server](deployment/running-server.md)
- [Server Configuration](deployment/server-configuration.md)
- [HTTP Deployment](deployment/http.md)
- [FastMCP Cloud](deployment/fastmcp-cloud.md)

## Integrations

### AI Clients
- [Anthropic (Claude)](integrations/anthropic.md)
- [Claude Code](integrations/claude-code.md)
- [Claude Desktop](integrations/claude-desktop.md)
- [OpenAI](integrations/openai.md)
- [ChatGPT](integrations/chatgpt.md)
- [Google Gemini](integrations/gemini.md)
- [Gemini CLI](integrations/gemini-cli.md)
- [Cursor](integrations/cursor.md)

### Authentication Providers
- [Auth0](integrations/auth0.md)
- [AuthKit](integrations/authkit.md)
- [AWS Cognito](integrations/aws-cognito.md)
- [Azure](integrations/azure.md)
- [Descope](integrations/descope.md)
- [GitHub](integrations/github.md)
- [Google](integrations/google.md)
- [Scalekit](integrations/scalekit.md)
- [WorkOS](integrations/workos.md)

### Authorization
- [Eunomia Authorization](integrations/eunomia-authorization.md)
- [Permit](integrations/permit.md)

### Other
- [FastAPI](integrations/fastapi.md)
- [OpenAPI](integrations/openapi.md)
- [MCP JSON Configuration](integrations/mcp-json-configuration.md)

## Patterns

- [CLI](patterns/cli.md)
- [Contrib](patterns/contrib.md)
- [Decorating Methods](patterns/decorating-methods.md)
- [Testing](patterns/testing.md)
- [Tool Transformation](patterns/tool-transformation.md)

## Development

- [Contributing](development/contributing.md)
- [Tests](development/tests.md)
- [Releases](development/releases.md)
- [Upgrade Guide](development/upgrade-guide.md)

## Python SDK Reference

### CLI
- [CLI Init](python-sdk/fastmcp-cli-__init__.md)
- [CLI](python-sdk/fastmcp-cli-cli.md)
- [CLI Run](python-sdk/fastmcp-cli-run.md)
- **Install Commands**
  - [Install Init](python-sdk/fastmcp-cli-install-__init__.md)
  - [Claude Code](python-sdk/fastmcp-cli-install-claude_code.md)
  - [Claude Desktop](python-sdk/fastmcp-cli-install-claude_desktop.md)
  - [Cursor](python-sdk/fastmcp-cli-install-cursor.md)
  - [Gemini CLI](python-sdk/fastmcp-cli-install-gemini_cli.md)
  - [MCP JSON](python-sdk/fastmcp-cli-install-mcp_json.md)
  - [Shared](python-sdk/fastmcp-cli-install-shared.md)

### Client
- [Client Init](python-sdk/fastmcp-client-__init__.md)
- [Client](python-sdk/fastmcp-client-client.md)
- [Auth Init](python-sdk/fastmcp-client-auth-__init__.md)
- [Bearer Auth](python-sdk/fastmcp-client-auth-bearer.md)
- [OAuth Auth](python-sdk/fastmcp-client-auth-oauth.md)
- [OAuth Callback](python-sdk/fastmcp-client-oauth_callback.md)
- [Elicitation](python-sdk/fastmcp-client-elicitation.md)
- [Logging](python-sdk/fastmcp-client-logging.md)
- [Messages](python-sdk/fastmcp-client-messages.md)
- [Progress](python-sdk/fastmcp-client-progress.md)
- [Roots](python-sdk/fastmcp-client-roots.md)
- [Sampling](python-sdk/fastmcp-client-sampling.md)
- [Transports](python-sdk/fastmcp-client-transports.md)

### Server
- [Server Init](python-sdk/fastmcp-server-__init__.md)
- [Server](python-sdk/fastmcp-server-server.md)
- [Context](python-sdk/fastmcp-server-context.md)
- [Dependencies](python-sdk/fastmcp-server-dependencies.md)
- [Elicitation](python-sdk/fastmcp-server-elicitation.md)
- [HTTP](python-sdk/fastmcp-server-http.md)
- [Low Level](python-sdk/fastmcp-server-low_level.md)
- [OpenAPI](python-sdk/fastmcp-server-openapi.md)
- [Proxy](python-sdk/fastmcp-server-proxy.md)

#### Server Auth
- [Auth Init](python-sdk/fastmcp-server-auth-__init__.md)
- [Auth](python-sdk/fastmcp-server-auth-auth.md)
- [JWT Issuer](python-sdk/fastmcp-server-auth-jwt_issuer.md)
- [Middleware](python-sdk/fastmcp-server-auth-middleware.md)
- [OAuth Proxy](python-sdk/fastmcp-server-auth-oauth_proxy.md)
- [OIDC Proxy](python-sdk/fastmcp-server-auth-oidc_proxy.md)
- [Redirect Validation](python-sdk/fastmcp-server-auth-redirect_validation.md)

**Auth Providers:**
- [Providers Init](python-sdk/fastmcp-server-auth-providers-__init__.md)
- [Auth0](python-sdk/fastmcp-server-auth-providers-auth0.md)
- [AWS](python-sdk/fastmcp-server-auth-providers-aws.md)
- [Azure](python-sdk/fastmcp-server-auth-providers-azure.md)
- [Bearer](python-sdk/fastmcp-server-auth-providers-bearer.md)
- [Descope](python-sdk/fastmcp-server-auth-providers-descope.md)
- [GitHub](python-sdk/fastmcp-server-auth-providers-github.md)
- [Google](python-sdk/fastmcp-server-auth-providers-google.md)
- [In Memory](python-sdk/fastmcp-server-auth-providers-in_memory.md)
- [Introspection](python-sdk/fastmcp-server-auth-providers-introspection.md)
- [JWT](python-sdk/fastmcp-server-auth-providers-jwt.md)
- [Scalekit](python-sdk/fastmcp-server-auth-providers-scalekit.md)
- [Supabase](python-sdk/fastmcp-server-auth-providers-supabase.md)
- [WorkOS](python-sdk/fastmcp-server-auth-providers-workos.md)

#### Server Middleware
- [Middleware Init](python-sdk/fastmcp-server-middleware-__init__.md)
- [Middleware](python-sdk/fastmcp-server-middleware-middleware.md)
- [Caching](python-sdk/fastmcp-server-middleware-caching.md)
- [Error Handling](python-sdk/fastmcp-server-middleware-error_handling.md)
- [Logging](python-sdk/fastmcp-server-middleware-logging.md)
- [Rate Limiting](python-sdk/fastmcp-server-middleware-rate_limiting.md)
- [Timing](python-sdk/fastmcp-server-middleware-timing.md)
- [Tool Injection](python-sdk/fastmcp-server-middleware-tool_injection.md)

### Tools
- [Tools Init](python-sdk/fastmcp-tools-__init__.md)
- [Tool](python-sdk/fastmcp-tools-tool.md)
- [Tool Manager](python-sdk/fastmcp-tools-tool_manager.md)
- [Tool Transform](python-sdk/fastmcp-tools-tool_transform.md)

### Prompts
- [Prompts Init](python-sdk/fastmcp-prompts-__init__.md)
- [Prompt](python-sdk/fastmcp-prompts-prompt.md)
- [Prompt Manager](python-sdk/fastmcp-prompts-prompt_manager.md)

### Resources
- [Resources Init](python-sdk/fastmcp-resources-__init__.md)
- [Resource](python-sdk/fastmcp-resources-resource.md)
- [Resource Manager](python-sdk/fastmcp-resources-resource_manager.md)
- [Template](python-sdk/fastmcp-resources-template.md)
- [Types](python-sdk/fastmcp-resources-types.md)

### Utilities
- [Utilities Init](python-sdk/fastmcp-utilities-__init__.md)
- [Auth](python-sdk/fastmcp-utilities-auth.md)
- [CLI](python-sdk/fastmcp-utilities-cli.md)
- [Components](python-sdk/fastmcp-utilities-components.md)
- [Exceptions](python-sdk/fastmcp-utilities-exceptions.md)
- [HTTP](python-sdk/fastmcp-utilities-http.md)
- [Inspect](python-sdk/fastmcp-utilities-inspect.md)
- [JSON Schema](python-sdk/fastmcp-utilities-json_schema.md)
- [JSON Schema Type](python-sdk/fastmcp-utilities-json_schema_type.md)
- [Logging](python-sdk/fastmcp-utilities-logging.md)
- [MCP Config](python-sdk/fastmcp-utilities-mcp_config.md)
- [OpenAPI](python-sdk/fastmcp-utilities-openapi.md)
- [Tests](python-sdk/fastmcp-utilities-tests.md)
- [Types](python-sdk/fastmcp-utilities-types.md)
- [UI](python-sdk/fastmcp-utilities-ui.md)

**MCP Server Config:**
- [MCP Server Config Init](python-sdk/fastmcp-utilities-mcp_server_config-__init__.md)
- [V1 Init](python-sdk/fastmcp-utilities-mcp_server_config-v1-__init__.md)
- [MCP Server Config](python-sdk/fastmcp-utilities-mcp_server_config-v1-mcp_server_config.md)
- **Environments:**
  - [Environments Init](python-sdk/fastmcp-utilities-mcp_server_config-v1-environments-__init__.md)
  - [Base](python-sdk/fastmcp-utilities-mcp_server_config-v1-environments-base.md)
  - [UV](python-sdk/fastmcp-utilities-mcp_server_config-v1-environments-uv.md)
- **Sources:**
  - [Sources Init](python-sdk/fastmcp-utilities-mcp_server_config-v1-sources-__init__.md)
  - [Base](python-sdk/fastmcp-utilities-mcp_server_config-v1-sources-base.md)
  - [Filesystem](python-sdk/fastmcp-utilities-mcp_server_config-v1-sources-filesystem.md)

### Core
- [Exceptions](python-sdk/fastmcp-exceptions.md)
- [MCP Config](python-sdk/fastmcp-mcp_config.md)
- [Settings](python-sdk/fastmcp-settings.md)

## Additional Resources

- [Changelog](changelog.md)
- [Updates](updates.md)

---

*Documentation mirrored from https://gofastmcp.com/*
