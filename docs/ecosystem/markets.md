# Markets & exchanges

This page is designed to be **operationally safe**:

- It does **not** try to predict price or recommend trading.
- It focuses on whether venues are real, reachable, and whether deposits/withdrawals function.
- Every venue entry should include a **Last checked** date.

## Verification rubric (minimum)

Before sending funds to an exchange or custodian, verify **at least**:

1. **Domain authenticity**: correct domain, HTTPS, no look‑alike spelling.
2. **RDD wallet status**: deposits enabled? withdrawals enabled? or “maintenance/disabled”.
3. **Chain correctness**: the venue is on the same chain height as public explorers (e.g., Blockbook).
4. **Confirmations & fees**: required confirmations, withdraw fees, and minimums.
5. **Small test first**: do a small deposit and a small withdrawal before moving larger amounts.

### Status levels we track

Use these simple levels in the table below:

- **Market only**: trading pair exists, but deposits/withdrawals unknown.
- **Deposits OK**: deposit addresses work and credits post.
- **Withdrawals OK**: withdrawals complete and land on-chain.
- **Fully functional**: deposits + withdrawals verified recently.

## Official pointers (Linktree)

The project’s Linktree is the best “single list” of external pointers that the team is intentionally surfacing.

> Editors: please update **Last checked** when you personally verify a venue.

| Venue | Market link | Deposits | Withdrawals | Notes | Last checked |
|---|---|---|---|---|---|
| NonKYC | https://nonkyc.io/market/RDD_BTC | Unknown | Unknown | Link surfaced via official Linktree | — |
| StakeCube | https://stakecube.net/app/exchange/RDD_SCC | Unknown | Unknown | Link surfaced via official Linktree | — |
| FreiExchange | https://freiexchange.com/market/RDD/LTC | Unknown | Unknown | Link surfaced via official Linktree | — |
| EnnoDigital | https://ennodigital.com/exchange/RDD_BTC | Unknown | Unknown | Link surfaced via official Linktree | — |

## Market data aggregators

Aggregators can be useful for discovery, but they can also lag reality. Always validate deposits/withdrawals directly.

- CoinGecko listing: https://www.coingecko.com/en/coins/reddcoin

## Legacy directory (broader, community-maintained)

For a longer historical list (including venues that may no longer be active), see:

- [Exchanges (legacy)](../legacy_wiki/exchanges.md)

> Important: Always independently verify withdrawals, network status, and listing reality before sending funds.


## Operational alerts from Telegram (curated)

These are **time-bound** operational notes from public channel admins. They are not endorsements or accusations—just reminders to *verify before you trust*.

- Admins advised caution about **StakeCube** and recommended withdrawing RDD as soon as possible due to withdrawal concerns.[^message2038600]
- Admins discussed repeated exchange disruptions and emphasized diversification and small test transactions first.[^message2034105]

> Always treat exchange availability as temporary and re-check **today** before sending funds.

### Footnotes

[^message2038600]: Telegram export (ReddCoinOfficial), 2026-01-29, Kpcrypt0, message2038600. Permalink: https://t.me/ReddcoinOfficial/2038600.
[^message2034105]: Telegram export (ReddCoinOfficial), 2025-10-18, obito, message2034105. Permalink: https://t.me/ReddcoinOfficial/2034105.

