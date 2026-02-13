# Community archive index

This section is the “bridge” between **fast-moving community discussion** (Telegram/Reddit/forums) and **durable documentation**.

We do **not** mirror entire chat logs or threads. Instead we:

1. Identify recurring high-signal topics.
2. Extract a short, sanitized summary.
3. Link to the original source.
4. Cross-check against canonical sources where rules/behavior are involved.

## High-signal topic clusters

Use these clusters to decide what to ingest next:

### Wallets & upgrades

- Major version upgrades (e.g., Core v3 → v4)
- Bootstrapping and sync performance
- Chain fork recovery and “wrong chain” detection
- Restoring `wallet.dat` and key import

### Staking operations

- Staking configuration and uptime
- Expected yield behavior (clearly label historical vs PoSV v2)
- Common misconceptions (weight, maturity, reward timing)

### Network incidents

- Reported forks, stalls, or explorer inconsistencies
- Known “bad fork” heights and recovery commands (only when confirmed)

### Ecosystem / exchanges

- Listings, delistings, maintenance windows
- Deposits/withdrawals health (must include a Last checked date)

## Safe ingestion workflow

1. **Triage** the post/thread using [How we curate community sources](triage.md).
2. **Summarize** in 1–5 sentences. Do not copy-paste long content.
3. **Remove risky content** (addresses, keys, screenshots, personal info, DMs).
4. **Replace links** with official equivalents when available.
5. Mark with:
   - Status: Confirmed / Plausible / Historical / Unverified
   - Last reviewed: YYYY-MM-DD

## Tooling notes (optional)

If the team wants to turn community review into a repeatable process:

- **Telegram:** use Telegram Desktop “Export chat history” (HTML/JSON) for time-bounded review.
- **ReddcoinTalk (Discourse):** many topics have JSON endpoints by appending `.json` to a topic URL (useful for building an index).
- **Reddit:** use search queries and curated link lists; if you automate, prefer official APIs and store only post metadata + your own summaries.

## Pointers

- Telegram (official group): https://t.me/ReddcoinOfficial
- Reddit: https://www.reddit.com/r/reddCoin/
- ReddcoinTalk forum: https://reddcointalk.org/
