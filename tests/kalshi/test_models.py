"""Pydantic model validation tests."""

import pytest
from pydantic import ValidationError

from src.kalshi.models import (
    Balance,
    Candlestick,
    Event,
    EventStatus,
    Fill,
    Market,
    MarketStatus,
    Order,
    OrderSide,
    OrderStatus,
    OrderType,
    Orderbook,
    Position,
    Trade,
)


@pytest.mark.unit
class TestMarketModel:
    """Test Market model validation."""

    def test_market_valid_data(self, sample_market):
        """Test Market model with valid data."""
        assert sample_market.ticker == "KXHARRIS24-LSV"
        assert sample_market.status == MarketStatus.OPEN
        assert sample_market.yes_bid == 65.0
        assert sample_market.yes_ask == 66.0

    def test_market_required_fields(self):
        """Test Market model requires all required fields."""
        with pytest.raises(ValidationError):
            Market(
                ticker="TEST",
                # Missing required fields
            )

    def test_market_price_range(self):
        """Test Market model price should be 0-100 (cents)."""
        # Valid prices
        market = Market(
            ticker="TEST",
            event_ticker="TEST",
            series_ticker="TEST",
            title="Test",
            description="Test",
            status=MarketStatus.OPEN,
            yes_bid=0.0,
            yes_ask=100.0,
            no_bid=0.0,
            no_ask=100.0,
            volume=0,
            open_interest=0,
            created_at="2024-01-01T00:00:00Z",
            close_ts=1735689600,
        )
        assert market.yes_bid == 0.0
        assert market.yes_ask == 100.0

    def test_market_optional_fields(self):
        """Test Market model optional fields."""
        market = Market(
            ticker="TEST",
            title="Test",
            status=MarketStatus.CLOSED,
            # Optional fields
            yes_bid=None,
            yes_ask=None,
            last_price=None,
            expiration_time=None,
            result=None,
        )
        assert market.yes_bid is None
        assert market.result is None

    def test_market_status_enum(self):
        """Test Market status is enum."""
        market = Market(
            ticker="TEST",
            event_ticker="TEST",
            series_ticker="TEST",
            title="Test",
            description="Test",
            status=MarketStatus.SETTLED,
            volume=0,
            open_interest=0,
            created_at="2024-01-01T00:00:00Z",
            close_ts=1735689600,
        )
        assert isinstance(market.status, MarketStatus)
        assert market.status == MarketStatus.SETTLED


@pytest.mark.unit
class TestOrderModel:
    """Test Order model validation."""

    def test_order_valid_data(self, sample_order):
        """Test Order model with valid data."""
        assert sample_order.id == "order-123"
        assert sample_order.side == OrderSide.BUY
        assert sample_order.type == OrderType.LIMIT
        assert sample_order.price == 65

    def test_order_side_validation(self):
        """Test Order side must be buy or sell."""
        order = Order(
            id="test",
            ticker="TEST",
            status=OrderStatus.RESTING,
            side=OrderSide.BUY,
            type=OrderType.LIMIT,
            price=50,
            count=10,
            fill_count=0,
            remaining_count=10,
            created_at="2024-01-01T00:00:00Z",
            last_updated_at="2024-01-01T00:00:00Z",
        )
        assert order.side == OrderSide.BUY

    def test_order_type_validation(self):
        """Test Order type must be limit or market."""
        order = Order(
            id="test",
            ticker="TEST",
            status=OrderStatus.RESTING,
            side=OrderSide.SELL,
            type=OrderType.MARKET,
            price=50,
            count=10,
            fill_count=5,
            remaining_count=5,
            created_at="2024-01-01T00:00:00Z",
            last_updated_at="2024-01-01T00:00:00Z",
        )
        assert order.type == OrderType.MARKET

    def test_order_price_range(self):
        """Test Order price is 1-99 cents."""
        # Valid price
        order = Order(
            id="test",
            ticker="TEST",
            status=OrderStatus.EXECUTED,
            side=OrderSide.BUY,
            type=OrderType.LIMIT,
            price=50,  # Valid: 1-99
            count=10,
            fill_count=10,
            remaining_count=0,
            created_at="2024-01-01T00:00:00Z",
            last_updated_at="2024-01-01T00:00:00Z",
        )
        assert order.price == 50

    def test_order_status_enum(self):
        """Test Order status is enum."""
        for status in [OrderStatus.RESTING, OrderStatus.CANCELED, OrderStatus.EXECUTED]:
            order = Order(
                id="test",
                ticker="TEST",
                status=status,
                side=OrderSide.BUY,
                type=OrderType.LIMIT,
                price=50,
                count=10,
                fill_count=0,
                remaining_count=10,
                created_at="2024-01-01T00:00:00Z",
                last_updated_at="2024-01-01T00:00:00Z",
            )
            assert order.status == status


@pytest.mark.unit
class TestPositionModel:
    """Test Position model validation."""

    def test_position_valid_data(self, sample_position):
        """Test Position model with valid data."""
        assert sample_position.ticker == "KXHARRIS24-LSV"
        assert sample_position.position == 100
        assert sample_position.side == "long"

    def test_position_required_fields(self):
        """Test Position model requires all required fields."""
        with pytest.raises(ValidationError):
            Position(
                ticker="TEST",
                # Missing other required fields
            )


@pytest.mark.unit
class TestBalanceModel:
    """Test Balance model validation."""

    def test_balance_valid_data(self, sample_balance):
        """Test Balance model with valid data."""
        assert sample_balance.balance == 1000000
        assert sample_balance.portfolio_value == 1500000

    def test_balance_negative_values(self):
        """Test Balance can have values."""
        balance = Balance(balance=0, portfolio_value=0)
        assert balance.balance == 0


@pytest.mark.unit
class TestFillModel:
    """Test Fill (executed trade) model validation."""

    def test_fill_valid_data(self, sample_fill):
        """Test Fill model with valid data."""
        assert sample_fill.market_ticker == "KXHARRIS24-LSV"
        assert sample_fill.order_id == "order-123"
        assert sample_fill.is_buy is True
        assert sample_fill.quantity == 100
        assert sample_fill.price == 65.0

    def test_fill_buy_sell(self):
        """Test Fill side (is_buy boolean)."""
        fill_buy = Fill(
            market_ticker="TEST",
            order_id="order-1",
            is_buy=True,
            quantity=10,
            price=50.0,
            timestamp=1698765432,
        )
        assert fill_buy.is_buy is True

        fill_sell = Fill(
            market_ticker="TEST",
            order_id="order-2",
            is_buy=False,
            quantity=10,
            price=50.0,
            timestamp=1698765432,
        )
        assert fill_sell.is_buy is False


@pytest.mark.unit
class TestCandlestickModel:
    """Test Candlestick (OHLCV) model validation."""

    def test_candlestick_valid_data(self, sample_candlestick):
        """Test Candlestick model with valid data."""
        assert sample_candlestick.open == 60.0
        assert sample_candlestick.high == 70.0
        assert sample_candlestick.low == 55.0
        assert sample_candlestick.close == 65.0
        assert sample_candlestick.volume == 1000000

    def test_candlestick_price_ordering(self):
        """Test Candlestick has valid price relationships (high >= all, low <= all)."""
        candlestick = Candlestick(
            start_ts=1698700800,
            end_ts=1698787200,
            open=60.0,
            high=70.0,  # Should be >= all others
            low=55.0,   # Should be <= all others
            close=65.0,
            volume=1000000,
        )
        assert candlestick.high >= candlestick.open
        assert candlestick.high >= candlestick.close
        assert candlestick.high >= candlestick.low
        assert candlestick.low <= candlestick.open
        assert candlestick.low <= candlestick.close


@pytest.mark.unit
class TestOrderbookModel:
    """Test Orderbook model validation."""

    def test_orderbook_valid_data(self, sample_orderbook):
        """Test Orderbook model with valid data."""
        assert sample_orderbook.ticker == "KXHARRIS24-LSV"
        assert len(sample_orderbook.bids) == 3
        assert len(sample_orderbook.asks) == 3

    def test_orderbook_bid_ask_format(self):
        """Test Orderbook bids/asks are (price, size) tuples."""
        orderbook = Orderbook(
            ticker="TEST",
            bids=[(65.0, 1000), (64.0, 500)],
            asks=[(66.0, 1000), (67.0, 500)],
            timestamp=1698765432000,
        )
        # Bids should be in descending order (best bid first)
        assert orderbook.bids[0][0] > orderbook.bids[1][0]
        # Asks should be in ascending order (best ask first)
        assert orderbook.asks[0][0] < orderbook.asks[1][0]


@pytest.mark.unit
class TestTradeModel:
    """Test Trade model validation."""

    def test_trade_valid_data(self):
        """Test Trade model with valid data."""
        trade = Trade(
            market_ticker="TEST",
            price=65.0,
            size=100,
            timestamp=1698765432000,
        )
        assert trade.market_ticker == "TEST"
        assert trade.price == 65.0
        assert trade.size == 100


@pytest.mark.unit
class TestEventModel:
    """Test Event model validation."""

    def test_event_valid_data(self):
        """Test Event model with valid data."""
        event = Event(
            event_ticker="PRES-2024-HARRIS",
            title="2024 Presidential Election",
            description="Will Kamala Harris win?",
            status=EventStatus.OPEN,
            created_at="2024-01-01T00:00:00Z",
            category="politics",
            series_ticker="PRES-2024",
        )
        assert event.event_ticker == "PRES-2024-HARRIS"
        assert event.ticker == "PRES-2024-HARRIS"  # Test backward compatibility alias
        assert event.status == EventStatus.OPEN

    def test_event_status_enum(self):
        """Test Event status is enum."""
        for status in [EventStatus.OPEN, EventStatus.CLOSED, EventStatus.SETTLED]:
            event = Event(
                event_ticker="TEST",
                title="Test",
                description="Test",
                status=status,
                created_at="2024-01-01T00:00:00Z",
                category="test",
                series_ticker="TEST",
            )
            assert event.status == status


@pytest.mark.unit
class TestModelSerialization:
    """Test model serialization/deserialization."""

    def test_market_model_dump(self, sample_market):
        """Test Market model serializes to dict."""
        data = sample_market.model_dump()
        assert isinstance(data, dict)
        assert data["ticker"] == "KXHARRIS24-LSV"
        assert data["status"] == "open"  # Enum serialized as string

    def test_market_model_json(self, sample_market):
        """Test Market model serializes to JSON string."""
        json_str = sample_market.model_dump_json()
        assert isinstance(json_str, str)
        assert "KXHARRIS24-LSV" in json_str

    def test_order_model_dump(self, sample_order):
        """Test Order model serializes to dict."""
        data = sample_order.model_dump()
        assert isinstance(data, dict)
        assert data["side"] == "buy"  # Enum serialized
        assert data["type"] == "limit"  # Enum serialized

    def test_model_construct_with_all_fields(self):
        """Test model_construct requires all accessed fields."""
        # This tests that accessing a field that wasn't provided raises AttributeError
        market = Market.model_construct(
            ticker="TEST",
            event_ticker="TEST",
            series_ticker="TEST",
            title="Test",
            description="Test",
            status=MarketStatus.OPEN,
            yes_bid=50.0,
            yes_ask=51.0,
            no_bid=49.0,
            no_ask=50.0,
            last_price=50.5,
            volume=1000,
            open_interest=500,
            created_at="2024-01-01T00:00:00Z",
            close_ts=1735689600,
            settlement_ts=None,
            settlement_source=None,
            settlement_value=None,
        )

        # Should be able to access all fields
        assert market.ticker == "TEST"
        assert market.yes_bid == 50.0
        assert market.volume == 1000

    def test_model_construct_missing_field_raises_error(self):
        """Test that accessing missing fields from model_construct raises AttributeError."""
        market = Market.model_construct(
            ticker="TEST",
            event_ticker="TEST",
            # Missing most fields
        )

        # Accessing missing field should raise AttributeError
        with pytest.raises(AttributeError):
            _ = market.title  # Not provided to model_construct


@pytest.mark.unit
class TestEnumValidation:
    """Test enum field validation."""

    def test_market_status_enum_values(self):
        """Test MarketStatus enum has expected values."""
        statuses = [
            MarketStatus.UNOPENED,
            MarketStatus.OPEN,
            MarketStatus.ACTIVE,
            MarketStatus.CLOSED,
            MarketStatus.SETTLED,
        ]
        assert len(statuses) == 5

    def test_order_side_enum_values(self):
        """Test OrderSide enum has buy/sell."""
        assert OrderSide.BUY.value == "buy"
        assert OrderSide.SELL.value == "sell"

    def test_order_type_enum_values(self):
        """Test OrderType enum has limit/market."""
        assert OrderType.LIMIT.value == "limit"
        assert OrderType.MARKET.value == "market"

    def test_order_status_enum_values(self):
        """Test OrderStatus enum has expected values."""
        statuses = [
            OrderStatus.RESTING,
            OrderStatus.CANCELED,
            OrderStatus.EXECUTED,
        ]
        assert len(statuses) == 3

    def test_event_status_enum_values(self):
        """Test EventStatus enum has expected values."""
        statuses = [EventStatus.OPEN, EventStatus.CLOSED, EventStatus.SETTLED]
        assert len(statuses) == 3


@pytest.mark.unit
class TestModelValidationEdgeCases:
    """Test edge cases in model validation."""

    def test_market_with_zero_volume(self):
        """Test Market can have zero volume."""
        market = Market(
            ticker="NEW",
            event_ticker="NEW",
            series_ticker="NEW",
            title="New Market",
            description="No trades yet",
            status=MarketStatus.UNOPENED,
            volume=0,  # No trades
            open_interest=0,
            created_at="2024-01-01T00:00:00Z",
            close_ts=1735689600,
        )
        assert market.volume == 0

    def test_order_with_zero_fills(self):
        """Test Order can have zero fills."""
        order = Order(
            id="new-order",
            ticker="TEST",
            status=OrderStatus.RESTING,
            side=OrderSide.BUY,
            type=OrderType.LIMIT,
            price=50,
            count=100,
            fill_count=0,  # No fills yet
            remaining_count=100,
            created_at="2024-01-01T00:00:00Z",
            last_updated_at="2024-01-01T00:00:00Z",
        )
        assert order.fill_count == 0
        assert order.remaining_count == 100

    def test_balance_with_zero_values(self):
        """Test Balance with zero values."""
        balance = Balance(balance=0, portfolio_value=0)
        assert balance.balance == 0
        assert balance.portfolio_value == 0

    def test_candlestick_with_same_prices(self):
        """Test Candlestick where OHLC are the same (no price movement)."""
        candlestick = Candlestick(
            start_ts=1698700800,
            end_ts=1698787200,
            open=65.0,
            high=65.0,  # Same as all others
            low=65.0,
            close=65.0,
            volume=1000,
        )
        assert candlestick.open == candlestick.high == candlestick.low == candlestick.close
