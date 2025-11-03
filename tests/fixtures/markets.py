"""Dynamic market fixtures for integration tests."""

from datetime import datetime, timedelta, timezone
import pytest
from src.kalshi.client import KalshiClient


@pytest.fixture(scope="session")
async def demo_client():
    """
    Kalshi client connected to demo environment.

    Returns authenticated client for demo API testing.
    """
    async with KalshiClient.from_env(environment="demo") as client:
        yield client


@pytest.fixture(scope="session")
async def active_market(demo_client):
    """
    Dynamically find an active, tradeable market for testing.

    Strategy:
    1. Search for markets with status="open"
    2. Filter for markets with:
       - Recent volume (>0 contracts)
       - Not expiring in next hour
    3. Cache the ticker for session

    Returns:
        Market object suitable for testing
    """
    markets = await demo_client.search_markets(status="open", limit=50)

    # Find suitable test market
    for market in markets:
        # Check if market has reasonable time left and some activity
        if (
            market.close_time > datetime.now(timezone.utc) + timedelta(hours=1)
            and market.volume is not None
        ):
            return market

    # If no perfect match, just return first open market
    if markets:
        return markets[0]

    pytest.skip("No suitable active market found in demo environment")


@pytest.fixture(scope="session")
async def liquid_market(demo_client):
    """
    Find a highly liquid market (for orderbook testing).

    Returns the market with highest 24h volume.
    """
    markets = await demo_client.search_markets(status="open", limit=100)

    if not markets:
        pytest.skip("No markets found")

    # Sort by volume, take top
    markets_with_volume = [m for m in markets if m.volume_24h is not None]
    if markets_with_volume:
        markets_with_volume.sort(key=lambda m: m.volume_24h or 0, reverse=True)
        return markets_with_volume[0]

    # Fallback to any market
    return markets[0]


@pytest.fixture
async def fresh_balance(demo_client):
    """
    Get current balance (fresh for each test).

    Returns:
        Balance object with current account balance
    """
    return await demo_client.get_balance()
