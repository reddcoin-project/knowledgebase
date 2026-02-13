# PoSV v2 & Enhanced Staking (PoSVv2)

PoSV v2 (Proof-of-Stake-Velocity v2) is a **consensus-breaking protocol upgrade** to ReddCoin’s original PoSV design.
It was introduced to:

1. **Restore the intended ~5% annual network growth/inflation target** (PoSV design target)
2. **Increase security** by incentivizing more wallets to be online staking
3. **Create a sustainable development funding stream** for long-term maintenance and ecosystem growth

!!! tip "TL;DR"
    - **Base target remains ~5% annual growth** (PoSV design target).  
    - **Enhanced Staking Rewards (ESR)** multiply the staking reward when *staking participation is low*.  
    - **Developer Fund** splits **8%** of the stake reward to a dedicated funding address once activated.  
    - This is a **hard fork / consensus fork**: you must run an upgraded wallet/node to stay on the main chain.

---

## Why PoSV v2 exists

ReddCoin observed that *not enough holders were actually staking*, because coins often sit on exchanges, paper wallets, or otherwise offline.
That weakens security and also reduces the realized growth rate versus the original design intent (PoSV’s ~5% nominal rate).

PoSV v2 addresses this by **rewarding active stakers more when fewer wallets are staking**, while keeping the network’s overall growth on target.

---

## What changed in PoSV v2

PoSV v2 introduces two major changes on top of PoSV.

### 1) Enhanced Staking Rewards (ESR)

PoSV v2 applies a **staking participation multiplier** so that *active stakers are rewarded more* when fewer wallets are staking.

Conceptually:

- Let **P** be the protocol’s estimate of *staking participation* (as a fraction, e.g., 0.20 = 20%).
- The **multiplier M** is approximately **M = 1 / P**.
- M is recalculated as the network changes (implementation details are in code and release notes).

**Examples given in the PoSV v2 paper:**
- If only ~20% of the network is staking (P ≈ 0.20), the reward multiplier is ~5×.
- If staking participation rises to ~50% (P ≈ 0.50), the multiplier is ~2×.

> Practical meaning: PoSV v2 strongly incentivizes people to stake **in the official wallet** (and keep it online), especially when network participation is low.

### 2) Developers Funding Address (8% split)

PoSV v2 also introduced an on-chain, protocol-level development funding mechanism:

- **8% of the stake reward** is routed to a **Developers Funding Address** (once the new rules activate).
- This is meant to replace ad-hoc donations and support ongoing maintenance, releases, infrastructure, and growth work.

In other words, the staker receives the reward **minus** the dev-fund portion, and the dev fund receives the remainder automatically.

---

## Reward calculation (mental model)

PoSV v2’s staking reward can be thought of as a pipeline:

1. Start with the **base PoSV reward** (built around a ~5% nominal annual target).
2. Apply the **ESR multiplier** based on staking participation.
3. Split the final stake reward:
   - **92%** → paid to the staking wallet
   - **8%** → Developers Funding Address

### Formula (simplified)

Let:

- **R_base** = base PoSV staking reward
- **M** = ESR multiplier (≈ 1 / P)
- **f_dev** = 0.08

Then:

- **R_total = R_base × M**
- **R_user = R_total × (1 − f_dev)**
- **R_dev  = R_total × f_dev**

!!! note
    This is the *conceptual* model used to explain PoSV v2. Exact consensus logic (including how P is computed) lives in the implementation and release notes.

---

## Fork and activation behavior

PoSV v2 was shipped as a **hard fork / consensus-breaking upgrade**, coordinated via ReddCoin Core releases.

### Planned fork height

The “Faith, Hope & Charity” announcement described an expected activation around **block 3,000,000 (3M)**.

### Activation gating (v5 blocks threshold)

Core release notes describe that PoSV v2 rules (and the dev-fund split) only **take effect after a threshold of upgraded blocks**:

- Activation after **90% of the network** (i.e., **9000 / 10000 recent blocks**) are producing the upgraded block version (**v5**),
- Where 10,000 blocks ≈ **7 days worth of blocks**.

This type of “activation gating” helps avoid unstable split-chain behavior during rollout.

---

## What users need to do

### If you hold RDD in your own wallet

- **Upgrade your wallet** before (or as soon as) the fork is active.
- Being on the wrong chain can lead to serious issues (including coins becoming hard to recover in practice).
- Staking is built into the wallet—keep it online to participate.

### If you hold RDD on an exchange or third-party service

- You do **not always** need to withdraw, *as long as the service upgrades*.
- If you’re unsure whether a service will upgrade promptly, withdrawing to a local wallet can reduce risk.

!!! warning
    Always verify you are running the **latest official release** and are on the **main chain** during any consensus upgrade.

---

## FAQ highlights (from the PoSV v2 FAQ)

### Can I improve returns by manually moving coins between my own addresses?
No. “Shuffling” coins can reset eligibility / coin age and generally harms your expected staking results. The wallet handles staking automatically.

### What returns should I expect?
The FAQ describes **~5% per annum on average** as the baseline target, with PoSV v2 applying a multiplier based on staking participation (meaning returns can be higher when fewer wallets stake).

### Do I need to upgrade my wallet?
Yes. This was a **hard fork**; older clients are not compatible with the post-fork chain.

---

## Diagrams

### Reward pipeline

```mermaid
flowchart LR
  A[Base PoSV staking reward\n(~5% nominal target)] --> B[Compute staking participation P]
  B --> C[Enhanced Staking multiplier\nM ≈ 1 / P]
  C --> D[Total stake reward\nR_total = R_base × M]
  D --> E[User payout\nR_user = R_total × 0.92]
  D --> F[Dev fund payout\nR_dev = R_total × 0.08]
```

### Activation gating (simplified)

```mermaid
flowchart TB
  A[Network before upgrade] --> B[Users/Exchanges upgrade to PoSVv2 wallet]
  B --> C[Upgraded nodes produce v5 blocks]
  C --> D{≥ 90% of last 10,000 blocks are v5?}
  D -- No --> C
  D -- Yes --> E[PoSV v2 consensus rules enforced\n(including dev-fund split)]
```

---

## References and further reading

- PoSV v2 paper (Aug 2019): [ReddPaper PoSV v2 (Summer 2019)](../../assets/docs/ReddPaper-PoSV-v2-Summer-2019.pdf)
- PoSV v2 FAQ (Aug 2019): [PoSV v2 FAQ](../../assets/docs/ReddPaper-PoSV-v2-FAQ.pdf)
- Official fork announcement: “Faith, Hope & Charity” — <https://www.reddcoin.com/faith-hope-charity-official-announcement-reddcoin-rdd-upcoming-consensus-fork-posv-v2-protocol-enhancement/>
- Core release notes: Official Release v3.0 PoSV2 — <https://www.reddcoin.com/official-release-v3-0-posv2/>
- (Optional) Broader explanation: “RDD PoSV v2 with Enhanced Staking…” — <https://www.reddcoin.com/rdd-posv-v2-with-enhanced-staking-a-simple-core-wallet-upgrade-and-a-quantum-leap-forward-for-reddcoin-rdd/>

## Activation / enforcement

See: [PoSV v2 activation & enforcement](posv-v2-activation.md)


---

## Legacy PoSV (historical)

# PoSV (Proof-of-Stake-Velocity)

PoSV is a consensus approach that emphasizes:

- **Stake** (ownership)
- **Velocity** (activity)

The design aims to support a usable currency (store of value + medium of exchange) rather than rewarding pure hoarding.

## References

- PoSV v2 FAQ / Redd Paper
