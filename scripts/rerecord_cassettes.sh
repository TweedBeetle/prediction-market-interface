#!/usr/bin/env bash
# Re-record VCR cassettes for integration tests
#
# Usage:
#   ./scripts/rerecord_cassettes.sh                    # Re-record all cassettes
#   ./scripts/rerecord_cassettes.sh test_client.py     # Re-record specific test file
#   ./scripts/rerecord_cassettes.sh --new-only         # Only record missing cassettes

set -euo pipefail

# Color output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Project root (assuming script is in scripts/)
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
cd "$PROJECT_ROOT"

echo -e "${GREEN}VCR Cassette Re-recording Tool${NC}"
echo "=============================="
echo ""

# Check if cassette directory exists
if [ ! -d "tests/cassettes" ]; then
    echo -e "${YELLOW}Warning: tests/cassettes directory does not exist${NC}"
    echo "Creating directory..."
    mkdir -p tests/cassettes
fi

# Count existing cassettes
EXISTING_COUNT=$(find tests/cassettes -name "*.yaml" | wc -l)
echo "Current cassettes: $EXISTING_COUNT"
echo ""

# Determine record mode
RECORD_MODE="all"
TEST_FILTER=""

if [ $# -gt 0 ]; then
    if [ "$1" = "--new-only" ]; then
        RECORD_MODE="new_episodes"
        echo "Mode: Recording only NEW cassettes (existing will be preserved)"
    elif [ "$1" = "--help" ] || [ "$1" = "-h" ]; then
        echo "Usage:"
        echo "  $0                    # Re-record all cassettes"
        echo "  $0 test_file.py       # Re-record cassettes for specific test file"
        echo "  $0 --new-only         # Only record missing cassettes"
        echo ""
        echo "Examples:"
        echo "  $0                              # Re-record everything"
        echo "  $0 test_mcp_tools.py            # Re-record MCP tools tests"
        echo "  $0 --new-only                   # Add cassettes for new tests only"
        echo ""
        exit 0
    else
        TEST_FILTER="$1"
        echo "Filter: Running only tests in '$TEST_FILTER'"
    fi
else
    echo "Mode: Re-recording ALL cassettes"
fi

echo ""

# Warn user
if [ "$RECORD_MODE" = "all" ]; then
    echo -e "${YELLOW}WARNING: This will re-record cassettes using the LIVE demo API.${NC}"
    echo "This means:"
    echo "  - All existing cassettes will be replaced"
    echo "  - Tests will make real HTTP requests to demo-api.kalshi.co"
    echo "  - If the API is down, cassettes may contain error responses"
    echo ""
    read -p "Continue? [y/N] " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Aborted."
        exit 1
    fi
    echo ""
fi

# Check API health first
echo "Checking demo API health..."
API_STATUS=$(curl -s -o /dev/null -w "%{http_code}" https://demo-api.kalshi.co/trade-api/v2/exchange/status || echo "000")

if [ "$API_STATUS" = "200" ]; then
    echo -e "${GREEN}✓ Demo API is healthy (HTTP 200)${NC}"
elif [ "$API_STATUS" = "000" ]; then
    echo -e "${RED}✗ Cannot reach demo API (connection failed)${NC}"
    echo "  Cassettes may not record properly. Continue anyway? [y/N]"
    read -p "" -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
else
    echo -e "${YELLOW}⚠ Demo API returned HTTP $API_STATUS (expected 200)${NC}"
    echo "  Cassettes may contain error responses. Continue anyway? [y/N]"
    read -p "" -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

echo ""

# Run pytest with VCR record mode override
echo "Running tests to record cassettes..."
echo "Command: uv run pytest tests/kalshi/integration/$TEST_FILTER --record-mode=$RECORD_MODE"
echo ""

# Set environment variable to override VCR mode
export VCR_RECORD_MODE="$RECORD_MODE"

# Run tests
if uv run pytest tests/kalshi/integration/$TEST_FILTER -v --record-mode="$RECORD_MODE"; then
    echo ""
    echo -e "${GREEN}✓ Tests completed successfully${NC}"
else
    echo ""
    echo -e "${YELLOW}⚠ Some tests failed${NC}"
    echo "Cassettes may have been recorded anyway, but check for errors above."
fi

# Count new cassettes
NEW_COUNT=$(find tests/cassettes -name "*.yaml" | wc -l)
DELTA=$((NEW_COUNT - EXISTING_COUNT))

echo ""
echo "Recording complete!"
echo "==================="
echo "Before: $EXISTING_COUNT cassettes"
echo "After:  $NEW_COUNT cassettes"
if [ $DELTA -gt 0 ]; then
    echo -e "${GREEN}Added: $DELTA new cassettes${NC}"
elif [ $DELTA -lt 0 ]; then
    echo -e "${YELLOW}Removed: ${DELTA#-} cassettes${NC}"
else
    echo "No change in cassette count"
fi

echo ""
echo "Next steps:"
echo "  1. Review cassettes in tests/cassettes/"
echo "  2. Check git diff to see what changed"
echo "  3. Run tests normally to verify: uv run pytest tests/kalshi/integration/"
echo "  4. Commit updated cassettes if they look good"
