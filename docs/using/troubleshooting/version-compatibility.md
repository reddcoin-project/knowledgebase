# Version compatibility & upgrades (v3 → v4)

ReddCoin Core has had multiple major lines in the wild:

- **v3.x** (legacy line)
- **v4.22.x** (current desktop wallet line, based on Bitcoin Core 0.22 heritage)

## Key reality: v3 and v4 do not share a compatible on-disk chain state

Community support repeatedly observed that:

- Running **v4 over a v3 data directory** can cause peer-mixing (v3 peers cached in `peers.dat`) and/or a chain mismatch.
- A common fix after upgrading is a **full resync** (delete `blocks/`, `chainstate/`, `indexes/`, and `peers.dat`, then sync again).
- It is also possible to appear “healthy” while staking on a **wrong fork**, producing rewards that are not recognized on the correct chain.

## Quick upgrade checklist (safe-default)

1. **Backup** `wallet.dat` (and any `wallets/` dir if present).  
2. Install the **current v4 wallet** from the official download site.
3. If you upgraded from v3, plan to **resync v4**:
   - Close the wallet.
   - Delete `blocks/`, `chainstate/`, `indexes/`, and `peers.dat` in the data directory.
   - Restart and let it sync fully.

This specific delete-and-resync procedure (including default data paths for Linux/macOS/Windows) was repeatedly used by admins to resolve “blockchain data file is corrupted” and “incorrect blockchain” cases after v4 upgrades.[^message2035575]


## Current stable wallet (as of Feb 2026)

- The official **ReddWallet** page lists **Reddcoin Core 4.22.9** as the latest desktop wallet.
- Official binaries are hosted under `download.reddcoin.com/bin/` (look for `reddcoin-core-4.22.9/`), including a `SHA256SUMS` file.

> Note: community posts sometimes reference “4.22.10”, but if it is not present on the official download site, treat it as **planned / in-progress** rather than a generally available release.



## Wallet file location difference (v3 vs v4)

If you install v4 fresh, note that `wallet.dat` should live in the **`wallets/`** subfolder (not the root data directory as in v3). See: [Wallets](../wallets.md#wallet-file-locations-walletdat-by-version).


## Data directory locations (defaults)

- **Linux:** `~/.reddcoin`
- **macOS:** `~/Library/Application Support/Reddcoin`
- **Windows:** `%APPDATA%\Reddcoin`

(These are the defaults cited in the admin runbook.[^message2035575])

## When you might be on the wrong fork

Warning signs:

- You see staking activity, but a transaction/txid does not appear on explorers.
- You have unusually few peers, or peers appear to be on mismatched versions.
- Admins explicitly noted “v3 is on a fork of the blockchain” during the 2024 incidents.[^message2000805]

If you suspect this, see: [Wrong fork / wrong chain](wrong-fork.md).

---

## Footnotes

[^message2035575]: Telegram export (ReddCoinOfficial), 2025-11-24, obito, message2035575. Permalink: https://t.me/ReddcoinOfficial/2035575.
[^message2000805]: Telegram export (ReddCoinOfficial), 2024-08-19, John (cryptognasher) Nash, message2000805. Permalink: https://t.me/ReddcoinOfficial/2000805.


## v4-specific notes (HD wallets / seed phrases)

Support admins noted that v4 can support HD wallets with recovery seed phrases and multiple wallet files.[^message2025586]

A **time-bound** warning (mid-2025) described a potential mismatch in seed standard when enabling encryption during wallet creation on some systems; suggested workaround was to create the wallet first, then encrypt afterward.[^message2025586]

## v4 fast sync

Admins also stated that newer v4 builds can synchronize quickly enough that bootstrap is often unnecessary, and recommended verifying your wallet’s “current block height” against Blockbook.[^message2022388]
