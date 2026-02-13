# Fix: restore from seed phrase (v4 HD / BIP39)

--8<-- "_includes/safety-banner.md"

**Applies to:** v4.22.x (desktop)

Starting with v4, ReddCoin Core uses an HD wallet model and can create a BIP39 recovery seed phrase for new wallets. [^tg-2025-03-29-2019826]

## When this works (and when it doesn’t)

- **Works best** if your v4 wallet was created as a BIP39/HD wallet and you saved the seed phrase.
- If you restored/migrated via copying `wallet.dat`, the seed phrase may not represent that wallet state; rely on file backups instead. (See: [Restore wallet files](restore-wallet-files.md).)

## Restore steps (high-level)

1. Install the latest **v4.22.x** Core from official sources.
2. Let it synchronize (or use [Clean resync](clean-resync-v4.md) if needed).
3. Use the wallet creation flow to **restore** or **recover** using your BIP39 seed phrase.
4. Encrypt the wallet, and make a fresh `wallet.dat` backup after confirming balances.

!!! success "Admin-verified pattern"
    Admin guidance often pairs “BIP39 seed phrase” with “encrypt wallet.dat + backup wallet.dat” as the practical, redundant backup strategy. [^tg-2025-03-29-2019826] [^tg-2026-01-29-2038543]

## Footnotes

[^tg-2025-03-29-2019826]: Telegram export (ReddCoinOfficial), obito, 29 Mar 2025 06:10 UTC-05, message2019826 (messages976.html). (HD/BIP39 explanation + practical steps + staking notes; includes a release-candidate link in that message, but the HD/seed workflow is the key takeaway.)
[^tg-2026-01-29-2038543]: Telegram export (ReddCoinOfficial), obito, 29 Jan 2026 09:08 UTC-05, message2038543 (messages992.html). (Encrypting wallet.dat is recommended for safety; not mandatory but protects against theft.)
