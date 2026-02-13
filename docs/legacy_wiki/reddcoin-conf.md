# reddcoin.conf (legacy notes)

This is a **legacy reference** derived from the historic wiki page.

Use it as a starting point only — always confirm settings against the current Reddcoin Core version and release notes.

**Source:** `wiki.reddcoin.com/Reddcoin.conf` (historic content; legacy addnodes/port details may be outdated).

## Common patterns

- Network / connectivity
  - `addnode=<ip-or-host>`
  - `maxconnections=<n>`

- RPC (only if you know you need it)
  - `rpcuser=<user>`
  - `rpcpassword=<strong password>`
  - `rpcallowip=<ip>`

> Security: Do not expose RPC to the public internet.

