# FastMCP Testing Guide

## Overview

FastMCP testing patterns validated through Context7 and web research. This document consolidates best practices for testing Kalshi MCP server.

## Core Testing Patterns

### 1. In-Memory Testing (Recommended for Unit Tests)

**Pattern**: Connect client directly to server instance without network overhead.

```python
from fastmcp import FastMCP, Client

# Create server with tools
server = FastMCP("Kalshi Prediction Markets")

@server.tool
def kalshi_search_markets(status: str = None) -> dict:
    """Search markets"""
    pass

# Test in-memory (no subprocess, no network)
async def test_search_markets():
    async with Client(server) as client:
        result = await client.call_tool("kalshi_search_markets", {"status": "open"})
        assert result.data is not None
```

**Benefits**:
- Fast execution (no network overhead)
- Deterministic results
- Easy debugging
- No subprocess management

### 2. Pytest Fixtures for Reusable Setup

**Pattern**: Use fixtures to avoid duplicating server setup across tests.

```python
@pytest.fixture
def kalshi_server():
    """Reusable FastMCP server fixture."""
    mcp = FastMCP("Kalshi Prediction Markets")

    @mcp.tool
    def kalshi_search_markets(status: Optional[str] = None) -> dict:
        """Search markets"""
        # Implementation
        pass

    return mcp

async def test_with_fixture(kalshi_server):
    """Test using the fixture."""
    async with Client(kalshi_server) as client:
        result = await client.call_tool("kalshi_search_markets", {})
        assert result is not None
```

### 3. Tool Registration Validation

**Pattern**: Access internal tool manager to verify registration.

```python
def test_all_tools_registered(kalshi_mcp_server):
    """Verify all 29 tools are registered."""
    tools_dict = kalshi_mcp_server._tool_manager._tools

    expected_tools = [
        "kalshi_search_markets",
        "kalshi_get_balance",
        "kalshi_create_order",
        # ... etc
    ]

    tool_names = set(tools_dict.keys())
    for expected in expected_tools:
        assert expected in tool_names

def test_tool_has_parameters(kalshi_mcp_server):
    """Verify tool has expected parameters."""
    tools_dict = kalshi_mcp_server._tool_manager._tools
    tool = tools_dict["kalshi_search_markets"]

    assert tool.description is not None
    assert tool.parameters is not None

    schema_props = tool.parameters.get("properties", {})
    assert "status" in schema_props or "limit" in schema_props
```

### 4. Mocking External Dependencies

**Pattern**: Use `unittest.mock.AsyncMock` for external API calls.

```python
from unittest.mock import AsyncMock, patch

async def test_search_markets_with_mock():
    """Test tool with mocked API client."""
    mcp = FastMCP("Test")

    @mcp.tool
    async def kalshi_search_markets(status: str = None) -> dict:
        client = KalshiClient()
        markets, _ = await client.search_markets(status=status)
        return {"markets": [m.model_dump() for m in markets]}

    # Mock the KalshiClient
    with patch.object(KalshiClient, "search_markets", new_callable=AsyncMock) as mock:
        mock.return_value = ([sample_market], None)

        async with Client(mcp) as client:
            result = await client.call_tool("kalshi_search_markets", {})
            assert result.data["markets"][0]["ticker"] == "TEST"
```

### 5. Tool Execution Testing

**Pattern**: Call tools through client to test end-to-end behavior.

```python
async def test_tool_execution(kalshi_server):
    """Test actual tool execution."""
    async with Client(kalshi_server) as client:
        # List available tools
        tools = await client.list_tools()
        tool_names = [t.name for t in tools]
        assert "kalshi_search_markets" in tool_names

        # Call a tool
        result = await client.call_tool(
            "kalshi_search_markets",
            {"status": "open", "limit": 10}
        )

        # Verify result structure
        assert "markets" in result.data
        assert isinstance(result.data["markets"], list)
```

### 6. Atomic Tests (Single Responsibility)

**Good Practice**: Each test validates one specific behavior.

```python
# ✅ GOOD - Single assertion
def test_mcp_server_initialization(kalshi_mcp_server):
    """Test that FastMCP server is properly initialized."""
    assert kalshi_mcp_server is not None
    assert kalshi_mcp_server.name == "Kalshi Prediction Markets"

# ✅ GOOD - One behavior per test
def test_all_readonly_tools_registered(kalshi_mcp_server):
    """Test that all 8 read-only tools are registered."""
    tools_dict = kalshi_mcp_server._tool_manager._tools
    tool_names = set(tools_dict.keys())

    readonly_tools = [
        "kalshi_search_markets",
        "kalshi_get_market",
        # ... etc
    ]

    for tool_name in readonly_tools:
        assert tool_name in tool_names, f"Missing tool: {tool_name}"

# ❌ BAD - Multiple behaviors
def test_server_everything():
    """Test multiple features at once."""
    # This mixes tool registration, parameter validation, and execution
    # If it fails, you don't know what broke
    assert mcp.list_tools()
    assert mcp.list_resources()
    assert mcp.auth is not None
```

### 7. Integration Testing with Network Transports

**Pattern**: Test with actual network transports using fixtures.

```python
@pytest.fixture
async def http_server():
    """Run MCP server in subprocess on HTTP transport."""
    from fastmcp.utilities.tests import run_server_in_process

    def run_server(host: str, port: int):
        server = FastMCP("Test")
        @server.tool
        def greet(name: str) -> str:
            return f"Hello, {name}!"
        server.run(host=host, port=port)

    with run_server_in_process(run_server, transport="http") as url:
        yield f"{url}/mcp"

async def test_http_transport(http_server):
    """Test with actual HTTP transport."""
    from fastmcp.client.transports import StreamableHttpTransport

    async with Client(transport=StreamableHttpTransport(http_server)) as client:
        result = await client.ping()
        assert result is True
```

## Kalshi Project Testing Strategy

### Test Organization

1. **test_auth.py** (23 tests) - RSA-PSS authentication
   - Signature generation
   - Header validation
   - Private key handling

2. **test_models.py** (37 tests) - Pydantic models
   - Data validation
   - Enum validation
   - Serialization

3. **test_client.py** (41 tests) - API client
   - Initialization
   - Method signatures
   - Error handling

4. **test_mcp_tools.py** (11 tests) - MCP tool registration
   - Tool registration verification
   - Parameter validation
   - Tool descriptions

5. **test_api.py** (pending, 10 tests) - API integration with VCR.py
   - Real API response recording
   - Pagination testing
   - Error response handling

### Coverage Goals

- **Overall**: 80%+ coverage
- **Authentication**: 100% (critical security path)
- **Models**: 100% (data integrity)
- **Client**: 70%+ (API integration)
- **MCP Server**: 75%+ (tool functionality)

## Running Tests

```bash
# All tests
uv run pytest tests/kalshi/ -v

# Unit tests only (fast)
uv run pytest tests/kalshi/ -m "unit" -v

# With coverage
uv run pytest tests/kalshi/ --cov=src/kalshi --cov-report=html

# Specific file
uv run pytest tests/kalshi/test_mcp_tools.py -v
```

## Key Learnings from FastMCP Research

### 1. FunctionTool Objects Are Not Directly Callable

When FastMCP registers a tool with `@mcp.tool()`, the decorated function becomes a `FunctionTool` object, NOT a callable. To access tools for testing:

```python
# ❌ WRONG
from src.kalshi.kalshi_mcp_server import kalshi_search_markets
assert callable(kalshi_search_markets)  # FAILS - it's a FunctionTool

# ✅ CORRECT
tools_dict = mcp_server._tool_manager._tools
tool = tools_dict["kalshi_search_markets"]  # Access as FunctionTool object
assert tool.description is not None
assert tool.parameters is not None
```

### 2. Tool Parameter Schema

FunctionTool objects have a `parameters` dict (not `inputSchema`):

```python
# ❌ WRONG
assert tool.inputSchema is not None

# ✅ CORRECT
schema_props = tool.parameters.get("properties", {})
assert "status" in schema_props
```

### 3. Tool Execution Testing

To actually execute tools, use the FastMCP Client pattern:

```python
async with Client(server) as client:
    result = await client.call_tool("tool_name", {"arg": "value"})
    assert result.data == expected_data
```

## Next Steps

1. Create test_api.py with 10 VCR.py-based integration tests
2. Implement rate limiter with token bucket
3. Implement WebSocket manager
4. Achieve 80%+ overall coverage

## References

- FastMCP Testing Documentation: https://gofastmcp.com/patterns/testing
- MCP Unit Testing Guide: https://mcpcat.io/guides/writing-unit-tests-mcp-servers/
- Blog: "Stop Vibe-Testing Your MCP Server": https://www.jlowin.dev/blog/stop-vibe-testing-mcp-servers
