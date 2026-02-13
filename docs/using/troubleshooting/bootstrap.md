# Bootstrap (speed up initial sync)

A **bootstrap** is a packaged snapshot of chain data that can dramatically reduce first-time sync, and can also help recover from certain “stuck sync / wrong chain” states.

!!! warning "Version-specific"
    Do **not** mix v3 and v4 data directories. Use the bootstrap that matches the wallet line you run.

---

## Official bootstrap locations (recommended)

The official download server provides bootstrap snapshots for multiple wallet lines:

- Bootstrap index: `https://download.reddcoin.com/bin/bootstrap/`[^bootstrap_index]
  - **v4**: `https://download.reddcoin.com/bin/bootstrap/v4/`[^bootstrap_v4_listing]
  - **v3 archive**: `https://download.reddcoin.com/bin/bootstrap/v3-archive/`[^bootstrap_v3_listing]

John Nash also posted the v4 bootstrap location publicly on Telegram.[^message2001059]

---

## How to use a bootstrap safely (Core v4)

1. **Close** Reddcoin Core.
2. **Backup** your wallet(s):
   - If you have a single legacy wallet: backup `wallet.dat`.
   - If you have multiple wallets: backup the entire `wallets/` directory (plus `wallet.dat` if it exists).
3. In the Reddcoin data directory:
   - Delete (or move aside) `blocks/`, `chainstate/`, `indexes/` (if present), and `peers.dat`.
   - **Do not delete** your wallet files.
4. Download and extract `bootstrap_v4.zip` (or `.tar.gz`) from the official v4 directory.[^bootstrap_v4_listing]
5. Copy the extracted `blocks/` and `chainstate/` into your Reddcoin data directory.
6. Start Core and let it finish syncing.

If you see errors after bootstrapping, revert to the safe-default **delete-and-resync** procedure in **[Corrupted blockchain / resync](corrupted-blockchain.md)**.

---

## Legacy note: v2/v3 “bootstrap.dat” threads

Older community guides (especially pre-v4) often reference `bootstrap.dat`. That was a **legacy mechanism** and may not match v4 packaging. If you’re reading old forum threads, confirm which wallet line they reference before applying steps.

---

## Footnotes

[^bootstrap_index]: Official directory listing: https://download.reddcoin.com/bin/bootstrap/ (shows `v3-archive/` and `v4/`).  
[^bootstrap_v4_listing]: Official directory listing: https://download.reddcoin.com/bin/bootstrap/v4/ (includes `bootstrap_v4.zip` / `bootstrap_v4.tar.gz` and the block height marker file).  
[^bootstrap_v3_listing]: Official directory listing: https://download.reddcoin.com/bin/bootstrap/v3-archive/ (archived v3 snapshot).  


[^message2001059]: Telegram export (ReddCoinOfficial), 2024-08-22, John (cryptognasher) Nash, message2001059. Note: V4 Bootstrap https://download.reddcoin.com/bin/bootstrap/v4/ Permalink: https://t.me/ReddcoinOfficial/2001059.
