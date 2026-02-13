---
title: Tipping on Twitch
---

On Twitch, the classic ReddCoin tipbot user referenced in the community guide is **heyreddcoin**.

Primary reference: https://www.reddit.com/r/reddCoin/wiki/tipbot_twitch/

!!! info "Last verified: 2026-02-13"
    Twitch chat rate-limits are strict. Commands may feel “slow” during heavy load.

## Register

In the bot channel or a channel where it is present:

```
+register
```

In a public channel (with the bot), you may need to prepend:

```
@heyreddcoin +register
```

## Check your account

```
+info
```

(or `@heyreddcoin +info` in public channels)

## Tip the streamer (default)

To tip the channel owner (common case):

```
+tip 100 RDD
```

To tip another user:

```
+tip @recipient 100 RDD
```

## Withdraw

```
+withdraw <RDD_address> 100 RDD
```

## Troubleshooting

- **No response / delays:** the guide explains Twitch rate limits and lossy chat delivery.
- **Bot not present:** the bot must be in the channel (or use its own channel).
- **Use small tests first** before big tips.
