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

`crates/gcode/src/graph/code_graph/read` is the read-side query layer for the code graph. It builds Falkor/Cypher-style graph queries for project overview payloads, file views, symbol neighborhoods, callers/usages, imports, callees, symbol paths, and blast-radius analysis. The module is split between query-string builders and execution helpers: `relationship_queries.rs` and `payload_queries.rs` construct parameterized queries with `typed_query`, while `relationships.rs` exposes higher-level functions that accept `Context`, run through `with_optional_core_graph`, call `GraphClient::query`, and convert rows into counts or model results (`relationships.rs:3-18`, `relationships.rs:35-67`).

The key flow is “public read API → query builder → graph client → row conversion.” For example, `count_callers` and `count_usages` build project-scoped queries from `ctx.project_id`, execute them only when the core graph is available, and otherwise return `0` (`relationships.rs:35-67`). Query builders clamp offsets/limits before embedding pagination and return `(String, HashMap<String, String>)` parameter bundles (`relationship_queries.rs:8-58`). Payload graph queries similarly select project files, imports, and definitions, adding relationship metadata where available (`payload_queries.rs:9-68`).

This module collaborates with surrounding graph infrastructure rather than owning storage. It imports `Context`, `typed_query`, `GraphResult`, `GraphPathStep`, payload row helpers, optional graph connection handling, and `gobby_core::falkor::GraphClient` (`relationships.rs:3-18`). Shared support code centralizes graph predicates, node-type cases, confidence-label logic, link metadata projection, the maximum graph limit, and `row_to_graph_result` mapping (`support.rs:6-43`, `support.rs:44-100`). The relationship queries deliberately distinguish “callers” from the broader “usages” command surface even though both currently traverse `CALLS`, leaving room for future imports/references expansion (`relationship_queries.rs:20-36`).

| Public API / Symbol Group | Symbols |
| --- | --- |
| Graph payloads | `project_overview_graph`, `file_graph`, `symbol_neighbors`, `blast_radius_graph` |
| Payload query builders | `project_overview_files_query`, `project_overview_imports_query`, `project_overview_defines_query`, `project_overview_calls_query`, `file_symbols_query`, `file_calls_query`, `symbol_neighbors_query`, `blast_radius_center_query`, `blast_radius_file_call_query`, `blast_radius_file_import_query` |
| Relationship reads | `count_callers`, `count_usages`, `find_callers`, `find_usages`, `find_caller_ids`, `find_usage_ids`, `find_callers_batch`, `find_caller_ids_batch`, `find_callees_batch`, `find_callee_ids_batch`, `get_imports`, `resolve_external_call_target`, `symbol_callee_edges`, `symbol_path_steps`, `reconstruct_symbol_path`, `shortest_symbol_path`, `blast_radius` |
| Support / limits | `row_to_graph_result`, `clamp_limit`, `clamp_offset`, `dedupe_limited_blast_rows`, `count_from_rows`, `MAX_GRAPH_LIMIT` |
| Constants / structs | `DEFAULT_SYMBOL_PATH_MAX_DEPTH`, `MAX_SYMBOL_PATH_DEPTH`, `ResolvedExternalCallTarget` |

| Shared Query Fact | Value / Role | Source |
| --- | --- | --- |
| Call target predicate | Allows `CodeSymbol`, `UnresolvedCallee`, or `ExternalSymbol` targets | `support.rs:6-8` |
| Neighbor predicate | Allows symbol, unresolved, or external neighbor nodes | `support.rs:9-10` |
| Confidence label case | Projects provenance into `AMBIGUOUS`, `INFERRED`, or `EXTRACTED` | `support.rs:20-24` |
| Link metadata return | Returns provenance, confidence, source system/file/line/symbol, and matching method | `support.rs:32-39` |
| Max graph limit | `100` | `support.rs:40` |
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

