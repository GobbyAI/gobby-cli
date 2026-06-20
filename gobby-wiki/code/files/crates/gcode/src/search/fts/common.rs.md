---
title: crates/gcode/src/search/fts/common.rs
type: code_file
provenance:
- file: crates/gcode/src/search/fts/common.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/search/fts/common.rs

Module: [[code/modules/crates/gcode/src/search/fts|crates/gcode/src/search/fts]]

## Overview

`crates/gcode/src/search/fts/common.rs` exposes 24 indexed API symbols.

## How it fits

`crates/gcode/src/search/fts/common.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `PgParam` | type | Indexed type `PgParam` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:16] |
| `ResolvedGraphSymbol` | class | 'ResolvedGraphSymbol' is a struct that stores a graph symbol’s unique identifier as 'id' and its human-readable label as 'display_name'. [crates/gcode/src/search/fts/common.rs:19-22] |
| `SymbolFilters` | class | 'SymbolFilters<'a>' is a scoped filter record that optionally constrains symbols by 'kind' and 'language', and carries a borrowed slice of 'paths' to match against. [crates/gcode/src/search/fts/common.rs:25-29] |
| `SymbolOrder` | type | Indexed type `SymbolOrder` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:32-36] |
| `SymbolOrder::sql` | method | Builds and returns an 'ORDER BY' SQL fragment for the current sort variant: BM25 score descending then 'cs.id' ascending, name/path/line ascending, or a case-sensitive exact-name priority 'CASE' expression followed by file path and line number. [crates/gcode/src/search/fts/common.rs:39-53] |
| `trusted_row_id` | function | Constructs a 'TrustedRowId' from a '&str' by unsafely calling 'TrustedRowId::new_unchecked', relying on the caller to supply a static SQL row identifier for a local table alias. [crates/gcode/src/search/fts/common.rs:56-59] |
| `push_param` | function | Appends a 'ToSql + Sync + 'static' value to the PostgreSQL parameter vector as a boxed 'PgParam' and returns its 1-based placeholder string in the form '"$N"'. [crates/gcode/src/search/fts/common.rs:63-69] |
| `param_refs` | function | Converts a slice of 'PgParam' values into a 'Vec' of '&(dyn ToSql + Sync)' trait-object references by iterating over each parameter, calling 'as_ref()', and collecting the cast references. [crates/gcode/src/search/fts/common.rs:71-76] |
| `query_count` | function | Executes the given SQL with converted PostgreSQL parameters via 'query_one', then reads the 'count' column as 'i64' and returns it as 'usize'. [crates/gcode/src/search/fts/common.rs:78-86] |
| `push_visible_project_file_filter` | function | Builds SQL WHERE-clause predicates to exclude tombstone-language files and restrict rows to either the current project or, for overlay indexing, the overlay project plus parent-project rows whose file paths do not have a shadowing file in the overlay. [crates/gcode/src/search/fts/common.rs:88-123] |
| `escape_like` | function | Returns a new string with every '\\', '%', and '_' character prefixed by a backslash so the input can be used safely in a SQL 'LIKE' pattern. [crates/gcode/src/search/fts/common.rs:126-135] |
| `glob_to_like_prefix` | function | Returns 'Some(escaped_prefix_with_trailing_% )' for the longest leading substring of 'pattern' before any glob metacharacter ('*', '?', or '['), or 'None' if the pattern starts with a wildcard or bracket. [crates/gcode/src/search/fts/common.rs:138-148] |
| `has_glob_meta` | function | Returns 'true' if the input path contains any glob metacharacter ('*', '?', or '['), otherwise 'false'. [crates/gcode/src/search/fts/common.rs:150-152] |
| `expand_paths` | function | Trims each input path, skips empties, expands non-glob paths into both the path itself and a recursive '/**' glob, and returns the resulting patterns in first-seen order with duplicates removed. [crates/gcode/src/search/fts/common.rs:154-175] |
| `compile_patterns` | function | Compiles each input string into a 'glob::Pattern', returning a 'Vec`<glob::Pattern>`' or an 'anyhow::Error' that wraps the first invalid glob with its original path and parser error. [crates/gcode/src/search/fts/common.rs:177-184] |
| `path_like_prefixes` | function | Returns 'Some' containing the 'glob_to_like_prefix' conversion of each input path in order, or 'None' if any path cannot be converted, and returns an empty vector when 'paths' is empty. [crates/gcode/src/search/fts/common.rs:186-196] |
| `path_filter_requires_post_filter` | function | Returns 'true' when 'paths' is non-empty and 'path_like_prefixes(paths)' yields 'None', indicating a post-filter is required. [crates/gcode/src/search/fts/common.rs:198-200] |
| `push_path_filter` | function | Builds and appends an 'OR'-joined SQL 'LIKE' predicate over 'alias.file_path' for path patterns that can be converted to prefixes, logs a warning and falls back to post-query glob filtering when conversion is impossible, and returns whether any non-empty path filter still requires post-processing. [crates/gcode/src/search/fts/common.rs:202-233] |
| `push_symbol_filters` | function | Appends SQL predicates for optional 'kind' and 'language' symbol filters, binds their values as 'PgParam's, and then delegates to 'push_path_filter', returning that function’s boolean result. [crates/gcode/src/search/fts/common.rs:235-250] |
| `symbols_matching_paths` | function | Compiles the provided path filters into match patterns, returns an empty vector if compilation fails, and otherwise filters the input 'Symbol' iterator to those whose 'file_path' matches at least one pattern or all symbols when no patterns are present. [crates/gcode/src/search/fts/common.rs:252-272] |
| `append_unique_symbols` | function | Appends symbols whose 'id' has not yet been seen to 'out', tracking IDs in 'seen' and stopping early once 'out' reaches 'limit' or immediately returning when 'limit == 0'. [crates/gcode/src/search/fts/common.rs:274-291] |
| `query_symbols_by_conditions` | function | Executes a parameterized SQL query against 'code_symbols' joined to 'code_indexed_files' using the provided conditions, filters, order, and limit, converts rows into 'Symbol' values, logs and returns an empty vector on query failure, and applies an in-memory path post-filter plus truncation when path filters cannot be fully pushed into SQL. [crates/gcode/src/search/fts/common.rs:293-341] |

_Verified by 2 in-file unit tests._

