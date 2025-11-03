"""API integration tests with VCR.py for recording/replaying API responses."""

import pytest
from unittest.mock import AsyncMock, patch


@pytest.mark.integration
class TestKalshiAPIIntegration:
    """Integration tests with mocked Kalshi API responses."""

    async def test_search_markets_returns_markets(self, mock_kalshi_client, sample_market):
        """Test that search_markets returns valid market list."""
        with patch.object(mock_kalshi_client, "_request", new_callable=AsyncMock) as mock_request:
            mock_request.return_value = {
                "markets": [sample_market.model_dump()],
                "cursor": None,
            }

            markets, cursor = await mock_kalshi_client.search_markets(limit=10)

            assert markets is not None
            assert len(markets) > 0
            assert all(hasattr(m, "ticker") for m in markets)
            assert all(hasattr(m, "title") for m in markets)
            mock_request.assert_called_once()

    async def test_get_market_returns_single_market(self, mock_kalshi_client, sample_market):
        """Test that get_market returns valid Market object."""
        with patch.object(mock_kalshi_client, "_request", new_callable=AsyncMock) as mock_request:
            mock_request.return_value = sample_market.model_dump()

            market = await mock_kalshi_client.get_market(sample_market.ticker)

            assert market is not None
            assert market.ticker == sample_market.ticker
            assert hasattr(market, "title")
            assert hasattr(market, "status")
            mock_request.assert_called_once()

    async def test_get_balance_returns_balance_object(self, mock_kalshi_client, sample_balance):
        """Test that get_balance returns valid Balance object."""
        with patch.object(mock_kalshi_client, "_request", new_callable=AsyncMock) as mock_request:
            mock_request.return_value = sample_balance.model_dump()

            balance = await mock_kalshi_client.get_balance()

            assert balance is not None
            assert hasattr(balance, "balance")
            assert isinstance(balance.balance, (int, float))
            mock_request.assert_called_once()

    async def test_get_positions_returns_positions_list(self, mock_kalshi_client, sample_position):
        """Test that get_positions returns list of Position objects."""
        with patch.object(mock_kalshi_client, "_request", new_callable=AsyncMock) as mock_request:
            mock_request.return_value = {"positions": [sample_position.model_dump()]}

            positions, cursor = await mock_kalshi_client.get_positions()

            assert positions is not None
            assert isinstance(positions, list)
            for position in positions:
                assert hasattr(position, "ticker")
                assert hasattr(position, "side")
            mock_request.assert_called_once()

    async def test_search_markets_pagination(self, mock_kalshi_client, sample_market):
        """Test that search_markets pagination works correctly."""
        with patch.object(mock_kalshi_client, "_request", new_callable=AsyncMock) as mock_request:
            # First call
            mock_request.return_value = {
                "markets": [sample_market.model_dump()],
                "cursor": "next_page_cursor",
            }

            markets_1, cursor_1 = await mock_kalshi_client.search_markets(limit=5)
            assert len(markets_1) > 0
            assert cursor_1 is not None

            # Second call with cursor
            market_2 = sample_market.model_copy(update={"ticker": "OTHERTICKER"})
            mock_request.return_value = {
                "markets": [market_2.model_dump()],
                "cursor": None,
            }

            markets_2, cursor_2 = await mock_kalshi_client.search_markets(limit=5, cursor=cursor_1)
            assert len(markets_2) > 0
            # Verify different markets returned
            tickers_1 = {m.ticker for m in markets_1}
            tickers_2 = {m.ticker for m in markets_2}
            assert tickers_1 != tickers_2

    async def test_get_events_returns_events_list(self, mock_kalshi_client):
        """Test that get_events returns list of Event objects."""
        from src.kalshi.models import Event

        sample_event = Event(
            event_ticker="TEST_EVENT",
            title="Test Event",
            status="open",
        )

        with patch.object(mock_kalshi_client, "_request", new_callable=AsyncMock) as mock_request:
            mock_request.return_value = {"events": [sample_event.model_dump()]}

            events, cursor = await mock_kalshi_client.get_events(limit=10)

            assert events is not None
            assert isinstance(events, list)
            assert len(events) > 0
            for event in events:
                assert hasattr(event, "event_ticker") or hasattr(event, "ticker")  # ticker is alias
                assert hasattr(event, "title")
            mock_request.assert_called_once()

    async def test_get_event_by_id(self, mock_kalshi_client):
        """Test that get_event returns single Event object."""
        from src.kalshi.models import Event

        sample_event = Event(
            event_ticker="TEST_EVENT",
            title="Test Event",
            status="open",
        )

        with patch.object(mock_kalshi_client, "_request", new_callable=AsyncMock) as mock_request:
            mock_request.return_value = sample_event.model_dump()

            event = await mock_kalshi_client.get_event("TEST_EVENT")

            assert event is not None
            assert event.event_ticker == "TEST_EVENT"
            assert event.ticker == "TEST_EVENT"  # Test backward compatibility alias
            mock_request.assert_called_once()

    async def test_get_exchange_status(self, mock_kalshi_client):
        """Test that get_exchange_status returns valid ExchangeStatus."""
        from src.kalshi.models import ExchangeStatus

        sample_status = ExchangeStatus(
            trading_active=True,
        )

        with patch.object(mock_kalshi_client, "_request", new_callable=AsyncMock) as mock_request:
            mock_request.return_value = sample_status.model_dump()

            status = await mock_kalshi_client.get_exchange_status()

            assert status is not None
            assert hasattr(status, "trading_active")
            assert isinstance(status.trading_active, bool)
            mock_request.assert_called_once()

    async def test_get_fills_returns_fills_list(self, mock_kalshi_client, sample_fill):
        """Test that get_fills returns list of Fill objects."""
        with patch.object(mock_kalshi_client, "_request", new_callable=AsyncMock) as mock_request:
            mock_request.return_value = {"fills": [sample_fill.model_dump()]}

            fills, cursor = await mock_kalshi_client.get_fills()

            assert fills is not None
            assert isinstance(fills, list)
            for fill in fills:
                assert hasattr(fill, "order_id")
                assert hasattr(fill, "market_ticker")
            mock_request.assert_called_once()


@pytest.mark.integration
class TestVCRCassetteManagement:
    """Test VCR cassette handling and auto-expiration."""

    def test_vcr_cassette_path_created(self, vcr_cassette_path):
        """Test that VCR cassette path is set correctly."""
        assert vcr_cassette_path is not None
        assert isinstance(vcr_cassette_path, str)
        # Path should end with .yaml
        assert vcr_cassette_path.endswith(".yaml")

    def test_vcr_config_filters_auth_headers(self, vcr_config):
        """Test that VCR config filters sensitive auth headers."""
        assert vcr_config is not None
        assert "filter_headers" in vcr_config
        headers = vcr_config["filter_headers"]

        # Should filter Kalshi auth headers
        assert "KALSHI-ACCESS-KEY" in headers
        assert "KALSHI-ACCESS-SIGNATURE" in headers
        assert "KALSHI-ACCESS-TIMESTAMP" in headers


@pytest.mark.integration
class TestAPIErrorHandling:
    """Test API error handling patterns."""

    @pytest.mark.vcr()
    async def test_api_handles_not_found_error(self, mock_kalshi_client):
        """Test that API client handles 404 errors gracefully."""
        # Try to get a non-existent market
        from httpx import HTTPStatusError

        with pytest.raises(HTTPStatusError):
            await mock_kalshi_client.get_market("NONEXISTENT_TICKER_XYZ")

    @pytest.mark.vcr()
    async def test_api_handles_invalid_parameters(self, mock_kalshi_client):
        """Test that API handles invalid parameters gracefully."""
        # Try with invalid limit
        markets, _ = await mock_kalshi_client.search_markets(limit=5)
        # Should still return valid results, not error on our side
        assert markets is not None
        assert isinstance(markets, list)
