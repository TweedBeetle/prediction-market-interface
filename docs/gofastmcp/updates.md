---
url: https://gofastmcp.com/updates
title: FastMCP Updates - FastMCP
scraped_at: 2025-11-03T18:43:24.843906
---

[Skip to main content](https://gofastmcp.com/updates#content-area)

Join the [FastMCP community](https://discord.gg/uu8dJCgttd)
!

[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)

Search...

Navigation

Get Started

FastMCP Updates

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
    

FiltersClear

ReleasesBlog PostsTutorialsAnnouncements

[​](https://gofastmcp.com/updates#fastmcp-2-13-0)

FastMCP 2.13.0

Releases

October 25, 2025

[](https://github.com/jlowin/fastmcp/releases/tag/v2.13.0)

[](https://github.com/jlowin/fastmcp/releases/tag/v2.13.0)

[FastMCP 2.13.0: Cache Me If You Can\
-----------------------------------](https://github.com/jlowin/fastmcp/releases/tag/v2.13.0)

[FastMCP 2.13 “Cache Me If You Can” represents a fundamental maturation of the framework. After months of community feedback on authentication and state management, this release delivers the infrastructure FastMCP needs to handle production workloads: persistent storage, response caching, and pragmatic OAuth improvements that reflect real-world deployment challenges.💾 **Pluggable storage backends** bring persistent state to FastMCP servers. Built on](https://github.com/jlowin/fastmcp/releases/tag/v2.13.0)
 [py-key-value-aio](https://github.com/strawgate/py-key-value)
, a new library from FastMCP maintainer Bill Easton ([@strawgate](https://github.com/strawgate)
), the storage layer provides encrypted disk storage by default, platform-aware token management, and a simple key-value interface for application state. We’re excited to bring this elegantly designed library into the FastMCP ecosystem - it’s both powerful and remarkably easy to use, including wrappers to add encryption, TTLs, caching, and more to backends ranging from Elasticsearch, Redis, DynamoDB, filesystem, in-memory, and more!🔐 **OAuth maturity** brings months of production learnings into the framework. The new consent screen prevents confused deputy and authorization bypass attacks discovered in earlier versions, while the OAuth proxy now issues its own tokens with automatic key derivation. RFC 7662 token introspection support enables enterprise auth flows, and path prefix mounting enables OAuth-protected servers to integrate into existing web applications. FastMCP now supports out-of-the-box authentication with [WorkOS](https://gofastmcp.com/integrations/workos)
 and [AuthKit](https://gofastmcp.com/integrations/authkit)
, [GitHub](https://gofastmcp.com/integrations/github)
, [Google](https://gofastmcp.com/integrations/google)
, [Azure](https://gofastmcp.com/integrations/azure)
 (Entra ID), [AWS Cognito](https://gofastmcp.com/integrations/aws-cognito)
, [Auth0](https://gofastmcp.com/integrations/auth0)
, [Descope](https://gofastmcp.com/integrations/descope)
, [Scalekit](https://gofastmcp.com/integrations/scalekit)
, [JWTs](https://gofastmcp.com/servers/auth/token-verification#jwt-token-verification)
, and [RFC 7662 token introspection](https://gofastmcp.com/servers/auth/token-verification#token-introspection-protocol)
.⚡ **Response Caching Middleware** dramatically improves performance for expensive operations, while **Server lifespans** provide proper initialization and cleanup hooks that run once per server instance instead of per client session.✨ **Developer experience improvements** include Pydantic input validation, icon support, RFC 6570 query parameters for resource templates, improved Context API methods, and async file/directory resources.

Read the release notes

[​](https://gofastmcp.com/updates#fastmcp-2-12-5)

FastMCP 2.12.5

Releases

October 17, 2025

[FastMCP 2.12.5: Safety Pin\
--------------------------\
\
Pins MCP SDK version below 1.17 to ensure the `.well-known` payload appears in the expected location when using FastMCP auth providers with composite applications.\
\
Read the release notes](https://github.com/jlowin/fastmcp/releases/tag/v2.12.5)

[​](https://gofastmcp.com/updates#fastmcp-2-12-4)

FastMCP 2.12.4

Releases

September 26, 2025

[FastMCP 2.12.4: OIDC What You Did There\
---------------------------------------\
\
FastMCP 2.12.4 adds comprehensive OIDC support and expands authentication options with AWS Cognito and Descope providers. The release also includes improvements to logging middleware, URL handling for nested resources, persistent OAuth client registration storage, and various fixes to the experimental OpenAPI parser.🔐 **OIDC Configuration** brings native support for OpenID Connect, enabling seamless integration with enterprise identity providers.🏢 **Enterprise Authentication** expands with AWS Cognito and Descope providers, broadening the authentication ecosystem.🛠️ **Improved Reliability** through enhanced URL handling, persistent OAuth storage, and numerous parser fixes based on community feedback.\
\
Read the release notes](https://github.com/jlowin/fastmcp/releases/tag/v2.12.4)

[​](https://gofastmcp.com/updates#fastmcp-2-12-3)

FastMCP 2.12.3

Releases

September 17, 2025

[FastMCP 2.12.3: Double Time\
---------------------------\
\
FastMCP 2.12.3 focuses on performance and developer experience improvements. This release includes optimized auth provider imports that reduce server startup time, enhanced OIDC authentication flows, and automatic inline snapshot creation for testing.\
\
Read the release notes](https://github.com/jlowin/fastmcp/releases/tag/v2.12.3)

[​](https://gofastmcp.com/updates#fastmcp-2-12-2)

FastMCP 2.12.2

Releases

September 3, 2025

[FastMCP 2.12.2: Perchance to Stream\
-----------------------------------\
\
Hotfix for streamable-http transport validation in fastmcp.json configuration files, resolving a parsing error when CLI arguments were merged against the configuration spec.\
\
Read the release notes](https://github.com/jlowin/fastmcp/releases/tag/v2.12.2)

[​](https://gofastmcp.com/updates#fastmcp-2-12-1)

FastMCP 2.12.1

Releases

September 3, 2025

[FastMCP 2.12.1: OAuth to Joy\
----------------------------\
\
FastMCP 2.12.1 strengthens OAuth proxy implementation with improved client storage reliability, PKCE forwarding, configurable token endpoint authentication methods, and expanded scope handling based on extensive community testing.\
\
Read the release notes](https://github.com/jlowin/fastmcp/releases/tag/v2.12.1)

[​](https://gofastmcp.com/updates#fastmcp-2-12)

FastMCP 2.12

Releases

August 31, 2025

[FastMCP 2.12: Auth to the Races\
-------------------------------\
\
FastMCP 2.12 represents one of our most significant releases to date. After extensive testing and iteration with the community, we’re shipping major improvements to authentication, configuration, and MCP feature adoption.🔐 **OAuth Proxy** bridges the gap for providers that don’t support Dynamic Client Registration, enabling authentication with GitHub, Google, WorkOS, and Azure through minimal configuration.📋 **Declarative JSON Configuration** introduces `fastmcp.json` as the single source of truth for server settings, making MCP servers as portable and shareable as container images.🧠 **Sampling API Fallback** tackles adoption challenges by letting servers generate completions server-side when clients don’t support the feature, encouraging innovation while maintaining compatibility.\
\
Read the release notes](https://github.com/jlowin/fastmcp/releases/tag/v2.12.0)

[​](https://gofastmcp.com/updates#fastmcp-2-11)

FastMCP 2.11

Releases

August 1, 2025

[FastMCP 2.11: Auth to a Good Start\
----------------------------------\
\
FastMCP 2.11 brings enterprise-ready authentication and dramatic performance improvements.🔒 **Comprehensive OAuth 2.1 Support** with WorkOS AuthKit integration, Dynamic Client Registration, and support for separate resource and authorization servers.⚡ **Experimental OpenAPI Parser** delivers dramatic performance gains through single-pass schema processing and optimized memory usage (enable with environment variable).💾 **Enhanced State Management** provides persistent state across tool calls with a simple dictionary interface, improving context handling and type annotations.This release emphasizes speed and simplicity while setting the foundation for future enterprise features.\
\
Read the release notes](https://github.com/jlowin/fastmcp/releases/tag/v2.11.0)

[​](https://gofastmcp.com/updates#fastmcp-2-10)

FastMCP 2.10

Releases

July 2, 2025

[FastMCP 2.10: Great Spec-tations\
--------------------------------\
\
FastMCP 2.10 achieves full compliance with the 6/18/2025 MCP specification update, introducing powerful new communication patterns.💬 **Elicitation Support** enables dynamic server-client communication and “human-in-the-loop” workflows, allowing servers to request additional information during execution.📊 **Output Schemas** provide structured outputs for tools, making results more predictable and easier to parse programmatically.🛠️ **Enhanced HTTP Routing** with OpenAPI extensions support and configurable algorithms for more flexible API integration.This release includes a breaking change to `client.call_tool()` return signatures but significantly expands the interaction capabilities of MCP servers.\
\
Read the release notes](https://github.com/jlowin/fastmcp/releases/tag/v2.10.0)

[​](https://gofastmcp.com/updates#fastmcp-2-9)

FastMCP 2.9

ReleasesBlog Posts

June 23, 2025

[![_image?href=%2F_astro%2Fhero.BkVTdeBk](https://jlowin.dev/_image?href=%2F_astro%2Fhero.BkVTdeBk.jpg&w=1200&h=630&f=png)\
\
FastMCP 2.9: MCP-Native Middleware\
----------------------------------\
\
FastMCP 2.9 is a major release that, among other things, introduces two important features that push beyond the basic MCP protocol.🤝 _MCP Middleware_ brings a flexible middleware system for intercepting and controlling server operations - think authentication, logging, rate limiting, and custom business logic without touching core protocol code.✨ _Server-side type conversion_ for prompts solves a major developer pain point: while MCP requires string arguments, your functions can now work with native Python types like lists and dictionaries, with automatic conversion handling the complexity.These features transform FastMCP from a simple protocol implementation into a powerful framework for building sophisticated MCP applications. Combined with the new `File` utility for binary data and improvements to authentication and serialization, this release makes FastMCP significantly more flexible and developer-friendly while maintaining full protocol compliance.\
\
Read more](https://www.jlowin.dev/blog/fastmcp-2-9-middleware)

[​](https://gofastmcp.com/updates#fastmcp-2-8)

FastMCP 2.8

ReleasesBlog Posts

June 11, 2025

[![_image?href=%2F_astro%2Fhero.su3kspkP](https://www.jlowin.dev/_image?href=%2F_astro%2Fhero.su3kspkP.png&w=1000&h=500&f=webp)](https://www.jlowin.dev/blog/fastmcp-2-8-tool-transformation)

[](https://www.jlowin.dev/blog/fastmcp-2-8-tool-transformation)

[FastMCP 2.8: Transform and Roll Out\
-----------------------------------](https://www.jlowin.dev/blog/fastmcp-2-8-tool-transformation)

[FastMCP 2.8 is here, and it’s all about taking control of your tools.This release is packed with new features for curating the perfect LLM experience:🛠️ Tool TransformationThe headline feature lets you wrap any tool—from your own code, a third-party library, or an OpenAPI spec—to create an enhanced, LLM-friendly version. You can rename arguments, rewrite descriptions, and hide parameters without touching the original code.This feature was developed in close partnership with Bill Easton. As Bill brilliantly](https://www.jlowin.dev/blog/fastmcp-2-8-tool-transformation)
 [put it](https://www.linkedin.com/posts/williamseaston_huge-thanks-to-william-easton-for-providing-activity-7338011349525983232-Mw6T?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAAd6d0B3uL9zpCsq9eYWKi3HIvb8eN_r_Q)
, “Tool transformation flips Prompt Engineering on its head: stop writing tool-friendly LLM prompts and start providing LLM-friendly tools.”🏷️ Component ControlNow that you’re transforming tools, you need a way to hide the old ones! In FastMCP 2.8 you can programmatically enable/disable any component, and for everyone who’s been asking what FastMCP’s tags are for—they finally have a purpose! You can now use tags to declaratively filter which components are exposed to your clients.🚀 Pragmatic by DefaultLastly, to ensure maximum compatibility with the ecosystem, we’ve made the pragmatic decision to default all OpenAPI routes to Tools, making your entire API immediately accessible to any tool-using agent. When the industry catches up and supports resources, we’ll restore the old default — but no reason you should do extra work before OpenAI, Anthropic, or Google!

Read more

[​](https://gofastmcp.com/updates#fastmcp-2-7)

FastMCP 2.7

Releases

June 6, 2025

[![release-2-7](https://mintcdn.com/fastmcp/hUosZw7ujHZFemrG/assets/updates/release-2-7.png?fit=max&auto=format&n=hUosZw7ujHZFemrG&q=85&s=20d59e8a64fc284178c5e5ecf581a816)\
\
FastMCP 2.7: Pare Programming\
-----------------------------\
\
FastMCP 2.7 has been released!Most notably, it introduces the highly requested (and Pythonic) “naked” decorator usage:\
\
Copy\
\
    mcp = FastMCP()\
    \
    @mcp.tool\
    def add(a: int, b: int) -> int:\
        return a + b\
    \
\
In addition, decorators now return the objects they create, instead of the decorated function. This is an important usability enhancement.The bulk of the update is focused on improving the FastMCP internals, including a few breaking internal changes to private APIs. A number of functions that have clung on since 1.0 are now deprecated.\
\
Read the release notes](https://github.com/jlowin/fastmcp/releases/tag/v2.7.0)

[​](https://gofastmcp.com/updates#fastmcp-2-6)

FastMCP 2.6

ReleasesBlog Posts

June 2, 2025

[![_image?href=%2F_astro%2Fhero.Bsu8afiw](https://www.jlowin.dev/_image?href=%2F_astro%2Fhero.Bsu8afiw.png&w=1000&h=500&f=webp)\
\
FastMCP 2.6: Blast Auth\
-----------------------\
\
FastMCP 2.6 is here!This release introduces first-class authentication for MCP servers and clients, including pragmatic Bearer token support and seamless OAuth 2.1 integration. This release aligns with how major AI platforms are adopting MCP today, making it easier than ever to securely connect your tools to real-world AI models. Dive into the update and secure your stack with minimal friction.\
\
Read more](https://www.jlowin.dev/blog/fastmcp-2-6)

[​](https://gofastmcp.com/updates#vibe-testing)

Vibe-Testing

Blog PostsTutorials

May 21, 2025

[![_image?href=%2F_astro%2Fhero.BUPy9I9c](https://www.jlowin.dev/_image?href=%2F_astro%2Fhero.BUPy9I9c.png&w=1000&h=500&f=webp)\
\
Stop Vibe-Testing Your MCP Server\
---------------------------------\
\
Your tests are bad and you should feel bad.Stop vibe-testing your MCP server through LLM guesswork. FastMCP 2.0 introduces in-memory testing for fast, deterministic, and fully Pythonic validation of your MCP logic—no network, no subprocesses, no vibes.\
\
Read more](https://www.jlowin.dev/blog/stop-vibe-testing-mcp-servers)

[​](https://gofastmcp.com/updates#10%2C000-stars)

10,000 Stars

Blog Posts

May 8, 2025

[![_image?href=%2F_astro%2Fhero.Cnvci9Q_](https://www.jlowin.dev/_image?href=%2F_astro%2Fhero.Cnvci9Q_.png&w=1000&h=500&f=webp)\
\
Reflecting on FastMCP at 10k stars 🌟\
-------------------------------------\
\
In just six weeks since its relaunch, FastMCP has surpassed 10,000 GitHub stars—becoming the fastest-growing OSS project in our orbit. What started as a personal itch has become the backbone of Python-based MCP servers, powering a rapidly expanding ecosystem. While the protocol itself evolves, FastMCP continues to lead with clarity, developer experience, and opinionated tooling. Here’s to what’s next.\
\
Read more](https://www.jlowin.dev/blog/fastmcp-2-10k-stars)

[​](https://gofastmcp.com/updates#fastmcp-2-3)

FastMCP 2.3

Blog PostsReleases

May 8, 2025

[![_image?href=%2F_astro%2Fhero.M_hv6gEB](https://www.jlowin.dev/_image?href=%2F_astro%2Fhero.M_hv6gEB.png&w=1000&h=500&f=webp)\
\
Now Streaming: FastMCP 2.3\
--------------------------\
\
FastMCP 2.3 introduces full support for Streamable HTTP, a modern alternative to SSE that simplifies MCP deployments over the web. It’s efficient, reliable, and now the default HTTP transport. Just run your server with transport=“http” and connect clients via a standard URL—FastMCP handles the rest. No special setup required. This release makes deploying MCP servers easier and more portable than ever.\
\
Read more](https://www.jlowin.dev/blog/fastmcp-2-3-streamable-http)

[​](https://gofastmcp.com/updates#proxy-servers)

Proxy Servers

Blog PostsTutorials

April 23, 2025

[![_image?href=%2F_astro%2Frobot-hero.DpmAqgui](https://www.jlowin.dev/_image?href=%2F_astro%2Frobot-hero.DpmAqgui.png&w=1000&h=500&f=webp)\
\
MCP Proxy Servers with FastMCP 2.0\
----------------------------------\
\
Even AI needs a good travel adapter 🔌FastMCP now supports proxying arbitrary MCP servers, letting you run a local FastMCP instance that transparently forwards requests to any remote or third-party server—regardless of transport. This enables transport bridging (e.g., stdio ⇄ SSE), simplified client configuration, and powerful gateway patterns. Proxies are fully composable with other FastMCP servers, letting you mount or import them just like local servers. Use `FastMCP.from_client()` to wrap any backend in a clean, Pythonic proxy.\
\
Read more](https://www.jlowin.dev/blog/fastmcp-proxy)

[​](https://gofastmcp.com/updates#fastmcp-2-0)

FastMCP 2.0

ReleasesBlog Posts

April 16, 2025

[![_image?href=%2F_astro%2Fhero.DpbmGNrr](https://www.jlowin.dev/_image?href=%2F_astro%2Fhero.DpbmGNrr.png&w=1000&h=500&f=webp)\
\
Introducing FastMCP 2.0 🚀\
--------------------------\
\
This major release reimagines FastMCP as a full ecosystem platform, with powerful new features for composition, integration, and client interaction. You can now compose local and remote servers, proxy arbitrary MCP servers (with transport translation), and generate MCP servers from OpenAPI or FastAPI apps. A new client infrastructure supports advanced workflows like LLM sampling.FastMCP 2.0 builds on the success of v1 with a cleaner, more flexible foundation—try it out today!\
\
Read more](https://www.jlowin.dev/blog/fastmcp-2)

[​](https://gofastmcp.com/updates#official-sdk)

Official SDK

Announcements

December 3, 2024

[FastMCP is joining the official MCP Python SDK!\
-----------------------------------------------\
\
FastMCP 1.0 will become part of the official MCP Python SDK!\
\
Read the announcement](https://bsky.app/profile/jlowin.dev/post/3lch4xk5cf22c)

[​](https://gofastmcp.com/updates#fastmcp-1-0)

FastMCP 1.0

ReleasesBlog Posts

December 1, 2024

[![_image?href=%2F_astro%2Ffastmcp.Bep7YlTw](https://www.jlowin.dev/_image?href=%2F_astro%2Ffastmcp.Bep7YlTw.png&w=1000&h=500&f=webp)\
\
Introducing FastMCP 🚀\
----------------------\
\
Because life’s too short for boilerplate.This is where it all started. FastMCP’s launch post introduced a clean, Pythonic way to build MCP servers without the protocol overhead. Just write functions; FastMCP handles the rest. What began as a weekend project quickly became the foundation of a growing ecosystem.\
\
Read more](https://www.jlowin.dev/blog/introducing-fastmcp)

[Quickstart\
\
Previous](https://gofastmcp.com/getting-started/quickstart)
[The FastMCP Server\
\
Next](https://gofastmcp.com/servers/server)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.