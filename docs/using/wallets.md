# Wallets

## ReddCoin Core (desktop)

ReddCoin Core is the full node wallet used to store, send, receive, and (optionally) stake RDD.

### Good practices

- Always **backup `wallet.dat`** before upgrades or troubleshooting.
- Keep your wallet up to date with current releases.
- Prefer downloading binaries from official project sources.

## Versions & compatibility notes

Major wallet changes can require re-syncing chain data. Read release notes and upgrade instructions.

### Common upgrade pitfall: v3 → v4 chain data incompatibility

Community support reports indicate that upgrading “in place” from Core v3 to Core v4 can trigger errors such as **“corrupted block database detected”** or **“Error opening block database”** because the on-disk blockchain data formats are not compatible between major versions.

A conservative, low-risk approach is a **clean install**:

1. **Back up** `wallet.dat` to removable media.
2. Close the wallet.
3. Uninstall the old wallet.
4. Remove the old data directory (keep only your backed up `wallet.dat`).
5. Install the new wallet.
6. Restore `wallet.dat` to the correct folder and resync.

For a worked example and additional fork/sync notes, see:

- https://www.reddit.com/r/reddCoin/comments/1gznin7/corrupted_block_database_detected/
- https://www.reddit.com/r/reddCoin/comments/1idjzz1/how_to_pass_on_right_fork_chain_with_old_wallet/

> Caution: community threads may include extra links. Prefer official domains and the official GitHub releases.

## References

- GitHub releases: https://github.com/reddcoin-project/reddcoin/releases
- Explorer (chain status): https://blockbook.reddcoin.com/
- Legacy wiki (backup guidance): https://wiki.reddcoin.com/Backing_up_your_wallet


## Troubleshooting

If you run into sync, peer, or corruption issues, see the [Troubleshooting runbooks](troubleshooting/index.md).


## Wallet file locations (`wallet.dat`) by version

### Core v3.x (legacy)

By default, Core v3 stored `wallet.dat` in the **root** of the ReddCoin data directory (e.g., `~/.reddcoin`). 

### Core v4.x (current)

Core v4 uses a dedicated **`wallets/`** folder inside the data directory. If you install v4 fresh and simply drop `wallet.dat` into the root folder, you may not see your balance. Admin guidance was:

1. Open Core once, then close it, to create the `wallets/` folder.
2. Copy your backed-up `wallet.dat` into `wallets/`.
3. Reopen Core and allow it to sync.

This procedure was shared explicitly during v3→v4 migration support.[^message2034327][^message2036056]

### Important: always backup first

Use **File → Backup Wallet** and also keep a copy on removable storage.[^message2034327]

#### Footnotes

[^message2034327]: Telegram export (ReddCoinOfficial), 2025-10-22, obito, message2034327. Permalink: https://t.me/ReddcoinOfficial/2034327.
[^message2036056]: Telegram export (ReddCoinOfficial), 2025-12-04, obito, message2036056. Permalink: https://t.me/ReddcoinOfficial/2036056.


## Third-party and mobile wallets (community notes)

Telegram admins have noted that **mobile wallets may lag** behind the latest network/software changes. In Jan 2026, an admin stated that only the web wallet and desktop wallet were at a newer internal release level while mobile wallets were not yet updated.[^message2038344][^message2038345]

Admins also mentioned some non-custodial third-party wallet options (at that time), and described the Telegram bot wallet as custodial.[^message2036635]

> This is **not an endorsement**. Always verify current support, verify the correct chain, and never share seeds/keys with anyone.

#### Footnotes

[^message2038344]: Telegram export (ReddCoinOfficial), 2026-01-26, obito, message2038344. Permalink: https://t.me/ReddcoinOfficial/2038344.
[^message2038345]: Telegram export (ReddCoinOfficial), 2026-01-26, obito, message2038345. Permalink: https://t.me/ReddcoinOfficial/2038345.
[^message2036635]: Telegram export (ReddCoinOfficial), 2025-12-13, obito, message2036635. Permalink: https://t.me/ReddcoinOfficial/2036635.

