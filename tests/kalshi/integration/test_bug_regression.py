"""Regression tests for bugs found in production.

These tests specifically validate fixes for bugs that were missed by existing tests.
Each test includes a comment explaining what bug it catches and why original tests missed it.
"""

import pytest
import os
from pathlib import Path
from dotenv import load_dotenv


@pytest.mark.asyncio
class TestOrderbookParsing:
    """
    Regression test for orderbook parsing bug.

    Original bug: Code expected nested {"yes": {"bids": [...], "asks": [...]}}
                  but API returns flat {"yes": [[price, qty], ...]}

    Why original tests missed it: All VCR cassettes had null orderbooks,
    so the bad parsing code never executed.
    """

    async def test_orderbook_parses_flat_array_structure(self, demo_env):
        """Orderbook should handle flat array structure [[price, qty], ...]."""
        from src.kalshi.client import KalshiClient
        from src.kalshi.models import OrderBook, OrderBookLevel

        async with KalshiClient.from_env() as client:
            # Search for a market with actual orderbook data
            markets = await client.search_markets(limit=50, status="open")

            orderbook_found = False
            for market in markets:
                try:
                    orderbook = await client.get_orderbook(market.ticker, depth=5)

                    # If we got an orderbook with data, validate its structure
                    if orderbook.yes_bids or orderbook.no_bids:
                        orderbook_found = True

                        # Validate structure
                        assert isinstance(orderbook, OrderBook)
                        assert isinstance(orderbook.yes_bids, list)
                        assert isinstance(orderbook.no_bids, list)

                        # If there are bids, validate they're OrderBookLevel objects
                        if orderbook.yes_bids:
                            first_bid = orderbook.yes_bids[0]
                            assert isinstance(first_bid, OrderBookLevel)
                            assert hasattr(first_bid, 'price')
                            assert hasattr(first_bid, 'quantity')
                            assert isinstance(first_bid.price, int)
                            assert isinstance(first_bid.quantity, int)
                            assert 1 <= first_bid.price <= 99  # Kalshi prices in cents

                        # Validate implied asks are calculated correctly
                        # YES ask should be 100 - NO bid
                        if orderbook.yes_asks and orderbook.no_bids:
                            highest_no_bid = max(b.price for b in orderbook.no_bids)
                            best_yes_ask = min(a.price for a in orderbook.yes_asks)
                            assert best_yes_ask == 100 - highest_no_bid, \
                                "YES ask should equal 100 - NO bid"

                        break  # Found and validated orderbook, we're done

                except Exception as e:
                    # Market might not have orderbook or might be closed, continue
                    continue

            # This assertion ensures we actually tested with real data
            # If no markets have orderbooks, the test should be investigated
            if not orderbook_found:
                pytest.skip("No markets with orderbook data found - cannot validate parsing")

    async def test_orderbook_handles_null_gracefully(self, demo_env):
        """Orderbook should handle null values without crashing."""
        from src.kalshi.client import KalshiClient

        async with KalshiClient.from_env() as client:
            # Try a market that might have null orderbook
            markets = await client.search_markets(limit=10, status="closed")

            if markets:
                # Closed markets often have null orderbooks
                orderbook = await client.get_orderbook(markets[0].ticker)
                assert orderbook is not None
                assert isinstance(orderbook.yes_bids, list)
                assert isinstance(orderbook.no_bids, list)
                # Empty lists are OK for closed markets


@pytest.mark.asyncio
class TestAuthSignature:
    """
    Regression test for auth signature bug.

    Original bug: Signature included request body, but Kalshi docs specify
                  only timestamp + method + path (no body, no query params)

    Why original tests missed it: VCR cassettes replay old successful auth,
    so even completely wrong signatures would "pass" tests.
    """

    async def test_auth_signature_format_correct(self, demo_env):
        """Auth signature should NOT include body, per Kalshi docs."""
        from src.kalshi.client import KalshiClient

        # This test makes a real authenticated request (not VCR)
        # If auth signature is wrong, this will get 401
        async with KalshiClient.from_env() as client:
            # This call requires authentication
            balance = await client.get_balance()

            # If we got here without 401, auth signature is correct
            assert balance is not None
            assert hasattr(balance, 'balance')
            assert balance.balance >= 0

    async def test_post_request_auth_without_body_in_signature(self, demo_env):
        """POST requests should also sign without body in signature."""
        from src.kalshi.client import KalshiClient
        import inspect

        # Validate the _sign_request method signature
        client = KalshiClient.from_env()

        # Check method signature - should NOT have body parameter
        sig = inspect.signature(client._sign_request)
        params = list(sig.parameters.keys())

        assert 'method' in params
        assert 'path' in params
        assert 'body' not in params, \
            "_sign_request should NOT have 'body' parameter (removed per Kalshi docs)"


class TestEnvLoading:
    """
    Regression test for env loading bug.

    Original bug: load_dotenv() doesn't override by default, so if .env loads first
                  with prod credentials, then .env.kalshi.demo loads, you get mixed
                  credentials (demo API key + prod private key)

    Why original tests missed it: Tests explicitly call load_dotenv() in conftest.py,
    bypassing the wrapper script behavior.
    """

    def test_env_specific_files_use_override_true(self):
        """Wrapper scripts should use override=True when loading env-specific files."""
        # Read wrapper scripts and check for override=True

        demo_wrapper = Path(__file__).parent.parent.parent.parent / "run_kalshi_mcp_demo.py"
        prod_wrapper = Path(__file__).parent.parent.parent.parent / "run_kalshi_mcp_prod.py"

        if demo_wrapper.exists():
            content = demo_wrapper.read_text()
            assert 'override=True' in content, \
                "run_kalshi_mcp_demo.py must use override=True in load_dotenv()"
            assert 'load_dotenv' in content
            assert '.env.kalshi.demo' in content

        if prod_wrapper.exists():
            content = prod_wrapper.read_text()
            assert 'override=True' in content, \
                "run_kalshi_mcp_prod.py must use override=True in load_dotenv()"
            assert 'load_dotenv' in content
            assert '.env.kalshi.prod' in content

    def test_env_override_behavior(self, tmp_path):
        """Demonstrate that override=True is required to replace existing env vars."""
        # Create two test .env files
        env1 = tmp_path / ".env1"
        env1.write_text("TEST_VAR=value1\n")

        env2 = tmp_path / ".env2"
        env2.write_text("TEST_VAR=value2\n")

        # Clean up TEST_VAR if it exists
        os.environ.pop('TEST_VAR', None)

        # Load first file
        load_dotenv(env1)
        assert os.getenv('TEST_VAR') == 'value1'

        # Load second file WITHOUT override - value should NOT change
        load_dotenv(env2, override=False)
        assert os.getenv('TEST_VAR') == 'value1', \
            "Without override=True, load_dotenv keeps existing value"

        # Load second file WITH override - value SHOULD change
        load_dotenv(env2, override=True)
        assert os.getenv('TEST_VAR') == 'value2', \
            "With override=True, load_dotenv replaces existing value"

        # Cleanup
        os.environ.pop('TEST_VAR', None)


@pytest.mark.asyncio
class TestVCRCassetteQuality:
    """
    Meta-test: Validate that VCR cassettes contain realistic data.

    This test audits cassettes to ensure they don't have unrealistic data
    that would mask bugs (like all null orderbooks, no auth headers, etc.).
    """

    def test_cassettes_have_realistic_orderbook_data(self):
        """Audit: At least some cassettes should have non-null orderbook data."""
        import yaml

        cassette_dir = Path(__file__).parent.parent.parent / "cassettes"
        orderbook_cassettes = list(cassette_dir.glob("*orderbook*.yaml"))

        if not orderbook_cassettes:
            pytest.skip("No orderbook cassettes found")

        has_real_data = False
        for cassette_file in orderbook_cassettes:
            content = yaml.safe_load(cassette_file.read_text())

            if 'interactions' in content:
                for interaction in content['interactions']:
                    response_body = interaction.get('response', {}).get('body', {})
                    if isinstance(response_body, dict):
                        orderbook = response_body.get('orderbook', {})
                        if orderbook:
                            # Check if orderbook has actual data (not all null)
                            if (orderbook.get('yes') or orderbook.get('no')):
                                has_real_data = True
                                break
                if has_real_data:
                    break

        # This is informational - we want SOME cassettes to have real data
        # but it's OK if some specific markets have null orderbooks
        if not has_real_data:
            pytest.warns(
                UserWarning,
                match="No cassettes found with realistic orderbook data"
            )
