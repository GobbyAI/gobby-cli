---
title: crates/gwiki/src/support
type: code_module
provenance:
- file: crates/gwiki/src/support/config.rs
- file: crates/gwiki/src/support/counts.rs
- file: crates/gwiki/src/support/env.rs
- file: crates/gwiki/src/support/graph.rs
- file: crates/gwiki/src/support/mod.rs
- file: crates/gwiki/src/support/postgres.rs
- file: crates/gwiki/src/support/scope.rs
- file: crates/gwiki/src/support/search.rs
- file: crates/gwiki/src/support/text.rs
- file: crates/gwiki/src/support/time.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/support

Parent: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/support` is the utility layer for gwiki runtime plumbing: configuration, environment discovery, graph shaping, and text/search helpers. Config is hub-aware: `HubPrimary` implements `ConfigSource`, reads values through PostgreSQL when available, resolves `$secret:` values through the hub, and rejects secret references when no hub exists (crates/gwiki/src/support/config.rs:18-43). `hub_ai_config_source` ties this to command execution by resolving Gobby home, asking `support::env::database_url_for` for a hub DSN, optionally connecting to Postgres, and building an `AiConfigSource` (crates/gwiki/src/support/config.rs:46-60).

Environment resolution is the main inbound collaboration point for hub-backed flows. `database_url` prefers explicit env vars, then falls back through Gobby home bootstrap/broker resolution, bootstrap file values, and gcore config (crates/gwiki/src/support/env.rs:32-49). `config` imports core config/provisioning, `postgres::Client`, crate indexer/error types, and `super::search::PostgresConfigSource`, then calls `super::env::database_url_for` during AI config construction (crates/gwiki/src/support/config.rs:1-10, crates/gwiki/src/support/config.rs:52-53).

The text and graph helpers normalize data before higher-level features consume it. `text` tokenizes and scores search strings, sanitizes repo-relative code paths, clips snippets, and produces stable degradation labels (crates/gwiki/src/support/text.rs:7-69). `graph` converts a `store::MemoryWikiStore` plus `search::SearchScope` into `graph::MemoryWikiGraph` facts, resolving internal links, skipping external targets, and using `text::slugify` for slug lookup (crates/gwiki/src/support/graph.rs:4-6, crates/gwiki/src/support/graph.rs:8-84).

| Symbol | Role | Source |
| --- | --- | --- |
| `hub_ai_config_source` | Builds hub-aware AI config source | crates/gwiki/src/support/config.rs:46-60 |
| `database_url` | Resolves hub database URL | crates/gwiki/src/support/env.rs:32-49 |
| `database_url_for` | Wraps DB URL errors as `WikiError::Config` | crates/gwiki/src/support/env.rs:51-55 |
| `database_url_from_env` | Reads explicit DB env vars | crates/gwiki/src/support/env.rs:57-65 |
| `query_tokens` / `keyword_score` | Query normalization and scoring | crates/gwiki/src/support/text.rs:7-22 |
| `sanitize_code_path` | Rejects unsafe code paths | crates/gwiki/src/support/text.rs:24-45 |
| `memory_graph_from_store` | Builds in-memory graph facts | crates/gwiki/src/support/graph.rs:8-55 |

| Key / Constant | Value / Behavior | Source |
| --- | --- | --- |
| `GWIKI_DATABASE_URL` | Preferred explicit DB URL env var | crates/gwiki/src/support/env.rs:14-16 |
| `GOBBY_POSTGRES_DSN` | Fallback explicit DB URL env var | crates/gwiki/src/support/env.rs:14-16 |
| `GWIKI_BROKER_TIMEOUT_MS` | Broker timeout override env var | crates/gwiki/src/support/env.rs:16-18 |
| `DEFAULT_BROKER_TIMEOUT` | 7000 ms | crates/gwiki/src/support/env.rs:18 |
| `DEFAULT_MAX_INBOX_ITEM_BYTES` | 500 MB import ceiling | crates/gwiki/src/support/env.rs:1-4 |
| `DEFAULT_SHARED_CODE_GRAPH_EDGE_LIMIT` | 200 | crates/gwiki/src/support/config.rs:63 |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/src/support/config.rs\|crates/gwiki/src/support/config.rs]] | `crates/gwiki/src/support/config.rs` exposes 30 indexed API symbols. |
| [[code/files/crates/gwiki/src/support/counts.rs\|crates/gwiki/src/support/counts.rs]] | `crates/gwiki/src/support/counts.rs` exposes 7 indexed API symbols. |
| [[code/files/crates/gwiki/src/support/env.rs\|crates/gwiki/src/support/env.rs]] | `crates/gwiki/src/support/env.rs` exposes 22 indexed API symbols. |
| [[code/files/crates/gwiki/src/support/graph.rs\|crates/gwiki/src/support/graph.rs]] | `crates/gwiki/src/support/graph.rs` exposes 11 indexed API symbols. |
| [[code/files/crates/gwiki/src/support/mod.rs\|crates/gwiki/src/support/mod.rs]] | `crates/gwiki/src/support/mod.rs` has no indexed API symbols. |
| [[code/files/crates/gwiki/src/support/postgres.rs\|crates/gwiki/src/support/postgres.rs]] | `crates/gwiki/src/support/postgres.rs` exposes 2 indexed API symbols. |
| [[code/files/crates/gwiki/src/support/scope.rs\|crates/gwiki/src/support/scope.rs]] | `crates/gwiki/src/support/scope.rs` exposes 10 indexed API symbols. |
| [[code/files/crates/gwiki/src/support/search.rs\|crates/gwiki/src/support/search.rs]] | `crates/gwiki/src/support/search.rs` exposes 8 indexed API symbols. |
| [[code/files/crates/gwiki/src/support/text.rs\|crates/gwiki/src/support/text.rs]] | `crates/gwiki/src/support/text.rs` exposes 13 indexed API symbols. |
| [[code/files/crates/gwiki/src/support/time.rs\|crates/gwiki/src/support/time.rs]] | `crates/gwiki/src/support/time.rs` exposes 3 indexed API symbols. |

