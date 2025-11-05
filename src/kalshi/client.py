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
    BatchOrderRequest,
    BatchOrderResponse,
    OrderGroup,
)


class KalshiClient:
    """Wrapper for Kalshi API with authentication and rate limiting."""

    def __init__(
        self,
        api_key: str,
        private_key: Optional[str] = None,
        private_key_path: Optional[str] = None,
        base_url: str = "https://trading-api.kalshi.com",
        api_version: str = "v2",
    ):
        """
        Initialize Kalshi API client.

        Args:
            api_key: Kalshi API key
            private_key: Private key content as PEM-encoded string (NEW)
            private_key_path: Path to private key file (EXISTING)
            base_url: API base URL
            api_version: API version

        Note:
            Must provide either private_key (direct content) or private_key_path (file).
            private_key takes precedence if both are provided.
        """
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.api_version = api_version
        self.client = httpx.AsyncClient(timeout=30.0)

        # Load private key for request signing
        # Try direct key content first, then fall back to file path
        key_bytes = None

        if private_key:
            # Direct key content - encode string to bytes
            logger.info("Loading private key from KALSHI_PRIVATE_KEY environment variable")
            key_bytes = private_key.encode('utf-8')
        elif private_key_path:
            # File path - read from file
            logger.info(f"Loading private key from file: {private_key_path}")
            key_path = Path(private_key_path).expanduser()
            if not key_path.exists():
                raise FileNotFoundError(f"Private key file not found: {key_path}")

            with open(key_path, "rb") as f:
                key_bytes = f.read()
        else:
            raise ValueError(
                "Must provide either 'private_key' (direct content) or "
                "'private_key_path' (file path)"
            )

        # Parse PEM-encoded key (works for both sources)
        self.private_key = serialization.load_pem_private_key(
            key_bytes, password=None, backend=default_backend()
        )

        logger.info(f"Initialized Kalshi client: {self.base_url}")

    @classmethod
    def from_env(cls, environment: Optional[str] = None) -> "KalshiClient":
        """
        Create client from environment variables.

        Args:
            environment: Override environment ("demo" or "production")
                        If None, uses KALSHI_ENVIRONMENT env var

        Environment Variables:
            KALSHI_API_KEY: API key (required)
            KALSHI_PRIVATE_KEY: Private key content as PEM string (NEW - takes precedence)
            KALSHI_PRIVATE_KEY_PATH: Path to private key file (EXISTING - fallback)
            KALSHI_ENVIRONMENT: Environment name ("demo" or "production")
            KALSHI_BASE_URL: API base URL (optional, auto-selected based on environment)
            KALSHI_API_VERSION: API version (default: "v2")
        """
        env = environment or os.getenv("KALSHI_ENVIRONMENT", "demo")

        api_key = os.getenv("KALSHI_API_KEY")
        if not api_key:
            raise ValueError("KALSHI_API_KEY environment variable not set")

        # Try direct key first (new), then fall back to file path (existing)
        private_key = os.getenv("KALSHI_PRIVATE_KEY")
        private_key_path = os.getenv("KALSHI_PRIVATE_KEY_PATH")

        if not private_key and not private_key_path:
            raise ValueError(
                "Must set either KALSHI_PRIVATE_KEY (direct key content) or "
                "KALSHI_PRIVATE_KEY_PATH (file path)"
            )

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
            private_key=private_key,
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

    async def _paginate(
        self,
        endpoint: str,
        result_key: str,
        params: Optional[dict[str, Any]] = None,
        max_results: Optional[int] = None,
    ) -> list[dict[str, Any]]:
        """
        Fetch all paginated results using cursor-based pagination.

        Args:
            endpoint: API endpoint (e.g., "markets")
            result_key: Key in response containing results (e.g., "markets")
            params: Initial query parameters
            max_results: Maximum total results to fetch (None = fetch all)

        Returns:
            List of all result items across all pages
        """
        params = params or {}
        all_results = []
        cursor = None
        page_size = 100  # Kalshi's max per page

        while True:
            # Add cursor to params if we have one
            if cursor:
                params["cursor"] = cursor

            # Fetch page
            data = await self._request("GET", endpoint, params=params)
            results = data.get(result_key, [])
            all_results.extend(results)

            # Check if we've hit max_results
            if max_results and len(all_results) >= max_results:
                return all_results[:max_results]

            # Check for next page
            cursor = data.get("cursor")
            if not cursor:
                # No more pages
                break

        return all_results

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
        Search for markets with client-side text filtering.

        Note: Kalshi API has no text search. This method fetches markets page-by-page
        and filters locally by title/subtitle. Stops early once enough matches found.

        Args:
            query: Text to search in market titles/subtitles (case-insensitive)
            limit: Maximum number of results to return
            status: Market status filter (open, closed, settled)

        Returns:
            List of matching markets
        """
        if query:
            # Fetch pages incrementally and filter as we go
            logger.info(f"Searching for '{query}' - fetching pages incrementally (need {limit} matches)")
            query_lower = query.lower()
            filtered = []
            cursor = None
            params = {"status": status, "limit": 100}
            page_num = 0
            max_pages = 100  # Safety limit to prevent infinite loops

            while len(filtered) < limit and page_num < max_pages:
                page_num += 1
                # Add cursor if we have one
                if cursor:
                    params["cursor"] = cursor

                # Fetch next page
                logger.info(f"Fetching page {page_num} (have {len(filtered)}/{limit} matches so far)")
                data = await self._request("GET", "markets", params=params)
                markets = data.get("markets", [])
                logger.info(f"Page {page_num}: received {len(markets)} markets")

                # Filter this page
                matches_this_page = 0
                for m in markets:
                    title = m.get("title", "").lower()
                    subtitle = m.get("subtitle", "").lower()
                    if query_lower in title or query_lower in subtitle:
                        filtered.append(m)
                        matches_this_page += 1
                        if len(filtered) >= limit:
                            break  # Have enough matches

                logger.info(f"Page {page_num}: found {matches_this_page} matches (total: {len(filtered)}/{limit})")

                # Check for next page
                cursor = data.get("cursor")
                if not cursor:
                    logger.info("No more pages available")
                    break

            if page_num >= max_pages:
                logger.warning(f"Hit max pages limit ({max_pages}) - returning {len(filtered)} matches")

            logger.info(f"Search complete: returning {len(filtered)} matches for '{query}'")
            return [Market(**m) for m in filtered]

        else:
            # No query - just fetch requested number of markets
            params = {"status": status, "limit": 100}
            markets_data = await self._paginate(
                "markets", "markets", params=params, max_results=limit
            )
            return [Market(**m) for m in markets_data]

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
        Get list of events with pagination support.

        Args:
            limit: Maximum number of results
            status: Event status filter

        Returns:
            List of events
        """
        params = {"status": status, "limit": 100}
        events = await self._paginate("events", "events", params=params, max_results=limit)
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
        Get recent public trades with pagination support.

        Args:
            ticker: Filter by market ticker (optional)
            limit: Maximum number of trades

        Returns:
            List of recent trades
        """
        params = {"limit": 100}
        if ticker:
            params["ticker"] = ticker

        trades = await self._paginate("markets/trades", "trades", params=params, max_results=limit)
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
        order_group_id: Optional[str] = None,
        # Advanced parameters
        time_in_force: Optional[str] = None,
        expiration_ts: Optional[int] = None,
        post_only: Optional[bool] = None,
        reduce_only: Optional[bool] = None,
        self_trade_prevention_type: Optional[str] = None,
        buy_max_cost: Optional[int] = None,
        sell_position_floor: Optional[int] = None,
    ) -> Order:
        """
        Create an order with optional advanced parameters.

        Args:
            ticker: Market ticker
            side: "yes" or "no"
            count: Number of contracts
            action: "buy" or "sell" (default: "buy")
            order_type: "market" or "limit" (default: "market")
            yes_price: Limit price for yes side (cents, 1-99)
            no_price: Limit price for no side (cents, 1-99)
            order_group_id: Optional order group ID to associate order with

        Advanced Parameters:
            time_in_force: "fok" (Fill-or-Kill), "ioc" (Immediate-or-Cancel), "gtc" (Good-til-Cancel), "gtt" (Good-til-Time)
            expiration_ts: Unix timestamp for order expiration (required if time_in_force="gtt")
            post_only: If True, order will only be accepted as a maker order (no immediate fill)
            reduce_only: If True, order will only reduce existing position, not increase it
            self_trade_prevention_type: "cancel_resting", "cancel_aggressing", or "cancel_both"
            buy_max_cost: Maximum cost in cents for buy orders (risk limit)
            sell_position_floor: Minimum position after sell (prevents overselling)

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

        # Optional parameters
        if order_group_id:
            payload["order_group_id"] = order_group_id

        if time_in_force:
            payload["time_in_force"] = time_in_force

        if expiration_ts:
            payload["expiration_ts"] = expiration_ts

        if post_only is not None:
            payload["post_only"] = post_only

        if reduce_only is not None:
            payload["reduce_only"] = reduce_only

        if self_trade_prevention_type:
            payload["self_trade_prevention_type"] = self_trade_prevention_type

        if buy_max_cost is not None:
            payload["buy_max_cost"] = buy_max_cost

        if sell_position_floor is not None:
            payload["sell_position_floor"] = sell_position_floor

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
        # First get the existing order to retrieve required fields
        order_data = await self._request("GET", f"portfolio/orders/{order_id}")
        existing_order = order_data.get("order", order_data)

        # Build payload with all required fields from API
        payload = {
            "ticker": existing_order["ticker"],
            "side": existing_order["side"],
            "action": existing_order["action"],
            "count": new_count,
        }

        # Add price based on side
        if existing_order["side"] == "yes":
            payload["yes_price"] = new_price
        else:
            payload["no_price"] = new_price

        # Call the correct endpoint (POST with /amend suffix)
        data = await self._request(
            "POST", f"portfolio/orders/{order_id}/amend", json_data=payload
        )

        # API returns both old_order and new_order
        return Order(**data.get("new_order", data))

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
        Get orders with pagination support.

        Args:
            ticker: Filter by ticker (optional)
            status: Filter by status (default: "resting")
            limit: Maximum results

        Returns:
            List of orders
        """
        params = {"status": status, "limit": 100}
        if ticker:
            params["ticker"] = ticker

        orders = await self._paginate("portfolio/orders", "orders", params=params, max_results=limit)
        return [Order(**o) for o in orders]

    # Portfolio Operations

    async def get_positions(
        self,
        ticker: Optional[str] = None,
        limit: int = 100,
        settlement_status: Optional[str] = None,
    ) -> list[Position]:
        """
        Get portfolio positions with pagination support.

        Args:
            ticker: Filter by ticker (optional)
            limit: Maximum results
            settlement_status: Filter by settlement status (optional)

        Returns:
            List of positions
        """
        params = {"limit": 100}
        if ticker:
            params["ticker"] = ticker
        if settlement_status:
            params["settlement_status"] = settlement_status

        positions = await self._paginate("portfolio/positions", "positions", params=params, max_results=limit)
        return [Position(**p) for p in positions]

    async def get_fills(
        self,
        ticker: Optional[str] = None,
        order_id: Optional[str] = None,
        limit: int = 100,
    ) -> list[Fill]:
        """
        Get trade fills with pagination support.

        Args:
            ticker: Filter by ticker (optional)
            order_id: Filter by order ID (optional)
            limit: Maximum results

        Returns:
            List of fills
        """
        params = {"limit": 100}
        if ticker:
            params["ticker"] = ticker
        if order_id:
            params["order_id"] = order_id

        fills = await self._paginate("portfolio/fills", "fills", params=params, max_results=limit)
        return [Fill(**f) for f in fills]

    # Batch Operations

    async def batch_create_orders(
        self, orders: list[dict[str, Any]]
    ) -> list[BatchOrderResponse]:
        """
        Create multiple orders in a single batch request.

        Args:
            orders: List of order specifications (max 20 orders)
                   Each order dict should contain:
                   - ticker: str
                   - type: "market" or "limit"
                   - action: "buy" or "sell"
                   - side: "yes" or "no"
                   - count: int
                   - client_order_id: Optional[str]
                   - yes_price/no_price: Optional[int] (for limit orders)

        Returns:
            List of batch order responses (one per order)

        Note:
            Requires advanced access from Kalshi.
            Will raise HTTPError with 403 status if access not granted.
        """
        if len(orders) > 20:
            raise ValueError(f"Batch size {len(orders)} exceeds maximum of 20 orders")

        logger.info(f"Creating batch of {len(orders)} orders")

        # API expects "orders" array in request body
        data = await self._request("POST", "portfolio/orders/batched", json_data={"orders": orders})

        # Parse responses
        responses = []
        for item in data.get("orders", []):
            responses.append(BatchOrderResponse(**item))

        # Log summary
        successful = sum(1 for r in responses if r.is_success)
        failed = len(responses) - successful
        logger.info(f"Batch complete: {successful} succeeded, {failed} failed")

        return responses

    async def batch_cancel_orders(self, order_ids: list[str]) -> list[dict]:
        """
        Cancel multiple orders in a single batch request.

        Args:
            order_ids: List of order IDs to cancel (max 20 orders)

        Returns:
            List of cancellation results

        Note:
            Requires advanced access from Kalshi.
            Will raise HTTPError with 403 status if access not granted.
        """
        if len(order_ids) > 20:
            raise ValueError(f"Batch size {len(order_ids)} exceeds maximum of 20 orders")

        logger.info(f"Canceling batch of {len(order_ids)} orders")

        # API expects "ids" array in request body
        data = await self._request("DELETE", "portfolio/orders/batched", json_data={"ids": order_ids})

        # Log summary
        logger.info(f"Batch cancel complete: {len(order_ids)} orders processed")

        return data.get("orders", [])

    # Order Groups

    async def create_order_group(self, contracts_limit: int) -> OrderGroup:
        """
        Create an order group with contract limit.

        Args:
            contracts_limit: Maximum contracts that can be filled across all orders in group

        Returns:
            OrderGroup details

        Order groups allow you to link multiple orders with a shared contract limit.
        When the limit is reached, all remaining orders in the group are automatically canceled.
        Use this for OCO (One-Cancels-Other) behavior.
        """
        logger.info(f"Creating order group with limit: {contracts_limit} contracts")

        data = await self._request(
            "POST",
            "portfolio/order_groups/create",
            json_data={"contracts_limit": contracts_limit}
        )

        # API returns just {"order_group_id": "..."}, not a full object
        return OrderGroup(order_group_id=data["order_group_id"])

    async def get_order_group(self, group_id: str) -> OrderGroup:
        """
        Get order group details.

        Args:
            group_id: Order group ID

        Returns:
            OrderGroup details
        """
        data = await self._request("GET", f"portfolio/order_groups/{group_id}")
        # API returns {"is_auto_cancel_enabled": bool, "orders": [...]}
        # Add the group_id since it's not in the response
        return OrderGroup(order_group_id=group_id, **data)

    async def get_order_groups(self, limit: int = 100) -> list[OrderGroup]:
        """
        Get list of order groups with pagination support.

        Args:
            limit: Maximum number of order groups to return

        Returns:
            List of order groups
        """
        params = {"limit": 100}
        groups = await self._paginate(
            "portfolio/order_groups",
            "order_groups",
            params=params,
            max_results=limit
        )
        return [OrderGroup(**g) for g in groups]

    async def reset_order_group(self, group_id: str) -> OrderGroup:
        """
        Reset an order group (clears filled count, allows new orders).

        Args:
            group_id: Order group ID

        Returns:
            Updated OrderGroup details
        """
        logger.info(f"Resetting order group: {group_id}")

        await self._request(
            "POST",
            f"portfolio/order_groups/{group_id}/reset"
        )

        # Fetch the updated group details (API doesn't return full object on reset)
        return await self.get_order_group(group_id)

    async def delete_order_group(self, group_id: str) -> None:
        """
        Delete an order group.

        Args:
            group_id: Order group ID

        Note:
            This cancels all active orders in the group.
        """
        logger.info(f"Deleting order group: {group_id}")

        await self._request("DELETE", f"portfolio/order_groups/{group_id}")
        logger.info(f"Order group {group_id} deleted")

    async def close(self):
        """Close HTTP client."""
        await self.client.aclose()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()
