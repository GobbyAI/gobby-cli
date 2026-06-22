---
title: crates/gcore/src/qdrant
type: code_module
provenance:
- file: crates/gcore/src/qdrant/naming.rs
- file: crates/gcore/src/qdrant/tests.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/qdrant

Parent: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Overview

## crates/gcore/src/qdrant

This module is the core abstraction layer between `gcore` and a Qdrant vector-database backend. It owns two concerns: safe, validated collection-name construction (`naming.rs`) and the behavioral contract tests that exercise the full Qdrant client surface (`tests.rs`). The public API exposed here is consumed by higher-level features in `gcore` — such as symbol search and project-scoped vector stores — without those callers needing to reason about raw Qdrant HTTP semantics.

### Collection naming

`naming.rs` encodes the convention that every Qdrant collection owned by `gcore` carries a namespace prefix and a scope qualifier naming.rs:1-65. `CollectionScope` controls which pattern is applied:

| Variant | Resulting name pattern | Use case |
|---|---|---|
| `Project(&str)` | `{namespace}_project_{id}` | Per-project vector store |
| `Topic(&str)` | `{namespace}_topic_{name}` | Topic-scoped shared store |
| `Custom(&str)` | verbatim `name` | Caller-managed or legacy names |

The `collection_name` function delegates to `validate_collection_name_component` before formatting any string naming.rs:26-45. Validation rejects empty strings, path-like reserved names (`.` and `..`), surrounding whitespace, and characters that would be illegal in filesystem or URL contexts (`/`, `\`, `:`, ASCII control characters) naming.rs:47-68. Failures surface as typed `CollectionNameError` variants, making error handling exhaustive at call sites.

| Error variant | Condition |
|---|---|
| `Empty` | Zero-length component |
| `Reserved` | Component equals `.` or `..` |
| `InvalidCharacter` | Control chars, whitespace, `/`, `\`, `:` |
| `SurroundingWhitespace` | Leading or trailing whitespace |

### Client contract and test coverage

`tests.rs` acts as an executable specification of the module's behavioral contracts. The `with_qdrant_degradation_contract` test verifies that `with_qdrant` returns `ServiceState::NotConfigured` when no config is supplied or when the config's URL is absent, and `ServiceState::Available` only for a fully-specified config tests.rs:33-57. This makes the degradation signal explicit and machine-checkable. The `sync_search_from_cli_path` test spins up a local TCP listener via `spawn_qdrant_response`, fires a real HTTP `search` call, and asserts on scored result payloads tests.rs:59-90. Complementary tests cover upsert batching (`upsert_batched_splits_points_by_batch_size`), rejection of incomplete Qdrant operations (`upsert_rejects_non_completed_qdrant_operation`), typed HTTP error mapping (`qdrant_http_failures_are_typed_errors`), server-error-only unreachability classification (`qdrant_http_status_unreachable_only_for_server_errors`), collection schema validation, lifecycle management (schema enforcement and filtered-point deletion), and point-count reads against collection info.

### Key public API symbols

| Symbol | Kind | File |
|---|---|---|
| `CollectionScope` | enum | naming.rs:1 |
| `CollectionNameError` | enum | naming.rs:11 |
| `collection_name` | fn | naming.rs:26 |
| `validate_collection_name_component` | fn (private) | naming.rs:47 |
| `UpsertRequest` | struct | (parent module, exercised in tests.rs:14) |
| `SearchRequest` | struct | (parent module, exercised in tests.rs:21) |
| `with_qdrant` | fn | (parent module, exercised in tests.rs:33) |
| `search` | fn | (parent module, exercised in tests.rs:74) |

### Cross-module collaboration

The tests import `crate::config::QdrantConfig` for URL/API-key configuration and `crate::degradation::ServiceState` to assert on availability outcomes tests.rs:2-3. HTTP fixture infrastructure comes from `crate::test_http` (`spawn_json_response_with_status`, `RequestHandle`, `read_http_request`) tests.rs:4, allowing tests to intercept outbound Qdrant HTTP calls without a live instance. The module therefore sits between the configuration layer (`crate::config`), the degradation-state machinery (`crate::degradation`), and any feature crate that needs namespaced Qdrant collections — providing both the naming contract and the HTTP client wrapper as stable integration points.
[crates/gcore/src/qdrant/naming.rs:3-10]
[crates/gcore/src/qdrant/tests.rs:12-30]
[crates/gcore/src/qdrant/naming.rs:13-22]
[crates/gcore/src/qdrant/naming.rs:25-43]
[crates/gcore/src/qdrant/naming.rs:45-70]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcore/src/qdrant/naming.rs\|crates/gcore/src/qdrant/naming.rs]] | `crates/gcore/src/qdrant/naming.rs` exposes 7 indexed API symbols. |
| [[code/files/crates/gcore/src/qdrant/tests.rs\|crates/gcore/src/qdrant/tests.rs]] | `crates/gcore/src/qdrant/tests.rs` exposes 15 indexed API symbols. |

