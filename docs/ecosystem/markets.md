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

## Official exchange advisories (project posts)

These are project-authored posts that may impact exchange availability:

- **Xeggex shutdown / bankruptcy notice (June 26, 2025):** https://wordpress.reddcoin.com/index.php/2025/06/26/xeggex-shutting-down/
- **Project Update – October 2025** includes notes on repeated exchange outages (TradeOgre, Xeggex, SLEX) and why self-custody matters: https://wordpress.reddcoin.com/index.php/2025/10/01/project-update-october-2025/

### Footnotes

[^message2038600]: Telegram export (ReddCoinOfficial), 2026-01-30, Kpcrypt0, message2038600. Note: We are coming with another ⚠️ warning ⚠️! It appears StakeCube has an extremely low volume on all markets together(less than $1000 on 24h). If you have funds there, and … Permalink: https://t.me/ReddcoinOfficial/2038600.
[^message2034105]: Telegram export (ReddCoinOfficial), 2025-10-18, obito, message2034105. Note: StakeCube announcement Due to an apparent security issue discovered, we've locked down portions of the platform to prevent possible issues. All withdraws are paused for … Permalink: https://t.me/ReddcoinOfficial/2034105.

