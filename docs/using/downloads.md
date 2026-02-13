# Downloads

!!! info "Last verified: 2026-02-13"

    External links can change over time. If something looks outdated, please report it.

    Hashes (SHA256) are published alongside downloads at the official host. Verify before installing.



!!! warning "Security: verify what you download"

    Only download from the official host and **verify the SHA256 hash** before running installers.
    If you’re unsure, ask in the official community channels and do not install.

This page links to official ReddCoin binaries and shows how to **verify what you downloaded** before installing.

## Official download host

Binaries and related files are hosted at:

- https://download.reddcoin.com/

The `bin/` directory contains versioned release folders (for example, `reddcoin-core-4.22.9/`) and each release folder includes a `SHA256SUMS` file alongside the binaries.  

## Verify SHA256 hashes (recommended)

### Linux

1. Download your binary **and** the `SHA256SUMS` file from the same release folder.
2. Run:

```bash
sha256sum -c SHA256SUMS
```

If your file matches, you’ll see `OK` for it.

### macOS

```bash
shasum -a 256 <filename>
```

Compare the output to the value listed in `SHA256SUMS`.

### Windows (PowerShell)

```powershell
Get-FileHash .\<filename> -Algorithm SHA256
```

Compare the output to the value listed in `SHA256SUMS`.

## Signatures / “signed” binaries

Some releases include “signed” installers (for example, macOS `.dmg` or Windows `.exe` builds labeled signed).  
Even when using signed builds, we still recommend verifying the SHA256 hash from the same release directory.

## Safety notes

- Always download from the official host above or links that clearly point back to it.
- Make a wallet backup before upgrading.

_Last reviewed: 2026-02-13_