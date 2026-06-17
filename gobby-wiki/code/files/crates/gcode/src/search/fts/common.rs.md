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
  - 39-53
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

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/search/fts/common.rs:16](crates/gcode/src/search/fts/common.rs#L16), [crates/gcode/src/search/fts/common.rs:19-22](crates/gcode/src/search/fts/common.rs#L19-L22), [crates/gcode/src/search/fts/common.rs:25-29](crates/gcode/src/search/fts/common.rs#L25-L29), [crates/gcode/src/search/fts/common.rs:32-36](crates/gcode/src/search/fts/common.rs#L32-L36), [crates/gcode/src/search/fts/common.rs:39-53](crates/gcode/src/search/fts/common.rs#L39-L53), [crates/gcode/src/search/fts/common.rs:56-59](crates/gcode/src/search/fts/common.rs#L56-L59), [crates/gcode/src/search/fts/common.rs:63-69](crates/gcode/src/search/fts/common.rs#L63-L69), [crates/gcode/src/search/fts/common.rs:71-76](crates/gcode/src/search/fts/common.rs#L71-L76), [crates/gcode/src/search/fts/common.rs:78-86](crates/gcode/src/search/fts/common.rs#L78-L86), [crates/gcode/src/search/fts/common.rs:88-123](crates/gcode/src/search/fts/common.rs#L88-L123), [crates/gcode/src/search/fts/common.rs:126-135](crates/gcode/src/search/fts/common.rs#L126-L135), [crates/gcode/src/search/fts/common.rs:138-148](crates/gcode/src/search/fts/common.rs#L138-L148), [crates/gcode/src/search/fts/common.rs:150-152](crates/gcode/src/search/fts/common.rs#L150-L152), [crates/gcode/src/search/fts/common.rs:154-175](crates/gcode/src/search/fts/common.rs#L154-L175), [crates/gcode/src/search/fts/common.rs:177-184](crates/gcode/src/search/fts/common.rs#L177-L184), [crates/gcode/src/search/fts/common.rs:186-196](crates/gcode/src/search/fts/common.rs#L186-L196), [crates/gcode/src/search/fts/common.rs:198-200](crates/gcode/src/search/fts/common.rs#L198-L200), [crates/gcode/src/search/fts/common.rs:202-233](crates/gcode/src/search/fts/common.rs#L202-L233), [crates/gcode/src/search/fts/common.rs:235-250](crates/gcode/src/search/fts/common.rs#L235-L250), [crates/gcode/src/search/fts/common.rs:252-272](crates/gcode/src/search/fts/common.rs#L252-L272), [crates/gcode/src/search/fts/common.rs:274-291](crates/gcode/src/search/fts/common.rs#L274-L291), [crates/gcode/src/search/fts/common.rs:293-341](crates/gcode/src/search/fts/common.rs#L293-L341), [crates/gcode/src/search/fts/common.rs:348-354](crates/gcode/src/search/fts/common.rs#L348-L354), [crates/gcode/src/search/fts/common.rs:357-362](crates/gcode/src/search/fts/common.rs#L357-L362)

</details>

# crates/gcode/src/search/fts/common.rs

Module: [[code/modules/crates/gcode/src/search/fts|crates/gcode/src/search/fts]]

## Purpose

Shared full-text-search query helpers for symbol lookup. The file defines small data types for resolved graph symbols, filter criteria, and ordering, then builds the SQL fragments and parameter lists used by symbol search queries. Its helpers cover safe Postgres parameter handling, count queries, visibility and path filtering, glob/prefix expansion, de-duplicating symbol results, and BM25-based ordering; it also centralizes pg_search query sanitization and trusted row-id handling so gcode and related search code generate consistent FTS SQL.
[crates/gcode/src/search/fts/common.rs:16]
[crates/gcode/src/search/fts/common.rs:19-22]
[crates/gcode/src/search/fts/common.rs:25-29]
[crates/gcode/src/search/fts/common.rs:32-36]
[crates/gcode/src/search/fts/common.rs:39-53]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `PgParam` | type | `pub(super) type PgParam = Box<dyn ToSql + Sync>;` | `PgParam [type]` | `875a5446-fa88-50ae-8ce9-ad57a6deeec3` | 16-16 [crates/gcode/src/search/fts/common.rs:16] | Indexed type `PgParam` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:16] |
| `ResolvedGraphSymbol` | class | `pub struct ResolvedGraphSymbol {` | `ResolvedGraphSymbol [class]` | `5b940a4c-43f0-5ceb-9f69-bb58acf44bb5` | 19-22 [crates/gcode/src/search/fts/common.rs:19-22] | Indexed class `ResolvedGraphSymbol` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:19-22] |
| `SymbolFilters` | class | `pub(super) struct SymbolFilters<'a> {` | `SymbolFilters [class]` | `37a9e542-63a5-5f2a-88b9-a8daa24f4685` | 25-29 [crates/gcode/src/search/fts/common.rs:25-29] | Indexed class `SymbolFilters` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:25-29] |
| `SymbolOrder` | type | `pub(super) enum SymbolOrder {` | `SymbolOrder [type]` | `e6bb7f19-4789-53b7-b4a5-7a3d95651935` | 32-36 [crates/gcode/src/search/fts/common.rs:32-36] | Indexed type `SymbolOrder` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:32-36] |
| `SymbolOrder::sql` | method | `fn sql(&self) -> String {` | `SymbolOrder::sql [method]` | `80bd4151-9a3a-5dae-89d9-58ac38cdf4fb` | 39-53 [crates/gcode/src/search/fts/common.rs:39-53] | Indexed method `SymbolOrder::sql` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:39-53] |
| `trusted_row_id` | function | `pub(super) fn trusted_row_id(row_id: &str) -> TrustedRowId {` | `trusted_row_id [function]` | `3167635d-631c-5707-8b2d-6aa46bf46019` | 56-59 [crates/gcode/src/search/fts/common.rs:56-59] | Indexed function `trusted_row_id` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:56-59] |
| `push_param` | function | `pub(super) fn push_param<T>(params: &mut Vec<PgParam>, value: T) -> String` | `push_param [function]` | `33186fc9-8d87-555c-89d0-58c4b6c54b97` | 63-69 [crates/gcode/src/search/fts/common.rs:63-69] | Indexed function `push_param` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:63-69] |
| `param_refs` | function | `pub(super) fn param_refs(params: &[PgParam]) -> Vec<&(dyn ToSql + Sync)> {` | `param_refs [function]` | `95df4599-dd9f-564b-83ca-459b096613b2` | 71-76 [crates/gcode/src/search/fts/common.rs:71-76] | Indexed function `param_refs` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:71-76] |
| `query_count` | function | `pub(super) fn query_count(` | `query_count [function]` | `06820a48-7d6c-549b-a9e6-b1b1c68426de` | 78-86 [crates/gcode/src/search/fts/common.rs:78-86] | Indexed function `query_count` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:78-86] |
| `push_visible_project_file_filter` | function | `pub(super) fn push_visible_project_file_filter(` | `push_visible_project_file_filter [function]` | `a0cab5a7-d2d4-5809-9959-3c3e8c5a211f` | 88-123 [crates/gcode/src/search/fts/common.rs:88-123] | Indexed function `push_visible_project_file_filter` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:88-123] |
| `escape_like` | function | `pub(super) fn escape_like(s: &str) -> String {` | `escape_like [function]` | `8ff760fe-39ec-53a5-b358-e26a76e1864a` | 126-135 [crates/gcode/src/search/fts/common.rs:126-135] | Indexed function `escape_like` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:126-135] |
| `glob_to_like_prefix` | function | `pub(super) fn glob_to_like_prefix(pattern: &str) -> Option<String> {` | `glob_to_like_prefix [function]` | `03a59319-cb90-5da0-b6da-513367ba0b40` | 138-148 [crates/gcode/src/search/fts/common.rs:138-148] | Indexed function `glob_to_like_prefix` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:138-148] |
| `has_glob_meta` | function | `pub(super) fn has_glob_meta(path: &str) -> bool {` | `has_glob_meta [function]` | `434dcd5b-7d2e-58e3-a9ca-16cfcc62b746` | 150-152 [crates/gcode/src/search/fts/common.rs:150-152] | Indexed function `has_glob_meta` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:150-152] |
| `expand_paths` | function | `pub fn expand_paths(paths: &[String]) -> Vec<String> {` | `expand_paths [function]` | `b759e95a-8cff-5199-ac82-4dc2ff56645b` | 154-175 [crates/gcode/src/search/fts/common.rs:154-175] | Indexed function `expand_paths` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:154-175] |
| `compile_patterns` | function | `pub fn compile_patterns(paths: &[String]) -> anyhow::Result<Vec<glob::Pattern>> {` | `compile_patterns [function]` | `bbf9795e-e4aa-5b94-b61c-4c2f44ba6e94` | 177-184 [crates/gcode/src/search/fts/common.rs:177-184] | Indexed function `compile_patterns` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:177-184] |
| `path_like_prefixes` | function | `pub(super) fn path_like_prefixes(paths: &[String]) -> Option<Vec<String>> {` | `path_like_prefixes [function]` | `930b5993-fb3e-5fb7-8d6c-f60518226697` | 186-196 [crates/gcode/src/search/fts/common.rs:186-196] | Indexed function `path_like_prefixes` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:186-196] |
| `path_filter_requires_post_filter` | function | `pub fn path_filter_requires_post_filter(paths: &[String]) -> bool {` | `path_filter_requires_post_filter [function]` | `6a5ed17f-f567-5446-8471-355288c34719` | 198-200 [crates/gcode/src/search/fts/common.rs:198-200] | Indexed function `path_filter_requires_post_filter` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:198-200] |
| `push_path_filter` | function | `pub(super) fn push_path_filter(` | `push_path_filter [function]` | `24e75ff8-ffee-5114-97b1-60fbc8300eea` | 202-233 [crates/gcode/src/search/fts/common.rs:202-233] | Indexed function `push_path_filter` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:202-233] |
| `push_symbol_filters` | function | `pub(super) fn push_symbol_filters(` | `push_symbol_filters [function]` | `615c1ea3-a547-58c7-b5f1-bf520f214fec` | 235-250 [crates/gcode/src/search/fts/common.rs:235-250] | Indexed function `push_symbol_filters` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:235-250] |
| `symbols_matching_paths` | function | `pub(super) fn symbols_matching_paths(` | `symbols_matching_paths [function]` | `c748a762-7ce0-5443-819e-c67875245c7d` | 252-272 [crates/gcode/src/search/fts/common.rs:252-272] | Indexed function `symbols_matching_paths` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:252-272] |
| `append_unique_symbols` | function | `pub(super) fn append_unique_symbols(` | `append_unique_symbols [function]` | `021bf360-d2b3-5062-a29f-aaba0c00a4fc` | 274-291 [crates/gcode/src/search/fts/common.rs:274-291] | Indexed function `append_unique_symbols` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:274-291] |
| `query_symbols_by_conditions` | function | `pub(super) fn query_symbols_by_conditions(` | `query_symbols_by_conditions [function]` | `f7d875d0-1c61-5191-8ace-0132624e23a2` | 293-341 [crates/gcode/src/search/fts/common.rs:293-341] | Indexed function `query_symbols_by_conditions` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:293-341] |
| `bm25_score_expression_uses_pdb_score` | function | `fn bm25_score_expression_uses_pdb_score() {` | `bm25_score_expression_uses_pdb_score [function]` | `0c94647d-0190-534c-ab66-e0696b6a8385` | 348-354 [crates/gcode/src/search/fts/common.rs:348-354] | Indexed function `bm25_score_expression_uses_pdb_score` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:348-354] |
| `symbol_bm25_order_uses_pdb_score` | function | `fn symbol_bm25_order_uses_pdb_score() {` | `symbol_bm25_order_uses_pdb_score [function]` | `627e2f5a-6d72-59b1-b259-70253558829d` | 357-362 [crates/gcode/src/search/fts/common.rs:357-362] | Indexed function `symbol_bm25_order_uses_pdb_score` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:357-362] |
