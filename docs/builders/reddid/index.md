# ReddID

ReddID is ReddCoin’s identity and social tipping layer. The current product messaging describes it as a human-readable username that links to a ReddCoin wallet, originally delivered as a browser plugin and now being integrated into the Core Wallet as a next-generation foundation. citeturn2view2

## What’s in scope

From the most recent “Comprehensive Design Document” and “Technical Architecture Specification” on the GitHub wiki, the modern ReddID vision expands beyond simple usernames into:

- **Namespaces** (top-level), **User IDs** within namespaces, and **ReddID profiles** that can link identities across namespaces citeturn0view1
- Network-level protocol extensions (P2P messages) and wallet/API interfaces (RPC categories) citeturn3view2turn3view4

## Canonical source docs

- Comprehensive Design Document (ReddID): https://github.com/reddcoin-project/reddcoin/wiki/Comprehensive-Design-Document-Reddid citeturn0view1
- Technical Architecture Specification: https://github.com/reddcoin-project/reddcoin/wiki/Reddid-Technical-Architecture-Specification citeturn3view2

Next: read **Design (auction + identity model)** and **Architecture (components, P2P, RPC)** in this section.


## Builder-ready references

- [Namespaces](namespaces.md)
- [Database schema](database-schema.md)
- [Implementation plan](implementation-plan.md)
