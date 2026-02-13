# Fix: v3 → v4 upgrade (clean method)

--8<-- "_includes/safety-banner.md"

**Applies to:** users moving from **Core v3.x** to **Core v4.22.x**

## Why this matters

v3 and v4 blockchains are not compatible, and installing v4 over an old v3 data directory can cause peer-mixing and sync failures unless you reset the blockchain state. [^tg-2025-08-16-2031121] [^tg-2024-09-18-2002895]

## Recommended (safe-default) method

### Step 1 — backup funds

- Backup **v3** `wallet.dat` (File → Backup Wallet).
- Keep a second copy offline.

### Step 2 — install v4 (fresh)

Install the latest v4.22.x from official sources.

### Step 3 — clean the data directory

Close v4, then in the data directory delete or move aside:

- `blocks/`
- `chainstate/`
- `indexes/` (if present)
- `peers.dat`

This “clean update” is the approach admins recommend when moving between major lines. [^tg-2025-08-16-2031121]

### Step 4 — bring your funds into v4

You have two practical options:

1. **Send from v3 to a new v4 address** (preferred for HD seed phrase workflow).
2. **Move/restore wallet files** (see: [Restore wallet files](restore-wallet-files.md)).

## Footnotes

[^tg-2025-08-16-2031121]: Telegram export (ReddCoinOfficial), obito, 16 Aug 2025 14:26 UTC-05, message2031121 (messages986.html). (v3/v4 not compatible; clean update preferred.)
[^tg-2024-09-18-2002895]: Telegram export (ReddCoinOfficial), obito, 18 Sep 2024 06:34 UTC-05, message2002895 (messages962.html). (v4 should connect only to v4 peers; peers.dat can carry old v3 peers.)
