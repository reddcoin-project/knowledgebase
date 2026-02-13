---
title: ReddID name cost calculator
---

ReddID is ReddCoin’s **social identity layer**. Names are intentionally priced to balance:

- **affordability**
- **anti-squatting incentives**
- **real-world value anchoring**

## Official calculator (hosted)

The community-released calculator is hosted here:  
https://reddcoin-project.github.io/reddid-name-calculator/

<iframe
  src="https://reddcoin-project.github.io/reddid-name-calculator/"
  style="width:100%;height:750px;border:1px solid rgba(0,0,0,0.15);border-radius:12px"
  title="ReddID name cost calculator"
  loading="lazy"
></iframe>

## “Logic” summary (builder-ready)

- Prices are **scenario-plannable** using adjustable BTC/RDD assumptions.
- Names are intended to be **case-insensitive**.
- Some character choices affect cost:
  - vowels can cost more
  - underscores/symbols can reduce cost

<details>
<summary><strong>Deep dive: where fees go</strong></summary>

As discussed publicly, fees are designed to flow back to the network (e.g., via staking rewards), aligning the identity system with community security incentives.
</details>

## Next steps for builders

- Read the ReddID Architecture Spec (Builders → ReddID → Technical architecture)
- Review Namespaces and schema pages for storage/integration assumptions
