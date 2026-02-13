# Reindex & rescan (startup flags)

These are advanced startup options used when Core is synced incorrectly, indexes are inconsistent, or transactions/staking appear wrong.

> Always backup `wallet.dat` before running any startup flags.

## `-reindex-chainstate=1` (targeted reindex)

John Nash recommended trying a chainstate reindex based on a database/index error, after first backing up `wallet.dat`.[^message1997316]

Example:

```bash
reddcoin-qt -reindex-chainstate=1
```

## `-reindex`

If you are troubleshooting stuck behavior and already know how to pass flags, admins suggested a `-reindex` pass as a follow-up to other recovery steps.[^message1962358]

## `-rescan`

A rescan can be appropriate after restoring an older wallet file, but it is slower and does not fix a corrupted blockchain database by itself. If you have “blockchain data file is corrupted,” prefer the [Corrupted blockchain / resync](corrupted-blockchain.md) procedure.

---

## Footnotes

[^message1997316]: Telegram export (ReddCoinOfficial), 2024-07-05, John (cryptognasher) Nash, message1997316. Permalink: https://t.me/ReddcoinOfficial/1997316.
[^message1962358]: Telegram export (ReddCoinOfficial), 2023-12-12, Kpcrypt0, message1962358. Permalink: https://t.me/ReddcoinOfficial/1962358.
