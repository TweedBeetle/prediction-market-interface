"""
EIP-712 authentication signer for Polymarket.

Implements the EIP-712 standard for signing authentication messages
to obtain CLOB API credentials.
"""

import time
from typing import Dict, Any

from eth_account import Account
from eth_account.messages import encode_typed_data
from loguru import logger


class AuthSigner:
    """
    EIP-712 signer for Polymarket authentication.

    Handles signing authentication messages to obtain API credentials
    for the CLOB (Central Limit Order Book) API.
    """

    # EIP-712 domain for authentication
    AUTH_DOMAIN = {
        "name": "Polymarket",
        "version": "1",
        "chainId": 137,  # Polygon mainnet
    }

    def __init__(self, private_key: str, chain_id: int = 137):
        """
        Initialize auth signer with private key.

        Args:
            private_key: Ethereum private key (with or without 0x prefix)
            chain_id: Chain ID (137 for Polygon mainnet)
        """
        # Ensure private key has 0x prefix
        if not private_key.startswith("0x"):
            private_key = f"0x{private_key}"

        self.private_key = private_key
        self.account = Account.from_key(private_key)
        self.address = self.account.address
        self.chain_id = chain_id

        logger.info(f"Initialized AuthSigner for address {self.address}")

    def create_api_creds_message(self, nonce: int) -> Dict[str, Any]:
        """
        Create the EIP-712 message for API credentials request.

        Args:
            nonce: Unique nonce for this request (typically current timestamp)

        Returns:
            EIP-712 typed data structure
        """
        message = {
            "account": self.address,
            "nonce": nonce,
        }

        typed_data = {
            "types": {
                "EIP712Domain": [
                    {"name": "name", "type": "string"},
                    {"name": "version", "type": "string"},
                    {"name": "chainId", "type": "uint256"},
                ],
                "ClobAuth": [
                    {"name": "account", "type": "address"},
                    {"name": "nonce", "type": "uint256"},
                ],
            },
            "primaryType": "ClobAuth",
            "domain": {
                "name": self.AUTH_DOMAIN["name"],
                "version": self.AUTH_DOMAIN["version"],
                "chainId": self.chain_id,
            },
            "message": message,
        }

        return typed_data

    def sign_api_creds_message(self, nonce: int | None = None) -> tuple[str, int]:
        """
        Sign an API credentials request message.

        Args:
            nonce: Optional nonce (defaults to current timestamp)

        Returns:
            Tuple of (signature, nonce)
        """
        if nonce is None:
            nonce = int(time.time() * 1000)  # Millisecond timestamp

        typed_data = self.create_api_creds_message(nonce)

        # Encode and sign the message
        encoded_message = encode_typed_data(full_message=typed_data)
        signed_message = self.account.sign_message(encoded_message)

        # Add 0x prefix to signature
        signature = "0x" + signed_message.signature.hex()

        logger.debug(f"Signed API creds message with nonce {nonce}")

        return signature, nonce

    def create_hmac_signature(
        self,
        method: str,
        path: str,
        body: str = "",
        timestamp: int | None = None,
        api_secret: str | None = None
    ) -> tuple[str, int]:
        """
        Create HMAC signature for authenticated CLOB API requests.

        Used after obtaining API credentials for subsequent requests.

        Args:
            method: HTTP method (GET, POST, DELETE)
            path: Request path (e.g., /orders)
            body: Request body as JSON string
            timestamp: Request timestamp (defaults to current time)
            api_secret: API secret from credentials

        Returns:
            Tuple of (signature, timestamp)
        """
        import hmac
        import hashlib

        if timestamp is None:
            timestamp = int(time.time())

        if api_secret is None:
            raise ValueError("API secret required for HMAC signatures")

        # Create message to sign: timestamp + method + path + body
        message = f"{timestamp}{method}{path}{body}"

        # Create HMAC-SHA256 signature
        signature = hmac.new(
            api_secret.encode("utf-8"),
            message.encode("utf-8"),
            hashlib.sha256
        ).hexdigest()

        logger.debug(f"Created HMAC signature for {method} {path}")

        return signature, timestamp

    @staticmethod
    def create_nonce() -> int:
        """
        Create a unique nonce for requests.

        Returns:
            Current timestamp in milliseconds
        """
        return int(time.time() * 1000)
