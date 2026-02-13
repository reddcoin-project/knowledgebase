# Fix: wrong fork / chain split (v4)

--8<-- "_includes/safety-banner.md"

**Applies to:** v4.22.x (desktop)

## Symptoms

- Wallet says “synced” but block height differs from explorers
- Deposits/withdrawals don’t match what you expect
- Admins mention you may be on the “wrong chain”

## First: do a clean resync (recommended)

In many cases, doing a **[clean resync](clean-resync-v4.md)** (delete `blocks/`, `chainstate/`, `indexes/`, `peers.dat`) will return you to the correct chain. [^tg-2025-12-22-2036920]

## If you need to *verify* (advanced)

The community documented two historical bad splits and a deterministic way to check which chain you’re on using `getblockhash` at specific heights, then `invalidateblock` on the wrong hash. [^tg-2024-09-28-2003569]

!!! warning "High-impact action"
    `invalidateblock` changes your node’s view of the chain. This is safe when done correctly, but **copy/paste carefully**. If you’re not comfortable, do the clean resync instead.

### How to run the check

1. Open **ReddCoin Core → Tools → Debug console**
2. Run the check commands below.

### Split #1 (height 5,448,005)

Run:

- `getblockhash 5448005`

If you get the **wrong-chain hash**, invalidate it:

- `invalidateblock 809a59a737c3479ac17ad0fd426193596cc02cfb82cd1c87fa05ef94f8f8587a`

### Split #2 (height 5,519,068)

Run:

- `getblockhash 5519068`

If you get the **wrong-chain hash**, invalidate it:

- `invalidateblock 420d82c48eea24cd9a06b24cc012bb89abdcab95bdbc29ef02d9fd55ef41f570`

## What to expect afterward

- Core will reorganize and continue syncing on the correct chain.
- If you had “stake rewards” on a bad fork, those may disappear after you return to the correct chain (because those blocks aren’t in the canonical chain). This was explicitly called out in admin guidance. [^tg-2024-12-25-2010662]

## Footnotes

[^tg-2025-12-22-2036920]: Telegram export (ReddCoinOfficial), obito, 22 Dec 2025 03:04 UTC-05, message2036920 (messages991.html). (v4 resync guidance.)
[^tg-2024-09-28-2003569]: Telegram export (ReddCoinOfficial), Kpcrypt0, 28 Sep 2024 12:44 UTC-05, message2003569 (messages962.html). (Two historical splits + getblockhash + invalidateblock instructions.)
[^tg-2024-12-25-2010662]: Telegram export (ReddCoinOfficial), obito, 25 Dec 2024 15:24 UTC-05, message2010662 (messages968.html). (Scam warning + note about stake rewards disappearing when returning to correct chain.)
