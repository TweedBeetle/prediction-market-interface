---
url: https://gofastmcp.com/servers/auth/full-oauth-server
title: Full OAuth Server - FastMCP
description: Build a self-contained authentication system where your FastMCP server manages users, issues tokens, and validates them.
scraped_at: 2025-11-03T18:43:11.723734
---

[Skip to main content](https://gofastmcp.com/servers/auth/full-oauth-server#content-area)

Join the [FastMCP community](https://discord.gg/uu8dJCgttd)
!

[FastMCP home page![light logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=67680e9b1c641023511881a24f296077)![dark logo](https://mintcdn.com/fastmcp/Lu2sdJVHDyHdvswk/assets/brand/wordmark-white.png?fit=max&auto=format&n=Lu2sdJVHDyHdvswk&q=85&s=776d9c0663633c9b9782b9f3f9785960)](https://gofastmcp.com/)

Search...

Navigation

Authentication

Full OAuth Server

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
    
    *   [Overview](https://gofastmcp.com/servers/auth/authentication)
        
    *   [Token Verification](https://gofastmcp.com/servers/auth/token-verification)
        
    *   [Remote OAuth\
        \
        NEW](https://gofastmcp.com/servers/auth/remote-oauth)
        
    *   [OAuth Proxy\
        \
        NEW](https://gofastmcp.com/servers/auth/oauth-proxy)
        
    *   [OIDC Proxy\
        \
        NEW](https://gofastmcp.com/servers/auth/oidc-proxy)
        
    *   [Full OAuth Server](https://gofastmcp.com/servers/auth/full-oauth-server)
        
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
    

On this page

*   [OAuthProvider](https://gofastmcp.com/servers/auth/full-oauth-server#oauthprovider)
    
*   [Required Implementation](https://gofastmcp.com/servers/auth/full-oauth-server#required-implementation)
    
*   [Client Management](https://gofastmcp.com/servers/auth/full-oauth-server#client-management)
    
*   [Authorization Flow](https://gofastmcp.com/servers/auth/full-oauth-server#authorization-flow)
    
*   [Token Management](https://gofastmcp.com/servers/auth/full-oauth-server#token-management)
    

`` New in version: `2.11.0` ``

**This is an extremely advanced pattern that most users should avoid.** Building a secure OAuth 2.1 server requires deep expertise in authentication protocols, cryptography, and security best practices. The complexity extends far beyond initial implementation to include ongoing security monitoring, threat response, and compliance maintenance.**Use [Remote OAuth](https://gofastmcp.com/servers/auth/remote-oauth)
 instead** unless you have compelling requirements that external identity providers cannot meet, such as air-gapped environments or specialized compliance needs.

The Full OAuth Server pattern exists to support the MCP protocol specification’s requirements. Your FastMCP server becomes both an Authorization Server and Resource Server, handling the complete authentication lifecycle from user login to token validation. This documentation exists for completeness - the vast majority of applications should use external identity providers instead.

[​](https://gofastmcp.com/servers/auth/full-oauth-server#oauthprovider)

OAuthProvider
----------------------------------------------------------------------------------------

FastMCP provides the `OAuthProvider` abstract class that implements the OAuth 2.1 specification. To use this pattern, you must subclass `OAuthProvider` and implement all required abstract methods.

`OAuthProvider` handles OAuth endpoints, protocol flows, and security requirements, but delegates all storage, user management, and business logic to your implementation of the abstract methods.

[​](https://gofastmcp.com/servers/auth/full-oauth-server#required-implementation)

Required Implementation
------------------------------------------------------------------------------------------------------------

You must implement these abstract methods to create a functioning OAuth server:

### 

[​](https://gofastmcp.com/servers/auth/full-oauth-server#client-management)

Client Management

Client Management Methods
-------------------------

[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-get-client)

get\_client

async method

Retrieve client information by ID from your database.

Show Parameters

[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-client-id)

client\_id

str

Client identifier to look up

Show Returns

[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-o-auth-client-information-full-none)

OAuthClientInformationFull | None

return type

Client information object or `None` if client not found

[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-register-client)

register\_client

async method

Store new client registration information in your database.

Show Parameters

[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-client-info)

client\_info

OAuthClientInformationFull

Complete client registration information to store

Show Returns

[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-none)

None

return type

No return value

### 

[​](https://gofastmcp.com/servers/auth/full-oauth-server#authorization-flow)

Authorization Flow

Authorization Flow Methods
--------------------------

[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-authorize)

authorize

async method

Handle authorization request and return redirect URL. Must implement user authentication and consent collection.

Show Parameters

[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-client)

client

OAuthClientInformationFull

OAuth client making the authorization request

[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-params)

params

AuthorizationParams

Authorization request parameters from the client

Show Returns

[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-str)

str

return type

Redirect URL to send the client to

[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-load-authorization-code)

load\_authorization\_code

async method

Load authorization code from storage by code string. Return `None` if code is invalid or expired.

Show Parameters

[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-client-1)

client

OAuthClientInformationFull

OAuth client attempting to use the authorization code

[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-authorization-code)

authorization\_code

str

Authorization code string to look up

Show Returns

[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-authorization-code-none)

AuthorizationCode | None

return type

Authorization code object or `None` if not found

### 

[​](https://gofastmcp.com/servers/auth/full-oauth-server#token-management)

Token Management

Token Management Methods
------------------------

[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-exchange-authorization-code)

exchange\_authorization\_code

async method

Exchange authorization code for access and refresh tokens. Must validate code and create new tokens.

Show Parameters

[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-client-2)

client

OAuthClientInformationFull

OAuth client exchanging the authorization code

[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-authorization-code-1)

authorization\_code

AuthorizationCode

Valid authorization code object to exchange

Show Returns

[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-o-auth-token)

OAuthToken

return type

New OAuth token containing access and refresh tokens

[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-load-refresh-token)

load\_refresh\_token

async method

Load refresh token from storage by token string. Return `None` if token is invalid or expired.

Show Parameters

[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-client-3)

client

OAuthClientInformationFull

OAuth client attempting to use the refresh token

[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-refresh-token)

refresh\_token

str

Refresh token string to look up

Show Returns

[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-refresh-token-none)

RefreshToken | None

return type

Refresh token object or `None` if not found

[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-exchange-refresh-token)

exchange\_refresh\_token

async method

Exchange refresh token for new access/refresh token pair. Must validate scopes and token.

Show Parameters

[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-client-4)

client

OAuthClientInformationFull

OAuth client using the refresh token

[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-refresh-token-1)

refresh\_token

RefreshToken

Valid refresh token object to exchange

[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-scopes)

scopes

list\[str\]

Requested scopes for the new access token

Show Returns

[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-o-auth-token-1)

OAuthToken

return type

New OAuth token with updated access and refresh tokens

[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-load-access-token)

load\_access\_token

async method

Load an access token by its token string.

Show Parameters

[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-token)

token

str

The access token to verify

Show Returns

[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-access-token-none)

AccessToken | None

return type

The access token object, or `None` if the token is invalid

[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-revoke-token)

revoke\_token

async method

Revoke access or refresh token, marking it as invalid in storage.

Show Parameters

[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-token-1)

token

AccessToken | RefreshToken

Token object to revoke and mark invalid

Show Returns

[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-none-1)

None

return type

No return value

[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-verify-token)

verify\_token

async method

Verify bearer token for incoming requests. Return `AccessToken` if valid, `None` if invalid.

Show Parameters

[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-token-2)

token

str

Bearer token string from incoming request

Show Returns

[​](https://gofastmcp.com/servers/auth/full-oauth-server#param-access-token-none-1)

AccessToken | None

return type

Access token object if valid, `None` if invalid or expired

Each method must handle storage, validation, security, and error cases according to the OAuth 2.1 specification. The implementation complexity is substantial and requires expertise in OAuth security considerations.

**Security Notice:** OAuth server implementation involves numerous security considerations including PKCE, state parameters, redirect URI validation, token binding, replay attack prevention, and secure storage requirements. Mistakes can lead to serious security vulnerabilities.

[OIDC Proxy\
\
Previous](https://gofastmcp.com/servers/auth/oidc-proxy)
[Running Your Server\
\
Next](https://gofastmcp.com/deployment/running-server)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.