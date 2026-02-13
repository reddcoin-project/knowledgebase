# Blockbook explorer & API (blockbook.reddcoin.com)

ReddCoin operates a Trezor/SatoshiLabs **Blockbook** instance that serves as:

- a public block explorer UI
- an indexed API backend for address/tx/block lookups

Explorer: https://blockbook.reddcoin.com/

## Why Blockbook matters

Blockbook is an *indexer* sitting in front of a full node. It maintains an address index and exposes fast queries without requiring each user to run a full chain index locally.

## Endpoints you can rely on today

The ReddCoin Blockbook instance is known to expose a money-supply endpoint used by external data providers:

- Money supply: `https://blockbook.reddcoin.com/api/moneysupply/`

(See also: CoinGecko’s supply references, which link to this endpoint.)

## Common Blockbook API v2 patterns (upstream)

Most Blockbook instances expose a standardized `/api/v2/...` REST surface. Typical calls include:

- `GET /api/v2/address/<address>` – balances + transactions
- `GET /api/v2/tx/<txid>` – transaction detail
- `GET /api/v2/block/<hash-or-height>` – block detail

> Practical note: confirm endpoints against the live instance before depending on them in production, as operators sometimes restrict or proxy routes.

## Operational notes

- For mission-critical applications, run your own full node and/or your own Blockbook instance.
- Blockbook is a convenience layer; consensus truth is still the chain.

## Related

- [Explorer & APIs](../../tech/explorer.md)
