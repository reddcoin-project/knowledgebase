# Version matrix (what’s current vs legacy)

This page helps you quickly identify what guidance applies to your wallet/node.

!!! warning "Reality check"
    A lot of community advice on the internet is **time-bound**. Always confirm:
    1) what version you run, and 2) whether you are on the correct chain.

---

## Wallet / node lines commonly seen

### Core v4.22.x (current desktop line)

- **Who should use it:** most users staking today (desktop).
- **Binaries:** v4.22.9 downloads include multiple Linux architectures (including ARM tarballs); verify which build matches your device.[^download4229]
- **Notable operational differences:**
  - May require “unlock for staking only” + an explicit “Enable Staking” action (anvil icon).[^message2038537]
  - v4 introduced faster sync behavior; bootstrap is often unnecessary on modern releases.[^message2025586]
  - Supports multiple wallets and HD wallet restore flows (seed phrase) depending on configuration.[^message2022388]

### Core v3.10.x (legacy line)

- **Who might still have it:** older desktop installs; some long-running nodes.
- **Important:** during 2024 incidents, admins attributed chain splits to **old wallets** and urged upgrades.[^message2000580]
- **Upgrade path:** v3 → v4 often requires a **full resync** (see [Version compatibility & upgrades](troubleshooting/version-compatibility.md)).

### Core v2.x and older (very legacy)

- **Who might still have it:** extremely old installs or services.
- **Risk:** admins noted v2 nodes still existed and were implicated in splits alongside v3.[^message2000511]

---

## Practical “which page do I read?”

- Staking UX steps (anvil icon, staking toggle): **v4** → [Staking ops FAQ](staking-ops-faq.md)
- Chain mismatch or missing transactions: [Wrong fork / wrong chain](troubleshooting/wrong-fork.md)
- Upgrade checklist: [Version compatibility & upgrades](troubleshooting/version-compatibility.md)

---

## Footnotes (Telegram export)

[^message2038537]: Telegram export `message2038537` (2026-01-29, admin) — staking does not start by default in v4; sync + unlock + enable staking.
[^message2025586]: Telegram export `message2025586` (2025-06-08, admin) — v4 fast sync guidance and time-bound wallet-creation notes.
[^message2022388]: Telegram export `message2022388` (2025-04-28, admin) — compare wallet block height to Blockbook; seed restore steps.
[^message2000580]: Telegram export `message2000580` (2024-08-17, admin) — “Important - Update Required” advisory about old wallets and chain splits.
[^message2000511]: Telegram export `message2000511` (2024-08-16, admin) — chainsplits created by old wallets, including v2 nodes.


[^download4229]: Download index for ReddCoin Core v4.22.9 binaries (dated 2025-04-09). See `download.reddcoin.com/bin/reddcoin-core-4.22.9/`.
