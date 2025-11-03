---
url: https://docs.polymarket.com/developers/neg-risk/overview
title: Overview - Polymarket Documentation
scraped_at: 2025-11-03T15:04:09.275768
---

[Skip to main content](https://docs.polymarket.com/developers/neg-risk/overview#content-area)

[Polymarket Documentation home page![light logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-light.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=a5d3469d0a3a79a41f8d2c92c526ac1a)![dark logo](https://mintcdn.com/polymarket-292d1b1b/YUHnSq4JdekVofRY/logo/logo-dark.svg?fit=max&auto=format&n=YUHnSq4JdekVofRY&q=85&s=4ef5b023ddd4145812e02d98c48e33b6)](https://docs.polymarket.com/)

Search...

Ctrl K

Search...

Navigation

Negative Risk

Overview

[User Guide](https://docs.polymarket.com/polymarket-learn/get-started/what-is-polymarket)
[For Developers](https://docs.polymarket.com/quickstart/introduction/main)
[Changelog](https://docs.polymarket.com/changelog/changelog)

On this page

*   [Augmented Negative Risk](https://docs.polymarket.com/developers/neg-risk/overview#augmented-negative-risk)
    
*   [Original Outcomes](https://docs.polymarket.com/developers/neg-risk/overview#original-outcomes)
    
*   [Placeholder Outcomes](https://docs.polymarket.com/developers/neg-risk/overview#placeholder-outcomes)
    
*   [Explicit Other](https://docs.polymarket.com/developers/neg-risk/overview#explicit-other)
    

Certain events which meet the criteria of being “winner-take-all” may be deployed as **“negative risk”** events/markets. The Gamma API includes a boolean field on events, `negRisk`, which indicates whether the event is negative risk. Negative risk allows for increased capital efficiency by relating all markets within events via a convert action. More explicitly, a NO share in any market can be converted into 1 YES share in all other markets. Converts can be exercised via the [Negative Adapter](https://polygonscan.com/address/0xd91E80cF2E7be2e162c6513ceD06f1dD0dA35296)
. You can read more about negative risk [here](https://github.com/Polymarket/neg-risk-ctf-adapter)
.

* * *

[​](https://docs.polymarket.com/developers/neg-risk/overview#augmented-negative-risk)

Augmented Negative Risk
----------------------------------------------------------------------------------------------------------------

There is a known issue with the negative risk architecture which is that the outcome universe must be complete before conversions are made or otherwise conversion will “cost” something. In most cases, the outcome universe can be made complete by deploying all the named outcomes and then an “other” option. But in some cases this is undesirable as new outcomes can come out of nowhere and you’d rather them be directly named versus grouped together in an “other”. To fix this, some markets use a system of **“augmented negative risk”**, where named outcomes, a collection of unnamed outcomes, and an _other_ is deployed. When a new outcome needs to be added, an unnamed outcome can be clarified to be the new outcome via the bulletin board. This means the “other” in the case of augmented negative risk can effectively change definitions (outcomes can be taken out of it). As such, trading should only happen on the named outcomes, and the other outcomes should be ignored until they are named or until resolution occurs. The Polymarket UI will not show unnamed outcomes. If a market becomes resolvable and the correct outcome is not named (originally or via placeholder clarification), it should resolve to the _“other”_ outcome. An event can be considered “augmented negative risk” when `enableNegRisk` is true **AND** `negRiskAugmented` is true. The naming conventions are as follows:

### 

[​](https://docs.polymarket.com/developers/neg-risk/overview#original-outcomes)

Original Outcomes

*   Outcome A
*   Outcome B
*   …

### 

[​](https://docs.polymarket.com/developers/neg-risk/overview#placeholder-outcomes)

Placeholder Outcomes

*   Person A -> can be clarified to a named outcome
*   Person B -> can be clarified to a named outcome
*   …

### 

[​](https://docs.polymarket.com/developers/neg-risk/overview#explicit-other)

Explicit Other

*   Other -> not meant to be traded as the definition of this changes as placeholder outcomes are clarified to named outcomes

[Proxy wallet](https://docs.polymarket.com/developers/proxy-wallet)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.