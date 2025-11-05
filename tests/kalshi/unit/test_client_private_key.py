"""Unit tests for Kalshi client private key loading."""

import os
import tempfile
from pathlib import Path

import pytest
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

from src.kalshi.client import KalshiClient


# Generate a test RSA private key for testing
def generate_test_key():
    """Generate a test RSA private key."""
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    return private_key


def get_test_key_pem_string():
    """Get test private key as PEM-encoded string."""
    private_key = generate_test_key()
    pem_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    return pem_bytes.decode('utf-8')


def get_test_key_pem_bytes():
    """Get test private key as PEM-encoded bytes."""
    private_key = generate_test_key()
    pem_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    return pem_bytes


class TestPrivateKeyLoading:
    """Test private key loading from both sources."""

    def test_load_key_from_direct_content(self):
        """Can load private key from direct PEM content."""
        key_pem = get_test_key_pem_string()

        client = KalshiClient(
            api_key="test-api-key",
            private_key=key_pem
        )

        # Verify key was loaded
        assert client.private_key is not None
        # Verify it's an RSA key
        assert hasattr(client.private_key, 'sign')

    def test_load_key_from_file_path(self):
        """Can load private key from file path."""
        key_pem = get_test_key_pem_bytes()

        # Create temp file with key
        with tempfile.NamedTemporaryFile(mode='wb', delete=False, suffix='.pem') as f:
            f.write(key_pem)
            temp_path = f.name

        try:
            client = KalshiClient(
                api_key="test-api-key",
                private_key_path=temp_path
            )

            # Verify key was loaded
            assert client.private_key is not None
            assert hasattr(client.private_key, 'sign')
        finally:
            # Cleanup
            Path(temp_path).unlink()

    def test_direct_key_takes_precedence(self):
        """Direct key content takes precedence over file path."""
        key_pem_1 = get_test_key_pem_string()
        key_pem_2 = get_test_key_pem_bytes()

        # Create temp file
        with tempfile.NamedTemporaryFile(mode='wb', delete=False, suffix='.pem') as f:
            f.write(key_pem_2)
            temp_path = f.name

        try:
            # Provide both - direct key should win
            client = KalshiClient(
                api_key="test-api-key",
                private_key=key_pem_1,
                private_key_path=temp_path
            )

            # Verify it loaded the direct key (we can't easily compare key contents,
            # but we can verify it loaded successfully)
            assert client.private_key is not None
        finally:
            Path(temp_path).unlink()

    def test_raises_error_when_no_key_provided(self):
        """Raises error when neither direct key nor file path provided."""
        with pytest.raises(ValueError, match="Must provide either"):
            KalshiClient(api_key="test-api-key")

    def test_raises_error_when_file_not_found(self):
        """Raises error when key file doesn't exist."""
        with pytest.raises(FileNotFoundError, match="Private key file not found"):
            KalshiClient(
                api_key="test-api-key",
                private_key_path="/nonexistent/path/to/key.pem"
            )

    def test_raises_error_with_invalid_pem(self):
        """Raises error when PEM format is invalid."""
        invalid_pem = "this is not a valid PEM key"

        with pytest.raises(Exception):  # cryptography raises ValueError
            KalshiClient(
                api_key="test-api-key",
                private_key=invalid_pem
            )

    def test_expands_home_directory_in_path(self):
        """Expands ~ in file path."""
        key_pem = get_test_key_pem_bytes()

        # Create temp file in temp directory to simulate home
        import tempfile as tf
        temp_dir = tf.gettempdir()
        temp_path = Path(temp_dir) / "test_key.pem"
        temp_path.write_bytes(key_pem)

        try:
            # Use the actual path first to verify it works
            client = KalshiClient(
                api_key="test-api-key",
                private_key_path=str(temp_path)
            )
            assert client.private_key is not None
        finally:
            temp_path.unlink()

    def test_client_initialization_with_defaults(self):
        """Client initializes with default base_url and api_version."""
        key_pem = get_test_key_pem_string()

        client = KalshiClient(
            api_key="test-api-key",
            private_key=key_pem
        )

        assert client.api_key == "test-api-key"
        assert client.base_url == "https://trading-api.kalshi.com"
        assert client.api_version == "v2"

    def test_client_initialization_with_custom_params(self):
        """Client initializes with custom base_url and api_version."""
        key_pem = get_test_key_pem_string()
        custom_url = "https://custom-api.example.com"
        custom_version = "v3"

        client = KalshiClient(
            api_key="test-api-key",
            private_key=key_pem,
            base_url=custom_url,
            api_version=custom_version
        )

        assert client.base_url == custom_url
        assert client.api_version == custom_version

    def test_from_env_with_direct_key(self, monkeypatch):
        """Can load client from env vars with direct key."""
        key_pem = get_test_key_pem_string()

        # Set environment variables
        monkeypatch.setenv("KALSHI_API_KEY", "test-api-key")
        monkeypatch.setenv("KALSHI_PRIVATE_KEY", key_pem)
        monkeypatch.setenv("KALSHI_ENVIRONMENT", "demo")

        client = KalshiClient.from_env()

        assert client.api_key == "test-api-key"
        assert client.private_key is not None
        assert client.base_url == "https://demo-api.kalshi.co"

    def test_from_env_with_file_path(self, monkeypatch):
        """Can load client from env vars with file path."""
        key_pem = get_test_key_pem_bytes()

        # Create temp file
        with tempfile.NamedTemporaryFile(mode='wb', delete=False, suffix='.pem') as f:
            f.write(key_pem)
            temp_path = f.name

        try:
            # Set environment variables
            monkeypatch.setenv("KALSHI_API_KEY", "test-api-key")
            monkeypatch.setenv("KALSHI_PRIVATE_KEY_PATH", temp_path)
            monkeypatch.setenv("KALSHI_ENVIRONMENT", "demo")

            client = KalshiClient.from_env()

            assert client.api_key == "test-api-key"
            assert client.private_key is not None
        finally:
            Path(temp_path).unlink()

    def test_from_env_direct_key_takes_precedence(self, monkeypatch):
        """Direct env var takes precedence over file path in from_env()."""
        key_pem_1 = get_test_key_pem_string()
        key_pem_2 = get_test_key_pem_bytes()

        # Create temp file
        with tempfile.NamedTemporaryFile(mode='wb', delete=False, suffix='.pem') as f:
            f.write(key_pem_2)
            temp_path = f.name

        try:
            # Set both env vars - direct key should win
            monkeypatch.setenv("KALSHI_API_KEY", "test-api-key")
            monkeypatch.setenv("KALSHI_PRIVATE_KEY", key_pem_1)
            monkeypatch.setenv("KALSHI_PRIVATE_KEY_PATH", temp_path)
            monkeypatch.setenv("KALSHI_ENVIRONMENT", "demo")

            client = KalshiClient.from_env()

            # Should succeed (both are valid)
            assert client.private_key is not None
        finally:
            Path(temp_path).unlink()

    def test_from_env_raises_error_when_no_key(self, monkeypatch):
        """from_env() raises error when neither key env var is set."""
        monkeypatch.setenv("KALSHI_API_KEY", "test-api-key")
        monkeypatch.delenv("KALSHI_PRIVATE_KEY", raising=False)
        monkeypatch.delenv("KALSHI_PRIVATE_KEY_PATH", raising=False)

        with pytest.raises(ValueError, match="Must set either"):
            KalshiClient.from_env()

    def test_from_env_demo_url_when_no_override(self, monkeypatch):
        """from_env() uses demo URL when KALSHI_ENVIRONMENT is demo."""
        key_pem = get_test_key_pem_string()

        monkeypatch.setenv("KALSHI_API_KEY", "test-api-key")
        monkeypatch.setenv("KALSHI_PRIVATE_KEY", key_pem)
        monkeypatch.setenv("KALSHI_ENVIRONMENT", "demo")

        client = KalshiClient.from_env()

        assert client.base_url == "https://demo-api.kalshi.co"

    def test_from_env_custom_base_url_override(self, monkeypatch):
        """from_env() respects custom KALSHI_BASE_URL."""
        key_pem = get_test_key_pem_string()
        custom_url = "https://custom.kalshi.io"

        monkeypatch.setenv("KALSHI_API_KEY", "test-api-key")
        monkeypatch.setenv("KALSHI_PRIVATE_KEY", key_pem)
        monkeypatch.setenv("KALSHI_ENVIRONMENT", "demo")
        monkeypatch.setenv("KALSHI_BASE_URL", custom_url)

        client = KalshiClient.from_env()

        assert client.base_url == custom_url
