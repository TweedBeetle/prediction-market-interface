#!/usr/bin/env python3
"""
Fast Fed market discovery test.

Tests only the comprehensive search and direct series lookup.
Regular search would take 60+ seconds (100+ pages with no matches).

Run: uv run python3 test_fed_discovery_fast.py
"""

import asyncio
from dotenv import load_dotenv

# Load environment
load_dotenv(".env.kalshi.demo", override=True)

from src.kalshi.client import KalshiClient


async def main():
    print("=" * 80)
    print("Fed Market Discovery Test (Fast Version)")
    print("=" * 80)
    print()

    async with KalshiClient.from_env() as client:
        # Test 1: Comprehensive search (should find Fed markets quickly)
        print("TEST 1: Comprehensive search for 'Fed'")
        print("-" * 80)
        comprehensive_markets = await client.search_markets_comprehensive(
            query="Fed", limit=5, status="open", include_mve=True
        )
        print(f"Found {len(comprehensive_markets)} markets")
        if comprehensive_markets:
            print("  ✅ Fed markets discovered via comprehensive search!")
            print()
            print("Sample markets:")
            for market in comprehensive_markets:
                print(f"  - {market.ticker}")
                print(f"    Title: {market.title}")
                if market.yes_bid and market.yes_ask:
                    print(f"    Price: {market.yes_bid}¢ bid / {market.yes_ask}¢ ask")
                print()
        else:
            print("  ❌ No markets found (unexpected!)")
        print()

        # Test 2: Direct series lookup
        print("TEST 2: Direct series lookup (KXRATECUTCOUNT)")
        print("-" * 80)
        series_markets = await client.get_markets_by_series(
            series_ticker="KXRATECUTCOUNT", limit=10, status="open"
        )
        print(f"Found {len(series_markets)} markets in KXRATECUTCOUNT series")
        for market in series_markets:
            print(f"  - {market.ticker}: {market.title}")
            if market.yes_bid and market.yes_ask:
                mid_price = (market.yes_bid + market.yes_ask) / 2
                print(f"    Mid price: {mid_price:.1f}¢ (implies {mid_price:.1f}% probability)")
        print()

        # Test 3: Search series
        print("TEST 3: Search series titles for 'rate'")
        print("-" * 80)
        series_list = await client.search_series(query="rate", limit=5)
        print(f"Found {len(series_list)} series matching 'rate'")
        for series in series_list:
            ticker = series.get("ticker", "N/A")
            title = series.get("title", "N/A")
            print(f"  - {ticker}: {title}")
        print()

    print("=" * 80)
    print("Test Complete!")
    print("=" * 80)
    print()
    print("Summary:")
    print(f"  Comprehensive search:  {len(comprehensive_markets)} markets")
    print(f"  Direct series lookup:  {len(series_markets)} markets")
    print(f"  Series search:         {len(series_list)} series")
    print()

    if comprehensive_markets and series_markets:
        print("✅ SUCCESS: MVE markets are now discoverable!")
        print("   - Comprehensive search finds them via series/event search")
        print("   - Direct series lookup works perfectly")
        print("   - Series text search finds matching series")
    else:
        print("❌ FAILURE: Something went wrong")


if __name__ == "__main__":
    asyncio.run(main())
