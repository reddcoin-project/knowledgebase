# Fix: staking is enabled but you never win

--8<-- "_includes/safety-banner.md"

**Applies to:** PoSV v2 staking on v4.22.x

## The key idea

Your chance of receiving a stake depends on:

- **coin age** (how long your coins have been eligible),
- **network conditions / difficulty** (how many coins are staking),
- **your effective stake weight** (how many coins are actually competing).

Admins often explain this as a “lottery ticket” model: small balances may take a very long time to win. [^tg-2024-02-26-1983214]

## Quick checks

1. Confirm staking is actually enabled: see [Staking doesn’t start](staking-doesnt-start.md)
2. Leave Core running long enough — many users underestimate how long small balances take. [^tg-2025-05-06-2023026]

## Practical expectations

- Very small balances can look “stuck” for weeks/months (or longer).
- Consolidating many tiny UTXOs into fewer can help practical stake behavior (but do this carefully; fees apply and you may reset coin age).

## Footnotes

[^tg-2024-02-26-1983214]: Telegram export (ReddCoinOfficial), obito, 26 Feb 2024 10:34 UTC-05, message1983214 (messages946.html). (Coin-age/difficulty explanation; lottery analogy; small balances may take very long.)
[^tg-2025-05-06-2023026]: Telegram export (ReddCoinOfficial), obito, 6 May 2025 12:45 UTC-05, message2023026 (messages979.html). (Example: 120,000 RDD is “small” and may take a while; includes unlock + anvil steps.)
