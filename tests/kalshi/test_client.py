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
