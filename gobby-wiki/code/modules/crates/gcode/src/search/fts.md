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

## Module: crates/gcode/src/search/fts

### Responsibilities

The `fts` module implements full-text search (FTS) over a PostgreSQL database using the `pg_search` BM25 extension. It provides all query construction, parameter binding, filtering, result hydration, and result-counting logic needed to search code symbols and file-content chunks. The module is organized into five focused sub-files — `common`, `content`, `counts`, `graph`, and `symbols` — plus a comprehensive integration test suite. BM25 query sanitization is deliberately re-exported from `gobby_core::search::sanitize_pg_search_query` (common.rs:12) to ensure `gcode` and `gwiki` apply identical escaping rules.

### Key Flows

**Symbol search** begins at `search_symbols_fts` / `search_symbols_fts_visible` (symbols.rs), which sanitize the raw query string, build a dynamic SQL `WHERE` clause by calling `push_symbol_filters` and optionally `push_visible_project_file_filter` (common.rs), and then hand off to `query_symbols_by_conditions` or `query_visible_symbols_by_conditions`. Path patterns are compiled with `compile_patterns`, converted to LIKE prefixes via `glob_to_like_prefix` (common.rs), or to PostgreSQL regexes via `glob_to_pg_regex` (common.rs), depending on whether the pattern contains unsupported glob meta-characters detected by `has_glob_meta`. Result ordering is governed by the `SymbolOrder` enum (common.rs:35-52): `Bm25Score` computes a BM25 rank with `bm25_score_expr`, `Name` sorts lexicographically, and `ExactCaseFirst` surfaces exact name/qualified-name matches first. The convenience entry points `search_symbols_exact_first` and `search_symbols_by_name` compose these ordering strategies. The `VisibleSearchOutcome` type (symbols.rs) wraps results as either `ok` or `degraded`, signaling when the visibility overlay was bypassed.

**Content search** follows a parallel path through `search_content` / `search_content_visible` (content.rs:22-), building a BM25 query against `code_content_chunks`, joining to `code_indexed_files`, and ordering by `content_bm25_order_by_sql` (content.rs:13). Rows are mapped to `ContentSearchHit` values by `content_hits_from_rows`, with highlighted snippets produced by `make_snippet` → `make_snippet_with_tokens` → `snippet_tokens`, the last of which builds a character-map via `lowercase_with_original_char_map`.

**Counting** (`counts.rs`) mirrors every search function with a `COUNT(*)` variant — `count_text`, `count_content`, `count_symbols_fts_visible`, `count_content_bm25_visible`, etc. — returning `usize` and swallowing errors to zero rather than propagating them.

**Graph symbol resolution** (`graph.rs`) provides `resolve_graph_symbol` and `resolve_graph_symbol_by_id`, which translate fuzzy candidate sets into a single `ResolvedGraphSymbol` via `resolve_from_candidates` and `decisive_resolution`. `resolve_graph_symbol` calls `search_symbols_by_name` internally to enumerate candidates before attempting resolution.

### Collaboration Points

The module imports foundational types from several sibling crates:

| Import site | Symbol | Source |
|---|---|---|
| common.rs:12-13 | `sanitize_pg_search_query`, `TrustedRowId`, `bm25_score_expr` | `gobby_core::search` |
| common.rs:7 | `Context`, `ProjectIndexScope` | `crate::config` |
| common.rs:9 | `Symbol` | `crate::models` |
| common.rs:10 | `visibility` | `crate::visibility` |
| content.rs:5 | `ContentSearchHit` | `crate::models` |
| content.rs:6 | `TOMBSTONE_LANGUAGE` | `crate::visibility` |

The module calls into the PostgreSQL client (`postgres::Client`) directly for all query execution; it does not go through any ORM layer. Parameter binding is mediated entirely by the local helpers `push_param` / `param_refs` / `query_count` (common.rs:64-86) so that every call site stays free of manual `$N` index arithmetic.

### Public API Summary

| Symbol | File | Role |
|---|---|---|
| `PgParam` | common.rs | Type alias: `Box<dyn ToSql + Sync>` for query parameters |
| `ResolvedGraphSymbol` | common.rs | Resolved symbol id + display name |
| `SymbolFilters` | common.rs | `kind`, `language`, `paths` filter bag |
| `SymbolOrder` | common.rs | BM25, name, or exact-case-first ordering |
| `escape_like` / `glob_to_like_prefix` | common.rs | Path → SQL LIKE conversion |
| `glob_to_pg_regex` | common.rs | Path glob → PostgreSQL regex |
| `expand_paths` / `compile_patterns` | common.rs | Path list normalization and validation |
| `push_symbol_filters` / `push_path_filter` | common.rs | Dynamic WHERE-clause builders |
| `push_visible_project_file_filter` | common.rs | Visibility overlay SQL injection |
| `search_symbols_fts` / `search_symbols_fts_visible` | symbols.rs | Main BM25 symbol search entry points |
| `search_symbols_by_name` / `search_symbols_by_name_visible` | symbols.rs | Name-ordered symbol search |
| `search_symbols_exact_first` / `search_symbols_exact_first_visible` | symbols.rs | Exact-match-prioritized symbol search |
| `search_content` / `search_content_visible` | content.rs | BM25 content-chunk search |
| `search_text` / `search_text_visible` | symbols.rs | Thin text-search wrappers |
| `count_text` / `count_text_visible` | counts.rs | Symbol BM25 result count |
| `count_content` / `count_content_visible` | counts.rs | Content-chunk BM25 result count |
| `count_symbols_fts_visible` | counts.rs | Visibility-filtered symbol count |
| `count_content_bm25_visible` | counts.rs | Visibility-filtered content count |
| `resolve_graph_symbol` / `resolve_graph_symbol_by_id` | graph.rs | Fuzzy → decisive symbol resolution |
| `VisibleSearchOutcome` | symbols.rs | `ok` / `degraded` visibility wrapper |
| `make_snippet` / `snippet_tokens` | content.rs | Hit highlighting helpers |
| `FILTERED_FETCH_CAP` | common.rs | Hard cap (10 000) for pre-filter fetches |

### Test Coverage

`tests.rs` (34 symbols) exercises path utilities (`glob_to_like_prefix`, `expand_paths`, `compile_patterns`, `path_like_prefixes`), query sanitization rules (`sanitize_pg_search_query` — leading-minus escaping, DSL punctuation preservation), glob-to-PostgreSQL-regex conversion, and — through fixtures that create isolated overlay-visibility tables using a `unique_test_id` timestamp prefix (tests.rs:17-25) — the full end-to-end search and count functions against a live Postgres client. The overlay tables covered are `code_calls`, `code_imports`, `code_symbols`, `code_content_chunks`, `code_indexed_files`, and `code_indexed_projects` (tests.rs:8-14).
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

