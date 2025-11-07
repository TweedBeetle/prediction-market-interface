"""
EIP-712 order signer for Polymarket.

Implements the EIP-712 standard for signing orders on the CLOB
(Central Limit Order Book).
"""

from typing import Dict, Any

from eth_account import Account
from eth_account.messages import encode_typed_data
from loguru import logger

from ..models import OrderParams, OrderSide, SignatureType


class OrderSigner:
    """
    EIP-712 signer for Polymarket orders.

    Handles signing order messages for submission to the CLOB API.
    """

    # EIP-712 domain for orders
    ORDER_DOMAIN = {
        "name": "Polymarket CTF Exchange",
        "version": "1",
        "chainId": 137,  # Polygon mainnet
        "verifyingContract": "0x4bFb41d5B3570DeFd03C39a9A4D8dE6Bd8B8982E",  # CTF Exchange contract
    }

    def __init__(self, private_key: str, chain_id: int = 137):
        """
        Initialize order signer with private key.

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

        logger.info(f"Initialized OrderSigner for address {self.address}")

    def create_order_message(self, order_params: OrderParams) -> Dict[str, Any]:
        """
        Create the EIP-712 message for an order.

        Args:
            order_params: Order parameters

        Returns:
            EIP-712 typed data structure
        """
        # Convert price to integer (Polymarket uses fixed-point arithmetic)
        # Price is multiplied by 10^6 for precision
        price_int = int(order_params.price * 1_000_000)

        # Convert size to integer (also uses fixed-point)
        size_int = int(order_params.size * 1_000_000)

        # Determine if this is a BUY (makerAmount = size) or SELL (takerAmount = size)
        if order_params.side == OrderSide.BUY:
            maker_amount = size_int
            taker_amount = int(size_int * order_params.price)
        else:  # SELL
            maker_amount = int(size_int * (1 - order_params.price))
            taker_amount = size_int

        message = {
            "maker": order_params.maker,
            "taker": order_params.taker or "0x0000000000000000000000000000000000000000",
            "tokenId": order_params.token_id,
            "makerAmount": str(maker_amount),
            "takerAmount": str(taker_amount),
            "side": order_params.side.value,
            "feeRateBps": str(order_params.fee_rate_bps),
            "nonce": str(order_params.nonce or 0),
            "signer": order_params.maker,
            "expiration": str(order_params.expiration or 0),
            "signatureType": order_params.signature_type.value,
        }

        typed_data = {
            "types": {
                "EIP712Domain": [
                    {"name": "name", "type": "string"},
                    {"name": "version", "type": "string"},
                    {"name": "chainId", "type": "uint256"},
                    {"name": "verifyingContract", "type": "address"},
                ],
                "Order": [
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
                ],
            },
            "primaryType": "Order",
            "domain": {
                "name": self.ORDER_DOMAIN["name"],
                "version": self.ORDER_DOMAIN["version"],
                "chainId": self.chain_id,
                "verifyingContract": self.ORDER_DOMAIN["verifyingContract"],
            },
            "message": message,
        }

        return typed_data

    def sign_order(self, order_params: OrderParams) -> str:
        """
        Sign an order for submission to the CLOB.

        Args:
            order_params: Order parameters to sign

        Returns:
            Signature as hex string
        """
        typed_data = self.create_order_message(order_params)

        # Encode and sign the message
        encoded_message = encode_typed_data(full_message=typed_data)
        signed_message = self.account.sign_message(encoded_message)

        # Add 0x prefix to signature
        signature = "0x" + signed_message.signature.hex()

        logger.debug(
            f"Signed order: {order_params.side.value} {order_params.size} "
            f"@ {order_params.price} (token {order_params.token_id})"
        )

        return signature

    def build_signed_order(self, order_params: OrderParams) -> Dict[str, Any]:
        """
        Build a complete signed order ready for API submission.

        Args:
            order_params: Order parameters

        Returns:
            Dictionary with order data and signature
        """
        signature = self.sign_order(order_params)

        # Convert to API format
        order_data = {
            "maker": order_params.maker,
            "taker": order_params.taker or "0x0000000000000000000000000000000000000000",
            "tokenId": order_params.token_id,
            "side": order_params.side.value,
            "price": str(order_params.price),
            "size": str(order_params.size),
            "feeRateBps": str(order_params.fee_rate_bps),
            "nonce": str(order_params.nonce or 0),
            "expiration": str(order_params.expiration or 0),
            "signatureType": order_params.signature_type.value,
            "signature": signature,
        }

        return order_data
