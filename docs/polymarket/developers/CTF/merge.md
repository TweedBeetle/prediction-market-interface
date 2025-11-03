---
url: https://docs.polymarket.com/developers/CTF/merge
title: Merging Tokens - Polymarket Documentation
scraped_at: 2025-11-03T15:04:05.250060
---

[Skip to main content](https://docs.polymarket.com/developers/CTF/merge#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

Ctrl K

Search...

Navigation

Conditional Token Frameworks

Merging Tokens

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

In addition to splitting collateral for a full set, the inverse can also happen; a full set can be “merged” for collateral. This operation can again happen at any time after a condition has been prepared on the CTF contract. One unit of each position in a full set is burned in return for 1 collateral unit. This operation happens via the `mergePositions()` function on the CTF contract with the following parameters:

*   `collateralToken`: IERC20 - The address of the positions’ backing collateral token.
*   `parentCollectionId`: bytes32 - The ID of the outcome collections common to the position being merged and the merge target positions. Null in Polymarket case.
*   `conditionId`: bytes32 - The ID of the condition to merge on.
*   `partition`: uint\[\] - An array of disjoint index sets representing a nontrivial partition of the outcome slots of the given condition. E.G. A|B and C but not A|B and B|C (is not disjoint). Each element’s a number which, together with the condition, represents the outcome collection. E.G. 0b110 is A|B, 0b010 is B, etc. In the Polymarket case 1|2.
*   `amount` - The number of full sets to merge. Also the amount of collateral to receive.

[Splitting USDC](https://docs.polymarket.com/developers/CTF/split)
[Reedeeming Tokens](https://docs.polymarket.com/developers/CTF/redeem)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.