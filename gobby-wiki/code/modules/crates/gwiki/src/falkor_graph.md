---
title: crates/gwiki/src/falkor_graph
type: code_module
provenance:
- file: crates/gwiki/src/falkor_graph/boost.rs
- file: crates/gwiki/src/falkor_graph/code_edges.rs
- file: crates/gwiki/src/falkor_graph/query.rs
- file: crates/gwiki/src/falkor_graph/sync.rs
- file: crates/gwiki/src/falkor_graph/tests.rs
- file: crates/gwiki/src/falkor_graph/wiki_facts.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/falkor_graph

Parent: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

## crates/gwiki/src/falkor_graph

The `falkor_graph` module is the bridge between the gwiki crate and FalkorDB, Gobby's property-graph store. It owns three distinct concerns: loading wiki graph boost data to enhance search ranking, synchronising authoritative wiki facts from PostgreSQL into the FalkorDB wiki graph (`gobby_wiki`), and enriching wiki documents with code-graph edges drawn from a separate FalkorDB graph (`gobby_code`). The module maintains its own graph-name constant (`FALKORDB_GRAPH_NAME = "gobby_wiki"`, tests.rs:27) distinct from the code graph, and enforces a hard ceiling of `MAX_TOTAL_CODE_EDGES` across all edge types to keep response sizes predictable (code_edges.rs:44–48).

`wiki_facts.rs` drives the sync pipeline. It issues two PostgreSQL queries against `gwiki_documents` and `gwiki_links` (wiki_facts.rs:20–70), reconstructs `WikiGraphDocument`, `WikiGraphLink`, and `WikiGraphSource` values, and resolves every raw link target to either a `WikiGraphLinkTarget::Resolved` path or a `WikiGraphLinkTarget::Unresolved` string — filtering out external URLs entirely (tests.rs:44–70). The resulting `WikiGraphFacts` struct is passed upstream, where `sync.rs` (4 symbols) converts it into FalkorDB write statements via `graph_write_statements` from `crate::graph`. `boost.rs` runs the complementary read path: it queries `WikiDoc` nodes and link relationships from FalkorDB using scope-aware Cypher (global vs. scoped), applies document and link limits, and returns a `GraphBoostData` payload that includes an optional `DegradationKind` warning when results are capped (boost.rs:15–34).

`code_edges.rs` adds cross-language context to wiki pages. For every wiki document whose path maps to a source file, it issues two parameterised Cypher queries — one for call edges (`code_call_edges_query`) and one for import edges (`code_import_edges_query`) — against the `CODE_GRAPH_NAME` graph via `GraphClient::from_config` (code_edges.rs:22–27). Remaining-edge budgets are tracked per document, and three distinct truncation components are recorded when limits are reached, enabling downstream consumers to surface precise degradation messages.

`query.rs` provides shared helpers (`optional_row_string`, `optional_row_usize`, `scope_params`) used by both `boost.rs` and `code_edges.rs` to build scope-keyed parameter maps and safely extract typed values from graph rows. The full test surface lives in `tests.rs`, which directly imports internal helpers from every sibling file to assert on slug resolution, query parameter generation, truncation arithmetic, and Cypher query string correctness.

### Public / Internal API surface

| File | Key Symbols |
|---|---|
| boost.rs | `load_graph_boost_data`, `partial_graph_degradation`, `GraphBoostData`, `LimitedQuery` |
| code_edges.rs | `load_code_graph_edges`, `code_call_edges_query`, `code_import_edges_query`, `code_edge_query_params`, `code_doc_source_path`, `truncate_to_limit`, `truncation_component`, `record_code_edge_truncation`, `remaining_code_edge_limit`, `SharedCodeGraphEdges`, `SharedCodeGraphTruncation` |
| query.rs | `optional_row_string`, `optional_row_usize`, `scope_params` |
| sync.rs | 4 symbols (sync entrypoint and helpers) |
| wiki_facts.rs | `load_wiki_graph_facts`, `slug_target_map`, `resolve_graph_target` |

### Module-level constants

| Constant | Value / Purpose |
|---|---|
| `FALKORDB_GRAPH_NAME` | `"gobby_wiki"` — wiki-owned graph (tests.rs:27) |
| `CODE_GRAPH_NAME` | `"gobby_code"` — sourced from `gobby_core::config` (code_edges.rs:4) |
| `MAX_TOTAL_CODE_EDGES` | Hard ceiling on combined call + import edges per request (code_edges.rs:44) |
| `CODE_CALL_EDGE_TRUNCATION_COMPONENT` | Truncation label for call-edge cap (code_edges.rs:12) |
| `CODE_IMPORT_EDGE_TRUNCATION_COMPONENT` | Truncation label for import-edge cap (code_edges.rs:13) |
| `CODE_TOTAL_EDGE_TRUNCATION_COMPONENT` | Truncation label for global edge cap (code_edges.rs:14) |
| `CODE_GRAPH_PROVENANCE` | Provenance tag attached to code-derived edges (code_edges.rs:11) |

### Cross-module collaboration

| Direction | Counterpart | Purpose |
|---|---|---|
| Imports from | `gobby_core::falkor::GraphClient` | FalkorDB connection and query execution |
| Imports from | `gobby_core::config::{FalkorConfig, CODE_GRAPH_NAME}` | Connection config and graph name (code_edges.rs:4) |
| Imports from | `postgres::Client` | PostgreSQL reads in wiki_facts.rs (wiki_facts.rs:4) |
| Imports from | `crate::graph` | `WikiGraphDocument`, `WikiGraphFacts`, `WikiGraphCodeEdge`, write-statement builder (code_edges.rs:7–8) |
| Imports from | `crate::search::{SearchScope, SearchError}` | Scope-keyed queries and error type (boost.rs:6) |
| Imports from | `crate::support::config::SharedCodeGraphLimits` | Per-edge-type limits injected at call time (code_edges.rs:8) |
| Exports to | `crate::search` callers | `GraphBoostData` for search ranking signals |
| Exports to | sync callers | `WikiGraphFacts` and `SharedCodeGraphEdges` for FalkorDB write path |
[crates/gwiki/src/falkor_graph/code_edges.rs:18-21]
[crates/gwiki/src/falkor_graph/wiki_facts.rs:13-98]
[crates/gwiki/src/falkor_graph/boost.rs:11-35]
[crates/gwiki/src/falkor_graph/query.rs:8-23]
[crates/gwiki/src/falkor_graph/sync.rs:13-29]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/src/falkor_graph/boost.rs\|crates/gwiki/src/falkor_graph/boost.rs]] | `crates/gwiki/src/falkor_graph/boost.rs` exposes 6 indexed API symbols. |
| [[code/files/crates/gwiki/src/falkor_graph/code_edges.rs\|crates/gwiki/src/falkor_graph/code_edges.rs]] | `crates/gwiki/src/falkor_graph/code_edges.rs` exposes 15 indexed API symbols. |
| [[code/files/crates/gwiki/src/falkor_graph/query.rs\|crates/gwiki/src/falkor_graph/query.rs]] | `crates/gwiki/src/falkor_graph/query.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gwiki/src/falkor_graph/sync.rs\|crates/gwiki/src/falkor_graph/sync.rs]] | `crates/gwiki/src/falkor_graph/sync.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gwiki/src/falkor_graph/tests.rs\|crates/gwiki/src/falkor_graph/tests.rs]] | `crates/gwiki/src/falkor_graph/tests.rs` exposes 14 indexed API symbols. |
| [[code/files/crates/gwiki/src/falkor_graph/wiki_facts.rs\|crates/gwiki/src/falkor_graph/wiki_facts.rs]] | `crates/gwiki/src/falkor_graph/wiki_facts.rs` exposes 7 indexed API symbols. |

