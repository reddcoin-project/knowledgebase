# ReddID Technical Architecture (curated)

This page curates the **ReddID Technical Architecture Specification** wiki document into a quick reference for engineers and builders. citeturn3view2

## Table of contents (as published)

The spec organizes the system into: overview, architecture, components, database schema, blockchain integration, P2P protocol extensions, API interfaces, security model, dependencies, performance, deployment, and implementation guidelines. citeturn3view2

## Two practical anchor points

### P2P protocol extensions

The spec describes new P2P message categories for:
- namespace auctions/config,
- user ID auctions,
- and ReddID/profile exchanges. citeturn3view4

### RPC / API interfaces

The spec groups RPC commands into categories such as “Namespace Commands” and “User ID Commands” (and additional categories beyond that) to support wallet and third‑party integrations. citeturn3view4

## External dependencies (as published)

The spec calls out dependency floors such as **LevelDB 1.22+**, **OpenSSL 1.1.1+**, and **Boost 1.70.0+**. citeturn3view4

## Canonical source

Full spec: https://github.com/reddcoin-project/reddcoin/wiki/Reddid-Technical-Architecture-Specification citeturn3view2
