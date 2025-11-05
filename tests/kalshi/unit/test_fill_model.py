"""Unit tests for Fill model to ensure proper parsing of API responses.

These tests catch model structure bugs that VCR cassettes miss when
API returns empty results.
"""

import pytest
from datetime import datetime
from src.kalshi.models import Fill


class TestFillModel:
    """Test Fill model validation and parsing."""

    def test_fill_model_with_float_price(self):
        """
        Test that Fill model accepts float prices (in dollars).

        The Kalshi API returns fill prices as floats in dollars (e.g., 0.42),
        not integers in cents. This test ensures the model handles this correctly.

        Regression test for bug caught during system demonstration (2025-11-03).
        """
        # Simulate real API response format
        fill_data = {
            "fill_id": "12345",
            "order_id": "67890",
            "ticker": "TEST-MARKET",
            "side": "yes",
            "action": "buy",
            "count": 10,
            "price": 0.42,  # ← Float in dollars (not int in cents)
            "created_time": "2025-11-03T20:00:00Z",
            "is_taker": True,
            "fees": 5,
        }

        # This should NOT raise a validation error
        fill = Fill(**fill_data)

        # Verify parsing
        assert fill.price == 0.42
        assert fill.count == 10
        assert fill.ticker == "TEST-MARKET"

    def test_fill_cost_calculations(self):
        """Test Fill model cost calculation properties."""
        fill = Fill(
            fill_id="test",
            order_id="order123",
            ticker="TEST",
            side="yes",
            action="buy",
            count=10,
            price=0.50,  # 50¢
            created_time=datetime.now(),
            fees=10,
        )

        # 10 contracts @ $0.50 each = $5.00
        assert fill.cost_dollars == 5.0
        assert fill.cost_cents == 500

        # Fees: 10¢ = $0.10
        assert fill.fees_dollars == 0.10

    def test_fill_price_validation_bounds(self):
        """Test that Fill model validates price is between 0 and 1."""
        # Valid prices (0.00 to 1.00)
        Fill(
            fill_id="test",
            order_id="order",
            ticker="TEST",
            side="yes",
            action="buy",
            count=1,
            price=0.01,  # Min valid
            created_time=datetime.now(),
        )

        Fill(
            fill_id="test",
            order_id="order",
            ticker="TEST",
            side="yes",
            action="buy",
            count=1,
            price=0.99,  # Max valid
            created_time=datetime.now(),
        )

        # Invalid prices should raise validation error
        with pytest.raises(ValueError):
            Fill(
                fill_id="test",
                order_id="order",
                ticker="TEST",
                side="yes",
                action="buy",
                count=1,
                price=1.50,  # > 1.0 - invalid
                created_time=datetime.now(),
            )

        with pytest.raises(ValueError):
            Fill(
                fill_id="test",
                order_id="order",
                ticker="TEST",
                side="yes",
                action="buy",
                count=1,
                price=-0.10,  # < 0.0 - invalid
                created_time=datetime.now(),
            )

    def test_fill_optional_fields(self):
        """Test Fill model with optional fields."""
        # Minimal valid fill (only required fields)
        fill = Fill(
            fill_id="test",
            order_id="order",
            ticker="TEST",
            side="no",
            action="sell",
            count=5,
            price=0.75,
            created_time=datetime.now(),
        )

        # Optional fields should have defaults
        assert fill.trade_id is None
        assert fill.is_taker is False
        assert fill.fees is None
        assert fill.fees_dollars == 0.0

    def test_fill_realistic_api_response(self):
        """
        Test Fill model with realistic API response from Kalshi demo.

        This is the actual response format that caused the validation error.
        """
        # Actual response from Kalshi API that triggered the bug
        api_response = {
            "fills": [
                {
                    "fill_id": "abc123",
                    "order_id": "def456",
                    "ticker": "KXQUICKSETTLE-25NOV03H1510-2",
                    "side": "yes",
                    "action": "buy",
                    "count": 1,
                    "price": 0.01,  # ← This was causing "int_from_float" error
                    "created_time": "2025-11-03T19:00:00Z",
                    "trade_id": "trade789",
                    "is_taker": True,
                    "fees": 0,
                }
            ]
        }

        # Parse all fills from response
        fills = [Fill(**f) for f in api_response["fills"]]

        assert len(fills) == 1
        assert fills[0].price == 0.01
        assert fills[0].cost_dollars == 0.01  # 1 contract @ $0.01
        assert fills[0].cost_cents == 1  # 1 cent

    def test_empty_fill_list_handling(self):
        """Test that empty fill lists don't break (common in demo)."""
        # This is what cassettes contain - empty results
        api_response = {"cursor": "", "fills": []}

        fills = [Fill(**f) for f in api_response["fills"]]

        # Should successfully create empty list (no parsing error)
        assert fills == []
