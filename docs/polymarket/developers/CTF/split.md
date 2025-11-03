---
url: https://docs.polymarket.com/developers/CTF/split
title: Splitting USDC - Polymarket Documentation
scraped_at: 2025-11-03T15:04:05.463735
---

[Skip to main content](https://docs.polymarket.com/developers/CTF/split#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

Ctrl K

Search...

Navigation

Conditional Token Frameworks

Splitting USDC

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

At any time, after a condition has been prepared on the CTF contract (via `prepareCondition`), it is possible to “split” collateral into a full (position) set. In other words, one unit USDC can be split into 1 YES unit and 1 NO unit. If splitting from the collateral, the CTF contract will attempt to transfer `amount` collateral from the message sender to itself. If successful, `amount` stake will be minted in the split target positions. If any of the transfers, mints, or burns fail, the transaction will revert. The transaction will also revert if the given partition is trivial, invalid, or refers to more slots than the condition is prepared with. This operation happens via the `splitPosition()` function on the CTF contract with the following parameters:

*   `collateralToken`: IERC20 - The address of the positions’ backing collateral token.
*   `parentCollectionId`: bytes32 - The ID of the outcome collections common to the position being split and the split target positions. Null in Polymarket case.
*   `conditionId`: bytes32 - The ID of the condition to split on.
*   `partition`: uint\[\] - An array of disjoint index sets representing a nontrivial partition of the outcome slots of the given condition. E.G. A|B and C but not A|B and B|C (is not disjoint). Each element’s a number which, together with the condition, represents the outcome collection. E.G. 0b110 is A|B, 0b010 is B, etc. In the Polymarket case 1|2.
*   `amount` - The amount of collateral or stake to split. Also the number of full sets to receive.

[Overview](https://docs.polymarket.com/developers/CTF/overview)
[Merging Tokens](https://docs.polymarket.com/developers/CTF/merge)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.