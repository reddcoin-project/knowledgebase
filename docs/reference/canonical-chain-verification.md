# Canonical chain verification

When troubleshooting **“wrong chain / fork / split”** issues, you need a repeatable way to verify you are on the canonical chain.

## Quick checks

1. **Compare your local block height** to a public explorer.
2. **Compare a block hash at a specific height** (not just height).
3. If you are on the wrong fork: **stop sending transactions**, and recover (usually via clean resync).

## Recommended verification sources

- Blockbook explorer (live chain status): https://blockbook.reddcoin.com/
- Your own full node (authoritative for your local view)

## Safe default recovery path

If you cannot confirm you are on the canonical chain:

1. Backup `wallet.dat` (and/or your seed phrase, if applicable).
2. Perform a **clean resync** (see: Troubleshooting → Recipes → Clean resync (v4)).
3. Re-verify height + hash after resync.

## Advanced recovery

Some historical incidents used **invalidateblock** to force reorg onto the canonical chain. This is an **advanced, incident-specific** operation and should only be used when:
- you have a known-good canonical hash checkpoint, and
- the official team has published/confirmed the exact instructions.

_Last reviewed: 2026-02-13_
