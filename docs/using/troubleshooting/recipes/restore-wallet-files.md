# Fix: restore wallet files / move to a new computer

--8<-- "_includes/safety-banner.md"

**Applies to:** v4.22.x (desktop) — also useful for v3.x concepts

## What to backup

- `wallet.dat` (legacy single-wallet file)
- `wallets/` directory (v4 multiwallet storage)

Admins repeatedly remind users that `wallet.dat` contains private keys and should be backed up before troubleshooting. [^tg-2024-08-27-2001366]

## Restore workflow (v4)

### Option A — restore an existing v4 wallet folder

1. Close Core
2. Copy your backed-up `wallets/` folder into the data directory
3. Start Core and select the wallet (if prompted)

### Option B — recreate `wallets/` then move `wallet.dat` in

If your `wallets/` folder is missing or damaged, one field-tested approach is:

1. Save your `wallet.dat` **outside** the data directory (desktop, USB, etc.)
2. Delete the `wallets/` folder
3. Start Core and create a **blank wallet** (so Core recreates `wallets/`)
4. Move your `wallet.dat` into the newly created `wallets/` folder [^tg-2024-12-26-2010851]

This approach was suggested as a practical fix when the `wallets/` folder structure needs to be rebuilt.

## After restore: rescan if balances look wrong

If your wallet loads but balances/transactions look incomplete, you may need a **rescan** (see: [Reindex & rescan](../reindex-rescan.md)).

## Footnotes

[^tg-2024-08-27-2001366]: Telegram export (ReddCoinOfficial), John (cryptognasher) Nash, 27 Aug 2024 06:03 UTC-05, message2001366 (messages961.html). (`wallet.dat` contains private keys; backup is critical.)
[^tg-2024-12-26-2010851]: Telegram export (ReddCoinOfficial), obito, 26 Dec 2024 16:53 UTC-05, message2010851 (messages968.html). (Delete wallets folder, create blank wallet, move wallet.dat into wallets.)
