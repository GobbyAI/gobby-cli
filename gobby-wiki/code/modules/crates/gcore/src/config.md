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

## crates/gcore/src/config

### Responsibilities

This module is the shared configuration-resolution boundary for all Gobby Rust crates (crates/gcore/src/config/mod.rs:1-6). It owns two concerns: lightweight domain types that describe service connections and AI capabilities (`types.rs`), and resolution logic that reads from layered sources and collapses them into those types (`resolve.rs`). The module intentionally stays small so that downstream crates can depend on it without pulling in heavy service machinery. A single constant, `CODE_GRAPH_NAME = "gobby_code"`, pins the FalkorDB graph name used by the `gcode` code-graph projection (crates/gcore/src/config/mod.rs:11).

### Key Flows

Resolution begins with a `ConfigSource` trait implemented by `LayeredConfigSource` and `EnvOnlySource` (crates/gcore/src/config/resolve.rs:1). `LayeredConfigSource` merges an ordered stack of sources, each queried by `config_value` and then `resolve_value`. Raw stored values pass through `decode_config_value`, which parses JSON strings, arrays, objects, and null, falling back to the literal text when the input is not valid JSON (crates/gcore/src/config/resolve.rs:11-21). Values containing `${VAR}` or `${VAR:-default}` shell-like patterns are expanded by `resolve_env_pattern`, which walks the string segment by segment, resolves each named variable from the process environment, and either applies the inline default or leaves the slot unresolved (crates/gcore/src/config/resolve.rs:24-65). Higher-level functions (`resolve_falkordb_config`, `resolve_qdrant_config`, `resolve_embedding_config`, `resolve_indexing_config`, `resolve_capability_binding`, `resolve_ai_tuning`) each call the primitive helpers `resolve_setting`, `resolve_setting_from_keys`, `resolve_port`, `resolve_non_empty`, and `resolve_config_bool` to assemble typed structs from the layered source. Embedding resolution has two additional entry points, `resolve_embedding_config_resolution` and `resolve_embedding_config_from_binding`, to support capability-scoped overrides via `CapabilityBinding`.

### Public API

**Service configuration types** (crates/gcore/src/config/types.rs:1-45)

| Type | Key Fields |
| --- | --- |
| `FalkorConfig` | `host`, `port` (default 16379), `password?: String` |
| `QdrantConfig` | `url?: String`, `api_key?: String` |
| `EmbeddingConfig` | `api_base`, `model` (default `nomic-embed-text`), `api_key?`, `query_prefix?`, `timeout_seconds` (default 10) |
| `IndexingConfig` | `respect_gitignore: bool` (default `true`) |
| `AiTuning` | max concurrency (default 1), tuning fields |
| `CapabilityBinding` | per-capability AI routing + connection overrides |
| `EmbeddingConfigResolution` | resolved embedding config with source provenance |
| `FeatureCandidate` | deserializable feature-flag record |

**`AiRouting` variants** (crates/gcore/src/config/types.rs:46-70)

| Variant | Parse string |
| --- | --- |
| `Auto` (default) | `"auto"` |
| `Daemon` | `"daemon"` |
| `Direct` | `"direct"` |
| `Off` | `"off"` |

**`AiCapability` variants and config key accessors** (crates/gcore/src/config/types.rs:80-100)

| Variant | `as_str` | Key methods |
| --- | --- | --- |
| `Embed` | `"embed"` | `routing_key`, `transport_key`, `api_base_key`, `api_key_key`, `model_key`, `provider_key` |
| `AudioTranscribe` | `"audio_transcribe"` | same set |
| `AudioTranslate` | `"audio_translate"` | same set |
| `VisionExtract` | `"vision_extract"` | same set |
| `TextGenerate` | `"text_generate"` | same set |

**Environment variables read during resolution** (inferred from crates/gcore/src/config/tests.rs:62-85)

| Variable | Purpose |
| --- | --- |
| `GOBBY_FALKORDB_HOST` | FalkorDB hostname |
| `GOBBY_FALKORDB_PORT` | FalkorDB port (default 16379) |
| `GOBBY_FALKORDB_PASSWORD` | FalkorDB password |
| `GOBBY_QDRANT_URL` | Qdrant service URL |
| `GOBBY_QDRANT_API_KEY` | Qdrant API key |
| `GOBBY_INDEXING_RESPECT_GITIGNORE` | Boolean; key `indexing.respect_gitignore` (crates/gcore/src/config/resolve.rs:7-8) |

**Notable public constants** (crates/gcore/src/config/resolve.rs:3-8, crates/gcore/src/config/mod.rs:11)

| Constant | Value |
| --- | --- |
| `CODE_GRAPH_NAME` | `"gobby_code"` |
| `FALKORDB_DEFAULT_PORT` | `16379` |
| `EMBEDDING_DEFAULT_MODEL` | `"nomic-embed-text"` |
| `EMBEDDING_DEFAULT_TIMEOUT_SECONDS` | `10` |
| `INDEXING_RESPECT_GITIGNORE_KEY` | `"indexing.respect_gitignore"` |

### Test Infrastructure

`tests.rs` supplies a suite of in-process fixtures so that resolution logic can be exercised without live services (crates/gcore/src/config/tests.rs:1-100). `TestSource` and its `with_values` / `with_raw_values` constructors provide an in-memory `ConfigSource` backed by a `HashMap`. `FailingResolveSource` injects controlled errors into `resolve_value` for specific keys. `LayeredTestSource` stacks multiple `TestSource` maps to verify priority semantics. `EnvGuard` serializes all process-environment mutations through a crate-level `TEST_ENV_LOCK` mutex and restores a fixed allowlist of `GOBBY_*` keys on drop, preventing cross-test pollution (crates/gcore/src/config/tests.rs:53-85). `TestLogger` and `capture_warn_logs` intercept `log::warn!` emissions so tests can assert on diagnostic output without writing to stderr.

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcore/src/config/mod.rs\|crates/gcore/src/config/mod.rs]] | `crates/gcore/src/config/mod.rs` has no indexed API symbols. |
| [[code/files/crates/gcore/src/config/resolve.rs\|crates/gcore/src/config/resolve.rs]] | `crates/gcore/src/config/resolve.rs` exposes 34 indexed API symbols. |
| [[code/files/crates/gcore/src/config/tests.rs\|crates/gcore/src/config/tests.rs]] | `crates/gcore/src/config/tests.rs` exposes 26 indexed API symbols. |
| [[code/files/crates/gcore/src/config/types.rs\|crates/gcore/src/config/types.rs]] | `crates/gcore/src/config/types.rs` exposes 31 indexed API symbols. |

