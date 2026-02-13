# Version compatibility & upgrades (v3 → v4)

ReddCoin Core has had multiple major wallet lines in the wild:

- **v3.x** (legacy line)
- **v4.22.x** (current desktop wallet line)

!!! tip "Current status snapshot (Last reviewed: 2026-02-13)"
    - Latest published v4 desktop build folder in the official download index: **4.22.9**
      - https://download.reddcoin.com/bin/
    - Project updates describe work toward **4.22.10** with staged protocol activations (CSV, SegWit, and potentially Taproot). See:
      - https://wordpress.reddcoin.com/index.php/2025/10/01/project-update-october-2025/
      - https://wordpress.reddcoin.com/index.php/2025/11/17/project-update-november-2025/

!!! info "Why upgrades feel “bigger” than expected"
    v4 introduces newer wallet capabilities (including multi-wallet tooling; and, depending on wallet creation flow, seed-phrase style recovery) and also changes what’s safe to reuse from an old install. Plan on a clean resync when moving from v3 → v4.

---

## The critical rule: do not reuse v3 chainstate in v4

Community support repeatedly observed that running v4 over a v3 data directory can cause peer-mixing (v3 peers cached in `peers.dat`) and/or chain mismatch.

**Safe default:** treat v3 → v4 as a clean install for blockchain data.

---

## Quick upgrade checklist (safe-default)

1. **Backup**:
   - `wallet.dat` (and/or the `wallets/` directory if present)
2. Install the current **v4** wallet from official downloads.
3. **Clean resync (recommended)**:
   - Close Core.
   - Delete (or move aside) `blocks/`, `chainstate/`, `indexes/` (if present), and `peers.dat` in the data directory.
   - Start Core and let it fully sync.
   - Optional: use the official **[v4 bootstrap](bootstrap.md)** to speed up sync.

---

## Two field-tested migration methods (v3 funds → v4 wallet)

obito summarized two practical patterns used by community members.[^message1988156]

### Method 1: “New v4 address” (recommended if you want the v4 seed phrase workflow)

1. Open **Reddcoin Core v4** and generate a receiving address.
2. Close v4.
3. Open **v3** and **send** your coins to the v4 address you generated.
4. Now your funds live in a v4 wallet that can be backed up via:
   - v4 recovery seed phrase (HD wallet),
   - `wallet.dat`,
   - and private keys (as applicable).[^message1988156]

### Method 2: “Move wallet.dat” (works, but seed phrase may not be usable as a backup)

If you restore a v4 balance by copying `wallet.dat` across versions, users noted that the **v4 recovery seed phrase may not function as a backup** for that restored wallet state. In this case you should rely on:

- `wallet.dat` backups
- exported private keys (where appropriate)[^message1988156]

---

## If you think you’re on the wrong chain

If deposits/withdrawals don’t arrive, or your “synced” wallet doesn’t match explorers, read:

- **[Wrong fork / wrong chain recovery](wrong-fork.md)**

---

## Footnotes


[^message1988156]: Telegram export (ReddCoinOfficial), 2024-03-23, obito, message1988156. Note: Method 1 - method where you take advantage of the recovery seed phrase v4 HD wallet Open ReddCoin Core Wallet 4.22.8. Generate a receiving address. Close the wallet. Ope… Permalink: https://t.me/ReddcoinOfficial/1988156.
