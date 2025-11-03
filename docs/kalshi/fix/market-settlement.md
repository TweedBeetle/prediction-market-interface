---
url: https://docs.kalshi.com/fix/market-settlement
title: Market Settlement - API Documentation
description: Settlement reports for market outcomes and position resolution
scraped_at: 2025-11-03T14:46:33.754449
---

[Skip to main content](https://docs.kalshi.com/fix/market-settlement#content-area)

[API Documentation home page![light logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)![dark logo](https://mintcdn.com/kalshi-b198743e/LjaX_RZSj3IuB_Zg/logo.svg?fit=max&auto=format&n=LjaX_RZSj3IuB_Zg&q=85&s=8cb4d2ff7d6d4e72624d957b5c6a84be)](https://docs.kalshi.com/)

Search...

Ctrl K

Search...

Navigation

Market Settlement

[Welcome](https://docs.kalshi.com/welcome)
[Quick Start](https://docs.kalshi.com/getting_started/quick_start_market_data)
[Reference](https://docs.kalshi.com/getting_started/making_your_first_request)
[API](https://docs.kalshi.com/api-reference/exchange/get-exchange-status)
[Websockets](https://docs.kalshi.com/websockets/websocket-connection)
[SDKs](https://docs.kalshi.com/sdks/overview)
[FIX](https://docs.kalshi.com/fix)
[Changelog](https://docs.kalshi.com/changelog)

On this page

*   [Market Settlement](https://docs.kalshi.com/fix/market-settlement#market-settlement)
    
*   [Overview](https://docs.kalshi.com/fix/market-settlement#overview)
    
*   [Market Settlement Report (35=UMS)](https://docs.kalshi.com/fix/market-settlement#market-settlement-report-35%3Dums)
    
*   [Message Structure](https://docs.kalshi.com/fix/market-settlement#message-structure)
    
*   [Repeating Groups](https://docs.kalshi.com/fix/market-settlement#repeating-groups)
    
*   [Party Information (NoMarketSettlementPartyIDs)](https://docs.kalshi.com/fix/market-settlement#party-information-nomarketsettlementpartyids)
    
*   [Collateral Changes (NoCollateralAmountChanges)](https://docs.kalshi.com/fix/market-settlement#collateral-changes-nocollateralamountchanges)
    
*   [Fees (NoMiscFees)](https://docs.kalshi.com/fix/market-settlement#fees-nomiscfees)
    
*   [Settlement Process](https://docs.kalshi.com/fix/market-settlement#settlement-process)
    
*   [Market Resolution Flow](https://docs.kalshi.com/fix/market-settlement#market-resolution-flow)
    
*   [Settlement Calculations](https://docs.kalshi.com/fix/market-settlement#settlement-calculations)
    
*   [Example Settlement Report](https://docs.kalshi.com/fix/market-settlement#example-settlement-report)
    
*   [Pagination](https://docs.kalshi.com/fix/market-settlement#pagination)
    
*   [Settlement Timing](https://docs.kalshi.com/fix/market-settlement#settlement-timing)
    
*   [Integration Considerations](https://docs.kalshi.com/fix/market-settlement#integration-considerations)
    
*   [1\. Position Reconciliation](https://docs.kalshi.com/fix/market-settlement#1-position-reconciliation)
    
*   [2\. Multi-Account Handling](https://docs.kalshi.com/fix/market-settlement#2-multi-account-handling)
    
*   [3\. Fee Processing](https://docs.kalshi.com/fix/market-settlement#3-fee-processing)
    
*   [Best Practices](https://docs.kalshi.com/fix/market-settlement#best-practices)
    
*   [Real-time Processing](https://docs.kalshi.com/fix/market-settlement#real-time-processing)
    
*   [Batch Processing](https://docs.kalshi.com/fix/market-settlement#batch-processing)
    
*   [Related Systems](https://docs.kalshi.com/fix/market-settlement#related-systems)
    
*   [Error Scenarios](https://docs.kalshi.com/fix/market-settlement#error-scenarios)
    
*   [Missing Settlements](https://docs.kalshi.com/fix/market-settlement#missing-settlements)
    
*   [Incorrect Positions](https://docs.kalshi.com/fix/market-settlement#incorrect-positions)
    

[​](https://docs.kalshi.com/fix/market-settlement#market-settlement)

Market Settlement
=========================================================================================

[​](https://docs.kalshi.com/fix/market-settlement#overview)

Overview
-----------------------------------------------------------------------

Market settlement messages provide information about market outcomes and the resulting position settlements. These messages are available on:

*   **KalshiPT** (Post Trade) sessions
*   **KalshiRT** sessions when `ReceiveSettlementReports=Y` in Logon

Settlement occurs when a market’s outcome is determined, triggering automatic position resolution and fund transfers.

[​](https://docs.kalshi.com/fix/market-settlement#market-settlement-report-35%3Dums)

Market Settlement Report (35=UMS)
-------------------------------------------------------------------------------------------------------------------------

Provides settlement details for a specific market.

### 

[​](https://docs.kalshi.com/fix/market-settlement#message-structure)

Message Structure

| Tag | Name | Description | Required |
| --- | --- | --- | --- |
| 20105 | MarketSettlementReportID | Unique settlement identifier | Yes |
| 55  | Symbol | Market ticker (e.g., NHIGH-23JAN02-66) | Yes |
| 715 | ClearingBusinessDate | Date settlement cleared (YYYYMMDD) | Yes |
| 20106 | TotNumMarketSettlementReports | Total number of settlement reports in sequence | No  |
| 20107 | MarketResult | Result of the market when determined | Yes |
| 893 | LastFragment | Last page indicator (Y/N) | No  |
| 730 | SettlementPrice | Settlement price of market | Yes |

### 

[​](https://docs.kalshi.com/fix/market-settlement#repeating-groups)

Repeating Groups

#### 

[​](https://docs.kalshi.com/fix/market-settlement#party-information-nomarketsettlementpartyids)

Party Information (NoMarketSettlementPartyIDs)

| Tag | Name | Description |
| --- | --- | --- |
| 20108 | NoMarketSettlementPartyIDs | Number of parties |
| 20109 | MarketSettlementPartyID | Unique identifier for party |
| 20110 | MarketSettlementPartyRole | Type of party (Customer Account<24>) |
| 704 | LongQty | Number of YES contracts held |
| 705 | ShortQty | Number of NO contracts held |

#### 

[​](https://docs.kalshi.com/fix/market-settlement#collateral-changes-nocollateralamountchanges)

Collateral Changes (NoCollateralAmountChanges)

| Tag | Name | Description |
| --- | --- | --- |
| 1703 | NoCollateralAmountChanges | Number of collateral changes (should be only 1 - payout balance change) |
| 1704 | CollateralAmountChange | Delta in dollars |
| 1705 | CollateralAmountType | Balance<1> or Payout<2> |

#### 

[​](https://docs.kalshi.com/fix/market-settlement#fees-nomiscfees)

Fees (NoMiscFees)

| Tag | Name | Description |
| --- | --- | --- |
| 136 | NoMiscFees | Number of fees (currently zero, single item with zeroed values) |
| 137 | MiscFeeAmt | Total fees for settlement in dollars |
| 138 | MiscFeeCurr | Currency (USD) |
| 139 | MiscFeeType | Type of fee (Exchange fees<4>) |
| 891 | MiscFeeBasis | Unit for fee (Absolute<0>) |

[​](https://docs.kalshi.com/fix/market-settlement#settlement-process)

Settlement Process
-------------------------------------------------------------------------------------------

### 

[​](https://docs.kalshi.com/fix/market-settlement#market-resolution-flow)

Market Resolution Flow

### 

[​](https://docs.kalshi.com/fix/market-settlement#settlement-calculations)

Settlement Calculations

For each position:

*   **Yes outcome**: Yes contract holders receive $1 per contract
*   **No outcome**: No contract holders receive $1 per contract
*   **Net position**: Only net positions are settled (after netting)

[​](https://docs.kalshi.com/fix/market-settlement#example-settlement-report)

Example Settlement Report
---------------------------------------------------------------------------------------------------------

Copy

Ask AI

    // Market settled as "Yes"
    8=FIXT.1.1|35=UMS|
    20105=settle-123|55=HIGHNY-23DEC31|715=20231231|
    20107=Yes|
    20108=1|
      20109=user-456|20110=24|
      704=100|705=0|
      1703=1|
        1704=10000|1705=1|
      136=1|
        137=0.00|138=USD|139=4|891=0|
    893=Y|
    

This example shows:

*   Market HIGHNY-23DEC31 settled as “Yes”
*   User held 100 Yes contracts
*   Received $100.00 (10000 cents) to balance
*   No settlement fees

[​](https://docs.kalshi.com/fix/market-settlement#pagination)

Pagination
---------------------------------------------------------------------------

Large settlement batches may span multiple messages:

| Tag | Use Case |
| --- | --- |
| 20106 | Total number of reports in batch |
| 893 | LastFragment=N for more pages, Y for last |

[​](https://docs.kalshi.com/fix/market-settlement#settlement-timing)

Settlement Timing
-----------------------------------------------------------------------------------------

Markets typically settle shortly after expiration, but timing can vary based on:

*   Market type
*   Data source availability
*   Manual review requirements

[​](https://docs.kalshi.com/fix/market-settlement#integration-considerations)

Integration Considerations
-----------------------------------------------------------------------------------------------------------

### 

[​](https://docs.kalshi.com/fix/market-settlement#1-position-reconciliation)

1\. Position Reconciliation

Copy

Ask AI

    def reconcile_settlement(report):
        # Verify position matches records
        our_position = get_position(report.Symbol)
    
        if report.LongQty != our_position.yes_contracts:
            alert("Position mismatch", report)
    
        # Verify payout calculation
        if report.MarketResult == "Yes":
            expected_payout = report.LongQty * 100  # cents
        else:
            expected_payout = report.ShortQty * 100
    
        if report.CollateralAmountChange != expected_payout:
            alert("Payout mismatch", report)
    

### 

[​](https://docs.kalshi.com/fix/market-settlement#2-multi-account-handling)

2\. Multi-Account Handling

For sessions managing multiple accounts:

*   Each party (sub-account) receives separate entry
*   Aggregate by MarketSettlementPartyID
*   Track settlements per account

### 

[​](https://docs.kalshi.com/fix/market-settlement#3-fee-processing)

3\. Fee Processing

Currently settlement fees are zero, but implement handling for future changes:

*   Parse NoMiscFees group
*   Account for fees in P&L calculations
*   Track fee types for reporting

[​](https://docs.kalshi.com/fix/market-settlement#best-practices)

Best Practices
-----------------------------------------------------------------------------------

### 

[​](https://docs.kalshi.com/fix/market-settlement#real-time-processing)

Real-time Processing

1

Subscribe to Reports

Set ReceiveSettlementReports=Y in KalshiRT Logon

2

Process Immediately

Update positions and balances in real-time

3

Reconcile

Compare with expected outcomes and positions

4

Update Risk

Adjust risk calculations for settled positions

### 

[​](https://docs.kalshi.com/fix/market-settlement#batch-processing)

Batch Processing

For post-trade reconciliation:

1.  Connect to KalshiPT session
2.  Query for day’s settlements
3.  Process in sequence order
4.  Generate settlement reports

[​](https://docs.kalshi.com/fix/market-settlement#related-systems)

Related Systems
-------------------------------------------------------------------------------------

| System | Purpose |
| --- | --- |
| Order Entry | Track positions leading to settlement |
| Drop Copy | Audit trail of trades |
| Market Data | Market expiration times |
| REST API | Query market details and outcomes |

[​](https://docs.kalshi.com/fix/market-settlement#error-scenarios)

Error Scenarios
-------------------------------------------------------------------------------------

### 

[​](https://docs.kalshi.com/fix/market-settlement#missing-settlements)

Missing Settlements

If settlements are missing:

1.  Check connection to appropriate session
2.  Verify ReceiveSettlementReports flag
3.  Use REST API as backup data source
4.  Contact support if discrepancies persist

### 

[​](https://docs.kalshi.com/fix/market-settlement#incorrect-positions)

Incorrect Positions

Position mismatches may indicate:

*   Missed execution reports
*   Incorrect position tracking
*   Late trades near expiration

Always maintain independent position tracking for verification.

[Drop Copy Session](https://docs.kalshi.com/fix/drop-copy)
[Error Handling](https://docs.kalshi.com/fix/error-handling)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.