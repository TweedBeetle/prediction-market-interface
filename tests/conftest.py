"""Shared test fixtures and pytest configuration."""

import os
import time
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock

import pytest
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend


# ========== RSA KEY FIXTURES ==========


@pytest.fixture(scope="session")
def test_private_key():
    """Generate RSA key pair for testing (session-scoped for performance)."""
    return rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend(),
    )


@pytest.fixture(scope="session")
def test_public_key(test_private_key):
    """Extract public key from private key."""
    return test_private_key.public_key()


@pytest.fixture
def test_private_key_pem(test_private_key, tmp_path):
    """Write test private key to PEM file."""
    key_path = tmp_path / "test_private_key.pem"
    key_path.write_bytes(
        test_private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        )
    )
    return str(key_path)


# ========== KALSHI CLIENT FIXTURES ==========


@pytest.fixture
def mock_kalshi_client(test_private_key_pem, monkeypatch):
    """Create KalshiClient with test credentials."""
    # Set environment variables
    monkeypatch.setenv("KALSHI_API_KEY_ID", "test-key-id-550e8400-e29b-41d4-a716-446655440000")
    monkeypatch.setenv("KALSHI_PRIVATE_KEY_PATH", test_private_key_pem)

    from src.kalshi import KalshiClient

    return KalshiClient()


@pytest.fixture
async def async_mock_kalshi_client(test_private_key_pem, monkeypatch):
    """Async-compatible KalshiClient fixture with cleanup."""
    monkeypatch.setenv("KALSHI_API_KEY_ID", "test-key-id-550e8400-e29b-41d4-a716-446655440000")
    monkeypatch.setenv("KALSHI_PRIVATE_KEY_PATH", test_private_key_pem)

    from src.kalshi import KalshiClient

    client = KalshiClient()
    yield client
    # Cleanup if needed (close connections, etc.)


# ========== FASTMCP SERVER FIXTURES ==========


@pytest.fixture
def kalshi_mcp_server():
    """Create FastMCP server for testing."""
    from src.kalshi.kalshi_mcp_server import mcp

    return mcp


# ========== VCR CONFIGURATION ==========


@pytest.fixture(scope="module")
def vcr_config():
    """VCR.py configuration for recording API responses."""
    return {
        "filter_headers": [
            "KALSHI-ACCESS-KEY",
            "KALSHI-ACCESS-SIGNATURE",
            "KALSHI-ACCESS-TIMESTAMP",
            "authorization",
        ],
        "record_mode": "once",  # Record on first run, use cassette on subsequent runs
        "match_on": ["method", "scheme", "host", "port", "path", "query"],
        "cassette_library_dir": str(Path(__file__).parent / "cassettes"),
    }


@pytest.fixture(scope="function")
def vcr_cassette_path(request, tmp_path):
    """Auto-expire VCR cassettes after TTL."""
    cassette_dir = Path(__file__).parent / "cassettes" / "kalshi"
    cassette_dir.mkdir(parents=True, exist_ok=True)

    cassette_name = request.node.name
    cassette_path = cassette_dir / f"{cassette_name}.yaml"

    if cassette_path.exists():
        ttl_days = int(os.getenv("VCR_TTL_DAYS", "7"))

        if ttl_days == 0:
            # Force refresh
            cassette_path.unlink()
        elif ttl_days > 0:
            # Check age
            age_seconds = time.time() - cassette_path.stat().st_mtime
            age_days = age_seconds / 86400

            if age_days > ttl_days:
                # Expired - delete for re-recording
                cassette_path.unlink()

    return str(cassette_path)


# ========== PYTEST CONFIGURATION ==========


def pytest_configure(config):
    """Configure pytest with custom markers."""
    config.addinivalue_line("markers", "unit: Unit tests (no external dependencies)")
    config.addinivalue_line("markers", "integration: Integration tests (external APIs)")
    config.addinivalue_line("markers", "auth: Authentication tests")
    config.addinivalue_line("markers", "vcr: Tests using VCR.py cassettes")
    config.addinivalue_line("markers", "slow: Slow tests")


# ========== PYDANTIC MODEL FIXTURES ==========


@pytest.fixture
def sample_market():
    """Sample Market object for testing."""
    from src.kalshi.models import Market, MarketStatus

    return Market(
        ticker="KXHARRIS24-LSV",
        title="Will Kamala Harris win the 2024 US Presidential Election?",
        status=MarketStatus.OPEN,
        event_ticker="PRES-2024-HARRIS",
        mve_collection_ticker=None,
        yes_bid=65.0,
        yes_ask=66.0,
        no_bid=34.0,
        no_ask=35.0,
        last_price=65.5,
        volume=1000000,
        volume_24h=50000,
        open_interest=500000,
        close_time="2025-01-01T00:00:00Z",
        expiration_time="2025-01-01T00:00:00Z",
    )


@pytest.fixture
def sample_order():
    """Sample Order object for testing."""
    from src.kalshi.models import Order, OrderSide, OrderType, OrderStatus

    return Order(
        id="order-123",
        ticker="KXHARRIS24-LSV",
        status=OrderStatus.RESTING,
        side=OrderSide.BUY,
        type=OrderType.LIMIT,
        price=65,
        count=100,
        fill_count=0,
        remaining_count=100,
        created_at="2024-11-01T12:00:00Z",
        last_updated_at="2024-11-01T12:00:00Z",
    )


@pytest.fixture
def sample_position():
    """Sample Position object for testing."""
    from src.kalshi.models import Position

    return Position(
        ticker="KXHARRIS24-LSV",
        event_ticker="PRES-2024-HARRIS",
        side="long",
        position=100,
        fill_price=65,
        total_traded=100,
        resting_order_count=0,
    )


@pytest.fixture
def sample_balance():
    """Sample Balance object for testing."""
    from src.kalshi.models import Balance

    return Balance(
        balance=1000000,  # $10,000 in cents
        portfolio_value=1500000,  # $15,000 in cents
    )


@pytest.fixture
def sample_fill():
    """Sample Fill object for testing."""
    from src.kalshi.models import Fill

    return Fill(
        market_ticker="KXHARRIS24-LSV",
        order_id="order-123",
        is_buy=True,
        quantity=100,
        price=65.0,
        timestamp=1698765432,
    )


@pytest.fixture
def sample_candlestick():
    """Sample Candlestick object for testing."""
    from src.kalshi.models import Candlestick

    return Candlestick(
        start_ts=1698700800,  # 2023-11-01 00:00:00 UTC
        end_ts=1698787200,  # 2023-11-02 00:00:00 UTC
        open=60.0,
        high=70.0,
        low=55.0,
        close=65.0,
        volume=1000000,
    )


@pytest.fixture
def sample_orderbook():
    """Sample Orderbook object for testing."""
    from src.kalshi.models import Orderbook

    return Orderbook(
        ticker="KXHARRIS24-LSV",
        bids=[(65.0, 1000), (64.0, 500), (63.0, 250)],
        asks=[(66.0, 1000), (67.0, 500), (68.0, 250)],
        timestamp=1698765432000,
    )
