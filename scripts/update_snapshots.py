#!/usr/bin/env python3

"""
Update auto-generated snapshot sections for:
- docs/reference/current_state.md
- docs/ecosystem/markets_snapshot.md

Designed to run in GitHub Actions (scheduled) and commit changes back to the repo.
"""

from __future__ import annotations

import datetime as _dt
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import requests


ROOT = Path(__file__).resolve().parents[1]
CURRENT_STATE = ROOT / "docs" / "reference" / "current_state.md"
MARKETS_SNAPSHOT = ROOT / "docs" / "ecosystem" / "markets_snapshot.md"

COINGECKO_TICKERS = "https://api.coingecko.com/api/v3/coins/reddcoin/tickers"
DOWNLOAD_INDEX = "https://download.reddcoin.com/bin/"
BLOCKBOOK_HOME = "https://blockbook.reddcoin.com/"


def _replace_autogen_block(path: Path, new_block: str) -> None:
    text = path.read_text(encoding="utf-8")
    pattern = r"<!-- AUTOGEN:BEGIN -->.*?<!-- AUTOGEN:END -->"
    replacement = f"<!-- AUTOGEN:BEGIN -->\n{new_block}\n<!-- AUTOGEN:END -->"
    new_text, n = re.subn(pattern, replacement, text, flags=re.S)
    if n != 1:
        raise RuntimeError(f"Expected exactly one AUTOGEN block in {path}, found {n}.")
    path.write_text(new_text, encoding="utf-8")


def _semver_key(v: str) -> Tuple[int, int, int, str]:
    # v like "4.22.9" or "3.10.6"
    m = re.match(r"(\d+)\.(\d+)\.(\d+)(.*)$", v)
    if not m:
        return (0, 0, 0, v)
    a, b, c, rest = m.groups()
    return (int(a), int(b), int(c), rest or "")


def _fetch_text(url: str, timeout: int = 30) -> str:
    r = requests.get(url, timeout=timeout, headers={"User-Agent": "reddcoin-kb-snapshot/1.0"})
    r.raise_for_status()
    return r.text


def _fetch_json(url: str, timeout: int = 30) -> Dict[str, Any]:
    r = requests.get(url, timeout=timeout, headers={"User-Agent": "reddcoin-kb-snapshot/1.0"})
    r.raise_for_status()
    return r.json()


def get_latest_core_version_from_download_index(html: str) -> Optional[str]:
    # Prefer "reddcoin-core-X.Y.Z/" directories, fall back to "X.Y.Z/".
    versions = set()

    for m in re.finditer(r"reddcoin-core-(\d+\.\d+\.\d+)/", html):
        versions.add(m.group(1))
    for m in re.finditer(r">\s*(\d+\.\d+\.\d+)/\s*<", html):
        versions.add(m.group(1))

    if not versions:
        return None
    return sorted(versions, key=_semver_key)[-1]


def parse_blockbook_status_from_home(html: str) -> Dict[str, str]:
    # Parse a few key fields from the Blockbook "Status" page.
    out: Dict[str, str] = {}

    # Backend subversion
    m = re.search(r"Subversion/Reddoshi:(\d+\.\d+\.\d+)/", html)
    if m:
        out["core_subversion"] = m.group(0)

    m = re.search(r"Protocol Version\s*</[^>]+>\s*([0-9]+)", html, flags=re.I)
    if m:
        out["protocol"] = m.group(1)

    m = re.search(r"Last Block\s*</[^>]+>\s*([0-9\s]+)", html, flags=re.I)
    if m:
        out["height"] = re.sub(r"\s+", "", m.group(1))

    m = re.search(r"Money Supply\s*</[^>]+>\s*([0-9\.]+)", html, flags=re.I)
    if m:
        out["money_supply"] = m.group(1)

    # Blockbook version/build
    m = re.search(r"Version / Commit / Build\s*</[^>]+>\s*([^<]+)<", html, flags=re.I)
    if m:
        out["blockbook_version"] = m.group(1).strip()

    return out


def build_current_state_block() -> str:
    now = _dt.datetime.utcnow().replace(microsecond=0)

    # Download index -> latest version
    dl_html = _fetch_text(DOWNLOAD_INDEX)
    latest = get_latest_core_version_from_download_index(dl_html) or "unknown"

    # Blockbook home parse
    bb_html = _fetch_text(BLOCKBOOK_HOME)
    bb = parse_blockbook_status_from_home(bb_html)

    lines: List[str] = []
    lines.append(f"_Last updated: **{now.isoformat()}Z**_")
    lines.append("")
    lines.append("## Recommended Core wallet")
    lines.append(f"- Latest in download index: **{latest}**")
    lines.append(f"- Download index: {DOWNLOAD_INDEX}")
    lines.append("")
    lines.append("## Explorer / indexer (Blockbook)")
    if "height" in bb:
        lines.append(f"- Reference height: **{bb['height']}**")
    if "protocol" in bb:
        lines.append(f"- Protocol version: **{bb['protocol']}**")
    if "core_subversion" in bb:
        lines.append(f"- Backend: `{bb['core_subversion']}`")
    if "money_supply" in bb:
        lines.append(f"- Money supply (from Blockbook): **{bb['money_supply']} RDD**")
    lines.append(f"- Status page: {BLOCKBOOK_HOME}")
    lines.append("")
    lines.append("## Sanity-check hints")
    lines.append("- If your node height lags significantly, see: `Using RDD → Troubleshooting` (no peers / wrong fork / corrupted blockchain).")
    lines.append("- If you are upgrading from 3.10.x → 4.22.x, rebuild chain data (do not reuse old v3 blocks/chainstate).")

    return "\n".join(lines)


def build_markets_snapshot_block(max_rows: int = 25) -> str:
    now = _dt.datetime.utcnow().replace(microsecond=0)

    data = _fetch_json(COINGECKO_TICKERS + "?page=1&order=volume_desc")
    tickers = data.get("tickers", []) or []

    # Sort by converted_volume.usd desc if present
    def vol_usd(t: Dict[str, Any]) -> float:
        cv = t.get("converted_volume") or {}
        try:
            return float(cv.get("usd") or 0.0)
        except Exception:
            return 0.0

    tickers = sorted(tickers, key=vol_usd, reverse=True)[:max_rows]

    lines: List[str] = []
    lines.append(f"_Last updated: **{now.isoformat()}Z**_")
    lines.append("")
    lines.append("## Top reported tickers (CoinGecko)")
    lines.append("")
    lines.append("| Exchange | Pair | Last | Volume (USD) | Trust score |")
    lines.append("|---|---:|---:|---:|---:|")

    for t in tickers:
        m = t.get("market") or {}
        ex = m.get("name") or "Unknown"
        base = t.get("base") or ""
        target = t.get("target") or ""
        pair = f"{base}/{target}" if base and target else ""
        last = t.get("last")
        try:
            last_s = f"{float(last):.8g}" if last is not None else ""
        except Exception:
            last_s = ""
        v = vol_usd(t)
        trust = t.get("trust_score") or ""
        lines.append(f"| {ex} | {pair} | {last_s} | {v:,.0f} | {trust} |")

    lines.append("")
    lines.append("Notes:")
    lines.append("- CoinGecko data can include stale/incorrect tickers. Always verify deposits/withdrawals directly with the venue.")
    lines.append(f"- API: {COINGECKO_TICKERS}")

    return "\n".join(lines)


def main() -> None:
    # Current state
    cs_block = build_current_state_block()
    _replace_autogen_block(CURRENT_STATE, cs_block)

    # Markets snapshot
    mk_block = build_markets_snapshot_block()
    _replace_autogen_block(MARKETS_SNAPSHOT, mk_block)

    print("Updated snapshots.")


if __name__ == "__main__":
    main()
