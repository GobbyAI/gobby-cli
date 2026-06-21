---
title: crates/gcode/src/graph/code_graph/read
type: code_module
provenance:
- file: crates/gcode/src/graph/code_graph/read/graph_payloads.rs
- file: crates/gcode/src/graph/code_graph/read/payload_queries.rs
- file: crates/gcode/src/graph/code_graph/read/relationship_queries.rs
- file: crates/gcode/src/graph/code_graph/read/relationships.rs
- file: crates/gcode/src/graph/code_graph/read/support.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/code_graph/read

Parent: [[code/modules/crates/gcode/src/graph/code_graph|crates/gcode/src/graph/code_graph]]

## Overview

## crates/gcode/src/graph/code_graph/read

This module is the read-side of the code graph subsystem, responsible for translating high-level requests about code structure into parameterized Cypher queries, executing those queries against the FalkorDB graph database, and converting raw rows into typed domain models such as `GraphResult` and `GraphPathStep`. It is organised as a strict three-layer stack: `support.rs` supplies shared string constants and row-mapping utilities; `payload_queries.rs` and `relationship_queries.rs` build parameterized Cypher strings without touching the database; and `graph_payloads.rs` and `relationships.rs` form the public API that drives actual graph I/O through `with_optional_core_graph` from the sibling `connection` module (relationships.rs:7).

`relationships.rs` exports the primary callable surface for the rest of the crate. It handles caller/callee counting and retrieval (including batched variants), import discovery, external-call-target resolution, blast-radius computation, and shortest-symbol-path reconstruction (relationships.rs:1–100). Every function opens a graph connection through `gobby_core::falkor::GraphClient`, delegates query construction to the matching `*_query` function in `relationship_queries.rs`, and maps result rows with helpers from `support.rs`. `graph_payloads.rs` follows the same pattern for the four overview-style graph projections (`project_overview_graph`, `file_graph`, `symbol_neighbors`, `blast_radius_graph`), each assembling multiple sub-queries from `payload_queries.rs`. `support.rs` keeps shared Cypher fragments that are embedded literally into query strings via Rust's `format!` macro, so all queries share consistent predicate and return-column conventions (support.rs:1–100).

The module imports `crate::config::Context` for project identity, `crate::graph::typed_query` for parameter encoding helpers (e.g. `string_params`, `id_list_literal`), and `crate::models::{GraphResult, GraphPathStep, ProjectionProvenance}` for output types (relationships.rs:3–6; support.rs:4–5). It calls out to `super::super::connection::with_optional_core_graph`, which gracefully returns a default value when no graph is configured, and to `super::super::payload::{row_string_owned, row_usize, row_to_projection_metadata}` for per-field extraction from FalkorDB rows (relationships.rs:7–8; support.rs:7).

### Shared Cypher constants (support.rs:8–40)

| Constant | Purpose |
| --- | --- |
| `CALL_TARGET_PREDICATE` | WHERE clause accepting `CodeSymbol`, `UnresolvedCallee`, or `ExternalSymbol` as call targets |
| `NEIGHBOR_PREDICATE` | Same labels, used in neighbor queries |
| `TARGET_TYPE_CASE` | CASE expression mapping target labels to type strings (`external`, `unresolved`, kind) |
| `NEIGHBOR_TYPE_CASE` | Same as above for neighbor nodes |
| `NODE_TYPE_CASE` | Covers `CodeFile`, `CodeModule`, `CodeSymbol`, `ExternalSymbol` |
| `CONFIDENCE_LABEL_CASE` | Folds collected provenances to `AMBIGUOUS` > `INFERRED` > `EXTRACTED` |
| `LINK_METADATA_RETURN` | Standard SELECT clause for edge metadata (provenance, confidence, source system, file/line/symbol) |
| `MAX_GRAPH_LIMIT` | Hard ceiling of 100 rows per query |

### Public API — relationship queries (relationships.rs)

| Symbol | Description |
| --- | --- |
| `count_callers(ctx, symbol_id)` | Count distinct callers of a symbol |
| `count_usages(ctx, symbol_id)` | Count CALLS-edge usages of a symbol |
| `find_callers(ctx, symbol_id, offset, limit)` | Paginated caller list with confidence label |
| `find_usages(ctx, symbol_id, offset, limit)` | Paginated usage list |
| `find_caller_ids / find_usage_ids` | Return only IDs for the above |
| `find_callers_batch / find_caller_ids_batch` | Multi-symbol caller lookups |
| `find_callees_batch / find_callee_ids_batch` | Multi-symbol callee lookups |
| `get_imports(ctx, symbol_id)` | Retrieve import edges for a symbol |
| `resolve_external_call_target(ctx, …)` | Resolve an unresolved callee to a `ResolvedExternalCallTarget`; returns ambiguity hints when multiple candidates match |
| `symbol_callee_edges(ctx, symbol_id)` | Raw callee edge list for a symbol |
| `symbol_path_steps / reconstruct_symbol_path / shortest_symbol_path` | Shortest-path traversal up to `MAX_SYMBOL_PATH_DEPTH` (16) hops, default 8 |
| `blast_radius(ctx, symbol_id, …)` | Compute the blast-radius subgraph for a symbol |

### Public API — graph payloads (graph_payloads.rs)

| Symbol | Description |
| --- | --- |
| `project_overview_graph` | Multi-query snapshot of files, imports, defines, and calls for a project |
| `file_graph` | File-scoped symbols and call edges |
| `symbol_neighbors` | Immediate call/import neighbours of a symbol |
| `blast_radius_graph` | Subgraph centred on a symbol showing its downstream impact |
[crates/gcode/src/graph/code_graph/read/payload_queries.rs:10-29]
[crates/gcode/src/graph/code_graph/read/relationship_queries.rs:9-21]
[crates/gcode/src/graph/code_graph/read/graph_payloads.rs:19-98]
[crates/gcode/src/graph/code_graph/read/relationships.rs:24-27]
[crates/gcode/src/graph/code_graph/read/support.rs:43-94]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/graph/code_graph/read/graph_payloads.rs\|crates/gcode/src/graph/code_graph/read/graph_payloads.rs]] | `crates/gcode/src/graph/code_graph/read/graph_payloads.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gcode/src/graph/code_graph/read/payload_queries.rs\|crates/gcode/src/graph/code_graph/read/payload_queries.rs]] | `crates/gcode/src/graph/code_graph/read/payload_queries.rs` exposes 10 indexed API symbols. |
| [[code/files/crates/gcode/src/graph/code_graph/read/relationship_queries.rs\|crates/gcode/src/graph/code_graph/read/relationship_queries.rs]] | `crates/gcode/src/graph/code_graph/read/relationship_queries.rs` exposes 18 indexed API symbols. |
| [[code/files/crates/gcode/src/graph/code_graph/read/relationships.rs\|crates/gcode/src/graph/code_graph/read/relationships.rs]] | `crates/gcode/src/graph/code_graph/read/relationships.rs` exposes 24 indexed API symbols. |
| [[code/files/crates/gcode/src/graph/code_graph/read/support.rs\|crates/gcode/src/graph/code_graph/read/support.rs]] | `crates/gcode/src/graph/code_graph/read/support.rs` exposes 7 indexed API symbols. |

