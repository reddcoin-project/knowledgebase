# Reddcoin Core issues (legacy)

**Source:** `wiki.reddcoin.com/Reddcoin_Core_Issues` permalink `oldid=6906`.

This page captures a couple of **specific UI issues** observed in Reddcoin Core 3.10.x around the PoSV v2 activation period.

## Staking icon shows incorrect staking status (Core 3.10.0 / 3.10.1)

The legacy report notes that the staking check-mark icon could show **green** even when an encrypted wallet was not unlocked for staking.

Practical takeaway:

- If your wallet is encrypted, explicitly **unlock for staking** (Settings → Unlock Wallet… → check “For staking only”).

## Display issue: received staking amount shown incorrectly (Core 3.10.1)

The legacy report notes that Core could display the full staking reward amount even though a portion is routed to the dev fund under PoSV v2.

Workaround in the legacy report:

- Wait for confirmations, or **restart** Core to refresh the displayed values.

