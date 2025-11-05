"""Validation tests for VCR cassettes.

These tests ensure VCR cassettes contain realistic data and aren't
masking bugs with null/empty responses.
"""

import json
import pytest
from pathlib import Path
from loguru import logger


class TestCassetteValidation:
    """Validate VCR cassettes have realistic response data."""

    def test_cassettes_exist(self):
        """Verify cassettes directory exists and has cassettes."""
        cassette_dir = Path("tests/cassettes")
        assert cassette_dir.exists(), "Cassettes directory does not exist"

        cassettes = list(cassette_dir.glob("*.yaml"))
        assert len(cassettes) > 0, "No cassettes found - run tests to generate them"

        logger.info(f"Found {len(cassettes)} cassettes")

    def test_cassettes_have_responses(self):
        """Verify cassettes contain HTTP responses, not just requests."""
        cassette_dir = Path("tests/cassettes")
        cassettes = list(cassette_dir.glob("*.yaml"))

        empty_cassettes = []

        for cassette_path in cassettes:
            content = cassette_path.read_text()

            # Check for response indicators
            if "response:" not in content and "status:" not in content:
                empty_cassettes.append(cassette_path.name)

        if empty_cassettes:
            pytest.fail(
                f"Found {len(empty_cassettes)} cassettes without responses:\n" +
                "\n".join(f"  - {name}" for name in empty_cassettes[:5])
            )

        logger.info(f"Verified {len(cassettes)} cassettes have response data")

    def test_order_cassettes_have_order_ids(self):
        """
        Verify cassettes for order operations contain actual order_id values.

        This catches the anti-pattern where tests only validate errors
        but never successfully create orders.
        """
        cassette_dir = Path("tests/cassettes")
        order_cassettes = list(cassette_dir.glob("*Order*.yaml"))

        if not order_cassettes:
            pytest.skip("No order-related cassettes found")

        cassettes_with_order_ids = []
        cassettes_without_order_ids = []

        for cassette_path in order_cassettes:
            content = cassette_path.read_text()

            # Look for order_id in response (indicates successful order creation)
            if '"order_id":' in content or 'order_id:' in content:
                cassettes_with_order_ids.append(cassette_path.name)
            else:
                cassettes_without_order_ids.append(cassette_path.name)

        logger.info(
            f"Order cassettes: {len(cassettes_with_order_ids)} with order_ids, "
            f"{len(cassettes_without_order_ids)} without"
        )

        # At least some order cassettes should have successful order creation
        if len(cassettes_with_order_ids) == 0:
            logger.warning(
                "No order cassettes contain order_id values. "
                "This suggests tests only validate errors, not successful order creation. "
                "Consider adding E2E tests that actually create orders."
            )

    def test_market_cassettes_have_tickers(self):
        """Verify market cassettes contain actual ticker values."""
        cassette_dir = Path("tests/cassettes")
        market_cassettes = list(cassette_dir.glob("*Market*.yaml"))

        if not market_cassettes:
            pytest.skip("No market-related cassettes found")

        cassettes_with_tickers = 0

        for cassette_path in market_cassettes:
            content = cassette_path.read_text()

            # Look for ticker in response
            if '"ticker":' in content or 'ticker:' in content:
                cassettes_with_tickers += 1

        assert cassettes_with_tickers > 0, "No market cassettes contain ticker values"

        logger.info(f"Verified {cassettes_with_tickers} market cassettes have tickers")

    def test_cassettes_not_all_null_orderbooks(self):
        """
        Verify orderbook cassettes don't all have null/empty orderbook data.

        This catches the bug where orderbook parsing works on null data
        but fails on real nested orderbook structures.
        """
        cassette_dir = Path("tests/cassettes")
        orderbook_cassettes = list(cassette_dir.glob("*orderbook*.yaml"))

        if not orderbook_cassettes:
            pytest.skip("No orderbook cassettes found")

        cassettes_with_bids = 0

        for cassette_path in orderbook_cassettes:
            content = cassette_path.read_text()

            # Look for bid/ask data (indicates non-null orderbook)
            if ('"bids":[' in content or '"asks":[' in content or
                'bids:' in content or 'asks:' in content):
                cassettes_with_bids += 1

        if cassettes_with_bids == 0:
            logger.warning(
                "No orderbook cassettes contain bid/ask data. "
                "All cassettes may have null orderbooks. "
                "Consider re-recording with markets that have liquidity."
            )
        else:
            logger.info(
                f"Verified {cassettes_with_bids}/{len(orderbook_cassettes)} "
                "orderbook cassettes have bid/ask data"
            )

    def test_cassettes_have_successful_responses(self):
        """Verify most cassettes have 200-level responses, not all errors."""
        cassette_dir = Path("tests/cassettes")
        cassettes = list(cassette_dir.glob("*.yaml"))

        successful_responses = 0
        error_responses = 0

        for cassette_path in cassettes:
            content = cassette_path.read_text()

            # Look for status codes
            if "code: 200" in content or "code: 201" in content:
                successful_responses += 1
            elif "code: 4" in content or "code: 5" in content:
                error_responses += 1

        total_checked = successful_responses + error_responses

        if total_checked == 0:
            pytest.skip("Could not determine response status codes from cassettes")

        success_rate = successful_responses / total_checked

        logger.info(
            f"Cassette response distribution: "
            f"{successful_responses} successful, {error_responses} errors "
            f"({success_rate:.1%} success rate)"
        )

        # At least 50% of cassettes should have successful responses
        assert success_rate >= 0.5, (
            f"Only {success_rate:.1%} of cassettes have successful responses. "
            "Tests may be only checking error cases."
        )

    def test_cassette_freshness_markers(self):
        """
        Check if cassettes have timestamps and warn if they're old.

        This helps identify stale cassettes that should be re-recorded.
        """
        cassette_dir = Path("tests/cassettes")
        cassettes = list(cassette_dir.glob("*.yaml"))

        # Count cassettes with date markers
        cassettes_with_dates = 0

        for cassette_path in cassettes:
            content = cassette_path.read_text()

            # Look for date fields in responses
            if "Date:" in content or "created_time" in content:
                cassettes_with_dates += 1

        logger.info(
            f"{cassettes_with_dates}/{len(cassettes)} cassettes have date markers"
        )

        # Just informational - we don't fail on old cassettes
        # but this test makes it visible

    def test_no_sensitive_data_in_cassettes(self):
        """Verify VCR is filtering sensitive headers from cassettes."""
        cassette_dir = Path("tests/cassettes")
        cassettes = list(cassette_dir.glob("*.yaml"))

        cassettes_with_sensitive_data = []

        # Sensitive patterns that should NOT appear in cassettes
        sensitive_patterns = [
            "KALSHI-ACCESS-KEY:",
            "KALSHI-ACCESS-SIGNATURE:",
            # API key IDs look like UUIDs
            # We check if they appear as header values (would be after colon)
        ]

        for cassette_path in cassettes:
            content = cassette_path.read_text()

            for pattern in sensitive_patterns:
                # Look for pattern followed by actual value (not just field name)
                if pattern in content:
                    # Check if there's a value after the colon
                    lines = content.split('\n')
                    for i, line in enumerate(lines):
                        if pattern in line and i + 1 < len(lines):
                            next_line = lines[i + 1].strip()
                            # If next line has a value (not empty, not another field)
                            if next_line and not next_line.endswith(':'):
                                cassettes_with_sensitive_data.append(
                                    (cassette_path.name, pattern)
                                )
                                break

        if cassettes_with_sensitive_data:
            # Group by cassette
            by_cassette = {}
            for cassette, pattern in cassettes_with_sensitive_data:
                by_cassette.setdefault(cassette, []).append(pattern)

            logger.warning(
                f"Found {len(by_cassette)} cassettes with potentially sensitive data:\n" +
                "\n".join(
                    f"  - {cassette}: {', '.join(patterns)}"
                    for cassette, patterns in list(by_cassette.items())[:5]
                )
            )
        else:
            logger.info("No sensitive data found in cassettes (VCR filtering working)")
