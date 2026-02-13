# Staking operations FAQ (PoSV v2)

This page collates **real-world operational guidance** from the public ReddCoin Telegram export (Feb 2019 → Feb 2026), with emphasis on **recent years** and admin-authored support.

It is intended for practical troubleshooting, not as a protocol spec. For the formal design, see **[Technology → PoSV v2 & Enhanced Staking](../tech/consensus/posv-v2.md)**.

!!! warning "Version-specific"
    ReddCoin guidance can be **version-specific**. If you're unsure what you run, start with **[Version matrix](version-matrix.md)** and **[Version compatibility & upgrades](troubleshooting/version-compatibility.md)**.

---

## Starting staking in Core v4 (desktop)

On Core v4.x, staking may require **two explicit actions** after the wallet is fully synced:

1. **Unlock “for staking only”** (you’ll still need the password again to send coins).[^message2021513][^message2038537]  
2. Click the **bottom-right anvil icon → Enable Staking**.[^message2021513][^message2038537]

If you skip step (2), the wallet can appear healthy but won’t actually stake.[^message2021513]

---

## “I’m synced but I’m not staking” (common causes)

### 1) Not actually enabled (anvil icon)

This is the #1 miss; see “Starting staking” above.[^message2038537]

### 2) v4.22.8 staking toggle bug (time-bound)

During v4.22.8, users reported a behavior where staking did not start until they **disabled staking and enabled it again**.[^message1988235]  
obito also flagged this as a version-specific bug and linked to internal dev discussion.[^message1988846]

If you’re still on 4.22.8, upgrading is recommended.

---

## Wallet backups and “wrong chain” gotchas

### Wallet backups

John Nash reassured users that if they have a `wallet.dat` backup from v3, they are covered; v4 should not cause funds loss by itself, but you should confirm you are on the correct chain (e.g., compare block height with Blockbook).[^message2007420]

### Coin age note when moving funds

obito advised that if you intend to move coins from an old wallet to a new wallet and you care about staking cadence, **stake before sending** (otherwise coin age is lost).[^message2038108]

---

## Operational tips (high-signal)

- If you’re receiving stakes but later they “disappear”, confirm you are not staking on a wrong fork. Start with **[Wrong fork / wrong chain](troubleshooting/wrong-fork.md)**.[^message2007420]
- If Core shows **no peers / no block source**, deleting `peers.dat` is a common first step. See **[No peers](troubleshooting/no-peers.md)**.

---

## Footnotes


[^message2021513]: Telegram export (ReddCoinOfficial), 2025-04-18, obito, message2021513. Note: To stake you must: 1) Unlock the wallet for staking only with the password from the top menu. 2) Click on the bottom right icon (the anvil icon) - Enable Staking I think… Permalink: https://t.me/ReddcoinOfficial/2021513.
[^message2038537]: Telegram export (ReddCoinOfficial), 2026-01-29, obito, message2038537. Note: The staking does not start by default. To stake you must have the wallet fully synchronized with the network. Then there are two steps: 1) Unlock the wallet "for staking… Permalink: https://t.me/ReddcoinOfficial/2038537.
[^message1988235]: Telegram export (ReddCoinOfficial), 2024-03-23, Paulus, message1988235. Note: stop staking, then enable again and then it starts some kind of bug or so, had the same Permalink: https://t.me/ReddcoinOfficial/1988235.
[^message1988846]: Telegram export (ReddCoinOfficial), 2024-03-28, obito, message1988846. Note: I think I know why you are not receiving stakes. It could be that you are not actually staking although you think you are. This wallet version has a bug. Read this: http… Permalink: https://t.me/ReddcoinOfficial/1988846.
[^message2007420]: Telegram export (ReddCoinOfficial), 2024-11-20, John (cryptognasher) Nash, message2007420. Note: If you have a backup of your wallet.dat from v3, you are covered. V4 will not cause you to lose funds. Just to confirm, you are on the correct chain. Compare blockheight… Permalink: https://t.me/ReddcoinOfficial/2007420.
[^message2038108]: Telegram export (ReddCoinOfficial), 2026-01-23, obito, message2038108. Note: If your wallet is on the correct chain, you don't need to run the getblockhash command. Just copy the wallet.dat file to your wallet and send the coins to his new wallet… Permalink: https://t.me/ReddcoinOfficial/2038108.
