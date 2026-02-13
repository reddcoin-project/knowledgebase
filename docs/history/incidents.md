# Known incidents & advisories (curated)

This page records **notable incidents and operational advisories** observed in public channels, prioritized for **recent years** and **team/admin-authored** guidance.

!!! info "How to use this page"
    - For practical fixes, start with **[Troubleshooting](../using/troubleshooting/index.md)**.
    - If you’re unsure what version you run, read **[Version matrix](../using/version-matrix.md)**.

---

## 2024–2026 incident log (high signal)

| Date | Type | What happened | What users saw | Fix / runbook | Notes | Sources |
|---|---|---|---|---|---|---|
| 2024-01-19 | Release / advisory | Core **v4.22.8** announced (incl. fix for blockchain stalling download) | Upgrade/sync questions | [Known-good fixes by version](../using/troubleshooting/known-good-fixes.md) | Prefer official downloads; for v3→v4 follow the upgrade runbook | [^message1975134][^message1975136] |
| 2024-07-05 | Incident | **Wrong-chain / fork** observed; console-level recovery instructions shared | Block heights differ; transactions with certain services fail | [Wrong fork / chain split](../using/troubleshooting/recipes/wrong-fork-chain-split.md) | Safe-default: clean resync (optionally bootstrap). Advanced: `invalidateblock <hash>` + restart | [^message1997330][^message1997333] |
| 2024-08-17 | **Update required** | Team tracked incidental chain splits and highlighted conflicts between v4→v3 transaction behavior | Chainsplits; v3 not accepting certain v4 tx features | [v3 → v4 upgrade](../using/troubleshooting/recipes/v3-to-v4-upgrade.md) | Upgrade legacy nodes/services to v4; avoid mixed-version operation | [^message2000580] |
| 2024-09-14 | Incident / diagnostic | Admin published **two known “bad fork” checks** (heights + hashes) and matching `invalidateblock` commands | Wallet appears synced but blockhash differs at known heights | [Wrong fork / chain split](../using/troubleshooting/recipes/wrong-fork-chain-split.md) | Non-experts: full resync. Experts: invalidate wrong-fork hash, then reorg | [^message2002551] |
| 2024-08-22 | Infrastructure | Official **v4 bootstrap** link circulated by lead dev | Slow initial sync; recovery workflows | [Bootstrap](../using/troubleshooting/bootstrap.md) | Use official bootstrap v4; do not mix v3/v4 snapshots | [^message2001059] |
| 2025-04-09 | Release | **4.22.9** published (downloads + release post) | v4 desktop wallet users | Upgrade questions; sync behavior; general maintenance release | [Releases hub](../news/releases.md) | Prefer official downloads; follow version-compatibility guidance | [^wp-4.22.9] |
| 2025-06-26 | Exchange advisory | **Xeggex shutting down** (exchange closure notice) | Users with funds on Xeggex | Potential loss of access / withdrawals depending on exchange status | [Markets & exchanges](../ecosystem/markets.md) | If you still have access, withdraw to self-custody; treat centralized exchanges as temporary | [^wp-xeggex] |
| 2025-10-01 | Development update | **4.22.10** described as a major protocol upgrade path (SegWit/CSV activations), plus exchange reliability concerns | Community | Confusion about “released vs. planned”; timing of upgrades | [Version compatibility & upgrades](../using/troubleshooting/version-compatibility.md) | Verify latest published builds via download index; track monthly project updates for timelines | [^wp-update-oct2025] |
| 2025-11-17 | Development update | Testing progress update; next release focuses on **CSV, SegWit, Taproot (stretch goal)** | Community | Expectations-setting about testing duration | [Releases hub](../news/releases.md) | Treat as “in progress” until a build appears in the official download index | [^wp-update-nov2025] |
| 2025-12-15 | Roadmap update | Dev update: **v4.22.10** in progress, targeting SegWit/CSV/Taproot with stronger test frameworks | Community asking for “what’s next” | [Roadmap / Backlog](../roadmap.md) | Track official updates; expect release after functional tests complete | [^message2036694] |
| 2026-02-13 | Operational check | Admin reiterated a **canonical blockhash check** for chain verification | Wallet “synced” but mismatch suspected | [Wrong fork / chain split](../using/troubleshooting/recipes/wrong-fork-chain-split.md) | `getblockhash 5519068` should match canonical hash | [^message2039543] |

---

## Notes on “wrong-chain stakes”

Admins repeatedly emphasized that if your wallet is on a wrong fork, “stakes” and transactions may not be recognized once you return to the canonical chain. If you suspect this, start with **[Wrong fork / chain split](../using/troubleshooting/recipes/wrong-fork-chain-split.md)**.

---

## Footnotes


[^message1975134]: Telegram export (ReddCoinOfficial), 2024-01-19, Tech Adept (RDD) https://reddcoin.com / https://redd.love, message1975134. Note: Hey, Good news.. 4.22.8 is done. https://download.reddcoin.com/bin/reddcoin-core-4.22.8/ there are 3 changes. 1. Fix for blockchain stalling download [This is a major]. … Permalink: https://t.me/ReddcoinOfficial/1975134.
[^message1975136]: Telegram export (ReddCoinOfficial), 2024-01-19, Tech Adept (RDD) https://reddcoin.com / https://redd.love, message1975136. Note: https://github.com/reddcoin-project/reddcoin-0.22/releases/tag/v4.22.8 Permalink: https://t.me/ReddcoinOfficial/1975136.
[^message1997330]: Telegram export (ReddCoinOfficial), 2024-07-05, John (cryptognasher) Nash, message1997330. Note: just to help out here..and for completeness in the console of core wallet invalidateblock 809a59a737c3479ac17ad0fd426193596cc02cfb82cd1c87fa05ef94f8f8587a this will take… Permalink: https://t.me/ReddcoinOfficial/1997330.
[^message1997333]: Telegram export (ReddCoinOfficial), 2024-07-05, obito, message1997333. Note: After the command wrote by John the block heights still doesn't match? Your wallet is on the wrong chain. Until you fix this, you can't use your wallet Permalink: https://t.me/ReddcoinOfficial/1997333.
[^message2000580]: Telegram export (ReddCoinOfficial), 2024-08-17, HPMentjox, message2000580. Note: ‼️ Important - Update Required ‼️ The ReddCoin CoreTeam has been tracking these incidental chainsplits that have happened twice now, and we have found an issue which is … Permalink: https://t.me/ReddcoinOfficial/2000580.
[^message2002551]: Telegram export (ReddCoinOfficial), 2024-09-14, obito, message2002551. Note: We had two bad blockchain splits. First at block 5448005 and the second one at block 5519068. I) To verify if you're on the first bad fork run in the Console of the Core… Permalink: https://t.me/ReddcoinOfficial/2002551.
[^message2001059]: Telegram export (ReddCoinOfficial), 2024-08-22, John (cryptognasher) Nash, message2001059. Note: V4 Bootstrap https://download.reddcoin.com/bin/bootstrap/v4/ Permalink: https://t.me/ReddcoinOfficial/2001059.
[^message2036694]: Telegram export (ReddCoinOfficial), 2025-12-15, John (cryptognasher) Nash, message2036694. Note: Current Development Update - December 2025 Hey Reddcoin Family, As we get close to the end of 2025, I just wanted to give a heads up on where things are at with Reddcoin… Permalink: https://t.me/ReddcoinOfficial/2036694.
[^message2039543]: Telegram export (ReddCoinOfficial), 2026-02-13, obito, message2039543. Note: Run in the Console of the Core Wallet: getblockhash 5519068 Is the output of this command this string of characters? 1d6ebb2d73dccc03b7b9b013c3b08ec8a83919ed4480edbad6e0… Permalink: https://t.me/ReddcoinOfficial/2039543.

[^wp-4.22.9]: ReddCoin News (WordPress), “Reddcoin 4.22.9 Release”, 2025-04-09. https://wordpress.reddcoin.com/index.php/2025/04/09/reddcoin-4-22-9-release/
[^wp-xeggex]: ReddCoin News (WordPress), “Xeggex Shutting Down”, 2025-06-26. https://wordpress.reddcoin.com/index.php/2025/06/26/xeggex-shutting-down/
[^wp-update-oct2025]: ReddCoin News (WordPress), “Project Update – October 2025”, 2025-10-01. https://wordpress.reddcoin.com/index.php/2025/10/01/project-update-october-2025/
[^wp-update-nov2025]: ReddCoin News (WordPress), “Project Update – November 2025”, 2025-11-17. https://wordpress.reddcoin.com/index.php/2025/11/17/project-update-november-2025/
