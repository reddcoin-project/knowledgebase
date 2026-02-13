# Wrong fork / wrong chain recovery

This page documents a class of incidents where a wallet is **operating on a fork** (or talking to peers on a fork), leading to misleading staking status and/or transactions that never appear on explorers.

## What can go wrong

During 2024 incidents, admins explicitly warned:

- **v3 is on a fork of the blockchain**.[^message2000805]
- Staking rewards may be generated on the wrong chain and won’t be recognized on the correct chain.[^message2000808]
- Any transactions or stakes created on the wrong fork will not be recognized on the correct chain.[^message2001872]

## Safe-default fix (recommended for most users)

1. **Upgrade to the current v4 wallet** (see [Version compatibility](version-compatibility.md)).
2. **Resync** using the delete-and-redownload procedure:
   - delete `blocks/`, `chainstate/`, `indexes/`, and `peers.dat`
3. Optionally use the [v4 bootstrap](bootstrap.md).

John Nash suggested a “delete blocks/chainstate/index + restart” approach to stop recurring invalid-block messages and force correct sync.[^message2000756]

## Advanced tooling (for expert users)


## 2024 “bad fork” checks (block heights + hashes)

During September 2024 incidents, an admin posted deterministic checks using `getblockhash` at two heights, with known-good hashes and corresponding `invalidateblock` actions.[^message2002551]

If you are investigating a suspected chain mismatch, consider reading **[Known incidents](../../history/incidents.md)** for the full table and context.


### Invalidate a bad block and rewind

John Nash shared an approach using Core’s console:

- `invalidateblock <hash>`

…which rewinds blocks to a given height, then you restart and sync forward on the correct chain.[^message1997330]

### Ban known-bad peers (historical)

During the same period, John Nash provided `setban` commands for specific IPs that were reportedly on the wrong chain or old versions.[^message2000407]

> **Important:** this is **time-bound** operational guidance from a specific incident. These IPs may be benign later. Use only if you are actively diagnosing a fork/peer poisoning situation and you understand the implications.

---

## Footnotes

[^message2000805]: Telegram export (ReddCoinOfficial), 2024-08-19, John (cryptognasher) Nash, message2000805. Permalink: https://t.me/ReddcoinOfficial/2000805.
[^message2000808]: Telegram export (ReddCoinOfficial), 2024-08-19, John (cryptognasher) Nash, message2000808. Permalink: https://t.me/ReddcoinOfficial/2000808.
[^message2001872]: Telegram export (ReddCoinOfficial), 2024-09-04, John (cryptognasher) Nash, message2001872. Permalink: https://t.me/ReddcoinOfficial/2001872.
[^message2000756]: Telegram export (ReddCoinOfficial), 2024-08-18, John (cryptognasher) Nash, message2000756. Permalink: https://t.me/ReddcoinOfficial/2000756.
[^message1997330]: Telegram export (ReddCoinOfficial), 2024-07-05, John (cryptognasher) Nash, message1997330. Permalink: https://t.me/ReddcoinOfficial/1997330.
[^message2000407]: Telegram export (ReddCoinOfficial), 2024-08-15, John (cryptognasher) Nash, message2000407. Permalink: https://t.me/ReddcoinOfficial/2000407.
