---
title: Upgrade to Core v4.22+
---

This guide helps you upgrade to **ReddCoin Core v4.22+** (the modern Core line that includes SegWit-era address support and related improvements).

!!! info "Last verified: 2026-02-13"
    If you hit anything unexpected, please report it (we’re 100% volunteers). Also check **Start Here → Live Project Status** for the latest release notes and known issues.

## Why this upgrade matters (the “why”, not just the “how”)

ReddCoin’s mission is social-first value transfer — but we still need **modern, secure, maintainable Core software** so that nodes, wallets, and exchanges can operate reliably for years.

The Core v4.22 line is discussed publicly by the project as a major modernization effort (address types, faster sync, new wallet capabilities, and broader protocol-era compatibility).  
References:
- Core v4.22 open beta announcement (features + safety warnings): https://www.reddcoin.com/reddcoin-4-22-0-entering-open-beta-testing/  
- Project AMA mentioning SegWit support and ongoing 4.22.x work: https://www.reddcoin.com/reddcoin-rdd-development-teams-march-23-2024-live-ama-an-in-depth-look/  
- Background context on SegWit-era capabilities in 4.22: https://medium.com/projectredd/reddcoin-rdd-core-wallet-4-22-taproot-efficiency-security-privacy-1d7fde2d8b7  

## Before you upgrade (safety first)

### 1) Back up your wallet and keys
- Back up `wallet.dat` (Core wallet file) **before** you install anything.
- If your wallet is encrypted, make sure you have your passphrase recorded securely.

### 2) Verify the chain you’re on
Before and after upgrading, confirm you’re on the canonical chain:
- **Reference → Canonical chain verification**

### 3) Plan for time + disk
A full sync can take time and disk. Don’t do the upgrade 5 minutes before you need to send funds.

## Download & verify (recommended)
1. Go to **For Users → Downloads** (official host).
2. Download the installer/archive that matches your OS.
3. **Verify SHA256** using the published `SHA256SUMS` on the download host.
   - This step is intentionally emphasized for safety and crypto-ethics: don’t trust binaries blindly.

## Install & first run (standard path)

1. Install the new version as normal for your OS.
2. Start the wallet once and let it create its data directory.
3. Close the wallet.

### Keep your existing wallet file
If your existing installation already has a data directory, the new version will typically reuse it.

If you need to manually restore:
- Place your backed-up `wallet.dat` into the ReddCoin data directory (replace only after making copies).
- Start the wallet and let it fully sync.

## Post-upgrade checklist (the 5 things that catch most issues)

1. **Let it fully synchronize** before judging balances.
2. Confirm your wallet is on the canonical chain (again).
3. Confirm your **receive address** type matches what you expect (legacy vs newer formats).
4. If staking: confirm the wallet is unlocked for staking (if encrypted) and has mature coins.
5. Send a **small test transaction** before moving large amounts.

## Troubleshooting (common fixes)

### “My balance is wrong / missing / not showing”
Most often: the wallet isn’t fully synced yet.

If it *is* synced:
- Try a **rescan** (wallet reads the chain again for your transactions)
- If the chainstate looks corrupted, try a **reindex**

Typical flags (run with the GUI app or daemon):
- `-rescan`
- `-reindex`

### “My wallet crashes on startup”
1. Make sure you have a safe backup of `wallet.dat`.
2. Try `-salvagewallet` (attempts key recovery).
3. If problems persist, ask for help in the community channels (and include logs).

(General recovery patterns are also summarized in the legacy wiki material under **Legacy Wiki → Wallet recovery**.)

### “Not staking because coins are immature”
Coins typically must mature for a period before they can stake. This is normal — wait and re-check.

### “Exchange deposit/withdrawal stuck”
Start here:
- Check the transaction on a block explorer (**Technology → Explorer & APIs**).
- Verify confirmations and whether the exchange requires memo/extra data (most don’t, but exchanges vary).
- If needed, contact the exchange with the TXID.

## Node operators: minimal config hygiene

- Keep a backup of `reddcoin.conf`.
- If you run a full node, ensure your inbound port is open (historically **45444**, if unchanged in your deployment).

## If you get stuck
We want “volunteer-run” to still feel **high-trust and responsive**.

- Check: **Start Here → Live Project Status** (known issues / releases)
- Ask in the community channels (Telegram/Discord listed in **Community → Links**)
- When reporting: include OS, wallet version, what step you’re on, and relevant log lines (never share private keys).
