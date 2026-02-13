# Troubleshooting (ReddCoin Core)

This section is a curated, **version-aware** set of runbooks for the ReddCoin Core desktop wallet.

> **Safety first:** before you try any recovery action, make a copy of `wallet.dat` (and any `wallets/` directory) to an offline backup location.

**Last reviewed:** 2026-02-12

## Start here

1. **Confirm your Core version** (and whether you're on v3.x or v4.x). See: [Version compatibility & upgrades](version-compatibility.md)
2. If you have **no peers / “no block source”**: see [No peers / no block source](no-peers.md)
3. If you see **“blockchain data file is corrupted”**: see [Corrupted blockchain / resync](corrupted-blockchain.md)
4. If you sent RDD and it is **unconfirmed / stuck**: see [Stuck transactions](stuck-transactions.md)
5. If you suspect you are on the **wrong fork / wrong chain**: see [Wrong fork / wrong chain](wrong-fork.md)
6. If you need startup flags like **reindex / rescan**: see [Reindex & rescan](reindex-rescan.md)
7. If you want to **speed up sync**: see [Bootstrap](bootstrap.md)

## Source provenance

Most procedures here are distilled from:

- Project-controlled docs (ReddPaper / ReddBook / redd.love)
- Official downloads and repos (reddcoin.com, download.reddcoin.com, GitHub)
- Curated admin guidance from the public Telegram channel export (ReddCoinOfficial)

See: [Telegram export notes](../../sources/telegram-export.md)
