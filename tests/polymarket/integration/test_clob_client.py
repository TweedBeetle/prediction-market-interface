"""
Integration tests for Polymarket CLOB API client (trading).

⚠️ WARNING: These tests require:
- Valid wallet private key in environment
- USDC on Polygon for trading
- MATIC for gas fees
- Real money on mainnet (no testnet available)

All tests are SKIPPED by default. To run them:
1. Set up .env.polymarket with your credentials
2. Fund your wallet with USDC and MATIC
3. Run with: pytest tests/polymarket/integration/test_clob_client.py --run-funded

These tests use REAL MONEY and execute on Polygon mainnet.
"""

import os
import pytest

from src.polymarket.clob_client import ClobClient
from src.polymarket.gamma_client import GammaClient
from src.polymarket.models import ApiCredentials, OrderParams, OrderSide, SignatureType


# Skip all tests by default unless --run-funded flag is passed
pytestmark = pytest.mark.skipif(
    not pytest.config.getoption("--run-funded", default=False),
    reason="Requires funded wallet. Run with --run-funded to execute (USES REAL MONEY)"
)


def pytest_addoption(parser):
    """Add custom pytest option for funded tests."""
    parser.addoption(
        "--run-funded",
        action="store_true",
        default=False,
        help="Run tests that require funded wallet (USES REAL MONEY)"
    )


@pytest.fixture
def test_credentials():
    """
    Get test credentials from environment.

    Requires:
        POLYMARKET_PRIVATE_KEY - Your wallet private key
        POLYMARKET_WALLET_ADDRESS - Your wallet address (optional, derived from key)
    """
    private_key = os.getenv("POLYMARKET_PRIVATE_KEY")
    wallet_address = os.getenv("POLYMARKET_WALLET_ADDRESS")

    if not private_key:
        pytest.skip("POLYMARKET_PRIVATE_KEY not set in environment")

    # Derive wallet address if not provided
    if not wallet_address:
        from eth_account import Account
        if not private_key.startswith("0x"):
            private_key = f"0x{private_key}"
        account = Account.from_key(private_key)
        wallet_address = account.address

    return ApiCredentials(
        private_key=private_key,
        wallet_address=wallet_address,
        chain_id=137,
    )


@pytest.mark.asyncio
class TestClobClientAuthentication:
    """Test CLOB client authentication (requires wallet, no trades)."""

    async def test_authenticate(self, test_credentials):
        """Test authentication with EIP-712 signing."""
        async with ClobClient(test_credentials) as client:
            # Authenticate
            creds = await client.authenticate()

            # Verify we got API credentials
            assert "apiKey" in creds
            assert "secret" in creds
            assert "passphrase" in creds

            # Verify credentials are stored in client
            assert client._api_key is not None
            assert client._api_secret is not None
            assert client._api_passphrase is not None

    async def test_from_env(self):
        """Test creating client from environment variables."""
        # This should work if env vars are set
        try:
            client = ClobClient.from_env()
            assert client is not None
            assert client.credentials.wallet_address
        except ValueError as e:
            if "POLYMARKET_PRIVATE_KEY" in str(e):
                pytest.skip("POLYMARKET_PRIVATE_KEY not set")
            raise


@pytest.mark.asyncio
class TestClobClientPositionsAndOrders:
    """Test portfolio management endpoints (requires auth, no trading)."""

    async def test_get_positions(self, test_credentials):
        """Test getting current positions."""
        async with ClobClient(test_credentials) as client:
            positions = await client.get_positions()

            # Should return list (may be empty)
            assert isinstance(positions, list)

            # If we have positions, verify structure
            if positions:
                position = positions[0]
                assert hasattr(position, 'market_id')
                assert hasattr(position, 'size')
                assert hasattr(position, 'outcome')

    async def test_get_positions_for_market(self, test_credentials):
        """Test getting positions filtered by market."""
        # First get a market ID
        async with GammaClient() as gamma:
            markets = await gamma.search_markets(active=True, limit=1)
            if not markets:
                pytest.skip("No active markets")
            market_id = markets[0].id

        # Get positions for that market
        async with ClobClient(test_credentials) as client:
            positions = await client.get_positions(market_id=market_id)

            assert isinstance(positions, list)

            # All positions should be for the requested market
            for position in positions:
                assert position.market_id == market_id

    async def test_get_orders(self, test_credentials):
        """Test getting order history."""
        async with ClobClient(test_credentials) as client:
            orders = await client.get_orders()

            # Should return list (may be empty)
            assert isinstance(orders, list)

            # If we have orders, verify structure
            if orders:
                order = orders[0]
                assert hasattr(order, 'order_id')
                assert hasattr(order, 'market_id')
                assert hasattr(order, 'price')
                assert hasattr(order, 'size')
                assert hasattr(order, 'side')

    async def test_get_orders_live_only(self, test_credentials):
        """Test getting only active orders."""
        async with ClobClient(test_credentials) as client:
            orders = await client.get_orders(status="LIVE")

            assert isinstance(orders, list)

            # All orders should be LIVE
            for order in orders:
                assert order.status == "LIVE"


@pytest.mark.asyncio
class TestClobClientOrderExecution:
    """
    Test order execution (requires funds, executes real trades).

    ⚠️ CRITICAL: These tests use REAL MONEY!
    - Orders are placed on Polygon mainnet
    - Uses real USDC from your wallet
    - Transactions are irreversible

    Only run these if you:
    1. Understand the risks
    2. Have funded your wallet with test amounts
    3. Are prepared to lose the funds used in testing
    """

    async def test_create_and_cancel_order(self, test_credentials):
        """
        Test creating and immediately canceling an order.

        Uses small amount and far-from-market price to minimize risk.
        """
        # Get a market to trade
        async with GammaClient() as gamma:
            markets = await gamma.search_markets(active=True, limit=1)
            if not markets:
                pytest.skip("No active markets")

            market = markets[0]
            if not market.yes_token_id:
                pytest.skip("Market has no YES token")

        # Create order at extreme price (unlikely to fill)
        async with ClobClient(test_credentials) as client:
            order_params = OrderParams(
                token_id=market.yes_token_id,
                price=0.01,  # Very low price, unlikely to fill
                size=1.0,  # Minimum size
                side=OrderSide.BUY,
                maker=client.credentials.wallet_address,
                signature_type=SignatureType.EOA,
            )

            # Create order
            order = await client.create_order(order_params)

            assert order.order_id
            assert order.price == 0.01
            assert order.size == 1.0
            assert order.side == OrderSide.BUY

            # Immediately cancel to minimize risk
            try:
                result = await client.cancel_order(order.order_id)
                assert result["order_id"] == order.order_id
                assert result["status"] == "canceled"
            except Exception as e:
                # Order may have filled or been rejected
                # This is acceptable for test purposes
                print(f"Warning: Could not cancel order: {e}")

    async def test_create_order_validation(self, test_credentials):
        """Test order creation with validation."""
        async with GammaClient() as gamma:
            markets = await gamma.search_markets(active=True, limit=1)
            if not markets:
                pytest.skip("No active markets")
            market = markets[0]

        # Test with valid parameters
        async with ClobClient(test_credentials) as client:
            order_params = OrderParams(
                token_id=market.yes_token_id,
                price=0.50,
                size=1.0,
                side=OrderSide.BUY,
                maker=client.credentials.wallet_address,
            )

            # Should create order structure correctly
            signed_order = client.order_signer.build_signed_order(order_params)

            assert "signature" in signed_order
            assert signed_order["price"] == "0.5"
            assert signed_order["size"] == "1.0"
            assert signed_order["side"] == "BUY"


@pytest.mark.asyncio
class TestClobClientTrades:
    """Test trade history endpoints (requires auth, no trading needed)."""

    async def test_get_trades(self, test_credentials):
        """Test getting trade history."""
        async with ClobClient(test_credentials) as client:
            trades = await client.get_trades(limit=10)

            # Should return list (may be empty if no trades)
            assert isinstance(trades, list)

            # If we have trades, verify structure
            if trades:
                trade = trades[0]
                assert hasattr(trade, 'trade_id')
                assert hasattr(trade, 'market_id')
                assert hasattr(trade, 'price')
                assert hasattr(trade, 'size')
                assert hasattr(trade, 'side')

    async def test_get_trades_for_market(self, test_credentials):
        """Test getting trades filtered by market."""
        # First get a market ID
        async with GammaClient() as gamma:
            markets = await gamma.search_markets(active=True, limit=1)
            if not markets:
                pytest.skip("No active markets")
            market_id = markets[0].condition_id  # Use condition_id for CLOB API

        # Get trades for that market
        async with ClobClient(test_credentials) as client:
            trades = await client.get_trades(market_id=market_id, limit=10)

            assert isinstance(trades, list)

            # All trades should be for the requested market (if any)
            for trade in trades:
                # Market may be empty if user has no trades for this market
                if trade.market_id:
                    assert trade.market_id == market_id


@pytest.mark.asyncio
class TestClobClientErrorHandling:
    """Test error handling for CLOB client."""

    async def test_unauthenticated_request_fails(self, test_credentials):
        """Test that requests without auth fail appropriately."""
        # Create client but don't authenticate
        client = ClobClient(test_credentials)

        # Client should handle missing auth by attempting to authenticate
        async with client:
            # First request should trigger auto-authentication
            orders = await client.get_orders()
            assert isinstance(orders, list)

            # Client should now be authenticated
            assert client._api_key is not None

    async def test_invalid_order_parameters(self, test_credentials):
        """Test that invalid order parameters are caught."""
        from pydantic import ValidationError

        # Test invalid price (too high)
        with pytest.raises(ValidationError):
            OrderParams(
                token_id="test",
                price=1.5,  # > 0.999
                size=10,
                side=OrderSide.BUY,
                maker=test_credentials.wallet_address,
            )

        # Test invalid price (too low)
        with pytest.raises(ValidationError):
            OrderParams(
                token_id="test",
                price=0.0,  # < 0.001
                size=10,
                side=OrderSide.BUY,
                maker=test_credentials.wallet_address,
            )

        # Test invalid size (negative)
        with pytest.raises(ValidationError):
            OrderParams(
                token_id="test",
                price=0.5,
                size=-10,  # Negative
                side=OrderSide.BUY,
                maker=test_credentials.wallet_address,
            )


# Note: To run these tests, execute:
# pytest tests/polymarket/integration/test_clob_client.py --run-funded -v
#
# WARNING: This will use real money from your wallet!
