"""
Unit tests for EIP-712 signers.

Tests authentication and order signing match Polymarket API specification.
Uses a test private key for deterministic signature generation.
"""

import pytest
from eth_account import Account

from src.polymarket.utils.auth_signer import AuthSigner
from src.polymarket.utils.order_signer import OrderSigner
from src.polymarket.models import OrderParams, OrderSide, SignatureType


# Test private key (DO NOT use in production!)
TEST_PRIVATE_KEY = "0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef"
TEST_WALLET_ADDRESS = Account.from_key(TEST_PRIVATE_KEY).address


class TestAuthSigner:
    """Test AuthSigner for EIP-712 authentication."""

    def test_signer_initialization(self):
        """Test signer initialization with private key."""
        signer = AuthSigner(TEST_PRIVATE_KEY, chain_id=137)

        assert signer.address == TEST_WALLET_ADDRESS
        assert signer.chain_id == 137

    def test_signer_initialization_without_0x_prefix(self):
        """Test signer handles private key without 0x prefix."""
        key_without_prefix = TEST_PRIVATE_KEY[2:]  # Remove 0x
        signer = AuthSigner(key_without_prefix, chain_id=137)

        assert signer.address == TEST_WALLET_ADDRESS

    def test_create_api_creds_message_structure(self):
        """Test API credentials message structure matches Polymarket spec."""
        signer = AuthSigner(TEST_PRIVATE_KEY, chain_id=137)
        nonce = 1000000

        typed_data = signer.create_api_creds_message(nonce)

        # Verify EIP-712 structure
        assert "types" in typed_data
        assert "primaryType" in typed_data
        assert "domain" in typed_data
        assert "message" in typed_data

        # Verify primary type
        assert typed_data["primaryType"] == "ClobAuth"

        # Verify domain
        domain = typed_data["domain"]
        assert domain["name"] == "Polymarket"
        assert domain["version"] == "1"
        assert domain["chainId"] == 137

        # Verify message structure
        message = typed_data["message"]
        assert message["account"] == TEST_WALLET_ADDRESS
        assert message["nonce"] == nonce

        # Verify type definitions
        types = typed_data["types"]
        assert "EIP712Domain" in types
        assert "ClobAuth" in types

        # Verify ClobAuth type structure
        clob_auth_type = types["ClobAuth"]
        assert len(clob_auth_type) == 2
        assert clob_auth_type[0] == {"name": "account", "type": "address"}
        assert clob_auth_type[1] == {"name": "nonce", "type": "uint256"}

    def test_sign_api_creds_message(self):
        """Test signing API credentials message."""
        signer = AuthSigner(TEST_PRIVATE_KEY, chain_id=137)
        nonce = 1000000

        signature, returned_nonce = signer.sign_api_creds_message(nonce)

        # Verify signature format
        assert isinstance(signature, str)
        assert signature.startswith("0x")
        assert len(signature) == 132  # 0x + 130 hex chars (65 bytes)

        # Verify nonce returned
        assert returned_nonce == nonce

    def test_sign_api_creds_message_auto_nonce(self):
        """Test signing with auto-generated nonce."""
        signer = AuthSigner(TEST_PRIVATE_KEY, chain_id=137)

        signature, nonce = signer.sign_api_creds_message()

        # Verify signature generated
        assert isinstance(signature, str)
        assert signature.startswith("0x")

        # Verify nonce was auto-generated (timestamp)
        assert isinstance(nonce, int)
        assert nonce > 1000000000000  # Should be millisecond timestamp

    def test_create_nonce(self):
        """Test nonce generation."""
        nonce = AuthSigner.create_nonce()

        assert isinstance(nonce, int)
        assert nonce > 1000000000000  # Millisecond timestamp

    def test_hmac_signature(self):
        """Test HMAC signature generation for authenticated requests."""
        signer = AuthSigner(TEST_PRIVATE_KEY, chain_id=137)
        api_secret = "test_secret"
        timestamp = 1234567890

        signature, returned_ts = signer.create_hmac_signature(
            method="POST",
            path="/orders",
            body='{"order":"data"}',
            timestamp=timestamp,
            api_secret=api_secret
        )

        # Verify signature format
        assert isinstance(signature, str)
        assert len(signature) == 64  # SHA256 hex digest

        # Verify timestamp returned
        assert returned_ts == timestamp


class TestOrderSigner:
    """Test OrderSigner for EIP-712 order signing."""

    def test_signer_initialization(self):
        """Test order signer initialization."""
        signer = OrderSigner(TEST_PRIVATE_KEY, chain_id=137)

        assert signer.address == TEST_WALLET_ADDRESS
        assert signer.chain_id == 137

    def test_create_order_message_structure(self):
        """Test order message structure matches Polymarket spec."""
        signer = OrderSigner(TEST_PRIVATE_KEY, chain_id=137)

        order_params = OrderParams(
            token_id="12345",
            price=0.65,
            size=100.0,
            side=OrderSide.BUY,
            maker=TEST_WALLET_ADDRESS,
            nonce=1000,
            expiration=1700000000,
        )

        typed_data = signer.create_order_message(order_params)

        # Verify EIP-712 structure
        assert "types" in typed_data
        assert "primaryType" in typed_data
        assert "domain" in typed_data
        assert "message" in typed_data

        # Verify primary type
        assert typed_data["primaryType"] == "Order"

        # Verify domain (Polymarket CTF Exchange)
        domain = typed_data["domain"]
        assert domain["name"] == "Polymarket CTF Exchange"
        assert domain["version"] == "1"
        assert domain["chainId"] == 137
        assert domain["verifyingContract"] == "0x4bFb41d5B3570DeFd03C39a9A4D8dE6Bd8B8982E"

        # Verify message structure
        message = typed_data["message"]
        assert message["maker"] == TEST_WALLET_ADDRESS
        assert message["tokenId"] == "12345"
        assert message["side"] == "BUY"
        assert message["nonce"] == "1000"
        assert message["expiration"] == "1700000000"
        assert message["signer"] == TEST_WALLET_ADDRESS
        assert message["signatureType"] == "EOA"

        # Verify type definitions
        types = typed_data["types"]
        assert "EIP712Domain" in types
        assert "Order" in types

        # Verify Order type structure (matches Polymarket API)
        order_type = types["Order"]
        expected_fields = [
            {"name": "maker", "type": "address"},
            {"name": "taker", "type": "address"},
            {"name": "tokenId", "type": "uint256"},
            {"name": "makerAmount", "type": "uint256"},
            {"name": "takerAmount", "type": "uint256"},
            {"name": "side", "type": "string"},
            {"name": "feeRateBps", "type": "uint256"},
            {"name": "nonce", "type": "uint256"},
            {"name": "signer", "type": "address"},
            {"name": "expiration", "type": "uint256"},
            {"name": "signatureType", "type": "string"},
        ]
        assert order_type == expected_fields

    def test_buy_order_amounts(self):
        """Test BUY order amount calculations."""
        signer = OrderSigner(TEST_PRIVATE_KEY, chain_id=137)

        order_params = OrderParams(
            token_id="12345",
            price=0.60,  # 60 cents
            size=100.0,  # 100 tokens
            side=OrderSide.BUY,
            maker=TEST_WALLET_ADDRESS,
        )

        typed_data = signer.create_order_message(order_params)
        message = typed_data["message"]

        # For BUY: makerAmount = size, takerAmount = size * price
        # Using fixed-point arithmetic (multiply by 1_000_000)
        expected_maker_amount = int(100.0 * 1_000_000)  # 100_000_000
        expected_taker_amount = int(100.0 * 0.60 * 1_000_000)  # 60_000_000

        assert message["makerAmount"] == str(expected_maker_amount)
        assert message["takerAmount"] == str(expected_taker_amount)

    def test_sell_order_amounts(self):
        """Test SELL order amount calculations."""
        signer = OrderSigner(TEST_PRIVATE_KEY, chain_id=137)

        order_params = OrderParams(
            token_id="12345",
            price=0.60,  # 60 cents
            size=100.0,  # 100 tokens
            side=OrderSide.SELL,
            maker=TEST_WALLET_ADDRESS,
        )

        typed_data = signer.create_order_message(order_params)
        message = typed_data["message"]

        # For SELL: makerAmount = size * (1 - price), takerAmount = size
        # Using fixed-point arithmetic
        expected_maker_amount = int(100.0 * (1 - 0.60) * 1_000_000)  # 40_000_000
        expected_taker_amount = int(100.0 * 1_000_000)  # 100_000_000

        assert message["makerAmount"] == str(expected_maker_amount)
        assert message["takerAmount"] == str(expected_taker_amount)

    def test_sign_order(self):
        """Test order signing."""
        signer = OrderSigner(TEST_PRIVATE_KEY, chain_id=137)

        order_params = OrderParams(
            token_id="12345",
            price=0.65,
            size=100.0,
            side=OrderSide.BUY,
            maker=TEST_WALLET_ADDRESS,
        )

        signature = signer.sign_order(order_params)

        # Verify signature format
        assert isinstance(signature, str)
        assert signature.startswith("0x")
        assert len(signature) == 132  # 0x + 130 hex chars

    def test_build_signed_order(self):
        """Test building complete signed order for API submission."""
        signer = OrderSigner(TEST_PRIVATE_KEY, chain_id=137)

        order_params = OrderParams(
            token_id="12345",
            price=0.65,
            size=100.0,
            side=OrderSide.BUY,
            maker=TEST_WALLET_ADDRESS,
            fee_rate_bps=10,
            nonce=1000,
            expiration=1700000000,
        )

        order_data = signer.build_signed_order(order_params)

        # Verify order data structure matches API requirements
        assert order_data["maker"] == TEST_WALLET_ADDRESS
        assert order_data["tokenId"] == "12345"
        assert order_data["side"] == "BUY"
        assert order_data["price"] == "0.65"
        assert order_data["size"] == "100.0"
        assert order_data["feeRateBps"] == "10"
        assert order_data["nonce"] == "1000"
        assert order_data["expiration"] == "1700000000"
        assert order_data["signatureType"] == "EOA"
        assert "signature" in order_data
        assert order_data["signature"].startswith("0x")

    def test_default_taker_address(self):
        """Test taker address defaults to zero address."""
        signer = OrderSigner(TEST_PRIVATE_KEY, chain_id=137)

        order_params = OrderParams(
            token_id="12345",
            price=0.65,
            size=100.0,
            side=OrderSide.BUY,
            maker=TEST_WALLET_ADDRESS,
        )

        typed_data = signer.create_order_message(order_params)
        message = typed_data["message"]

        # Should default to zero address (public order)
        assert message["taker"] == "0x0000000000000000000000000000000000000000"

    def test_custom_taker_address(self):
        """Test custom taker address for private orders."""
        signer = OrderSigner(TEST_PRIVATE_KEY, chain_id=137)
        custom_taker = "0xabcdefabcdefabcdefabcdefabcdefabcdefabcd"

        order_params = OrderParams(
            token_id="12345",
            price=0.65,
            size=100.0,
            side=OrderSide.BUY,
            maker=TEST_WALLET_ADDRESS,
            taker=custom_taker,
        )

        typed_data = signer.create_order_message(order_params)
        message = typed_data["message"]

        assert message["taker"] == custom_taker

    def test_signature_types(self):
        """Test different signature types."""
        signer = OrderSigner(TEST_PRIVATE_KEY, chain_id=137)

        # Test EOA
        order_params = OrderParams(
            token_id="12345",
            price=0.65,
            size=100.0,
            side=OrderSide.BUY,
            maker=TEST_WALLET_ADDRESS,
            signature_type=SignatureType.EOA,
        )
        typed_data = signer.create_order_message(order_params)
        assert typed_data["message"]["signatureType"] == "EOA"

        # Test POLY_PROXY
        order_params.signature_type = SignatureType.POLY_PROXY
        typed_data = signer.create_order_message(order_params)
        assert typed_data["message"]["signatureType"] == "POLY_PROXY"

        # Test POLY_GNOSIS_SAFE
        order_params.signature_type = SignatureType.POLY_GNOSIS_SAFE
        typed_data = signer.create_order_message(order_params)
        assert typed_data["message"]["signatureType"] == "POLY_GNOSIS_SAFE"


class TestSignerConsistency:
    """Test signers produce consistent results."""

    def test_auth_signature_deterministic(self):
        """Test auth signatures are deterministic for same nonce."""
        signer = AuthSigner(TEST_PRIVATE_KEY, chain_id=137)
        nonce = 1234567890

        sig1, _ = signer.sign_api_creds_message(nonce)
        sig2, _ = signer.sign_api_creds_message(nonce)

        # Same nonce should produce same signature
        assert sig1 == sig2

    def test_order_signature_deterministic(self):
        """Test order signatures are deterministic for same parameters."""
        signer = OrderSigner(TEST_PRIVATE_KEY, chain_id=137)

        order_params = OrderParams(
            token_id="12345",
            price=0.65,
            size=100.0,
            side=OrderSide.BUY,
            maker=TEST_WALLET_ADDRESS,
            nonce=1000,
            expiration=1700000000,
        )

        sig1 = signer.sign_order(order_params)
        sig2 = signer.sign_order(order_params)

        # Same parameters should produce same signature
        assert sig1 == sig2

    def test_different_nonce_different_signature(self):
        """Test different nonces produce different signatures."""
        signer = OrderSigner(TEST_PRIVATE_KEY, chain_id=137)

        params1 = OrderParams(
            token_id="12345",
            price=0.65,
            size=100.0,
            side=OrderSide.BUY,
            maker=TEST_WALLET_ADDRESS,
            nonce=1000,
        )

        params2 = OrderParams(
            token_id="12345",
            price=0.65,
            size=100.0,
            side=OrderSide.BUY,
            maker=TEST_WALLET_ADDRESS,
            nonce=2000,  # Different nonce
        )

        sig1 = signer.sign_order(params1)
        sig2 = signer.sign_order(params2)

        # Different nonces should produce different signatures
        assert sig1 != sig2
