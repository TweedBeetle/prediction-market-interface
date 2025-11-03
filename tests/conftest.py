"""Pytest configuration and shared fixtures."""

import os
import pytest
from dotenv import load_dotenv

# Load demo environment for all tests
# override=True ensures demo values replace any existing .env values
load_dotenv(".env.kalshi.demo", override=True)

# Import all fixtures from fixtures module
pytest_plugins = ["tests.fixtures.markets"]


@pytest.fixture(scope="session")
def demo_env():
    """Ensure demo environment is loaded."""
    env = os.getenv("KALSHI_ENVIRONMENT")
    assert env == "demo", f"Tests must run in demo environment, got: {env}"
    return env


@pytest.fixture(scope="module")
def vcr_config():
    """VCR configuration for recording/replaying HTTP requests."""
    return {
        "filter_headers": [
            "KALSHI-ACCESS-KEY",
            "KALSHI-ACCESS-SIGNATURE",
            "KALSHI-ACCESS-TIMESTAMP"
        ],
        "record_mode": "once",  # Record once, replay thereafter
        "match_on": ["method", "scheme", "host", "port", "path", "query"],
        "cassette_library_dir": "tests/cassettes",
        "decode_compressed_response": True,
        "filter_post_data_parameters": [
            "api_key",
            "private_key"
        ],
    }


def pytest_collection_modifyitems(config, items):
    """Automatically mark integration tests to use VCR."""
    for item in items:
        # Mark integration tests with vcr
        if "integration" in str(item.fspath):
            item.add_marker(pytest.mark.vcr)
