# Quick triage (1–2 clicks)

--8<-- "_includes/safety-banner.md"

Use this page to **jump straight to a fix**.

Prefer a guided flow? See: **[Troubleshooting decision tree](decision-tree.md)**.

> **Before you change anything:** make an offline backup of your wallet files (`wallet.dat` and/or the `wallets/` folder). If you need the file paths, see: **[Wallet files & locations](../../reference/wallet-files.md)**.

## Pick your symptom

| What you see | Best next step |
|---|---|
| Wallet won’t sync / hours behind / stuck at a block height | [Clean resync (v4)](recipes/clean-resync-v4.md) |
| “No peers”, “0 connections”, or can’t find the network | [Fix: no peers / connections](recipes/no-peers.md) |
| “Corrupted” database / wallet crashes on startup | [Fix: corrupted blockchain data](recipes/clean-resync-v4.md#when-a-clean-resync-is-the-right-move) |
| Sent RDD but it’s unconfirmed / “stuck” | [Fix: stuck transaction (zapwallettxes)](recipes/stuck-transaction-zapwallettxes.md) |
| Balance looks wrong / wallet shows “wrong chain” | [Fix: wrong fork / chain split](recipes/wrong-fork-chain-split.md) |
| Upgrading from a very old wallet (v3.x) to current (v4.x) | [Fix: v3 → v4 upgrade](recipes/v3-to-v4-upgrade.md) |
| Restoring from backup / moving to a new computer | [Fix: restore wallet files](recipes/restore-wallet-files.md) |
| Staking isn’t starting / no anvil / “not staking” | [Fix: staking doesn’t start](recipes/staking-doesnt-start.md) |
| Staking is enabled but you never win a block | [Fix: staking expectations & coin age](recipes/staking-expectations.md) |
| Exchange deposit/withdrawal missing | [Fix: exchange issues](recipes/exchange-deposits-withdrawals.md) |
| You’re not sure if you’re on v3 or v4 | [Version compatibility & upgrades](version-compatibility.md) |

## If you still can’t tell what’s wrong

1. Check the **block height** in your wallet and compare it to a public explorer.
2. Check your wallet’s **Core version** and whether it’s **v3** or **v4**.
3. If asked to share logs, start with the **last 100 lines** of `debug.log` and redact personal info (paths/IPs).

Next: [Troubleshooting overview](index.md)
