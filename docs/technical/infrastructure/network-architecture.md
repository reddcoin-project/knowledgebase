
# Network Architecture (Deep Dive)

ReddCoin is a first‑generation UTXO blockchain optimized for **social payments and staking participation**, not high‑frequency financial settlement.

## Core properties

- Proof‑of‑Stake‑Velocity (PoSV v2)
- UTXO model (Bitcoin‑derived architecture)
- Long chain history and high distribution
- Emphasis on wallet participation rather than mining hardware

## Node types

### Full nodes
- Validate all blocks
- Relay transactions
- Maintain full blockchain history
- Provide network stability

### Staking nodes
- Full nodes with unlocked wallet
- Participate in PoSV consensus
- Improve decentralization

### Lightweight wallets
- Use remote nodes / simplified validation
- Suitable for mobile and casual users
- Should not be used for long‑term large holdings

## Why this architecture matters

PoSV incentivizes **holding + using** coins rather than speculative idle storage.  
This is consistent with ReddCoin’s design as a *social currency*, not just a store of value.

