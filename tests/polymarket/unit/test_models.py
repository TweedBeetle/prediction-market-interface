"""
Unit tests for Polymarket Pydantic models.

Tests model validation, computed properties, and serialization.
"""

import pytest
from pydantic import ValidationError

from src.polymarket.models import (
    Market,
    Order,
    OrderParams,
    OrderSide,
    OrderType,
    OrderBook,
    OrderBookLevel,
    Position,
    Trade,
    Event,
    ApiCredentials,
    SignatureType,
)


class TestMarketModel:
    """Test Market model validation and properties."""

    def test_market_creation(self):
        """Test creating a valid market."""
        market = Market(
            id="market123",
            condition_id="condition123",
            question="Will Bitcoin reach $100k in 2024?",
            clob_token_ids=["token_yes", "token_no"],
            best_bid=0.65,
            best_ask=0.67,
            last_price=0.66,
            volume=100000.0,
            volume_24h=5000.0,
            liquidity=50000.0,
            active=True,
            closed=False,
        )

        assert market.id == "market123"
        assert market.question == "Will Bitcoin reach $100k in 2024?"
        assert market.active is True

    def test_market_token_ids(self):
        """Test YES/NO token ID properties."""
        market = Market(
            id="m1",
            condition_id="c1",
            question="Test?",
            clob_token_ids=["yes_token", "no_token"],
            active=True,
            closed=False,
        )

        assert market.yes_token_id == "yes_token"
        assert market.no_token_id == "no_token"

    def test_market_spread_calculation(self):
        """Test spread calculation."""
        market = Market(
            id="m1",
            condition_id="c1",
            question="Test?",
            clob_token_ids=["yes", "no"],
            best_bid=0.60,
            best_ask=0.65,
            active=True,
            closed=False,
        )

        assert market.spread == pytest.approx(0.05)
        assert market.midpoint_price == pytest.approx(0.625)

    def test_market_spread_none_when_missing_prices(self):
        """Test spread is None when prices missing."""
        market = Market(
            id="m1",
            condition_id="c1",
            question="Test?",
            clob_token_ids=["yes", "no"],
            active=True,
            closed=False,
        )

        assert market.spread is None
        assert market.midpoint_price is None

    def test_market_interpretation(self):
        """Test LLM-friendly interpretation."""
        market = Market(
            id="m1",
            condition_id="c1",
            question="Will it rain tomorrow?",
            clob_token_ids=["yes", "no"],
            best_bid=0.70,
            best_ask=0.72,
            active=True,
            closed=False,
        )

        interpretation = market.interpretation
        assert "71%" in interpretation  # Midpoint of 0.70 and 0.72
        assert "Will it rain tomorrow?" in interpretation


class TestOrderParamsModel:
    """Test OrderParams model validation."""

    def test_order_params_creation(self):
        """Test creating valid order parameters."""
        params = OrderParams(
            token_id="token123",
            price=0.65,
            size=100.0,
            side=OrderSide.BUY,
            maker="0x1234567890abcdef1234567890abcdef12345678",
        )

        assert params.token_id == "token123"
        assert params.price == 0.65
        assert params.side == OrderSide.BUY

    def test_order_params_price_validation(self):
        """Test price must be between 0.001 and 0.999."""
        # Valid prices
        OrderParams(
            token_id="t1",
            price=0.001,
            size=10,
            side=OrderSide.BUY,
            maker="0x1234567890abcdef1234567890abcdef12345678",
        )

        OrderParams(
            token_id="t1",
            price=0.999,
            size=10,
            side=OrderSide.BUY,
            maker="0x1234567890abcdef1234567890abcdef12345678",
        )

        # Invalid - too low
        with pytest.raises(ValidationError):
            OrderParams(
                token_id="t1",
                price=0.0,
                size=10,
                side=OrderSide.BUY,
                maker="0x1234567890abcdef1234567890abcdef12345678",
            )

        # Invalid - too high
        with pytest.raises(ValidationError):
            OrderParams(
                token_id="t1",
                price=1.0,
                size=10,
                side=OrderSide.BUY,
                maker="0x1234567890abcdef1234567890abcdef12345678",
            )

    def test_order_params_size_validation(self):
        """Test size must be positive."""
        # Invalid - zero size
        with pytest.raises(ValidationError):
            OrderParams(
                token_id="t1",
                price=0.5,
                size=0,
                side=OrderSide.BUY,
                maker="0x1234567890abcdef1234567890abcdef12345678",
            )

        # Invalid - negative size
        with pytest.raises(ValidationError):
            OrderParams(
                token_id="t1",
                price=0.5,
                size=-10,
                side=OrderSide.BUY,
                maker="0x1234567890abcdef1234567890abcdef12345678",
            )

    def test_order_params_total_cost(self):
        """Test total cost calculation."""
        params = OrderParams(
            token_id="t1",
            price=0.65,
            size=100,
            side=OrderSide.BUY,
            maker="0x1234567890abcdef1234567890abcdef12345678",
        )

        assert params.total_cost == 65.0  # 0.65 * 100


class TestOrderModel:
    """Test Order model validation and properties."""

    def test_order_creation(self):
        """Test creating a valid order."""
        order = Order(
            order_id="order123",
            market_id="market123",
            token_id="token_yes",
            price=0.65,
            size=100.0,
            side=OrderSide.BUY,
            size_matched=50.0,
            owner="0x1234567890abcdef1234567890abcdef12345678",
            status="LIVE",
        )

        assert order.order_id == "order123"
        assert order.size == 100.0
        assert order.size_matched == 50.0

    def test_order_fill_status(self):
        """Test order fill status calculations."""
        order = Order(
            order_id="o1",
            market_id="m1",
            token_id="t1",
            price=0.5,
            size=100.0,
            side=OrderSide.BUY,
            size_matched=75.0,
            owner="0x1234567890abcdef1234567890abcdef12345678",
        )

        assert order.is_filled is False
        assert order.remaining_size == 25.0
        assert order.fill_percentage == 75.0

    def test_order_fully_filled(self):
        """Test fully filled order."""
        order = Order(
            order_id="o1",
            market_id="m1",
            token_id="t1",
            price=0.5,
            size=100.0,
            side=OrderSide.BUY,
            size_matched=100.0,
            owner="0x1234567890abcdef1234567890abcdef12345678",
        )

        assert order.is_filled is True
        assert order.remaining_size == 0.0
        assert order.fill_percentage == 100.0

    def test_order_total_cost(self):
        """Test total cost of filled portion."""
        order = Order(
            order_id="o1",
            market_id="m1",
            token_id="t1",
            price=0.60,
            size=100.0,
            side=OrderSide.BUY,
            size_matched=50.0,
            owner="0x1234567890abcdef1234567890abcdef12345678",
        )

        assert order.total_cost == 30.0  # 0.60 * 50


class TestOrderBookModel:
    """Test OrderBook model and calculations."""

    def test_orderbook_creation(self):
        """Test creating an orderbook."""
        orderbook = OrderBook(
            market_id="m1",
            token_id="token_yes",
            bids=[
                OrderBookLevel(price=0.65, size=100),
                OrderBookLevel(price=0.64, size=200),
            ],
            asks=[
                OrderBookLevel(price=0.67, size=150),
                OrderBookLevel(price=0.68, size=250),
            ],
        )

        assert len(orderbook.bids) == 2
        assert len(orderbook.asks) == 2

    def test_orderbook_best_bid_ask(self):
        """Test best bid/ask properties."""
        orderbook = OrderBook(
            market_id="m1",
            token_id="t1",
            bids=[
                OrderBookLevel(price=0.65, size=100),
                OrderBookLevel(price=0.64, size=200),
            ],
            asks=[
                OrderBookLevel(price=0.67, size=150),
                OrderBookLevel(price=0.68, size=250),
            ],
        )

        assert orderbook.best_bid.price == 0.65
        assert orderbook.best_ask.price == 0.67

    def test_orderbook_spread(self):
        """Test spread calculation."""
        orderbook = OrderBook(
            market_id="m1",
            token_id="t1",
            bids=[OrderBookLevel(price=0.65, size=100)],
            asks=[OrderBookLevel(price=0.68, size=150)],
        )

        assert orderbook.spread == pytest.approx(0.03)
        assert orderbook.midpoint_price == pytest.approx(0.665)

    def test_orderbook_empty(self):
        """Test empty orderbook."""
        orderbook = OrderBook(
            market_id="m1",
            token_id="t1",
            bids=[],
            asks=[],
        )

        assert orderbook.best_bid is None
        assert orderbook.best_ask is None
        assert orderbook.spread is None

    def test_orderbook_liquidity(self):
        """Test liquidity calculations."""
        orderbook = OrderBook(
            market_id="m1",
            token_id="t1",
            bids=[
                OrderBookLevel(price=0.60, size=100),  # 60 liquidity
                OrderBookLevel(price=0.55, size=200),  # 110 liquidity
            ],
            asks=[
                OrderBookLevel(price=0.70, size=100),  # 70 liquidity
                OrderBookLevel(price=0.75, size=200),  # 150 liquidity
            ],
        )

        assert orderbook.total_bid_liquidity == 170.0  # 60 + 110
        assert orderbook.total_ask_liquidity == 220.0  # 70 + 150


class TestPositionModel:
    """Test Position model and P&L calculations."""

    def test_position_creation(self):
        """Test creating a position."""
        position = Position(
            market_id="m1",
            token_id="token_yes",
            size=100.0,
            outcome="YES",
            average_price=0.60,
            total_cost=60.0,
            current_price=0.70,
            market_value=70.0,
            unrealized_pnl=10.0,
        )

        assert position.size == 100.0
        assert position.unrealized_pnl == 10.0

    def test_position_pnl_percentage(self):
        """Test P&L percentage calculation."""
        position = Position(
            market_id="m1",
            token_id="t1",
            size=100.0,
            outcome="YES",
            total_cost=50.0,
            unrealized_pnl=10.0,
        )

        assert position.pnl_percentage == 20.0  # 10/50 * 100

    def test_position_is_profitable(self):
        """Test profitability check."""
        profitable = Position(
            market_id="m1",
            token_id="t1",
            size=100.0,
            outcome="YES",
            unrealized_pnl=10.0,
        )

        unprofitable = Position(
            market_id="m2",
            token_id="t2",
            size=100.0,
            outcome="NO",
            unrealized_pnl=-5.0,
        )

        assert profitable.is_profitable is True
        assert unprofitable.is_profitable is False


class TestTradeModel:
    """Test Trade model."""

    def test_trade_creation(self):
        """Test creating a trade."""
        trade = Trade(
            trade_id="trade123",
            market_id="m1",
            token_id="token_yes",
            price=0.65,
            size=100.0,
            side=OrderSide.BUY,
            outcome="YES",
        )

        assert trade.trade_id == "trade123"
        assert trade.price == 0.65

    def test_trade_total_value(self):
        """Test total value calculation."""
        trade = Trade(
            trade_id="t1",
            market_id="m1",
            token_id="token_yes",
            price=0.60,
            size=150.0,
            side=OrderSide.BUY,
            outcome="YES",
        )

        assert trade.total_value == 90.0  # 0.60 * 150


class TestEventModel:
    """Test Event model."""

    def test_event_creation(self):
        """Test creating an event."""
        markets = [
            Market(
                id="m1",
                condition_id="c1",
                question="Market 1?",
                clob_token_ids=["yes", "no"],
                volume=1000.0,
                active=True,
                closed=False,
            ),
            Market(
                id="m2",
                condition_id="c2",
                question="Market 2?",
                clob_token_ids=["yes", "no"],
                volume=2000.0,
                active=True,
                closed=False,
            ),
        ]

        event = Event(
            id="event123",
            slug="test-event",
            title="Test Event",
            markets=markets,
        )

        assert event.title == "Test Event"
        assert event.market_count == 2

    def test_event_total_volume(self):
        """Test total volume calculation."""
        markets = [
            Market(
                id="m1",
                condition_id="c1",
                question="Market 1?",
                clob_token_ids=["yes", "no"],
                volume=1000.0,
                active=True,
                closed=False,
            ),
            Market(
                id="m2",
                condition_id="c2",
                question="Market 2?",
                clob_token_ids=["yes", "no"],
                volume=2000.0,
                active=True,
                closed=False,
            ),
        ]

        event = Event(
            id="e1",
            slug="test",
            title="Test",
            markets=markets,
        )

        assert event.total_volume == 3000.0


class TestApiCredentialsModel:
    """Test ApiCredentials model."""

    def test_credentials_creation(self):
        """Test creating API credentials."""
        creds = ApiCredentials(
            private_key="0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",
            wallet_address="0x1234567890abcdef1234567890abcdef12345678",
            chain_id=137,
        )

        assert creds.wallet_address == "0x1234567890abcdef1234567890abcdef12345678"
        assert creds.chain_id == 137

    def test_credentials_with_api_key(self):
        """Test credentials with API key."""
        creds = ApiCredentials(
            private_key="0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",
            wallet_address="0x1234567890abcdef1234567890abcdef12345678",
            api_key="key123",
            api_secret="secret123",
            api_passphrase="pass123",
            chain_id=137,
        )

        assert creds.api_key == "key123"
        assert creds.api_secret == "secret123"
        assert creds.api_passphrase == "pass123"


class TestEnums:
    """Test enum values."""

    def test_order_side_enum(self):
        """Test OrderSide enum."""
        assert OrderSide.BUY.value == "BUY"
        assert OrderSide.SELL.value == "SELL"

    def test_order_type_enum(self):
        """Test OrderType enum."""
        assert OrderType.FOK.value == "FOK"
        assert OrderType.GTC.value == "GTC"
        assert OrderType.GTD.value == "GTD"

    def test_signature_type_enum(self):
        """Test SignatureType enum."""
        assert SignatureType.EOA.value == "EOA"
        assert SignatureType.POLY_PROXY.value == "POLY_PROXY"
        assert SignatureType.POLY_GNOSIS_SAFE.value == "POLY_GNOSIS_SAFE"
