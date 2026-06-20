---
title: crates/gcode/src/graph
type: code_module
provenance:
- file: crates/gcode/src/graph/code_graph.rs
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
- file: crates/gcode/src/graph/mod.rs
- file: crates/gcode/src/graph/report.rs
- file: crates/gcode/src/graph/report/generation.rs
- file: crates/gcode/src/graph/report/loading.rs
- file: crates/gcode/src/graph/report/queries.rs
- file: crates/gcode/src/graph/report/render.rs
- file: crates/gcode/src/graph/report/rows.rs
- file: crates/gcode/src/graph/report/summary.rs
- file: crates/gcode/src/graph/report/tests.rs
- file: crates/gcode/src/graph/report/time.rs
- file: crates/gcode/src/graph/report/types.rs
- file: crates/gcode/src/graph/typed_query.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph

Parent: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

The `crates/gcode/src/graph` module is the public graph namespace for `gcode`, exposing `code_graph`, `report`, and `typed_query` as child modules (`crates/gcode/src/graph/mod.rs:1-3`). `code_graph` owns the code-index graph projection: it persists `Code*` FalkorDB nodes and edges derived from PostgreSQL index rows, making the projection a `gcode`-owned store (`crates/gcode/src/graph/code_graph/write.rs:1-4`). Its central write flow is `CodeGraph::sync_file`, which creates a sync token, maps imports, definitions, and calls into graph items, partitions call relations, then delegates mutation and cleanup work (`crates/gcode/src/graph/code_graph/write.rs:18-31`, `crates/gcode/src/graph/code_graph/write.rs:43-100`). Edges such as `IMPORTS`, `DEFINES`, and `CALLS` carry provenance, confidence, source-system, source-file, and sync-token metadata (`crates/gcode/src/graph/code_graph/write/mutation.rs:1-100`).

The module also provides read, lifecycle, payload, and reporting surfaces. `code_graph.rs` imports internal `connection`, `lifecycle`, `payload`, `read`, and `write` modules, then re-exports daemon lifecycle helpers, graph payload types, graph read APIs, and write/cleanup operations (`crates/gcode/src/graph/code_graph.rs:1-24`). `report.rs` composes report generation from `generation`, `loading`, `queries`, `render`, `rows`, `summary`, `time`, and `types`, then exposes report generation entry points plus the report DTOs (`crates/gcode/src/graph/report.rs:1-16`). Reports can be generated from snapshots or loaded rows, rendered as structured JSON plus Markdown, and summarized through `ProjectGraphReport`, which includes identity, generation time, counts, hotspots, unresolved or external targets, bridge summaries, degradation details, suggested questions, and rendered Markdown (`crates/gcode/src/graph/report/types.rs:42-61`).

`typed_query` is the shared Cypher parameter-rendering layer. It defines `TypedQuery`, `TypedValue`, identifier kinds, and typed errors, serializes query structs with `serde`, validates parameter names, and renders nested values into Cypher-safe string parameters (`crates/gcode/src/graph/typed_query.rs:1-64`). Its value renderer supports nulls, strings, integers, finite floats, booleans, lists, and maps, routing strings through escaped Cypher literals (`crates/gcode/src/graph/typed_query.rs:66-100`).

| Public area | Symbols | Source |
| --- | --- | --- |
| Child modules | `code_graph`, `report`, `typed_query` | `crates/gcode/src/graph/mod.rs:1-3` |
| Code graph lifecycle/read/write API | `GraphLifecycleAction`, `GraphLifecycleOutput`, `GraphLifecycleRequest`, `GraphReadError`, `GraphReadRequest`, `run_lifecycle_action`, read graph functions, `CodeGraph`, cleanup and sync functions | `crates/gcode/src/graph/code_graph.rs:8-24` |
| Graph payload API | `GraphBlastRadiusTarget`, `GraphLink`, `GraphNode`, `GraphPayload`, `extracted_code_edge_metadata` | `crates/gcode/src/graph/code_graph.rs:13-15` |
| Report API | `empty_report`, `generate_report`, `generate_report_with_options`, report summary/types/options/errors | `crates/gcode/src/graph/report.rs:10-16` |
| Typed query API | `TypedQuery`, `TypedValue`, `IdentifierKind`, `TypedQueryError`, `TypedQuery::new`, `with_params`, `insert_param`, `cypher_string_literal`, `render_cypher_value` | `crates/gcode/src/graph/typed_query.rs:6-70` |

| Constant | Purpose | Source |
| --- | --- | --- |
| `RELATES_TO_CODE` | Report bridge/code relationship label | `crates/gcode/src/graph/report.rs:18` |
| `DEFAULT_TOP_LIMIT` | Default report top-N sizing via `ProjectGraphReportOptions` | `crates/gcode/src/graph/report.rs:19`, `crates/gcode/src/graph/report/types.rs:64-76` |

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gcode/src/graph/code_graph\|crates/gcode/src/graph/code_graph]] | The `code_graph` module owns the code-index graph projection: write-side code persists `Code*` FalkorDB nodes and edges derived from PostgreSQL index rows, intentionally making this projection a `gcode`-owned store (`crates/gcode/src/graph/code_graph/write.rs:1-4`). Its write path centers on `CodeGraph::sync_file`, which creates a sync token, maps imports, definitions, and calls into graph items, partitions call relations, and delegates mutations/cleanup through `mutation`, `deletion`, `support`, and `sync_plan` helpers (`crates/gcode/src/graph/code_graph/write.rs:18-31`,… |
| [[code/modules/crates/gcode/src/graph/report\|crates/gcode/src/graph/report]] | `crates/gcode/src/graph/report` builds project graph reports from snapshots or loaded graph rows, then renders the same report as structured JSON plus Markdown. Its core model is `ProjectGraphReport`, which carries project identity, generation time, summary counts, hotspots, unresolved/external targets, optional bridge summaries, degradation details, suggested questions, and rendered Markdown (`crates/gcode/src/graph/report/types.rs:42-61`). Report sizing is controlled by `ProjectGraphReportOptions`, whose default `top_n` comes from `DEFAULT_TOP_LIMIT`… |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/graph/code_graph.rs\|crates/gcode/src/graph/code_graph.rs]] | `crates/gcode/src/graph/code_graph.rs` has no indexed API symbols. |
| [[code/files/crates/gcode/src/graph/mod.rs\|crates/gcode/src/graph/mod.rs]] | `crates/gcode/src/graph/mod.rs` has no indexed API symbols. |
| [[code/files/crates/gcode/src/graph/report.rs\|crates/gcode/src/graph/report.rs]] | `crates/gcode/src/graph/report.rs` has no indexed API symbols. |
| [[code/files/crates/gcode/src/graph/typed_query.rs\|crates/gcode/src/graph/typed_query.rs]] | `crates/gcode/src/graph/typed_query.rs` exposes 25 indexed API symbols. |

