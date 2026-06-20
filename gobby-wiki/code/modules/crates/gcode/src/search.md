---
title: crates/gcode/src/search
type: code_module
provenance:
- file: crates/gcode/src/search/fts.rs
- file: crates/gcode/src/search/fts/common.rs
- file: crates/gcode/src/search/fts/content.rs
- file: crates/gcode/src/search/fts/counts.rs
- file: crates/gcode/src/search/fts/graph.rs
- file: crates/gcode/src/search/fts/symbols.rs
- file: crates/gcode/src/search/fts/tests.rs
- file: crates/gcode/src/search/graph_boost.rs
- file: crates/gcode/src/search/mod.rs
- file: crates/gcode/src/search/rrf.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/search

Parent: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

The `crates/gcode/src/search` module is the search facade for gcode: it groups pg_search BM25 full-text search, graph-based ranking support, and Reciprocal Rank Fusion under `fts`, `graph_boost`, and `rrf` submodules (`crates/gcode/src/search/mod.rs:1-11`). The FTS layer keeps the legacy module name while executing PostgreSQL `pg_search` BM25 keyword search against Gobby’s PostgreSQL hub (`crates/gcode/src/search/fts.rs:1-4`). Its child modules cover symbols, content, counts, graph-symbol resolution, path/language filtering, snippets, and shared query sanitation via `gobby_core::search::sanitize_pg_search_query` (`crates/gcode/src/search/fts/common.rs:9`).

The main flow is hybrid search composition: callers can combine lexical FTS, semantic vectors, and graph boost, then merge ranked sources with RRF; the module is designed to degrade when semantic or graph services are unavailable (`crates/gcode/src/search/mod.rs:3-6`). Graph boosting resolves the query to a visible symbol through `fts::search_symbols_exact_first_visible`, scopes graph access through `visibility::context_for_source_project`, and calls `code_graph::find_caller_ids` / `find_usage_ids` to produce related symbol IDs for ranking (`crates/gcode/src/search/graph_boost.rs:24-39`). Graph expansion similarly starts from seed result IDs and returns deduplicated neighbors, ranking callees before callers for conceptual queries (`crates/gcode/src/search/graph_boost.rs:42-60`).

Collaboration points are explicit: `graph_boost` imports `crate::config::Context`, `crate::graph::code_graph`, `crate::search::fts`, and `crate::visibility` (`crates/gcode/src/search/graph_boost.rs:8-12`), while `rrf::merge` delegates the actual fusion implementation to `gobby_core::search::rrf_merge` and adapts its result shape (`crates/gcode/src/search/rrf.rs:12-16`). When FalkorDB or a PostgreSQL connection is absent, graph helpers return empty lists so upstream hybrid callers can still return lexical results (`crates/gcode/src/search/graph_boost.rs:16-30`).

| Public surface | Purpose | Anchor |
| --- | --- | --- |
| `fts` module | Re-exports BM25 symbol/content search, counts, graph-symbol resolution, path helpers, and visible-search outcomes | `crates/gcode/src/search/fts.rs:12-22` |
| `graph_boost` | Finds graph-related symbol IDs for boosting and expands neighborhoods from seed IDs | `crates/gcode/src/search/graph_boost.rs:14-60` |
| `rrf::MergedResult` | Tuple shape for fused results: symbol id, score, source names | `crates/gcode/src/search/rrf.rs:7-8` |
| `rrf::merge` | Merges ranked source lists using Reciprocal Rank Fusion | `crates/gcode/src/search/rrf.rs:10-16` |

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gcode/src/search/fts\|crates/gcode/src/search/fts]] | The `crates/gcode/src/search/fts` module implements pg_search-backed full-text search for symbols and content, plus count helpers, path/language filters, graph-symbol resolution, and shared SQL parameter plumbing. `common.rs` centralizes query sanitation through `gobby_core::search::sanitize_pg_search_query` so gcode and gwiki escape BM25 DSL consistently, and wraps pg_search row scoring via trusted local SQL aliases (`TrustedRowId`, `bm25_score_expr`) (crates/gcode/src/search/fts/common.rs:9). |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/search/fts.rs\|crates/gcode/src/search/fts.rs]] | `crates/gcode/src/search/fts.rs` has no indexed API symbols. |
| [[code/files/crates/gcode/src/search/graph_boost.rs\|crates/gcode/src/search/graph_boost.rs]] | `crates/gcode/src/search/graph_boost.rs` exposes 9 indexed API symbols. |
| [[code/files/crates/gcode/src/search/mod.rs\|crates/gcode/src/search/mod.rs]] | `crates/gcode/src/search/mod.rs` has no indexed API symbols. |
| [[code/files/crates/gcode/src/search/rrf.rs\|crates/gcode/src/search/rrf.rs]] | `crates/gcode/src/search/rrf.rs` exposes 9 indexed API symbols. |

