# Fix: exchange deposits / withdrawals don’t show up

--8<-- "_includes/safety-banner.md"

**Applies to:** all users interacting with exchanges

This page is intentionally conservative: exchanges are third parties, and the safest default is self-custody.

## Step 1 — rule out scams first

If anyone DMs you offering “help” with a missing deposit/withdrawal, treat it as a scam attempt and keep the discussion public. [^tg-2024-12-25-2010662]

## Step 2 — verify on-chain reality

1. Get your **txid** from the sending platform (exchange/wallet).
2. Check the txid in a public explorer / Blockbook.
3. Confirm:
   - the transaction exists,
   - confirmations are accruing,
   - the destination address matches what you intended.

(If the tx doesn’t exist on-chain, it’s an exchange-side issue.)

## Step 3 — confirm you’re on the correct chain

If you’re receiving into Core and your wallet “looks synced” but doesn’t match explorers, fix your wallet first:

- [Wrong fork / chain split](wrong-fork-chain-split.md)
- [Clean resync (v4)](clean-resync-v4.md)

## Step 4 — contact the exchange (with evidence)

Provide:

- txid
- address
- timestamp (UTC)
- number of confirmations observed on the explorer

## Caution: exchange risk & low-liquidity warnings

Admins periodically warn about exchange operational risk (low volume, regulatory uncertainty) and recommend withdrawing to self-custody when possible. [^tg-2026-01-30-2038600]

## Footnotes

[^tg-2024-12-25-2010662]: Telegram export (ReddCoinOfficial), obito, 25 Dec 2024 15:24 UTC-05, message2010662 (messages968.html). (Scam warning in the context of wallet troubleshooting.)
[^tg-2026-01-30-2038600]: Telegram export (ReddCoinOfficial), Kpcrypt0, 30 Jan 2026 03:35 UTC-05, message2038600 (messages992.html). (Exchange risk warning; recommend withdrawing to private wallets.)
