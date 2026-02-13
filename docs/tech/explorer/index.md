---
title: Explorer & APIs
---

## Blockbook (Trezor / SatoshiLabs)

ReddCoin provides a **Blockbook-based explorer** that exposes:

- Chain status (sync, last block)
- Mempool info
- Basic address / transaction / block queries

**Explorer:** https://blockbook.reddcoin.com/

More detail (including common API patterns):

- [Blockbook explorer & API](../../reference/external/blockbook.md)

!!! note
    Blockbook is intended for indexing and explorer functionality. For critical validation, use your own node (or compare multiple sources).

## Common “checkpoints” ReddHeads ask for

- **Is my wallet on the right chain?** See: [Canonical chain verification](../../reference/canonical-chain-verification.md)
- **Is the network moving?** Compare latest block height across:
  - Blockbook explorer
  - Your local node (`getblockcount`)
- **Exchange deposit stuck?** Start with: [Exchange deposits/withdrawals](../../using/troubleshooting/recipes/exchange-deposits-withdrawals.md)

