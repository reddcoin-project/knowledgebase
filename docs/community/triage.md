# How we curate community sources

This knowledgebase aims to be a **single point of reference**. That only works if we are strict about what we treat as canonical, and careful about spam, scams, and polluted content.

## Source tiers

### Tier 1 — Canonical (authoritative)

Use these to define reality when there is conflict:

- Official published documents (ReddPaper, ReddBook, PoSV v2 paper, PoSV v2 FAQ)
- Official project sites and release posts (e.g., reddcoin.com, redd.love, download.reddcoin.com)
- Official source code and tagged releases (GitHub repos under the project org)

### Tier 2 — Operational (live network truth)

- Explorers and APIs that reflect current chain state (e.g., Blockbook)
- Node-level verification (your own full node, reproducible builds, checksums)

### Tier 3 — Community (context and practical troubleshooting)

- Telegram groups and channels (public communities)
- ReddcoinTalk (reddcointalk.org)
- Reddit (r/reddCoin)

Tier 3 sources are valuable for *patterns* (what users run into, what fixes worked), but they are **not canonical** by default.

## What we accept (and what we reject)

### We accept

- Historical narratives and community retrospectives, clearly labeled as historical
- Troubleshooting steps that are consistent with Tier 1/2 sources
- Links to official downloads, official repos, and official explorers

### We reject (or heavily quarantine)

- “Download this wallet” links that do not point to official domains or GitHub
- Referral links, airdrop “tasks”, pay-to-join groups, or “send X to get Y” schemes
- Random ZIP/RAR attachments, unsigned binaries, and “DM me for the file” posts
- Doxxing, personal data, or screenshots containing private keys / seed phrases
- Market manipulation content (pump groups, coordinated shilling) and price predictions

## Sanitization rules

When incorporating community content into documentation:

1. **Summarize; do not mirror.** Paraphrase and link the source instead of copying long text.
2. **Strip risky details.** Remove wallet addresses, QR codes, transaction IDs, screenshots of balances, private chats, and any personally identifying information.
3. **Prefer official endpoints.** If a post includes links, replace them with official equivalents when possible.
4. **Mark confidence.** Use one of:
   - *Confirmed* (supported by Tier 1/2)
   - *Plausible* (multiple community reports, but not fully confirmed)
   - *Historical* (true at the time, may not match current software)
   - *Unverified* (kept only as a pointer, not recommended)
5. **Add “Last reviewed”.** Community-derived items should include a date (and ideally a reviewer handle).

## How to add a community item

Use this minimal template:

- **Claim / Topic:** what the item is about
- **Summary:** 1–3 sentences (what it teaches)
- **Source:** link(s)
- **Tier:** 3 (community)
- **Status:** Confirmed / Plausible / Historical / Unverified
- **Last reviewed:** YYYY-MM-DD

