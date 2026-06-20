---
title: crates/gcode/src/search/fts
type: code_module
provenance:
- file: crates/gcode/src/search/fts/common.rs
- file: crates/gcode/src/search/fts/content.rs
- file: crates/gcode/src/search/fts/counts.rs
- file: crates/gcode/src/search/fts/graph.rs
- file: crates/gcode/src/search/fts/symbols.rs
- file: crates/gcode/src/search/fts/tests.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/search/fts

Parent: [[code/modules/crates/gcode/src/search|crates/gcode/src/search]]

## Overview

The `crates/gcode/src/search/fts` module implements PostgreSQL-backed full-text search for code symbols and content chunks. `common.rs` centralizes shared SQL helpers: pg_search query sanitation from `gobby_core`, trusted BM25 row IDs, parameter binding, count execution, symbol ordering, and reusable filter construction for projects, languages, paths, and visibility (`crates/gcode/src/search/fts/common.rs:1-100`). Content search builds BM25 queries against `code_content_chunks`, joins `code_indexed_files`, applies language/path filters, and orders results by BM25 score with deterministic tie-breakers (`crates/gcode/src/search/fts/content.rs:1-100`).

The count path mirrors the search path: `count_text` and `count_content` reject empty queries, sanitize BM25 input, build parameterized SQL over symbols or content, and return zero on unsupported or failed pg_search execution. Symbol counts can fall back to row counting with post-filtered file paths when path glob handling requires it (`crates/gcode/src/search/fts/counts.rs:1-100`). The visible variants and graph helpers in the component table show this module also participates in scoped search, visibility-aware queries, and symbol resolution flows.

This module collaborates with the wider system through `postgres::Client` and `ToSql` for database execution, `crate::config::{Context, ProjectIndexScope}` for scoped/visible search context, `crate::models::{Symbol, ContentSearchHit}` for returned domain objects, and `crate::visibility` for overlay/tombstone behavior (`crates/gcode/src/search/fts/common.rs:1-100`, `crates/gcode/src/search/fts/content.rs:1-100`). Its tests cover shared search syntax rules, glob/path expansion, invalid glob reporting, and overlay visibility tables, anchoring expected behavior across symbols, content, and visibility-aware indexes (`crates/gcode/src/search/fts/tests.rs:1-100`).

| Public API area | Symbols |
| --- | --- |
| Shared SQL/query helpers | `sanitize_pg_search_query`, `trusted_row_id`, `push_param`, `param_refs`, `query_count` |
| Path/filter helpers | `expand_paths`, `compile_patterns`, `path_like_prefixes`, `push_path_filter`, `push_symbol_filters` |
| Content search | `search_content`, `search_content_visible`, `content_hits_from_rows`, `make_snippet` |
| Count APIs | `count_text`, `count_content`, `count_text_visible`, `count_content_visible` |
| Symbol search | `search_symbols_fts`, `search_symbols_by_name`, `search_symbols_exact_first`, visible variants |
| Graph resolution | `resolve_graph_symbol_by_id`, `resolve_graph_symbol`, `ResolvedGraphSymbol` |
[crates/gcode/src/search/fts/common.rs:16]
[crates/gcode/src/search/fts/content.rs:13-21]
[crates/gcode/src/search/fts/counts.rs:10-66]
[crates/gcode/src/search/fts/graph.rs:16-50]
[crates/gcode/src/search/fts/symbols.rs:15-18]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/search/fts/common.rs\|crates/gcode/src/search/fts/common.rs]] | `crates/gcode/src/search/fts/common.rs` exposes 24 indexed API symbols. |
| [[code/files/crates/gcode/src/search/fts/content.rs\|crates/gcode/src/search/fts/content.rs]] | `crates/gcode/src/search/fts/content.rs` exposes 12 indexed API symbols. |
| [[code/files/crates/gcode/src/search/fts/counts.rs\|crates/gcode/src/search/fts/counts.rs]] | `crates/gcode/src/search/fts/counts.rs` exposes 13 indexed API symbols. |
| [[code/files/crates/gcode/src/search/fts/graph.rs\|crates/gcode/src/search/fts/graph.rs]] | `crates/gcode/src/search/fts/graph.rs` exposes 8 indexed API symbols. |
| [[code/files/crates/gcode/src/search/fts/symbols.rs\|crates/gcode/src/search/fts/symbols.rs]] | `crates/gcode/src/search/fts/symbols.rs` exposes 12 indexed API symbols. |
| [[code/files/crates/gcode/src/search/fts/tests.rs\|crates/gcode/src/search/fts/tests.rs]] | `crates/gcode/src/search/fts/tests.rs` exposes 34 indexed API symbols. |

