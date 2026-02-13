# Known incidents & advisories (curated)

This page records **notable incidents and operational advisories** observed in public channels, prioritized for **recent years** and **team/admin-authored** guidance.

!!! info "How to use this page"
    - For practical fixes, start with **[Troubleshooting](../using/troubleshooting/index.md)**.
    - If you’re unsure what version you run, read **[Version matrix](../using/version-matrix.md)**.

---

## 2024–2026 incident log (high signal)

| Date | Type | What happened | Affected | What users saw | Recommended action | Sources |
|---|---|---|---|---|---|---|
| 2024-01-19 | Release / advisory | Core **v4.22.8** announced (incl. fix for blockchain stalling download) | Desktop wallets | Upgrade questions; sync behavior discussed | Prefer official downloads; treat v3→v4 as clean resync | [^message1975134][^message1975136] |
| 2024-07-05 | Incident | **Wrong-chain / fork** observed; console-level recovery instructions shared | Some nodes; some services | Block heights differ; transactions with certain services fail | Safe-default: delete & resync (optionally bootstrap). Advanced: `invalidateblock <hash>` + restart | [^message1997330][^message1997333] |
| 2024-08-17 | **Update required** | Team tracked incidental chain splits and highlighted conflicts between v4→v3 transaction behavior | Legacy v3 nodes; mixed services | Chainsplits; v3 not accepting certain v4 tx features | Backup and upgrade legacy nodes/services to v4; avoid mixed-version operation | [^message2000580] |
| 2024-09-14 | Incident / diagnostic | Admin published **two known “bad fork” checks** (heights + hashes) and matching `invalidateblock` commands | Nodes on wrong forks | Wallet appears synced but has different blockhash at known heights | Use the published hash checks; for non-experts prefer full resync; experts can invalidate the wrong-fork hash | [^message2002551] |
| 2024-08-22 | Infrastructure | Official **v4 bootstrap** link circulated by lead dev | Users needing fast sync | Slow initial sync; recovery workflows | Use official bootstrap v4; do not mix v3/v4 snapshots | [^message2001059] |
| 2025-12-15 | Roadmap update | Dev update: **v4.22.10** in progress, targeting SegWit/CSV/Taproot with stronger test frameworks | Future release | Community asking for “what’s next” | Track official updates; expect release after functional tests complete | [^message2036694] |
| 2026-02-12 | Operational check | Admin reiterated a **canonical blockhash check** for chain verification | Users diagnosing wrong chain | Wallet “synced” but mismatch suspected | `getblockhash 5519068` should match canonical hash | [^message2039543] |

---

## Notes on “wrong-chain stakes”

Admins repeatedly emphasized that if your wallet is on a wrong fork, “stakes” and transactions may not be recognized once you return to the canonical chain. If you suspect this, follow **[Wrong fork / wrong chain recovery](../using/troubleshooting/wrong-fork.md)** first.

---

## Footnotes


[^message1975134]: Telegram export (ReddCoinOfficial), 2024-01-19, Tech Adept (RDD) reddcoin.com / redd.love, message1975134. Note: Hey, Good news.. 4.22.8 is done. https://download.reddcoin.com/bin/reddcoin-core-4.22.8/ there are 3 changes. 1. Fix for blockchain stalling download [This is a major]. … Permalink: https://t.me/ReddcoinOfficial/1975134.
[^message1975136]: Telegram export (ReddCoinOfficial), 2024-01-19, Tech Adept (RDD) reddcoin.com / redd.love, message1975136. Note: https://github.com/reddcoin-project/reddcoin-0.22/releases/tag/v4.22.8 Permalink: https://t.me/ReddcoinOfficial/1975136.
[^message1997330]: Telegram export (ReddCoinOfficial), 2024-07-05, John (cryptognasher) Nash, message1997330. Note: just to help out here..and for completeness in the console of core wallet invalidateblock 809a59a737c3479ac17ad0fd426193596cc02cfb82cd1c87fa05ef94f8f8587a this will take… Permalink: https://t.me/ReddcoinOfficial/1997330.
[^message1997333]: Telegram export (ReddCoinOfficial), 2024-07-05, obito, message1997333. Note: After the command wrote by John the block heights still doesn't match? Your wallet is on the wrong chain. Until you fix this, you can't use your wallet Permalink: https://t.me/ReddcoinOfficial/1997333.
[^message2000580]: Telegram export (ReddCoinOfficial), 2024-08-17, HPMentjox, message2000580. Note: ‼️ Important - Update Required ‼️ The ReddCoin CoreTeam has been tracking these incidental chainsplits that have happened twice now, and we have found an issue which is … Permalink: https://t.me/ReddcoinOfficial/2000580.
[^message2002551]: Telegram export (ReddCoinOfficial), 2024-09-14, obito, message2002551. Note: We had two bad blockchain splits. First at block 5448005 and the second one at block 5519068. I) To verify if you're on the first bad fork run in the Console of the Core… Permalink: https://t.me/ReddcoinOfficial/2002551.
[^message2001059]: Telegram export (ReddCoinOfficial), 2024-08-22, John (cryptognasher) Nash, message2001059. Note: V4 Bootstrap https://download.reddcoin.com/bin/bootstrap/v4/ Permalink: https://t.me/ReddcoinOfficial/2001059.
[^message2036694]: Telegram export (ReddCoinOfficial), 2025-12-15, John (cryptognasher) Nash, message2036694. Note: Current Development Update - December 2025 Hey Reddcoin Family, As we get close to the end of 2025, I just wanted to give a heads up on where things are at with Reddcoin… Permalink: https://t.me/ReddcoinOfficial/2036694.
[^message2039543]: Telegram export (ReddCoinOfficial), 2026-02-12, obito, message2039543. Note: Run in the Console of the Core Wallet: getblockhash 5519068 Is the output of this command this string of characters? 1d6ebb2d73dccc03b7b9b013c3b08ec8a83919ed4480edbad6e0… Permalink: https://t.me/ReddcoinOfficial/2039543.
