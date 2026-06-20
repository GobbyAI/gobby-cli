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

`crates/gcore/src` is the shared core layer for Gobby Rust crates: it centralizes AI routing/types, configuration resolution, storage clients, indexing/search primitives, graph analytics, setup/degradation contracts, and local provisioning. Configuration stays behind a lightweight shared surface, with service config types for FalkorDB, Qdrant, embeddings, indexing, AI routing, AI capability bindings, tuning, and feature candidates, while consumer-owned choices such as graph and collection names remain outside the shared config layer (`crates/gcore/src/config/mod.rs:1-17`, `crates/gcore/src/config/types.rs:1-30`).

The AI flow is split between config-only context resolution and transport-backed execution. `AiContext` resolves per-capability bindings, tuning, concurrency limits, and optional command-scoped overrides, but intentionally stays transport-free (`crates/gcore/src/ai_context.rs:1-16`, `crates/gcore/src/ai_context.rs:20-58`). The transport layer imports `AiContext`, shared `AiError`/result types, and config bindings, then selects a route per capability: explicit `Off`, `Direct`, and `Daemon` modes are honored, while `Auto` probes daemon availability and falls back to direct config or `Off` (`crates/gcore/src/ai/mod.rs:1-14`, `crates/gcore/src/ai/mod.rs:28-63`). Shared AI wire models normalize outputs for callers across transports, including transcription segments in milliseconds, vision OCR/metadata, text usage, and provider metadata (`crates/gcore/src/ai_types.rs:1-66`).

The module also supplies backend and analysis boundaries. Qdrant owns collection naming and client-facing vector behavior, including scoped project/topic/custom names and validation against blank, reserved, whitespace, control, path-like, and URL-like names (`crates/gcore/src/qdrant/naming.rs:1`, `crates/gcore/src/qdrant/naming.rs:44`). Graph analytics exposes public graph/community analysis while delegating community detection to a deterministic std-only Leiden kernel over dense integer node IDs; the facade adapts external node IDs into that representation (`crates/gcore/src/graph_analytics/leiden.rs:1-7`). Provisioning owns standalone Docker bootstrap by mirroring service assets under `~/.gobby/services`, starting daemon-style profiles, and persisting bootstrap keys in `gcore.yaml` (`crates/gcore/src/provisioning/mod.rs:1-7`, `crates/gcore/src/provisioning/mod.rs:14-52`).

| Public API Area | Representative Symbols | Responsibility |
| --- | --- | --- |
| AI context | `AiContext`, `AiContext::resolve`, `AiContext::resolve_with_options`, `AiContext::binding` | Resolve shared per-capability AI bindings, tuning, limiter, and project identity (`crates/gcore/src/ai_context.rs:20-58`). |
| AI routing | `effective_route`, `effective_route_with_probe` | Collapse configured routing into daemon/direct/off behavior with capability probing (`crates/gcore/src/ai/mod.rs:28-63`). |
| AI results/errors | `TranscriptionResult`, `VisionResult`, `TextResult`, `TokenUsage`, `AiError` | Normalize AI transport outputs and parse failures across transcription, vision, and text generation (`crates/gcore/src/ai_types.rs:1-66`). |
| Graph analytics | `GraphAnalytics`, `AnalyticsGraph`, `Community`, `detect_communities` | Adapt public graph data to deterministic weighted Leiden community detection (`crates/gcore/src/graph_analytics/leiden.rs:1-7`). |
| Provisioning | `StandaloneConfig`, `provision_docker_services`, `ensure_hub` | Manage local service assets, Docker profiles, and persisted bootstrap config (`crates/gcore/src/provisioning/mod.rs:1-7`). |

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gcore/src/ai\|crates/gcore/src/ai]] | The `crates/gcore/src/ai` module centralizes AI routing, transport, and capability-specific clients for text generation, embeddings, transcription, translation, and vision. Its top-level `mod.rs` exposes the child modules, imports `AiContext`, shared result/error types, and config bindings, then defines shared timeout, retry, and backoff policy used by capability flows (crates/gcore/src/ai/mod.rs:1). Route selection is capability-aware: `effective_route` delegates daemon probing to `probe::probe_daemon_capability`, while `Auto` mode uses daemon only when its status endpoint advertises the… |
| [[code/modules/crates/gcore/src/config\|crates/gcore/src/config]] | `crates/gcore/src/config` is the shared configuration-resolution boundary for Gobby Rust crates, keeping lightweight contracts and resolver entry points behind one public module surface (`crates/gcore/src/config/mod.rs:1-17`). It owns common service config types for FalkorDB, Qdrant, embeddings, indexing, AI routing, AI capability bindings, tuning, and feature candidates, while leaving consumer-specific choices such as graph names and collection names outside the shared layer (`crates/gcore/src/config/types.rs:1-30`). |
| [[code/modules/crates/gcore/src/graph_analytics\|crates/gcore/src/graph_analytics]] | `crates/gcore/src/graph_analytics/leiden.rs` implements a std-only, deterministic weighted Leiden community detection kernel over dense integer node indices. It is intentionally decoupled from public `AnalyticsGraph` and `Community` types so the algorithm can be tested in isolation, while the higher-level facade in `graph_analytics.rs` adapts external node IDs and memberships into this integer-index representation (crates/gcore/src/graph_analytics/leiden.rs:1-7). |
| [[code/modules/crates/gcore/src/provisioning\|crates/gcore/src/provisioning]] | `crates/gcore/src/provisioning` owns standalone bootstrap plus local Docker service provisioning: it mirrors daemon service assets, copies them under `~/.gobby/services`, starts daemon-style profiles, and persists bootstrap keys in `gcore.yaml` (`crates/gcore/src/provisioning/mod.rs:1-7`). The module root centralizes service filenames, default database/vector/AI endpoint settings, and embedded Docker/Postgres asset templates (`crates/gcore/src/provisioning/mod.rs:14-52`). |
| [[code/modules/crates/gcore/src/qdrant\|crates/gcore/src/qdrant]] | The `crates/gcore/src/qdrant` module owns Qdrant collection naming plus the client-facing behavior exercised by its tests. Its naming layer defines scoped collection names for project, topic, and caller-supplied custom collections, with namespace prefixes for project/topic scopes and verbatim names for custom scopes ((crates/gcore/src/qdrant/naming.rs:1)). It rejects empty names, reserved path-like names, whitespace-surrounded names, ASCII whitespace/control characters, and path/URL-like separators (`/`, `\`, `:`) before building collection names ((crates/gcore/src/qdrant/naming.rs:44)). |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcore/src/ai/daemon/operations.rs\|crates/gcore/src/ai/daemon/operations.rs]] | `crates/gcore/src/ai/daemon/operations.rs` exposes 5 indexed API symbols. |
| [[code/files/crates/gcore/src/ai/daemon/request.rs\|crates/gcore/src/ai/daemon/request.rs]] | `crates/gcore/src/ai/daemon/request.rs` exposes 8 indexed API symbols. |
| [[code/files/crates/gcore/src/ai/daemon/response.rs\|crates/gcore/src/ai/daemon/response.rs]] | `crates/gcore/src/ai/daemon/response.rs` exposes 3 indexed API symbols. |
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

