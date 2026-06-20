---
title: crates/gcode/src/search/fts/counts.rs
type: code_file
provenance:
- file: crates/gcode/src/search/fts/counts.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/search/fts/counts.rs

Module: [[code/modules/crates/gcode/src/search/fts|crates/gcode/src/search/fts]]

## Overview

`crates/gcode/src/search/fts/counts.rs` exposes 13 indexed API symbols.

## How it fits

`crates/gcode/src/search/fts/counts.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `count_text` | function | Returns the count of code-symbol rows in a project whose name, qualified name, signature, docstring, or summary match a sanitized BM25 'pg_search' query, optionally filtered by language and paths, falling back to a post-filtered file-path count when needed and returning '0' on empty/invalid queries or database errors. [crates/gcode/src/search/fts/counts.rs:10-66] |
| `count_content` | function | Returns the number of 'code_content_chunks' rows matching a sanitized BM25/pg_search query for a given project, with optional language and path filters, and falls back to '0' on empty/invalid queries or database errors. [crates/gcode/src/search/fts/counts.rs:69-113] |
| `count_visible_symbols_by_conditions` | function | Counts visible code-symbol rows matching the given conditions, applying symbol and project-file visibility filters and, if path predicates require post-filtering, delegating to a path-aware counting helper; otherwise it executes a 'COUNT(*)' SQL join over 'code_symbols' and 'code_indexed_files'. [crates/gcode/src/search/fts/counts.rs:115-146] |
| `count_symbol_file_path_rows` | function | Builds a 'COUNT(*)' query over 'code_symbols' joined to 'code_indexed_files' on 'project_id' and 'file_path', adds a regex-based file-path filter for the provided 'paths' via 'push_pg_regex_path_filter', and returns the matching row count as a 'usize'. [crates/gcode/src/search/fts/counts.rs:148-164] |
| `push_pg_regex_path_filter` | function | Builds a PostgreSQL file-path filter by converting valid glob 'paths' to regexes, adding them as a text-array parameter, and appending either 'FALSE' when none are valid or a 'alias.file_path ~ ANY(...)' condition to 'conditions'. [crates/gcode/src/search/fts/counts.rs:166-191] |
| `glob_to_pg_regex` | function | Converts a limited glob pattern into a PostgreSQL-compatible anchored regex by translating '*' to '[^/]*' or '.*' for '**', '?' to '[^/]', bracket classes with '!' negation, escaping regex metacharacters, and returning 'None' for unterminated character classes. [crates/gcode/src/search/fts/counts.rs:193-243] |
| `count_symbols_fts_visible` | function | Counts the number of visible symbols matching a BM25 full-text query across 'name', 'qualified_name', 'signature', 'docstring', or 'summary', then delegates filtering by context, language, and paths to 'count_visible_symbols_by_conditions'. [crates/gcode/src/search/fts/counts.rs:245-259] |
| `push_content_filters` | function | Appends SQL filter predicates to 'conditions' for an optional 'alias.language' equality check and the path-based constraints produced by 'push_path_filter', while registering any bound values in 'params'. [crates/gcode/src/search/fts/counts.rs:261-273] |
| `count_visible_content_by_conditions` | function | Builds a 'COUNT(*)' query over 'code_content_chunks' joined to 'code_indexed_files', applies content/language/path filters plus a visible-project-file filter, and returns the resulting row count as a 'usize'. [crates/gcode/src/search/fts/counts.rs:275-294] |
| `count_content_bm25_visible` | function | Executes a visible-content count query by building a single PostgreSQL condition 'c.content @@@ bm25_query' and delegating to 'count_visible_content_by_conditions' with the provided context, language filter, and path list. [crates/gcode/src/search/fts/counts.rs:296-307] |
| `count_text_visible` | function | Returns the number of visible symbols matching a sanitized 'pg_search' full-text query, or '0' if the input is blank, contains no searchable terms, or the underlying count query fails. [crates/gcode/src/search/fts/counts.rs:309-333] |
| `count_content_visible` | function | Returns the count of visible content matching a sanitized 'pg_search' BM25 query for the given context, language, and paths, but yields '0' if the query is empty, sanitizes to no search terms, or the underlying count operation fails. [crates/gcode/src/search/fts/counts.rs:335-359] |

_Verified by 1 in-file unit test._

