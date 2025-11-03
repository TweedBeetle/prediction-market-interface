---
url: https://docs.polymarket.com/developers/builders/relayer-client
title: Relayer Client - Polymarket Documentation
description: Use Polymarket's Polygon relayer to execute gasless transactions for your users
scraped_at: 2025-11-03T15:04:08.492079
---

[Skip to main content](https://docs.polymarket.com/developers/builders/relayer-client#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

Ctrl K

Search...

Navigation

Polymarket Builders Program

Relayer Client

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

On this page

*   [Overview](https://docs.polymarket.com/developers/builders/relayer-client#overview)
    
*   [Installation](https://docs.polymarket.com/developers/builders/relayer-client#installation)
    
*   [Quick Start](https://docs.polymarket.com/developers/builders/relayer-client#quick-start)
    
*   [Relayer URL](https://docs.polymarket.com/developers/builders/relayer-client#relayer-url)
    
*   [Basic Setup](https://docs.polymarket.com/developers/builders/relayer-client#basic-setup)
    
*   [Remote Signing](https://docs.polymarket.com/developers/builders/relayer-client#remote-signing)
    
*   [Core Features](https://docs.polymarket.com/developers/builders/relayer-client#core-features)
    
*   [Deploying Safe Wallets](https://docs.polymarket.com/developers/builders/relayer-client#deploying-safe-wallets)
    
*   [Setting Token Approvals](https://docs.polymarket.com/developers/builders/relayer-client#setting-token-approvals)
    
*   [Monitoring Transaction Status](https://docs.polymarket.com/developers/builders/relayer-client#monitoring-transaction-status)
    
*   [Transaction States](https://docs.polymarket.com/developers/builders/relayer-client#transaction-states)
    
*   [CTF Operations](https://docs.polymarket.com/developers/builders/relayer-client#ctf-operations)
    
*   [Split Positions](https://docs.polymarket.com/developers/builders/relayer-client#split-positions)
    
*   [Merge Positions](https://docs.polymarket.com/developers/builders/relayer-client#merge-positions)
    
*   [Redeem Positions](https://docs.polymarket.com/developers/builders/relayer-client#redeem-positions)
    
*   [Transaction Metadata](https://docs.polymarket.com/developers/builders/relayer-client#transaction-metadata)
    
*   [TypeScript Types](https://docs.polymarket.com/developers/builders/relayer-client#typescript-types)
    
*   [Contract Addresses](https://docs.polymarket.com/developers/builders/relayer-client#contract-addresses)
    
*   [Polygon Mainnet](https://docs.polymarket.com/developers/builders/relayer-client#polygon-mainnet)
    
*   [Resources](https://docs.polymarket.com/developers/builders/relayer-client#resources)
    
*   [Support](https://docs.polymarket.com/developers/builders/relayer-client#support)
    

[​](https://docs.polymarket.com/developers/builders/relayer-client#overview)

Overview
----------------------------------------------------------------------------------------

The Polymarket Relayer Client allows builders to route on-chain transactions through Polymarket’s Polygon relayer infrastructure. This provides several key benefits:

*   **Gasless Transactions**: Polymarket pays for all gas fees on your behalf
*   **Safe Wallet Deployment**: Deploy _Safe Wallets_ for your users and customers
*   **Token Approvals**: Set allowances for trading tokens
*   **CTF Operations**: Execute Conditional Token Framework (CTF) operations including:
    *   Splitting positions
    *   Merging positions
    *   Redeeming positions
    *   Converting positions

[​](https://docs.polymarket.com/developers/builders/relayer-client#installation)

Installation
------------------------------------------------------------------------------------------------

Copy

Ask AI

    npm install @polymarket/builder-relayer-client
    # or
    pnpm install @polymarket/builder-relayer-client
    

[​](https://docs.polymarket.com/developers/builders/relayer-client#quick-start)

Quick Start
----------------------------------------------------------------------------------------------

### 

[​](https://docs.polymarket.com/developers/builders/relayer-client#relayer-url)

Relayer URL

The Polymarket relayer is publicly available at:

Copy

Ask AI

    https://relayer-v2.polymarket.com/
    

### 

[​](https://docs.polymarket.com/developers/builders/relayer-client#basic-setup)

Basic Setup

The relayer client supports both Ethers v5 and Viem wallets:

Ethers v5

Viem

Copy

Ask AI

    import { ethers } from "ethers";
    import { RelayClient } from "@polymarket/builder-relayer-client";
    import { BuilderApiKeyCreds, BuilderConfig } from "@polymarket/builder-signing-sdk";
    
    const relayerUrl = process.env.POLYMARKET_RELAYER_URL;
    const chainId = 137; // Polygon mainnet
    
    // Create wallet
    const provider = new ethers.providers.JsonRpcProvider(process.env.RPC_URL);
    const wallet = new ethers.Wallet(process.env.PRIVATE_KEY, provider);
    
    // Configure builder credentials
    const builderCreds: BuilderApiKeyCreds = {
        key: process.env.BUILDER_API_KEY!,
        secret: process.env.BUILDER_SECRET!,
        passphrase: process.env.BUILDER_PASS_PHRASE!
    };
    
    const builderConfig = new BuilderConfig({
        localBuilderCreds: builderCreds
    });
    
    // Initialize client
    const client = new RelayClient(relayerUrl, chainId, wallet, builderConfig);
    

### 

[​](https://docs.polymarket.com/developers/builders/relayer-client#remote-signing)

Remote Signing

For enhanced security, you can use remote signing to keep your builder credentials on a secure server:

Copy

Ask AI

    import { BuilderConfig } from "@polymarket/builder-signing-sdk";
    
    const builderConfig = new BuilderConfig({
        remoteBuilderConfig: {url: "http://localhost:3000/sign"}
    });
    
    const client = new RelayClient(relayerUrl, chainId, wallet, builderConfig);
    

[​](https://docs.polymarket.com/developers/builders/relayer-client#core-features)

Core Features
--------------------------------------------------------------------------------------------------

### 

[​](https://docs.polymarket.com/developers/builders/relayer-client#deploying-safe-wallets)

Deploying Safe Wallets

Deploy a Safe wallet for your user with a single call. Polymarket pays the gas fees:

Copy

Ask AI

    const response = await client.deploySafe();
    const result = await response.wait();
    
    if (result) {
        console.log("Safe deployed successfully!");
        console.log("Transaction Hash:", result.transactionHash);
        console.log("Safe Address:", result.proxyAddress);
    } else {
        console.log("Safe deployment failed");
    }
    

### 

[​](https://docs.polymarket.com/developers/builders/relayer-client#setting-token-approvals)

Setting Token Approvals

Set token allowances to enable trading. This example approves USDC spending for the Conditional Token Framework:

Copy

Ask AI

    import { ethers } from "ethers";
    import { Interface } from "ethers/lib/utils";
    import { OperationType, SafeTransaction } from "@polymarket/builder-relayer-client";
    
    // Define ERC20 approval interface
    const erc20Interface = new Interface([{\
        "constant": false,\
        "inputs": [\
            {"name": "_spender", "type": "address"},\
            {"name": "_value", "type": "uint256"}\
        ],\
        "name": "approve",\
        "outputs": [{"name": "", "type": "bool"}],\
        "payable": false,\
        "stateMutability": "nonpayable",\
        "type": "function"\
    }]);
    
    // Create approval transaction
    function createApprovalTransaction(
        tokenAddress: string,
        spenderAddress: string
    ): SafeTransaction {
        return {
            to: tokenAddress,
            operation: OperationType.Call,
            data: erc20Interface.encodeFunctionData("approve", [\
                spenderAddress,\
                ethers.constants.MaxUint256\
            ]),
            value: "0"
        };
    }
    
    // Execute the approval
    const usdcAddress = "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174";
    const ctfAddress = "0x4d97dcd97ec945f40cf65f87097ace5ea0476045";
    
    const approvalTx = createApprovalTransaction(usdcAddress, ctfAddress);
    const response = await client.executeSafeTransactions(
        [approvalTx],
        "Approve USDC for CTF"
    );
    
    const result = await response.wait();
    console.log("Approval completed:", result?.transactionHash);
    

### 

[​](https://docs.polymarket.com/developers/builders/relayer-client#monitoring-transaction-status)

Monitoring Transaction Status

The relayer client provides built-in transaction monitoring:

Copy

Ask AI

    // Automatic waiting (recommended)
    const response = await client.executeSafeTransactions(transactions);
    const result = await response.wait();
    
    if (result) {
        console.log("Transaction confirmed:", result.transactionHash);
        console.log("Transaction state:", result.state);
    } else {
        console.log("Transaction failed or timed out");
    }
    

[​](https://docs.polymarket.com/developers/builders/relayer-client#transaction-states)

Transaction States
------------------------------------------------------------------------------------------------------------

Transactions move through the following states:

*   `STATE_NEW`: Transaction received by relayer
*   `STATE_EXECUTED`: Transaction executed on-chain
*   `STATE_MINED`: Transaction included in a block
*   `STATE_CONFIRMED`: Transaction confirmed (final state)
*   `STATE_FAILED`: Transaction failed (terminal state)
*   `STATE_INVALID`: Transaction rejected as invalid (terminal state)

[​](https://docs.polymarket.com/developers/builders/relayer-client#ctf-operations)

CTF Operations
----------------------------------------------------------------------------------------------------

The relayer client enables you to execute Conditional Token Framework operations for your users:

### 

[​](https://docs.polymarket.com/developers/builders/relayer-client#split-positions)

Split Positions

Split collateral tokens into conditional tokens representing different outcomes:

Copy

Ask AI

    import { Interface } from "ethers/lib/utils";
    import { OperationType, SafeTransaction } from "@polymarket/builder-relayer-client";
    
    const ctfInterface = new Interface([\
        "function splitPosition(address collateralToken, bytes32 parentCollectionId, bytes32 conditionId, uint[] partition, uint amount)"\
    ]);
    
    const splitTx: SafeTransaction = {
        to: ctfAddress,
        operation: OperationType.Call,
        data: ctfInterface.encodeFunctionData("splitPosition", [\
            collateralToken,\
            parentCollectionId,\
            conditionId,\
            partition,\
            amount\
        ]),
        value: "0"
    };
    
    const response = await client.executeSafeTransactions([splitTx], "Split position");
    const result = await response.wait();
    

### 

[​](https://docs.polymarket.com/developers/builders/relayer-client#merge-positions)

Merge Positions

Merge conditional tokens back into collateral:

Copy

Ask AI

    const ctfInterface = new Interface([\
        "function mergePositions(address collateralToken, bytes32 parentCollectionId, bytes32 conditionId, uint[] partition, uint amount)"\
    ]);
    
    const mergeTx: SafeTransaction = {
        to: ctfAddress,
        operation: OperationType.Call,
        data: ctfInterface.encodeFunctionData("mergePositions", [\
            collateralToken,\
            parentCollectionId,\
            conditionId,\
            partition,\
            amount\
        ]),
        value: "0"
    };
    
    const response = await client.executeSafeTransactions([mergeTx], "Merge position");
    const result = await response.wait();
    

### 

[​](https://docs.polymarket.com/developers/builders/relayer-client#redeem-positions)

Redeem Positions

Redeem winning conditional tokens for collateral after market resolution:

Copy

Ask AI

    const ctfInterface = new Interface([\
        "function redeemPositions(address collateralToken, bytes32 parentCollectionId, bytes32 conditionId, uint[] indexSets)"\
    ]);
    
    const redeemTx: SafeTransaction = {
        to: ctfAddress,
        operation: OperationType.Call,
        data: ctfInterface.encodeFunctionData("redeemPositions", [\
            collateralToken,\
            parentCollectionId,\
            conditionId,\
            indexSets\
        ]),
        value: "0"
    };
    
    const response = await client.executeSafeTransactions([redeemTx], "Redeem position");
    const result = await response.wait();
    

### 

[​](https://docs.polymarket.com/developers/builders/relayer-client#transaction-metadata)

Transaction Metadata

Use descriptive metadata to track transaction purposes:

Metadata is limited to 500 characters or less

Copy

Ask AI

    await client.executeSafeTransactions(
        transactions,
        "User deposit: 100 USDC for market ABC123"
    );
    

[​](https://docs.polymarket.com/developers/builders/relayer-client#typescript-types)

TypeScript Types
--------------------------------------------------------------------------------------------------------

The relayer client is fully typed. Key types include:

Copy

Ask AI

    interface SafeTransaction {
        to: string;
        operation: OperationType;
        data: string;
        value: string;
    }
    
    enum OperationType {
        Call = 0,
        DelegateCall = 1
    }
    
    enum RelayerTransactionState {
        STATE_NEW = "STATE_NEW",
        STATE_EXECUTED = "STATE_EXECUTED",
        STATE_MINED = "STATE_MINED",
        STATE_CONFIRMED = "STATE_CONFIRMED",
        STATE_FAILED = "STATE_FAILED",
        STATE_INVALID = "STATE_INVALID"
    }
    
    interface RelayerTransaction {
        transactionID: string;
        transactionHash: string;
        from: string;
        to: string;
        proxyAddress: string;
        data: string;
        state: string;
        type: string;
        metadata: string;
        createdAt: Date;
        updatedAt: Date;
    }
    

[​](https://docs.polymarket.com/developers/builders/relayer-client#contract-addresses)

Contract Addresses
------------------------------------------------------------------------------------------------------------

### 

[​](https://docs.polymarket.com/developers/builders/relayer-client#polygon-mainnet)

Polygon Mainnet

*   **USDC**: `0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174`
*   **CTF (Conditional Token Framework)**: `0x4d97dcd97ec945f40cf65f87097ace5ea0476045`
*   **CTF Exchange**: `0x4bFb41d5B3570DeFd03C39a9A4D8dE6Bd8B8982E`
*   **Neg Risk CTF Exchange**: `0xC5d563A36AE78145C45a50134d48A1215220f80a`

These addresses are commonly used for token approvals and CTF operations.

[​](https://docs.polymarket.com/developers/builders/relayer-client#resources)

Resources
------------------------------------------------------------------------------------------

*   [Builder Relayer Client Repository](https://github.com/Polymarket/builder-relayer-client)
    
*   [Example Code](https://github.com/Polymarket/builder-relayer-client/tree/main/examples)
    
*   [Order Attribution Guide](https://docs.polymarket.com/developers/builders/order-attribution)
    

[​](https://docs.polymarket.com/developers/builders/relayer-client#support)

Support
--------------------------------------------------------------------------------------

If you encounter issues or have questions about using the relayer client, please contact [support@polymarket.com](mailto:support@polymarket.com)
.

[Builder Signing Server](https://docs.polymarket.com/developers/builders/builder-signing-server)
[CLOB Introduction](https://docs.polymarket.com/developers/CLOB/introduction)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.