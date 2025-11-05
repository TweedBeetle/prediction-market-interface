"""
CLOB API client for Polymarket trading operations.

Provides authenticated access to:
- Order placement and cancellation
- Position management
- Order history
- API credential management
"""

from typing import Dict, List, Optional

from loguru import logger

from .base_client import BaseClient, OrderError
from .models import Order, Position, OrderParams, OrderSide, ApiCredentials, Trade
from .utils.auth_signer import AuthSigner
from .utils.order_signer import OrderSigner


class ClobClient(BaseClient):
    """
    Client for Polymarket CLOB API (trading operations).

    The CLOB (Central Limit Order Book) API provides authenticated
    access to order placement, cancellation, and portfolio management.

    Requires EIP-712 signing with a private key.
    """

    CLOB_BASE_URL = "https://clob.polymarket.com"

    def __init__(
        self,
        credentials: ApiCredentials,
        base_url: str = CLOB_BASE_URL,
        timeout: int = 30,
        max_retries: int = 3,
        rate_limit_calls: int = 100,
        rate_limit_period: int = 60,
    ):
        """
        Initialize CLOB client.

        Args:
            credentials: API credentials (wallet + optional API key)
            base_url: Base URL for CLOB API
            timeout: Request timeout in seconds
            max_retries: Maximum retries for failed requests
            rate_limit_calls: Max calls per period
            rate_limit_period: Rate limit period in seconds
        """
        super().__init__(base_url, timeout, max_retries, rate_limit_calls, rate_limit_period)

        self.credentials = credentials
        self.auth_signer = AuthSigner(credentials.private_key, credentials.chain_id)
        self.order_signer = OrderSigner(credentials.private_key, credentials.chain_id)

        # API credentials (obtained via L1 auth)
        self._api_key: Optional[str] = credentials.api_key
        self._api_secret: Optional[str] = credentials.api_secret
        self._api_passphrase: Optional[str] = credentials.api_passphrase

        logger.info(f"Initialized ClobClient for address {credentials.wallet_address}")

    def _get_default_headers(self) -> Dict[str, str]:
        """
        Get default headers with authentication.

        Overrides base class to add API key authentication headers.
        """
        headers = super()._get_default_headers()

        # Add API key authentication if available
        if self._api_key and self._api_secret and self._api_passphrase:
            headers["POLY-ADDRESS"] = self.credentials.wallet_address
            headers["POLY-API-KEY"] = self._api_key
            headers["POLY-PASSPHRASE"] = self._api_passphrase

        return headers

    async def authenticate(self) -> Dict[str, str]:
        """
        Authenticate and obtain API credentials.

        Uses EIP-712 signing to prove wallet ownership and obtain
        API key, secret, and passphrase for subsequent requests.

        Returns:
            Dictionary with apiKey, secret, and passphrase

        Raises:
            AuthenticationError: If authentication fails
        """
        logger.info(f"Authenticating wallet {self.credentials.wallet_address}")

        # Sign auth message
        signature, nonce = self.auth_signer.sign_api_creds_message()

        # Request API credentials
        auth_payload = {
            "address": self.credentials.wallet_address,
            "signature": signature,
            "nonce": nonce,
        }

        try:
            response = await self.post("/auth/api-key", json_data=auth_payload)

            # Extract credentials
            api_key = response.get("apiKey")
            api_secret = response.get("secret")
            api_passphrase = response.get("passphrase")

            if not all([api_key, api_secret, api_passphrase]):
                raise OrderError("Incomplete API credentials in response")

            # Store credentials
            self._api_key = api_key
            self._api_secret = api_secret
            self._api_passphrase = api_passphrase

            logger.info("Successfully authenticated and obtained API credentials")

            return {
                "apiKey": api_key,
                "secret": api_secret,
                "passphrase": api_passphrase,
            }

        except Exception as e:
            logger.error(f"Authentication failed: {e}")
            raise

    async def create_order(self, order_params: OrderParams) -> Order:
        """
        Create a new order.

        Args:
            order_params: Order parameters (token_id, price, size, side)

        Returns:
            Created order data

        Raises:
            OrderError: If order creation fails
        """
        logger.info(
            f"Creating order: {order_params.side.value} {order_params.size} "
            f"@ {order_params.price} (token {order_params.token_id})"
        )

        try:
            # Ensure we're authenticated
            if not self._api_key:
                await self.authenticate()

            # Build and sign order
            signed_order = self.order_signer.build_signed_order(order_params)

            # Submit order
            response = await self.post("/orders", json_data=signed_order)

            # Parse response
            order_data = response if "order_id" in response else response.get("order", response)

            order = Order(
                order_id=order_data.get("order_id", order_data.get("id", "")),
                market_id=order_data.get("market_id", ""),
                token_id=order_params.token_id,
                price=order_params.price,
                size=order_params.size,
                side=order_params.side,
                size_matched=float(order_data.get("size_matched", 0)),
                outcome=order_data.get("outcome"),
                created_at=order_data.get("created_at"),
                owner=self.credentials.wallet_address,
                status=order_data.get("status", "LIVE"),
            )

            logger.info(f"Order created successfully: {order.order_id}")
            return order

        except Exception as e:
            logger.error(f"Failed to create order: {e}")
            raise OrderError(f"Order creation failed: {str(e)}")

    async def cancel_order(self, order_id: str) -> Dict[str, str]:
        """
        Cancel an existing order.

        Args:
            order_id: Order ID to cancel

        Returns:
            Cancellation status

        Raises:
            OrderError: If cancellation fails
        """
        logger.info(f"Canceling order {order_id}")

        try:
            # Ensure we're authenticated
            if not self._api_key:
                await self.authenticate()

            # Submit cancellation
            response = await self.delete(f"/orders/{order_id}")

            logger.info(f"Order {order_id} canceled successfully")

            return {
                "order_id": order_id,
                "status": "canceled",
                "message": response.get("message", "Order canceled"),
            }

        except Exception as e:
            logger.error(f"Failed to cancel order {order_id}: {e}")
            raise OrderError(f"Order cancellation failed: {str(e)}")

    async def get_orders(
        self,
        market_id: Optional[str] = None,
        status: Optional[str] = None,
    ) -> List[Order]:
        """
        Get user's orders.

        Args:
            market_id: Filter by market ID
            status: Filter by status (LIVE, MATCHED, CANCELLED)

        Returns:
            List of orders
        """
        logger.info("Fetching orders")

        try:
            # Ensure we're authenticated
            if not self._api_key:
                await self.authenticate()

            params = {}
            if market_id:
                params["market_id"] = market_id
            if status:
                params["status"] = status

            response = await self.get("/orders", params=params)

            # Parse orders
            orders_data = response if isinstance(response, list) else response.get("orders", [])

            orders = []
            for order_data in orders_data:
                try:
                    order = Order(
                        order_id=order_data.get("order_id", order_data.get("id", "")),
                        market_id=order_data.get("market_id", ""),
                        token_id=order_data.get("token_id", ""),
                        price=float(order_data.get("price", 0)),
                        size=float(order_data.get("size", 0)),
                        side=order_data.get("side", "BUY"),
                        size_matched=float(order_data.get("size_matched", 0)),
                        outcome=order_data.get("outcome"),
                        created_at=order_data.get("created_at"),
                        owner=order_data.get("owner", self.credentials.wallet_address),
                        status=order_data.get("status", "LIVE"),
                    )
                    orders.append(order)
                except Exception as e:
                    logger.warning(f"Failed to parse order: {e}")
                    continue

            logger.info(f"Retrieved {len(orders)} orders")
            return orders

        except Exception as e:
            logger.error(f"Failed to get orders: {e}")
            raise

    async def get_positions(self, market_id: Optional[str] = None) -> List[Position]:
        """
        Get user's current positions.

        Args:
            market_id: Filter by market ID

        Returns:
            List of positions
        """
        logger.info("Fetching positions")

        try:
            # Ensure we're authenticated
            if not self._api_key:
                await self.authenticate()

            params = {}
            if market_id:
                params["market_id"] = market_id

            response = await self.get("/positions", params=params)

            # Parse positions
            positions_data = response if isinstance(response, list) else response.get("positions", [])

            positions = []
            for pos_data in positions_data:
                try:
                    position = Position(
                        market_id=pos_data.get("market_id", ""),
                        token_id=pos_data.get("token_id", ""),
                        size=float(pos_data.get("size", 0)),
                        outcome=pos_data.get("outcome", "YES"),
                        average_price=float(pos_data.get("average_price", 0)) if pos_data.get("average_price") else None,
                        total_cost=float(pos_data.get("total_cost", 0)) if pos_data.get("total_cost") else None,
                        current_price=float(pos_data.get("current_price", 0)) if pos_data.get("current_price") else None,
                        market_value=float(pos_data.get("market_value", 0)) if pos_data.get("market_value") else None,
                        unrealized_pnl=float(pos_data.get("unrealized_pnl", 0)) if pos_data.get("unrealized_pnl") else None,
                    )
                    positions.append(position)
                except Exception as e:
                    logger.warning(f"Failed to parse position: {e}")
                    continue

            logger.info(f"Retrieved {len(positions)} positions")
            return positions

        except Exception as e:
            logger.error(f"Failed to get positions: {e}")
            raise

    async def get_trades(
        self,
        market_id: Optional[str] = None,
        maker_address: Optional[str] = None,
        limit: int = 100,
    ) -> List[Trade]:
        """
        Get user's trade history.

        Args:
            market_id: Filter by market ID (condition ID)
            maker_address: Filter by maker address (defaults to user's address)
            limit: Maximum number of trades

        Returns:
            List of trades

        Note:
            This endpoint requires authentication via L2 headers.
        """
        logger.info(f"Fetching trades (limit={limit})")

        try:
            # Ensure we're authenticated
            if not self._api_key:
                await self.authenticate()

            params = {"limit": limit}

            if market_id:
                params["market"] = market_id  # API uses "market" not "market_id"

            if maker_address:
                params["maker"] = maker_address
            elif self.credentials:
                # Default to user's address
                params["maker"] = self.credentials.wallet_address

            response = await self.get("/data/trades", params=params)

            # Parse trades - API returns array or dict with trades key
            trades_data = response if isinstance(response, list) else response.get("trades", [])

            trades = []
            for trade_data in trades_data:
                try:
                    trade = Trade(
                        trade_id=trade_data.get("id", ""),
                        market_id=trade_data.get("market", market_id or ""),
                        token_id=trade_data.get("asset_id", ""),
                        price=float(trade_data.get("price", 0)),
                        size=float(trade_data.get("size", 0)),
                        side=OrderSide.BUY if trade_data.get("side", "").upper() == "BUY" else OrderSide.SELL,
                        outcome=trade_data.get("outcome", "YES"),
                        timestamp=trade_data.get("match_time"),
                        maker_address=trade_data.get("maker_address"),
                        taker_address=None,  # Not in CLOB trade response
                    )
                    trades.append(trade)
                except Exception as e:
                    logger.warning(f"Failed to parse trade: {e}")
                    continue

            logger.info(f"Retrieved {len(trades)} trades")
            return trades

        except Exception as e:
            logger.error(f"Failed to get trades: {e}")
            raise

    @classmethod
    def from_env(cls) -> "ClobClient":
        """
        Create client from environment variables.

        Expects:
            POLYMARKET_PRIVATE_KEY: Ethereum private key
            POLYMARKET_WALLET_ADDRESS: Wallet address
            POLYMARKET_CHAIN_ID: Chain ID (defaults to 137)

        Returns:
            Configured ClobClient instance

        Raises:
            ValueError: If required env vars are missing
        """
        import os

        private_key = os.getenv("POLYMARKET_PRIVATE_KEY")
        wallet_address = os.getenv("POLYMARKET_WALLET_ADDRESS")

        if not private_key:
            raise ValueError("POLYMARKET_PRIVATE_KEY environment variable required")

        # If wallet address not provided, derive it from private key
        if not wallet_address:
            from eth_account import Account

            # Ensure private key has 0x prefix
            if not private_key.startswith("0x"):
                private_key = f"0x{private_key}"

            account = Account.from_key(private_key)
            wallet_address = account.address
            logger.info(f"Derived wallet address from private key: {wallet_address}")

        chain_id = int(os.getenv("POLYMARKET_CHAIN_ID", "137"))
        base_url = os.getenv("POLYMARKET_CLOB_URL", cls.CLOB_BASE_URL)

        credentials = ApiCredentials(
            private_key=private_key,
            wallet_address=wallet_address,
            chain_id=chain_id,
        )

        return cls(credentials=credentials, base_url=base_url)
