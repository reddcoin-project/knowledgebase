# Legacy wiki notes (archival)

These pages are preserved for historical/archival purposes.

## reddcoin.conf notes

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

## zapwallettxes (stuck transactions)

# Remove stuck transactions (zapwallettxes)

**Source:** `wiki.reddcoin.com/Remove_stuck_transactions_with_zapwallettxes` permalink `oldid=4783`.

The `zapwallet` option removes wallet transactions that are **not** on the blockchain (for example: conflicted, stuck unconfirmed).

> Use with care: it removes certain wallet-recorded transactions and then rebuilds the wallet’s transaction view from the chain.

## Linux

```bash
cd /path/to/reddcoin-qt
./reddcoin-qt --zapwallettxes=1
```

## macOS

```bash
/Applications/Reddcoin-Qt.app/Contents/MacOS/Reddcoin-Qt --zapwallettxes=1
```

## Windows

```text
"C:\Program Files\Reddcoin\reddcoin-qt.exe" -zapwallettxes=1
```

After startup, check the **Transactions** tab.
