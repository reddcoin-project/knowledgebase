# Troubleshooting (ReddCoin Core)

--8<-- "_includes/safety-banner.md"

This section is a curated, **version-aware** set of runbooks for the ReddCoin Core desktop wallet.

**Last reviewed:** 2026-02-12

## Start here

- **Fastest path:** [Quick triage (1–2 clicks)](quick-triage.md)
- **Version sanity check:** [Version compatibility & upgrades](version-compatibility.md)
- **Scam avoidance:** [Support safety](support-safety.md)
- **Version-specific index:** [Known-good fixes by version](known-good-fixes.md)

## Common fixes

| Symptom | Fix |
|---|---|
| Won’t sync / stuck / corrupted | [Clean resync (v4)](recipes/clean-resync-v4.md) |
| No peers / 0 connections | [No peers](recipes/no-peers.md) |
| Transaction stuck / unconfirmed | [zapwallettxes](recipes/stuck-transaction-zapwallettxes.md) |
| Wrong chain / fork | [Wrong fork / chain split](recipes/wrong-fork-chain-split.md) |
| Upgrading v3 → v4 | [v3 → v4 upgrade](recipes/v3-to-v4-upgrade.md) |
| Restoring wallet files | [Restore wallet files](recipes/restore-wallet-files.md) |
| Staking not starting | [Enable staking + unlock](recipes/staking-doesnt-start.md) |

## Source provenance

Most procedures here are distilled from:

- Project-controlled docs (ReddPaper / ReddBook / redd.love)
- Official downloads and repos (reddcoin.com, download.reddcoin.com, GitHub)
- Curated admin guidance from the public Telegram channel export (ReddCoinOfficial)

See: [Telegram export notes](../../sources/telegram-export.md)
