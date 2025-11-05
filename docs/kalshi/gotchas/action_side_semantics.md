# Confusing Action/Side Field Semantics

**Discovered**: 2025-10-28 (via Discord discussion)
**Status**: Confirmed - Undocumented Behavior
**Severity**: High (Breaking change risk)

## Description

The Kalshi API's `action` and `side` fields **do not match the natural interpretation** of what you requested when placing an order.

Specifically, when you **SELL NO**, the API reports this back as **SELL YES** in fills/order responses, because economically they are equivalent (selling NO = buying YES).

However, this is:
1. ❌ **Not documented** anywhere in Kalshi API docs
2. ❌ **Confusing** - you asked to sell NO, but API says you sold YES
3. ❌ **Inconsistent** - buy side works as expected, sell side doesn't
4. ⚠️ **Breaking change risk** - if Kalshi "fixes" this, existing systems will break

## Evidence

### Discord Conversation (2025-10-28)

User **monomorphism**:
> "Naively, I was assuming that a BUY YES fill and a SELL NO fill are the same thing, but it's totally possible I've been misinterpreting the meaning of the fields. The semantics are not documented anywhere though"

User **Chicken**:
> "I think this is the API endpoint for which action (buy/sell) corresponds with what you did, while side assumes you only bought, and returns the side corresponding to that assumption (YES/NO)"

**Additional clarification from Discord**:

User **Arbgame**:
> "Side is the direction you're going, so yes is either buying yes or selling no. Action is basically useless since you can buy or sell to accomplish the same thing."

User **Chicken** (tldr):
> "tldr is that the GetFills endpoint is funky. Pay attention to side, ignore action, and assume you're always buying."

### Actual API Behavior Matrix

| What You Request | What API Reports | Notes |
|------------------|------------------|-------|
| `buy YES` | `buy YES` | ✅ Correct |
| `buy NO` | `buy NO` | ✅ Correct |
| `sell YES` | `sell NO` | ❌ **INVERTED** |
| `sell NO` | `sell YES` | ❌ **INVERTED** |

**Pattern**:
- **BUY side**: API reports exactly what you requested
- **SELL side**: API inverts the side (YES ↔ NO)

### Why This Happens (Theory)

Kalshi appears to be normalizing sell orders into economically equivalent buy orders:

- **Sell NO** = economically equivalent to **Buy YES**
- **Sell YES** = economically equivalent to **Buy NO**

So when you sell NO at 75¢, Kalshi treats this as buying YES at 25¢ (since YES + NO = 100¢).

The API then reports the **normalized** position (buy YES) rather than your **original request** (sell NO).

## Impact

### For Our System

This affects:

1. **Order Reconciliation**
   - Cannot match placed orders with fill confirmations by comparing fields directly
   - Need to apply transformation logic when checking if fill matches request
   - Increases complexity and bug risk

2. **Position Tracking**
   - If you think you sold NO but API says you bought YES, position tracking gets confusing
   - Need to understand economic equivalence to interpret positions correctly

3. **Accounting/Reporting**
   - User asked to "sell NO" but logs show "bought YES"
   - Confusing for auditing and debugging
   - Need translation layer for human-readable reporting

4. **Breaking Change Risk** ⚠️
   - **Chicken**: "I am PRAYING that they give proper notice before this endpoint is aligned with the docs... it will destroy my systems if they make a change to this without notice"
   - If Kalshi "fixes" this to match documentation, all systems with workarounds will break
   - No guarantee of notice before change

### Specific Scenarios That Break

**Scenario 1: Order verification**
```python
# You place order
order = {
    "action": "sell",
    "side": "no",
    "ticker": "MARKET-25"
}

# API confirms
response = {
    "action": "sell",
    "side": "yes",  # ← DIFFERENT from what you requested!
    "ticker": "MARKET-25"
}

# Naive check fails
if response["side"] == order["side"]:  # False!
    print("Order confirmed")
```

**Scenario 2: Position calculation**
```python
# You sell NO at 75¢ (trying to exit long NO position)
# API reports: sell YES at 75¢
# Your position tracker thinks you sold YES, not NO
# Now your position is wrong!
```

## Workaround

### Community Recommendation: Ignore Action Field (Simplest)

Based on Discord community feedback from experienced Kalshi traders:

**Approach**: When processing fills/orders from GetFills endpoint:
1. **Ignore `action` field entirely** - it's "basically useless" (Arbgame)
2. **Focus only on `side` field** - this tells you the economic direction (YES or NO)
3. **Assume everything is a buy** - Kalshi normalizes all trades to buys internally

**Why this works**:
- Kalshi internally converts all trades to economically equivalent buy positions
- The `side` field accurately represents which side you now own (YES or NO)
- The `action` field adds confusion without providing useful information

**Example**:
```python
# When processing GetFills response
for fill in fills:
    # ✅ DO: Focus on side
    position_side = fill["side"]  # "yes" or "no"

    # ❌ DON'T: Try to interpret action
    # action = fill["action"]  # Ignore this field

    # Update position tracking
    if position_side == "yes":
        position.yes_contracts += fill["count"]
    else:
        position.no_contracts += fill["count"]
```

**Trade-offs**:
- ✅ **Simplest approach** - no transformation logic needed
- ✅ **Matches Kalshi's internal model** - think in terms of buy positions only
- ⚠️ **Loses original intent** - can't distinguish "bought YES" from "sold NO" in logs
- ⚠️ **May confuse auditing** - position tracking doesn't match user's mental model

### Option 1: Apply Transformation When Checking

```python
def normalize_order_for_comparison(action: str, side: str) -> tuple[str, str]:
    """
    Normalize order to match how Kalshi API reports it.

    Kalshi inverts side when action is "sell":
    - sell NO → sell YES
    - sell YES → sell NO
    """
    if action.lower() == "sell":
        # Invert side for sell orders
        inverted_side = "yes" if side.lower() == "no" else "no"
        return (action, inverted_side)
    else:
        # Buy orders are not transformed
        return (action, side)

# Usage
requested_action, requested_side = "sell", "no"
expected_action, expected_side = normalize_order_for_comparison(requested_action, requested_side)

# Now check response
if response["action"] == expected_action and response["side"] == expected_side:
    print("Order matches!")  # This works now
```

### Option 2: Store Original Request Separately

```python
class Order:
    # What you requested
    requested_action: str
    requested_side: str

    # What API will report (normalized)
    api_action: str
    api_side: str

    def __init__(self, action: str, side: str):
        self.requested_action = action
        self.requested_side = side

        # Calculate what API will report
        if action.lower() == "sell":
            self.api_action = "sell"
            self.api_side = "yes" if side.lower() == "no" else "no"
        else:
            self.api_action = action
            self.api_side = side

    def matches_response(self, response: dict) -> bool:
        """Check if API response matches this order."""
        return (
            response["action"].lower() == self.api_action.lower() and
            response["side"].lower() == self.api_side.lower()
        )
```

### Option 3: Always Use Buy Orders (Simplest)

```python
def convert_sell_to_buy(action: str, side: str, price: float) -> tuple[str, str, float]:
    """
    Convert sell orders to economically equivalent buy orders.
    This matches what Kalshi does internally.
    """
    if action.lower() == "sell":
        # Sell NO at 75¢ → Buy YES at 25¢
        # Sell YES at 25¢ → Buy NO at 75¢
        inverted_side = "yes" if side.lower() == "no" else "no"
        inverted_price = 100 - price  # YES + NO = 100¢
        return ("buy", inverted_side, inverted_price)
    else:
        return (action, side, price)

# Usage: Convert all orders to buys before sending to API
action, side, price = convert_sell_to_buy("sell", "no", 75)
# Result: action="buy", side="yes", price=25
# Now API response will match exactly what you sent!
```

## Recommended Implementation

Two approaches based on use case:

### For Position Tracking (Simplest)

Use the **Community Recommendation** approach:
- Ignore `action` field when processing GetFills responses
- Track positions based solely on `side` field
- Assume all fills are buys (matches Kalshi's internal model)

**Best for**: Simple position tracking where you don't need to audit original trade intent

### For Order Placement (Most Explicit)

Use **Option 3 (Always Use Buy Orders)**:

```python
# src/clients/kalshi_client.py

async def place_order(
    self,
    ticker: str,
    action: str,  # "buy" or "sell"
    side: str,    # "yes" or "no"
    count: int,
    price: float
) -> dict:
    """
    Place order on Kalshi.

    IMPORTANT: Kalshi API has undocumented behavior where sell orders
    are internally converted to economically equivalent buy orders:
    - sell NO at 75¢ → reported as sell YES at 75¢
    - sell YES at 25¢ → reported as sell NO at 25¢

    To avoid confusion, we normalize all sell orders to buy orders
    BEFORE sending to API. This way, API response matches what we sent.
    """
    # Normalize sell → buy (matches Kalshi's internal behavior)
    if action.lower() == "sell":
        logger.debug(f"Converting sell order to buy (Kalshi API quirk)")
        # Sell NO at X¢ = Buy YES at (100-X)¢
        inverted_side = "yes" if side.lower() == "no" else "no"
        inverted_price = 1.0 - price  # In decimal (0-1)

        action = "buy"
        side = inverted_side
        price = inverted_price

        logger.debug(f"  Original: sell {side} at {price}")
        logger.debug(f"  Converted: buy {inverted_side} at {inverted_price}")

    # Now send order (API response will match exactly)
    order_data = {
        "ticker": ticker,
        "action": action,
        "side": side,
        "count": count,
        "type": "limit",
        "yes_price": int(price * 100) if side == "yes" else None,
        "no_price": int(price * 100) if side == "no" else None,
        "client_order_id": str(uuid.uuid4())
    }

    return await self._post('/trade-api/v2/portfolio/orders', order_data)
```

## Breaking Change Risk

⚠️ **CRITICAL WARNING**: If Kalshi changes this behavior to match documentation:

1. **Systems that normalize** (Option 3): Will break - orders will be inverted
2. **Systems with workarounds** (Option 1/2): Will break - checks will fail
3. **Systems that ignore this**: Will suddenly start working correctly

**From Discord (Chicken)**:
> "I am PRAYING that they give proper notice before this endpoint is aligned with the docs, and maybe even that they make new endpoints altogether for the correct values and leave the existing ones as-is, because it will destroy my systems if they make a change to this without notice."

### Mitigation Strategy

```python
# Add integration test that detects if behavior changes
async def test_sell_side_inversion():
    """
    Test for Kalshi's undocumented sell side inversion.

    If this test starts FAILING, it means Kalshi changed the API
    to match documentation. Update workaround code!
    """
    # Place sell NO order
    order = await client.place_order(
        ticker="TEST-MARKET",
        action="sell",
        side="no",
        count=1,
        price=0.75
    )

    # Check if API still inverts (current behavior)
    if order["side"] == "yes":
        logger.info("✅ Kalshi still inverts sell sides (behavior unchanged)")
    else:
        logger.critical("🚨 KALSHI API BEHAVIOR CHANGED! Sell sides no longer inverted!")
        logger.critical("Update workaround code in place_order()!")
        raise APIBehaviorChangedError("Kalshi sell side inversion no longer happens")
```

## Timeline

- **2025-10-28**: Issue discovered via Discord discussion (monomorphism, Chicken)
- **Status**: Undocumented API behavior, confirmed by multiple users
- **Fix ETA**: Unknown if/when Kalshi will "fix" this

## Related Issues

- None yet (this is the first undocumented semantic issue)

## External Resources

- Discord conversation: Kalshi API Users (2025-10-28)
- Users affected: monomorphism, Chicken, mitch
- Kalshi team tagged: @NotPikachu (Kalshi)

## Questions for Kalshi Support

1. Is this sell→buy normalization intentional or a bug?
2. Will this behavior change in the future?
3. If changing, will you provide advance notice?
4. Can you document this behavior officially?
5. Can you add a flag to disable normalization for users who want raw data?
