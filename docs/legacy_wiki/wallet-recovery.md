# Wallet recovery (legacy how-to)

This page summarizes the legacy wiki’s operational guidance for restoring access to an existing wallet.

**Primary source:** `wiki.reddcoin.com/Restore_your_wallet` permalink `oldid=4846`.

## Core idea

If you have a backup wallet file (a `.dat` file), you can restore it by placing it into your **Reddcoin data directory** as `wallet.dat`, then starting Reddcoin Core.

## Default data directories

- **Linux:** `~/.reddcoin`
- **macOS:** `~/Library/Application Support/Reddcoin`
- **Windows:** `%APPDATA%\Reddcoin`

## Safe restore procedure

1. **Close Reddcoin Core** completely.
2. Open the Reddcoin data directory.
3. If a `wallet.dat` already exists, **rename it** (e.g., `old_wallet.dat`).
4. Copy your backup `.dat` file into the directory and name it **`wallet.dat`**.
5. Start Reddcoin Core.
6. Wait until the wallet is fully synced (avoid sending until “out of sync” indicators stop).

## Finding the data directory from inside Core

If you cannot locate the directory:

- Open **Help → Debug window**.
- Use the button that opens the debug log file.
- Search the log for: `Using data directory`.

## Support

If the above steps don’t work, request help in official community channels (see the Community links page) and **never share your wallet file or private keys**.

