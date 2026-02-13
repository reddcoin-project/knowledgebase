# Troubleshooting decision tree

--8<-- "_includes/safety-banner.md"

If you prefer a guided flow (instead of scanning a table), follow this decision tree.

> **Before you change anything:** make an offline backup of your wallet files (`wallet.dat` and/or the `wallets/` folder). If you’re unsure where those are, see **[Wallet files & locations](../../reference/wallet-files.md)**.

```mermaid
flowchart TD
  A[Pick the closest symptom] --> B{Does the wallet start?}

  B -->|No / crashes| C[Startup crash / corrupted database]
  C --> C1[Likely fix: clean resync]

  B -->|Yes| D{Do you have peers?}
  D -->|0 connections| E[No peers / can't connect]
  E --> E1[Likely fix: reset peers + check conf]

  D -->|Yes| F{Is sync progressing?}
  F -->|Stuck / hours behind| G[Sync stalled / stuck at a height]
  G --> G1[Likely fix: clean resync or bootstrap]

  F -->|Looks synced but balance/tx looks wrong| H[Suspect wrong chain / fork]
  H --> H1[Likely fix: verify known hashes; resync or invalidate]

  F -->|Synced| I{Is the problem a transaction?}
  I -->|Unconfirmed / stuck| J[Stuck transaction]
  J --> J1[Likely fix: zapwallettxes + resend]

  I -->|Exchange deposit/withdrawal missing| K[Exchange issue]
  K --> K1[Likely fix: verify tx, explorer, and venue status]

  I -->|Not about a transaction| L{Is the problem staking?}
  L -->|No anvil / not staking| M[Staking won't start]
  M --> M1[Likely fix: unlock-for-staking + enable staking]

  L -->|Staking enabled but no rewards yet| N[Staking expectations]
  N --> N1[Likely: coin age / weight / patience]

  A --> O{Are you upgrading?}
  O -->|v3 → v4 upgrade| P[Upgrade path]
  P --> P1[Likely fix: clean upgrade + resync]

  A --> Q{Are you restoring a backup?}
  Q -->|Moved computers / restoring wallet| R[Restore wallet files]
  R --> R1[Likely fix: copy wallets into data directory]
```

## Go to the matching runbook

- **Startup crash / corrupted database** → [Clean resync (v4)](recipes/clean-resync-v4.md)
- **No peers / 0 connections** → [No peers / connections](recipes/no-peers.md)
- **Sync stalled / stuck** → [Clean resync (v4)](recipes/clean-resync-v4.md) and/or [Bootstrap (v4)](bootstrap.md)
- **Wrong chain / fork** → [Wrong fork / chain split](recipes/wrong-fork-chain-split.md)
- **Stuck transaction** → [Stuck transaction (zapwallettxes)](recipes/stuck-transaction-zapwallettxes.md)
- **Exchange deposits/withdrawals** → [Exchange deposits/withdrawals](recipes/exchange-deposits-withdrawals.md)
- **Staking won’t start** → [Staking doesn’t start](recipes/staking-doesnt-start.md)
- **Staking is slow / no wins yet** → [Staking expectations](recipes/staking-expectations.md)
- **v3 → v4 upgrade** → [v3 → v4 upgrade](recipes/v3-to-v4-upgrade.md)
- **Restoring from backup / moving computers** → [Restore wallet files](recipes/restore-wallet-files.md)

If you’re still unsure which branch applies, use: [Quick triage (1–2 clicks)](quick-triage.md)
