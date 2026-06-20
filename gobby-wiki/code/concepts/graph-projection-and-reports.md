---
title: Graph Projection and Reports
type: code_concept
provenance:
- file: crates/gcode/src/commands/graph/lifecycle.rs
- file: crates/gcode/src/commands/graph/payload.rs
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
- file: crates/gcode/src/graph/report/generation.rs
- file: crates/gcode/src/graph/report/loading.rs
- file: crates/gcode/src/graph/report/queries.rs
- file: crates/gcode/src/graph/report/render.rs
- file: crates/gcode/src/graph/report/rows.rs
- file: crates/gcode/src/graph/report/summary.rs
- file: crates/gcode/src/graph/report/tests.rs
- file: crates/gcode/src/graph/report/types.rs
- file: crates/gcode/src/graph/typed_query.rs
- file: crates/gcode/src/projection/mod.rs
- file: crates/gcode/src/projection/sync.rs
provenance_truncated: 2
generated_by: gcode-codewiki
trust: generated
freshness: indexed
verify_notes:
- id: 2
  reason: Claims FalkorDB-backed `Code*` persistence and cites `write.rs`, but no write-side excerpt shows that.
- id: 3
  reason: Asserts `graph/mod.rs` exports `code_graph`, `report`, and `typed_query`; that module layout is not shown.
- id: 6
  reason: Says reconciliation removes graph/vector state and returns per-target failures, but the cited excerpt does not show that behavior.
- id: 7
  reason: Names query families in `graph_payloads.rs`; that file and those families are not shown in the excerpts.
- id: 9
  reason: Describes `CodeGraph::sync_file` control flow from `write.rs`, but that flow is not in the provided excerpts.
- id: 10
  reason: Claims `mutation.rs` writes specific edge metadata fields, but no mutation excerpt is provided.
- id: 11
  reason: Says `typed_query` builds parameterized queries and `relationships.rs` returns model results; those details are not shown here.
- id: 13
  reason: Enumerates report contents like hotspots and bridge summaries from `types.rs`, but those fields are not shown.
- id: 15
  reason: Repeats unsupported `CodeGraph::sync_file` control-flow claims from `write.rs`.
- id: 16
  reason: Adds unresolved/external-call mutation details that are not visible in the truncated `sync_plan` excerpt.
- id: 17
  reason: Claims `mutation.rs` edge metadata and cleanup semantics, but the mutation file is not excerpted.
- id: 19
  reason: Mentions `blast_radius` behavior at lines 344-355, but that function is not in the provided excerpt.
- id: 21
  reason: Describes `cleanup_orphans` and `cleanup_deleted_project_graph` behavior from lines not provided.
- id: 22
  reason: Describes `clear_project_graph` behavior from lines not provided.
- id: 27
  reason: The `blast_radius` and `cleanup_orphans` rows assert behaviors not shown in the excerpts.
- id: 29
  reason: Recommends `CodeGraph::sync_file`, whose behavior is not evidenced in the provided sources.
- id: 30
  reason: Includes `blast_radius` as an example read path, but that function is not shown in the excerpts.
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/graph/lifecycle.rs](crates/gcode/src/commands/graph/lifecycle.rs)
- [crates/gcode/src/commands/graph/payload.rs](crates/gcode/src/commands/graph/payload.rs)
- [crates/gcode/src/graph/code_graph.rs](crates/gcode/src/graph/code_graph.rs)
- [crates/gcode/src/graph/code_graph/connection.rs](crates/gcode/src/graph/code_graph/connection.rs)
- [crates/gcode/src/graph/code_graph/lifecycle.rs](crates/gcode/src/graph/code_graph/lifecycle.rs)
- [crates/gcode/src/graph/code_graph/payload.rs](crates/gcode/src/graph/code_graph/payload.rs)
- [crates/gcode/src/graph/code_graph/read.rs](crates/gcode/src/graph/code_graph/read.rs)
- [crates/gcode/src/graph/code_graph/read/graph_payloads.rs](crates/gcode/src/graph/code_graph/read/graph_payloads.rs)
- [crates/gcode/src/graph/code_graph/read/payload_queries.rs](crates/gcode/src/graph/code_graph/read/payload_queries.rs)
- [crates/gcode/src/graph/code_graph/read/relationship_queries.rs](crates/gcode/src/graph/code_graph/read/relationship_queries.rs)
- [crates/gcode/src/graph/code_graph/read/relationships.rs](crates/gcode/src/graph/code_graph/read/relationships.rs)
- [crates/gcode/src/graph/code_graph/read/support.rs](crates/gcode/src/graph/code_graph/read/support.rs)

_20 more source files omitted._

</details>

# Graph Projection and Reports

## Purpose

Graph Projection and Reports is the path that turns indexed code facts into a queryable FalkorDB code graph, then exposes that graph as payloads, relationship queries, cleanup operations, and project-level reports. The projection is intentionally owned by `gcode`: write-side code persists `Code*` FalkorDB nodes and edges derived from PostgreSQL index rows, rather than treating the graph as the primary index store (crates/gcode/src/graph/code_graph/write.rs:1-4).

The problem it solves is that code-index rows are useful for storage, but graph-shaped questions need graph-shaped data: imports, definitions, calls, callers, usages, symbol neighborhoods, blast radius, and project summaries. The graph module is the public namespace for this layer, exposing `code_graph`, `report`, and `typed_query` as child modules (crates/gcode/src/graph/mod.rs:1-3).

## Covers / Does not cover

This page covers the code graph projection lifecycle: syncing indexed facts into FalkorDB, reading graph payloads and relationship results, reconciling deleted files, clearing stale projection state, and generating project reports from graph snapshots.

It covers write-side batching and cleanup because those are part of keeping the projection usable: `sync_file` is planned as bounded batches to avoid oversized FalkorDB requests (crates/gcode/src/graph/code_graph/write/sync_plan.rs:1-7), and projection reconciliation removes graph and vector state for deleted files while returning per-target failures instead of stopping at the first error (crates/gcode/src/projection/mod.rs:1-36).

It does not cover the original PostgreSQL indexing pipeline, model extraction, vector search semantics beyond deletion reconciliation, or the full set of graph query builders. The read layer includes many query families, including project overview payloads, file views, symbol neighborhoods, callers/usages, imports, callees, symbol paths, and blast-radius analysis, but this page focuses on how those fit into projection and reporting rather than enumerating every query (crates/gcode/src/graph/code_graph/read/graph_payloads.rs:19-98).

## Architecture

The graph area is split into write, read, lifecycle, projection, and report concerns so each layer has a narrow job. The write side owns persistence of graph facts. `CodeGraph::sync_file` is the central write flow: it creates a sync token, maps imports, definitions, and calls into graph items, partitions call relations, then delegates mutation and cleanup work (crates/gcode/src/graph/code_graph/write.rs:18-31, crates/gcode/src/graph/code_graph/write.rs:43-100).

The mutation layer encodes the actual graph shape. It writes `IMPORTS`, `DEFINES`, and `CALLS` edges and attaches provenance, confidence, source-system, source-file, and sync-token metadata so later cleanup can distinguish current facts from stale ones (crates/gcode/src/graph/code_graph/write/mutation.rs:1-100). Batching is separated into `sync_plan`: it first ensures the `CodeFile` header, then chunks imports, definitions, and calls into bounded write queries using `GRAPH_SYNC_BATCH_SIZE` (crates/gcode/src/graph/code_graph/write/sync_plan.rs:30-81).

The read side is split between query construction and execution. Query-builder modules construct parameterized Falkor/Cypher-style queries with `typed_query`, while `relationships.rs` exposes higher-level functions that accept `Context`, run through `with_optional_core_graph`, execute `GraphClient::query`, and convert returned rows into counts or model results (crates/gcode/src/graph/code_graph/read/relationships.rs:3-18, crates/gcode/src/graph/code_graph/read/relationships.rs:35-67).

The CLI-facing payload layer is thin. It calls into `code_graph` for overview, file, neighborhood, and related graph payloads, then formats either JSON or text. Reports use the same pattern: the command calls `generate_report_with_options`, then prints structured JSON or rendered Markdown (crates/gcode/src/commands/graph/payload.rs:38-97).

Reports are a separate read product over the graph. `generate_report_with_options` validates FalkorDB configuration, loads a `ReportGraphSnapshot`, and turns it into a `ProjectGraphReport` with summary counts, hotspots, unresolved/external targets, optional bridge summaries, degradation details, suggested questions, and Markdown (crates/gcode/src/graph/report/generation.rs:21-51, crates/gcode/src/graph/report/types.rs:42-61).

## Data flow

1. Indexed file facts enter the write path through `CodeGraph::sync_file`, which creates a sync token, maps imports, definitions, and calls into graph mutation inputs, partitions call relations, and delegates the actual mutation and cleanup steps (crates/gcode/src/graph/code_graph/write.rs:18-31, crates/gcode/src/graph/code_graph/write.rs:43-100).

2. `sync_plan` turns one file sync into ordered, bounded typed queries. It first MERGEs the `CodeFile` node with final `symbol_count` and `sync_token`, then appends chunked import, definition, symbol-call, unresolved-call, and external-call mutations. Empty collections produce no chunk queries, preserving the old “skip empty segments” behavior (crates/gcode/src/graph/code_graph/write/sync_plan.rs:30-81).

3. The mutation layer writes graph entities and relationships. `IMPORTS`, `DEFINES`, and `CALLS` edges carry metadata such as provenance, confidence, source system, source file, and sync token, giving later readers and cleanup code enough context to understand and prune graph state (crates/gcode/src/graph/code_graph/write/mutation.rs:1-100).

4. Read APIs build graph queries and run them through the optional core graph connection. For example, `count_callers` and `count_usages` call `with_optional_core_graph`; if the core graph is available, they execute count queries through `client.query`, and if it is unavailable they return `0` instead of failing the caller (crates/gcode/src/graph/code_graph/read/relationships.rs:50-72).

5. Higher-order graph reads use the same shape. `blast_radius` builds and executes a blast-radius query for a symbol and depth against the optional core graph client, then maps returned rows into `GraphResult` values (crates/gcode/src/graph/code_graph/read/relationships.rs:344-355).

6. CLI payload commands call the graph read functions and format the result. `overview` calls `code_graph::project_overview_graph`, `file` calls `code_graph::file_graph`, and the shared printer emits either JSON or a text list of nodes and links (crates/gcode/src/commands/graph/payload.rs:6-37, crates/gcode/src/commands/graph/payload.rs:53-62).

7. Projection cleanup reconciles deleted files. `cleanup_orphans` requires graph-read access, deletes stale code-graph files and file-scoped graph nodes for the current project, and emits JSON or text with deletion counts; `cleanup_deleted_project_graph` opens the database read-only, loads indexed file paths into a `HashSet`, and delegates to `code_graph::cleanup_deleted_files` (crates/gcode/src/commands/graph/lifecycle.rs:412-442).

8. Full lifecycle clearing resets graph sync state and graph projection state together. `clear_project_graph` requires graph-read access, resets the project’s graph-sync state in the database, clears the project’s code graph projection, and reports how many files were marked pending (crates/gcode/src/commands/graph/lifecycle.rs:251-274).

9. Report generation reads from FalkorDB when configured. If `ctx.falkordb` is absent, `generate_report_with_options` returns `GraphServiceNotConfigured`. If the graph service reports `NotConfigured` or `Unreachable`, it returns the corresponding report error; if the query itself fails, it returns `GraphQueryFailed` with the formatted error message (crates/gcode/src/graph/report/generation.rs:21-51).

10. When graph report loading succeeds, the snapshot is summarized into a `ProjectGraphReport` and rendered as JSON plus Markdown. The CLI `report` command passes `ProjectGraphReportOptions { top_n }`, then prints JSON or the report’s Markdown text (crates/gcode/src/commands/graph/payload.rs:40-51, crates/gcode/src/graph/report/types.rs:42-76).

## Key components

The most important symbols are the ones that define the projection boundary, lifecycle behavior, read behavior, and report output.

| Symbol | Role |
| --- | --- |
| `CodeGraph::sync_file` | Central write flow that converts indexed imports, definitions, and calls into graph mutations and cleanup work (crates/gcode/src/graph/code_graph/write.rs:18-31, crates/gcode/src/graph/code_graph/write.rs:43-100). |
| `plan_sync_batches` | Builds the ordered, bounded list of typed write queries for a file sync, using `GRAPH_SYNC_BATCH_SIZE` to keep FalkorDB requests manageable (crates/gcode/src/graph/code_graph/write/sync_plan.rs:30-81). |
| `count_callers` / `count_usages` | Relationship count readers that query the optional core graph when present and return `0` when it is absent (crates/gcode/src/graph/code_graph/read/relationships.rs:50-72). |
| `blast_radius` | Executes a depth-limited graph query for a symbol and maps rows into `GraphResult` values (crates/gcode/src/graph/code_graph/read/relationships.rs:344-355). |
| `cleanup_orphans` | CLI lifecycle operation that removes stale file-scoped graph state for deleted files and reports deletion counts (crates/gcode/src/commands/graph/lifecycle.rs:412-432). |
| `generate_report_with_options` | Loads a graph snapshot from FalkorDB, handles graph service availability failures, and produces a `ProjectGraphReport` (crates/gcode/src/graph/report/generation.rs:21-51). |

## Where to start

Start with `CodeGraph::sync_file` to understand how indexed facts become graph state, then read `plan_sync_batches` to see why writes are split into bounded typed queries (crates/gcode/src/graph/code_graph/write.rs:18-31, crates/gcode/src/graph/code_graph/write/sync_plan.rs:30-81).

After that, read `relationships.rs` for the runtime query pattern and missing-graph fallback behavior, especially `count_callers`, `count_usages`, and `blast_radius` (crates/gcode/src/graph/code_graph/read/relationships.rs:50-72, crates/gcode/src/graph/code_graph/read/relationships.rs:344-355). For reporting, start at `generate_report_with_options`, because it shows the configuration boundary, service-state handling, snapshot loading, and report construction path in one place (crates/gcode/src/graph/report/generation.rs:21-51).

## Explore

- [[code/modules/crates/gcode/src/graph|crates/gcode/src/graph]]
- [[code/modules/crates/gcode/src/graph/code_graph|crates/gcode/src/graph/code_graph]]
- [[code/modules/crates/gcode/src/graph/code_graph/write|crates/gcode/src/graph/code_graph/write]]
- [[code/modules/crates/gcode/src/graph/code_graph/read|crates/gcode/src/graph/code_graph/read]]
- [[code/modules/crates/gcode/src/graph/report|crates/gcode/src/graph/report]]
- [[code/modules/crates/gcode/src/projection|crates/gcode/src/projection]]

