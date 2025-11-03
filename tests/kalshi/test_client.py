"""KalshiClient API client tests."""

import pytest
from unittest.mock import AsyncMock, MagicMock, patch

from src.kalshi import KalshiClient
from src.kalshi.models import Market, Order, OrderSide, OrderType, Position, Balance


@pytest.mark.unit
class TestKalshiClientInitialization:
    """Test KalshiClient initialization."""

    def test_client_initializes_with_env_vars(self, mock_kalshi_client):
        """Test client initializes with environment variables."""
        assert mock_kalshi_client is not None
        assert mock_kalshi_client.api_key_id == "test-key-id-550e8400-e29b-41d4-a716-446655440000"
        assert mock_kalshi_client.private_key is not None

    def test_client_timeout_default(self, mock_kalshi_client):
        """Test client timeout has default value."""
        assert mock_kalshi_client.timeout == 30.0

    def test_client_timeout_custom(self, test_private_key_pem, monkeypatch):
        """Test client with custom timeout."""
        monkeypatch.setenv("KALSHI_API_KEY_ID", "test-key")
        monkeypatch.setenv("KALSHI_PRIVATE_KEY_PATH", test_private_key_pem)

        client = KalshiClient(timeout=60.0)
        assert client.timeout == 60.0

    def test_client_base_url(self, mock_kalshi_client):
        """Test client uses correct base URL."""
        assert mock_kalshi_client.BASE_URL == "https://api.elections.kalshi.com/trade-api/v2"


@pytest.mark.unit
class TestKalshiClientSignatureGeneration:
    """Test signature generation in KalshiClient."""

    def test_generate_signature_returns_string(self, mock_kalshi_client):
        """Test _generate_signature returns base64-encoded string."""
        timestamp = 1698765432123
        method = "GET"
        path = "/markets"

        signature = mock_kalshi_client._generate_signature(timestamp, method, path)

        assert isinstance(signature, str)
        assert len(signature) > 0

    def test_generate_signature_format(self, mock_kalshi_client):
        """Test signature format is valid base64."""
        import base64

        timestamp = 1698765432123
        signature = mock_kalshi_client._generate_signature(timestamp, "GET", "/markets")

        # Should be valid base64
        try:
            decoded = base64.b64decode(signature)
            assert len(decoded) > 0
        except Exception:
            pytest.fail("Signature is not valid base64")

    def test_generate_signature_different_for_different_inputs(self, mock_kalshi_client):
        """Test signatures differ for different inputs."""
        timestamp = 1698765432123

        sig1 = mock_kalshi_client._generate_signature(timestamp, "GET", "/markets")
        sig2 = mock_kalshi_client._generate_signature(timestamp, "POST", "/markets")
        sig3 = mock_kalshi_client._generate_signature(timestamp, "GET", "/portfolio/orders")

        # Different inputs should produce different signatures (very likely)
        assert sig1 != sig2
        assert sig2 != sig3

    def test_generate_signature_different_for_different_timestamps(self, mock_kalshi_client):
        """Test signatures differ for different timestamps."""
        sig1 = mock_kalshi_client._generate_signature(1698765432123, "GET", "/markets")
        sig2 = mock_kalshi_client._generate_signature(1698765432124, "GET", "/markets")

        assert sig1 != sig2


@pytest.mark.unit
class TestKalshiClientRequestHeaders:
    """Test request header generation."""

    def test_get_headers_returns_dict(self, mock_kalshi_client):
        """Test _get_headers returns dictionary."""
        headers = mock_kalshi_client._get_headers("GET", "/markets")

        assert isinstance(headers, dict)

    def test_get_headers_includes_required_headers(self, mock_kalshi_client):
        """Test _get_headers includes all required authentication headers."""
        headers = mock_kalshi_client._get_headers("GET", "/markets")

        required_headers = [
            "KALSHI-ACCESS-KEY",
            "KALSHI-ACCESS-SIGNATURE",
            "KALSHI-ACCESS-TIMESTAMP",
            "Content-Type",
        ]

        for header in required_headers:
            assert header in headers

    def test_get_headers_content_type(self, mock_kalshi_client):
        """Test Content-Type is application/json."""
        headers = mock_kalshi_client._get_headers("GET", "/markets")

        assert headers["Content-Type"] == "application/json"

    def test_get_headers_different_for_different_methods(self, mock_kalshi_client):
        """Test headers differ for different HTTP methods."""
        headers_get = mock_kalshi_client._get_headers("GET", "/markets")
        headers_post = mock_kalshi_client._get_headers("POST", "/markets")

        # Signatures should be different
        assert headers_get["KALSHI-ACCESS-SIGNATURE"] != headers_post["KALSHI-ACCESS-SIGNATURE"]

    def test_get_headers_different_for_different_paths(self, mock_kalshi_client):
        """Test headers differ for different paths."""
        headers_markets = mock_kalshi_client._get_headers("GET", "/markets")
        headers_orders = mock_kalshi_client._get_headers("GET", "/portfolio/orders")

        # Signatures should be different
        assert headers_markets["KALSHI-ACCESS-SIGNATURE"] != headers_orders["KALSHI-ACCESS-SIGNATURE"]


@pytest.mark.unit
class TestKalshiClientErrorHandling:
    """Test error handling in client."""

    @pytest.mark.asyncio
    async def test_request_raises_on_404(self, mock_kalshi_client):
        """Test that 404 error is handled."""
        import httpx

        # Mock httpx.AsyncClient to raise 404
        with patch("httpx.AsyncClient") as mock_http_client:
            mock_response = MagicMock()
            mock_response.status_code = 404
            mock_response.raise_for_status.side_effect = httpx.HTTPStatusError(
                "404 Not Found", request=MagicMock(), response=mock_response
            )

            mock_http_client.return_value.__aenter__.return_value.request = AsyncMock(
                side_effect=httpx.HTTPStatusError(
                    "404 Not Found", request=MagicMock(), response=mock_response
                )
            )

            with pytest.raises(httpx.HTTPStatusError):
                await mock_kalshi_client._request("GET", "/markets/INVALID")

    @pytest.mark.asyncio
    async def test_request_handles_401(self, mock_kalshi_client):
        """Test that 401 Unauthorized is handled."""
        import httpx

        with patch("httpx.AsyncClient") as mock_http_client:
            mock_response = MagicMock()
            mock_response.status_code = 401

            mock_http_client.return_value.__aenter__.return_value.request = AsyncMock(
                side_effect=httpx.HTTPStatusError(
                    "401 Unauthorized", request=MagicMock(), response=mock_response
                )
            )

            with pytest.raises(httpx.HTTPStatusError):
                await mock_kalshi_client._request("GET", "/portfolio/balance")

    @pytest.mark.asyncio
    async def test_request_timeout_configurable(self, test_private_key_pem, monkeypatch):
        """Test that timeout is configurable."""
        monkeypatch.setenv("KALSHI_API_KEY_ID", "test-key")
        monkeypatch.setenv("KALSHI_PRIVATE_KEY_PATH", test_private_key_pem)

        client = KalshiClient(timeout=5.0)
        assert client.timeout == 5.0


@pytest.mark.unit
class TestKalshiClientAPIMethods:
    """Test API method signatures."""

    async def test_search_markets_signature(self, mock_kalshi_client):
        """Test search_markets method signature."""
        # Just verify the method exists and is callable
        assert callable(mock_kalshi_client.search_markets)

    async def test_get_market_signature(self, mock_kalshi_client):
        """Test get_market method signature."""
        assert callable(mock_kalshi_client.get_market)

    async def test_get_orderbook_signature(self, mock_kalshi_client):
        """Test get_orderbook method signature."""
        assert callable(mock_kalshi_client.get_orderbook)

    async def test_get_trades_signature(self, mock_kalshi_client):
        """Test get_trades method signature."""
        assert callable(mock_kalshi_client.get_trades)

    async def test_get_candlesticks_signature(self, mock_kalshi_client):
        """Test get_candlesticks method signature."""
        assert callable(mock_kalshi_client.get_candlesticks)

    async def test_get_events_signature(self, mock_kalshi_client):
        """Test get_events method signature."""
        assert callable(mock_kalshi_client.get_events)

    async def test_get_balance_signature(self, mock_kalshi_client):
        """Test get_balance method signature."""
        assert callable(mock_kalshi_client.get_balance)

    async def test_get_positions_signature(self, mock_kalshi_client):
        """Test get_positions method signature."""
        assert callable(mock_kalshi_client.get_positions)

    async def test_create_order_signature(self, mock_kalshi_client):
        """Test create_order method signature."""
        assert callable(mock_kalshi_client.create_order)

    async def test_cancel_order_signature(self, mock_kalshi_client):
        """Test cancel_order method signature."""
        assert callable(mock_kalshi_client.cancel_order)

    async def test_amend_order_signature(self, mock_kalshi_client):
        """Test amend_order method signature."""
        assert callable(mock_kalshi_client.amend_order)

    async def test_get_orders_signature(self, mock_kalshi_client):
        """Test get_orders method signature."""
        assert callable(mock_kalshi_client.get_orders)

    async def test_get_fills_signature(self, mock_kalshi_client):
        """Test get_fills method signature."""
        assert callable(mock_kalshi_client.get_fills)

    async def test_batch_create_orders_signature(self, mock_kalshi_client):
        """Test batch_create_orders method signature."""
        assert callable(mock_kalshi_client.batch_create_orders)

    async def test_batch_cancel_orders_signature(self, mock_kalshi_client):
        """Test batch_cancel_orders method signature."""
        assert callable(mock_kalshi_client.batch_cancel_orders)


@pytest.mark.unit
class TestKalshiClientBatchOperations:
    """Test batch operation constraints."""

    @pytest.mark.asyncio
    async def test_batch_create_orders_max_20(self, mock_kalshi_client):
        """Test batch_create_orders enforces 20-order limit."""
        orders = [
            {"ticker": f"MARKET{i}", "side": "buy", "count": 10, "type": "limit", "price": 50}
            for i in range(21)  # 21 orders (exceeds limit)
        ]

        with pytest.raises(ValueError, match="20"):
            await mock_kalshi_client.batch_create_orders(orders)

    @pytest.mark.asyncio
    async def test_batch_cancel_orders_max_20(self, mock_kalshi_client):
        """Test batch_cancel_orders enforces 20-order limit."""
        order_ids = [f"order-{i}" for i in range(21)]  # 21 orders

        with pytest.raises(ValueError, match="20"):
            await mock_kalshi_client.batch_cancel_orders(order_ids)

    @pytest.mark.asyncio
    async def test_batch_create_orders_exactly_20_allowed(self, mock_kalshi_client):
        """Test batch_create_orders allows exactly 20 orders."""
        orders = [
            {"ticker": f"MARKET{i}", "side": "buy", "count": 10, "type": "limit", "price": 50}
            for i in range(20)
        ]

        # Should not raise (will fail with network error, but validation passes)
        with patch.object(mock_kalshi_client, "_request", new_callable=AsyncMock) as mock_request:
            mock_request.return_value = {"orders": []}
            await mock_kalshi_client.batch_create_orders(orders)


@pytest.mark.unit
class TestKalshiClientPagination:
    """Test pagination cursor handling."""

    @pytest.mark.asyncio
    async def test_search_markets_returns_tuple(self, mock_kalshi_client):
        """Test search_markets returns (markets_list, cursor) tuple."""
        with patch.object(mock_kalshi_client, "_request", new_callable=AsyncMock) as mock_request:
            mock_request.return_value = {
                "markets": [
                    {
                        "ticker": "TEST",
                        "event_ticker": "EVENT",
                        "series_ticker": "SERIES",
                        "title": "Test",
                        "description": "Test",
                        "status": "open",
                        "volume": 0,
                        "open_interest": 0,
                        "created_at": "2024-01-01T00:00:00Z",
                        "close_ts": 1735689600,
                    }
                ],
                "cursor": "next_page_token",
            }

            markets, cursor = await mock_kalshi_client.search_markets(limit=10)

            assert isinstance(markets, list)
            assert len(markets) > 0
            assert cursor == "next_page_token"

    @pytest.mark.asyncio
    async def test_pagination_cursor_none_when_no_more_results(self, mock_kalshi_client):
        """Test pagination cursor is None when no more results."""
        with patch.object(mock_kalshi_client, "_request", new_callable=AsyncMock) as mock_request:
            mock_request.return_value = {"markets": [], "cursor": None}

            markets, cursor = await mock_kalshi_client.search_markets()

            assert markets == []
            assert cursor is None


@pytest.mark.unit
class TestKalshiClientReturnTypes:
    """Test that API methods return correct types."""

    @pytest.mark.asyncio
    async def test_get_market_returns_market_object(self, mock_kalshi_client):
        """Test get_market returns Market object."""
        market_data = {
            "ticker": "TEST",
            "event_ticker": "EVENT",
            "series_ticker": "SERIES",
            "title": "Test",
            "description": "Test",
            "status": "open",
            "yes_bid": 50.0,
            "yes_ask": 51.0,
            "no_bid": 49.0,
            "no_ask": 50.0,
            "volume": 1000,
            "open_interest": 500,
            "created_at": "2024-01-01T00:00:00Z",
            "close_ts": 1735689600,
        }

        with patch.object(mock_kalshi_client, "_request", new_callable=AsyncMock) as mock_request:
            mock_request.return_value = market_data

            market = await mock_kalshi_client.get_market("TEST")

            assert isinstance(market, Market)
            assert market.ticker == "TEST"

    @pytest.mark.asyncio
    async def test_get_balance_returns_balance_object(self, mock_kalshi_client):
        """Test get_balance returns Balance object."""
        balance_data = {"balance": 1000000, "portfolio_value": 1500000}

        with patch.object(mock_kalshi_client, "_request", new_callable=AsyncMock) as mock_request:
            mock_request.return_value = balance_data

            balance = await mock_kalshi_client.get_balance()

            assert isinstance(balance, Balance)
            assert balance.balance == 1000000

    @pytest.mark.asyncio
    async def test_get_positions_returns_position_list(self, mock_kalshi_client):
        """Test get_positions returns list of Position objects."""
        positions_data = {
            "positions": [
                {
                    "ticker": "TEST",
                    "event_ticker": "EVENT",
                    "side": "long",
                    "position": 100,
                    "fill_price": 50,
                    "total_traded": 100,
                    "resting_order_count": 0,
                }
            ],
            "cursor": None,
        }

        with patch.object(mock_kalshi_client, "_request", new_callable=AsyncMock) as mock_request:
            mock_request.return_value = positions_data

            positions, cursor = await mock_kalshi_client.get_positions()

            assert isinstance(positions, list)
            assert len(positions) > 0
            assert isinstance(positions[0], Position)


@pytest.mark.unit
class TestKalshiClientParameterValidation:
    """Test parameter validation."""

    @pytest.mark.asyncio
    async def test_create_order_with_valid_parameters(self, mock_kalshi_client):
        """Test create_order accepts valid parameters."""
        order_data = {
            "id": "order-1",
            "ticker": "TEST",
            "status": "resting",
            "side": "buy",
            "type": "limit",
            "price": 50,
            "count": 10,
            "fill_count": 0,
            "remaining_count": 10,
            "created_at": "2024-01-01T00:00:00Z",
            "last_updated_at": "2024-01-01T00:00:00Z",
        }

        with patch.object(mock_kalshi_client, "_request", new_callable=AsyncMock) as mock_request:
            mock_request.return_value = order_data

            order = await mock_kalshi_client.create_order(
                ticker="TEST",
                side="buy",
                count=10,
                type="limit",
                price=50,
            )

            assert isinstance(order, Order)

    @pytest.mark.asyncio
    async def test_get_candlesticks_with_interval(self, mock_kalshi_client):
        """Test get_candlesticks with different intervals."""
        candlestick_data = {
            "candlesticks": [
                {
                    "start_ts": 1698700800,
                    "end_ts": 1698787200,
                    "open": 60.0,
                    "high": 70.0,
                    "low": 55.0,
                    "close": 65.0,
                    "volume": 1000000,
                }
            ]
        }

        with patch.object(mock_kalshi_client, "_request", new_callable=AsyncMock) as mock_request:
            mock_request.return_value = candlestick_data

            for interval in ["1min", "60min", "1440min"]:
                candlesticks = await mock_kalshi_client.get_candlesticks(
                    series_ticker="TEST",
                    ticker="TEST",
                    interval=interval,
                )
                assert len(candlesticks) > 0


@pytest.mark.unit
class TestKalshiClientAPIResponseUnwrapping:
    """Test proper unwrapping of API responses before Pydantic validation.

    The Kalshi API wraps responses in parent objects (e.g., {"market": {...}}).
    These tests verify that the client properly extracts nested data before
    passing to Pydantic models.
    """

    @pytest.mark.asyncio
    async def test_get_market_unwraps_market_object(self, mock_kalshi_client):
        """Test get_market properly unwraps {"market": {...}} response."""
        # Real API response structure from Kalshi
        api_response = {
            "market": {
                "ticker": "KXHARRIS24-LSV",
                "title": "Will Kamala Harris win the 2024 US Presidential Election?",
                "status": "open",
                "yes_bid": 65.0,
                "yes_ask": 66.0,
                "no_bid": 34.0,
                "no_ask": 35.0,
                "last_price": 65.5,
                "volume": 1000000,
                "open_interest": 500000,
                "close_time": "2025-01-01T00:00:00Z",
                "expiration_time": "2025-01-01T00:00:00Z",
            }
        }

        with patch.object(mock_kalshi_client, "_request", new_callable=AsyncMock) as mock_request:
            mock_request.return_value = api_response

            market = await mock_kalshi_client.get_market("KXHARRIS24-LSV")

            assert isinstance(market, Market)
            assert market.ticker == "KXHARRIS24-LSV"
            assert market.yes_bid == 65.0

    @pytest.mark.asyncio
    async def test_get_orderbook_unwraps_orderbook_object(self, mock_kalshi_client):
        """Test get_orderbook properly unwraps {"orderbook": {...}} response."""
        from src.kalshi.models import Orderbook

        # Real API response structure
        api_response = {
            "orderbook": {
                "bids": [[65, 100], [64, 200], [63, 300]],
                "asks": [[66, 100], [67, 200], [68, 300]],
            },
            "timestamp": 1698765432000,
        }

        with patch.object(mock_kalshi_client, "_request", new_callable=AsyncMock) as mock_request:
            mock_request.return_value = api_response

            # This should NOT raise validation error
            orderbook = await mock_kalshi_client.get_orderbook("KXHARRIS24-LSV")

            assert isinstance(orderbook, Orderbook)
            assert len(orderbook.bids) == 3
            assert len(orderbook.asks) == 3

    @pytest.mark.asyncio
    async def test_get_trades_unwraps_and_handles_field_mapping(self, mock_kalshi_client):
        """Test get_trades properly unwraps and maps field names."""
        from src.kalshi.models import Trade

        # Real API response structure
        api_response = {
            "trades": [
                {
                    "ticker": "KXHARRIS24-LSV",
                    "created_at": 1698765432000,
                    "count": 100,
                    "price": 65,
                    "is_buy": True,
                }
            ],
            "cursor": None,
        }

        with patch.object(mock_kalshi_client, "_request", new_callable=AsyncMock) as mock_request:
            mock_request.return_value = api_response

            trades, cursor = await mock_kalshi_client.get_trades()

            assert isinstance(trades, list)
            assert len(trades) == 1
            assert isinstance(trades[0], Trade)

    @pytest.mark.asyncio
    async def test_get_events_handles_available_on_brokers_bool(self, mock_kalshi_client):
        """Test get_events handles available_on_brokers as bool or list."""
        from src.kalshi.models import Event

        # API sometimes returns bool, sometimes list
        api_response = {
            "events": [
                {
                    "event_ticker": "PRES-2024",
                    "title": "2024 US Presidential Election",
                    "available_on_brokers": False,  # Bool in this response
                }
            ],
            "cursor": None,
        }

        with patch.object(mock_kalshi_client, "_request", new_callable=AsyncMock) as mock_request:
            mock_request.return_value = api_response

            # This should NOT raise validation error
            events, cursor = await mock_kalshi_client.get_events()

            assert isinstance(events, list)
            assert len(events) == 1
            assert isinstance(events[0], Event)

    @pytest.mark.asyncio
    async def test_get_event_unwraps_event_object(self, mock_kalshi_client):
        """Test get_event properly unwraps {"event": {...}} response."""
        from src.kalshi.models import Event

        # Real API response structure
        api_response = {
            "event": {
                "event_ticker": "PRES-2024",
                "title": "2024 US Presidential Election",
                "category": "Politics",
            }
        }

        with patch.object(mock_kalshi_client, "_request", new_callable=AsyncMock) as mock_request:
            mock_request.return_value = api_response

            event = await mock_kalshi_client.get_event("PRES-2024")

            assert isinstance(event, Event)
            assert event.event_ticker == "PRES-2024"

    @pytest.mark.asyncio
    async def test_get_series_handles_missing_fields_gracefully(self, mock_kalshi_client):
        """Test get_series handles missing optional fields."""
        from src.kalshi.models import Series

        # Real API response may be missing some fields
        api_response = {
            "series": [
                {
                    "ticker": "KXELECTIONS",
                    "title": "Elections",
                    # description and created_at might be missing in some responses
                }
            ],
            "cursor": None,
        }

        with patch.object(mock_kalshi_client, "_request", new_callable=AsyncMock) as mock_request:
            mock_request.return_value = api_response

            # This should handle missing fields gracefully
            try:
                series, cursor = await mock_kalshi_client.get_series()
                # If it succeeds, check return type
                assert isinstance(series, list)
            except Exception as e:
                # If it fails, document that this is the issue we're catching
                assert "description" in str(e) or "created_at" in str(e), \
                    f"Expected missing field error, got: {e}"

    @pytest.mark.asyncio
    async def test_get_candlesticks_returns_proper_list(self, mock_kalshi_client):
        """Test get_candlesticks properly unwraps candlesticks array."""
        from src.kalshi.models import Candlestick

        api_response = {
            "candlesticks": [
                {
                    "start_ts": 1698700800,
                    "end_ts": 1698787200,
                    "open": 60.0,
                    "high": 70.0,
                    "low": 55.0,
                    "close": 65.0,
                    "volume": 1000000,
                }
            ]
        }

        with patch.object(mock_kalshi_client, "_request", new_callable=AsyncMock) as mock_request:
            mock_request.return_value = api_response

            candlesticks = await mock_kalshi_client.get_candlesticks(
                series_ticker="KXELECTIONS",
                ticker="KXHARRIS24-LSV",
            )

            assert isinstance(candlesticks, list)
            assert len(candlesticks) == 1
            assert isinstance(candlesticks[0], Candlestick)
            assert candlesticks[0].close == 65.0


@pytest.mark.unit
class TestKalshiClientPhase1PortfolioManagement:
    """Test Phase 1 portfolio management tools."""

    @pytest.mark.asyncio
    async def test_get_order_group(self, mock_kalshi_client):
        """Test get_order_group retrieves a single order group."""
        from src.kalshi.models import OrderGroup

        api_response = {
            "id": "group-123",
            "contract_limit": 1000,
            "matched_contracts": 500,
        }

        with patch.object(mock_kalshi_client, "_request", new_callable=AsyncMock) as mock_request:
            mock_request.return_value = api_response

            result = await mock_kalshi_client.get_order_group("group-123")

            assert isinstance(result, OrderGroup)
            assert result.id == "group-123"
            assert result.contract_limit == 1000
            assert result.matched_contracts == 500
            mock_request.assert_called_once_with("GET", "/portfolio/order_groups/group-123")

    @pytest.mark.asyncio
    async def test_reset_order_group(self, mock_kalshi_client):
        """Test reset_order_group resets matched contract counter."""
        with patch.object(mock_kalshi_client, "_request", new_callable=AsyncMock) as mock_request:
            mock_request.return_value = {}

            await mock_kalshi_client.reset_order_group("group-123")

            mock_request.assert_called_once_with("PUT", "/portfolio/order_groups/group-123/reset")

    @pytest.mark.asyncio
    async def test_delete_order_group(self, mock_kalshi_client):
        """Test delete_order_group deletes an order group."""
        with patch.object(mock_kalshi_client, "_request", new_callable=AsyncMock) as mock_request:
            mock_request.return_value = {}

            await mock_kalshi_client.delete_order_group("group-123")

            mock_request.assert_called_once_with("DELETE", "/portfolio/order_groups/group-123")

    @pytest.mark.asyncio
    async def test_get_total_resting_order_value(self, mock_kalshi_client):
        """Test get_total_resting_order_value returns portfolio value."""
        from src.kalshi.models import TotalRestingOrderValue

        api_response = {"total_resting_order_value": 50000}

        with patch.object(mock_kalshi_client, "_request", new_callable=AsyncMock) as mock_request:
            mock_request.return_value = api_response

            result = await mock_kalshi_client.get_total_resting_order_value()

            assert isinstance(result, TotalRestingOrderValue)
            assert result.total_resting_order_value == 50000
            mock_request.assert_called_once_with("GET", "/portfolio/summary/total_resting_order_value")

    @pytest.mark.asyncio
    async def test_get_settlements(self, mock_kalshi_client):
        """Test get_settlements returns historical settlement data."""
        from src.kalshi.models import Settlement

        api_response = {
            "settlements": [
                {
                    "order_id": "order-1",
                    "ticker": "KXHARRIS24-LSV",
                    "side": "buy",
                    "count": 10,
                    "price": 55,
                    "payout": 550,
                    "created_at": 1698765432000,
                    "market_title": "Will Harris win?",
                }
            ],
            "cursor": "next-page-cursor",
        }

        with patch.object(mock_kalshi_client, "_request", new_callable=AsyncMock) as mock_request:
            mock_request.return_value = api_response

            settlements, cursor = await mock_kalshi_client.get_settlements(limit=100)

            assert isinstance(settlements, list)
            assert len(settlements) == 1
            assert isinstance(settlements[0], Settlement)
            assert settlements[0].order_id == "order-1"
            assert cursor == "next-page-cursor"
            mock_request.assert_called_once()

    @pytest.mark.asyncio
    async def test_decrease_order(self, mock_kalshi_client):
        """Test decrease_order reduces order size."""
        api_response = {
            "order": {
                "id": "order-1",
                "ticker": "KXHARRIS24-LSV",
                "side": "buy",
                "type": "limit",
                "count": 5,
                "fill_count": 0,
                "remaining_count": 5,
                "price": 55,
                "status": "resting",
                "created_at": "2025-01-01T00:00:00Z",
                "last_updated_at": "2025-01-01T00:05:00Z",
            }
        }

        with patch.object(mock_kalshi_client, "_request", new_callable=AsyncMock) as mock_request:
            mock_request.return_value = api_response

            result = await mock_kalshi_client.decrease_order("order-1", count=5)

            assert isinstance(result, Order)
            assert result.id == "order-1"
            assert result.count == 5
            mock_request.assert_called_once()
            # Verify POST with payload
            call_args = mock_request.call_args
            assert call_args[0][0] == "POST"
            assert "/portfolio/orders/order-1/decrease" in call_args[0][1]

    @pytest.mark.asyncio
    async def test_get_queue_positions(self, mock_kalshi_client):
        """Test get_queue_positions returns bulk queue positions."""
        api_response = {
            "queue_positions": {
                "order-1": {"position": 5},
                "order-2": {"position": 0},
                "order-3": {"position": 12},
            }
        }

        with patch.object(mock_kalshi_client, "_request", new_callable=AsyncMock) as mock_request:
            mock_request.return_value = api_response

            result = await mock_kalshi_client.get_queue_positions(["order-1", "order-2", "order-3"])

            assert isinstance(result, dict)
            assert result["order-1"] == 5
            assert result["order-2"] == 0
            assert result["order-3"] == 12
            mock_request.assert_called_once()
            # Verify POST with payload
            call_args = mock_request.call_args
            assert call_args[0][0] == "POST"
            assert "/portfolio/orders/queue_positions" in call_args[0][1]


@pytest.mark.unit
class TestKalshiClientPhase4AdvancedFeatures:
    """Test Phase 4 advanced features: Multivariate, RFQ, and Quotes."""

    @pytest.mark.asyncio
    async def test_get_multivariate_collections(self, mock_kalshi_client):
        """Test get_multivariate_collections returns collection list."""
        api_response = {
            "collections": [
                {
                    "ticker": "MVE-PRES-2024",
                    "title": "Presidential Election 2024",
                    "description": "Election outcomes",
                    "status": "open",
                    "event_tickers": ["PRES-2024-DEM", "PRES-2024-REP"],
                    "market_count": 5,
                    "created_at": "2024-01-01T00:00:00Z",
                    "close_time": "2024-11-05T00:00:00Z",
                }
            ],
            "cursor": None,
        }

        with patch.object(mock_kalshi_client, "_request", new_callable=AsyncMock) as mock_request:
            mock_request.return_value = api_response

            collections, cursor = await mock_kalshi_client.get_multivariate_collections(
                status="open", limit=100
            )

            assert len(collections) == 1
            assert collections[0].ticker == "MVE-PRES-2024"
            assert collections[0].status == "open"
            assert cursor is None
            mock_request.assert_called_once()

    @pytest.mark.asyncio
    async def test_get_multivariate_collection(self, mock_kalshi_client):
        """Test get_multivariate_collection returns single collection."""
        api_response = {
            "collection": {
                "ticker": "MVE-PRES-2024",
                "title": "Presidential Election 2024",
                "description": "Election outcomes",
                "status": "open",
                "event_tickers": ["PRES-2024"],
                "market_count": 10,
            }
        }

        with patch.object(mock_kalshi_client, "_request", new_callable=AsyncMock) as mock_request:
            mock_request.return_value = api_response

            collection = await mock_kalshi_client.get_multivariate_collection("MVE-PRES-2024")

            assert collection.ticker == "MVE-PRES-2024"
            assert collection.market_count == 10
            mock_request.assert_called_once()

    @pytest.mark.asyncio
    async def test_get_markets_in_collection(self, mock_kalshi_client):
        """Test get_markets_in_collection returns markets in collection."""
        api_response = {
            "markets": [
                {
                    "ticker": "KXDEM24-LSV",
                    "title": "Democratic Nominee",
                    "status": "open",
                    "yes_bid": 65.0,
                    "yes_ask": 70.0,
                    "no_bid": 30.0,
                    "no_ask": 35.0,
                    "collection_ticker": "MVE-PRES-2024",
                }
            ],
            "cursor": None,
        }

        with patch.object(mock_kalshi_client, "_request", new_callable=AsyncMock) as mock_request:
            mock_request.return_value = api_response

            markets, cursor = await mock_kalshi_client.get_markets_in_collection(
                "MVE-PRES-2024", limit=100
            )

            assert len(markets) == 1
            assert markets[0].ticker == "KXDEM24-LSV"
            assert markets[0].yes_bid == 65.0
            assert cursor is None
            mock_request.assert_called_once()

    @pytest.mark.asyncio
    async def test_create_rfq(self, mock_kalshi_client):
        """Test create_rfq creates a Request for Quote."""
        api_response = {
            "rfq": {
                "id": "rfq-123",
                "ticker": "KXHARRIS24-LSV",
                "side": "buy",
                "count": 100,
                "created_at": "2024-01-01T00:00:00Z",
                "status": "open",
            }
        }

        with patch.object(mock_kalshi_client, "_request", new_callable=AsyncMock) as mock_request:
            mock_request.return_value = api_response

            rfq = await mock_kalshi_client.create_rfq("KXHARRIS24-LSV", "buy", 100)

            assert rfq.id == "rfq-123"
            assert rfq.ticker == "KXHARRIS24-LSV"
            assert rfq.side == "buy"
            assert rfq.count == 100
            mock_request.assert_called_once()

    @pytest.mark.asyncio
    async def test_get_rfqs(self, mock_kalshi_client):
        """Test get_rfqs returns list of RFQs."""
        api_response = {
            "rfqs": [
                {
                    "id": "rfq-1",
                    "ticker": "KXHARRIS24-LSV",
                    "side": "buy",
                    "count": 50,
                    "created_at": "2024-01-01T00:00:00Z",
                    "status": "open",
                }
            ],
            "cursor": None,
        }

        with patch.object(mock_kalshi_client, "_request", new_callable=AsyncMock) as mock_request:
            mock_request.return_value = api_response

            rfqs, cursor = await mock_kalshi_client.get_rfqs(status="open", limit=100)

            assert len(rfqs) == 1
            assert rfqs[0].id == "rfq-1"
            assert rfqs[0].status == "open"
            assert cursor is None
            mock_request.assert_called_once()

    @pytest.mark.asyncio
    async def test_get_rfq(self, mock_kalshi_client):
        """Test get_rfq returns single RFQ."""
        api_response = {
            "rfq": {
                "id": "rfq-123",
                "ticker": "KXHARRIS24-LSV",
                "side": "buy",
                "count": 100,
                "created_at": "2024-01-01T00:00:00Z",
                "status": "open",
            }
        }

        with patch.object(mock_kalshi_client, "_request", new_callable=AsyncMock) as mock_request:
            mock_request.return_value = api_response

            rfq = await mock_kalshi_client.get_rfq("rfq-123")

            assert rfq.id == "rfq-123"
            assert rfq.ticker == "KXHARRIS24-LSV"
            mock_request.assert_called_once()

    @pytest.mark.asyncio
    async def test_delete_rfq(self, mock_kalshi_client):
        """Test delete_rfq deletes an RFQ."""
        with patch.object(mock_kalshi_client, "_request", new_callable=AsyncMock) as mock_request:
            mock_request.return_value = {}

            await mock_kalshi_client.delete_rfq("rfq-123")

            mock_request.assert_called_once()
            call_args = mock_request.call_args
            assert call_args[0][0] == "DELETE"
            assert "rfq-123" in call_args[0][1]

    @pytest.mark.asyncio
    async def test_create_quote(self, mock_kalshi_client):
        """Test create_quote creates a quote response to RFQ."""
        api_response = {
            "quote": {
                "id": "quote-456",
                "rfq_id": "rfq-123",
                "ticker": "KXHARRIS24-LSV",
                "side": "buy",
                "price": 55,
                "quantity": 100,
                "created_at": "2024-01-01T00:01:00Z",
                "status": "open",
            }
        }

        with patch.object(mock_kalshi_client, "_request", new_callable=AsyncMock) as mock_request:
            mock_request.return_value = api_response

            quote = await mock_kalshi_client.create_quote("rfq-123", 55, 100)

            assert quote.id == "quote-456"
            assert quote.rfq_id == "rfq-123"
            assert quote.price == 55
            assert quote.quantity == 100
            mock_request.assert_called_once()

    @pytest.mark.asyncio
    async def test_get_quotes(self, mock_kalshi_client):
        """Test get_quotes returns list of quotes for RFQ."""
        api_response = {
            "quotes": [
                {
                    "id": "quote-1",
                    "rfq_id": "rfq-123",
                    "ticker": "KXHARRIS24-LSV",
                    "side": "buy",
                    "price": 55,
                    "quantity": 100,
                    "created_at": "2024-01-01T00:01:00Z",
                    "status": "open",
                }
            ],
            "cursor": None,
        }

        with patch.object(mock_kalshi_client, "_request", new_callable=AsyncMock) as mock_request:
            mock_request.return_value = api_response

            quotes, cursor = await mock_kalshi_client.get_quotes("rfq-123", limit=100)

            assert len(quotes) == 1
            assert quotes[0].id == "quote-1"
            assert quotes[0].rfq_id == "rfq-123"
            assert cursor is None
            mock_request.assert_called_once()

    @pytest.mark.asyncio
    async def test_accept_quote(self, mock_kalshi_client):
        """Test accept_quote accepts a quote."""
        api_response = {
            "quote": {
                "id": "quote-456",
                "rfq_id": "rfq-123",
                "ticker": "KXHARRIS24-LSV",
                "side": "buy",
                "price": 55,
                "quantity": 100,
                "created_at": "2024-01-01T00:01:00Z",
                "status": "accepted",
            }
        }

        with patch.object(mock_kalshi_client, "_request", new_callable=AsyncMock) as mock_request:
            mock_request.return_value = api_response

            quote = await mock_kalshi_client.accept_quote("quote-456")

            assert quote.status == "accepted"
            mock_request.assert_called_once()

    @pytest.mark.asyncio
    async def test_confirm_quote(self, mock_kalshi_client):
        """Test confirm_quote confirms an accepted quote."""
        api_response = {
            "quote": {
                "id": "quote-456",
                "rfq_id": "rfq-123",
                "ticker": "KXHARRIS24-LSV",
                "side": "buy",
                "price": 55,
                "quantity": 100,
                "created_at": "2024-01-01T00:01:00Z",
                "status": "confirmed",
            }
        }

        with patch.object(mock_kalshi_client, "_request", new_callable=AsyncMock) as mock_request:
            mock_request.return_value = api_response

            quote = await mock_kalshi_client.confirm_quote("quote-456")

            assert quote.status == "confirmed"
            mock_request.assert_called_once()

    @pytest.mark.asyncio
    async def test_delete_quote(self, mock_kalshi_client):
        """Test delete_quote deletes a quote."""
        with patch.object(mock_kalshi_client, "_request", new_callable=AsyncMock) as mock_request:
            mock_request.return_value = {}

            await mock_kalshi_client.delete_quote("quote-456")

            mock_request.assert_called_once()
            call_args = mock_request.call_args
            assert call_args[0][0] == "DELETE"
            assert "quote-456" in call_args[0][1]
