"""Tests for MCP server startup and credential validation.

These tests verify that the Kalshi MCP server validates credentials at module
load time (fail-fast pattern) and provides clear error messages when credentials
are missing.
"""

import subprocess
import sys
from pathlib import Path

import pytest


@pytest.mark.unit
class TestMCPServerCredentialValidation:
    """Test fail-fast credential validation at MCP server startup."""

    def test_mcp_server_fails_without_api_key_id(self, tmp_path, test_private_key_pem):
        """Test that MCP server startup fails with clear error if KALSHI_API_KEY_ID missing."""
        # Create a test script that tries to import the server without API_KEY_ID
        test_script = tmp_path / "test_import.py"
        test_script.write_text(
            """
import os
import sys

# Unset KALSHI_API_KEY_ID, but set the private key
os.environ.pop("KALSHI_API_KEY_ID", None)
os.environ["KALSHI_PRIVATE_KEY_PATH"] = sys.argv[1]

try:
    from src.kalshi.kalshi_mcp_server import mcp
    print("ERROR: Server imported without KALSHI_API_KEY_ID!")
    sys.exit(1)
except ValueError as e:
    if "KALSHI_API_KEY_ID" in str(e):
        print(f"SUCCESS: {e}")
        sys.exit(0)
    else:
        print(f"ERROR: Wrong error message: {e}")
        sys.exit(1)
except Exception as e:
    print(f"ERROR: Unexpected exception: {type(e).__name__}: {e}")
    sys.exit(1)
"""
        )

        # Run the test script in a subprocess
        result = subprocess.run(
            [sys.executable, str(test_script), test_private_key_pem],
            cwd=Path(__file__).parent.parent.parent,
            capture_output=True,
            text=True,
        )

        assert result.returncode == 0, f"Expected exit 0, got {result.returncode}. Output: {result.stdout}{result.stderr}"
        assert "KALSHI_API_KEY_ID" in result.stdout

    def test_mcp_server_fails_without_private_key_path(self, tmp_path):
        """Test that MCP server startup fails with clear error if KALSHI_PRIVATE_KEY_PATH missing."""
        # Create a test script that tries to import the server without PRIVATE_KEY_PATH
        test_script = tmp_path / "test_import.py"
        test_script.write_text(
            """
import os

# Set API_KEY_ID but unset KALSHI_PRIVATE_KEY_PATH
os.environ["KALSHI_API_KEY_ID"] = "test-key-id"
os.environ.pop("KALSHI_PRIVATE_KEY_PATH", None)

try:
    from src.kalshi.kalshi_mcp_server import mcp
    print("ERROR: Server imported without KALSHI_PRIVATE_KEY_PATH!")
    exit(1)
except ValueError as e:
    if "KALSHI_PRIVATE_KEY_PATH" in str(e):
        print(f"SUCCESS: {e}")
        exit(0)
    else:
        print(f"ERROR: Wrong error message: {e}")
        exit(1)
except Exception as e:
    print(f"ERROR: Unexpected exception: {type(e).__name__}: {e}")
    exit(1)
"""
        )

        # Run the test script in a subprocess
        result = subprocess.run(
            [sys.executable, str(test_script)],
            cwd=Path(__file__).parent.parent.parent,
            capture_output=True,
            text=True,
        )

        assert result.returncode == 0, f"Expected exit 0, got {result.returncode}. Output: {result.stdout}{result.stderr}"
        assert "KALSHI_PRIVATE_KEY_PATH" in result.stdout

    def test_mcp_server_error_message_is_helpful(self, tmp_path, test_private_key_pem):
        """Test that error messages guide users to documentation."""
        test_script = tmp_path / "test_import.py"
        test_script.write_text(
            """
import os
import sys

os.environ.pop("KALSHI_API_KEY_ID", None)
os.environ["KALSHI_PRIVATE_KEY_PATH"] = sys.argv[1]

try:
    from src.kalshi.kalshi_mcp_server import mcp
except ValueError as e:
    error_msg = str(e)
    # Check that error message includes helpful guidance
    has_env_var_name = "KALSHI_API_KEY_ID" in error_msg
    has_setup_hint = ".env file" in error_msg or "environment" in error_msg
    has_docs_link = "CLAUDE.md" in error_msg or "setup" in error_msg

    if has_env_var_name and has_setup_hint:
        print("SUCCESS: Error message is helpful")
        exit(0)
    else:
        print(f"ERROR: Error message missing helpful info. Got: {error_msg}")
        exit(1)
"""
        )

        result = subprocess.run(
            [sys.executable, str(test_script), test_private_key_pem],
            cwd=Path(__file__).parent.parent.parent,
            capture_output=True,
            text=True,
        )

        assert result.returncode == 0, f"Error message not helpful. Output: {result.stdout}{result.stderr}"

    def test_mcp_server_initializes_with_valid_credentials(self, mock_kalshi_client, kalshi_mcp_server):
        """Test that MCP server initializes successfully with valid credentials."""
        # This test uses the kalshi_mcp_server fixture which sets credentials before import
        assert kalshi_mcp_server is not None
        # Server should be a FastMCP instance
        assert kalshi_mcp_server.__class__.__name__ == "FastMCP"
        # Server should have _tool_manager (internal tracking)
        assert hasattr(kalshi_mcp_server, "_tool_manager")


@pytest.mark.unit
class TestMCPServerModuleValidation:
    """Test that credentials are validated at module load (not deferred)."""

    def test_credentials_validated_at_import_not_at_tool_call(self, tmp_path, test_private_key_pem):
        """Verify fail-fast: credentials validated when module is imported, not when tools are called.

        This is the key difference from lazy validation. The server should fail
        at `import kalshi_mcp_server`, not at `await kalshi_search_markets()`.
        """
        test_script = tmp_path / "test_import.py"
        test_script.write_text(
            """
import os
import sys

# Missing credentials
os.environ.pop("KALSHI_API_KEY_ID", None)
os.environ["KALSHI_PRIVATE_KEY_PATH"] = sys.argv[1]

# Try to import the module
try:
    # This import should fail immediately, not later
    from src.kalshi.kalshi_mcp_server import mcp
    print("ERROR: Module imported successfully even with missing credentials!")
    print("This suggests validation is deferred (lazy), not fail-fast")
    sys.exit(1)
except ValueError as e:
    # Expected: validation happens at import time
    if "KALSHI_API_KEY_ID" in str(e):
        print("SUCCESS: Validation is fail-fast (happens at import)")
        sys.exit(0)
except Exception as e:
    print(f"ERROR: Unexpected exception type: {type(e).__name__}: {e}")
    sys.exit(1)
"""
        )

        result = subprocess.run(
            [sys.executable, str(test_script), test_private_key_pem],
            cwd=Path(__file__).parent.parent.parent,
            capture_output=True,
            text=True,
        )

        assert result.returncode == 0, (
            f"Validation is not fail-fast. Output: {result.stdout}{result.stderr}"
        )


@pytest.mark.unit
class TestMCPServerLazyClientInitialization:
    """Test that client is lazy-initialized (on first tool call, not at server startup)."""

    def test_client_is_none_after_server_import(self, kalshi_mcp_server):
        """Verify that client is not initialized when server imports."""
        # Import the module to get access to the global client variable
        from src.kalshi.kalshi_mcp_server import client

        # Client should not be initialized yet (None)
        assert client is None, "Client should be lazily initialized, not at server startup"

    def test_ensure_client_initializes_on_first_call(self, kalshi_mcp_server):
        """Verify that _ensure_client() creates the client on first call."""
        from src.kalshi.kalshi_mcp_server import _ensure_client, client as initial_client

        # Before calling _ensure_client, client should be None
        assert initial_client is None

        # Call _ensure_client
        client_instance = _ensure_client()

        # Should return a KalshiClient instance
        from src.kalshi.client import KalshiClient

        assert isinstance(client_instance, KalshiClient)

    def test_ensure_client_reuses_cached_client(self, kalshi_mcp_server):
        """Verify that _ensure_client() returns the same client on subsequent calls."""
        from src.kalshi.kalshi_mcp_server import _ensure_client

        # First call creates the client
        client1 = _ensure_client()

        # Second call should return the same instance
        client2 = _ensure_client()

        # Should be the exact same object (not just equal)
        assert client1 is client2, "Client should be cached and reused"


@pytest.mark.unit
class TestMCPServerStartupWithEnv:
    """Test server startup with environment variables set correctly."""

    def test_server_starts_with_both_env_vars_set(self, kalshi_mcp_server):
        """Test that server initializes successfully when both env vars are set."""
        # The kalshi_mcp_server fixture sets env vars before importing
        assert kalshi_mcp_server is not None

        # Server should be a FastMCP instance with tool manager
        assert kalshi_mcp_server.__class__.__name__ == "FastMCP"
        assert hasattr(kalshi_mcp_server, "_tool_manager")
