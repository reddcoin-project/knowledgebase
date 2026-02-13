# Fix: stuck / unconfirmed transactions (zapwallettxes)

--8<-- "_includes/safety-banner.md"

**Applies to:** Core desktop wallets (mostly v3.x; still relevant conceptually in v4)

## Symptoms

- You sent RDD but it stays **unconfirmed**
- Transaction shows as “stuck”
- Balance looks “locked” by an unconfirmed tx

## The standard fix

Community support repeatedly points users to the legacy wiki runbook for `zapwallettxes`, and recommends setting a small custom fee afterward to avoid repeats. [^tg-2024-03-02-1984569] [^tg-2024-02-21-1982275]

1. Follow the runbook:
   - Legacy wiki: “Remove stuck transactions with zapwallettxes”
2. After clearing the stuck tx, resend with a **custom fee** (example settings below).

### Fee settings (field-tested)

In the Send window:

- Choose **Custom**
- Choose **total at least**
- Set **total at least = 1 RDD**
- Ensure “Send as zero-fee transaction if possible” is **unchecked**

With those settings, admins noted the fee typically becomes **0.1 RDD**. [^tg-2024-03-02-1984569]

## Footnotes

[^tg-2024-03-02-1984569]: Telegram export (ReddCoinOfficial), obito, 2 Mar 2024 03:47 UTC-05, message1984569 (messages947.html). (zapwallettxes wiki link + fee settings.)
[^tg-2024-02-21-1982275]: Telegram export (ReddCoinOfficial), Kpcrypt0, 21 Feb 2024 16:11 UTC-05, message1982275 (messages945.html). (zapwallettxes wiki link + set custom fee.)
