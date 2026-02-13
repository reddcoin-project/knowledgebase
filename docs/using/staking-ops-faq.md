# Staking operations FAQ (PoSV v2)

This page collates **real-world operational guidance** from the public ReddCoin Telegram channel export (Feb 2019 → Feb 2026), with emphasis on **recent years** and admin-authored support.

For current binaries, the official ReddWallet download page lists **Reddcoin Core 4.22.9** as the latest desktop wallet.[^reddwallet4229]

It is intended for practical troubleshooting, not as a protocol spec. For the formal design, see the PoSV v2 docs in **[Technology → Consensus](/tech/consensus/posv-v2.md)**.

!!! warning "Version-specific"
    ReddCoin guidance can be **version-specific**. If you're unsure what you run, start with **[Version matrix](version-matrix.md)** and **[Version compatibility & upgrades](troubleshooting/version-compatibility.md)**.

---

## Starting staking in Core v4 (desktop)

On Core v4.x, staking may require **two explicit actions** after the wallet is fully synced:

1. **Unlock “for staking only”** (you’ll still need the password again to send coins).[^message2021513][^message2012781]  
2. Click the **bottom-right anvil icon → Enable Staking**.[^message2021513][^message2038537]

If staking still doesn't engage on v4.22.8, a workaround shared by admins was to **disable then re-enable staking** after unlocking.[^message2017279]

---

## Minimum “coin age” before coins can stake

Admins repeatedly referenced an **~8 hour minimum coin age** before newly received coins become eligible for staking.[^message2011503][^message2038582]

---

## Offline vs online

- Coin age continues to accumulate whether you are online or offline.[^message1977272]
- But the wallet must be **online** (and staking enabled) to actually mint a staking block.[^message1977272]

---

## “How often will I get rewards?”

PoSV v2 staking is **probabilistic**. Admin guidance commonly frames it as a **competition/race** where having more coins generally increases your chance of minting blocks.[^message1964075]

A common community rule-of-thumb is to use a calculator to estimate average frequency; John Nash noted that a calculator is useful for “how often you will stake”.[^message1964090]

---

## Multiplier, effective reward rate, and network inflation (how people talk about it)

In Telegram support, admins frequently described PoSV v2 in terms of a **dynamic “multiplier”**:

- **Effective annual reward rate** (rule-of-thumb) ≈ `5% * multiplier`.[^message1971842]
- Some admins also described **network inflation** (rule-of-thumb) ≈ `5% / multiplier`.[^message1996461][^message2025586]

!!! info "Where to see the current multiplier"
    Admins referenced checking the multiplier via the community bot (e.g., `/statistics`).[^message1938443]

!!! warning "Treat as operational guidance, not a spec"
    The above formulas reflect how admins explained the system in chat to help users reason about expectations. For protocol-level definitions, see the PoSV v2 paper and source code.

---

## “Why do I see new addresses I didn’t create?”

Two separate behaviors can look similar:

1. **Change addresses:** when you spend from an address/UTXO, the wallet may send the remaining “change” to a new internal address (common wallet behavior).[^message2021534]
2. **Staking internal grouping:** admins explained that the wallet may group large balances internally for staking frequency/variance, without creating on-chain transactions.[^message2020066][^message2021530][^message2030089]

---

## Upgrading v3 → v4: will I lose funds or rewards?

- John Nash stated that if you have a `wallet.dat` backup, **v4 will not cause you to lose funds**—but you must confirm you are on the correct chain (compare to Blockbook).[^message2007420]
- If you continued staking on the **wrong fork** (e.g., v3 during a fork event), those staking rewards exist **on the wrong chain** and do not “carry over” to v4.[^message2007420]

If you suspect you are on the wrong chain, see **[Wrong fork / wrong chain recovery](troubleshooting/wrong-fork.md)**.

---

## HD wallets, seed phrases (BIP39), and encryption (v4 notes)

Admins advised:

- v4 can support **HD wallets with seed phrases** (“BIP39 wallets”), and v4 can host **multiple wallets**.[^message2022388][^message2025586]
- A **time-bound warning (mid-2025)** described a potential mismatch in seed-phrase standard when enabling encryption during wallet creation on some systems; suggested workaround: **create the wallet first, then encrypt it afterward** via settings.[^message2025586]

!!! warning "Time-bound"
    If you are creating a new v4 wallet today, verify current release notes—this was reported during the v4.22.8 → v4.22.9 transition period.[^message2025586]

---

## Footnotes (Telegram export)

[^message2021513]: Telegram export `message2021513` (2025-04-18, admin) — v4 staking steps: unlock “for staking only”, then enable staking via anvil icon.
[^message2012781]: Telegram export `message2012781` (2025-01-21, admin) — explanation of “unlocked for staking only” security behavior.
[^message2038537]: Telegram export `message2038537` (2026-01-29, admin) — staking does not start by default; must sync, unlock for staking only, and enable staking.
[^message2017279]: Telegram export `message2017279` (2025-02-25, admin) — v4.22.8 staking UI workaround (toggle enable staking).
[^message2011503]: Telegram export `message2011503` (2025-01-03, John Nash) — “Minimum is 8hrs” before coins are considered for staking.
[^message2038582]: Telegram export `message2038582` (2026-01-29, John Nash) — reiterated 8-hour minimum coin age for newly transferred funds.
[^message1977272]: Telegram export `message1977272` (2024-01-30, John Nash) — coinage increases offline; must be online to stake.
[^message1964075]: Telegram export `message1964075` (2023-12-18, John Nash) — staking is competitive; more coins → more opportunity.
[^message1964090]: Telegram export `message1964090` (2023-12-18, John Nash) — calculator useful to estimate staking frequency.
[^message1971842]: Telegram export `message1971842` (2024-01-08, admin) — “staking percentage is 5% * multiplier” (rule-of-thumb framing).
[^message1938443]: Telegram export `message1938443` (2023-09-14, admin) — referenced checking multiplier via `/statistics`.
[^message1996461]: Telegram export `message1996461` (2024-04-22, admin) — discussed “actual inflation” vs 5% cap and multiplier-based reasoning.
[^message2020066]: Telegram export `message2020066` (2025-04-01, admin) — staking grouping is internal; coins remain in addresses; no on-chain shuffle.
[^message2021530]: Telegram export `message2021530` (2025-04-18, admin) — internal/virtual split described; no blockchain transactions.
[^message2021534]: Telegram export `message2021534` (2025-04-18, admin) — change addresses explained and contrasted with staking internal split.
[^message2030089]: Telegram export `message2030089` (2025-08-02, John Nash) — referenced UTXO split/combine behavior at larger amounts.
[^message2007420]: Telegram export `message2007420` (2024-11-20, John Nash) — wallet.dat backup protects funds; wrong-chain stakes don’t carry over; compare height to Blockbook.
[^message2022388]: Telegram export `message2022388` (2025-04-28, admin) — v4 fast sync; compare height to Blockbook; restore wallet via seed phrase workflow.
[^message2025586]: Telegram export `message2025586` (2025-06-08, admin) — v4 fast sync + HD wallet guidance + time-bound warning about seed standard mismatch when encrypting during creation.
