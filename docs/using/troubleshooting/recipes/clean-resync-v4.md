# Clean resync (v4) — rebuild blockchain data safely

--8<-- "_includes/safety-banner.md"

**Applies to:** ReddCoin Core **v4.22.x** (desktop)

**Use this when:** sync is stuck, wallet is on the wrong chain, or you see database / block corruption messages.

## Before you begin

1. **Close ReddCoin Core completely.**
2. **Backup your wallet files** to an offline location.
   - If you see a `wallets/` folder, back that up.
   - Also back up any `wallet.dat` you find in the data directory.

### Data folder locations

- **Windows:** `%APPDATA%\Reddcoin\`
- **macOS:** `~/Library/Application Support/Reddcoin/`
- **Linux:** `~/.reddcoin/`

These paths were repeatedly referenced in admin troubleshooting steps. [^tg-2025-02-25-2017277]

## Steps

### Step 1 — remove blockchain state (safe)

In the data directory, **delete or move aside**:

- `blocks/`
- `chainstate/`
- `indexes/` (if present)
- `peers.dat`

Then start ReddCoin Core and let it sync again.

!!! success "Admin-verified"
    This “delete blocks/chainstate/indexes + peers.dat” pattern is the standard fix for wrong-chain and sync problems in v4. [^tg-2025-12-22-2036920] [^tg-2025-02-25-2017277]

### Step 2 — optional: use the official v4 bootstrap (faster sync)

If you have slow bandwidth or limited time, you can use the **v4 bootstrap**:

1. Download the v4 bootstrap from the official download host.
2. Extract it into the data directory (it should create `blocks/` and `chainstate/` there).
3. Start Core and let it finish syncing.

The Telegram support guidance points to the official v4 bootstrap directory. [^tg-2025-02-25-2017277]

### Step 3 — last resort: clean reinstall

If you keep hitting the same failure after a clean resync:

1. Backup wallet files again.
2. Uninstall Core.
3. Install the latest v4 release from the official host.
4. Repeat **Step 1**.

Some users also resolved repeated sync failures by doing a clean resync and (if needed) moving between minor v4 releases. [^tg-2025-02-22-2017083]

## When a clean resync is the right move

A clean resync is usually the right first move if you:

- upgraded over an old v3 data directory,
- see “wrong chain” behavior (explorer height doesn’t match),
- see corruption warnings,
- have persistent peer-mixing / connection problems.

## Footnotes

[^tg-2025-12-22-2036920]: Telegram export (ReddCoinOfficial), obito, 22 Dec 2025 03:04 UTC-05, message2036920 (messages991.html). (v4.22.9 sync fix: delete blocks/chainstate/indexes + peers.dat, then resync.)
[^tg-2025-02-25-2017277]: Telegram export (ReddCoinOfficial), obito, 25 Feb 2025 09:51 UTC-05, message2017277 (messages973.html). (Default data folder paths + delete folders + v4 bootstrap.)
[^tg-2025-02-22-2017083]: Telegram export (ReddCoinOfficial), John (cryptognasher) Nash, 22 Feb 2025 15:14 UTC-05, message2017083 (messages973.html). (Clean resync steps including deleting data folders; historical context.)
