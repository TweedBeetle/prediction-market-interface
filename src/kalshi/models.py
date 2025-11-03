"""Pydantic models for Kalshi API data structures."""

from datetime import datetime
from typing import Optional, List, Union
from enum import Enum

from pydantic import BaseModel, Field, field_validator, ConfigDict


class MarketStatus(str, Enum):
    """Market trading status."""
    UNOPENED = "unopened"
    OPEN = "open"
    ACTIVE = "active"  # Real API sometimes returns this
    CLOSED = "closed"
    SETTLED = "settled"


class OrderSide(str, Enum):
    """Order side: buy or sell."""
    BUY = "buy"
    SELL = "sell"


class OrderType(str, Enum):
    """Order type: limit or market."""
    LIMIT = "limit"
    MARKET = "market"


class OrderStatus(str, Enum):
    """Order status."""
    RESTING = "resting"
    CANCELED = "canceled"
    EXECUTED = "executed"


class EventStatus(str, Enum):
    """Event status."""
    OPEN = "open"
    CLOSED = "closed"
    SETTLED = "settled"


class Market(BaseModel):
    """Kalshi market data - matches actual API response format."""

    # Core identifiers
    ticker: str = Field(..., description="Unique market identifier (e.g., KXHARRIS24-LSV)")
    title: str = Field(..., description="Market display name")
    subtitle: Optional[str] = Field(None, description="Secondary title")
    status: MarketStatus = Field(..., description="Market trading status (unopened/open/closed/settled)")

    # Event/Series relationships (optional - API may provide different fields)
    event_ticker: Optional[str] = Field(None, description="Parent event identifier")
    mve_collection_ticker: Optional[str] = Field(None, description="Multivariate collection identifier")

    # Category and type information
    category: Optional[str] = Field(None, description="Market category")
    market_type: Optional[str] = Field(None, description="Market type (e.g., 'binary')")
    strike_type: Optional[str] = Field(None, description="Strike type for custom strike markets")

    # Pricing - YES side (in cents, 0-100 range)
    yes_bid: Optional[float] = Field(None, description="Current yes side best bid (cents)")
    yes_ask: Optional[float] = Field(None, description="Current yes side best ask (cents)")
    yes_bid_dollars: Optional[str] = Field(None, description="yes_bid formatted in dollars")
    yes_ask_dollars: Optional[str] = Field(None, description="yes_ask formatted in dollars")

    # Pricing - NO side (in cents, 0-100 range)
    no_bid: Optional[float] = Field(None, description="Current no side best bid (cents)")
    no_ask: Optional[float] = Field(None, description="Current no side best ask (cents)")
    no_bid_dollars: Optional[str] = Field(None, description="no_bid formatted in dollars")
    no_ask_dollars: Optional[str] = Field(None, description="no_ask formatted in dollars")

    # Recent prices
    last_price: Optional[float] = Field(None, description="Most recent trade price (cents)")
    last_price_dollars: Optional[str] = Field(None, description="last_price formatted in dollars")
    previous_price: Optional[float] = Field(None, description="Previous trade price")
    previous_price_dollars: Optional[str] = Field(None, description="previous_price formatted in dollars")

    # Volume & Liquidity
    volume: Optional[int] = Field(None, description="Total contracts traded (all time)")
    volume_24h: Optional[int] = Field(None, description="Total contracts traded in 24h")
    open_interest: Optional[int] = Field(None, description="Open position count")
    liquidity: Optional[int] = Field(None, description="Current market liquidity")
    liquidity_dollars: Optional[str] = Field(None, description="Liquidity formatted in dollars")

    # Timestamps (actual API field names)
    open_time: Optional[str] = Field(None, description="ISO timestamp of market open")
    close_time: Optional[str] = Field(None, description="ISO timestamp of market close")
    expiration_time: Optional[str] = Field(None, description="ISO timestamp of expiration")
    expected_expiration_time: Optional[str] = Field(None, description="Expected expiration time")
    latest_expiration_time: Optional[str] = Field(None, description="Latest expiration time")
    settlement_timer_seconds: Optional[int] = Field(None, description="Seconds until settlement")

    # Settlement info
    result: Optional[str] = Field(None, description="Settlement result (yes/no)")
    expiration_value: Optional[str] = Field(None, description="Settlement value")

    # Additional metadata
    can_close_early: Optional[bool] = Field(None, description="Whether market can close early")
    notional_value: Optional[int] = Field(None, description="Notional value")
    notional_value_dollars: Optional[str] = Field(None, description="Notional value in dollars")
    rules_primary: Optional[str] = Field(None, description="Primary rules")
    rules_secondary: Optional[str] = Field(None, description="Secondary rules")


class Orderbook(BaseModel):
    """Order book for a market."""

    ticker: str = Field(..., description="Market ticker")
    bids: List[tuple[float, int]] = Field(default_factory=list, description="List of (price, size) bids")
    asks: List[tuple[float, int]] = Field(default_factory=list, description="List of (price, size) asks")
    timestamp: int = Field(..., description="Orderbook timestamp (Unix ms)")


class Trade(BaseModel):
    """Executed trade."""

    model_config = ConfigDict(populate_by_name=True)

    market_ticker: str = Field(..., alias="ticker", description="Market ticker")
    price: float = Field(..., description="Execution price (cents)")
    size: int = Field(..., alias="count", description="Number of contracts traded")
    timestamp: int = Field(..., alias="created_at", description="Trade timestamp (Unix ms)")


class Order(BaseModel):
    """User order."""

    id: str = Field(..., description="Unique order identifier")
    ticker: str = Field(..., description="Market ticker")
    status: OrderStatus = Field(..., description="Order status")
    side: OrderSide = Field(..., description="Buy or sell")
    type: OrderType = Field(..., description="Limit or market")
    price: int = Field(..., description="Limit price in cents (1-99)")
    count: int = Field(..., description="Total contracts")
    fill_count: int = Field(..., description="Filled contracts")
    remaining_count: int = Field(..., description="Unfilled contracts")
    created_at: str = Field(..., description="ISO timestamp")
    last_updated_at: str = Field(..., description="ISO timestamp")


class CreateOrderRequest(BaseModel):
    """Request to create an order."""

    ticker: str = Field(..., description="Market identifier")
    side: OrderSide = Field(..., description="Buy or sell")
    type: OrderType = Field(default=OrderType.LIMIT, description="Limit or market")
    price: Optional[int] = Field(None, description="Limit price in cents (1-99, required for limit orders)")
    count: int = Field(..., description="Number of contracts")
    expire_at: Optional[int] = Field(None, description="Unix timestamp for order expiration")
    order_group_id: Optional[str] = Field(None, description="Optional order group for risk management")


class Position(BaseModel):
    """User position in a market."""

    ticker: str = Field(..., description="Market ticker")
    event_ticker: str = Field(..., description="Event identifier")
    side: str = Field(..., description="long or short")
    position: int = Field(..., description="Net contracts held")
    fill_price: int = Field(..., description="Average fill price (cents)")
    total_traded: int = Field(..., description="Lifetime contracts traded")
    resting_order_count: int = Field(..., description="Active orders count")


class Fill(BaseModel):
    """Executed fill/trade."""

    market_ticker: str = Field(..., description="Market ticker")
    order_id: str = Field(..., description="Order identifier")
    is_buy: bool = Field(..., description="True if buy order, False if sell")
    quantity: int = Field(..., description="Contracts filled")
    price: float = Field(..., description="Execution price (cents)")
    timestamp: int = Field(..., description="Unix timestamp (seconds)")


class Balance(BaseModel):
    """Account balance and portfolio value."""

    balance: int = Field(..., description="Account balance in cents")
    portfolio_value: int = Field(..., description="Total portfolio value in cents (unrealized + cash)")


class Candlestick(BaseModel):
    """OHLCV candlestick data."""

    start_ts: int = Field(..., description="Period start (Unix seconds)")
    end_ts: int = Field(..., description="Period end (Unix seconds)")
    open: float = Field(..., description="Opening price (cents)")
    high: float = Field(..., description="High price (cents)")
    low: float = Field(..., description="Low price (cents)")
    close: float = Field(..., description="Closing price (cents)")
    volume: int = Field(..., description="Contracts traded")


class Event(BaseModel):
    """Kalshi event - matches actual API response format."""

    event_ticker: str = Field(..., description="Event identifier (e.g., PRES-2024)")
    title: str = Field(..., description="Event name")
    sub_title: Optional[str] = Field(None, description="Event subtitle")
    category: Optional[str] = Field(None, description="Event category")
    series_ticker: Optional[str] = Field(None, description="Associated series template")

    # Event properties
    strike_period: Optional[str] = Field(None, description="Strike period information")
    mutually_exclusive: Optional[bool] = Field(None, description="Whether markets are mutually exclusive")
    available_on_brokers: Optional[Union[bool, List[str]]] = Field(None, description="Brokers where available (bool or list)")
    collateral_return_type: Optional[str] = Field(None, description="Collateral return type")

    # For compatibility with old code that uses 'ticker'
    @property
    def ticker(self) -> str:
        """Alias for event_ticker for backward compatibility."""
        return self.event_ticker

    # Legacy fields (optional for backward compatibility)
    description: Optional[str] = Field(None, description="Event details")
    created_at: Optional[str] = Field(None, description="ISO timestamp")
    status: Optional[EventStatus] = Field(None, description="Event status")
    markets: Optional[List[Market]] = Field(None, description="Nested markets (optional)")

    @field_validator("available_on_brokers", mode="before")
    @classmethod
    def normalize_available_on_brokers(cls, v):
        """Normalize available_on_brokers to handle both bool and list.

        The API sometimes returns this as a boolean flag, sometimes as a list.
        We keep it as-is to maintain fidelity with the API response.
        """
        return v


class Series(BaseModel):
    """Kalshi series template."""

    ticker: str = Field(..., description="Series identifier")
    title: str = Field(..., description="Series name")
    description: Optional[str] = Field(None, description="Series details")
    category: Optional[str] = Field(None, description="Series category")
    created_at: Optional[str] = Field(None, description="ISO timestamp")


class OrderGroup(BaseModel):
    """Order group for risk management."""

    id: str = Field(..., description="Order group identifier")
    contract_limit: int = Field(..., description="Maximum contracts allowed in group")
    matched_contracts: int = Field(..., description="Currently matched contracts")


class Milestone(BaseModel):
    """Event milestone."""

    id: str = Field(..., description="Milestone identifier")
    event_ticker: str = Field(..., description="Associated event")
    title: str = Field(..., description="Milestone title")
    timestamp: int = Field(..., description="Milestone timestamp (Unix seconds)")
    source: str = Field(..., description="Milestone source")


class RFQ(BaseModel):
    """Request for Quote."""

    id: str = Field(..., description="RFQ identifier")
    ticker: str = Field(..., description="Market ticker")
    side: OrderSide = Field(..., description="Buy or sell")
    count: int = Field(..., description="Number of contracts")
    created_at: str = Field(..., description="ISO timestamp")
    status: str = Field(..., description="RFQ status")


class Quote(BaseModel):
    """Quote response to RFQ."""

    id: str = Field(..., description="Quote identifier")
    rfq_id: str = Field(..., description="Associated RFQ")
    price: int = Field(..., description="Quoted price (cents)")
    quantity: int = Field(..., description="Quoted quantity")
    created_at: str = Field(..., description="ISO timestamp")


class MultivarianateCollection(BaseModel):
    """Multivariate event collection."""

    ticker: str = Field(..., description="Collection identifier")
    title: str = Field(..., description="Collection name")
    description: str = Field(..., description="Collection details")
    status: str = Field(..., description="Collection status")


class QueuePosition(BaseModel):
    """Order's position in price-time priority queue."""

    order_id: str = Field(..., description="Order identifier")
    position: int = Field(..., description="Position in queue (0 = next to execute)")
    timestamp: int = Field(..., description="Timestamp when order entered queue")


class Settlement(BaseModel):
    """Settlement record - historical P&L tracking."""

    order_id: str = Field(..., description="Associated order ID")
    ticker: str = Field(..., description="Market ticker")
    side: OrderSide = Field(..., description="Buy or sell side")
    count: int = Field(..., description="Number of contracts")
    price: int = Field(..., description="Settlement price (cents)")
    payout: int = Field(..., description="Total payout (cents)")
    created_at: int = Field(..., description="Settlement timestamp (Unix milliseconds)")
    market_title: Optional[str] = Field(None, description="Market title")


class TotalRestingOrderValue(BaseModel):
    """Total value of all resting orders."""

    total_resting_order_value: int = Field(..., description="Total value of resting orders (cents)")


class ExchangeStatus(BaseModel):
    """Exchange-wide status information - matches actual API response format."""

    trading_active: bool = Field(..., description="Is trading currently active")
    timestamp: int = Field(default=0, description="Status timestamp (Unix seconds)")
    maintenance: Optional[str] = Field(None, description="Maintenance message if applicable")
