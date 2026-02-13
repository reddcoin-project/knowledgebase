---
title: Tipping on Twitter/X
---

ReddCoin tipping on Twitter/X has historically been driven through the **@tipreddcoin** bot and a “+command” syntax.

Primary reference: https://www.reddit.com/r/reddCoin/wiki/tipbot_twitter/

!!! info "Last verified: 2026-02-13"
    Commands and platform behavior can change. If the bot returns errors, check the official ReddBot page and your bot’s `+info`/help output first.

## Register / view your account

1. Follow **@tipreddcoin**.
2. Once mutual follows are enabled, send the command:

```
+info
```

(When used publicly, prefix with `@tipreddcoin`, e.g. `@tipreddcoin +info`.)  
Source: Reddit guide.

## Tip a user

Minimal format:

```
+tip @recipient 100 RDD
```

The guide also notes several aliases (e.g., `+give`, `+send`, `+pay`) and that you can withdraw with a similar pattern.  
Source: Reddit guide.

## Withdraw to your own wallet

```
+withdraw <RDD_address> 100 RDD
```

## Troubleshooting

- **No response:** you may not have mutual follows yet (Twitter DM restrictions are common).
- **Recipient didn’t get it:** the guide notes the recipient may need to follow the bot or accept pending tips.
- **Always keep big balances off the bot:** withdraw to self-custody.
