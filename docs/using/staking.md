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

[^message2038537]: Telegram export (ReddCoinOfficial), 2026-01-29, obito, message2038537. Note: The staking does not start by default. To stake you must have the wallet fully synchronized with the network. Then there are two steps: 1) Unlock the wallet "for staking… Permalink: https://t.me/ReddcoinOfficial/2038537.
[^message2011503]: Telegram export (ReddCoinOfficial), 2025-01-03, John (cryptognasher) Nash, message2011503. Note: Minimum is 8hrs. before they are considered for staking. How often will depend on how many coins you have. BTW, well done on sorting out the memory issue. Minimum of 4G … Permalink: https://t.me/ReddcoinOfficial/2011503.
[^message1977272]: Telegram export (ReddCoinOfficial), 2024-01-30, John (cryptognasher) Nash, message1977272. Note: Coinage will increase whether you are online or not. But you do need to be online to stake. Permalink: https://t.me/ReddcoinOfficial/1977272.
