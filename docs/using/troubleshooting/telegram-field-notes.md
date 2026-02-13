# Telegram field notes (curated troubleshooting)

These are **curated** notes extracted from the public Telegram group export (2019–Feb 2026), focusing on recurring technical issues and admin/dev guidance.

!!! warning "Version matters"
    Many fixes only apply to specific wallet lines (3.10.x vs 4.22.x). If in doubt, start with:
    - [Version matrix](../version-matrix.md)
    - [Versioning & compatibility](../../reference/versioning.md)

---

## 1) v3 vs v4 chain data is not interchangeable

> You either upgraded from version 3 (v3 blockchain is not compatible with v4) or your wallet is on one of the two bad blockchains that appeared after the forks.
Resync it from scratch.
Close the wallet.
Open Reddcoin folder. The default paths:
Linux: ~/.reddcoin
macOS: ~/Library/Application Support/Reddcoin
Windows: %APPDATA%/Reddcoin (Use Windows key + R to open the run window, type this into the run window)
Delete the "blocks", "chainstate" and "indexes" folders and "peers.dat" file.
Open the wallet and let it sync with the network.
If you're not on the correct chain you will lose all the stake rewards that you received while you were on the incorrect blockchain (you will see the transactions greyed-out and the stakes substracted from your balance) and because you'll have an older coin age, you'll receive higher stakes.
PS. Do not reply to anyone who writes to you privately because they are scammers.

_Source: obito, 2025-06-18._

Actionable takeaway:
- If you upgrade from **3.10.x → 4.22.x**, **do not reuse** old v3 blockchain data folders. Rebuild the chain data (optionally bootstrap).

## 2) “Corrupted block database” — typical rebuild steps

> Probably the database is corrupted. Instead of wasting time to troubleshoot the wallet, you can choose the approach that you know that works for sure.
1. Backup your wallet.dat file. You can also backup the private key if you want.
https://wiki.reddcoin.com/Backing_up_your_wallet
https://yavuz.uber.space/books/reddcoin-core-on-windows/page/backing-up-wallet
2. Uninstall Reddcoin Core Wallet and delete the existing blockchain data. The default locations of Reddcoin folder where the blockchain is stored is
Windows: C:\Users\your_user_name\AppData\Roaming
AppData is a hidden folder so you must write it by hand in the address bar of the folder
Linux: ~/.reddcoin
macOS: ~/Library/Application Support/Reddcoin
3. Install the latest version on Reddcoin Core Wallet from https://reddcoin.com/reddcoin.html
4. Disable the internet connection
5. Restore your wallet.dat file in C:\Users\your_user_name\AppData\Roaming\Reddcoin
https://wiki.reddcoin.com/Restore_your_wallet
6. Enable internet connection
7. Let the wallet sync

_Source: obito, 2023-04-05._

See also:
- [Corrupted blockchain](corrupted-blockchain.md)
- [Reindex / rescan](reindex-rescan.md)
- [Bootstrap](bootstrap.md)

## 3) No peers / won’t connect — reset peers list

> Close the wallet.
Open the Reddcoin folder.
Delete the "blocks", "chainstate" and "indexes" folders and "peers.dat" file.
The default path of the Reddcoin folder is:
~/.reddcoin
Open the wallet and let it sync with the network.

_Source: obito, 2025-12-04._

See also: [No peers](no-peers.md)

## 4) Staking not starting — unlock + enable staking

> The staking does not start by default.
To stake you must have the wallet fully synchronized with the network.
Then there are two steps:
1) Unlock the wallet "for staking only" with the password from the Settings on the top menu.
2) Click on the bottom right anvil icon - Enable Staking

_Source: obito, 2026-01-29._

See also: [Staking](../staking.md)

## 5) HD seed phrase ≠ imported single private keys

> You probably have autodelete messages, so I don't see anything in dm. That's probably the reason you haven't heard anything

_Source: Kpcrypt0, 2025-12-05._

Practical warning:
- If you import a single private key, it may **not** be recoverable from the HD seed phrase backup.

## 6) If you have a 12-word phrase with a missing word

> @flow0x1 On the bottom of the Ian Coleman's Recovery Tool page you can find Offline Usage to download the tool to use it offline on a computer. You must disconnect the computer from the internet for security reasons when extracting the private keys.

_Source: obito, 2024-11-05._

**Safety note:** use offline tools on an airgapped computer when handling seeds.

---

## What we intentionally excluded

- Non-admin “random advice”
- Any PII, addresses, or transaction IDs posted by users
- Any DMs or “support offers”
