# Known-good fixes by version (index)

--8<-- "_includes/safety-banner.md"

This page collates fixes that are **explicitly version-sensitive**.

!!! note "Last reviewed: 2026-02-13"
    The latest published v4 desktop build folder in the official download index is **4.22.9**. Planned / in-testing work toward **4.22.10** is tracked in official project updates (see **News → Releases**).

## v4.22.9 (and newer v4.22.x)

If you’re on v4.22.9 but still on the wrong chain, admins consistently point to a **clean resync** (delete `blocks/`, `chainstate/`, `indexes/`, `peers.dat`). [^tg-2025-12-22-2036920]

- [Clean resync (v4)](recipes/clean-resync-v4.md)

## v4.22.8 (staking quirk)

A v4.22.8 staking toggle quirk was reported: unlock, enable staking, then toggle off/on if it doesn’t start. [^tg-2025-02-25-2017279]

- [Staking doesn’t start](recipes/staking-doesnt-start.md)

## v3.x (legacy)

- Stuck tx fix is often `zapwallettxes`: [Stuck transaction](recipes/stuck-transaction-zapwallettxes.md)
- Upgrade path to v4: [v3 → v4 upgrade](recipes/v3-to-v4-upgrade.md)

## Footnotes

[^tg-2025-12-22-2036920]: Telegram export (ReddCoinOfficial), obito, 22 Dec 2025 03:04 UTC-05, message2036920 (messages991.html). (v4.22.9 resync guidance.)
[^tg-2025-02-25-2017279]: Telegram export (ReddCoinOfficial), obito, 25 Feb 2025 09:56 UTC-05, message2017279 (messages973.html). (v4.22.8 staking toggle quirk.)
