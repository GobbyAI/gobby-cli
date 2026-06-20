---
title: crates/gcode/src/graph/code_graph
type: code_module
provenance:
- file: crates/gcode/src/graph/code_graph/connection.rs
- file: crates/gcode/src/graph/code_graph/lifecycle.rs
- file: crates/gcode/src/graph/code_graph/payload.rs
- file: crates/gcode/src/graph/code_graph/read.rs
- file: crates/gcode/src/graph/code_graph/read/graph_payloads.rs
- file: crates/gcode/src/graph/code_graph/read/payload_queries.rs
- file: crates/gcode/src/graph/code_graph/read/relationship_queries.rs
- file: crates/gcode/src/graph/code_graph/read/relationships.rs
- file: crates/gcode/src/graph/code_graph/read/support.rs
- file: crates/gcode/src/graph/code_graph/tests.rs
- file: crates/gcode/src/graph/code_graph/write.rs
- file: crates/gcode/src/graph/code_graph/write/deletion.rs
- file: crates/gcode/src/graph/code_graph/write/mutation.rs
- file: crates/gcode/src/graph/code_graph/write/support.rs
- file: crates/gcode/src/graph/code_graph/write/sync_plan.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/code_graph

Parent: [[code/modules/crates/gcode/src/graph|crates/gcode/src/graph]]

## Overview

The `code_graph` module owns the code-index graph projection: write-side code persists `Code*` FalkorDB nodes and edges derived from PostgreSQL index rows, intentionally making this projection a `gcode`-owned store (`crates/gcode/src/graph/code_graph/write.rs:1-4`). Its write path centers on `CodeGraph::sync_file`, which creates a sync token, maps imports, definitions, and calls into graph items, partitions call relations, and delegates mutations/cleanup through `mutation`, `deletion`, `support`, and `sync_plan` helpers (`crates/gcode/src/graph/code_graph/write.rs:18-31`, `crates/gcode/src/graph/code_graph/write.rs:43-100`). The write child module encodes `IMPORTS`, `DEFINES`, and `CALLS` with provenance, confidence, source-system, source-file, and sync-token metadata (`crates/gcode/src/graph/code_graph/write/mutation.rs:1-100`).

The read side is the query and payload layer. It builds typed Falkor/Cypher-style queries for overview graphs, file graphs, symbol neighborhoods, callers/usages, imports, callees, symbol paths, and blast-radius analysis, then executes them through `with_optional_core_graph` and `GraphClient::query` before converting rows into counts or model results (`relationships.rs:3-18`, `relationships.rs:35-67`). `GraphPayload` deduplicates nodes, stores links, optionally tracks a center node, and can convert node/link parts into `AnalyticsGraph` objects with weighted analytics edges (`crates/gcode/src/graph/code_graph/payload.rs:1-100`). Tests assert that read APIs return node/link JSON with edge metadata and that projection metadata stays tied to metadata source paths (`crates/gcode/src/graph/code_graph/tests.rs:23-66`).

Lifecycle support connects CLI-facing graph operations to daemon HTTP endpoints. `GraphLifecycleAction` maps `Clear` and `Rebuild` to CLI command text, daemon endpoint paths, and success-message prefixes (`crates/gcode/src/graph/code_graph/lifecycle.rs:15-38`). `GraphLifecycleRequest::from_context` pulls `project_id` and `daemon_url` from `Context`, while lifecycle timeouts are configured from environment variables with defaults (`crates/gcode/src/graph/code_graph/lifecycle.rs:43-80`). Collaboration-wise, this module imports project configuration, graph clients, model relations, degradation/service state, and JSON/serde types, then calls out to FalkorDB and daemon HTTP APIs (`crates/gcode/src/graph/code_graph/write.rs:5-17`, `crates/gcode/src/graph/code_graph/lifecycle.rs:1-11`).

| Lifecycle action | CLI command | Endpoint | Success prefix |
| --- | --- | --- | --- |
| `Clear` | `gcode graph clear` | `/api/code-index/graph/clear` | `Cleared code-index graph` |
| `Rebuild` | `gcode graph rebuild` | `/api/code-index/graph/rebuild` | `Rebuilt code-index graph` |

| Environment variable | Purpose | Default |
| --- | --- | --- |
| `GCODE_GRAPH_CLEAR_TIMEOUT_SECS` | Clear request timeout | `15` seconds |
| `GCODE_GRAPH_REBUILD_TIMEOUT_SECS` | Rebuild request timeout | `120` seconds |

| Public surface | Responsibility |
| --- | --- |
| `CodeGraph::sync_file` | Sync one file’s imports, definitions, calls, and optional orphan cleanup |
| `GraphPayload` / `GraphNode` / `GraphLink` | Serializable graph read payloads |
| `project_overview_graph`, `file_graph`, `symbol_neighbors`, `blast_radius_graph` | High-level graph payload reads |
| `count_callers`, `find_usages`, `find_callees_batch`, `shortest_symbol_path`, `blast_radius` | Relationship and impact-analysis reads |
| `GraphLifecycleAction`, `GraphLifecycleRequest`, `run_lifecycle_action` | CLI/daemon lifecycle integration |
[crates/gcode/src/graph/code_graph/read/payload_queries.rs:10-29]
[crates/gcode/src/graph/code_graph/read/relationship_queries.rs:9-21]
[crates/gcode/src/graph/code_graph/write/sync_plan.rs:30-81]
[crates/gcode/src/graph/code_graph/read/graph_payloads.rs:19-98]
[crates/gcode/src/graph/code_graph/read/relationships.rs:24-27]

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gcode/src/graph/code_graph/read\|crates/gcode/src/graph/code_graph/read]] | `crates/gcode/src/graph/code_graph/read` is the read-side query layer for the code graph. It builds Falkor/Cypher-style graph queries for project overview payloads, file views, symbol neighborhoods, callers/usages, imports, callees, symbol paths, and blast-radius analysis. The module is split between query-string builders and execution helpers: `relationship_queries.rs` and `payload_queries.rs` construct parameterized queries with `typed_query`, while `relationships.rs` exposes higher-level functions that accept `Context`, run through `with_optional_core_graph`, call `GraphClient::query`, and… |
| [[code/modules/crates/gcode/src/graph/code_graph/write\|crates/gcode/src/graph/code_graph/write]] | This module owns write-side code graph persistence: it builds typed Falkor/Cypher mutations for files, symbols, imports, and calls, plus cleanup queries for stale graph state. The mutation layer imports typed query primitives and model types such as `Symbol`, `ImportRelation`, `CallRelation`, unresolved callees, and external symbol IDs, then encodes `IMPORTS`, `DEFINES`, and `CALLS` graph writes with provenance, confidence, source-system, source-file, and sync-token metadata (`crates/gcode/src/graph/code_graph/write/mutation.rs:1-100`). |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/graph/code_graph/connection.rs\|crates/gcode/src/graph/code_graph/connection.rs]] | `crates/gcode/src/graph/code_graph/connection.rs` exposes 3 indexed API symbols. |
| [[code/files/crates/gcode/src/graph/code_graph/lifecycle.rs\|crates/gcode/src/graph/code_graph/lifecycle.rs]] | `crates/gcode/src/graph/code_graph/lifecycle.rs` exposes 22 indexed API symbols. |
| [[code/files/crates/gcode/src/graph/code_graph/payload.rs\|crates/gcode/src/graph/code_graph/payload.rs]] | `crates/gcode/src/graph/code_graph/payload.rs` exposes 25 indexed API symbols. |
| [[code/files/crates/gcode/src/graph/code_graph/read.rs\|crates/gcode/src/graph/code_graph/read.rs]] | `crates/gcode/src/graph/code_graph/read.rs` has no indexed API symbols. |
| [[code/files/crates/gcode/src/graph/code_graph/tests.rs\|crates/gcode/src/graph/code_graph/tests.rs]] | `crates/gcode/src/graph/code_graph/tests.rs` exposes 22 indexed API symbols. |
| [[code/files/crates/gcode/src/graph/code_graph/write.rs\|crates/gcode/src/graph/code_graph/write.rs]] | `crates/gcode/src/graph/code_graph/write.rs` exposes 27 indexed API symbols. |

