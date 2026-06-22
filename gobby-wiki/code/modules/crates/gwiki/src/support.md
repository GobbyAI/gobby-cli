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

## crates/gwiki/src/support

The `support` module is the internal utility layer for the `gwiki` crate. It consolidates cross-cutting concerns — configuration resolution, environment discovery, text processing, graph construction, search helpers, scoping, PostgreSQL access, time utilities, and counters — so that the rest of the crate can import focused primitives without duplicating infrastructure logic. Nothing in this module is part of the public crate API; all symbols carry `pub(crate)` visibility and are imported directly by the indexer, graph, search, and command layers above.

Configuration and environment resolution are the most interconnected concerns. `env.rs` owns the database-URL discovery chain: it checks environment variables first, then falls back to a brokered lookup against `bootstrap.yaml`, then a direct file parse, and finally a `gobby_core` `gcore` config read (env.rs:33–49). `config.rs` builds on top of this by constructing a layered `AiConfigSource` whose primary layer is `HubPrimary` — an owned, optional `postgres::Client` that resolves `$secret:` references through the PostgreSQL hub when reachable, and rejects them with a clear error when the hub is absent (config.rs:22–44). `hub_ai_config_source()` calls `super::env::database_url_for` to obtain the connection string and delegates secret resolution to `gobby_core::secrets` (config.rs:47–62). The `search` sub-module supplies `PostgresConfigSource`, which is re-imported by `config.rs` (config.rs:9).

Text and graph utilities form a second cohesive pair. `text.rs` provides tokenisation (`query_tokens`), keyword scoring, safe path sanitisation (`sanitize_code_path` rejects absolute paths and `..` traversals), snippet extraction, and degradation label formatting. `graph.rs` imports `text::slugify` (graph.rs:6) to build the slug-to-path index used when resolving wiki link targets inside `memory_graph_from_store`, which converts a `MemoryWikiStore` + `SearchScope` into a `MemoryWikiGraph` containing documents, resolved links, and source mappings (graph.rs:7–54). `scope.rs`, `search.rs`, `counts.rs`, `time.rs`, and `postgres.rs` round out the layer with the remaining 10 + 8 + 7 + 3 + 2 symbols respectively.

### Environment variables (env.rs:13–17)

| Variable | Purpose | Default |
|---|---|---|
| `GWIKI_DATABASE_URL` | Primary PostgreSQL DSN override | — |
| `GOBBY_POSTGRES_DSN` | Secondary PostgreSQL DSN fallback | — |
| `GWIKI_BROKER_TIMEOUT_MS` | Broker connection timeout in milliseconds | `7000` |

### Notable constants and limits

| Symbol | Value | Location |
|---|---|---|
| `DEFAULT_MAX_INBOX_ITEM_BYTES` | 500 000 000 (500 MB) | env.rs:3 |
| `DEFAULT_BROKER_TIMEOUT` | 7 000 ms | env.rs:17 |
| `DEFAULT_SHARED_CODE_GRAPH_EDGE_LIMIT` | 200 | config.rs:64 |

### Key public(crate) API surface

| File | Representative symbols |
|---|---|
| `config.rs` | `HubPrimary`, `hub_ai_config_source` |
| `env.rs` | `database_url`, `database_url_for`, `database_url_from_env` |
| `text.rs` | `query_tokens`, `keyword_score`, `sanitize_code_path`, `snippet_from_text`, `degradation_label` |
| `graph.rs` | `memory_graph_from_store` |
| `search.rs` | `PostgresConfigSource` (imported by `config.rs`) |
| `postgres.rs` | 2 PostgreSQL helper symbols |
| `scope.rs` | 10 scope-management symbols |
| `counts.rs` | 7 counting symbols |
| `time.rs` | 3 time-formatting symbols |
[crates/gwiki/src/support/config.rs:18-20]
[crates/gwiki/src/support/counts.rs:4-10]
[crates/gwiki/src/support/env.rs:21-24]
[crates/gwiki/src/support/graph.rs:8-55]
[crates/gwiki/src/support/postgres.rs:6-39]

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

