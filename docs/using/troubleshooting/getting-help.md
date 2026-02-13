# Getting help (what to post, where to ask)

--8<-- "_includes/safety-banner.md"

If you followed the relevant runbook and you’re still stuck, this page helps you get **useful help fast** — without exposing private info.

## Where to ask

Start with a **public** support channel (never DMs):

- **Telegram (public group):** see [Telegram](../../community/telegram.md)
- **Reddit:** see [Reddit](../../community/reddit.md)
- **GitHub (bugs / reproducible issues):** open an issue in the official repo when you can share steps to reproduce.

## What *not* to post

- Do **not** post a seed phrase, private key, or your `wallet.dat` / `wallets/` folder.
- If you need file paths for backups/restore, see: **[Wallet files & locations](../../reference/wallet-files.md)**.
- Do **not** accept “support” in private DMs.
- Avoid posting full logs that contain personal file paths or IPs.

## What to include (non‑technical checklist)

Copy/paste and fill this in:

- **Wallet app:** ReddCoin Core Desktop / ReddWallet / Mobile wallet (which one?)
- **Core version:** (Help → About)
- **Operating system:** Windows / macOS / Linux (+ version if you know it)
- **Block height shown in wallet:**
- **Connections (peers):** (bottom-right network icon)
- **What you were trying to do:** sync / send / receive / stake / restore
- **What happened (exact message):**
- **What you already tried:** (link the runbook you followed)

## If you’re asked for `debug.log`

Send only what’s needed:

1. Close the wallet.
2. Find `debug.log` in your data directory (see **Reference → Wallet files & locations**).
3. Copy the **last 100–200 lines**.
4. Redact:
   - your Windows username / home folder path
   - IP addresses (unless the helper explicitly needs them for peer diagnostics)

> Do **not** redact block hashes and heights when diagnosing a wrong chain — those are the “evidence” needed to verify the fork.

## Template: Telegram / Reddit post

```
Hi ReddCoin team/community — I need help with:

Symptom: (e.g., wallet stuck syncing / 0 connections / staking not starting)
Wallet app: 
Core version: 
OS:
Block height shown:
Peers:
What I tried: (link runbook)
What happened:
Relevant error text:
Last 20 lines of debug.log (redacted):
```

## Template: GitHub issue (best for real bugs)

```
Title: (Short symptom) — (Core version) on (OS)

Environment
- OS:
- Core version:
- Install method: (download from reddcoin.com/download.reddcoin.com)

Steps to reproduce
1.
2.
3.

Expected result

Actual result

Logs
- Paste relevant debug.log lines (redacted paths/IPs)
```

## If the issue involves an exchange

Before you post:

- Verify the transaction on an explorer (see [Explorer & APIs](../../tech/explorer/index.md)).
- Note the **txid**, **time sent**, and the exchange **ticker**.
- Check whether the exchange is on **maintenance** (many venues post this).

Then use: [Exchange deposits/withdrawals](recipes/exchange-deposits-withdrawals.md)
