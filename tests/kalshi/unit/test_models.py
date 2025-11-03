"""Unit tests for Pydantic models."""

from datetime import datetime
import pytest
from pydantic import ValidationError

from src.kalshi.models import ExchangeStatus, Balance, Market, Event


class TestExchangeStatus:
    """Test ExchangeStatus model."""

    def test_valid_status(self):
        """Can create valid exchange status."""
        status = ExchangeStatus(exchange_active=True, trading_active=True)
        assert status.exchange_active is True
        assert status.trading_active is True

    def test_both_inactive(self):
        """Can represent fully inactive exchange."""
        status = ExchangeStatus(exchange_active=False, trading_active=False)
        assert status.exchange_active is False
        assert status.trading_active is False


class TestBalance:
    """Test Balance model."""

    def test_valid_balance(self):
        """Can create balance with cents."""
        balance = Balance(balance=100000)  # $1000.00
        assert balance.balance == 100000
        assert balance.balance_dollars == 1000.0

    def test_zero_balance(self):
        """Can represent zero balance."""
        balance = Balance(balance=0)
        assert balance.balance == 0
        assert balance.balance_dollars == 0.0

    def test_balance_dollars_conversion(self):
        """Properly converts cents to dollars."""
        balance = Balance(balance=12345)  # $123.45
        assert balance.balance_dollars == 123.45


class TestMarket:
    """Test Market model."""

    def test_minimal_market(self):
        """Can create market with minimal required fields."""
        market = Market(
            ticker="TEST-01JAN-Y",
            event_ticker="TEST",
            title="Test Market",
            subtitle=None,
            status="open",
            close_time=datetime(2025, 1, 1),
        )
        assert market.ticker == "TEST-01JAN-Y"
        assert market.status == "open"

    def test_market_with_prices(self):
        """Market with bid/ask prices."""
        market = Market(
            ticker="TEST-01JAN-Y",
            event_ticker="TEST",
            title="Test Market",
            status="open",
            close_time=datetime(2025, 1, 1),
            yes_bid=40,
            yes_ask=42,
            no_bid=58,
            no_ask=60,
        )
        assert market.yes_bid == 40
        assert market.yes_ask == 42
        assert market.spread == 2

    def test_interpretation_with_price(self):
        """Interpretation includes price and title."""
        market = Market(
            ticker="TEST-01JAN-Y",
            event_ticker="TEST",
            title="Bitcoin reaches $50K",
            status="open",
            close_time=datetime(2025, 1, 1),
            yes_ask=42,
        )
        assert "42%" in market.interpretation
        assert "Bitcoin reaches $50K" in market.interpretation

    def test_invalid_price_rejected(self):
        """Prices outside 1-99 range are rejected."""
        with pytest.raises(ValidationError):
            Market(
                ticker="TEST-01JAN-Y",
                event_ticker="TEST",
                title="Test",
                status="open",
                close_time=datetime(2025, 1, 1),
                yes_ask=150,  # Invalid: > 99
            )

    def test_spread_calculation(self):
        """Spread is calculated correctly."""
        market = Market(
            ticker="TEST-01JAN-Y",
            event_ticker="TEST",
            title="Test",
            status="open",
            close_time=datetime(2025, 1, 1),
            yes_bid=45,
            yes_ask=50,
        )
        assert market.spread == 5

    def test_spread_none_when_missing_prices(self):
        """Spread is None when prices missing."""
        market = Market(
            ticker="TEST-01JAN-Y",
            event_ticker="TEST",
            title="Test",
            status="open",
            close_time=datetime(2025, 1, 1),
        )
        assert market.spread is None


class TestEvent:
    """Test Event model."""

    def test_minimal_event(self):
        """Can create event with required fields."""
        event = Event(
            event_ticker="TEST",
            title="Test Event",
            category="crypto",
            mutually_exclusive=True,
        )
        assert event.event_ticker == "TEST"
        assert event.title == "Test Event"
        assert event.mutually_exclusive is True

    def test_event_with_optional_fields(self):
        """Event with all optional fields."""
        event = Event(
            event_ticker="TEST",
            title="Test Event",
            category="crypto",
            series_ticker="TEST-SERIES",
            sub_title="A test event",
            mutually_exclusive=False,
            strike_date=datetime(2025, 1, 1),
        )
        assert event.series_ticker == "TEST-SERIES"
        assert event.sub_title == "A test event"
        assert event.strike_date == datetime(2025, 1, 1)
