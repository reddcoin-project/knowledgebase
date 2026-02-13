# Stuck / unconfirmed transactions

If you sent RDD and it remains **unconfirmed**, or you see a “stuck” outgoing transaction that blocks further sends, this runbook captures the most common field-tested fixes.

!!! warning "Back up first"
    Always backup `wallet.dat` (and/or `wallets/`) before using repair flags like `-zapwallettxes`.[^message1940622]

---

## Step 1: Check whether the transaction actually left your wallet

1. Copy the txid.
2. Search it on an explorer (see [Explorer & APIs](../../tech/explorer.md)).

If the txid **does not appear anywhere**, John Nash noted the transaction may not have left the wallet, and recommended `zapwallettxes` as the quickest fix in that situation.[^message1989698]

---

## Step 2: Admin-recommended fix — `zapwallettxes`

The `zapwallettxes` flag removes unconfirmed transactions from your local wallet, allowing you to resend.

### Windows (GUI shortcut)

1. Create a shortcut to `reddcoin-qt.exe`
2. Edit the shortcut target and append:

- `-zapwallettxes=1`[^message1954386]

Start the wallet using that shortcut once, let it load, then close it and start normally.

### Linux/macOS (terminal)

Run once:

- `reddcoin-qt -zapwallettxes=1`

(Exact binary name/path varies by install.)

---

## Step 3: If needed — follow with `-reindex`

If your wallet behaves strangely after a zap pass, admins sometimes suggested following up with a **reindex** run.[^message1962358]

---

## Fee reliability note

obito recommended setting a **small custom fee** when users saw repeated stuck transactions, to improve relay/confirmation behavior.[^message1941782]

---

## Older community references (legacy, but still useful)

- ReddcoinTalk: “(solved) zapwallettxes how to” (legacy guide)  
  https://reddcointalk.org/t/solved-zapwallettxes-how-to/521
- Reddit thread discussing `zapwallettxes` for stuck tx (legacy context):  
  https://www.reddit.com/r/reddCoin/comments/kv6if9/using_zapwallettxes1/

Treat old threads as **Tier 3** and validate against current wallet behavior.

---

## Footnotes


[^message1940622]: Telegram export (ReddCoinOfficial), 2023-09-22, Kpcrypt0, message1940622. Note: @Polee1 I don't know which version of the wallet you are using. But there are a few reasons why this sometimes happens. The good news is that we know how to fix it. Crea… Permalink: https://t.me/ReddcoinOfficial/1940622.
[^message1989698]: Telegram export (ReddCoinOfficial), 2024-04-03, John (cryptognasher) Nash, message1989698. Note: Just jumping on the conv. Checking the txid given, the transaction has not left the wallet. It does not appear on any Explorer. So, the quickest method to resolve is to … Permalink: https://t.me/ReddcoinOfficial/1989698.
[^message1954386]: Telegram export (ReddCoinOfficial), 2023-11-13, Kpcrypt0, message1954386. Note: Best way in windows is to create a shortcut on the desktop and add the command line -zapwallettxes=1 Permalink: https://t.me/ReddcoinOfficial/1954386.
[^message1962358]: Telegram export (ReddCoinOfficial), 2023-12-12, unknown, message1962358. Note: Add "-reindex" in the command line. If you don't know how, it's the same as zapwallet. https://wiki.reddcoin.com/Remove_stuck_transactions_with_zapwallettxes Permalink: https://t.me/ReddcoinOfficial/1962358.
[^message1941782]: Telegram export (ReddCoinOfficial), 2023-09-26, obito, message1941782. Note: Your transaction got stuck. To solve the problem please follow the steps from the guide bellow: https://wiki.reddcoin.com/Remove_stuck_transactions_with_zapwallettxes Af… Permalink: https://t.me/ReddcoinOfficial/1941782.
