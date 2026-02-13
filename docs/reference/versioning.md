# Versioning & compatibility (why old advice breaks)

ReddCoin has multiple “eras” of software and consensus rules. A lot of advice on the internet assumes a specific era.

## The rule of thumb

If someone gives you instructions, first determine:

1. **Wallet line** (example: Core **3.10.6** vs **4.22.9**)
2. **Consensus era** (example: PoSV vs **PoSV v2**)
3. Whether their advice refers to **rebuilding the blockchain**, **recovering keys**, or **staking settings**

Then only apply instructions that match your era.

## Key eras (high-level)

| Era | Consensus / protocol | Typical desktop wallet line | Notes |
|---|---|---|---|
| Legacy PoSV | Original PoSV | older 2.x | Historical; most guidance is archival. |
| PoSV v2 activation | PoSV v2 | 3.x | PoSV v2 fork was announced to activate around block **3,000,000**. |
| Modern Core (0.22-based) | PoSV v2 + modern wallet features | 4.22.x | HD wallet + Wizard flows (BIP32/39/44) and newer address support. |

**Sources / canonical references**

- PoSV v2 fork announcement (block target and rationale): https://www.reddcoin.com/faith-hope-charity-official-announcement-reddcoin-rdd-upcoming-consensus-fork-posv-v2-protocol-enhancement/
- v3.0 PoSV v2 release notes: https://www.reddcoin.com/official-release-v3-0-posv2/
- v4.22 line background (Taproot / modernization): https://medium.com/projectredd/reddcoin-rdd-core-wallet-4-22-taproot-efficiency-security-privacy-1d7fde2d8b7
- v4.22.9 release (official): https://wordpress.reddcoin.com/index.php/news/

## Common failure mode: mixing v3 chain data with v4

If you install a modern 4.22 wallet but reuse an old chain-state / blocks folder from a v3 install, you can hit errors like **“corrupted block database”** or end up on the **wrong chain**. The fix is usually:

1. Backup wallet data
2. Install the correct modern release
3. Rebuild chain data (optionally with bootstrap)
