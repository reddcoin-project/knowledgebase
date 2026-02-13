# Wallet files & locations (what to back up)

This page is intentionally written for **non-technical users**.

## The one thing that matters

If you only do one thing, do this:

1. **Close the wallet app.**
2. Make a copy of your **wallet files** to an offline place (USB drive / external disk).

### What counts as “wallet files”?

- **ReddCoin Core Desktop (v4.x):** the `wallets/` folder inside the ReddCoin data directory (it contains one or more wallet files).
- **ReddCoin Core Desktop (v3.x):** typically a single `wallet.dat` file inside the data directory.
- **Mobile / seed-phrase wallets:** your **seed phrase** (write it down offline) and any app-specific backups.

> Important: **ReddCoin Core Desktop does not normally give you a seed phrase.** It uses wallet files. If you’re being asked for a seed phrase when you only ever used Core Desktop, pause and verify which wallet app you’re using.

## Default data directory locations

These are the *default* locations. If you set a custom `-datadir`, your files will be elsewhere.

### Windows

- `C:\Users\<YOU>\AppData\Roaming\Reddcoin\`

### macOS

- `~/Library/Application Support/Reddcoin/`

### Linux

- `~/.reddcoin/`

## What you’ll see inside the data directory

| File / folder | What it is | Safe to delete? |
|---|---|---|
| `wallets/` (v4) | Your wallet(s) | **No** |
| `wallet.dat` (v3) | Your wallet (legacy) | **No** |
| `backups/` | Auto/manual backups (if enabled) | No (keep) |
| `blocks/` | Raw blockchain data | Yes (re-download) |
| `chainstate/` | Database state for the chain | Yes (rebuild) |
| `indexes/` | Optional indexes | Yes (rebuild) |
| `peers.dat` | Saved peer addresses | Yes (will regenerate) |
| `debug.log` | Log file | Yes (but keep for troubleshooting) |
| `reddcoin.conf` | Configuration file | Yes (but you may lose custom settings) |

## How to find the folder quickly (easy methods)

### From inside the wallet

Many Core-style wallets have a menu option that opens the data folder (examples: “Open data directory”, “Show debug log”, etc.). If you see that, use it.

### Windows (manual)

1. Press `Win + R`
2. Paste: `%APPDATA%\Reddcoin`
3. Press Enter

### macOS (manual)

1. In Finder, click **Go** in the menu bar
2. Hold **Option** and click **Library**
3. Navigate to **Application Support → Reddcoin**

### Linux (manual)

Use your file manager to show hidden folders, then open `~/.reddcoin/`.

## If you’re moving to a new computer

Use this runbook:

- [Restore wallet files](../using/troubleshooting/recipes/restore-wallet-files.md)

## Sources / further reading

- ReddCoin legacy wiki (curated here): [Wallet recovery](../legacy_wiki/wallet-recovery.md)
- Bitcoin Core wallet file behavior (multi-wallet “wallets/” folder): https://github.com/bitcoin/bitcoin/blob/master/doc/managing-wallets.md
- Data directory conventions: https://en.bitcoin.it/wiki/Data_directory
