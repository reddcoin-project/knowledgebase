# Wrong fork / wrong chain recovery

This page documents what to do when your wallet is **on the wrong chain** (a fork), or is connected mostly to peers on a fork. Symptoms include:

- Your wallet reports “synced”, but explorers show a different block height
- Outgoing transactions never appear on explorers
- You receive “stakes” that later disappear after a resync
- Exchange deposits/withdrawals don’t arrive even though you used the right address

!!! warning "Backups first"
    Before any repair steps, **backup** your wallet files (`wallet.dat` and/or `wallets/`).

---

## Step 1: Verify you are on the canonical chain (console checks)

During a 2024 incident window, admins published **known block hashes** at fixed heights so users could detect two specific “bad forks”.[^message2002551]

Open the Core console and run:

### Check A (fork around height 5,448,005)

- `getblockhash 5448005`

Expected (canonical):  
`99e1ba495f4da89c2a0c8a0296cb1df69d5a76488c06517a5aee5c0000c496da`[^message2002551]

Known wrong-fork value:  
`809a59a737c3479ac17ad0fd426193596cc02cfb82cd1c87fa05ef94f8f8587a`[^message2002551]

### Check B (fork around height 5,519,068)

- `getblockhash 5519068`

Expected (canonical):  
`1d6ebb2d73dccc03b7b9b013c3b08ec8a83919ed4480edbad6e0604be53f5b40`[^message2002551][^message2039543]

Known wrong-fork value:  
`420d82c48eea24cd9a06b24cc012bb89abdcab95bdbc29ef02d9fd55ef41f570`[^message2002551]

If your wallet returns the wrong-fork value on either check, you are on a different chain.

---

## Step 2: Safe-default recovery (recommended)

For most users, the safest approach is a **clean resync**:

1. Upgrade to the **current v4 wallet** (see [Version compatibility & upgrades](version-compatibility.md)).
2. Close Core.
3. In the Reddcoin data directory, delete:
   - `blocks/`, `chainstate/`, `indexes/` (if present), and `peers.dat`
4. Restart Core and let it fully sync.
5. Optional: use the official **[v4 bootstrap](bootstrap.md)** to accelerate sync.

This “delete and resync” approach is what admins typically recommend for non-experts to force a wallet back onto the canonical chain.

---

## Step 3: Advanced recovery for known forks (experts only)

For the two 2024 “bad fork” checks above, admins recommended `invalidateblock` with the corresponding wrong-fork hash to rejoin the canonical chain.[^message2002551]

- For fork A:  
  `invalidateblock 809a59a737c3479ac17ad0fd426193596cc02cfb82cd1c87fa05ef94f8f8587a`[^message2002551]
- For fork B:  
  `invalidateblock 420d82c48eea24cd9a06b24cc012bb89abdcab95bdbc29ef02d9fd55ef41f570`[^message2002551]

John also posted the fork-A invalidate command earlier in July 2024 (same hash).[^message1997330]

!!! danger "Only for advanced users"
    `invalidateblock` is powerful. If you’re not comfortable with console commands, prefer **Safe-default recovery** above.

---

## Preventing repeat issues

- Keep Core updated; admins issued **update-required** advisories when old wallet versions were implicated in chain split behavior.[^message2000580]
- If you upgraded from v3 → v4, follow the version-specific guidance in **[Version compatibility](version-compatibility.md)** (don’t reuse v3 chainstate, and clear `peers.dat`).

---

## Footnotes


[^message2002551]: Telegram export (ReddCoinOfficial), 2024-09-14, obito, message2002551. Note: We had two bad blockchain splits. First at block 5448005 and the second one at block 5519068. I) To verify if you're on the first bad fork run in the Console of the Core… Permalink: https://t.me/ReddcoinOfficial/2002551.
[^message2039543]: Telegram export (ReddCoinOfficial), 2026-02-13, obito, message2039543. Note: Run in the Console of the Core Wallet: getblockhash 5519068 Is the output of this command this string of characters? 1d6ebb2d73dccc03b7b9b013c3b08ec8a83919ed4480edbad6e0… Permalink: https://t.me/ReddcoinOfficial/2039543.
[^message1997330]: Telegram export (ReddCoinOfficial), 2024-07-05, John (cryptognasher) Nash, message1997330. Note: just to help out here..and for completeness in the console of core wallet invalidateblock 809a59a737c3479ac17ad0fd426193596cc02cfb82cd1c87fa05ef94f8f8587a this will take… Permalink: https://t.me/ReddcoinOfficial/1997330.
[^message2000580]: Telegram export (ReddCoinOfficial), 2024-08-17, HPMentjox, message2000580. Note: ‼️ Important - Update Required ‼️ The ReddCoin CoreTeam has been tracking these incidental chainsplits that have happened twice now, and we have found an issue which is … Permalink: https://t.me/ReddcoinOfficial/2000580.
