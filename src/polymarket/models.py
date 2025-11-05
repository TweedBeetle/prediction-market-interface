"""
Pydantic models for Polymarket API data structures.

These models provide type-safe data validation and serialization for:
- Market data (from Gamma API)
- Orders and trades (from CLOB API)
- Positions and portfolio data
- Authentication credentials
"""

from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field, field_validator


class OrderSide(str, Enum):
    """Order side (buy or sell)."""

    BUY = "BUY"
    SELL = "SELL"


class OrderType(str, Enum):
    """Order type for execution."""

    FOK = "FOK"  # Fill-or-Kill (immediate or cancel entirely)
    GTC = "GTC"  # Good-til-Canceled
    GTD = "GTD"  # Good-til-Date


class SignatureType(str, Enum):
    """Signature type for authentication."""

    EOA = "EOA"  # Externally Owned Account (MetaMask, etc.)
    POLY_PROXY = "POLY_PROXY"  # Polymarket proxy wallet
    POLY_GNOSIS_SAFE = "POLY_GNOSIS_SAFE"  # Gnosis Safe multisig


class Market(BaseModel):
    """
    Polymarket market data from Gamma API.

    Represents a binary outcome market with pricing, volume, and metadata.
    """

    id: str = Field(..., description="Unique market ID")
    condition_id: str = Field(..., description="Condition ID for on-chain settlement")
    question: str = Field(..., description="Market question")
    description: Optional[str] = Field(None, description="Detailed market description")

    # Token IDs for trading (YES/NO outcomes)
    clob_token_ids: List[str] = Field(..., description="CLOB token IDs [YES, NO]")

    # Pricing
    best_bid: Optional[float] = Field(None, description="Best bid price (0-1)")
    best_ask: Optional[float] = Field(None, description="Best ask price (0-1)")
    last_price: Optional[float] = Field(None, description="Last trade price (0-1)")

    # Volume and liquidity
    volume: Optional[float] = Field(None, description="Total volume in USD")
    volume_24h: Optional[float] = Field(None, description="24h volume in USD")
    liquidity: Optional[float] = Field(None, description="Total liquidity in USD")

    # Metadata
    active: bool = Field(..., description="Whether market is active")
    closed: bool = Field(..., description="Whether market is closed")
    archived: bool = Field(False, description="Whether market is archived")

    end_date_iso: Optional[str] = Field(None, description="Market end date (ISO format)")
    game_start_time: Optional[str] = Field(None, description="Game start time for sports markets")

    # Tags and categorization
    tags: List[str] = Field(default_factory=list, description="Market tags")

    @property
    def yes_token_id(self) -> str:
        """Get YES outcome token ID."""
        return self.clob_token_ids[0] if self.clob_token_ids else ""

    @property
    def no_token_id(self) -> str:
        """Get NO outcome token ID."""
        return self.clob_token_ids[1] if len(self.clob_token_ids) > 1 else ""

    @property
    def spread(self) -> Optional[float]:
        """Calculate bid-ask spread."""
        if self.best_bid is not None and self.best_ask is not None:
            return self.best_ask - self.best_bid
        return None

    @property
    def midpoint_price(self) -> Optional[float]:
        """Calculate midpoint price between bid and ask."""
        if self.best_bid is not None and self.best_ask is not None:
            return (self.best_bid + self.best_ask) / 2
        return None

    @property
    def interpretation(self) -> str:
        """Human-readable market summary for LLMs."""
        price = self.midpoint_price or self.last_price
        if price is not None:
            prob_pct = int(price * 100)
            return f"Market implies {prob_pct}% probability: {self.question}"
        return f"Market: {self.question}"


class OrderParams(BaseModel):
    """
    Parameters for creating an order on Polymarket CLOB.

    Used to construct EIP-712 signed orders.
    """

    token_id: str = Field(..., description="Token ID to trade (YES or NO)")
    price: float = Field(..., ge=0.001, le=0.999, description="Price between 0.001-0.999")
    size: float = Field(..., gt=0, description="Order size in outcome tokens")
    side: OrderSide = Field(..., description="BUY or SELL")

    # Optional parameters
    fee_rate_bps: int = Field(0, description="Fee rate in basis points")
    nonce: Optional[int] = Field(None, description="Nonce for order uniqueness")
    expiration: Optional[int] = Field(None, description="Unix timestamp for order expiration")
    taker: Optional[str] = Field(None, description="Specific taker address (private order)")

    # Polymarket-specific
    maker: str = Field(..., description="Maker address (your wallet)")
    signature_type: SignatureType = Field(SignatureType.EOA, description="Signature type")

    @field_validator("price")
    @classmethod
    def validate_price(cls, v: float) -> float:
        """Ensure price is in valid range with reasonable precision."""
        if not 0.001 <= v <= 0.999:
            raise ValueError("Price must be between 0.001 and 0.999")
        # Round to 3 decimal places to avoid floating point issues
        return round(v, 3)

    @property
    def price_dollars(self) -> float:
        """Get price in dollars (for display)."""
        return self.price

    @property
    def total_cost(self) -> float:
        """Calculate total cost for this order."""
        return self.price * self.size


class Order(BaseModel):
    """
    Polymarket order data from CLOB API.

    Represents an active, filled, or canceled order.
    """

    order_id: str = Field(..., description="Unique order ID")
    market_id: str = Field(..., description="Market ID this order is for")
    token_id: str = Field(..., description="Token ID (YES or NO)")

    # Order details
    price: float = Field(..., description="Order price (0-1)")
    size: float = Field(..., description="Order size in outcome tokens")
    side: OrderSide = Field(..., description="BUY or SELL")
    order_type: Optional[OrderType] = Field(None, description="Order type (FOK/GTC/GTD)")

    # Fill status
    size_matched: float = Field(0, description="Size that has been filled")
    outcome: Optional[str] = Field(None, description="Outcome (YES or NO)")

    # Timestamps
    created_at: Optional[str] = Field(None, description="Order creation timestamp")
    last_update: Optional[str] = Field(None, description="Last update timestamp")
    expiration: Optional[int] = Field(None, description="Expiration timestamp")

    # User info
    owner: str = Field(..., description="Order owner address")
    maker_address: Optional[str] = Field(None, description="Maker address")

    # Status
    status: Optional[str] = Field(None, description="Order status (LIVE/MATCHED/CANCELLED)")

    @property
    def is_filled(self) -> bool:
        """Check if order is fully filled."""
        return self.size_matched >= self.size

    @property
    def remaining_size(self) -> float:
        """Calculate remaining unfilled size."""
        return max(0, self.size - self.size_matched)

    @property
    def fill_percentage(self) -> float:
        """Calculate fill percentage (0-100)."""
        if self.size == 0:
            return 0
        return (self.size_matched / self.size) * 100

    @property
    def total_cost(self) -> float:
        """Calculate total cost of filled portion."""
        return self.price * self.size_matched


class OrderBookLevel(BaseModel):
    """Single price level in an order book."""

    price: float = Field(..., description="Price at this level")
    size: float = Field(..., description="Total size at this price")

    @property
    def price_dollars(self) -> float:
        """Price in dollars (for display)."""
        return self.price


class OrderBook(BaseModel):
    """
    Order book for a Polymarket market.

    Contains bids and asks for both YES and NO outcomes.
    """

    market_id: str = Field(..., description="Market ID")
    token_id: str = Field(..., description="Token ID (YES or NO)")

    # Bid/ask levels
    bids: List[OrderBookLevel] = Field(default_factory=list, description="Bid levels (buy orders)")
    asks: List[OrderBookLevel] = Field(default_factory=list, description="Ask levels (sell orders)")

    # Aggregate stats
    timestamp: Optional[str] = Field(None, description="Orderbook snapshot timestamp")

    @property
    def best_bid(self) -> Optional[OrderBookLevel]:
        """Get best (highest) bid."""
        return self.bids[0] if self.bids else None

    @property
    def best_ask(self) -> Optional[OrderBookLevel]:
        """Get best (lowest) ask."""
        return self.asks[0] if self.asks else None

    @property
    def spread(self) -> Optional[float]:
        """Calculate bid-ask spread."""
        if self.best_bid and self.best_ask:
            return self.best_ask.price - self.best_bid.price
        return None

    @property
    def midpoint_price(self) -> Optional[float]:
        """Calculate midpoint price."""
        if self.best_bid and self.best_ask:
            return (self.best_bid.price + self.best_ask.price) / 2
        return None

    @property
    def total_bid_liquidity(self) -> float:
        """Calculate total liquidity on bid side."""
        return sum(level.price * level.size for level in self.bids)

    @property
    def total_ask_liquidity(self) -> float:
        """Calculate total liquidity on ask side."""
        return sum(level.price * level.size for level in self.asks)


class Position(BaseModel):
    """
    User position in a Polymarket market.

    Represents current holdings and P&L.
    """

    market_id: str = Field(..., description="Market ID")
    token_id: str = Field(..., description="Token ID (YES or NO)")

    # Position details
    size: float = Field(..., description="Position size (positive = long, negative = short)")
    outcome: str = Field(..., description="Outcome (YES or NO)")

    # Cost basis
    average_price: Optional[float] = Field(None, description="Average entry price")
    total_cost: Optional[float] = Field(None, description="Total cost basis in USD")

    # Current value
    current_price: Optional[float] = Field(None, description="Current market price")
    market_value: Optional[float] = Field(None, description="Current market value in USD")

    # P&L
    unrealized_pnl: Optional[float] = Field(None, description="Unrealized P&L in USD")

    @property
    def pnl_percentage(self) -> Optional[float]:
        """Calculate P&L as percentage of cost basis."""
        if self.total_cost and self.total_cost > 0 and self.unrealized_pnl is not None:
            return (self.unrealized_pnl / self.total_cost) * 100
        return None

    @property
    def is_profitable(self) -> bool:
        """Check if position is currently profitable."""
        return self.unrealized_pnl is not None and self.unrealized_pnl > 0


class Trade(BaseModel):
    """
    Trade execution data from Polymarket.

    Represents a completed trade.
    """

    trade_id: str = Field(..., description="Unique trade ID")
    market_id: str = Field(..., description="Market ID")
    token_id: str = Field(..., description="Token ID traded")

    # Trade details
    price: float = Field(..., description="Execution price")
    size: float = Field(..., description="Trade size")
    side: OrderSide = Field(..., description="BUY or SELL")
    outcome: str = Field(..., description="Outcome traded (YES or NO)")

    # Timestamp
    timestamp: Optional[str] = Field(None, description="Trade timestamp")

    # User info (if available)
    maker_address: Optional[str] = Field(None, description="Maker address")
    taker_address: Optional[str] = Field(None, description="Taker address")

    @property
    def total_value(self) -> float:
        """Calculate total value of trade."""
        return self.price * self.size


class Event(BaseModel):
    """
    Polymarket event (collection of related markets).

    Example: "2024 Presidential Election" contains multiple outcome markets.
    """

    id: str = Field(..., description="Event ID")
    slug: str = Field(..., description="URL-friendly slug")
    title: str = Field(..., description="Event title")
    description: Optional[str] = Field(None, description="Event description")

    # Markets in this event
    markets: List[Market] = Field(default_factory=list, description="Markets in this event")

    # Metadata
    active: bool = Field(True, description="Whether event is active")
    closed: bool = Field(False, description="Whether event is closed")

    end_date_iso: Optional[str] = Field(None, description="Event end date")

    @property
    def total_volume(self) -> float:
        """Calculate total volume across all markets."""
        return sum(m.volume or 0 for m in self.markets)

    @property
    def market_count(self) -> int:
        """Count of markets in this event."""
        return len(self.markets)


class ApiCredentials(BaseModel):
    """
    Polymarket API credentials.

    Contains wallet information and API keys for authentication.
    """

    # L1 Authentication (wallet)
    private_key: str = Field(..., description="Private key for EIP-712 signing")
    wallet_address: str = Field(..., description="Wallet address (derived from private key)")

    # L2 Authentication (optional API key for CLOB)
    api_key: Optional[str] = Field(None, description="CLOB API key")
    api_secret: Optional[str] = Field(None, description="CLOB API secret")
    api_passphrase: Optional[str] = Field(None, description="CLOB API passphrase")

    # Chain configuration
    chain_id: int = Field(137, description="Polygon chain ID (137 = mainnet)")

    class Config:
        """Pydantic config."""
        # Don't expose private key in repr/str
        json_schema_extra = {
            "example": {
                "private_key": "0x...",
                "wallet_address": "0x...",
                "chain_id": 137
            }
        }
