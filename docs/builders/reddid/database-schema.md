# Database schema

This page turns the wiki “Database Schema” into a practical reference for builders.

## Overview

The ReddID system uses a dedicated schema to store:

- Namespaces (rules + ownership + expiry)
- User IDs (ownership + expiry + activity)
- Auctions and bids
- ReddID profiles and reputation
- Mappings from a ReddID to namespace-specific user IDs

## Core tables (curated)

### `namespaces`

Stores namespace configuration and ownership.

Key fields include:

- `id` (namespace identifier, PK)
- `owner` (binary address)
- configuration flags: `allow_numbers`, `allow_hyphens`, `allow_underscores`
- length constraints: `min_length`, `max_length`
- renewal economics: `renewal_period`, `grace_period`
- revenue split: `namespace_revenue_pct`, `burn_pct`, `node_pct`, `dev_pct`
- auction bounds: `min_auction_duration`, `max_auction_duration`, `min_bid_increment`
- integrity + lifecycle: `config_hash`, `last_updated`, `expiration`

### `namespace_pricing_tiers`

Pricing tiers by name length (within a namespace):

- `namespace_id` (PK, FK)
- `min_length` (PK)
- `min_price`

### `user_ids`

Registered user IDs within namespaces (composite identity):

- `name` (PK part)
- `namespace_id` (PK part)
- `owner`
- `registration_time`, `expiration_time`
- activity: `last_transaction`, `transaction_count`
- `metadata_hash`

### `auctions`

Generic auctions used by the system:

- `auction_id` (PK)
- `name`, `namespace_id`
- `creator_address`
- `start_time`, `end_time`
- `reserve_price`
- `current_bid`, `current_bidder`
- `deposit_amount`
- `state`, `type`
- `block_height`, `txid`
- `metadata_hash`

### `bids`

Bids placed on auctions:

- `bid_id` (PK)
- `auction_id` (FK)
- `bidder_address`
- `bid_amount`, `deposit_amount`
- `bid_time`, `txid`
- `is_winner`, `refunded`

### `reddid_namespace_resolution`

Maps a top-level ReddID to per-namespace user IDs:

- `reddid` (PK part)
- `namespace_id` (PK part)
- `user_id`
- `is_primary`, `auto_update`
- `last_synced`

## Indexing notes

Indexes are intended to support:

- Foreign key joins
- Finding active auctions by state
- Renewal management by expiration timestamps
- Ranking by reputation score
- Fast namespace-specific user lookups via composite indexes

## Canonical source

- Database Schema: https://github.com/reddcoin-project/reddcoin/wiki/Database-Schema

_Last reviewed: 2026-02-13_
