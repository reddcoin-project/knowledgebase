# Knowledgebase changelog

## v0.37
- Added Node Operator Guide (running-a-node.md)
- Added Wallet Architecture explanation page
- Added Staking Mechanics guide for practical user expectations
- Expanded technical section into full operator/dev support structure


## v0.36
- Major expansion of technical/infrastructure documentation:
  - Added Network Architecture deep dive
  - Added PoSV v2 technical explanation page
- Exchanges: began structured “Former major venues” ledger expansion
- Added Technical Documentation Hub page for long‑term maintainability


## v0.35
- Exchanges: added Verified delistings/removals ledger (primary sources only).
- Exchanges: added curated r/reddcoin exchange/listings index for community evidence.
- Exchanges: added official/public announcement index (X/Twitter + Medium) for historical claims.
- Current markets: added CoinGecko “quick snapshot” pointer (Nonkyc.io mention; verify before use).
- Release hygiene: preserved single deploy workflow (deploy-pages.yml).


## v0.34.1
- Fix: corrected broken self-custody link on Ecosystem → Exchanges overview.
- Fix: enabled Markdown tables extension to prevent footnote backref anchor warnings in strict builds.


## v0.34
- Expanded Exchanges section: added “Where to buy RDD (today)” and “Exchange history timeline” pages.
- Strengthened historical archive with primary-source references (Bitcoin.com offer via Q1 2021 dev update; Xeggex listing mention via 2023 year-in-review).
- Upgraded Ecosystem navigation to provide a fully structured Exchanges submenu.
- Release hygiene: preserved single deploy workflow (deploy-pages.yml).


## v0.33
- Corrected historical exchange reference: Bitcoin.com replaces Crypto.com.
- Added structured archive table for historical exchanges.
- Added Exchange Safety Checklist page.
- Workflow hygiene: ensured only deploy-pages.yml included.


## v0.32
- Added Exchanges section (Current, Historical, Risk, Announcements) with aggregator + official source links.
- Added conservative “Former / historical listings” archive starter (BitMart listing source, Bittrex pair-removal discussion link).
- Release hygiene: ensured only deploy-pages workflow is included (no extra pages.yml/pages.yaml).



## v0.31
- Ecosystem Partners: rebuilt layout into card-grid, removed stray citation markup that broke rendering, and expanded integrations list from public announcements.
- Build hygiene: removed accidental extra workflow file (.github/workflows/pages.yml); keep deploy-pages.yml only.


## v0.30
## v0.30.3

## v0.30.3
- CI fix: restored mkdocs-material emoji configuration using callable functions (twemoji/to_svg) to stop pymdownx.emoji TypeError.
- Added PyYAML pin for consistent config parsing.

## v0.30.2
- CI fix: pin GitHub Actions build to Python 3.12 to avoid pymdownx.emoji incompatibility on 3.14.
- Added Actions troubleshooting notes.

- Build hardening: added requirements.txt, BUILDING.md, and GitHub Pages deploy workflow (deploy-pages).
- Uses mkdocs build --strict in CI to catch broken links early.

## v0.29.1
- Fix release: repaired mkdocs.yml navigation indentation that prevented nested ReddID pages from rendering properly.
- Restored complete changelog coverage for missing releases (v0.21, v0.24, v0.25).


## v0.29
- Added Decentralization & Governance page.
- Added ReddCoin Canon primary documents index.
- Added Technical Deep Dives diagrams.
- Enhanced State of the Network verification checklist.


## v0.28
- Added Roadmap Philosophy page.
- Added ReddHead Contributors recognition page.
- Added Historical Archive Index.
- Enhanced State of the Network dashboard section.
- Added SEO/site metadata enhancements.


## v0.27
- Added State of the Network page.
- Added architecture diagrams.
- Added Why ReddCoin Still Matters page.
- Expanded troubleshooting high-signal issues.
- Added Security & Responsibility doctrine.


## v0.26
- Added visual QA checklist and launch-readiness checks.
- Added CoinPaprika as a market data source alongside CoinGecko and CoinMarketCap.
- Added Reddit archive/research page and datamining workflow for long-term community memory.


## v0.25
- Fixed homepage “buttons/icons render as text” by enabling required Markdown extensions (attr_list, md_in_html, etc.).
- Converted key bare URLs into proper Markdown links where appropriate.


## v0.24
- Implemented dual‑path UX (Users vs Developers/Nodes) entry hubs.
- Added Staking 101 interactive teaching widget and accessibility styling.
- Converted bare URLs to clickable https:// links across the site (safe, outside code blocks).


## v0.23
- Added **Social tipping (ReddBot)** hub with platform sub-guides (Twitter/X, Twitch, Telegram, Reddit, Discord).
- Expanded **Upgrade to Core v4.22+** into a builder/operator-ready guide (download verification, post-upgrade checklist, troubleshooting).
- Fixed/locked **banner + header contrast** and ensured the site’s custom stylesheet loads via `extra_css` (prevents white-on-white visibility issues).
- Updated UI/UX decision log with explicit contrast + trust-marker guidance.


## v0.22
- Adopted dual-path information architecture: **For Users** vs **For Developers & Nodes**.
- Refactored homepage to foreground **Faith, Hope, and Charity** mission and volunteer ethos.
- Added **Live Project Status** transparency page linking to GitHub work streams.
- Added **ReddID Name Cost Calculator** hub page with embedded official calculator and builder-ready logic notes.
- Added **Staking 101** interactive teaching guide (PoSV/PoSV v2) with deep-dive toggles.
- Added new user guides: social tipping (ReddBot), self-custody (The Redd Way), and Core v4.22+ upgrade.
- Removed duplicate legacy ReddID docs under Ecosystem; Ecosystem now links to the canonical Builders hub.
- Accessibility & usability polish: improved focus outlines, link discoverability, and long-form readability.

This changelog tracks releases of the **ReddCoin Knowledgebase** (this website), not the ReddCoin protocol.


## v0.21
- Site-wide internal link cleanup and restored Explorer & APIs page interconnects.
- Hardened external PDF links to canonical sources to avoid missing-asset breakage.


## v0.20
- Added a true **Start Here portal** with card-based quick actions and guided links.
- Added **Knowledgebase Home** (wiki-style index) for fast scanning and discovery.
- Added a recorded **UI/UX & IA review** page so design decisions stay consistent.
- Enabled richer UI elements (icons/cards) via Material emoji support.
- Tuned site search tokenization (separator) for better findability.
- Applied “quiet authority” design polish: restrained color surfaces, improved contrast, and tighter readability defaults.


## v0.19
- Fixed header/banner contrast issues (prevents white-on-white or low-contrast headings).
- Upgraded homepage to a **trust-first, task-first** layout for ReddHeads (Download / Stake / Troubleshoot / Build).
- Added typography and layout improvements for long technical pages.


## v0.18
- Reduced repository file count (<100) to support GitHub web UI uploads.
- Consolidated small pages (FAQ → Quickstart; Explorer → Infrastructure; Legacy PoSV notes → PoSV v2).
- Centralized External references and Legacy wiki notes into single pages.
- Replaced bundled PDFs with canonical links on redd.love.
- Trimmed unused logo variants while keeping official branding.


## v0.17
Major:
- Added a **homepage Quick actions** block (Download / Stake / Troubleshoot / Build).
- Added **Quickstart (choose your path)** router for intent-based navigation.
- Split IA: created **Builders** (technical) separate from **Ecosystem** (user-facing).
- Added “Last verified” callouts and standardized safety admonitions.
- Reduced saturation and improved long-form readability (measure/spacing).


## v0.16
- Added additional **ReddID builder-ready** pages (Namespaces, Database schema, Implementation plan).
- Added **Downloads** hub with SHA verification guidance.
- Improved nav and release hygiene.


## v0.15
- Integrated official logo/art pack locally and wired it into theme branding.
- Added Products, Partners, and expanded ReddID coverage with curated wiki sources.


## v0.14
- Implemented brand palette + initial reference pages.
- Added canonical chain verification reference and exchanges/markets matrix.


## v0.13
- Initial packaged MkDocs baseline for the knowledgebase.
