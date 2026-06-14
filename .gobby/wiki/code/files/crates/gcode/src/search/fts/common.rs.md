---
title: crates/gcode/src/search/fts/common.rs
type: code_file
provenance:
- file: crates/gcode/src/search/fts/common.rs
  ranges:
  - '16'
  - 19-22
  - 25-29
  - 32-36
  - 38-54
  - 56-59
  - 63-69
  - 71-76
  - 78-86
  - 88-123
  - 126-135
  - 138-148
  - 150-152
  - 154-175
  - 177-184
  - 186-196
  - 198-200
  - 202-233
  - 235-250
  - 252-272
  - 274-291
  - 293-341
  - 348-354
  - 357-362
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/search/fts/common.rs

Module: [[code/modules/crates/gcode/src/search/fts|crates/gcode/src/search/fts]]

## Purpose

This file provides utilities for full-text search queries against PostgreSQL symbol records. It defines core types like `ResolvedGraphSymbol` and `SymbolFilters`, and exports a central `query_symbols_by_conditions` function that executes parameterized queries with dynamic SQL WHERE/ORDER BY clauses. Supporting functions build SQL fragments: `push_symbol_filters` adds kind/language/path conditions, `push_path_filter` handles glob-pattern matching via SQL LIKE expressions, and `push_visible_project_file_filter` excludes tombstoned files while enforcing project scope visibility. The `SymbolOrder` enum generates ORDER BY clauses for BM25 relevance, lexicographic name ordering, or case-sensitive exact-match prioritization. Helper functions like `push_param`, `param_refs`, and `trusted_row_id` manage parameter binding to prevent SQL injection, while path utilities (`escape_like`, `glob_to_like_prefix`, `expand_paths`, `compile_patterns`) transform glob patterns into SQL-safe prefixes. The module centralizes FTS SQL construction to keep query sanitation consistent across the codebase.
[crates/gcode/src/search/fts/common.rs:16]
[crates/gcode/src/search/fts/common.rs:19-22]
[crates/gcode/src/search/fts/common.rs:25-29]
[crates/gcode/src/search/fts/common.rs:32-36]
[crates/gcode/src/search/fts/common.rs:38-54]

## API Symbols

- `PgParam` (type) component `PgParam [type]` (`875a5446-fa88-50ae-8ce9-ad57a6deeec3`) lines 16-16 [crates/gcode/src/search/fts/common.rs:16]
  - Signature: `pub(super) type PgParam = Box<dyn ToSql + Sync>;`
  - Purpose: Indexed type `PgParam` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:16]
- `ResolvedGraphSymbol` (class) component `ResolvedGraphSymbol [class]` (`5b940a4c-43f0-5ceb-9f69-bb58acf44bb5`) lines 19-22 [crates/gcode/src/search/fts/common.rs:19-22]
  - Signature: `pub struct ResolvedGraphSymbol {`
  - Purpose: ResolvedGraphSymbol is a struct that encapsulates a resolved graph symbol with a unique string identifier and human-readable display name. [crates/gcode/src/search/fts/common.rs:19-22]
- `SymbolFilters` (class) component `SymbolFilters [class]` (`37a9e542-63a5-5f2a-88b9-a8daa24f4685`) lines 25-29 [crates/gcode/src/search/fts/common.rs:25-29]
  - Signature: `pub(super) struct SymbolFilters<'a> {`
  - Purpose: SymbolFilters is a borrowed filter struct that optionally constrains symbol queries by kind and language while requiring a slice of file paths. [crates/gcode/src/search/fts/common.rs:25-29]
- `SymbolOrder` (type) component `SymbolOrder [type]` (`e6bb7f19-4789-53b7-b4a5-7a3d95651935`) lines 32-36 [crates/gcode/src/search/fts/common.rs:32-36]
  - Signature: `pub(super) enum SymbolOrder {`
  - Purpose: Indexed type `SymbolOrder` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:32-36]
- `SymbolOrder` (class) component `SymbolOrder [class]` (`875c9f83-ee42-5335-a79a-f943fe8d6f9a`) lines 38-54 [crates/gcode/src/search/fts/common.rs:38-54]
  - Signature: `impl SymbolOrder {`
  - Purpose: SymbolOrder::sql() generates SQL ORDER BY clauses for three symbol-sorting strategies: BM25 relevance scoring, name/path/line lexicographic ordering, or exact-case-match prioritization with secondary sorting. [crates/gcode/src/search/fts/common.rs:38-54]
- `SymbolOrder.sql` (method) component `SymbolOrder.sql [method]` (`80bd4151-9a3a-5dae-89d9-58ac38cdf4fb`) lines 39-53 [crates/gcode/src/search/fts/common.rs:39-53]
  - Signature: `fn sql(&self) -> String {`
  - Purpose: Returns a SQL ORDER BY clause string based on the enum variant's sorting strategy: BM25 relevance scoring, lexicographic name/path/line ordering, or case-sensitive exact-match-first prioritization. [crates/gcode/src/search/fts/common.rs:39-53]
- `trusted_row_id` (function) component `trusted_row_id [function]` (`3167635d-631c-5707-8b2d-6aa46bf46019`) lines 56-59 [crates/gcode/src/search/fts/common.rs:56-59]
  - Signature: `pub(super) fn trusted_row_id(row_id: &str) -> TrustedRowId {`
  - Purpose: Constructs a `TrustedRowId` via unsafe unchecked initialization, assuming the input is a static SQL row identifier for local table aliases as guaranteed by FTS callers. [crates/gcode/src/search/fts/common.rs:56-59]
- `push_param` (function) component `push_param [function]` (`33186fc9-8d87-555c-89d0-58c4b6c54b97`) lines 63-69 [crates/gcode/src/search/fts/common.rs:63-69]
  - Signature: `pub(super) fn push_param<T>(params: &mut Vec<PgParam>, value: T) -> String`
  - Purpose: Appends a boxed SQL-serializable value to a parameter vector and returns its corresponding PostgreSQL positional placeholder string (e.g., `$1`, `$2`). [crates/gcode/src/search/fts/common.rs:63-69]
- `param_refs` (function) component `param_refs [function]` (`95df4599-dd9f-564b-83ca-459b096613b2`) lines 71-76 [crates/gcode/src/search/fts/common.rs:71-76]
  - Signature: `pub(super) fn param_refs(params: &[PgParam]) -> Vec<&(dyn ToSql + Sync)> {`
  - Purpose: Converts a slice of `PgParam` into a vector of trait object references implementing `ToSql + Sync`. [crates/gcode/src/search/fts/common.rs:71-76]
- `query_count` (function) component `query_count [function]` (`06820a48-7d6c-549b-a9e6-b1b1c68426de`) lines 78-86 [crates/gcode/src/search/fts/common.rs:78-86]
  - Signature: `pub(super) fn query_count(`
  - Purpose: Executes a parameterized SQL query against a PostgreSQL connection and extracts the "count" column value from the result row, returning it as a `usize`. [crates/gcode/src/search/fts/common.rs:78-86]
- `push_visible_project_file_filter` (function) component `push_visible_project_file_filter [function]` (`a0cab5a7-d2d4-5809-9959-3c3e8c5a211f`) lines 88-123 [crates/gcode/src/search/fts/common.rs:88-123]
  - Signature: `pub(super) fn push_visible_project_file_filter(`
  - Purpose: # Summary

Constructs SQL WHERE clause conditions to filter visible project files by excluding tombstoned entries and applying scope-specific project filtering, with overlay shadowing where overlay project files hide identically-pathed parent project files. [crates/gcode/src/search/fts/common.rs:88-123]
- `escape_like` (function) component `escape_like [function]` (`8ff760fe-39ec-53a5-b358-e26a76e1864a`) lines 126-135 [crates/gcode/src/search/fts/common.rs:126-135]
  - Signature: `pub(super) fn escape_like(s: &str) -> String {`
  - Purpose: Escapes SQL LIKE pattern metacharacters (backslash, percent sign, underscore) by prefixing each with a backslash to treat them as literals. [crates/gcode/src/search/fts/common.rs:126-135]
- `glob_to_like_prefix` (function) component `glob_to_like_prefix [function]` (`03a59319-cb90-5da0-b6da-513367ba0b40`) lines 138-148 [crates/gcode/src/search/fts/common.rs:138-148]
  - Signature: `pub(super) fn glob_to_like_prefix(pattern: &str) -> Option<String> {`
  - Purpose: Extracts the literal prefix from a glob pattern (characters before any wildcard) and returns it as an escaped SQL LIKE prefix string with `%` suffix, or `None` if the pattern begins with a wildcard. [crates/gcode/src/search/fts/common.rs:138-148]
- `has_glob_meta` (function) component `has_glob_meta [function]` (`434dcd5b-7d2e-58e3-a9ca-16cfcc62b746`) lines 150-152 [crates/gcode/src/search/fts/common.rs:150-152]
  - Signature: `pub(super) fn has_glob_meta(path: &str) -> bool {`
  - Purpose: Checks whether a path string contains any glob pattern metacharacters (`*`, `?`, or `[`). [crates/gcode/src/search/fts/common.rs:150-152]
- `expand_paths` (function) component `expand_paths [function]` (`b759e95a-8cff-5199-ac82-4dc2ff56645b`) lines 154-175 [crates/gcode/src/search/fts/common.rs:154-175]
  - Signature: `pub fn expand_paths(paths: &[String]) -> Vec<String> {`
  - Purpose: Expands input file paths by appending `/**` glob patterns to non-glob paths while deduplicating results via HashSet insertion. [crates/gcode/src/search/fts/common.rs:154-175]
- `compile_patterns` (function) component `compile_patterns [function]` (`bbf9795e-e4aa-5b94-b61c-4c2f44ba6e94`) lines 177-184 [crates/gcode/src/search/fts/common.rs:177-184]
  - Signature: `pub fn compile_patterns(paths: &[String]) -> anyhow::Result<Vec<glob::Pattern>> {`
  - Purpose: Compiles a slice of glob pattern strings into a vector of `glob::Pattern` objects, returning an error if any pattern fails to parse. [crates/gcode/src/search/fts/common.rs:177-184]
- `path_like_prefixes` (function) component `path_like_prefixes [function]` (`930b5993-fb3e-5fb7-8d6c-f60518226697`) lines 186-196 [crates/gcode/src/search/fts/common.rs:186-196]
  - Signature: `pub(super) fn path_like_prefixes(paths: &[String]) -> Option<Vec<String>> {`
  - Purpose: Converts a slice of glob-pattern paths into their SQL LIKE-compatible prefixes, returning `None` if any conversion fails. [crates/gcode/src/search/fts/common.rs:186-196]
- `path_filter_requires_post_filter` (function) component `path_filter_requires_post_filter [function]` (`6a5ed17f-f567-5446-8471-355288c34719`) lines 198-200 [crates/gcode/src/search/fts/common.rs:198-200]
  - Signature: `pub fn path_filter_requires_post_filter(paths: &[String]) -> bool {`
  - Purpose: Returns true if the paths slice is non-empty but has no common path-like prefixes, indicating post-filtering is required. [crates/gcode/src/search/fts/common.rs:198-200]
- `push_path_filter` (function) component `push_path_filter [function]` (`24e75ff8-ffee-5114-97b1-60fbc8300eea`) lines 202-233 [crates/gcode/src/search/fts/common.rs:202-233]
  - Signature: `pub(super) fn push_path_filter(`
  - Purpose: Appends parameterized SQL LIKE conditions derived from path glob patterns to a conditions vector and returns whether post-query glob filtering is still required. [crates/gcode/src/search/fts/common.rs:202-233]
- `push_symbol_filters` (function) component `push_symbol_filters [function]` (`615c1ea3-a547-58c7-b5f1-bf520f214fec`) lines 235-250 [crates/gcode/src/search/fts/common.rs:235-250]
  - Signature: `pub(super) fn push_symbol_filters(`
  - Purpose: Appends parameterized SQL WHERE clause conditions for symbol filtering on kind, language, and paths to prevent SQL injection. [crates/gcode/src/search/fts/common.rs:235-250]
- `symbols_matching_paths` (function) component `symbols_matching_paths [function]` (`c748a762-7ce0-5443-819e-c67875245c7d`) lines 252-272 [crates/gcode/src/search/fts/common.rs:252-272]
  - Signature: `pub(super) fn symbols_matching_paths(`
  - Purpose: Filters symbols to those whose file paths match any of the provided path patterns, or returns all symbols if no patterns are provided. [crates/gcode/src/search/fts/common.rs:252-272]
- `append_unique_symbols` (function) component `append_unique_symbols [function]` (`021bf360-d2b3-5062-a29f-aaba0c00a4fc`) lines 274-291 [crates/gcode/src/search/fts/common.rs:274-291]
  - Signature: `pub(super) fn append_unique_symbols(`
  - Purpose: Appends symbols from an input vector to an output vector while deduplicating by symbol ID using a HashSet, up to a specified limit. [crates/gcode/src/search/fts/common.rs:274-291]
- `query_symbols_by_conditions` (function) component `query_symbols_by_conditions [function]` (`f7d875d0-1c61-5191-8ace-0132624e23a2`) lines 293-341 [crates/gcode/src/search/fts/common.rs:293-341]
  - Signature: `pub(super) fn query_symbols_by_conditions(`
  - Purpose: Executes a parameterized PostgreSQL query to retrieve Symbol records matching dynamic conditions and filters, with optional post-filtering for path-based constraints before returning a limited result set. [crates/gcode/src/search/fts/common.rs:293-341]
- `bm25_score_expression_uses_pdb_score` (function) component `bm25_score_expression_uses_pdb_score [function]` (`0c94647d-0190-534c-ab66-e0696b6a8385`) lines 348-354 [crates/gcode/src/search/fts/common.rs:348-354]
  - Signature: `fn bm25_score_expression_uses_pdb_score() {`
  - Purpose: This test verifies that `bm25_score_expr()` generates a `pdb.score()` expression rather than `pg_search.score()` when passed a trusted row ID. [crates/gcode/src/search/fts/common.rs:348-354]
- `symbol_bm25_order_uses_pdb_score` (function) component `symbol_bm25_order_uses_pdb_score [function]` (`627e2f5a-6d72-59b1-b259-70253558829d`) lines 357-362 [crates/gcode/src/search/fts/common.rs:357-362]
  - Signature: `fn symbol_bm25_order_uses_pdb_score() {`
  - Purpose: This test verifies that `SymbolOrder::Bm25Score` generates SQL using `pdb.score(cs.id) DESC, cs.id ASC` ordering while excluding `pg_search.score()`. [crates/gcode/src/search/fts/common.rs:357-362]

