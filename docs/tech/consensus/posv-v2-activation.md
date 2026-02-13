# PoSV v2 activation & enforcement

PoSV v2 was rolled out as a **consensus change** (hard fork).

## Activation rule (supermajority window)

The network enforces PoSV v2 once a supermajority of recent blocks signal the new version:

- Window size: 10,000 blocks (≈ 7 days)
- Threshold: 90% of the window (9,000 / 10,000) must be v5 blocks

Once activated, older block versions are rejected.

## What changes at activation

### PoSV v2 staking reward logic

- PoSV v2 targets an overall network inflation rate of ~5% by applying an inflation adjustment factor to staking rewards.
- The scaling factor depends on the previous month’s staking reward output, and is bounded within upper and lower limits.

### Developer funding address

- A portion of each staking reward (8%) is routed to the developer funding address.

## Operator checklist

- Upgrade all nodes and staking wallets prior to activation.
- Exchanges and custodial services should validate: block version signaling, stake validation, and reward transaction parsing.
- Watch the explorer / blockbook for: block version distribution, last seen v4/v5 blocks, and fork warnings.

