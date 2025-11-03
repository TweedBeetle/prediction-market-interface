"""Kalshi API client with RSA-PSS authentication."""

import os
import time
import base64
import httpx
from typing import Optional, Any, Dict, List
from pathlib import Path

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from loguru import logger

from .models import (
    Market,
    Order,
    Position,
    Event,
    Series,
    Fill,
    Balance,
    Candlestick,
    Trade,
    Orderbook,
    Milestone,
    RFQ,
    Quote,
    QueuePosition,
    ExchangeStatus,
    OrderGroup,
    Settlement,
    TotalRestingOrderValue,
    MultivarianateCollection,
    MarketInCollection,
    CollectionLookup,
    MarketMakerMetrics,
)
from .websocket_client import KalshiWebSocketClient, WebSocketChannel


class KalshiClient:
    """Kalshi API client with RSA-PSS signature authentication and WebSocket support."""

    BASE_URL = "https://api.elections.kalshi.com/trade-api/v2"

    # Class-level WebSocket connection pool (shared across instances)
    _websocket_connections: Dict[str, KalshiWebSocketClient] = {}

    def __init__(
        self,
        api_key_id: Optional[str] = None,
        private_key_path: Optional[str] = None,
        timeout: float = 30.0,
    ):
        """Initialize Kalshi client.

        Args:
            api_key_id: API key ID (defaults to KALSHI_API_KEY_ID env var)
            private_key_path: Path to RSA private key PEM file (defaults to KALSHI_PRIVATE_KEY_PATH env var)
            timeout: Request timeout in seconds
        """
        self.api_key_id = api_key_id or os.getenv("KALSHI_API_KEY_ID")
        private_key_path = private_key_path or os.getenv("KALSHI_PRIVATE_KEY_PATH")

        if not self.api_key_id:
            raise ValueError("KALSHI_API_KEY_ID environment variable not set")
        if not private_key_path:
            raise ValueError("KALSHI_PRIVATE_KEY_PATH environment variable not set")

        # Load private key
        self.private_key_path = Path(private_key_path)
        if not self.private_key_path.exists():
            raise FileNotFoundError(f"Private key not found: {private_key_path}")

        with open(self.private_key_path, "rb") as f:
            self.private_key = serialization.load_pem_private_key(
                f.read(),
                password=None,
                backend=default_backend(),
            )

        self.timeout = timeout
        self._last_request_time = 0
        self._signature_cache: Dict[str, tuple[str, int]] = {}  # message -> (signature, timestamp)

    def _generate_signature(self, timestamp: int, method: str, path: str) -> str:
        """Generate RSA-PSS signature for request authentication.

        Args:
            timestamp: Unix timestamp in milliseconds
            method: HTTP method (GET, POST, DELETE, PUT)
            path: API path (e.g., /markets)

        Returns:
            Base64-encoded RSA-PSS signature
        """
        # Create message: timestamp + method + path
        message = f"{timestamp}{method}{path}".encode()

        # Sign with RSA-PSS (SHA-256)
        signature_bytes = self.private_key.sign(
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH,
            ),
            hashes.SHA256(),
        )

        # Return base64-encoded signature
        return base64.b64encode(signature_bytes).decode()

    def _get_headers(self, method: str, path: str) -> Dict[str, str]:
        """Get authentication headers for API request.

        Args:
            method: HTTP method
            path: API path

        Returns:
            Dictionary of headers including auth headers
        """
        # Timestamp in milliseconds
        timestamp = int(time.time() * 1000)

        # Generate signature
        signature = self._generate_signature(timestamp, method, path)

        return {
            "KALSHI-ACCESS-KEY": self.api_key_id,
            "KALSHI-ACCESS-SIGNATURE": signature,
            "KALSHI-ACCESS-TIMESTAMP": str(timestamp),
            "Content-Type": "application/json",
        }

    async def _request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        authenticated: bool = True,
    ) -> Dict[str, Any]:
        """Make authenticated API request.

        Args:
            method: HTTP method
            endpoint: API endpoint (e.g., /markets)
            params: Query parameters
            json: Request body (JSON)
            authenticated: Whether to include auth headers

        Returns:
            Response JSON

        Raises:
            httpx.HTTPStatusError: If response status is not 2xx
        """
        url = f"{self.BASE_URL}{endpoint}"

        headers = {}
        if authenticated:
            headers = self._get_headers(method, endpoint)

        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.request(
                method,
                url,
                params=params,
                json=json,
                headers=headers,
            )

            # Log request details for debugging
            logger.debug(f"{method} {endpoint} -> {response.status_code}")

            response.raise_for_status()
            return response.json()

    # ========== MARKET ENDPOINTS ==========

    async def search_markets(
        self,
        status: Optional[str] = None,
        series_ticker: Optional[str] = None,
        max_close_ts: Optional[int] = None,
        min_close_ts: Optional[int] = None,
        limit: int = 100,
        cursor: Optional[str] = None,
    ) -> tuple[List[Market], Optional[str]]:
        """Search and filter markets.

        Args:
            status: Market status filter (unopened, open, closed, settled)
            series_ticker: Filter by series
            max_close_ts: Maximum close timestamp (Unix seconds)
            min_close_ts: Minimum close timestamp (Unix seconds)
            limit: Number of results (max 1000)
            cursor: Pagination cursor

        Returns:
            Tuple of (markets list, next cursor or None)
        """
        params = {"limit": limit}
        if status:
            params["status"] = status
        if series_ticker:
            params["series_ticker"] = series_ticker
        if max_close_ts:
            params["max_close_ts"] = max_close_ts
        if min_close_ts:
            params["min_close_ts"] = min_close_ts
        if cursor:
            params["cursor"] = cursor

        response = await self._request("GET", "/markets", params=params, authenticated=False)
        markets = [Market(**m) for m in response.get("markets", [])]
        return markets, response.get("cursor")

    async def get_market(self, ticker: str) -> Market:
        """Get market details.

        Args:
            ticker: Market ticker

        Returns:
            Market object
        """
        response = await self._request("GET", f"/markets/{ticker}", authenticated=False)
        # API wraps response in "market" key
        market_data = response.get("market", response)
        return Market(**market_data)

    async def get_orderbook(self, ticker: str, depth: int = 5) -> Orderbook:
        """Get current order book.

        Args:
            ticker: Market ticker
            depth: Order book depth (0/-1 for full, 1-100 for specific depth)

        Returns:
            Orderbook object
        """
        params = {}
        if depth != -1:
            params["depth"] = depth

        response = await self._request("GET", f"/markets/{ticker}/orderbook", params=params)
        # API wraps response in "orderbook" key, need to add ticker
        orderbook_data = response.get("orderbook", response)
        orderbook_data["ticker"] = ticker
        # Ensure timestamp is present
        if "timestamp" not in orderbook_data:
            orderbook_data["timestamp"] = response.get("timestamp", int(time.time() * 1000))
        return Orderbook(**orderbook_data)

    async def get_trades(
        self,
        ticker: Optional[str] = None,
        limit: int = 100,
        before: Optional[int] = None,
        after: Optional[int] = None,
    ) -> tuple[List[Trade], Optional[str]]:
        """Get recent trades.

        Args:
            ticker: Filter by market ticker
            limit: Number of results
            before: Timestamp filter (Unix ms)
            after: Timestamp filter (Unix ms)

        Returns:
            Tuple of (trades list, next cursor)
        """
        params = {"limit": limit}
        if ticker:
            params["ticker"] = ticker
        if before:
            params["before"] = before
        if after:
            params["after"] = after

        response = await self._request("GET", "/markets/trades", params=params, authenticated=False)
        trades = [Trade(**t) for t in response.get("trades", [])]
        return trades, response.get("cursor")

    async def get_candlesticks(
        self,
        series_ticker: str,
        ticker: str,
        interval: str = "1440min",
    ) -> List[Candlestick]:
        """Get historical candlestick (OHLCV) data.

        Args:
            series_ticker: Series ticker
            ticker: Market ticker
            interval: Time interval (1min, 60min, 1440min)

        Returns:
            List of candlesticks
        """
        params = {"interval": interval}
        response = await self._request(
            "GET",
            f"/series/{series_ticker}/markets/{ticker}/candlesticks",
            params=params,
            authenticated=False,
        )
        return [Candlestick(**c) for c in response.get("candlesticks", [])]

    # ========== EVENT & SERIES ENDPOINTS ==========

    async def get_events(
        self,
        status: Optional[str] = None,
        limit: int = 100,
        cursor: Optional[str] = None,
    ) -> tuple[List[Event], Optional[str]]:
        """Get events.

        Args:
            status: Event status filter (open, closed, settled)
            limit: Number of results
            cursor: Pagination cursor

        Returns:
            Tuple of (events list, next cursor)
        """
        params = {"limit": limit}
        if status:
            params["status"] = status
        if cursor:
            params["cursor"] = cursor

        response = await self._request("GET", "/events", params=params, authenticated=False)
        events = [Event(**e) for e in response.get("events", [])]
        return events, response.get("cursor")

    async def get_event(self, ticker: str, include_markets: bool = False) -> Event:
        """Get event details.

        Args:
            ticker: Event ticker
            include_markets: Include nested markets

        Returns:
            Event object
        """
        params = {}
        if include_markets:
            params["include_markets"] = "true"

        response = await self._request("GET", f"/events/{ticker}", params=params, authenticated=False)
        # API wraps response in "event" key
        event_data = response.get("event", response)
        return Event(**event_data)

    async def get_event_metadata(self, ticker: str) -> Dict[str, Any]:
        """Get event metadata - additional event details.

        Args:
            ticker: Event ticker

        Returns:
            Dictionary of event metadata
        """
        response = await self._request("GET", f"/events/{ticker}/metadata", authenticated=False)
        # API wraps response in "metadata" key
        return response.get("metadata", response)

    async def get_series(
        self,
        category: Optional[str] = None,
        limit: int = 100,
        cursor: Optional[str] = None,
    ) -> tuple[List[Series], Optional[str]]:
        """Get series templates.

        Args:
            category: Filter by category
            limit: Number of results
            cursor: Pagination cursor

        Returns:
            Tuple of (series list, next cursor)
        """
        params = {"limit": limit}
        if category:
            params["category"] = category
        if cursor:
            params["cursor"] = cursor

        response = await self._request("GET", "/series", params=params, authenticated=False)
        series_list = [Series(**s) for s in response.get("series", [])]
        return series_list, response.get("cursor")

    async def get_milestones(
        self,
        category: Optional[str] = None,
        source: Optional[str] = None,
        min_ts: Optional[int] = None,
        max_ts: Optional[int] = None,
    ) -> List[Milestone]:
        """Get milestones.

        Args:
            category: Filter by category
            source: Filter by source
            min_ts: Minimum timestamp (Unix seconds)
            max_ts: Maximum timestamp (Unix seconds)

        Returns:
            List of milestones
        """
        params = {}
        if category:
            params["category"] = category
        if source:
            params["source"] = source
        if min_ts:
            params["min_ts"] = min_ts
        if max_ts:
            params["max_ts"] = max_ts

        response = await self._request("GET", "/milestones", params=params, authenticated=False)
        return [Milestone(**m) for m in response.get("milestones", [])]

    # ========== PORTFOLIO ENDPOINTS ==========

    async def get_balance(self) -> Balance:
        """Get account balance and portfolio value.

        Returns:
            Balance object
        """
        response = await self._request("GET", "/portfolio/balance")
        # Balance response is flat: {"balance": int, "portfolio_value": int}
        return Balance(**response)

    async def get_positions(
        self,
        ticker: Optional[str] = None,
        event_ticker: Optional[str] = None,
        limit: int = 100,
        cursor: Optional[str] = None,
    ) -> tuple[List[Position], Optional[str]]:
        """Get user positions.

        Args:
            ticker: Filter by market ticker
            event_ticker: Filter by event ticker
            limit: Number of results
            cursor: Pagination cursor

        Returns:
            Tuple of (positions list, next cursor)
        """
        params = {"limit": limit}
        if ticker:
            params["ticker"] = ticker
        if event_ticker:
            params["event_ticker"] = event_ticker
        if cursor:
            params["cursor"] = cursor

        response = await self._request("GET", "/portfolio/positions", params=params)
        positions = [Position(**p) for p in response.get("positions", [])]
        return positions, response.get("cursor")

    async def create_order(
        self,
        ticker: str,
        side: str,
        count: int,
        type: str = "limit",
        price: Optional[int] = None,
        expire_at: Optional[int] = None,
        order_group_id: Optional[str] = None,
    ) -> Order:
        """Create a new order.

        Args:
            ticker: Market ticker
            side: "buy" or "sell"
            count: Number of contracts
            type: "limit" or "market"
            price: Limit price in cents (required for limit orders)
            expire_at: Order expiration timestamp (Unix seconds)
            order_group_id: Optional order group ID

        Returns:
            Order object
        """
        payload = {
            "ticker": ticker,
            "side": side,
            "type": type,
            "count": count,
        }
        if price is not None:
            payload["price"] = price
        if expire_at:
            payload["expire_at"] = expire_at
        if order_group_id:
            payload["order_group_id"] = order_group_id

        response = await self._request("POST", "/portfolio/orders", json=payload)
        # Order responses are typically flat
        return Order(**response)

    async def get_orders(
        self,
        ticker: Optional[str] = None,
        event_ticker: Optional[str] = None,
        status: Optional[str] = None,
        min_ts: Optional[int] = None,
        max_ts: Optional[int] = None,
        limit: int = 100,
        cursor: Optional[str] = None,
    ) -> tuple[List[Order], Optional[str]]:
        """Get user orders.

        Args:
            ticker: Filter by market ticker
            event_ticker: Filter by event ticker
            status: Filter by status (resting, canceled, executed)
            min_ts: Minimum timestamp (Unix seconds)
            max_ts: Maximum timestamp (Unix seconds)
            limit: Number of results
            cursor: Pagination cursor

        Returns:
            Tuple of (orders list, next cursor)
        """
        params = {"limit": limit}
        if ticker:
            params["ticker"] = ticker
        if event_ticker:
            params["event_ticker"] = event_ticker
        if status:
            params["status"] = status
        if min_ts:
            params["min_ts"] = min_ts
        if max_ts:
            params["max_ts"] = max_ts
        if cursor:
            params["cursor"] = cursor

        response = await self._request("GET", "/portfolio/orders", params=params)
        orders = [Order(**o) for o in response.get("orders", [])]
        return orders, response.get("cursor")

    async def cancel_order(self, order_id: str) -> Order:
        """Cancel an order.

        Args:
            order_id: Order ID

        Returns:
            Updated order object
        """
        response = await self._request("DELETE", f"/portfolio/orders/{order_id}")
        # Order responses are typically flat
        return Order(**response)

    async def amend_order(
        self,
        order_id: str,
        price: Optional[int] = None,
        count: Optional[int] = None,
    ) -> Order:
        """Modify an order.

        Args:
            order_id: Order ID
            price: New limit price (cents)
            count: New contract count

        Returns:
            Updated order object
        """
        payload = {}
        if price is not None:
            payload["price"] = price
        if count is not None:
            payload["count"] = count

        response = await self._request("POST", f"/portfolio/orders/{order_id}/amend", json=payload)
        # Order responses are typically flat
        return Order(**response)

    async def get_fills(
        self,
        ticker: Optional[str] = None,
        order_id: Optional[str] = None,
        min_ts: Optional[int] = None,
        max_ts: Optional[int] = None,
        limit: int = 100,
        cursor: Optional[str] = None,
    ) -> tuple[List[Fill], Optional[str]]:
        """Get executed fills/trades.

        Args:
            ticker: Filter by market ticker
            order_id: Filter by order ID
            min_ts: Minimum timestamp (Unix seconds)
            max_ts: Maximum timestamp (Unix seconds)
            limit: Number of results
            cursor: Pagination cursor

        Returns:
            Tuple of (fills list, next cursor)
        """
        params = {"limit": limit}
        if ticker:
            params["ticker"] = ticker
        if order_id:
            params["order_id"] = order_id
        if min_ts:
            params["min_ts"] = min_ts
        if max_ts:
            params["max_ts"] = max_ts
        if cursor:
            params["cursor"] = cursor

        response = await self._request("GET", "/portfolio/fills", params=params)
        fills = [Fill(**f) for f in response.get("fills", [])]
        return fills, response.get("cursor")

    async def get_queue_position(self, order_id: str) -> QueuePosition:
        """Get order's queue position.

        Args:
            order_id: Order ID

        Returns:
            QueuePosition object
        """
        response = await self._request("GET", f"/portfolio/orders/{order_id}/queue_position")
        # API may wrap response in "queue_position" key, ensure order_id is present
        queue_data = response.get("queue_position", response)
        queue_data["order_id"] = order_id
        return QueuePosition(**queue_data)

    # ========== EXCHANGE ENDPOINTS ==========

    async def get_exchange_status(self) -> ExchangeStatus:
        """Get exchange status.

        Returns:
            ExchangeStatus object
        """
        response = await self._request("GET", "/exchange/status", authenticated=False)
        # API may wrap response in "status" key
        status_data = response.get("status", response)
        return ExchangeStatus(**status_data)

    # ========== BATCH OPERATIONS ==========

    async def batch_create_orders(self, orders: List[Dict[str, Any]]) -> List[Order]:
        """Create multiple orders in a batch (max 20).

        Args:
            orders: List of order dictionaries

        Returns:
            List of created Order objects
        """
        if len(orders) > 20:
            raise ValueError("Maximum 20 orders per batch")

        payload = {"orders": orders}
        response = await self._request("POST", "/portfolio/orders/batched", json=payload)
        return [Order(**o) for o in response.get("orders", [])]

    async def batch_cancel_orders(self, order_ids: List[str]) -> List[Order]:
        """Cancel multiple orders in a batch (max 20).

        Args:
            order_ids: List of order IDs

        Returns:
            List of canceled Order objects
        """
        if len(order_ids) > 20:
            raise ValueError("Maximum 20 orders per batch")

        payload = {"order_ids": order_ids}
        response = await self._request("DELETE", "/portfolio/orders/batched", json=payload)
        return [Order(**o) for o in response.get("orders", [])]

    # ========== ORDER GROUP MANAGEMENT ==========

    async def get_order_group(self, group_id: str) -> OrderGroup:
        """Get a single order group by ID.

        Args:
            group_id: Order group ID

        Returns:
            OrderGroup object
        """
        response = await self._request("GET", f"/portfolio/order_groups/{group_id}")
        return OrderGroup(**response)

    async def reset_order_group(self, group_id: str) -> None:
        """Reset an order group's matched contract counter.

        Args:
            group_id: Order group ID
        """
        await self._request("PUT", f"/portfolio/order_groups/{group_id}/reset")

    async def delete_order_group(self, group_id: str) -> None:
        """Delete an order group.

        Args:
            group_id: Order group ID
        """
        await self._request("DELETE", f"/portfolio/order_groups/{group_id}")

    # ========== PORTFOLIO METRICS ==========

    async def get_total_resting_order_value(self) -> TotalRestingOrderValue:
        """Get total value of all resting orders.

        Returns:
            TotalRestingOrderValue object with total in cents
        """
        response = await self._request("GET", "/portfolio/summary/total_resting_order_value")
        return TotalRestingOrderValue(**response)

    async def get_settlements(
        self,
        limit: int = 100,
        cursor: Optional[str] = None,
    ) -> tuple[List[Settlement], Optional[str]]:
        """Get historical settlements (filled orders).

        Args:
            limit: Number of results (default 100, max 200)
            cursor: Pagination cursor

        Returns:
            Tuple of (list of Settlement objects, next cursor)
        """
        params: Dict[str, Any] = {"limit": limit}
        if cursor:
            params["cursor"] = cursor

        response = await self._request("GET", "/portfolio/settlements", params=params)
        settlements = [Settlement(**s) for s in response.get("settlements", [])]
        return settlements, response.get("cursor")

    # ========== ORDER MODIFICATIONS ==========

    async def decrease_order(self, order_id: str, count: int) -> Order:
        """Decrease the size of an existing order.

        Args:
            order_id: Order ID to decrease
            count: Number of contracts to decrease by

        Returns:
            Updated Order object
        """
        payload = {"count": count}
        response = await self._request("POST", f"/portfolio/orders/{order_id}/decrease", json=payload)
        return Order(**response.get("order", response))

    async def get_queue_positions(self, order_ids: List[str]) -> Dict[str, int]:
        """Get queue positions for multiple orders in bulk.

        Args:
            order_ids: List of order IDs to check

        Returns:
            Dictionary mapping order_id to queue position
        """
        payload = {"order_ids": order_ids}
        response = await self._request("POST", "/portfolio/orders/queue_positions", json=payload)

        # API returns dict with order_id -> QueuePosition mapping
        # Extract just the position numbers
        positions = {}
        queue_positions_data = response.get("queue_positions", {})
        for order_id, pos_data in queue_positions_data.items():
            if isinstance(pos_data, dict):
                positions[order_id] = pos_data.get("position", 0)
            else:
                positions[order_id] = pos_data
        return positions

    # ========== MULTIVARIATE COLLECTIONS ==========

    async def get_multivariate_collections(
        self,
        status: Optional[str] = None,
        limit: int = 100,
        cursor: Optional[str] = None,
    ) -> tuple[List[MultivarianateCollection], Optional[str]]:
        """Get multivariate event collections.

        Args:
            status: Filter by status (open, closed, settled)
            limit: Number of results
            cursor: Pagination cursor

        Returns:
            Tuple of (list of collections, next cursor)
        """
        params: Dict[str, Any] = {"limit": limit}
        if status:
            params["status"] = status
        if cursor:
            params["cursor"] = cursor

        response = await self._request("GET", "/multivariate_collections", params=params, authenticated=False)
        collections = [
            MultivarianateCollection(**c) for c in response.get("collections", [])
        ]
        return collections, response.get("cursor")

    async def get_multivariate_collection(self, ticker: str) -> MultivarianateCollection:
        """Get a specific multivariate collection.

        Args:
            ticker: Collection ticker

        Returns:
            MultivarianateCollection object
        """
        response = await self._request(
            "GET",
            f"/multivariate_collections/{ticker}",
            authenticated=False,
        )
        collection_data = response.get("collection", response)
        return MultivarianateCollection(**collection_data)

    async def get_markets_in_collection(
        self,
        collection_ticker: str,
        limit: int = 100,
        cursor: Optional[str] = None,
    ) -> tuple[List[MarketInCollection], Optional[str]]:
        """Get markets within a multivariate collection.

        Args:
            collection_ticker: Collection ticker
            limit: Number of results
            cursor: Pagination cursor

        Returns:
            Tuple of (list of markets, next cursor)
        """
        params: Dict[str, Any] = {"limit": limit}
        if cursor:
            params["cursor"] = cursor

        response = await self._request(
            "GET",
            f"/multivariate_collections/{collection_ticker}/markets",
            params=params,
            authenticated=False,
        )
        markets = [MarketInCollection(**m) for m in response.get("markets", [])]
        return markets, response.get("cursor")

    async def lookup_market_in_collection(
        self,
        collection_ticker: str,
        market_ticker: str,
    ) -> CollectionLookup:
        """Lookup a specific market within a collection.

        Args:
            collection_ticker: Collection ticker
            market_ticker: Market ticker to lookup

        Returns:
            CollectionLookup object with tickers
        """
        response = await self._request(
            "POST",
            f"/multivariate_collections/{collection_ticker}/lookup",
            json={"market_ticker": market_ticker},
            authenticated=False,
        )
        lookup_data = response.get("lookup", response)
        return CollectionLookup(**lookup_data)

    # ========== COMMUNICATIONS: RFQs ==========

    async def create_rfq(
        self,
        ticker: str,
        side: str,
        count: int,
    ) -> RFQ:
        """Create a Request for Quote.

        Args:
            ticker: Market ticker
            side: "buy" or "sell"
            count: Number of contracts

        Returns:
            Created RFQ object
        """
        payload = {
            "ticker": ticker,
            "side": side,
            "count": count,
        }
        response = await self._request("POST", "/communications/rfq", json=payload)
        return RFQ(**response.get("rfq", response))

    async def get_rfqs(
        self,
        status: Optional[str] = None,
        ticker: Optional[str] = None,
        limit: int = 100,
        cursor: Optional[str] = None,
    ) -> tuple[List[RFQ], Optional[str]]:
        """Get RFQs (Request for Quotes).

        Args:
            status: Filter by status
            ticker: Filter by market ticker
            limit: Number of results
            cursor: Pagination cursor

        Returns:
            Tuple of (list of RFQs, next cursor)
        """
        params: Dict[str, Any] = {"limit": limit}
        if status:
            params["status"] = status
        if ticker:
            params["ticker"] = ticker
        if cursor:
            params["cursor"] = cursor

        response = await self._request("GET", "/communications/rfq", params=params)
        rfqs = [RFQ(**r) for r in response.get("rfqs", [])]
        return rfqs, response.get("cursor")

    async def get_rfq(self, rfq_id: str) -> RFQ:
        """Get a specific RFQ.

        Args:
            rfq_id: RFQ ID

        Returns:
            RFQ object
        """
        response = await self._request("GET", f"/communications/rfq/{rfq_id}")
        return RFQ(**response.get("rfq", response))

    async def delete_rfq(self, rfq_id: str) -> None:
        """Delete an RFQ.

        Args:
            rfq_id: RFQ ID to delete
        """
        await self._request("DELETE", f"/communications/rfq/{rfq_id}")

    # ========== COMMUNICATIONS: QUOTES ==========

    async def create_quote(
        self,
        rfq_id: str,
        price: int,
        quantity: int,
    ) -> Quote:
        """Create a quote response to an RFQ.

        Args:
            rfq_id: RFQ ID to respond to
            price: Quote price (cents)
            quantity: Quote quantity

        Returns:
            Created Quote object
        """
        payload = {
            "price": price,
            "quantity": quantity,
        }
        response = await self._request("POST", f"/communications/rfq/{rfq_id}/quote", json=payload)
        return Quote(**response.get("quote", response))

    async def get_quotes(
        self,
        rfq_id: str,
        limit: int = 100,
        cursor: Optional[str] = None,
    ) -> tuple[List[Quote], Optional[str]]:
        """Get quotes for a specific RFQ.

        Args:
            rfq_id: RFQ ID
            limit: Number of results
            cursor: Pagination cursor

        Returns:
            Tuple of (list of quotes, next cursor)
        """
        params: Dict[str, Any] = {"limit": limit}
        if cursor:
            params["cursor"] = cursor

        response = await self._request("GET", f"/communications/rfq/{rfq_id}/quote", params=params)
        quotes = [Quote(**q) for q in response.get("quotes", [])]
        return quotes, response.get("cursor")

    async def accept_quote(self, quote_id: str) -> Quote:
        """Accept a quote response.

        Args:
            quote_id: Quote ID to accept

        Returns:
            Updated Quote object
        """
        response = await self._request("POST", f"/communications/quote/{quote_id}/accept")
        return Quote(**response.get("quote", response))

    async def confirm_quote(self, quote_id: str) -> Quote:
        """Confirm an accepted quote.

        Args:
            quote_id: Quote ID to confirm

        Returns:
            Updated Quote object
        """
        response = await self._request("POST", f"/communications/quote/{quote_id}/confirm")
        return Quote(**response.get("quote", response))

    async def delete_quote(self, quote_id: str) -> None:
        """Delete a quote.

        Args:
            quote_id: Quote ID to delete
        """
        await self._request("DELETE", f"/communications/quote/{quote_id}")

    # ========== WEBSOCKET STREAMING ==========

    async def get_websocket_connection(self, connection_id: Optional[str] = None) -> KalshiWebSocketClient:
        """Get or create a WebSocket connection.

        Implements connection pooling - reuses existing connections if available.

        Args:
            connection_id: Optional connection ID (creates new if not provided)

        Returns:
            KalshiWebSocketClient instance
        """
        if not connection_id:
            connection_id = f"ws-{int(time.time() * 1000)}"

        # Return existing connection if available
        if connection_id in self._websocket_connections:
            conn = self._websocket_connections[connection_id]
            if conn.is_connected():
                return conn

        # Create new connection
        ws_client = KalshiWebSocketClient(
            api_key_id=self.api_key_id,
            private_key_pem=self.private_key,
            timeout=self.timeout,
        )

        # Store in pool
        self._websocket_connections[connection_id] = ws_client

        return ws_client

    @classmethod
    async def close_all_websockets(cls) -> None:
        """Close all WebSocket connections in the pool.

        Should be called on application shutdown.
        """
        for connection_id, ws_client in cls._websocket_connections.items():
            try:
                await ws_client.disconnect()
            except Exception as e:
                logger.error(f"Error closing WebSocket {connection_id}: {e}")

        cls._websocket_connections.clear()
        logger.info("All WebSocket connections closed")
