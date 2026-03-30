"""
Pydantic models for Polymarket WebSocket events.

These models define the structure of messages received from Polymarket's
real-time WebSocket API.
"""

from typing import Literal, Optional, List, Any
from datetime import datetime
from pydantic import BaseModel, Field
from enum import Enum


class WebSocketEventType(str, Enum):
    """Types of WebSocket events from Polymarket."""

    # Market data events (public)
    PRICE_CHANGE = "price_change"
    LAST_TRADE_PRICE = "last_trade_price"
    BOOK = "book"  # Order book update
    TICK_SIZE_CHANGE = "tick_size_change"

    # User events (authenticated)
    USER_ORDER = "user_order"
    USER_FILL = "user_fill"
    USER_BALANCE = "user_balance"

    # System events
    SUBSCRIBED = "subscribed"
    UNSUBSCRIBED = "unsubscribed"
    ERROR = "error"


class WebSocketChannel(str, Enum):
    """WebSocket subscription channels."""

    MARKET = "market"  # Public market data
    USER = "user"  # Authenticated user updates


class WebSocketMessage(BaseModel):
    """Base WebSocket message structure."""

    event_type: str = Field(..., alias="event_type")
    timestamp: Optional[datetime] = None

    class Config:
        populate_by_name = True


class PriceChangeEvent(WebSocketMessage):
    """Price change event for a market outcome."""

    event_type: Literal[WebSocketEventType.PRICE_CHANGE] = WebSocketEventType.PRICE_CHANGE
    asset_id: str = Field(..., description="Token ID (YES or NO outcome)")
    market: str = Field(..., description="Market condition ID")
    price: float = Field(..., description="New price (0.001-0.999)")
    side: Optional[str] = Field(None, description="BID or ASK")

    @property
    def probability_pct(self) -> float:
        """Convert price to probability percentage."""
        return self.price * 100


class LastTradePriceEvent(WebSocketMessage):
    """Last trade price update."""

    event_type: Literal[WebSocketEventType.LAST_TRADE_PRICE] = WebSocketEventType.LAST_TRADE_PRICE
    asset_id: str
    market: str
    price: float
    size: Optional[float] = None

    @property
    def probability_pct(self) -> float:
        """Convert price to probability percentage."""
        return self.price * 100


class OrderBookLevel(BaseModel):
    """Single price level in order book."""

    price: float = Field(..., description="Price in dollars (0.001-0.999)")
    size: float = Field(..., description="Size in shares")


class OrderBookUpdate(WebSocketMessage):
    """Order book depth update."""

    event_type: Literal[WebSocketEventType.BOOK] = WebSocketEventType.BOOK
    asset_id: str
    market: str
    bids: List[OrderBookLevel] = Field(default_factory=list)
    asks: List[OrderBookLevel] = Field(default_factory=list)

    @property
    def best_bid(self) -> Optional[OrderBookLevel]:
        """Get best bid (highest price)."""
        return self.bids[0] if self.bids else None

    @property
    def best_ask(self) -> Optional[OrderBookLevel]:
        """Get best ask (lowest price)."""
        return self.asks[0] if self.asks else None

    @property
    def spread(self) -> Optional[float]:
        """Calculate bid-ask spread."""
        if self.best_bid and self.best_ask:
            return self.best_ask.price - self.best_bid.price
        return None


class TickSizeChangeEvent(WebSocketMessage):
    """Tick size (minimum price increment) change."""

    event_type: Literal[WebSocketEventType.TICK_SIZE_CHANGE] = WebSocketEventType.TICK_SIZE_CHANGE
    asset_id: str
    market: str
    tick_size: float = Field(..., description="New minimum price increment")


class UserOrderEvent(WebSocketMessage):
    """User order status update (authenticated channel)."""

    event_type: Literal[WebSocketEventType.USER_ORDER] = WebSocketEventType.USER_ORDER
    order_id: str
    market: str
    asset_id: str
    side: str = Field(..., description="BUY or SELL")
    price: float
    size: float
    size_matched: float = Field(default=0.0, description="Filled size")
    status: str = Field(..., description="LIVE, MATCHED, CANCELLED")

    @property
    def is_filled(self) -> bool:
        """Check if order is fully filled."""
        return self.size_matched >= self.size

    @property
    def fill_percentage(self) -> float:
        """Calculate fill percentage."""
        return (self.size_matched / self.size * 100) if self.size > 0 else 0.0


class UserFillEvent(WebSocketMessage):
    """User trade fill notification (authenticated channel)."""

    event_type: Literal[WebSocketEventType.USER_FILL] = WebSocketEventType.USER_FILL
    fill_id: str
    order_id: str
    market: str
    asset_id: str
    side: str
    price: float = Field(..., description="Execution price")
    size: float = Field(..., description="Filled size")
    fee: Optional[float] = Field(None, description="Fee paid")
    trade_id: str

    @property
    def total_cost(self) -> float:
        """Calculate total cost including fees."""
        base_cost = self.price * self.size
        return base_cost + (self.fee or 0.0)


class UserBalanceEvent(WebSocketMessage):
    """User balance update (authenticated channel)."""

    event_type: Literal[WebSocketEventType.USER_BALANCE] = WebSocketEventType.USER_BALANCE
    asset: str = Field(..., description="Asset type (USDC, etc.)")
    balance: float = Field(..., description="New balance")


class SubscribedEvent(WebSocketMessage):
    """Subscription confirmation."""

    event_type: Literal[WebSocketEventType.SUBSCRIBED] = WebSocketEventType.SUBSCRIBED
    channel: WebSocketChannel
    market: Optional[str] = None


class UnsubscribedEvent(WebSocketMessage):
    """Unsubscription confirmation."""

    event_type: Literal[WebSocketEventType.UNSUBSCRIBED] = WebSocketEventType.UNSUBSCRIBED
    channel: WebSocketChannel
    market: Optional[str] = None


class ErrorEvent(WebSocketMessage):
    """Error event."""

    event_type: Literal[WebSocketEventType.ERROR] = WebSocketEventType.ERROR
    code: Optional[str] = None
    message: str
    details: Optional[dict] = None


# Union type for all possible WebSocket events
WebSocketEvent = (
    PriceChangeEvent
    | LastTradePriceEvent
    | OrderBookUpdate
    | TickSizeChangeEvent
    | UserOrderEvent
    | UserFillEvent
    | UserBalanceEvent
    | SubscribedEvent
    | UnsubscribedEvent
    | ErrorEvent
)


def parse_websocket_message(data: dict) -> WebSocketEvent:
    """
    Parse raw WebSocket message data into appropriate event model.

    Args:
        data: Raw message dictionary from WebSocket

    Returns:
        Parsed event model

    Raises:
        ValueError: If event type is unknown
    """
    event_type = data.get("event_type")

    # Map event types to model classes
    event_models = {
        WebSocketEventType.PRICE_CHANGE: PriceChangeEvent,
        WebSocketEventType.LAST_TRADE_PRICE: LastTradePriceEvent,
        WebSocketEventType.BOOK: OrderBookUpdate,
        WebSocketEventType.TICK_SIZE_CHANGE: TickSizeChangeEvent,
        WebSocketEventType.USER_ORDER: UserOrderEvent,
        WebSocketEventType.USER_FILL: UserFillEvent,
        WebSocketEventType.USER_BALANCE: UserBalanceEvent,
        WebSocketEventType.SUBSCRIBED: SubscribedEvent,
        WebSocketEventType.UNSUBSCRIBED: UnsubscribedEvent,
        WebSocketEventType.ERROR: ErrorEvent,
    }

    model_class = event_models.get(event_type)
    if model_class is None:
        raise ValueError(f"Unknown event type: {event_type}")

    return model_class.model_validate(data)
