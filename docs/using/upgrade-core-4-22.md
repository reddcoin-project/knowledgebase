---
title: Upgrade to Core v4.22+
---

This guide is for upgrading to **ReddCoin Core v4.22+** (SegWit/CSV-era modernizations).

## Before you upgrade (safety first)

1. **Back up your wallet**
   - Back up `wallet.dat` and/or your seed/keys (if applicable).
2. Verify you’re on the **canonical chain**:
   - See: Reference → Canonical chain verification
3. Use official downloads:
   - See: For Users → Downloads

## Upgrade steps (standard path)

1. Download the new version from the official site.
2. Verify the SHA256 hash (recommended).
3. Install/replace binaries.
4. Start the wallet and allow it to sync fully.
5. Confirm:
   - Your balance is correct
   - You are on the expected chain tip
   - Staking resumes after the required conditions

<details>
<summary><strong>Deep dive: why SegWit/CSV and modern Core matters</strong></summary>

- Improves compatibility with modern infrastructure and tooling
- Enables better transaction handling and future extensions
- Aligns with safer operational patterns for exchanges and integrators
</details>

## If something looks wrong

- If sync is stuck: Troubleshooting → Quick triage
- If your wallet shows an unexpected chain: Reference → Canonical chain verification
- If transactions look “missing”: check your wallet files and rescan guidance in Troubleshooting recipes
