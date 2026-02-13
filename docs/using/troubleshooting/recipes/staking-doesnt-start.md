# Fix: staking doesn’t start (enable staking + unlock)

--8<-- "_includes/safety-banner.md"

**Applies to:** v4.22.x (desktop)

## Symptoms

- Wallet is synced but shows **not staking**
- The anvil icon is present but staking stays disabled
- You upgraded and staking behavior seems “different”

## Two-step enablement (v4)

Admin guidance repeatedly describes staking as a **two-step** process:

1. **Unlock the wallet “for staking only”** (top menu: Settings)
2. Click the **anvil icon** (bottom-right) → **Enable staking** [^tg-2026-01-29-2038537]

## Known quirk: v4.22.8 staking toggle

A v4.22.8-specific quirk was noted: if staking won’t start, toggle it off/on using the anvil icon after unlocking. [^tg-2025-02-25-2017279]

!!! success "Admin-verified"
    - “Unlock for staking only” + “Enable staking (anvil)” is the baseline v4 recipe. [^tg-2026-01-29-2038537]
    - v4.22.8 may need a toggle cycle. [^tg-2025-02-25-2017279]

## Footnotes

[^tg-2026-01-29-2038537]: Telegram export (ReddCoinOfficial), obito, 29 Jan 2026 07:15 UTC-05, message2038537 (messages992.html). (Staking does not start by default; unlock + anvil icon.)
[^tg-2025-02-25-2017279]: Telegram export (ReddCoinOfficial), obito, 25 Feb 2025 09:56 UTC-05, message2017279 (messages973.html). (v4.22.8 staking bug; toggle staking after unlock.)
