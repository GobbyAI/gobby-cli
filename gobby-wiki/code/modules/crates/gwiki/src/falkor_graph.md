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

`crates/gwiki/src/falkor_graph` builds and consumes FalkorDB-backed graph data for wiki search. It loads wiki documents, links, and sources from PostgreSQL into `WikiGraphFacts`, resolving internal link targets while preserving unresolved wiki targets and skipping external URLs (`wiki_facts.rs:12-63`, `tests.rs:24-73`). It also loads graph boost data from FalkorDB, querying scoped or global `WikiDoc` nodes and links with caps that report partial degradation when limits are exceeded (`boost.rs:10-60`).

The code-edge path connects wiki documents back to the shared code graph. `load_code_graph_edges` opens `GraphClient` against `CODE_GRAPH_NAME`, maps wiki document paths to code source paths, queries call/import edges, tracks per-component truncation, and enforces `MAX_TOTAL_CODE_EDGES` (`code_edges.rs:1-70`). Shared query helpers such as `optional_row_string`, `optional_row_usize`, and `scope_params` centralize row decoding and scoped parameters across boost and code-edge queries (`code_edges.rs:13-17`, `boost.rs:8-9`, `tests.rs:17`).

Collaboration points are split across storage and search boundaries: `wiki_facts.rs` imports PostgreSQL `Client`, `SearchScope`, graph fact types, and text `slugify`; `boost.rs` consumes `gobby_core::falkor::GraphClient` and returns `GraphBoostData` for search boosting; `code_edges.rs` imports `SharedCodeGraphLimits` plus graph edge/document types and emits `SharedCodeGraphEdges` with truncation metadata (`wiki_facts.rs:1-11`, `boost.rs:3-9`, `code_edges.rs:1-18`). The test module exercises the integration surface, asserting graph ownership, target resolution behavior, query builders, truncation helpers, and constants such as `FALKORDB_GRAPH_NAME` and `MAX_TOTAL_CODE_EDGES` (`tests.rs:1-22`).

| Fact | Value / Symbols | Citation |
| --- | --- | --- |
| FalkorDB wiki graph name | `FALKORDB_GRAPH_NAME == "gobby_wiki"` and not `"gobby_code"` | `tests.rs:24-28` |
| Code graph client | `GraphClient::from_config(config, CODE_GRAPH_NAME)` | `code_edges.rs:24-25` |
| Wiki fact loader | `load_wiki_graph_facts(conn, scope)` | `wiki_facts.rs:12-19` |
| Boost loader | `load_graph_boost_data(client, scope, document_limit, link_limit)` | `boost.rs:10-18` |
| Code edge loader | `load_code_graph_edges(config, project_id, documents, limits)` | `code_edges.rs:20-27` |

| Public/internal symbols visible in supplied excerpts | Module |
| --- | --- |
| `load_graph_boost_data`, `partial_graph_degradation` | `boost.rs` |
| `load_code_graph_edges`, `code_doc_source_path`, `remaining_code_edge_limit`, `record_code_edge_truncation`, `truncation_component` | `code_edges.rs` |
| `scope_params`, `optional_row_string`, `optional_row_usize`, `row_string` | `query.rs` |
| `load_wiki_graph_facts`, `resolve_graph_target`, `slug_target_map` | `wiki_facts.rs` |
[crates/gwiki/src/falkor_graph/code_edges.rs:18-21]
[crates/gwiki/src/falkor_graph/wiki_facts.rs:13-98]
[crates/gwiki/src/falkor_graph/boost.rs:11-35]
[crates/gwiki/src/falkor_graph/query.rs:8-23]
[crates/gwiki/src/falkor_graph/tests.rs:27-30]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gwiki/src/falkor_graph/boost.rs\|crates/gwiki/src/falkor_graph/boost.rs]] | `crates/gwiki/src/falkor_graph/boost.rs` exposes 6 indexed API symbols. |
| [[code/files/crates/gwiki/src/falkor_graph/code_edges.rs\|crates/gwiki/src/falkor_graph/code_edges.rs]] | `crates/gwiki/src/falkor_graph/code_edges.rs` exposes 15 indexed API symbols. |
| [[code/files/crates/gwiki/src/falkor_graph/query.rs\|crates/gwiki/src/falkor_graph/query.rs]] | `crates/gwiki/src/falkor_graph/query.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gwiki/src/falkor_graph/sync.rs\|crates/gwiki/src/falkor_graph/sync.rs]] | `crates/gwiki/src/falkor_graph/sync.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gwiki/src/falkor_graph/tests.rs\|crates/gwiki/src/falkor_graph/tests.rs]] | `crates/gwiki/src/falkor_graph/tests.rs` exposes 14 indexed API symbols. |
| [[code/files/crates/gwiki/src/falkor_graph/wiki_facts.rs\|crates/gwiki/src/falkor_graph/wiki_facts.rs]] | `crates/gwiki/src/falkor_graph/wiki_facts.rs` exposes 7 indexed API symbols. |

