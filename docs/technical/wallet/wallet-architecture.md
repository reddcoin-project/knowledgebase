
# Wallet Architecture Explained

Understanding how the wallet works helps prevent data loss and user mistakes.

## Key concepts

### wallet.dat
This file contains:
- private keys
- transaction metadata
- address records

If you lose this file and have no backup, funds are lost permanently.

## Why backups matter

- Wallet files can corrupt
- Disk failures happen
- User mistakes happen

Best practice:
- Keep multiple encrypted backups
- Store offline copies
- Update backups after major activity

## Fork detection

Wallets detect forks by comparing:
- block headers
- network consensus rules
- peer data

If a fork occurs:
- update wallet
- resync chain
- verify block height

## Version compatibility

Older wallets may:
- fail to sync
- reject newer transactions
- misreport balances

Always run the latest stable version.

