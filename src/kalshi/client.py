"""Kalshi API client wrapper with authentication."""

import os
import time
import base64
import hashlib
from typing import Optional, Any
from pathlib import Path

import httpx
from loguru import logger
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend

from .models import (
    ExchangeStatus,
    Balance,
    Market,
    Event,
    Order,
    Position,
    Fill,
    OrderBook,
    OrderBookLevel,
    Trade,
)


class KalshiClient:
    """Wrapper for Kalshi API with authentication and rate limiting."""

    def __init__(
        self,
        api_key: str,
        private_key_path: str,
        base_url: str = "https://trading-api.kalshi.com",
        api_version: str = "v2",
    ):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.api_version = api_version
        self.client = httpx.AsyncClient(timeout=30.0)

        # Load private key for request signing
        private_key_path = Path(private_key_path).expanduser()
        if not private_key_path.exists():
            raise FileNotFoundError(f"Private key not found: {private_key_path}")

        with open(private_key_path, "rb") as f:
            self.private_key = serialization.load_pem_private_key(
                f.read(), password=None, backend=default_backend()
            )

        logger.info(f"Initialized Kalshi client: {self.base_url}")

    @classmethod
    def from_env(cls, environment: Optional[str] = None) -> "KalshiClient":
        """
        Create client from environment variables.

        Args:
            environment: Override environment ("demo" or "production")
                        If None, uses KALSHI_ENVIRONMENT env var
        """
        env = environment or os.getenv("KALSHI_ENVIRONMENT", "demo")

        api_key = os.getenv("KALSHI_API_KEY")
        if not api_key:
            raise ValueError("KALSHI_API_KEY environment variable not set")

        private_key_path = os.getenv("KALSHI_PRIVATE_KEY_PATH")
        if not private_key_path:
            raise ValueError("KALSHI_PRIVATE_KEY_PATH environment variable not set")

        base_url = os.getenv(
            "KALSHI_BASE_URL",
            "https://demo-api.kalshi.co"
            if env == "demo"
            else "https://trading-api.kalshi.com",
        )

        api_version = os.getenv("KALSHI_API_VERSION", "v2")

        logger.info(f"Loading Kalshi client from environment: {env}")
        return cls(
            api_key=api_key,
            private_key_path=private_key_path,
            base_url=base_url,
            api_version=api_version,
        )

    def _sign_request(self, method: str, path: str) -> tuple[str, str]:
        """
        Sign API request using private key.

        Args:
            method: HTTP method (GET, POST, etc.)
            path: API path (e.g., /trade-api/v2/markets)

        Returns:
            Tuple of (timestamp, signature) both base64-encoded
        """
        # Create message to sign: timestamp + method + path (NO body, NO query params)
        # Strip query parameters from path before signing
        path_without_query = path.split('?')[0]
        timestamp = str(int(time.time() * 1000))
        message = f"{timestamp}{method}{path_without_query}"

        # Sign with private key (using PSS padding as required by Kalshi)
        signature = self.private_key.sign(
            message.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.DIGEST_LENGTH
            ),
            hashes.SHA256()
        )

        return timestamp, base64.b64encode(signature).decode()

    async def _request(
        self,
        method: str,
        endpoint: str,
        params: Optional[dict[str, Any]] = None,
        json_data: Optional[dict[str, Any]] = None,
    ) -> dict[str, Any]:
        """
        Make authenticated API request.

        Args:
            method: HTTP method
            endpoint: API endpoint (e.g., "markets")
            params: Query parameters
            json_data: JSON body

        Returns:
            API response data
        """
        # Build full path
        path = f"/trade-api/{self.api_version}/{endpoint}"
        url = f"{self.base_url}{path}"

        # Sign request (signature never includes body, per Kalshi docs)
        timestamp, signature = self._sign_request(method, path)

        # Prepare headers
        headers = {
            "KALSHI-ACCESS-KEY": self.api_key,
            "KALSHI-ACCESS-SIGNATURE": signature,
            "KALSHI-ACCESS-TIMESTAMP": timestamp,
            "Content-Type": "application/json",
        }

        # Make request
        logger.debug(f"{method} {url}")
        response = await self.client.request(
            method=method, url=url, headers=headers, params=params, json=json_data
        )

        # Handle errors
        if response.status_code >= 400:
            logger.error(f"API error {response.status_code}: {response.text}")
            response.raise_for_status()

        return response.json()

    async def get_exchange_status(self) -> ExchangeStatus:
        """Get exchange operational status."""
        data = await self._request("GET", "exchange/status")
        return ExchangeStatus(**data)

    async def get_balance(self) -> Balance:
        """Get account balance."""
        data = await self._request("GET", "portfolio/balance")
        return Balance(**data)

    async def search_markets(
        self, query: Optional[str] = None, limit: int = 20, status: str = "open"
    ) -> list[Market]:
        """
        Search for markets.

        Args:
            query: Search query string
            limit: Maximum number of results
            status: Market status filter (open, closed, settled)

        Returns:
            List of matching markets
        """
        params = {"limit": limit, "status": status}
        if query:
            params["event_ticker"] = query  # Simple search for MVP

        data = await self._request("GET", "markets", params=params)
        markets = data.get("markets", [])
        return [Market(**m) for m in markets]

    async def get_market(self, ticker: str) -> Market:
        """
        Get detailed market information.

        Args:
            ticker: Market ticker symbol

        Returns:
            Market details
        """
        data = await self._request("GET", f"markets/{ticker}")
        return Market(**data.get("market", data))

    async def get_events(
        self, limit: int = 50, status: str = "open"
    ) -> list[Event]:
        """
        Get list of events.

        Args:
            limit: Maximum number of results
            status: Event status filter

        Returns:
            List of events
        """
        params = {"limit": limit, "status": status}
        data = await self._request("GET", "events", params=params)
        events = data.get("events", [])
        return [Event(**e) for e in events]

    async def get_event(self, event_ticker: str) -> Event:
        """
        Get a single event by ticker.

        Args:
            event_ticker: Event ticker (e.g., "INXD-25JAN31")

        Returns:
            Event details
        """
        data = await self._request("GET", f"events/{event_ticker}")
        return Event(**data.get("event", data))

    async def get_orderbook(self, ticker: str, depth: int = 10) -> OrderBook:
        """
        Get order book for a market.

        Args:
            ticker: Market ticker
            depth: Number of price levels per side (default: 10)

        Returns:
            Order book with bids and asks
        """
        params = {"depth": depth}
        data = await self._request("GET", f"markets/{ticker}/orderbook", params=params)
        orderbook_data = data.get("orderbook", data)

        # Kalshi API returns bids only (no asks) in a flat array structure:
        # {"yes": [[price, qty], ...], "no": [[price, qty], ...]}
        # In binary markets, YES bid @ X = NO ask @ (100-X), so asks are implied

        # Parse YES bids (returns None if no liquidity)
        yes_data = orderbook_data.get("yes")
        yes_bids = []
        if yes_data and isinstance(yes_data, list):
            yes_bids = [
                OrderBookLevel(price=level[0], quantity=level[1])
                for level in yes_data
            ]

        # Parse NO bids (returns None if no liquidity)
        no_data = orderbook_data.get("no")
        no_bids = []
        if no_data and isinstance(no_data, list):
            no_bids = [
                OrderBookLevel(price=level[0], quantity=level[1])
                for level in no_data
            ]

        # Calculate implied asks from reciprocal bids
        # YES ask = 100 - NO bid (highest NO bid gives best YES ask)
        yes_asks = []
        if no_bids:
            # Sort NO bids descending to find best (highest) bid first
            sorted_no_bids = sorted(no_bids, key=lambda x: x.price, reverse=True)
            yes_asks = [
                OrderBookLevel(price=100 - level.price, quantity=level.quantity)
                for level in sorted_no_bids
            ]

        # NO ask = 100 - YES bid (highest YES bid gives best NO ask)
        no_asks = []
        if yes_bids:
            # Sort YES bids descending to find best (highest) bid first
            sorted_yes_bids = sorted(yes_bids, key=lambda x: x.price, reverse=True)
            no_asks = [
                OrderBookLevel(price=100 - level.price, quantity=level.quantity)
                for level in sorted_yes_bids
            ]

        return OrderBook(
            ticker=ticker,
            yes_bids=yes_bids,
            yes_asks=yes_asks,
            no_bids=no_bids,
            no_asks=no_asks,
        )

    async def get_trades(
        self, ticker: Optional[str] = None, limit: int = 100
    ) -> list[Trade]:
        """
        Get recent public trades.

        Args:
            ticker: Filter by market ticker (optional)
            limit: Maximum number of trades

        Returns:
            List of recent trades
        """
        params = {"limit": limit}
        if ticker:
            params["ticker"] = ticker

        data = await self._request("GET", "markets/trades", params=params)
        trades = data.get("trades", [])
        return [Trade(**t) for t in trades]

    # Order Operations

    async def create_order(
        self,
        ticker: str,
        side: str,
        count: int,
        action: str = "buy",
        order_type: str = "market",
        yes_price: Optional[int] = None,
        no_price: Optional[int] = None,
    ) -> Order:
        """
        Create an order.

        Args:
            ticker: Market ticker
            side: "yes" or "no"
            count: Number of contracts
            action: "buy" or "sell" (default: "buy")
            order_type: "market" or "limit" (default: "market")
            yes_price: Limit price for yes side (cents, 1-99)
            no_price: Limit price for no side (cents, 1-99)

        Returns:
            Created order details
        """
        payload = {
            "ticker": ticker,
            "side": side,
            "action": action,
            "count": count,
            "type": order_type,
        }

        if order_type == "limit":
            if side == "yes" and yes_price:
                payload["yes_price"] = yes_price
            elif side == "no" and no_price:
                payload["no_price"] = no_price

        data = await self._request("POST", "portfolio/orders", json_data=payload)
        return Order(**data.get("order", data))

    async def cancel_order(self, order_id: str) -> Order:
        """
        Cancel an order.

        Args:
            order_id: Order ID to cancel

        Returns:
            Canceled order details
        """
        data = await self._request("DELETE", f"portfolio/orders/{order_id}")
        return Order(**data.get("order", data))

    async def amend_order(
        self, order_id: str, new_count: int, new_price: int
    ) -> Order:
        """
        Amend an order (modify without losing queue position).

        Args:
            order_id: Order ID to amend
            new_count: New contract count
            new_price: New price in cents

        Returns:
            Amended order details
        """
        payload = {"count": new_count, "price": new_price}
        data = await self._request(
            "PATCH", f"portfolio/orders/{order_id}", json_data=payload
        )
        return Order(**data.get("order", data))

    async def decrease_order(self, order_id: str, reduce_by: int) -> Order:
        """
        Decrease order size.

        Args:
            order_id: Order ID to decrease
            reduce_by: Number of contracts to reduce by

        Returns:
            Updated order details
        """
        payload = {"reduce_by": reduce_by}
        data = await self._request(
            "POST", f"portfolio/orders/{order_id}/decrease", json_data=payload
        )
        return Order(**data.get("order", data))

    async def get_orders(
        self,
        ticker: Optional[str] = None,
        status: str = "resting",
        limit: int = 100,
    ) -> list[Order]:
        """
        Get orders.

        Args:
            ticker: Filter by ticker (optional)
            status: Filter by status (default: "resting")
            limit: Maximum results

        Returns:
            List of orders
        """
        params = {"status": status, "limit": limit}
        if ticker:
            params["ticker"] = ticker

        data = await self._request("GET", "portfolio/orders", params=params)
        orders = data.get("orders", [])
        return [Order(**o) for o in orders]

    # Portfolio Operations

    async def get_positions(
        self,
        ticker: Optional[str] = None,
        limit: int = 100,
        settlement_status: Optional[str] = None,
    ) -> list[Position]:
        """
        Get portfolio positions.

        Args:
            ticker: Filter by ticker (optional)
            limit: Maximum results
            settlement_status: Filter by settlement status (optional)

        Returns:
            List of positions
        """
        params = {"limit": limit}
        if ticker:
            params["ticker"] = ticker
        if settlement_status:
            params["settlement_status"] = settlement_status

        data = await self._request("GET", "portfolio/positions", params=params)
        positions = data.get("positions", [])
        return [Position(**p) for p in positions]

    async def get_fills(
        self,
        ticker: Optional[str] = None,
        order_id: Optional[str] = None,
        limit: int = 100,
    ) -> list[Fill]:
        """
        Get trade fills.

        Args:
            ticker: Filter by ticker (optional)
            order_id: Filter by order ID (optional)
            limit: Maximum results

        Returns:
            List of fills
        """
        params = {"limit": limit}
        if ticker:
            params["ticker"] = ticker
        if order_id:
            params["order_id"] = order_id

        data = await self._request("GET", "portfolio/fills", params=params)
        fills = data.get("fills", [])
        return [Fill(**f) for f in fills]

    async def close(self):
        """Close HTTP client."""
        await self.client.aclose()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()
