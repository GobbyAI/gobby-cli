---
title: crates/gcore
type: code_module
provenance:
- file: crates/gcore/assets/docker-compose.services.yml
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
provenance_truncated: 16
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore

Parent: [[code/modules/crates|crates]]

## Overview

## Module: crates/gcore

`crates/gcore` is the foundational library crate of the Gobby system. It owns all domain-independent infrastructure: service provisioning, AI capability dispatch, database and vector-store connectivity, configuration resolution, content indexing, graph analytics, and shared error types. Higher-level crates depend on `gcore` rather than coupling directly to external services; `gcore` acts as the single translation layer between Gobby's configuration model and the underlying runtimes (Postgres, Qdrant, FalkorDB, and AI daemon/direct endpoints).

### Infrastructure Provisioning and Docker Services

The `assets` child module carries compose-template artifacts. The `src` child module exposes `provision_docker_services` / `provision_docker_services_with`, which orchestrate `docker compose up` for the three core backing services. `TcpDockerHealthChecker` polls each service after startup (`wait_postgres`, `wait_qdrant`, `wait_falkordb`). Named volumes, image references, and `pg_search` extension coordinates are centralized in `PgSearchManifest` and `PgSearchVersionFile` so that the build-time SHA-256 hashes remain a single source of truth.

| Service | Key Config Properties |
|---|---|
| `postgres` | `image`, `command`, `POSTGRES_DB/USER/PASSWORD`, `GOBBY_PGAUDIT_LOG`, `ports`, `volumes`, `healthcheck`, `profiles` |
| `qdrant` | `image`, `ports`, `volumes`, `healthcheck`, `restart`, `profiles` |
| `falkordb` | `image`, `ports`, `volumes`, `healthcheck`, `restart`, `profiles` |
| pg_search | `PG_SEARCH_VERSION`, `PG_SEARCH_SHA256` (per `amd64`/`arm64`) |

### AI Capability Routing and Transport

`AiContext` / `AiBindings` resolve which backend handles each `AiCapability` (text generation, embeddings, transcription, vision, audio translation). Routing follows `AiRouting` (`auto` | `daemon` | `direct`), probed at runtime via `probe_daemon_capability` and `CapabilityProbeReport`. `AiTransport` provides the HTTP client with `retry_with_backoff`, `parse_retry_after`, and per-capability `timeout_for` logic. Daemon fan-out helpers (`generate_via_daemon`, `embed_via_daemon`, `transcribe_via_daemon`, `describe_image_via_daemon`) build multipart or JSON requests and parse typed results (`TextResult`, `TranscriptionResult`, `VisionResult`, `DaemonEmbeddingResult`). `AiLimiter` / `AiPermit` enforce a semaphore-backed concurrency cap that callers acquire before dispatching.

| AiCapability key surface | Methods |
|---|---|
| `AiCapability` | `as_str`, `namespace`, `routing_key`, `transport_key`, `api_base_key`, `api_key_key`, `model_key`, `provider_key` |
| `AiRouting` | `from_str` (parses `auto`/`daemon`/`direct`) |
| `AiError` | `capability_unavailable`, `not_configured`, `transport_failure`, `rate_limited`, `parse_failure`, `retry_after` |
| `AiLimiter` | `new`, `max_concurrency`, `acquire`, `try_acquire` |

Config for each capability is resolved through a `ConfigSource` trait implemented by `LocalAiConfigSource` (flat YAML via `StandaloneConfig`), `PostgresAiConfigSource` (DB-backed), `NoPrimaryAiConfigSource`, and `LayeredConfigSource`. Secret interpolation (`resolve_secret`, `derive_fernet_key`, `decrypt_fernet`) and environment-pattern expansion (`resolve_env_pattern`) happen at value-resolution time.

### Database, Vector Store, and Graph Connectivity

Postgres connections flow through `connect_readonly` / `connect_readwrite` with TLS negotiated by `TlsConnectorMode` (`Unverified`, `VerifyCA`, `VerifyFull`) and `sslmode` normalization. `SchemaCheck` wraps domain-supplied validators without taking ownership. `read_config_value` surfaces runtime configuration rows; `TrustedRowId` gates raw row-id usage. Qdrant operations (`ensure_collection`, `search`, `upsert`, `upsert_batched`, `delete_points_by_filter`) are all typed through `VectorCollectionSchema` / `SearchHit` / `UpsertResult` and fail with `QdrantError`. FalkorDB is accessed via `GraphClient` (async) and `ReadOnlySyncGraph`; query tokens are sanitized by `escape_label`, `escape_rel_type`, `escape_property`, and `escape_string`.

### Configuration, Hub Identity, and Standalone Setup

`StandaloneConfig` reads and writes a flat YAML file (`gcore.yaml`) supporting dotted-key nesting, environment-pattern expansion, and JSON-serialized candidate lists. `resolve_embedding_config`, `resolve_capability_routing`, and `resolve_ai_tuning` drive the full AI configuration resolution pipeline. `ensure_hub` / `ensure_hub_with` manage hub database URL discovery, identity probing (`probe_postgres_hub_identity`), conflict detection, and bootstrap file writes. `HubIdentity` surfaces a `display_label` and carries `RecordedHubResolution` state. `redact_database_url` and `serialize_redacted_database_url` strip credentials from DSNs before logging or serializing.

### Graph Analytics, Search, and Content Indexing

`PreparedGraph` runs in-process analytics over FalkorDB results: betweenness centrality, bridge-node detection (`BridgeSearch`), community detection via a Leiden algorithm implementation (`LeidenGraph`, `Partition`, `detect_communities`, `local_moving`, `refine_partition`, `aggregate_graph`), god-node discovery, and hotspot ranking. Search results from Postgres BM25 (`bm25_score_expr`, `sanitize_pg_search_query`) and Qdrant are merged with `rrf_merge` (Reciprocal Rank Fusion) into `SearchResult` / `SourceExplanation`. The indexing pipeline is built around `Chunk` / `ChunkIdentity` (path + byte-range identity), `content_hash` / `file_content_hash` (SHA-256), and `index_events_from_hashes` which classifies incremental add/update/delete events. `WalkerSettings` provides consumer-extensible file discovery with generic discovery rules.

### CLI Contract and Core Error Types

`CliContract` declares the machine-readable shape of CLI commands through `CommandContract`, `FlagContract`, `PositionalContract`, `ScopeContract`, and `DegradationContract`. These serialize to a golden-page JSON format consumed by documentation and shell-completion tooling. `CoreError`, `ServiceState`, `SetupIssue`, `Guidance`, and `ModalityDegradationReason` form the shared error and status vocabulary surfaced to all callers.

| Symbol | Kind | Purpose |
|---|---|---|
| `CoreError` | type | Top-level serializable error with structured guidance |
| `ServiceState` | type | `is_available` predicate for backing-service health |
| `ModalityDegradationReason` | type | `as_str` / serde name for degradation reporting |
| `DegradationKind` | type | Classification of capability degradation severity |
| `SetupIssue` / `Guidance` | class | Structured remediation hints attached to setup errors |
| `ValidationContext` / `ValidationReport` | class | Non-destructive schema validation lifecycle |
| `RuntimeValidator` | class | `required_objects` and mutable-context query hook |
[crates/gcore/src/graph_analytics/leiden.rs:32-40]
[crates/gcore/src/ai/daemon/operations.rs:20-72]
[crates/gcore/src/ai/daemon/transport.rs:8-12]
[crates/gcore/src/ai/daemon/types.rs:4-9]
[crates/gcore/src/cli_contract.rs:4-12]

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gcore/assets\|crates/gcore/assets]] | ## Module: crates/gcore/assets |
| [[code/modules/crates/gcore/src\|crates/gcore/src]] | ## crates/gcore/src |

