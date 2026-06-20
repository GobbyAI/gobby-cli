---
title: crates/gcore/src/config
type: code_module
provenance:
- file: crates/gcore/src/config/mod.rs
- file: crates/gcore/src/config/resolve.rs
- file: crates/gcore/src/config/tests.rs
- file: crates/gcore/src/config/types.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/config

Parent: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Overview

`crates/gcore/src/config` is the shared configuration-resolution boundary for Gobby Rust crates, keeping lightweight contracts and resolver entry points behind one public module surface (`crates/gcore/src/config/mod.rs:1-17`). It owns common service config types for FalkorDB, Qdrant, embeddings, indexing, AI routing, AI capability bindings, tuning, and feature candidates, while leaving consumer-specific choices such as graph names and collection names outside the shared layer (`crates/gcore/src/config/types.rs:1-30`).

The main flow is: stored config values are decoded, environment patterns like `${VAR}` and `${VAR:-default}` are resolved, then typed resolver functions produce concrete configs for services and AI capabilities (`crates/gcore/src/config/resolve.rs:1-100`). Defaults are centralized here, including FalkorDB port `16379`, embedding model `nomic-embed-text`, embedding timeout `10`, AI max concurrency `1`, and indexing’s default `respect_gitignore = true` (`crates/gcore/src/config/resolve.rs:1-8`, `crates/gcore/src/config/types.rs:25-37`).

This module collaborates outward through re-exports: callers import `ConfigSource`, `LayeredConfigSource`, resolver functions, and typed config structs from `config::...` rather than reaching into `resolve` or `types` directly (`crates/gcore/src/config/mod.rs:6-24`). It also defines cross-crate constants and shared naming contracts, including the `CODE_GRAPH_NAME` used by gcode’s code graph projection and AI capability names shared with the daemon registry (`crates/gcore/src/config/mod.rs:9-17`, `crates/gcore/src/config/types.rs:76-100`). Internally, tests isolate process environment mutation behind `EnvGuard` and capture warnings with a test logger, reflecting that env resolution is a key behavior under test (`crates/gcore/src/config/tests.rs:1-100`).

| Public Symbol | Kind | Purpose |
| --- | --- | --- |
| `CODE_GRAPH_NAME` | constant | FalkorDB graph name for gcode code graph projection (`crates/gcore/src/config/mod.rs:9-10`) |
| `ConfigSource`, `LayeredConfigSource`, `EnvOnlySource` | source abstractions | Provide config lookup/resolution sources (`crates/gcore/src/config/mod.rs:12-17`) |
| `decode_config_value` | function | Decodes stored config-store values from JSON/raw representations (`crates/gcore/src/config/resolve.rs:10-22`) |
| `resolve_env_pattern` | function | Resolves `${VAR}` and `${VAR:-default}` patterns (`crates/gcore/src/config/resolve.rs:24-100`) |
| `resolve_falkordb_config`, `resolve_qdrant_config`, `resolve_embedding_config`, `resolve_indexing_config` | functions | Produce typed service/indexing configs (`crates/gcore/src/config/mod.rs:12-17`) |
| `AiCapability`, `AiRouting`, `CapabilityBinding`, `AiTuning` | types | Shared AI routing and capability contracts (`crates/gcore/src/config/mod.rs:18-24`, `crates/gcore/src/config/types.rs:39-100`) |

| Key / Env Var | Role | Default / Notes |
| --- | --- | --- |
| `indexing.respect_gitignore` | Config key for indexing behavior | Re-exported as `INDEXING_RESPECT_GITIGNORE_KEY` (`crates/gcore/src/config/resolve.rs:1-8`) |
| `GOBBY_INDEXING_RESPECT_GITIGNORE` | Env override for indexing behavior | Used by indexing resolver (`crates/gcore/src/config/resolve.rs:1-8`) |
| `GOBBY_FALKORDB_HOST`, `GOBBY_FALKORDB_PORT`, `GOBBY_FALKORDB_PASSWORD` | FalkorDB test/env keys | Cleared by test `EnvGuard` (`crates/gcore/src/config/tests.rs:46-77`) |
| `GOBBY_QDRANT_URL`, `GOBBY_QDRANT_API_KEY` | Qdrant test/env keys | Cleared by test `EnvGuard` (`crates/gcore/src/config/tests.rs:46-77`) |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcore/src/config/mod.rs\|crates/gcore/src/config/mod.rs]] | `crates/gcore/src/config/mod.rs` has no indexed API symbols. |
| [[code/files/crates/gcore/src/config/resolve.rs\|crates/gcore/src/config/resolve.rs]] | `crates/gcore/src/config/resolve.rs` exposes 34 indexed API symbols. |
| [[code/files/crates/gcore/src/config/tests.rs\|crates/gcore/src/config/tests.rs]] | `crates/gcore/src/config/tests.rs` exposes 26 indexed API symbols. |
| [[code/files/crates/gcore/src/config/types.rs\|crates/gcore/src/config/types.rs]] | `crates/gcore/src/config/types.rs` exposes 31 indexed API symbols. |

