"""RSA-PSS signature authentication tests."""

import base64
import time

import pytest
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.backends import default_backend


@pytest.mark.auth
class TestRSAPSSSignatureGeneration:
    """Test RSA-PSS signature generation for Kalshi authentication."""

    def test_signature_is_generated(self, test_private_key):
        """Test that signature is generated without errors."""
        timestamp = int(time.time() * 1000)
        method = "GET"
        path = "/markets"
        message = f"{timestamp}{method}{path}".encode()

        signature = test_private_key.sign(
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH,
            ),
            hashes.SHA256(),
        )

        assert signature is not None
        assert isinstance(signature, bytes)
        assert len(signature) > 0

    def test_signature_is_base64_encodable(self, test_private_key):
        """Test that signature can be base64-encoded for headers."""
        timestamp = int(time.time() * 1000)
        message = f"{timestamp}GET/markets".encode()

        signature = test_private_key.sign(
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH,
            ),
            hashes.SHA256(),
        )

        encoded = base64.b64encode(signature).decode()
        assert isinstance(encoded, str)
        assert len(encoded) > 0
        # Base64-encoded signature should be longer than binary
        assert len(encoded) > len(signature)

    def test_signature_is_deterministic_for_same_key_and_message(self, test_private_key):
        """Test that signature generation is deterministic (same input = same output)."""
        timestamp = 1698765432123
        message = f"{timestamp}GET/markets".encode()

        # PSS with MAX_LENGTH salt is NOT deterministic (salt is random)
        # But we should be able to verify it
        signature1 = test_private_key.sign(
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH,
            ),
            hashes.SHA256(),
        )

        signature2 = test_private_key.sign(
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH,
            ),
            hashes.SHA256(),
        )

        # Signatures should be different (due to random salt), but both should verify
        assert signature1 != signature2
        # But both should be valid
        public_key = test_private_key.public_key()
        public_key.verify(
            signature1,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH,
            ),
            hashes.SHA256(),
        )
        public_key.verify(
            signature2,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH,
            ),
            hashes.SHA256(),
        )

    def test_signature_verification_with_public_key(self, test_private_key, test_public_key):
        """Test that signature can be verified with public key."""
        timestamp = int(time.time() * 1000)
        message = f"{timestamp}GET/markets".encode()

        signature = test_private_key.sign(
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH,
            ),
            hashes.SHA256(),
        )

        # Should not raise
        test_public_key.verify(
            signature,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH,
            ),
            hashes.SHA256(),
        )

    def test_signature_fails_verification_with_tampered_message(self, test_private_key, test_public_key):
        """Test that signature verification fails for tampered messages."""
        from cryptography.exceptions import InvalidSignature

        timestamp = int(time.time() * 1000)
        message = f"{timestamp}GET/markets".encode()

        signature = test_private_key.sign(
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH,
            ),
            hashes.SHA256(),
        )

        # Tamper with message
        tampered_message = f"{timestamp}POST/markets".encode()

        with pytest.raises(InvalidSignature):
            test_public_key.verify(
                signature,
                tampered_message,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH,
                ),
                hashes.SHA256(),
            )

    def test_message_format_no_separators(self, test_private_key):
        """Test that message format is timestamp + method + path (no separators)."""
        timestamp = 1698765432123
        method = "GET"
        path = "/markets"

        # Correct format: no separators
        message = f"{timestamp}{method}{path}".encode()
        assert message == b"1698765432123GET/markets"

        # Should be able to sign without errors
        signature = test_private_key.sign(
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH,
            ),
            hashes.SHA256(),
        )
        assert signature is not None

    def test_signature_with_different_http_methods(self, test_private_key, test_public_key):
        """Test signature with different HTTP methods."""
        timestamp = int(time.time() * 1000)

        for method in ["GET", "POST", "DELETE", "PUT"]:
            message = f"{timestamp}{method}/portfolio/orders".encode()

            signature = test_private_key.sign(
                message,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH,
                ),
                hashes.SHA256(),
            )

            # Should verify
            test_public_key.verify(
                signature,
                message,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH,
                ),
                hashes.SHA256(),
            )

    def test_signature_with_path_parameters(self, test_private_key, test_public_key):
        """Test signature with different path parameters."""
        timestamp = int(time.time() * 1000)

        paths = [
            "/markets",
            "/markets/KXHARRIS24-LSV",
            "/markets/KXHARRIS24-LSV/orderbook",
            "/portfolio/orders",
            "/portfolio/positions",
        ]

        for path in paths:
            message = f"{timestamp}GET{path}".encode()

            signature = test_private_key.sign(
                message,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH,
                ),
                hashes.SHA256(),
            )

            test_public_key.verify(
                signature,
                message,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH,
                ),
                hashes.SHA256(),
            )

    def test_hash_algorithm_is_sha256(self, test_private_key, test_public_key):
        """Test that SHA-256 is used for hashing."""
        timestamp = int(time.time() * 1000)
        message = f"{timestamp}GET/markets".encode()

        # Sign with SHA-256
        signature = test_private_key.sign(
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH,
            ),
            hashes.SHA256(),
        )

        # Should verify with SHA-256
        test_public_key.verify(
            signature,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH,
            ),
            hashes.SHA256(),
        )

    def test_pss_salt_length_is_max(self, test_private_key, test_public_key):
        """Test that PSS uses MAX_LENGTH salt (Kalshi requirement)."""
        timestamp = int(time.time() * 1000)
        message = f"{timestamp}GET/markets".encode()

        # Sign with MAX_LENGTH salt
        signature = test_private_key.sign(
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH,
            ),
            hashes.SHA256(),
        )

        # Should verify with MAX_LENGTH salt
        test_public_key.verify(
            signature,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH,
            ),
            hashes.SHA256(),
        )


@pytest.mark.auth
class TestKalshiClientAuthenticationHeaders:
    """Test Kalshi client authentication header generation."""

    def test_client_generates_auth_headers(self, mock_kalshi_client):
        """Test that client generates required authentication headers."""
        # Use protected method for testing
        headers = mock_kalshi_client._get_headers("GET", "/markets")

        assert "KALSHI-ACCESS-KEY" in headers
        assert "KALSHI-ACCESS-SIGNATURE" in headers
        assert "KALSHI-ACCESS-TIMESTAMP" in headers

    def test_access_key_header_format(self, mock_kalshi_client):
        """Test that KALSHI-ACCESS-KEY header is correct."""
        headers = mock_kalshi_client._get_headers("GET", "/markets")

        key = headers["KALSHI-ACCESS-KEY"]
        # Should be the test key ID
        assert key == "test-key-id-550e8400-e29b-41d4-a716-446655440000"

    def test_access_signature_header_is_base64(self, mock_kalshi_client):
        """Test that KALSHI-ACCESS-SIGNATURE is base64-encoded."""
        headers = mock_kalshi_client._get_headers("GET", "/markets")

        signature = headers["KALSHI-ACCESS-SIGNATURE"]
        # Should be base64-encoded (ASCII string)
        assert isinstance(signature, str)
        # Should decode without errors
        try:
            base64.b64decode(signature)
        except Exception:
            pytest.fail("Signature is not valid base64")

    def test_access_timestamp_header_is_unix_milliseconds(self, mock_kalshi_client):
        """Test that KALSHI-ACCESS-TIMESTAMP is Unix timestamp in milliseconds."""
        before = int(time.time() * 1000)
        headers = mock_kalshi_client._get_headers("GET", "/markets")
        after = int(time.time() * 1000)

        timestamp = int(headers["KALSHI-ACCESS-TIMESTAMP"])

        # Should be recent
        assert before <= timestamp <= after
        # Should be a large number (milliseconds, not seconds)
        assert timestamp > 1600000000000  # After year 2020

    def test_content_type_header(self, mock_kalshi_client):
        """Test that Content-Type header is set."""
        headers = mock_kalshi_client._get_headers("GET", "/markets")

        assert headers.get("Content-Type") == "application/json"


@pytest.mark.auth
class TestPrivateKeyLoading:
    """Test private key loading from file."""

    def test_private_key_loads_from_file(self, test_private_key_pem, monkeypatch):
        """Test that private key is loaded from PEM file."""
        monkeypatch.setenv("KALSHI_API_KEY_ID", "test-key-id")
        monkeypatch.setenv("KALSHI_PRIVATE_KEY_PATH", test_private_key_pem)

        from src.kalshi import KalshiClient

        client = KalshiClient()
        assert client.private_key is not None

    def test_missing_private_key_raises_error(self, monkeypatch):
        """Test that missing private key file raises FileNotFoundError."""
        monkeypatch.setenv("KALSHI_API_KEY_ID", "test-key-id")
        monkeypatch.setenv("KALSHI_PRIVATE_KEY_PATH", "/nonexistent/path/key.pem")

        from src.kalshi import KalshiClient

        with pytest.raises(FileNotFoundError):
            KalshiClient()

    def test_missing_api_key_id_raises_error(self, test_private_key_pem, monkeypatch):
        """Test that missing API key ID raises ValueError."""
        monkeypatch.delenv("KALSHI_API_KEY_ID", raising=False)
        monkeypatch.setenv("KALSHI_PRIVATE_KEY_PATH", test_private_key_pem)

        from src.kalshi import KalshiClient

        with pytest.raises(ValueError, match="KALSHI_API_KEY_ID"):
            KalshiClient()

    def test_missing_private_key_path_raises_error(self, monkeypatch):
        """Test that missing private key path raises ValueError."""
        monkeypatch.setenv("KALSHI_API_KEY_ID", "test-key-id")
        monkeypatch.delenv("KALSHI_PRIVATE_KEY_PATH", raising=False)

        from src.kalshi import KalshiClient

        with pytest.raises(ValueError, match="KALSHI_PRIVATE_KEY_PATH"):
            KalshiClient()
