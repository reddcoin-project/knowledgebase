# No peers / “no block source”

This runbook is for cases where Core shows **0 connections**, **no block source**, or it never starts downloading headers/blocks.

## Common cause: stale `peers.dat` (especially v4 installed over v3)

Admins repeatedly recommended:

- **Close Core**
- Delete (or rename) `peers.dat` (and optionally `anchors.dat`)
- Reopen Core, allowing it to discover fresh peers again

TechAdept summarized this as a safe first-step when the wallet can’t find valid peers.[^message1908849][^message1908882]

For v4 specifically, obito noted that installing v4 over v3 can leave a v3-created `peers.dat` in place, causing v4 to connect to the wrong peer set. Deleting/renaming `peers.dat` forces v4 to rebuild it with v4 peers.[^message2002895][^message2012462]

## Step-by-step

1. **Close** ReddCoin Core.
2. Go to the data directory (see [Version compatibility](version-compatibility.md)).
3. **Backup** `wallet.dat` (do not skip).
4. Delete (or rename) **`peers.dat`**.
5. Optional: delete **`anchors.dat`** (if present).
6. Restart Core and wait a few minutes.


### If it still doesn’t connect

- Check firewall/security software (Windows Defender, third-party AV).
- Review `debug.log` for connection errors.
  - TechAdept specifically suggested `debug.log` as the next diagnostic artifact.[^message1908882]

### Fast-track tip (when peer count is low)

John Nash noted that peer discovery may “eventually” increase naturally, but you can fast-track by deleting `peers.dat` and restarting.[^message2016709]

---

## Footnotes

[^message1908849]: Telegram export (ReddCoinOfficial), 2023-05-24, Tech Adept (RDD) reddcoin.com / redd.love, message1908849. Permalink: https://t.me/ReddcoinOfficial/1908849.
[^message1908882]: Telegram export (ReddCoinOfficial), 2023-05-24, Tech Adept (RDD) reddcoin.com / redd.love, message1908882. Permalink: https://t.me/ReddcoinOfficial/1908882.
[^message2002895]: Telegram export (ReddCoinOfficial), 2024-09-18, obito, message2002895. Permalink: https://t.me/ReddcoinOfficial/2002895.
[^message2012462]: Telegram export (ReddCoinOfficial), 2025-01-09, obito, message2012462. Permalink: https://t.me/ReddcoinOfficial/2012462.
[^message2016709]: Telegram export (ReddCoinOfficial), 2025-02-18, John (cryptognasher) Nash, message2016709. Permalink: https://t.me/ReddcoinOfficial/2016709.
