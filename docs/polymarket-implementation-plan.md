# Polymarket MCP Server - Implementation Plan & Architecture

**Version**: 1.0
**Date**: 2025-11-05
**Status**: Technical Specification

## Table of Contents

1. [Project Structure](#project-structure)
2. [Data Models](#data-models)
3. [Client Architecture](#client-architecture)
4. [Authentication System](#authentication-system)
5. [Implementation Sequence](#implementation-sequence)
6. [Testing Strategy](#testing-strategy)
7. [Deployment Guide](#deployment-guide)

---

## Project Structure

```
prediction-market-interface/
├── src/
│   ├── kalshi/                    # Existing Kalshi implementation
│   │   ├── __init__.py
│   │   ├── client.py
│   │   ├── models.py
│   │   └── kalshi_mcp_server.py
│   │
│   └── polymarket/                # NEW: Polymarket implementation
│       ├── __init__.py
│       ├── polymarket_mcp_server.py    # Main FastMCP server
│       │
│       ├── clients/               # API client layer
│       │   ├── __init__.py
│       │   ├── gamma_client.py   # Market data API (read-only)
│       │   ├── clob_client.py    # Trading API (authenticated)
│       │   └── base_client.py    # Shared HTTP utilities
│       │
│       ├── signing/               # Blockchain signing utilities
│       │   ├── __init__.py
│       │   ├── eip712.py         # EIP-712 structured data signing
│       │   ├── order_signer.py   # Order signature generation
│       │   └── auth_signer.py    # Authentication signature generation
│       │
│       ├── models/                # Pydantic data models
│       │   ├── __init__.py
│       │   ├── market.py         # Market, Event, Series models
│       │   ├── order.py          # Order, Fill, Position models
│       │   ├── auth.py           # API credentials models
│       │   └── enums.py          # OrderType, Side, etc.
│       │
│       ├── tools/                 # MCP tools (one file per category)
│       │   ├── __init__.py
│       │   ├── authentication.py  # API key management
│       │   ├── market_discovery.py # Search, browse, market data
│       │   ├── trading.py        # Order execution
│       │   └── portfolio.py      # Positions, fills, analytics
│       │
│       └── utils/                 # Shared utilities
│           ├── __init__.py
│           ├── validation.py     # Order validation, safety checks
│           ├── formatting.py     # LLM-friendly response formatting
│           └── constants.py      # Chain IDs, endpoints, limits
│
├── tests/
│   ├── kalshi/                   # Existing Kalshi tests
│   └── polymarket/               # NEW: Polymarket tests
│       ├── unit/
│       │   ├── test_signing.py
│       │   ├── test_models.py
│       │   └── test_validation.py
│       │
│       └── integration/
│           ├── test_gamma_client.py
│           ├── test_clob_client.py
│           ├── test_mcp_tools.py
│           └── test_e2e_trading.py
│
├── docs/
│   ├── kalshi-mcp-prd.md        # Existing Kalshi PRD
│   ├── polymarket-mcp-prd.md    # NEW: Polymarket PRD
│   └── polymarket-implementation-plan.md  # This file
│
├── .env.polymarket.example      # Environment template
├── run_polymarket_mcp.py        # MCP server wrapper script
└── pyproject.toml               # Add new dependencies
```

---

## Data Models

### Core Models (`src/polymarket/models/`)

**1. Market Models (`market.py`)**

```python
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class Market(BaseModel):
    """
    Polymarket market with binary outcomes.

    Markets represent a single question with YES/NO outcomes.
    Each outcome has a corresponding CLOB token ID for trading.
    """
    # Identifiers
    id: str = Field(..., description="Unique market ID")
    condition_id: str = Field(..., description="Blockchain condition ID")
    question_id: Optional[str] = None
    slug: Optional[str] = None

    # Market Details
    question: str = Field(..., description="Market question")
    description: Optional[str] = None
    outcomes: List[str] = Field(..., description="['YES', 'NO']")
    clob_token_ids: List[str] = Field(..., description="Token IDs for YES/NO")

    # Market State
    active: bool
    closed: bool
    accepting_orders: bool
    end_date: datetime
    resolution_source: Optional[str] = None

    # Pricing
    best_bid: Optional[float] = Field(None, ge=0.001, le=0.999)
    best_ask: Optional[float] = Field(None, ge=0.001, le=0.999)
    last_price: Optional[float] = None
    spread: Optional[float] = None

    # Volume & Liquidity (24h, 1w, 1m, 1y breakdowns)
    volume_24h: Optional[float] = None
    volume_24h_clob: Optional[float] = None  # CLOB-only volume
    liquidity: Optional[float] = None
    liquidity_clob: Optional[float] = None
    open_interest: Optional[float] = None

    # Market Metadata
    category: Optional[str] = None
    tags: Optional[List[str]] = None
    neg_risk: bool = False  # Special market type flag

    # Fees
    maker_base_fee: Optional[int] = Field(None, description="Fee in basis points")
    taker_base_fee: Optional[int] = Field(None, description="Fee in basis points")

    # Helper properties
    @property
    def interpretation(self) -> str:
        """Human-readable market summary."""
        if self.last_price:
            pct = int(self.last_price * 100)
            return f"Market implies {pct}% chance: {self.question}"
        return f"Market: {self.question}"

    @property
    def spread_bps(self) -> Optional[int]:
        """Bid-ask spread in basis points."""
        if self.best_bid and self.best_ask:
            return int((self.best_ask - self.best_bid) * 10000)
        return None

    @property
    def yes_token_id(self) -> str:
        """Token ID for YES outcome."""
        return self.clob_token_ids[0]

    @property
    def no_token_id(self) -> str:
        """Token ID for NO outcome."""
        return self.clob_token_ids[1]

    def get_token_id(self, outcome: str) -> str:
        """Get token ID for a specific outcome."""
        if outcome.upper() == "YES":
            return self.yes_token_id
        elif outcome.upper() == "NO":
            return self.no_token_id
        else:
            raise ValueError(f"Invalid outcome: {outcome}. Must be YES or NO")


class Event(BaseModel):
    """
    Polymarket event (collection of related markets).

    Events group multiple markets together (e.g., "2024 Election" event
    contains markets for different candidates, states, etc.).
    """
    id: str
    ticker: str
    slug: str
    title: str
    subtitle: Optional[str] = None
    description: Optional[str] = None

    # State
    active: bool
    closed: bool
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

    # Aggregated Metrics
    liquidity: Optional[float] = None
    volume: Optional[float] = None
    open_interest: Optional[float] = None
    volume_24h: Optional[float] = None

    # Metadata
    category: Optional[str] = None
    tags: Optional[List[str]] = None
    neg_risk: bool = False

    # Nested data
    markets: Optional[List[Market]] = None  # Can include related markets


class OrderBookLevel(BaseModel):
    """Single price level in order book."""
    price: float = Field(..., ge=0.001, le=0.999, description="Price in dollars")
    quantity: float = Field(..., gt=0, description="Number of shares")


class OrderBook(BaseModel):
    """
    Order book for a market.

    Polymarket orderbooks show bid/ask for both YES and NO sides.
    """
    market_id: str
    timestamp: datetime

    # YES outcome orderbook
    yes_bids: List[OrderBookLevel] = Field(default_factory=list)
    yes_asks: List[OrderBookLevel] = Field(default_factory=list)

    # NO outcome orderbook
    no_bids: List[OrderBookLevel] = Field(default_factory=list)
    no_asks: List[OrderBookLevel] = Field(default_factory=list)

    @property
    def yes_best_bid(self) -> Optional[OrderBookLevel]:
        return self.yes_bids[0] if self.yes_bids else None

    @property
    def yes_best_ask(self) -> Optional[OrderBookLevel]:
        return self.yes_asks[0] if self.yes_asks else None

    @property
    def yes_spread(self) -> Optional[float]:
        if self.yes_best_bid and self.yes_best_ask:
            return self.yes_best_ask.price - self.yes_best_bid.price
        return None

    @property
    def total_yes_bid_liquidity(self) -> float:
        return sum(level.quantity for level in self.yes_bids)

    @property
    def total_yes_ask_liquidity(self) -> float:
        return sum(level.quantity for level in self.yes_asks)
```

**2. Order Models (`order.py`)**

```python
from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class OrderSide(str, Enum):
    """Order side (buy or sell)."""
    BUY = "BUY"
    SELL = "SELL"


class OrderType(str, Enum):
    """Order type / time in force."""
    GTC = "GTC"  # Good-til-canceled
    FOK = "FOK"  # Fill-or-kill
    IOC = "IOC"  # Immediate-or-cancel


class OrderStatus(str, Enum):
    """Order status."""
    PENDING = "pending"
    OPEN = "open"
    MATCHED = "matched"
    LIVE = "live"
    FILLED = "filled"
    CANCELLED = "cancelled"
    EXPIRED = "expired"


class OrderParams(BaseModel):
    """
    Parameters for creating an order.

    These are the inputs provided by the user/LLM.
    Will be signed with EIP-712 before submission.
    """
    token_id: str = Field(..., description="CLOB token ID (YES or NO)")
    price: float = Field(..., ge=0.001, le=0.999, description="Price in dollars")
    size: float = Field(..., gt=0, description="Number of shares")
    side: OrderSide = Field(..., description="BUY or SELL")
    order_type: OrderType = Field(default=OrderType.GTC)

    # Optional advanced params
    fee_rate_bps: Optional[int] = None  # Custom fee rate
    nonce: Optional[int] = None  # Custom nonce
    expiration: Optional[int] = None  # Unix timestamp
    neg_risk: bool = False  # NegRisk market flag

    # Client tracking
    client_order_id: Optional[str] = None


class SignedOrder(BaseModel):
    """
    Signed order ready for submission to CLOB.

    Contains the EIP-712 signature and all order parameters.
    """
    # Original params
    params: OrderParams

    # EIP-712 signature components
    signature: str = Field(..., description="0x-prefixed hex signature")
    signer: str = Field(..., description="Ethereum address of signer")
    timestamp: int = Field(..., description="Unix timestamp when signed")

    # Additional metadata
    order_hash: Optional[str] = None  # Pre-computed order hash


class Order(BaseModel):
    """
    Order response from CLOB API.

    Represents an order's current state in the system.
    """
    order_id: str
    market: str  # Market ID or ticker
    asset_id: str  # Token ID
    owner: str  # Wallet address

    # Order details
    price: float
    original_size: float
    size_matched: float = 0.0
    outcome: str  # "YES" or "NO"
    side: OrderSide
    order_type: OrderType
    status: OrderStatus

    # Timestamps
    created_at: datetime
    last_update: Optional[datetime] = None
    expires_at: Optional[datetime] = None

    # Fees & Costs
    fee_rate_bps: Optional[int] = None
    maker_fees: Optional[float] = None
    taker_fees: Optional[float] = None

    @property
    def size_remaining(self) -> float:
        return self.original_size - self.size_matched

    @property
    def is_filled(self) -> bool:
        return self.status == OrderStatus.FILLED

    @property
    def is_active(self) -> bool:
        return self.status in [OrderStatus.OPEN, OrderStatus.LIVE, OrderStatus.PENDING]

    @property
    def fill_percentage(self) -> float:
        return (self.size_matched / self.original_size) * 100 if self.original_size > 0 else 0


class Fill(BaseModel):
    """
    Trade execution (fill) record.

    Represents a matched trade between maker and taker.
    """
    fill_id: str
    order_id: str
    market_id: str
    asset_id: str  # Token ID
    owner: str  # Your wallet address

    # Fill details
    side: OrderSide
    outcome: str
    price: float
    size: float
    timestamp: datetime

    # Fees
    fee_rate_bps: int
    fees_paid: float

    # Transaction
    trade_id: Optional[str] = None
    match_id: Optional[str] = None

    @property
    def total_cost(self) -> float:
        """Total cost including fees."""
        base_cost = self.price * self.size
        if self.side == OrderSide.BUY:
            return base_cost + self.fees_paid
        else:
            return base_cost - self.fees_paid

    @property
    def average_price_with_fees(self) -> float:
        """Average price per share including fees."""
        return self.total_cost / self.size if self.size > 0 else 0


class Position(BaseModel):
    """
    Current position in a market.

    Represents token holdings (YES or NO shares).
    """
    market_id: str
    asset_id: str  # Token ID
    outcome: str  # "YES" or "NO"

    # Position size
    size: float = Field(..., description="Number of shares held")

    # Cost basis
    average_entry_price: Optional[float] = None
    total_cost: Optional[float] = None

    # Current valuation
    current_price: Optional[float] = None

    @property
    def current_value(self) -> Optional[float]:
        """Current market value of position."""
        if self.current_price is not None:
            return self.size * self.current_price
        return None

    @property
    def unrealized_pnl(self) -> Optional[float]:
        """Unrealized profit/loss."""
        if self.current_value is not None and self.total_cost is not None:
            return self.current_value - self.total_cost
        return None

    @property
    def unrealized_pnl_pct(self) -> Optional[float]:
        """Unrealized P&L percentage."""
        if self.unrealized_pnl is not None and self.total_cost and self.total_cost > 0:
            return (self.unrealized_pnl / self.total_cost) * 100
        return None
```

**3. Authentication Models (`auth.py`)**

```python
from pydantic import BaseModel, Field
from typing import Optional

class ApiCredentials(BaseModel):
    """
    L2 API credentials (HMAC-based).

    Generated from L1 wallet signature.
    """
    api_key: str = Field(..., description="UUID identifying the credentials")
    api_secret: str = Field(..., description="Secret for HMAC generation")
    api_passphrase: str = Field(..., description="Passphrase for encryption")

    # Metadata
    address: str = Field(..., description="Polygon wallet address")
    created_at: Optional[int] = None  # Unix timestamp


class AccessStatus(BaseModel):
    """User's access status and restrictions."""
    address: str
    cert_required: bool = False  # Whether KYC cert is required
    closed_only_mode: bool = False  # If true, can only close positions
```

---

## Client Architecture

### Base Client (`clients/base_client.py`)

```python
import httpx
from typing import Optional, Dict, Any
from loguru import logger

class BaseClient:
    """
    Base HTTP client with common functionality.

    Provides request handling, error parsing, rate limiting.
    """
    def __init__(self, base_url: str, timeout: int = 30):
        self.base_url = base_url
        self.timeout = timeout
        self.session: Optional[httpx.AsyncClient] = None

    async def __aenter__(self):
        self.session = httpx.AsyncClient(
            base_url=self.base_url,
            timeout=httpx.Timeout(self.timeout),
            follow_redirects=True
        )
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.aclose()

    async def _request(
        self,
        method: str,
        path: str,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Execute HTTP request with error handling."""
        if not self.session:
            raise RuntimeError("Client not initialized. Use 'async with' context manager")

        url = f"{self.base_url}{path}"
        logger.debug(f"{method} {url}")

        try:
            response = await self.session.request(
                method=method,
                url=url,
                headers=headers,
                params=params,
                json=json
            )
            response.raise_for_status()
            return response.json()

        except httpx.HTTPStatusError as e:
            logger.error(f"HTTP {e.response.status_code}: {e.response.text}")
            self._handle_http_error(e)
            raise

        except httpx.RequestError as e:
            logger.error(f"Request failed: {e}")
            raise

    def _handle_http_error(self, error: httpx.HTTPStatusError):
        """Parse and format HTTP errors for LLM consumption."""
        status = error.response.status_code
        try:
            detail = error.response.json()
        except:
            detail = {"error": error.response.text}

        # Map common errors to user-friendly messages
        if status == 401:
            raise PermissionError("Authentication failed. Check your API credentials.")
        elif status == 403:
            raise PermissionError(f"Access denied: {detail.get('error', 'Unknown reason')}")
        elif status == 404:
            raise ValueError(f"Resource not found: {error.request.url}")
        elif status == 400:
            raise ValueError(f"Invalid request: {detail.get('error', 'Unknown error')}")
        elif status == 429:
            raise RuntimeError("Rate limit exceeded. Please wait before retrying.")
        else:
            raise RuntimeError(f"API error ({status}): {detail}")
```

### Gamma Client (`clients/gamma_client.py`)

```python
from typing import List, Optional, Dict, Any
from ..models.market import Market, Event, OrderBook
from .base_client import BaseClient

class GammaClient(BaseClient):
    """
    Gamma Markets API client (read-only market data).

    No authentication required. Provides market discovery,
    historical data, and metadata.
    """
    def __init__(self):
        super().__init__(base_url="https://gamma-api.polymarket.com")

    async def get_market(self, market_id: str) -> Market:
        """Get market by ID or slug."""
        data = await self._request("GET", f"/markets/{market_id}")
        return Market(**data)

    async def list_markets(
        self,
        limit: int = 100,
        offset: int = 0,
        closed: Optional[bool] = None,
        order: Optional[str] = "volume_24h",
        ascending: bool = False,
        **filters
    ) -> List[Market]:
        """
        List markets with filtering and pagination.

        Args:
            limit: Max results to return
            offset: Pagination offset
            closed: Filter by closed status
            order: Field to sort by
            ascending: Sort direction
            **filters: Additional filters (liquidity_min, volume_min, etc.)
        """
        params = {
            "limit": limit,
            "offset": offset,
            "ascending": ascending,
        }

        if closed is not None:
            params["closed"] = closed
        if order:
            params["order"] = order

        # Add dynamic filters
        params.update(filters)

        data = await self._request("GET", "/markets", params=params)
        return [Market(**market) for market in data]

    async def search_markets(
        self,
        query: str,
        limit: int = 20
    ) -> List[Market]:
        """
        Search markets, events, and profiles.

        Uses Polymarket's universal search endpoint.
        """
        params = {"query": query, "limit": limit}
        data = await self._request("GET", "/search", params=params)

        # Extract markets from search results
        markets = []
        for result in data.get("markets", []):
            markets.append(Market(**result))

        return markets[:limit]

    async def get_event(self, event_id: str) -> Event:
        """Get event details by ID or slug."""
        data = await self._request("GET", f"/events/{event_id}")
        return Event(**data)

    async def list_events(
        self,
        limit: int = 50,
        offset: int = 0,
        closed: Optional[bool] = None
    ) -> List[Event]:
        """List events with pagination."""
        params = {"limit": limit, "offset": offset}
        if closed is not None:
            params["closed"] = closed

        data = await self._request("GET", "/events", params=params)
        return [Event(**event) for event in data]

    async def get_orderbook(
        self,
        token_id: str
    ) -> OrderBook:
        """
        Get order book for a specific token.

        Args:
            token_id: CLOB token ID (YES or NO)
        """
        data = await self._request("GET", f"/book/{token_id}")
        return OrderBook(**data)

    async def get_price_history(
        self,
        token_id: str,
        start_ts: Optional[int] = None,
        end_ts: Optional[int] = None,
        interval: str = "1h"
    ) -> List[Dict[str, Any]]:
        """
        Get historical price data for charting.

        Args:
            token_id: CLOB token ID
            start_ts: Start timestamp (Unix)
            end_ts: End timestamp (Unix)
            interval: Candle interval (1m, 5m, 1h, 1d)

        Returns:
            List of OHLCV candles
        """
        params = {"interval": interval}
        if start_ts:
            params["start_ts"] = start_ts
        if end_ts:
            params["end_ts"] = end_ts

        return await self._request("GET", f"/prices/{token_id}", params=params)
```

### CLOB Client (`clients/clob_client.py`)

```python
import os
import time
import hmac
import hashlib
from typing import Optional, List
from loguru import logger

from ..models.auth import ApiCredentials, AccessStatus
from ..models.order import OrderParams, SignedOrder, Order, Fill, Position
from ..signing.auth_signer import sign_clob_auth
from ..signing.order_signer import sign_order
from .base_client import BaseClient

class ClobClient(BaseClient):
    """
    CLOB API client (authenticated trading operations).

    Requires wallet private key for L1 auth and API credentials for L2 auth.
    """
    def __init__(
        self,
        private_key: str,
        proxy_address: Optional[str] = None,
        signature_type: Optional[int] = None,
        api_creds: Optional[ApiCredentials] = None
    ):
        super().__init__(base_url="https://clob.polymarket.com")

        self.private_key = private_key
        self.proxy_address = proxy_address
        self.signature_type = signature_type or 0  # 0=EOA, 1=Magic, 2=Browser wallet
        self.api_creds = api_creds

        # Derive wallet address from private key
        from eth_account import Account
        self.address = Account.from_key(private_key).address

    @classmethod
    def from_env(cls) -> "ClobClient":
        """Initialize from environment variables."""
        private_key = os.getenv("POLYMARKET_PRIVATE_KEY")
        if not private_key:
            raise ValueError("POLYMARKET_PRIVATE_KEY environment variable required")

        proxy_address = os.getenv("POLYMARKET_PROXY_ADDRESS")
        signature_type_str = os.getenv("POLYMARKET_SIGNATURE_TYPE")
        signature_type = int(signature_type_str) if signature_type_str else None

        return cls(
            private_key=private_key,
            proxy_address=proxy_address,
            signature_type=signature_type
        )

    async def create_or_derive_api_credentials(self) -> ApiCredentials:
        """
        Create new or derive existing API credentials.

        Uses L1 authentication (wallet signature).
        """
        timestamp = int(time.time())
        nonce = 0

        # Sign auth message with EIP-712
        signature = sign_clob_auth(
            private_key=self.private_key,
            timestamp=timestamp,
            nonce=nonce
        )

        # Build L1 headers
        headers = {
            "POLY_ADDRESS": self.address,
            "POLY_SIGNATURE": signature,
            "POLY_TIMESTAMP": str(timestamp),
            "POLY_NONCE": str(nonce)
        }

        # Try to derive existing credentials first
        try:
            logger.info("Attempting to derive existing API credentials")
            data = await self._request("GET", "/auth/derive-api-key", headers=headers)
        except:
            # If derivation fails, create new credentials
            logger.info("Creating new API credentials")
            data = await self._request("POST", "/auth/api-key", headers=headers)

        self.api_creds = ApiCredentials(**data)
        logger.info(f"API credentials ready for {self.address}")
        return self.api_creds

    def _build_l2_headers(self, method: str, path: str, body: Optional[str] = None) -> Dict[str, str]:
        """
        Build L2 (HMAC) authentication headers.

        Required for all authenticated API calls.
        """
        if not self.api_creds:
            raise RuntimeError("API credentials not initialized. Call create_or_derive_api_credentials() first")

        timestamp = str(int(time.time()))

        # Build signature message
        message_parts = [timestamp, method, path]
        if body:
            message_parts.append(body)
        message = "".join(message_parts)

        # Generate HMAC signature
        signature = hmac.new(
            self.api_creds.api_secret.encode(),
            message.encode(),
            hashlib.sha256
        ).hexdigest()

        return {
            "POLY_ADDRESS": self.address,
            "POLY_SIGNATURE": signature,
            "POLY_TIMESTAMP": timestamp,
            "POLY_API_KEY": self.api_creds.api_key,
            "POLY_PASSPHRASE": self.api_creds.api_passphrase
        }

    async def get_access_status(self) -> AccessStatus:
        """Check access status and restrictions."""
        params = {"address": self.address}
        data = await self._request("GET", "/auth/access-status", params=params)
        return AccessStatus(**data)

    async def create_order(self, params: OrderParams) -> Order:
        """
        Create and submit a limit order.

        Args:
            params: Order parameters

        Returns:
            Created order with ID and status
        """
        # Sign order with EIP-712
        signed_order = sign_order(
            private_key=self.private_key,
            params=params,
            signature_type=self.signature_type
        )

        # Build request body
        body = signed_order.dict()
        path = "/order"

        # Generate L2 auth headers
        headers = self._build_l2_headers("POST", path, body=str(body))

        # Submit order
        logger.info(f"Submitting order: {params.side} {params.size} @ ${params.price}")
        data = await self._request("POST", path, headers=headers, json=body)

        return Order(**data)

    async def cancel_order(self, order_id: str) -> Dict[str, Any]:
        """Cancel a pending order."""
        path = f"/order/{order_id}"
        headers = self._build_l2_headers("DELETE", path)

        logger.info(f"Cancelling order {order_id}")
        return await self._request("DELETE", path, headers=headers)

    async def cancel_orders(self, order_ids: List[str]) -> Dict[str, Any]:
        """Cancel multiple orders atomically."""
        path = "/orders"
        body = {"order_ids": order_ids}
        headers = self._build_l2_headers("DELETE", path, body=str(body))

        logger.info(f"Cancelling {len(order_ids)} orders")
        return await self._request("DELETE", path, headers=headers, json=body)

    async def get_order(self, order_id: str) -> Order:
        """Get order status and details."""
        path = f"/order/{order_id}"
        headers = self._build_l2_headers("GET", path)

        data = await self._request("GET", path, headers=headers)
        return Order(**data)

    async def get_orders(
        self,
        market_id: Optional[str] = None,
        asset_id: Optional[str] = None
    ) -> List[Order]:
        """
        Get user's orders.

        Can filter by market or specific token.
        """
        path = "/orders"
        headers = self._build_l2_headers("GET", path)

        params = {}
        if market_id:
            params["market"] = market_id
        if asset_id:
            params["asset_id"] = asset_id

        data = await self._request("GET", path, headers=headers, params=params)
        return [Order(**order) for order in data]

    async def get_fills(
        self,
        market_id: Optional[str] = None,
        asset_id: Optional[str] = None
    ) -> List[Fill]:
        """Get trade execution history."""
        path = "/fills"
        headers = self._build_l2_headers("GET", path)

        params = {}
        if market_id:
            params["market"] = market_id
        if asset_id:
            params["asset_id"] = asset_id

        data = await self._request("GET", path, headers=headers, params=params)
        return [Fill(**fill) for fill in data]

    async def get_positions(
        self,
        market_id: Optional[str] = None
    ) -> List[Position]:
        """Get current positions."""
        path = "/positions"
        headers = self._build_l2_headers("GET", path)

        params = {}
        if market_id:
            params["market"] = market_id

        data = await self._request("GET", path, headers=headers, params=params)
        return [Position(**pos) for pos in data]
```

---

## Authentication System

### EIP-712 Signing (`signing/eip712.py`)

```python
from eth_account import Account
from eth_account.messages import encode_structured_data
from typing import Dict, Any

def build_eip712_domain(chain_id: int = 137) -> Dict[str, Any]:
    """
    Build EIP-712 domain for Polymarket.

    Args:
        chain_id: Blockchain network (137 = Polygon mainnet)
    """
    return {
        "name": "ClobAuthDomain",
        "version": "1",
        "chainId": chain_id
    }

def sign_typed_data(
    private_key: str,
    domain: Dict[str, Any],
    types: Dict[str, Any],
    message: Dict[str, Any]
) -> str:
    """
    Sign EIP-712 structured data.

    Returns 0x-prefixed hex signature.
    """
    structured_data = encode_structured_data(
        domain_data=domain,
        message_types=types,
        message_data=message
    )

    account = Account.from_key(private_key)
    signed_message = account.sign_message(structured_data)

    return signed_message.signature.hex()
```

### Auth Signer (`signing/auth_signer.py`)

```python
from .eip712 import build_eip712_domain, sign_typed_data
from eth_account import Account

def sign_clob_auth(
    private_key: str,
    timestamp: int,
    nonce: int = 0,
    chain_id: int = 137
) -> str:
    """
    Sign CLOB authentication message.

    Used for L1 authentication (creating/deriving API keys).

    Args:
        private_key: Polygon wallet private key
        timestamp: Current Unix timestamp
        nonce: Nonce value (default 0)
        chain_id: Polygon chain ID (137 for mainnet)

    Returns:
        0x-prefixed hex signature
    """
    domain = build_eip712_domain(chain_id)

    types = {
        "ClobAuth": [
            {"name": "address", "type": "address"},
            {"name": "timestamp", "type": "string"},
            {"name": "nonce", "type": "uint256"},
            {"name": "message", "type": "string"},
        ]
    }

    address = Account.from_key(private_key).address

    message = {
        "address": address,
        "timestamp": str(timestamp),
        "nonce": nonce,
        "message": "This message attests that I control the given wallet",
    }

    return sign_typed_data(private_key, domain, types, message)
```

### Order Signer (`signing/order_signer.py`)

```python
import time
from eth_account import Account
from ..models.order import OrderParams, SignedOrder
from .eip712 import build_eip712_domain, sign_typed_data

def sign_order(
    private_key: str,
    params: OrderParams,
    signature_type: int = 0,
    chain_id: int = 137
) -> SignedOrder:
    """
    Sign an order with EIP-712.

    Args:
        private_key: Polygon wallet private key
        params: Order parameters
        signature_type: 0=EOA, 1=Magic, 2=Browser wallet
        chain_id: Polygon chain ID

    Returns:
        Signed order ready for submission
    """
    domain = build_eip712_domain(chain_id)

    # Order signing types (simplified - full spec is more complex)
    types = {
        "Order": [
            {"name": "salt", "type": "uint256"},
            {"name": "maker", "type": "address"},
            {"name": "signer", "type": "address"},
            {"name": "taker", "type": "address"},
            {"name": "tokenId", "type": "uint256"},
            {"name": "makerAmount", "type": "uint256"},
            {"name": "takerAmount", "type": "uint256"},
            {"name": "expiration", "type": "uint256"},
            {"name": "nonce", "type": "uint256"},
            {"name": "feeRateBps", "type": "uint256"},
            {"name": "side", "type": "uint8"},
            {"name": "signatureType", "type": "uint8"},
        ]
    }

    account = Account.from_key(private_key)
    address = account.address

    # Build order message
    # (Simplified - actual implementation needs proper amount calculation)
    message = {
        "salt": params.nonce or int(time.time()),
        "maker": address,
        "signer": address,
        "taker": "0x0000000000000000000000000000000000000000",  # Any taker
        "tokenId": int(params.token_id),
        "makerAmount": int(params.size * 10**6),  # USDC has 6 decimals
        "takerAmount": int(params.size * params.price * 10**6),
        "expiration": params.expiration or 0,  # 0 = no expiration
        "nonce": params.nonce or 0,
        "feeRateBps": params.fee_rate_bps or 0,
        "side": 0 if params.side == "BUY" else 1,
        "signatureType": signature_type
    }

    signature = sign_typed_data(private_key, domain, types, message)

    return SignedOrder(
        params=params,
        signature=signature,
        signer=address,
        timestamp=int(time.time())
    )
```

---

**Due to length constraints, I'll continue with the Implementation Sequence, Testing Strategy, and remaining sections in the next part.**

Would you like me to continue with the rest of the implementation plan? I can create:
1. Implementation Sequence (detailed step-by-step)
2. Testing Strategy (unit/integration/E2E)
3. Deployment Guide
4. Comparison table with Kalshi implementation
5. Dependencies and configuration examples
