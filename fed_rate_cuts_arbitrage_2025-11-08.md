# Fed Rate Cuts Arbitrage Analysis
**Date:** 2025-11-08
**Session:** Post-restart, production Kalshi data
**Platforms:** Kalshi (Production) vs Polymarket (Production)

## Executive Summary

**Finding:** No direct arbitrage opportunities - Kalshi and Polymarket measure **different events/timeframes**.

- **Kalshi:** Emergency rate cuts by 2026, total cuts by end 2026
- **Polymarket:** Exact cut counts for 2025 (2, 3, 4, 5, 6, 7, 8+)

---

## Key Findings

### 1. Zero Liquidity Investigation ✅

**Issue Resolved:** Markets showing "0 bid / 0 ask" or wide "0/100" spreads are **NOT a bug** - they genuinely have zero liquidity.

**Evidence:**
- Examined `KXLEADERNFLSACKS-26JAN05-RGAR` (NFL player prop)
- Orderbook confirmed: NO YES bids at all, only asks starting at 18¢
- Low-interest markets (niche NFL props, minor elections) have no liquidity
- High-interest markets (Fed rates, Bitcoin, Trump policies) have real liquidity

**User's hypothesis was correct:** The "legs" (major event markets) have liquidity, while obscure markets don't.

---

## 2. Market Comparison: Fed Rate Cuts

### Kalshi Production - Emergency Rate Cuts by 2026

**Series:** KXEMERCUTS-25
**Volume:** 88k-90k contracts
**Expiration:** January 1, 2026

| Outcome | Bid | Ask | Spread | Volume | Orderbook Depth |
|---------|-----|-----|--------|--------|-----------------|
| 0 emergency cuts | 97¢ | 98¢ | 1¢ | 88,248 | YES: 97¢×193, NO: 3¢×193 |
| 1 emergency cut | 3¢ | 4¢ | 1¢ | 90,245 | - |

**Market interpretation:** 97% confident there will be NO emergency rate cuts by 2026.

**Orderbook depth (KXEMERCUTS-25-T0):**
```
YES side: 97¢ bid (193 contracts) / 98¢ ask (469 contracts)
NO side: 2¢ bid (469 contracts) / 3¢ ask (193 contracts)

Deep bids at: 96¢×2000, 92¢×10000, 91¢×1000, 90¢×1457
```

**Tight 1¢ spread** with significant depth. This is a **highly liquid market**.

---

### Polymarket - Total Cuts in 2025

**Expiration:** December 10, 2025 (different from Kalshi!)
**Volume:** $2.5M-$2.7M per market

| Outcome | Bid | Ask | Spread | Volume | 24h Volume |
|---------|-----|-----|--------|--------|------------|
| Exactly 2 cuts in 2025 | 25¢ | 27¢ | 2¢ | $2.55M | $62k |
| Exactly 3 cuts in 2025 | - | - | - | $2.69M | $20k |
| Exactly 4 cuts in 2025 | - | - | - | $2.68M | $1.4k |

**Orderbook depth (2 cuts market, token 11661882248...):**
```
YES bids: 25¢×6,646 | 24¢×20,651 | 23¢×942 | ... | 1¢×315,521!
YES asks: 27¢×1,692 | 28¢×3,321 | 29¢×1,484 | 30¢×6,550
```

**Massive liquidity** - 315k contracts willing to buy at 1¢!

---

### Why No Arbitrage?

**Different event definitions:**

| Platform | Question | Timeframe | Event Type |
|----------|----------|-----------|------------|
| Kalshi | Emergency cuts | Through Jan 1, 2026 | Binary (yes/no) |
| Polymarket | Exact cut count (2, 3, 4...) | Through Dec 10, 2025 | Categorical |

**Cannot compare:**
- Kalshi asks: "Will there be an EMERGENCY cut?" (unscheduled FOMC action)
- Polymarket asks: "How many TOTAL cuts in 2025?" (scheduled + emergency)

**Result:** These measure fundamentally different events. No arbitrage possible.

---

## 3. Kalshi Production - High Volume Markets

Top markets by trading volume:

| Market | Ticker | Bid | Ask | Volume | 24h Vol | Spread |
|--------|--------|-----|-----|--------|---------|--------|
| Trump Bitcoin Reserve | KXBTCRESERVE-26-JAN01 | 6¢ | 7¢ | 2.13M | 101k | 1¢ |
| Bitcoin $150k by Dec 31 | KXBTCMAX150-25-DEC31 | 6¢ | 7¢ | 2.94M | 8.6k | 1¢ |
| Bitcoin $150k by Nov 30 | KXBTCMAX150-25-NOV30 | 2¢ | 3¢ | 2.31M | 8.3k | 1¢ |
| Bitcoin $150k by Feb 28 | KXBTCMAX150-25-26FEB28 | 14¢ | 16¢ | 1.53M | 4.9k | 2¢ |
| Bitcoin low ($90k+) | KXBTCMINY-25-2-DEC31 | 40¢ | 42¢ | 1.39M | 21.5k | 2¢ |
| Bitcoin $150k by May 31 | KXBTCMAX150-25-26MAY31 | 32¢ | 33¢ | 320k | 3.2k | 1¢ |

**Bitcoin markets dominate volume** on Kalshi production. All have tight 1-2¢ spreads.

---

## 4. Next Steps

### To Find Arbitrage Opportunities:

1. **Search Polymarket** for matching markets (rate limited - need to wait 48s):
   - Bitcoin Reserve Trump
   - Bitcoin $150k by specific dates
   - Trump policy markets

2. **Compare matching markets** with same:
   - Question (exact wording)
   - Resolution criteria
   - Timeframe

3. **Calculate arbitrage** when:
   - Spread > transaction costs (Kalshi ~2%, Polymarket gas fees)
   - Sufficient liquidity on both sides
   - Risk-adjusted return justifies capital lockup

### Current Blockers:

- ⏸️ **Polymarket rate limited** - must wait ~48 seconds between requests
- ⏸️ Cannot search for Bitcoin Reserve on Polymarket yet
- ⏸️ Cannot verify if Bitcoin $150k markets exist on Polymarket

---

## Technical Notes

### API Differences

**Polymarket:**
- Search returns `best_bid: null, best_ask: null` (metadata only)
- Must query orderbook separately for real prices
- Orderbook has massive depth (100k+ contracts common)
- Price as decimals (0.25 = 25¢)

**Kalshi:**
- Search returns bid/ask in response
- Orderbook query needed for depth
- Lower liquidity overall (1k-10k typical)
- Price in cents (25 = 25¢)

### Market Structure Differences

**Kalshi MVE Markets:**
- Each outcome gets separate ticker (e.g., `KXEMERCUTS-25-T0`, `KXEMERCUTS-25-T1`)
- Trade each outcome independently
- Must aggregate volume across tickers

**Polymarket:**
- Single market with YES/NO token pairs per outcome
- Each token has unique ID
- Volume tracked per market

**Implication:** Can't match by ticker - must map by question semantics and timeframe.

---

## Session State

✅ Connected to Kalshi production (`api.elections.kalshi.com`)
✅ Connected to Polymarket production
✅ Found high-volume markets on Kalshi
✅ Retrieved Polymarket Fed rate cut markets
✅ Analyzed orderbook depth
✅ Identified timeframe mismatches

⏸️ Rate limited on Polymarket (48s cooldown)
⏸️ Bitcoin Reserve comparison pending
⏸️ Cross-platform arbitrage search incomplete
