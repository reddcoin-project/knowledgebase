# Corrupted blockchain / resync

Symptom examples:

- “**blockchain data file is corrupted**”
- “incorrect blockchain”
- Core starts, then errors out while loading blocks

## Why this happens

Admins repeatedly pointed to three practical causes:

- The wallet/computer was shut down while Core was writing chain data (power outage, forced shutdown).[^message2023494][^message2019637]
- Storage issues (bad sectors / failing disk).[^message2019636][^message2023494]
- Mixing old v3 data with v4 (v4 chain state is not compatible with the previous version).[^message2035575]

## Safe-default recovery (v4)

This is the most commonly shared recovery sequence:

1. **Backup** `wallet.dat` (and `wallets/` if present).
2. **Close** Core.
3. In the data directory, delete:
   - `blocks/`
   - `chainstate/`
   - `indexes/`
   - `peers.dat`
4. Reopen Core and let it **sync fully**.

This full procedure (including OS data directory defaults) was posted as a single runbook by admins.[^message2035575]

## Disk health reminder

If corruption repeats, consider running a disk health test (vendor utilities), and keep **offline backups** of `wallet.dat` on external media.[^message2023494]

---

## Footnotes

[^message2035575]: Telegram export (ReddCoinOfficial), 2025-11-24, obito, message2035575. Permalink: https://t.me/ReddcoinOfficial/2035575.
[^message2023494]: Telegram export (ReddCoinOfficial), 2025-05-12, obito, message2023494. Permalink: https://t.me/ReddcoinOfficial/2023494.
[^message2019636]: Telegram export (ReddCoinOfficial), 2025-03-26, obito, message2019636. Permalink: https://t.me/ReddcoinOfficial/2019636.
[^message2019637]: Telegram export (ReddCoinOfficial), 2025-03-26, obito, message2019637. Permalink: https://t.me/ReddcoinOfficial/2019637.
