# Recipe: export/import a private key (advanced)

--8<-- "_includes/safety-banner.md"

**Applies to:** Core desktop wallets (use with extreme care)

## When you’d use this

- You can’t migrate normally but you still control an address in your wallet
- You need to recover a single address/UTXO into another wallet
- A support admin/dev explicitly asked you to export a key for debugging

!!! warning
    Exported private keys can be stolen if you paste them into chat or store them insecurely. Treat them like cash.

## How to export (Core console)

1. Open **Tools → Debug console**
2. Run:

- `dumpprivkey <your_public_address>`

## How to import (Core console)

- `importprivkey <your_private_key>`

Admins noted that file backups (`wallet.dat` / `wallets/`) are generally preferable, but provided these console commands when needed. [^tg-2024-08-27-2001368]

## v4 note: wallet file location

When restoring `wallet.dat` on v4, guidance cautions to place it inside the `wallets/` folder rather than the root data directory. [^tg-2024-08-27-2001368]

## Footnotes

[^tg-2024-08-27-2001368]: Telegram export (ReddCoinOfficial), obito, 27 Aug 2024 06:16 UTC-05, message2001368 (messages961.html). (dumpprivkey/importprivkey commands; prefer wallet.dat; place wallet.dat in wallets folder for v4.)
