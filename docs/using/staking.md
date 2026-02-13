# Staking (PoSV / PoSV v2)

Staking is built into the core wallet.

!!! info "See also"
    For protocol-level explanations, see **[PoSV v2 & Enhanced Staking](../tech/consensus/posv-v2.md)** and the PoSV v2 documents under **[Reference](../reference/index.md)**.

!!! warning "Version-specific"
    Staking UX differs by wallet line. Start with **[Version matrix](version-matrix.md)**.

## How to stake (practical)

1. Install and fully sync ReddCoin Core (v4 recommended).
2. Encrypt wallet (optional but recommended).
3. Unlock **for staking only**.
4. On Core v4, also click the **bottom-right anvil icon → Enable Staking**.[^message2038537]
5. Keep the wallet online to participate and earn rewards.

## Operational notes (from support)

- Newly received coins may need **~8 hours** before being eligible to stake.[^message2011503]
- Coin age continues to accumulate offline, but you must be online to mint.[^message1977272]
- v4 can require explicit “Enable Staking” action; staking may not start by default.[^message2038537]

For a deeper operational runbook (including multiplier talk, address/change behavior, and v3→v4 migration caveats), see **[Staking operations FAQ](staking-ops-faq.md)**.

## References

- PoSV v2 FAQ (Aug 2019)
- Redd Paper / PoSV v2 paper (Aug 2019)

## Footnotes (Telegram export)

[^message2038537]: Telegram export `message2038537` (2026-01-29, admin) — staking requires sync + unlock for staking only + anvil icon enable.
[^message2011503]: Telegram export `message2011503` (2025-01-03, John Nash) — referenced ~8 hour minimum coin age.
[^message1977272]: Telegram export `message1977272` (2024-01-30, John Nash) — coinage accumulates offline; must be online to stake.
