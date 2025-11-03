"""Pydantic models for Kalshi API requests and responses."""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class ExchangeStatus(BaseModel):
    """Exchange operational status."""

    exchange_active: bool
    trading_active: bool


class Balance(BaseModel):
    """Account balance information."""

    balance: int = Field(..., description="Balance in cents")

    @property
    def balance_dollars(self) -> float:
        """Balance in dollars."""
        return self.balance / 100


class Market(BaseModel):
    """Prediction market details."""

    ticker: str
    event_ticker: str
    title: str
    subtitle: Optional[str] = None
    yes_bid: Optional[int] = Field(None, ge=0, le=100)
    yes_ask: Optional[int] = Field(None, ge=0, le=100)
    no_bid: Optional[int] = Field(None, ge=0, le=100)
    no_ask: Optional[int] = Field(None, ge=0, le=100)
    last_price: Optional[int] = None
    volume: Optional[int] = None
    volume_24h: Optional[int] = None
    open_interest: Optional[int] = None
    status: str
    close_time: datetime
    expiration_time: Optional[datetime] = None
    result: Optional[str] = None

    @property
    def interpretation(self) -> str:
        """Human-readable market summary."""
        if self.yes_ask:
            return f"Market implies {self.yes_ask}% chance: {self.title}"
        elif self.last_price:
            return f"Last traded at {self.last_price}% probability: {self.title}"
        return f"Market: {self.title}"

    @property
    def spread(self) -> Optional[int]:
        """Bid-ask spread in cents."""
        if self.yes_bid and self.yes_ask:
            return self.yes_ask - self.yes_bid
        return None


class Event(BaseModel):
    """Prediction market event."""

    event_ticker: str
    title: str
    category: str
    series_ticker: Optional[str] = None
    sub_title: Optional[str] = None
    mutually_exclusive: bool
    strike_date: Optional[datetime] = None


class Order(BaseModel):
    """Order details."""

    order_id: str
    user_id: Optional[str] = None
    client_order_id: Optional[str] = None
    ticker: str
    side: str  # "yes" or "no"
    action: str  # "buy" or "sell"
    type: str  # "market" or "limit"
    status: str  # "resting", "filled", "canceled", etc.
    yes_price: Optional[int] = None
    no_price: Optional[int] = None
    fill_count: int = 0
    remaining_count: int = 0
    initial_count: int
    taker_fees: Optional[int] = None
    maker_fees: Optional[int] = None
    taker_fill_cost: Optional[int] = None
    maker_fill_cost: Optional[int] = None
    queue_position: Optional[int] = None
    expiration_time: Optional[datetime] = None
    created_time: datetime
    last_update_time: Optional[datetime] = None

    @property
    def is_filled(self) -> bool:
        """Check if order is fully filled."""
        return self.status == "filled"

    @property
    def is_active(self) -> bool:
        """Check if order is still active/resting."""
        return self.status == "resting"

    @property
    def average_fill_price(self) -> Optional[int]:
        """Average fill price in cents."""
        if self.fill_count > 0:
            total_cost = (self.taker_fill_cost or 0) + (self.maker_fill_cost or 0)
            return total_cost // self.fill_count
        return None


class Position(BaseModel):
    """Portfolio position details."""

    ticker: str
    market_ticker: Optional[str] = None
    event_ticker: Optional[str] = None
    position: int = Field(..., description="Number of contracts (positive=YES, negative=NO)")
    market_exposure: Optional[int] = Field(None, description="Current value in cents")
    total_cost: Optional[int] = Field(None, description="Total cost paid in cents")
    realized_pnl: Optional[int] = Field(None, description="Realized profit/loss in cents")
    unrealized_pnl: Optional[int] = Field(None, description="Unrealized profit/loss in cents")

    @property
    def pnl_dollars(self) -> float:
        """Total P&L in dollars (realized + unrealized)."""
        realized = self.realized_pnl or 0
        unrealized = self.unrealized_pnl or 0
        return (realized + unrealized) / 100

    @property
    def is_long(self) -> bool:
        """Check if position is long (positive contracts)."""
        return self.position > 0

    @property
    def side_name(self) -> str:
        """Human-readable position side."""
        return "YES" if self.position > 0 else "NO" if self.position < 0 else "FLAT"


class Fill(BaseModel):
    """Trade fill details."""

    fill_id: str
    order_id: str
    ticker: str
    side: str  # "yes" or "no"
    action: str  # "buy" or "sell"
    count: int = Field(..., description="Number of contracts filled")
    price: float = Field(..., description="Fill price in dollars", ge=0.0, le=1.0)
    created_time: datetime
    trade_id: Optional[str] = None
    is_taker: bool = False
    fees: Optional[int] = Field(None, description="Trading fees in cents")

    @property
    def cost_cents(self) -> int:
        """Total cost in cents (price × count × 100)."""
        return int(self.price * 100 * self.count)

    @property
    def cost_dollars(self) -> float:
        """Total cost in dollars."""
        return self.price * self.count

    @property
    def fees_dollars(self) -> float:
        """Fees in dollars."""
        return (self.fees or 0) / 100


class OrderBookLevel(BaseModel):
    """Single level in the order book."""

    price: int = Field(..., description="Price in cents", ge=0, le=100)
    quantity: int = Field(..., description="Number of contracts at this price")


class OrderBook(BaseModel):
    """Order book depth (bids and asks)."""

    ticker: str
    yes_bids: list[OrderBookLevel] = Field(default_factory=list, description="YES buy orders")
    yes_asks: list[OrderBookLevel] = Field(default_factory=list, description="YES sell orders")
    no_bids: list[OrderBookLevel] = Field(default_factory=list, description="NO buy orders")
    no_asks: list[OrderBookLevel] = Field(default_factory=list, description="NO sell orders")

    @property
    def yes_spread(self) -> Optional[int]:
        """Spread on YES side in cents."""
        if self.yes_bids and self.yes_asks:
            return self.yes_asks[0].price - self.yes_bids[0].price
        return None

    @property
    def yes_depth(self) -> int:
        """Total YES liquidity (both sides)."""
        bid_depth = sum(level.quantity for level in self.yes_bids)
        ask_depth = sum(level.quantity for level in self.yes_asks)
        return bid_depth + ask_depth


class Trade(BaseModel):
    """Public trade details."""

    trade_id: str
    ticker: str
    price: float = Field(..., description="Trade price in dollars")
    count: int = Field(..., description="Number of contracts traded")
    yes_price: Optional[float] = Field(None, description="YES side price in dollars")
    no_price: Optional[float] = Field(None, description="NO side price in dollars")
    yes_price_dollars: Optional[str] = None
    no_price_dollars: Optional[str] = None
    taker_side: Optional[str] = Field(None, description="Which side was the taker (yes/no)")
    created_time: datetime

    @property
    def price_cents(self) -> int:
        """Trade price in cents."""
        return int(self.price * 100)

    @property
    def volume_dollars(self) -> float:
        """Trade volume in dollars."""
        return self.price * self.count

    @property
    def side(self) -> str:
        """Derive trade side from yes/no prices."""
        if self.yes_price and not self.no_price:
            return "yes"
        elif self.no_price and not self.yes_price:
            return "no"
        elif self.taker_side:
            return self.taker_side
        else:
            return "unknown"


class BatchOrderRequest(BaseModel):
    """Single order specification in a batch request."""

    ticker: str
    client_order_id: Optional[str] = None
    type: str = Field(..., description="Order type: 'market' or 'limit'")
    action: str = Field(..., description="Order action: 'buy' or 'sell'")
    side: str = Field(..., description="Order side: 'yes' or 'no'")
    count: int = Field(..., ge=1, description="Number of contracts")
    yes_price: Optional[int] = Field(None, ge=1, le=99, description="YES limit price in cents")
    no_price: Optional[int] = Field(None, ge=1, le=99, description="NO limit price in cents")
    expiration_ts: Optional[int] = Field(None, description="Expiration timestamp (Unix seconds)")
    sell_position_floor: Optional[int] = None
    buy_max_cost: Optional[int] = None


class BatchOrderResponse(BaseModel):
    """Response for a single order in a batch operation."""

    client_order_id: Optional[str] = None
    order: Optional[Order] = None
    error: Optional[dict] = Field(None, description="Error details if order failed")

    @property
    def is_success(self) -> bool:
        """Check if order was successfully created."""
        return self.order is not None and self.error is None

    @property
    def error_message(self) -> Optional[str]:
        """Extract error message if present."""
        if self.error:
            return self.error.get("message", "Unknown error")
        return None


class OrderGroup(BaseModel):
    """
    Order group (minimal info - API doesn't return much).

    Note: The Kalshi API has a design limitation where you SET contracts_limit
    when creating a group, but it's NEVER returned in any query. This makes it
    impossible to track progress toward the limit or query the current limit value.
    """

    # Fields that actually exist in API responses
    id: Optional[str] = None  # Present in list response
    order_group_id: Optional[str] = None  # Present in create response
    is_auto_cancel_enabled: bool = False  # Present in GET and list responses
    orders: Optional[list[str]] = None  # Only present in GET single response

    # NOTE: These fields are NOT available from the API:
    # - contracts_limit: Set at creation but never returned
    # - contracts_filled: Not tracked in responses
    # - status: No status field exists
    # - created_time: Not in responses
    # - reset_time: Not in responses

    @property
    def group_id(self) -> str:
        """Get the group ID (handles both field names)."""
        return self.order_group_id or self.id or ""
