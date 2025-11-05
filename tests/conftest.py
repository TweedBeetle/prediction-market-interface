"""Pytest configuration and shared fixtures."""

import os
import pytest
import httpx
from dotenv import load_dotenv
from loguru import logger

# Load demo environment for all tests
# override=True ensures demo values replace any existing .env values
load_dotenv(".env.kalshi.demo", override=True)

# Import all fixtures from fixtures module
pytest_plugins = ["tests.fixtures.markets"]


@pytest.fixture(scope="session", autouse=True)
def check_demo_api_health():
    """
    Check demo API health before running test suite.

    Warns if API is experiencing issues (5xx errors) but doesn't skip tests
    since we use VCR cassettes that work even when API is down.
    """
    try:
        response = httpx.get(
            "https://demo-api.kalshi.co/trade-api/v2/exchange/status",
            timeout=10.0
        )

        if response.status_code >= 500:
            logger.warning(
                f"Demo API health check failed with {response.status_code}. "
                "Tests will use VCR cassettes but MCP tool testing may fail."
            )
        elif response.status_code >= 400:
            logger.warning(
                f"Demo API returned {response.status_code}. "
                "Check credentials or API availability."
            )
        else:
            logger.info("Demo API health check passed")

    except Exception as e:
        logger.warning(
            f"Demo API health check failed: {e}. "
            "Tests will use VCR cassettes but MCP tool testing may fail."
        )


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
        # Mark integration tests with vcr, unless they explicitly disable recording
        if "integration" in str(item.fspath):
            # Check if test has disable_recording marker
            if not any(marker.name == "disable_recording" for marker in item.iter_markers()):
                item.add_marker(pytest.mark.vcr)
