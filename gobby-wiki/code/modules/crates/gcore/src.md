---
title: crates/gcore/src
type: code_module
provenance:
- file: crates/gcore/src/ai/daemon/tests.rs
- file: crates/gcore/src/ai/embeddings.rs
- file: crates/gcore/src/ai/mod.rs
- file: crates/gcore/src/ai/probe.rs
- file: crates/gcore/src/ai/transcription.rs
- file: crates/gcore/src/ai/vision.rs
- file: crates/gcore/src/ai_context.rs
- file: crates/gcore/src/ai_types.rs
- file: crates/gcore/src/bootstrap.rs
- file: crates/gcore/src/cli_contract.rs
- file: crates/gcore/src/config/resolve.rs
- file: crates/gcore/src/config/tests.rs
- file: crates/gcore/src/config/types.rs
- file: crates/gcore/src/daemon_url.rs
- file: crates/gcore/src/degradation.rs
- file: crates/gcore/src/falkor.rs
- file: crates/gcore/src/graph_analytics.rs
- file: crates/gcore/src/graph_analytics/leiden.rs
- file: crates/gcore/src/indexing.rs
- file: crates/gcore/src/postgres.rs
- file: crates/gcore/src/provisioning/bootstrap.rs
- file: crates/gcore/src/provisioning/docker.rs
- file: crates/gcore/src/provisioning/hub.rs
- file: crates/gcore/src/provisioning/mod.rs
- file: crates/gcore/src/provisioning/tests.rs
- file: crates/gcore/src/qdrant.rs
- file: crates/gcore/src/qdrant/tests.rs
- file: crates/gcore/src/search.rs
- file: crates/gcore/src/secrets.rs
- file: crates/gcore/src/setup.rs
provenance_truncated: 13
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src

Parent: [[code/modules/crates/gcore|crates/gcore]]

## Overview

## crates/gcore/src

`gcore` is the foundational shared library for the gobby platform. It owns every cross-cutting concern that more than one binary or domain crate depends on: multi-modal AI dispatch, graph database access, vector-store operations, hybrid search, file indexing, PostgreSQL connectivity, secret/config resolution, service provisioning, and structured degradation reporting. The crate is intentionally transport-agnostic at its boundary — `ai_context.rs` resolves desired AI bindings and routing from caller-supplied config layers without importing any HTTP client, leaving probe-backed route collapse to the `ai` sub-module (ai_context.rs:1-6). The single public root (`lib.rs`) re-exports the sub-module tree so downstream crates receive a stable, version-locked surface.

The AI subsystem (`ai/`) provides five modal capabilities dispatched through a four-way routing enum. `ai/mod.rs` resolves the effective route via `effective_route` / `effective_route_with_probe` (ai/mod.rs:31-66): explicit `Off`, `Direct`, or `Daemon` modes are forced through unchanged; `Auto` probes the local daemon's status endpoint via `ai/probe.rs` and falls back to a configured direct endpoint or `Off`. All outbound requests are retried up to `MAX_RETRIES = 2` times with exponential backoff capped at 30 s, jitter, and `Retry-After` header parsing. Per-modal timeout constants reflect practical latency profiles: text generation gets 300 s for large local-reasoning models, vision 60 s, embeddings 10 s, and STT chunks 120 s (ai/mod.rs:22-28). `ai_context.rs` owns the concurrency limiter (`AiLimiter` / `AiPermit`) that enforces `max_concurrency` across the shared `AiContext`, and surfaces `AiContextOptions` for command-scoped `--no-ai` or forced routing overrides.

The storage layer bundles three distinct backends. `falkor.rs` wraps FalkorDB/RedisGraph with a `GraphClient` that handles Cypher identifier escaping, error classification, and a `ReadOnlySyncGraph` for read-path sharing. `qdrant.rs` manages Qdrant collections — creation, upsert (batched), vector search, and schema compatibility checks — surfacing a `CollectionScope` type for namespacing. `postgres.rs` provides read-only and read-write connection factories with a full TLS mode matrix (`Unverified`, `VerifyCA`, `VerifyFull`) and schema-validation hooks. `graph_analytics/leiden.rs` implements a deterministic, RNG-free, weighted Leiden community-detection kernel operating on dense integer indices, which the `graph_analytics.rs` façade adapts to the public `AnalyticsGraph` / `Community` / `CentralityScore` types (leiden.rs:1-12). `search.rs` fuses BM25 and vector hits via Reciprocal Rank Fusion (`rrf_merge`) and sanitises PostgreSQL full-text queries.

Configuration, secrets, and provisioning form the operational backbone. The `config` child module defines `ConfigSource`, `LayeredConfigSource`, and all resolution functions (`resolve_capability_binding`, `resolve_ai_tuning`, `resolve_embedding_config`, etc.) that populate `AiContext`. `secrets.rs` resolves inline secret references and Fernet-encrypted values from config strings. `provisioning/` owns `StandaloneConfig` (a YAML key-value store at `~/.gobby/gcore.yaml`), Docker service orchestration (`provision_docker_services`), and the `ensure_hub` flow that probes, records, and reconciles PostgreSQL hub identity. `daemon_url.rs` resolves the local AI daemon base URL from the bootstrap file or environment overrides, normalising wildcard bind addresses to loopback.

---

### AI Capability Routing

| Route value | Behaviour |
|---|---|
| `Off` | Capability disabled; no requests sent |
| `Direct` | POST directly to configured `api_base` endpoint |
| `Daemon` | Forward through local gobby AI daemon |
| `Auto` | Probe daemon; use `Daemon` if available, else `Direct` or `Off` |

### Per-Modal Timeouts

| Capability | Timeout |
|---|---|
| `TextGenerate` | 300 s |
| `VisionExtract` | 60 s |
| `AudioTranscribe` / `AudioTranslate` | 120 s per chunk |
| `Embed` | 10 s |

### AI Capabilities (`AiCapability`)

| Variant | `as_str` key |
|---|---|
| `Embed` | `ai.embeddings` |
| `AudioTranscribe` | `ai.audio.transcribe` |
| `AudioTranslate` | `ai.audio.translate` |
| `VisionExtract` | `ai.vision` |
| `TextGenerate` | `ai.text` |

### Public Result Types (`ai_types.rs`)

| Type | Purpose |
|---|---|
| `TranscriptionResult` / `TranscriptionSegment` | STT / translation output, millisecond-normalised segments |
| `VisionResult` | Image description + OCR text + metadata map |
| `TextResult` | Chat-completion text + token usage + reasoning effort |
| `TokenUsage` | Prompt / completion / total token counts |
| `AiError` | Typed errors: `capability_unavailable`, `not_configured`, `transport_failure`, `rate_limited`, `parse_failure` |

### Graph Analytics Outputs (`graph_analytics.rs`)

| Symbol | Description |
|---|---|
| `CentralityScore` | Betweenness / degree centrality per node |
| `Community` | Leiden-detected community membership |
| `Hotspot` | Nodes with anomalously high connection density |
| `BridgeSearch` | Tarjan-based bridge-node/edge detection |

### Retry Policy Constants

| Constant | Value |
|---|---|
| `MAX_RETRIES` | 2 |
| `BASE_BACKOFF` | 250 ms |
| `MAX_BACKOFF` | 30 s |

### Key Config/Env Resolution Helpers

| Function | Role |
|---|---|
| `resolve_capability_binding` | Reads routing, api_base, api_key, model per capability |
| `resolve_embedding_config` | Resolves embedding dimension, model, provider |
| `resolve_ai_tuning` | Reads `max_concurrency` and generation tuning knobs |
| `resolve_secret` | Decrypts Fernet-wrapped or env-patterned config values |
| `daemon_url` / `daemon_url_at` | Builds daemon base URL from bootstrap file + env overrides |
| `gobby_home` | Returns `$GOBBY_HOME` or `~/.gobby` |
[crates/gcore/src/graph_analytics/leiden.rs:32-40]
[crates/gcore/src/ai/daemon/operations.rs:20-72]
[crates/gcore/src/ai/daemon/transport.rs:8-12]
[crates/gcore/src/ai/daemon/types.rs:4-9]
[crates/gcore/src/config/mod.rs:1-31]

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gcore/src/ai\|crates/gcore/src/ai]] | ## crates/gcore/src/ai |
| [[code/modules/crates/gcore/src/config\|crates/gcore/src/config]] | ## crates/gcore/src/config |
| [[code/modules/crates/gcore/src/graph_analytics\|crates/gcore/src/graph_analytics]] | ## crates/gcore/src/graph_analytics |
| [[code/modules/crates/gcore/src/provisioning\|crates/gcore/src/provisioning]] | ## crates/gcore/src/provisioning |
| [[code/modules/crates/gcore/src/qdrant\|crates/gcore/src/qdrant]] | ## crates/gcore/src/qdrant |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcore/src/ai/daemon/transport.rs\|crates/gcore/src/ai/daemon/transport.rs]] | `crates/gcore/src/ai/daemon/transport.rs` exposes 5 indexed API symbols. |
| [[code/files/crates/gcore/src/ai/embeddings.rs\|crates/gcore/src/ai/embeddings.rs]] | `crates/gcore/src/ai/embeddings.rs` exposes 12 indexed API symbols. |
| [[code/files/crates/gcore/src/ai/mod.rs\|crates/gcore/src/ai/mod.rs]] | `crates/gcore/src/ai/mod.rs` exposes 37 indexed API symbols. |
| [[code/files/crates/gcore/src/ai/probe.rs\|crates/gcore/src/ai/probe.rs]] | `crates/gcore/src/ai/probe.rs` exposes 31 indexed API symbols. |
| [[code/files/crates/gcore/src/ai/text.rs\|crates/gcore/src/ai/text.rs]] | `crates/gcore/src/ai/text.rs` exposes 11 indexed API symbols. |
| [[code/files/crates/gcore/src/ai/transcription.rs\|crates/gcore/src/ai/transcription.rs]] | `crates/gcore/src/ai/transcription.rs` exposes 13 indexed API symbols. |
| [[code/files/crates/gcore/src/ai/vision.rs\|crates/gcore/src/ai/vision.rs]] | `crates/gcore/src/ai/vision.rs` exposes 18 indexed API symbols. |
| [[code/files/crates/gcore/src/ai_context.rs\|crates/gcore/src/ai_context.rs]] | `crates/gcore/src/ai_context.rs` exposes 56 indexed API symbols. |
| [[code/files/crates/gcore/src/ai_types.rs\|crates/gcore/src/ai_types.rs]] | `crates/gcore/src/ai_types.rs` exposes 34 indexed API symbols. |
| [[code/files/crates/gcore/src/bootstrap.rs\|crates/gcore/src/bootstrap.rs]] | `crates/gcore/src/bootstrap.rs` exposes 13 indexed API symbols. |
| [[code/files/crates/gcore/src/cli_contract.rs\|crates/gcore/src/cli_contract.rs]] | `crates/gcore/src/cli_contract.rs` exposes 15 indexed API symbols. |
| [[code/files/crates/gcore/src/codewiki_contract.rs\|crates/gcore/src/codewiki_contract.rs]] | `crates/gcore/src/codewiki_contract.rs` exposes 1 indexed API symbol. |
| [[code/files/crates/gcore/src/daemon_url.rs\|crates/gcore/src/daemon_url.rs]] | `crates/gcore/src/daemon_url.rs` exposes 20 indexed API symbols. |
| [[code/files/crates/gcore/src/degradation.rs\|crates/gcore/src/degradation.rs]] | `crates/gcore/src/degradation.rs` exposes 20 indexed API symbols. |
| [[code/files/crates/gcore/src/falkor.rs\|crates/gcore/src/falkor.rs]] | `crates/gcore/src/falkor.rs` exposes 31 indexed API symbols. |
| [[code/files/crates/gcore/src/graph_analytics.rs\|crates/gcore/src/graph_analytics.rs]] | `crates/gcore/src/graph_analytics.rs` exposes 33 indexed API symbols. |
| [[code/files/crates/gcore/src/graph_analytics/leiden.rs\|crates/gcore/src/graph_analytics/leiden.rs]] | `crates/gcore/src/graph_analytics/leiden.rs` exposes 36 indexed API symbols. |
| [[code/files/crates/gcore/src/indexing.rs\|crates/gcore/src/indexing.rs]] | `crates/gcore/src/indexing.rs` exposes 24 indexed API symbols. |
| [[code/files/crates/gcore/src/lib.rs\|crates/gcore/src/lib.rs]] | `crates/gcore/src/lib.rs` exposes 1 indexed API symbol. |
| [[code/files/crates/gcore/src/libpq.rs\|crates/gcore/src/libpq.rs]] | `crates/gcore/src/libpq.rs` exposes 1 indexed API symbol. |
| [[code/files/crates/gcore/src/postgres.rs\|crates/gcore/src/postgres.rs]] | `crates/gcore/src/postgres.rs` exposes 32 indexed API symbols. |
| [[code/files/crates/gcore/src/project.rs\|crates/gcore/src/project.rs]] | `crates/gcore/src/project.rs` exposes 8 indexed API symbols. |
| [[code/files/crates/gcore/src/provisioning/hub.rs\|crates/gcore/src/provisioning/hub.rs]] | `crates/gcore/src/provisioning/hub.rs` exposes 26 indexed API symbols. |
| [[code/files/crates/gcore/src/provisioning/mod.rs\|crates/gcore/src/provisioning/mod.rs]] | `crates/gcore/src/provisioning/mod.rs` exposes 19 indexed API symbols. |
| [[code/files/crates/gcore/src/qdrant.rs\|crates/gcore/src/qdrant.rs]] | `crates/gcore/src/qdrant.rs` exposes 30 indexed API symbols. |
| [[code/files/crates/gcore/src/search.rs\|crates/gcore/src/search.rs]] | `crates/gcore/src/search.rs` exposes 18 indexed API symbols. |
| [[code/files/crates/gcore/src/secrets.rs\|crates/gcore/src/secrets.rs]] | `crates/gcore/src/secrets.rs` exposes 23 indexed API symbols. |
| [[code/files/crates/gcore/src/setup.rs\|crates/gcore/src/setup.rs]] | `crates/gcore/src/setup.rs` exposes 22 indexed API symbols. |

