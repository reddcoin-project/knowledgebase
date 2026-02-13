# Known incidents & advisories (curated)

This page records **notable incidents and operational advisories** observed in the public ReddCoin Telegram channel export (Feb 2019 → Feb 2026), prioritized for **recent years** and **team/admin-authored** guidance.

!!! info "How to use this page"
    - If you are troubleshooting a wallet today, start with **[Troubleshooting](../using/troubleshooting/index.md)**.
    - If you’re unsure what version you run, read **[Version matrix](../using/version-matrix.md)**.

---

## 2024–2026 incident log (high signal)

| Date (UTC) | What happened | Affected | What users saw | Recommended action | Sources |
|---|---|---|---|---|---|
| 2024-01-19 | Core v4.22.8 release announced | Desktop wallets | Upgrade questions; download links circulated | Prefer official downloads; expect resync when moving v3 → v4 | [^message1975134][^message1975136] |
| 2024-08-17 | **Advisory:** Update required; old wallets implicated in chain splits | v2/v3 nodes; some services | Chain splits attributed to legacy nodes; v4 tx features rejected by v3 | Backup, upgrade legacy nodes to v4; coordinate with exchanges/services | [^message2000580][^message2000511] |
| 2024-09-14 | **Incident:** two “bad fork” events at specific block heights | Nodes on wrong fork | Wrong chain, misleading staking, tx issues, explorers disagree | Verify block hashes; use `invalidateblock` on the bad hash or resync with clean chainstate | [^message2002551] |
| 2025-02-25 | **Known issue:** v4.22.8 staking UX bug (toggle needed) | v4.22.8 | Staking not engaging even when unlocked | Unlock for staking → enable staking → if needed disable/enable staking icon | [^message2017279] |
| 2025-02-17 → 2025-02-26 | v4.22.9 release candidates (rc1/rc2) circulated; sync issues reported resolved | v4 line | Improved ability to sync from genesis/bootstrap | Upgrade and resync; bootstrap optional | [^message2017927][^message2017951][^message2017953][^download4229rc] |
| 2025-04-09 | v4.22.9 final binaries published on download site; ReddWallet page points to 4.22.9 as latest | Desktop wallets | “What version should I use?” | Prefer v4.22.9; verify checksums; resync if coming from v3 | [^download4229][^reddwallet4229] |
| 2025-04-28 | v4.22.9 fast sync guidance and seed restore steps shared | v4.22.9+ | Faster sync; HD wallet restore flows | Use “Window → Information” to compare height vs Blockbook; restore via “Create/Restore Wallet…” | [^message2022388] |
| 2025-06-08 | **Time-bound advisory:** potential seed-standard mismatch when encrypting during wallet creation (some setups) | v4 wallets (reported mid-2025) | Concern about BIP39/BIP44 mismatch at creation time | Create wallet unencrypted → then encrypt afterward; verify seed works | [^message2025586] |

---

## 2024-09 “bad fork” details (block heights + hashes)

Admins documented **two splits** and provided a deterministic way to check which chain you're on, using the Core debug console.[^message2002551]

### Fork 1 — height 5,448,005

Run:

- `getblockhash 5448005`

Expected (correct chain):

- `99e1ba495f4da89c2a0c8a0296cb1df69d5a76488c06517a5aee5c0000c496da`

Wrong-chain hash (bad fork):

- `809a59a737c3479ac17ad0fd426193596cc02cfb82cd1c87fa05ef94f8f8587a`

If on the wrong hash, admin instructions were:

- `invalidateblock 809a59a737c3479ac17ad0fd426193596cc02cfb82cd1c87fa05ef94f8f8587a`

### Fork 2 — height 5,519,068

Run:

- `getblockhash 5519068`

Expected (correct chain):

- `1d6ebb2d73dccc03b7b9b013c3b08ec8a83919ed4480edbad6e0604be53f5b40`

Wrong-chain hash (bad fork):

- `420d82c48eea24cd9a06b24cc012bb89abdcab95bdbc29ef02d9fd55ef41f570`

If on the wrong hash, admin instructions were:

- `invalidateblock 420d82c48eea24cd9a06b24cc012bb89abdcab95bdbc29ef02d9fd55ef41f570`

!!! warning "Advanced recovery"
    `invalidateblock` is an expert feature. Always back up `wallet.dat` first, and prefer the safe-default resync path in **[Wrong fork / wrong chain recovery](../using/troubleshooting/wrong-fork.md)** unless you know exactly what you're doing.

---

## Footnotes (Telegram export)

[^message1975134]: Telegram export `message1975134` (2024-01-19, TechAdept) — announcement that v4.22.8 is “done” with download link.
[^message1975136]: Telegram export `message1975136` (2024-01-19, TechAdept) — GitHub repository link for v4.22.8.
[^message2000580]: Telegram export `message2000580` (2024-08-17, admin) — “Important - Update Required” advisory about old wallets causing chain splits.
[^message2000511]: Telegram export `message2000511` (2024-08-16, admin) — “chainsplits were created by old wallets” note.
[^message2002551]: Telegram export `message2002551` (2024-09-14, admin) — detailed chain-split diagnosis + `getblockhash` and `invalidateblock` instructions.
[^message2017279]: Telegram export `message2017279` (2025-02-25, admin) — v4.22.8 staking enable/disable workaround.
[^message2017927]: Telegram export `message2017927` (2025-03-04, John Nash) — release resolved blockchain sync issue; can sync from genesis or bootstrap.
[^message2017951]: Telegram export `message2017951` (2025-03-05, John Nash) — request for feedback on v4.22.9rc2.
[^message2017953]: Telegram export `message2017953` (2025-03-05, admin) — v4.22.9rc2 availability announcement.
[^message2022388]: Telegram export `message2022388` (2025-04-28, admin) — v4.22.9 fast sync, compare height vs Blockbook, restore via seed phrase UI flow.
[^message2025586]: Telegram export `message2025586` (2025-06-08, admin) — time-bound warning about seed standard mismatch if encrypting during wallet creation, plus recommended workaround.
