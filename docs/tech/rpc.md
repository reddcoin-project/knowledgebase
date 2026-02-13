---
title: RPC quick reference
---

This is a **quick reference** for node operators and integrators. It’s intentionally concise.

> If you’re new: start with **For Users → Quickstart**.

## Basics

- RPC is local by default. Don’t expose it to the public internet.
- Prefer authentication + firewalling even on private networks.
- Back up `wallet.dat` before any upgrade or major changes.

## Common tasks

- Get current block height:
  - `getblockcount`
- Check network info:
  - `getnetworkinfo`
- Check chain tip:
  - `getchaintips`
- Get wallet info:
  - `getwalletinfo`

<details>
<summary><strong>Deep dive: safe RPC exposure patterns</strong></summary>

- Use a reverse proxy only on private LAN
- IP allowlists + strong credentials
- Separate “read-only” endpoints in your app layer when possible
</details>
