---
title: crates/gcode/src/search/fts/content.rs
type: code_file
provenance:
- file: crates/gcode/src/search/fts/content.rs
  ranges:
  - 13-21
  - 24-81
  - 83-138
  - 140-178
  - 180-196
  - 199-202
  - 204-210
  - 212-227
  - 229-244
  - 250-253
  - 256-261
  - 264-269
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/search/fts/content.rs:13-21](crates/gcode/src/search/fts/content.rs#L13-L21), [crates/gcode/src/search/fts/content.rs:24-81](crates/gcode/src/search/fts/content.rs#L24-L81), [crates/gcode/src/search/fts/content.rs:83-138](crates/gcode/src/search/fts/content.rs#L83-L138), [crates/gcode/src/search/fts/content.rs:140-178](crates/gcode/src/search/fts/content.rs#L140-L178), [crates/gcode/src/search/fts/content.rs:180-196](crates/gcode/src/search/fts/content.rs#L180-L196), [crates/gcode/src/search/fts/content.rs:199-202](crates/gcode/src/search/fts/content.rs#L199-L202), [crates/gcode/src/search/fts/content.rs:204-210](crates/gcode/src/search/fts/content.rs#L204-L210), [crates/gcode/src/search/fts/content.rs:212-227](crates/gcode/src/search/fts/content.rs#L212-L227), [crates/gcode/src/search/fts/content.rs:229-244](crates/gcode/src/search/fts/content.rs#L229-L244), [crates/gcode/src/search/fts/content.rs:250-253](crates/gcode/src/search/fts/content.rs#L250-L253), [crates/gcode/src/search/fts/content.rs:256-261](crates/gcode/src/search/fts/content.rs#L256-L261), [crates/gcode/src/search/fts/content.rs:264-269](crates/gcode/src/search/fts/content.rs#L264-L269)

</details>

# crates/gcode/src/search/fts/content.rs

Module: [[code/modules/crates/gcode/src/search/fts|crates/gcode/src/search/fts]]

## Purpose

This file builds the SQL and post-processing for full-text search over indexed file content. It defines the BM25 `ORDER BY` helper, runs content searches with project/language/path filters, and has a visibility-aware variant that restricts results to files allowed by the current scope. It then converts returned rows into `ContentSearchHit` values and constructs highlighted snippets by tokenizing, lowercasing with a character map, and reusing those tokens to extract snippet text. The last functions are test helpers that assert the generated BM25 ordering uses the expected `pdb_score` expression.
[crates/gcode/src/search/fts/content.rs:13-21]
[crates/gcode/src/search/fts/content.rs:24-81]
[crates/gcode/src/search/fts/content.rs:83-138]
[crates/gcode/src/search/fts/content.rs:140-178]
[crates/gcode/src/search/fts/content.rs:180-196]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `content_bm25_order_by_sql` | function | `fn content_bm25_order_by_sql(tiebreakers: &[&str]) -> String {` | `content_bm25_order_by_sql [function]` | `3468182c-fb0e-5b7c-b068-8f2eb57ea954` | 13-21 [crates/gcode/src/search/fts/content.rs:13-21] | Indexed function `content_bm25_order_by_sql` in `crates/gcode/src/search/fts/content.rs`. [crates/gcode/src/search/fts/content.rs:13-21] |
| `search_content` | function | `pub fn search_content(` | `search_content [function]` | `179dd1c5-b87f-53fc-a90c-763bdd51a20b` | 24-81 [crates/gcode/src/search/fts/content.rs:24-81] | Indexed function `search_content` in `crates/gcode/src/search/fts/content.rs`. [crates/gcode/src/search/fts/content.rs:24-81] |
| `search_content_visible` | function | `pub fn search_content_visible(` | `search_content_visible [function]` | `7446ca66-ab33-5eff-a2b1-e4b2938026a7` | 83-138 [crates/gcode/src/search/fts/content.rs:83-138] | Indexed function `search_content_visible` in `crates/gcode/src/search/fts/content.rs`. [crates/gcode/src/search/fts/content.rs:83-138] |
| `visible_files_sql` | function | `fn visible_files_sql(ctx: &Context, params: &mut Vec<PgParam>) -> String {` | `visible_files_sql [function]` | `4b716707-ac59-56cf-90a8-cd24217c2bf3` | 140-178 [crates/gcode/src/search/fts/content.rs:140-178] | Indexed function `visible_files_sql` in `crates/gcode/src/search/fts/content.rs`. [crates/gcode/src/search/fts/content.rs:140-178] |
| `content_hits_from_rows` | function | `fn content_hits_from_rows(rows: &[Row], query: &str) -> Vec<ContentSearchHit> {` | `content_hits_from_rows [function]` | `72fa13bb-eabb-5eb1-b8fe-d7db332ec1b3` | 180-196 [crates/gcode/src/search/fts/content.rs:180-196] | Indexed function `content_hits_from_rows` in `crates/gcode/src/search/fts/content.rs`. [crates/gcode/src/search/fts/content.rs:180-196] |
| `make_snippet` | function | `pub(super) fn make_snippet(content: &str, query: &str) -> String {` | `make_snippet [function]` | `648255b9-169c-51d5-a62f-939415961c7f` | 199-202 [crates/gcode/src/search/fts/content.rs:199-202] | Indexed function `make_snippet` in `crates/gcode/src/search/fts/content.rs`. [crates/gcode/src/search/fts/content.rs:199-202] |
| `snippet_tokens` | function | `fn snippet_tokens(query: &str) -> Vec<String> {` | `snippet_tokens [function]` | `579fd432-ba03-56e4-a645-d3e3cc2b7706` | 204-210 [crates/gcode/src/search/fts/content.rs:204-210] | Indexed function `snippet_tokens` in `crates/gcode/src/search/fts/content.rs`. [crates/gcode/src/search/fts/content.rs:204-210] |
| `make_snippet_with_tokens` | function | `fn make_snippet_with_tokens(content: &str, tokens: &[String]) -> String {` | `make_snippet_with_tokens [function]` | `cd1e698f-50a5-5e42-a7b8-ead4ee7ccce2` | 212-227 [crates/gcode/src/search/fts/content.rs:212-227] | Indexed function `make_snippet_with_tokens` in `crates/gcode/src/search/fts/content.rs`. [crates/gcode/src/search/fts/content.rs:212-227] |
| `lowercase_with_original_char_map` | function | `fn lowercase_with_original_char_map(content: &str) -> (String, Vec<usize>) {` | `lowercase_with_original_char_map [function]` | `632f29a2-e318-5128-9034-41b5bbff48db` | 229-244 [crates/gcode/src/search/fts/content.rs:229-244] | Indexed function `lowercase_with_original_char_map` in `crates/gcode/src/search/fts/content.rs`. [crates/gcode/src/search/fts/content.rs:229-244] |
| `assert_uses_pdb_score` | function | `fn assert_uses_pdb_score(sql: &str) {` | `assert_uses_pdb_score [function]` | `a1573ddd-d8c0-52ea-a258-0425f294c453` | 250-253 [crates/gcode/src/search/fts/content.rs:250-253] | Indexed function `assert_uses_pdb_score` in `crates/gcode/src/search/fts/content.rs`. [crates/gcode/src/search/fts/content.rs:250-253] |
| `content_bm25_order_by_uses_pdb_score` | function | `fn content_bm25_order_by_uses_pdb_score() {` | `content_bm25_order_by_uses_pdb_score [function]` | `68e1dadb-848a-5b23-8adb-ba7424a83bff` | 256-261 [crates/gcode/src/search/fts/content.rs:256-261] | Indexed function `content_bm25_order_by_uses_pdb_score` in `crates/gcode/src/search/fts/content.rs`. [crates/gcode/src/search/fts/content.rs:256-261] |
| `visible_content_bm25_order_by_uses_pdb_score` | function | `fn visible_content_bm25_order_by_uses_pdb_score() {` | `visible_content_bm25_order_by_uses_pdb_score [function]` | `758bf97b-7f2d-5b82-953f-9d352043a0d8` | 264-269 [crates/gcode/src/search/fts/content.rs:264-269] | Indexed function `visible_content_bm25_order_by_uses_pdb_score` in `crates/gcode/src/search/fts/content.rs`. [crates/gcode/src/search/fts/content.rs:264-269] |
