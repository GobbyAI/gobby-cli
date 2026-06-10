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

# crates/gcode/src/search/fts/common.rs

Module: [[code/modules/crates/gcode/src/search/fts|crates/gcode/src/search/fts]]

## Purpose

`crates/gcode/src/search/fts/common.rs` exposes 25 indexed API symbols.
[crates/gcode/src/search/fts/common.rs:16]
[crates/gcode/src/search/fts/common.rs:19-22]
[crates/gcode/src/search/fts/common.rs:25-29]
[crates/gcode/src/search/fts/common.rs:32-36]
[crates/gcode/src/search/fts/common.rs:38-54]
[crates/gcode/src/search/fts/common.rs:39-53]
[crates/gcode/src/search/fts/common.rs:56-59]
[crates/gcode/src/search/fts/common.rs:63-69]
[crates/gcode/src/search/fts/common.rs:71-76]
[crates/gcode/src/search/fts/common.rs:78-86]
[crates/gcode/src/search/fts/common.rs:88-123]
[crates/gcode/src/search/fts/common.rs:126-135]
[crates/gcode/src/search/fts/common.rs:138-148]
[crates/gcode/src/search/fts/common.rs:150-152]
[crates/gcode/src/search/fts/common.rs:154-175]
[crates/gcode/src/search/fts/common.rs:177-184]
[crates/gcode/src/search/fts/common.rs:186-196]
[crates/gcode/src/search/fts/common.rs:198-200]
[crates/gcode/src/search/fts/common.rs:202-233]
[crates/gcode/src/search/fts/common.rs:235-250]
[crates/gcode/src/search/fts/common.rs:252-272]
[crates/gcode/src/search/fts/common.rs:274-291]
[crates/gcode/src/search/fts/common.rs:293-341]
[crates/gcode/src/search/fts/common.rs:348-354]
[crates/gcode/src/search/fts/common.rs:357-362]

## API Symbols

- `PgParam` (type) component `PgParam [type]` (`875a5446-fa88-50ae-8ce9-ad57a6deeec3`) lines 16-16 [crates/gcode/src/search/fts/common.rs:16]
  - Signature: `pub(super) type PgParam = Box<dyn ToSql + Sync>;`
  - Purpose: Indexed type `PgParam` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:16]
- `ResolvedGraphSymbol` (class) component `ResolvedGraphSymbol [class]` (`5b940a4c-43f0-5ceb-9f69-bb58acf44bb5`) lines 19-22 [crates/gcode/src/search/fts/common.rs:19-22]
  - Signature: `pub struct ResolvedGraphSymbol {`
  - Purpose: Indexed class `ResolvedGraphSymbol` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:19-22]
- `SymbolFilters` (class) component `SymbolFilters [class]` (`37a9e542-63a5-5f2a-88b9-a8daa24f4685`) lines 25-29 [crates/gcode/src/search/fts/common.rs:25-29]
  - Signature: `pub(super) struct SymbolFilters<'a> {`
  - Purpose: Indexed class `SymbolFilters` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:25-29]
- `SymbolOrder` (type) component `SymbolOrder [type]` (`e6bb7f19-4789-53b7-b4a5-7a3d95651935`) lines 32-36 [crates/gcode/src/search/fts/common.rs:32-36]
  - Signature: `pub(super) enum SymbolOrder {`
  - Purpose: Indexed type `SymbolOrder` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:32-36]
- `SymbolOrder` (class) component `SymbolOrder [class]` (`875c9f83-ee42-5335-a79a-f943fe8d6f9a`) lines 38-54 [crates/gcode/src/search/fts/common.rs:38-54]
  - Signature: `impl SymbolOrder {`
  - Purpose: Indexed class `SymbolOrder` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:38-54]
- `SymbolOrder.sql` (method) component `SymbolOrder.sql [method]` (`80bd4151-9a3a-5dae-89d9-58ac38cdf4fb`) lines 39-53 [crates/gcode/src/search/fts/common.rs:39-53]
  - Signature: `fn sql(&self) -> String {`
  - Purpose: Indexed method `SymbolOrder.sql` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:39-53]
- `trusted_row_id` (function) component `trusted_row_id [function]` (`3167635d-631c-5707-8b2d-6aa46bf46019`) lines 56-59 [crates/gcode/src/search/fts/common.rs:56-59]
  - Signature: `pub(super) fn trusted_row_id(row_id: &str) -> TrustedRowId {`
  - Purpose: Indexed function `trusted_row_id` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:56-59]
- `push_param` (function) component `push_param [function]` (`33186fc9-8d87-555c-89d0-58c4b6c54b97`) lines 63-69 [crates/gcode/src/search/fts/common.rs:63-69]
  - Signature: `pub(super) fn push_param<T>(params: &mut Vec<PgParam>, value: T) -> String`
  - Purpose: Indexed function `push_param` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:63-69]
- `param_refs` (function) component `param_refs [function]` (`95df4599-dd9f-564b-83ca-459b096613b2`) lines 71-76 [crates/gcode/src/search/fts/common.rs:71-76]
  - Signature: `pub(super) fn param_refs(params: &[PgParam]) -> Vec<&(dyn ToSql + Sync)> {`
  - Purpose: Indexed function `param_refs` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:71-76]
- `query_count` (function) component `query_count [function]` (`06820a48-7d6c-549b-a9e6-b1b1c68426de`) lines 78-86 [crates/gcode/src/search/fts/common.rs:78-86]
  - Signature: `pub(super) fn query_count(`
  - Purpose: Indexed function `query_count` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:78-86]
- `push_visible_project_file_filter` (function) component `push_visible_project_file_filter [function]` (`a0cab5a7-d2d4-5809-9959-3c3e8c5a211f`) lines 88-123 [crates/gcode/src/search/fts/common.rs:88-123]
  - Signature: `pub(super) fn push_visible_project_file_filter(`
  - Purpose: Indexed function `push_visible_project_file_filter` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:88-123]
- `escape_like` (function) component `escape_like [function]` (`8ff760fe-39ec-53a5-b358-e26a76e1864a`) lines 126-135 [crates/gcode/src/search/fts/common.rs:126-135]
  - Signature: `pub(super) fn escape_like(s: &str) -> String {`
  - Purpose: Indexed function `escape_like` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:126-135]
- `glob_to_like_prefix` (function) component `glob_to_like_prefix [function]` (`03a59319-cb90-5da0-b6da-513367ba0b40`) lines 138-148 [crates/gcode/src/search/fts/common.rs:138-148]
  - Signature: `pub(super) fn glob_to_like_prefix(pattern: &str) -> Option<String> {`
  - Purpose: Indexed function `glob_to_like_prefix` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:138-148]
- `has_glob_meta` (function) component `has_glob_meta [function]` (`434dcd5b-7d2e-58e3-a9ca-16cfcc62b746`) lines 150-152 [crates/gcode/src/search/fts/common.rs:150-152]
  - Signature: `pub(super) fn has_glob_meta(path: &str) -> bool {`
  - Purpose: Indexed function `has_glob_meta` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:150-152]
- `expand_paths` (function) component `expand_paths [function]` (`b759e95a-8cff-5199-ac82-4dc2ff56645b`) lines 154-175 [crates/gcode/src/search/fts/common.rs:154-175]
  - Signature: `pub fn expand_paths(paths: &[String]) -> Vec<String> {`
  - Purpose: Indexed function `expand_paths` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:154-175]
- `compile_patterns` (function) component `compile_patterns [function]` (`bbf9795e-e4aa-5b94-b61c-4c2f44ba6e94`) lines 177-184 [crates/gcode/src/search/fts/common.rs:177-184]
  - Signature: `pub fn compile_patterns(paths: &[String]) -> anyhow::Result<Vec<glob::Pattern>> {`
  - Purpose: Indexed function `compile_patterns` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:177-184]
- `path_like_prefixes` (function) component `path_like_prefixes [function]` (`930b5993-fb3e-5fb7-8d6c-f60518226697`) lines 186-196 [crates/gcode/src/search/fts/common.rs:186-196]
  - Signature: `pub(super) fn path_like_prefixes(paths: &[String]) -> Option<Vec<String>> {`
  - Purpose: Indexed function `path_like_prefixes` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:186-196]
- `path_filter_requires_post_filter` (function) component `path_filter_requires_post_filter [function]` (`6a5ed17f-f567-5446-8471-355288c34719`) lines 198-200 [crates/gcode/src/search/fts/common.rs:198-200]
  - Signature: `pub fn path_filter_requires_post_filter(paths: &[String]) -> bool {`
  - Purpose: Indexed function `path_filter_requires_post_filter` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:198-200]
- `push_path_filter` (function) component `push_path_filter [function]` (`24e75ff8-ffee-5114-97b1-60fbc8300eea`) lines 202-233 [crates/gcode/src/search/fts/common.rs:202-233]
  - Signature: `pub(super) fn push_path_filter(`
  - Purpose: Indexed function `push_path_filter` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:202-233]
- `push_symbol_filters` (function) component `push_symbol_filters [function]` (`615c1ea3-a547-58c7-b5f1-bf520f214fec`) lines 235-250 [crates/gcode/src/search/fts/common.rs:235-250]
  - Signature: `pub(super) fn push_symbol_filters(`
  - Purpose: Indexed function `push_symbol_filters` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:235-250]
- `symbols_matching_paths` (function) component `symbols_matching_paths [function]` (`c748a762-7ce0-5443-819e-c67875245c7d`) lines 252-272 [crates/gcode/src/search/fts/common.rs:252-272]
  - Signature: `pub(super) fn symbols_matching_paths(`
  - Purpose: Indexed function `symbols_matching_paths` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:252-272]
- `append_unique_symbols` (function) component `append_unique_symbols [function]` (`021bf360-d2b3-5062-a29f-aaba0c00a4fc`) lines 274-291 [crates/gcode/src/search/fts/common.rs:274-291]
  - Signature: `pub(super) fn append_unique_symbols(`
  - Purpose: Indexed function `append_unique_symbols` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:274-291]
- `query_symbols_by_conditions` (function) component `query_symbols_by_conditions [function]` (`f7d875d0-1c61-5191-8ace-0132624e23a2`) lines 293-341 [crates/gcode/src/search/fts/common.rs:293-341]
  - Signature: `pub(super) fn query_symbols_by_conditions(`
  - Purpose: Indexed function `query_symbols_by_conditions` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:293-341]
- `bm25_score_expression_uses_pdb_score` (function) component `bm25_score_expression_uses_pdb_score [function]` (`0c94647d-0190-534c-ab66-e0696b6a8385`) lines 348-354 [crates/gcode/src/search/fts/common.rs:348-354]
  - Signature: `fn bm25_score_expression_uses_pdb_score() {`
  - Purpose: Indexed function `bm25_score_expression_uses_pdb_score` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:348-354]
- `symbol_bm25_order_uses_pdb_score` (function) component `symbol_bm25_order_uses_pdb_score [function]` (`627e2f5a-6d72-59b1-b259-70253558829d`) lines 357-362 [crates/gcode/src/search/fts/common.rs:357-362]
  - Signature: `fn symbol_bm25_order_uses_pdb_score() {`
  - Purpose: Indexed function `symbol_bm25_order_uses_pdb_score` in `crates/gcode/src/search/fts/common.rs`. [crates/gcode/src/search/fts/common.rs:357-362]

