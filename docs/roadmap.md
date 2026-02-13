# Roadmap / backlog

This is a living backlog for expanding the ReddCoin Knowledgebase.

## Next: “external source ingestion”

1. **Linktree audit**
   - Confirm every Linktree destination is still correct.
   - Convert each link into a stable knowledgebase page (with a short summary and purpose).

2. **Legacy wiki indexing**
   - Inventory top-level wiki sections and create an index.
   - Prioritize wallets, staking, and exchange information.

3. **Community-source curation (Telegram / Reddit / ReddcoinTalk)**
   - Maintain curated “high-signal thread” indexes.
   - Extract repeatable troubleshooting patterns into durable docs.
   - Add “Last reviewed” stamps and sanitize risky content.

4. **Explorer/APIs**
   - Document the ReddCoin Blockbook instance endpoints we actually rely on.
   - Add examples for common developer tasks: supply, address history, tx lookup.

5. **Core releases & upgrade guides**
   - Build a chronological release index (v2.x → v3.x → v4.x).
   - Provide "upgrade playbooks" for users, exchanges, and infrastructure operators.

6. **Exchange health tracking**
   - Add a per-venue checklist and a standard “Last checked” date field.
   - Track deposits/withdrawals separately from “market exists”.

7. **ReddID / Project Redd**
   - Consolidate design docs, tiers, and current implementation status.

## Governance of the knowledgebase

- Every page should cite a primary source (doc, release note, code, or official announcement) when stating protocol rules.
- Community sources are welcome but must be labeled (Confirmed / Plausible / Historical / Unverified) and have a “Last reviewed” date.
- If a topic is uncertain or time-sensitive, label it as such and link to the canonical upstream reference.


## Next: hardening + automation

1. **Version tagging everywhere**
   - Add “Applies to: vX.Y” badges at top of troubleshooting pages.
   - Create a “current supported wallet versions” page that is updated from GitHub releases.

2. **Automated health checks**
   - Pull current chain height from Blockbook and surface it on a “Network status” page.
   - Add a small script to compare wallet heights / API uptime (and log outages as incidents).

3. **Exchange matrix refresh**
   - Rebuild the legacy wiki exchange table as a structured dataset (YAML/CSV) so it can be rendered and diffed.
   - Add “Last verified” dates and remove dead/unknown entries.

4. **Telegram export mining improvements**
   - Build a reproducible pipeline that:
     - re-parses new Telegram exports,
     - flags new high-signal admin messages,
     - suggests PRs for updated runbooks.

5. **Security / scam playbook**
   - Add a dedicated page: common scams, what admins will never ask for, safe verification steps.
