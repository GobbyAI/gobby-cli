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

`crates/gcode/src/search/fts/common.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `PgParam` | type | Indexed type `PgParam` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:16] |
| `ResolvedGraphSymbol` | class | 'ResolvedGraphSymbol' is a struct that stores a graph symbol’s unique identifier as 'id' and its human-readable label as 'display_name'. [crates/gcode/src/search/fts/common.rs:19-22] |
| `SymbolFilters` | class | 'SymbolFilters<'a>' is a scoped filter record that optionally constrains symbols by 'kind' and 'language', and carries a borrowed slice of 'paths' to match against. [crates/gcode/src/search/fts/common.rs:25-29] |
| `SymbolOrder` | type | Indexed type `SymbolOrder` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:32-36] |
| `SymbolOrder::sql` | method | Indexed method `SymbolOrder::sql` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:39-53] |
| `trusted_row_id` | function | Constructs a 'TrustedRowId' from a '&str' by unsafely calling 'TrustedRowId::new_unchecked', relying on the caller to supply a static SQL row identifier for a local table alias. [crates/gcode/src/search/fts/common.rs:56-59] |
| `push_param` | function | Appends a 'ToSql + Sync + 'static' value to the PostgreSQL parameter vector as a boxed 'PgParam' and returns its 1-based placeholder string in the form '"$N"'. [crates/gcode/src/search/fts/common.rs:63-69] |
| `param_refs` | function | Converts a slice of 'PgParam' values into a 'Vec' of '&(dyn ToSql + Sync)' trait-object references by iterating over each parameter, calling 'as_ref()', and collecting the cast references. [crates/gcode/src/search/fts/common.rs:71-76] |
| `query_count` | function | Executes the given SQL with converted PostgreSQL parameters via 'query_one', then reads the 'count' column as 'i64' and returns it as 'usize'. [crates/gcode/src/search/fts/common.rs:78-86] |
| `push_visible_project_file_filter` | function | Builds SQL WHERE-clause predicates to exclude tombstone-language files and restrict rows to either the current project or, for overlay indexing, the overlay project plus parent-project rows whose file paths do not have a shadowing file in the overlay. [crates/gcode/src/search/fts/common.rs:88-123] |
| `escape_like` | function | Returns a new string with every '\\', '%', and '_' character prefixed by a backslash so the input can be used safely in a SQL 'LIKE' pattern. [crates/gcode/src/search/fts/common.rs:126-135] |
| `glob_to_like_prefix` | function | Indexed function `glob_to_like_prefix` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:138-148] |
| `has_glob_meta` | function | Indexed function `has_glob_meta` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:150-152] |
| `expand_paths` | function | Indexed function `expand_paths` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:154-175] |
| `compile_patterns` | function | Indexed function `compile_patterns` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:177-184] |
| `path_like_prefixes` | function | Indexed function `path_like_prefixes` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:186-196] |
| `path_filter_requires_post_filter` | function | Indexed function `path_filter_requires_post_filter` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:198-200] |
| `push_path_filter` | function | Indexed function `push_path_filter` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:202-233] |
| `push_symbol_filters` | function | Indexed function `push_symbol_filters` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:235-250] |
| `symbols_matching_paths` | function | Indexed function `symbols_matching_paths` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:252-272] |
| `append_unique_symbols` | function | Indexed function `append_unique_symbols` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:274-291] |
| `query_symbols_by_conditions` | function | Indexed function `query_symbols_by_conditions` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:293-341] |
| `bm25_score_expression_uses_pdb_score` | function | Indexed function `bm25_score_expression_uses_pdb_score` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:348-354] |
| `symbol_bm25_order_uses_pdb_score` | function | Indexed function `symbol_bm25_order_uses_pdb_score` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:357-362] |

