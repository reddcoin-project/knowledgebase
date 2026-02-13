# Fix: no peers / 0 connections

--8<-- "_includes/safety-banner.md"

**Applies to:** v3.x and v4.22.x (desktop)

## Symptoms

- “0 connections”
- “No peers”
- Sync never starts
- You upgraded from v3 → v4 and now v4 won’t connect

## Quick checks

1. Make sure your system clock is correct.
2. Check firewall / antivirus isn’t blocking the wallet.
3. Confirm you’re running a **current** Core version (v4.22.x).

## Fix (most common): reset `peers.dat`

`peers.dat` is a local cache of previously connected peers. If you installed v4 over v3, `peers.dat` may still contain **v3 peers**, which can prevent v4 from connecting correctly. [^tg-2024-09-18-2002895]

### Steps

1. **Close Core**
2. Open your data directory:
   - Windows: `%APPDATA%\Reddcoin\`
   - macOS: `~/Library/Application Support/Reddcoin/`
   - Linux: `~/.reddcoin/`
3. **Rename or delete** `peers.dat`
4. Start Core — it will create a fresh `peers.dat`

!!! success "Admin-verified"
    Resetting `peers.dat` is a standard fix when a v4 wallet is picking up old v3 peers. [^tg-2025-02-19-2016799] [^tg-2024-09-18-2002895]

## If you’re on v3 and upgrading soon

If you’re still on v3, upgrade guidance often includes removing `peers.dat` when switching to v4 to avoid peer-mixing. [^tg-2024-11-28-2008135]

## Footnotes

[^tg-2024-09-18-2002895]: Telegram export (ReddCoinOfficial), obito, 18 Sep 2024 06:34 UTC-05, message2002895 (messages962.html). (v4 should only connect to v4 peers; rename/move peers.dat.)
[^tg-2025-02-19-2016799]: Telegram export (ReddCoinOfficial), John (cryptognasher) Nash, 19 Feb 2025 04:31 UTC-05, message2016799 (messages973.html). (“delete peers.dat … might be picking up old v3 peers”.)
[^tg-2024-11-28-2008135]: Telegram export (ReddCoinOfficial), obito, 28 Nov 2024 07:25 UTC-05, message2008135 (messages966.html). (v3 upgrade guidance: remove peers.dat so wallet recreates it.)
