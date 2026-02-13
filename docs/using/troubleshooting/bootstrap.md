# Bootstrap (speed up initial sync)

A bootstrap is a prepackaged snapshot of blockchain data that can reduce initial download time.

John Nash posted the v4 bootstrap location here:[^message2001059]

- `https://download.reddcoin.com/bin/bootstrap/v4/`

## Safe use pattern

1. **Close** Core.
2. **Backup** `wallet.dat`.
3. Follow the bootstrap README/instructions provided with the snapshot (do not mix v3 and v4 data).
4. Start Core and allow it to complete syncing.

If you experience errors after bootstrapping, revert to the safe-default [Corrupted blockchain / resync](corrupted-blockchain.md).

---

## Footnotes

[^message2001059]: Telegram export (ReddCoinOfficial), 2024-08-22, John (cryptognasher) Nash, message2001059. Permalink: https://t.me/ReddcoinOfficial/2001059.
