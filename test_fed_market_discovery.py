#!/usr/bin/env python3
"""
Test script to demonstrate Fed market discovery fix.

This script tests both search methods:
1. Regular search (should find 0 Fed markets)
2. Comprehensive search (should find Fed markets)

Run: uv run python3 test_fed_market_discovery.py
"""

import asyncio
from dotenv import load_dotenv

# Load environment
load_dotenv(".env.kalshi.demo", override=True)

from src.kalshi.client import KalshiClient


async def main():
    print("=" * 80)
    print("Fed Market Discovery Test")
    print("=" * 80)
    print()

    async with KalshiClient.from_env() as client:
        # Test 1: Regular search (expected to find nothing)
        print("TEST 1: Regular search for 'Fed'")
        print("-" * 80)
        regular_markets = await client.search_markets(query="Fed", limit=20, status="open")
        print(f"Found {len(regular_markets)} markets")
        if regular_markets:
            for market in regular_markets[:3]:
                print(f"  - {market.ticker}: {market.title}")
        else:
            print("  ❌ No markets found (expected - MVE markets excluded)")
        print()

        # Test 2: Comprehensive search (expected to find Fed markets)
        print("TEST 2: Comprehensive search for 'Fed'")
        print("-" * 80)
        comprehensive_markets = await client.search_markets_comprehensive(
            query="Fed", limit=20, status="open", include_mve=True
        )
        print(f"Found {len(comprehensive_markets)} markets")
        if comprehensive_markets:
            print("  ✅ Fed markets discovered!")
            print()
            print("Sample markets:")
            for market in comprehensive_markets[:5]:
                print(f"  - {market.ticker}")
                print(f"    Title: {market.title}")
                if market.yes_bid and market.yes_ask:
                    print(f"    Price: {market.yes_bid}¢ bid / {market.yes_ask}¢ ask")
                print()
        else:
            print("  ❌ No markets found (unexpected!)")
        print()

        # Test 3: Search for "rate cuts" specifically
        print("TEST 3: Comprehensive search for 'rate cuts'")
        print("-" * 80)
        rate_cut_markets = await client.search_markets_comprehensive(
            query="rate cuts", limit=10, status="open", include_mve=True
        )
        print(f"Found {len(rate_cut_markets)} markets")
        if rate_cut_markets:
            print("  ✅ Rate cut markets discovered!")
            print()
            print("Markets by number of cuts:")
            for market in rate_cut_markets:
                print(f"  - {market.ticker}")
                print(f"    {market.title}")
                if market.yes_bid and market.yes_ask:
                    mid_price = (market.yes_bid + market.yes_ask) / 2
                    print(f"    Price: {mid_price:.1f}¢ (implies {mid_price:.1f}% probability)")
                print()
        print()

        # Test 4: Get markets for specific series
        print("TEST 4: Direct series lookup (KXRATECUTCOUNT)")
        print("-" * 80)
        series_markets = await client.get_markets_by_series(
            series_ticker="KXRATECUTCOUNT", limit=10, status="open"
        )
        print(f"Found {len(series_markets)} markets in KXRATECUTCOUNT series")
        for market in series_markets:
            print(f"  - {market.ticker}: {market.title}")
        print()

    print("=" * 80)
    print("Test Complete!")
    print("=" * 80)
    print()
    print("Summary:")
    print(f"  Regular search:        {len(regular_markets)} markets (expected: 0)")
    print(f"  Comprehensive search:  {len(comprehensive_markets)} markets (expected: >0)")
    print(f"  'Rate cuts' search:    {len(rate_cut_markets)} markets")
    print(f"  Series lookup:         {len(series_markets)} markets")
    print()

    if comprehensive_markets and not regular_markets:
        print("✅ SUCCESS: Comprehensive search finds MVE markets that regular search misses!")
    elif regular_markets:
        print("⚠️  UNEXPECTED: Regular search found markets (API may have changed)")
    else:
        print("❌ FAILURE: Comprehensive search also found nothing")


if __name__ == "__main__":
    asyncio.run(main())
