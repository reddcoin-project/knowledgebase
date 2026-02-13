# Recipe: debug.log basics (what to collect safely)

--8<-- "_includes/safety-banner.md"

**Applies to:** Core desktop wallets

## Where to find `debug.log`

It lives in the **data directory**:

- Windows: `%APPDATA%\Reddcoin\debug.log`
- macOS: `~/Library/Application Support/Reddcoin/debug.log`
- Linux: `~/.reddcoin/debug.log`

## What to share (and what not to share)

- Share the **last 100–200 lines** when asking for help.
- **Redact**: usernames, full filesystem paths, IP addresses, any identifying info.
- Do **not** share: seed phrases, private keys, or wallet files.

Admins may ask for logs when diagnosing corruption or startup issues. [^tg-2024-01-16-1974346]

## Footnotes

[^tg-2024-01-16-1974346]: Telegram export (ReddCoinOfficial), obito, 16 Jan 2024 09:42 UTC-05, message1974346 (messages937.html). (Admins/devs may request logs to diagnose corrupt files; keep support public.)
