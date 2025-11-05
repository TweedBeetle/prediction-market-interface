"""
Pytest configuration for Polymarket tests.
"""

import pytest


def pytest_addoption(parser):
    """Add custom pytest options."""
    parser.addoption(
        "--run-funded",
        action="store_true",
        default=False,
        help="Run tests that require funded wallet (USES REAL MONEY on Polygon mainnet)"
    )


def pytest_configure(config):
    """Configure pytest with custom markers."""
    config.addinivalue_line(
        "markers",
        "funded: mark test as requiring funded wallet (use --run-funded to run)"
    )


def pytest_collection_modifyitems(config, items):
    """
    Modify test collection to handle funded tests.

    Tests marked with @pytest.mark.funded will be skipped unless
    --run-funded flag is passed.
    """
    if config.getoption("--run-funded"):
        # Run all tests including funded ones
        return

    skip_funded = pytest.mark.skip(reason="Requires funded wallet. Use --run-funded to execute.")

    for item in items:
        if "funded" in item.keywords:
            item.add_marker(skip_funded)
