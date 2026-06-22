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

## Module: crates/gcode/src/search

This module is the top-level search subsystem for the Gobby code intelligence platform. As declared in `mod.rs:1-8`, it orchestrates three complementary retrieval strategies — full-text search (FTS) via PostgreSQL pg_search BM25, semantic vector search, and a FalkorDB call-graph boost — fusing their ranked outputs with Reciprocal Rank Fusion. The design explicitly supports graceful degradation: hybrid callers fall back to lexical-only results when graph or vector infrastructure is unavailable at query time.

The `fts` submodule (`fts.rs:1-32`) is itself a facade that re-exports from six internal child modules (`common`, `content`, `counts`, `graph`, `symbols`, `tests`). Its public surface covers symbol lookup by name, exact-first and BM25 ordering, content search with snippet generation, count queries, and graph-symbol resolution. The `graph_boost` submodule (`graph_boost.rs:1-100`) consults FalkorDB to expand a query into a set of related symbol IDs: `graph_boost` resolves the query string to a concrete symbol via `fts::search_symbols_exact_first_visible`, then fetches up to ten callers and ten usages from `code_graph::find_caller_ids` / `find_usage_ids` (`graph_boost.rs:35-45`). The companion `graph_expand` function takes seed IDs from prior FTS/semantic results and expands their call neighbourhood, with callees ranked ahead of callers because they surface implementation details. Both helpers return an empty list — never an error — when FalkorDB is absent (`graph_boost.rs:22-27`).

The `rrf` submodule (`rrf.rs:1-20`) provides the final merge step. It wraps `gobby_core::search::rrf_merge`, mapping each result to the `MergedResult` triple `(symbol_id, combined_score, source_names)`. Score is computed as `1.0 / (K + rank)` with K = 60, sources are sorted deterministically, and a symbol appearing in multiple lists accumulates contributions from each (`rrf.rs:43-49`).

### Public API — graph_boost

| Symbol | Kind | Description |
|---|---|---|
| `graph_boost` | `fn(ctx, conn, query) -> Vec<String>` | Callers + usages of the resolved query symbol; empty when FalkorDB absent |
| `graph_expand` | `fn(ctx, conn, seed_ids) -> Vec<String>` | Callees then callers for a set of seed IDs, deduplicated |
| `graph_expand_grouped` | `fn(…) -> …` | Expands per project scope and deduplicates across scopes |

### Public API — rrf

| Symbol | Kind | Description |
|---|---|---|
| `MergedResult` | `type` | `(String, f64, Vec<String>)` — id, RRF score, contributing source names |
| `merge` | `fn(Vec<(&str, Vec<String>)>) -> Vec<MergedResult>` | Fuses ranked lists; delegates to `gobby_core::search::rrf_merge` (`rrf.rs:15-20`) |

### Public API — fts (re-exports)

| Symbol | Origin child | Purpose |
|---|---|---|
| `search_symbols_fts` / `_visible` | `symbols` | BM25 symbol search, optional project/file filters |
| `search_symbols_by_name` / `_visible` | `symbols` | Name-based symbol lookup |
| `search_symbols_exact_first` / `_visible` | `symbols` | Exact match prioritised over BM25 |
| `search_text` / `_visible` | `symbols` | Full-text search over symbol text |
| `search_content` / `_visible` | `content` | BM25 content search with snippet generation |
| `count_content` / `_visible`, `count_text` / `_visible` | `counts` | Result-count queries for pagination |
| `resolve_graph_symbol`, `resolve_graph_symbol_by_id` | `graph` | Resolve a symbol row to a `ResolvedGraphSymbol` |
| `compile_patterns`, `expand_paths`, `sanitize_pg_search_query` | `common` | Query/path pre-processing utilities |
| `ResolvedGraphSymbol`, `VisibleSearchOutcome` | `common` / `symbols` | Result types |

### External dependencies and collaboration

`graph_boost` imports `crate::config::Context` for FalkorDB configuration, `crate::graph::code_graph` for graph traversal, `crate::search::fts` for the initial symbol resolution, and `crate::visibility` to scope the graph context to the source project (`graph_boost.rs:9-12`). `rrf` delegates entirely to `gobby_core::search::rrf_merge` (`rrf.rs:16`), keeping ranking logic in the shared core crate. Callers outside this module — hybrid search orchestrators — are expected to drive the three-phase pattern: run FTS, optionally run graph expansion, then call `rrf::merge` with the combined source lists.
[crates/gcode/src/search/fts/common.rs:16]
[crates/gcode/src/search/fts/content.rs:13-21]
[crates/gcode/src/search/fts/counts.rs:10-66]
[crates/gcode/src/search/fts/graph.rs:16-50]
[crates/gcode/src/search/fts/symbols.rs:15-18]

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/gcode/src/search/fts\|crates/gcode/src/search/fts]] | ## Module: crates/gcode/src/search/fts |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/search/fts.rs\|crates/gcode/src/search/fts.rs]] | `crates/gcode/src/search/fts.rs` has no indexed API symbols. |
| [[code/files/crates/gcode/src/search/graph_boost.rs\|crates/gcode/src/search/graph_boost.rs]] | `crates/gcode/src/search/graph_boost.rs` exposes 9 indexed API symbols. |
| [[code/files/crates/gcode/src/search/mod.rs\|crates/gcode/src/search/mod.rs]] | `crates/gcode/src/search/mod.rs` has no indexed API symbols. |
| [[code/files/crates/gcode/src/search/rrf.rs\|crates/gcode/src/search/rrf.rs]] | `crates/gcode/src/search/rrf.rs` exposes 9 indexed API symbols. |

