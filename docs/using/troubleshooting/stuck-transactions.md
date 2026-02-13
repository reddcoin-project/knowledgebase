# Stuck / unconfirmed transactions

If you sent RDD and it remains **unconfirmed**, or you see a “stuck” outgoing transaction that blocks further sends, the community historically used `zapwallettxes`.

## Before you do anything

- Verify whether the tx exists on an explorer:
  - If it **does not appear**, it may not have actually left the wallet. John Nash noted this and recommended the zap process as the quickest resolution.[^message1989698]
- **Backup** `wallet.dat` first.[^message1940622]

## Admin-recommended procedure

obito repeatedly pointed users to the wiki guide and then recommended setting a small custom fee to improve confirmation reliability.[^message1941782]

Windows convenience tip: create a desktop shortcut to `reddcoin-qt.exe` and append the flag:

- `-zapwallettxes=1` (suggested as the “best way in Windows”).[^message1954386]

If the wallet behaves strangely after the zap pass, admins also suggested a `-reindex` pass as a follow-up.[^message1962358]

## Fee setting (GUI)

After clearing the stuck tx, obito recommended a small custom fee configuration in the Send screen, resulting in ~0.1 RDD fee.[^message1941782]

> Note: fee behavior can be version-dependent. Treat this as operational guidance, not a protocol guarantee.

---

## Footnotes

[^message1989698]: Telegram export (ReddCoinOfficial), 2024-04-02, John (cryptognasher) Nash, message1989698. Permalink: https://t.me/ReddcoinOfficial/1989698.
[^message1940622]: Telegram export (ReddCoinOfficial), 2023-09-21, Kpcrypt0, message1940622. Permalink: https://t.me/ReddcoinOfficial/1940622.
[^message1941782]: Telegram export (ReddCoinOfficial), 2023-09-26, obito, message1941782. Permalink: https://t.me/ReddcoinOfficial/1941782.
[^message1954386]: Telegram export (ReddCoinOfficial), 2023-11-13, Kpcrypt0, message1954386. Permalink: https://t.me/ReddcoinOfficial/1954386.
[^message1962358]: Telegram export (ReddCoinOfficial), 2023-12-12, Kpcrypt0, message1962358. Permalink: https://t.me/ReddcoinOfficial/1962358.
