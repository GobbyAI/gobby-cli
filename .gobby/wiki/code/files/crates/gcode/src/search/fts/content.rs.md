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

# crates/gcode/src/search/fts/content.rs

Module: [[code/modules/crates/gcode/src/search/fts|crates/gcode/src/search/fts]]

## Purpose

`crates/gcode/src/search/fts/content.rs` exposes 12 indexed API symbols.
[crates/gcode/src/search/fts/content.rs:13-21]
[crates/gcode/src/search/fts/content.rs:24-81]
[crates/gcode/src/search/fts/content.rs:83-138]
[crates/gcode/src/search/fts/content.rs:140-178]
[crates/gcode/src/search/fts/content.rs:180-196]
[crates/gcode/src/search/fts/content.rs:199-202]
[crates/gcode/src/search/fts/content.rs:204-210]
[crates/gcode/src/search/fts/content.rs:212-227]
[crates/gcode/src/search/fts/content.rs:229-244]
[crates/gcode/src/search/fts/content.rs:250-253]
[crates/gcode/src/search/fts/content.rs:256-261]
[crates/gcode/src/search/fts/content.rs:264-269]

## API Symbols

- `content_bm25_order_by_sql` (function) component `content_bm25_order_by_sql [function]` (`3468182c-fb0e-5b7c-b068-8f2eb57ea954`) lines 13-21 [crates/gcode/src/search/fts/content.rs:13-21]
  - Signature: `fn content_bm25_order_by_sql(tiebreakers: &[&str]) -> String {`
  - Purpose: Generates a SQL ORDER BY clause that orders results by BM25 search relevance score in descending order, followed by specified tiebreaker columns. [crates/gcode/src/search/fts/content.rs:13-21]
- `search_content` (function) component `search_content [function]` (`179dd1c5-b87f-53fc-a90c-763bdd51a20b`) lines 24-81 [crates/gcode/src/search/fts/content.rs:24-81]
  - Signature: `pub fn search_content(`
  - Purpose: Executes a parameterized PostgreSQL BM25 full-text search on code content chunks, filtered by project ID, optional language, and file paths, returning ranked ContentSearchHit results. [crates/gcode/src/search/fts/content.rs:24-81]
- `search_content_visible` (function) component `search_content_visible [function]` (`7446ca66-ab33-5eff-a2b1-e4b2938026a7`) lines 83-138 [crates/gcode/src/search/fts/content.rs:83-138]
  - Signature: `pub fn search_content_visible(`
  - Purpose: Searches visible code content using PostgreSQL's BM25 full-text search algorithm with optional language and file path filtering, returning ranked ContentSearchHit results up to the specified limit. [crates/gcode/src/search/fts/content.rs:83-138]
- `visible_files_sql` (function) component `visible_files_sql [function]` (`4b716707-ac59-56cf-90a8-cd24217c2bf3`) lines 140-178 [crates/gcode/src/search/fts/content.rs:140-178]
  - Signature: `fn visible_files_sql(ctx: &Context, params: &mut Vec<PgParam>) -> String {`
  - Purpose: Generates a parameterized SQL query that retrieves indexed files with non-tombstone language from either a single project or an overlay project unioned with its parent, with overlay files shadowing parent duplicates. [crates/gcode/src/search/fts/content.rs:140-178]
- `content_hits_from_rows` (function) component `content_hits_from_rows [function]` (`72fa13bb-eabb-5eb1-b8fe-d7db332ec1b3`) lines 180-196 [crates/gcode/src/search/fts/content.rs:180-196]
  - Signature: `fn content_hits_from_rows(rows: &[Row], query: &str) -> Vec<ContentSearchHit> {`
  - Purpose: Converts database rows into a vector of `ContentSearchHit` objects by tokenizing the query string and constructing content snippets with extracted file metadata and line ranges. [crates/gcode/src/search/fts/content.rs:180-196]
- `make_snippet` (function) component `make_snippet [function]` (`648255b9-169c-51d5-a62f-939415961c7f`) lines 199-202 [crates/gcode/src/search/fts/content.rs:199-202]
  - Signature: `pub(super) fn make_snippet(content: &str, query: &str) -> String {`
  - Purpose: This function tokenizes a query string and generates a content snippet using the resulting tokens via `make_snippet_with_tokens`. [crates/gcode/src/search/fts/content.rs:199-202]
- `snippet_tokens` (function) component `snippet_tokens [function]` (`579fd432-ba03-56e4-a645-d3e3cc2b7706`) lines 204-210 [crates/gcode/src/search/fts/content.rs:204-210]
  - Signature: `fn snippet_tokens(query: &str) -> Vec<String> {`
  - Purpose: Tokenizes a query string by splitting on whitespace, converting each token to lowercase, filtering empty strings, and returning the result as a `Vec<String>`. [crates/gcode/src/search/fts/content.rs:204-210]
- `make_snippet_with_tokens` (function) component `make_snippet_with_tokens [function]` (`cd1e698f-50a5-5e42-a7b8-ead4ee7ccce2`) lines 212-227 [crates/gcode/src/search/fts/content.rs:212-227]
  - Signature: `fn make_snippet_with_tokens(content: &str, tokens: &[String]) -> String {`
  - Purpose: Extracts a text snippet around the first case-insensitive occurrence of any provided token, with 60 characters of leading context and up to 120 characters of trailing context. [crates/gcode/src/search/fts/content.rs:212-227]
- `lowercase_with_original_char_map` (function) component `lowercase_with_original_char_map [function]` (`632f29a2-e318-5128-9034-41b5bbff48db`) lines 229-244 [crates/gcode/src/search/fts/content.rs:229-244]
  - Signature: `fn lowercase_with_original_char_map(content: &str) -> (String, Vec<usize>) {`
  - Purpose: Converts a string to lowercase and returns a mapping vector that associates each byte in the lowercased output with the index of its originating character, accommodating Unicode case expansion. [crates/gcode/src/search/fts/content.rs:229-244]
- `assert_uses_pdb_score` (function) component `assert_uses_pdb_score [function]` (`a1573ddd-d8c0-52ea-a258-0425f294c453`) lines 250-253 [crates/gcode/src/search/fts/content.rs:250-253]
  - Signature: `fn assert_uses_pdb_score(sql: &str) {`
  - Purpose: Asserts that the provided SQL string contains `pdb.score(c.id)` and does not contain `pg_search.score`. [crates/gcode/src/search/fts/content.rs:250-253]
- `content_bm25_order_by_uses_pdb_score` (function) component `content_bm25_order_by_uses_pdb_score [function]` (`68e1dadb-848a-5b23-8adb-ba7424a83bff`) lines 256-261 [crates/gcode/src/search/fts/content.rs:256-261]
  - Signature: `fn content_bm25_order_by_uses_pdb_score() {`
  - Purpose: This test function verifies that `content_bm25_order_by_sql` correctly generates a BM25-ordered SQL query with descending PDB score as the primary sort key and ascending column ID as a tiebreaker. [crates/gcode/src/search/fts/content.rs:256-261]
- `visible_content_bm25_order_by_uses_pdb_score` (function) component `visible_content_bm25_order_by_uses_pdb_score [function]` (`758bf97b-7f2d-5b82-953f-9d352043a0d8`) lines 264-269 [crates/gcode/src/search/fts/content.rs:264-269]
  - Signature: `fn visible_content_bm25_order_by_uses_pdb_score() {`
  - Purpose: This test verifies that the BM25 content ordering SQL generator correctly prepends PDB score as the primary descending sort criterion when given secondary sort columns. [crates/gcode/src/search/fts/content.rs:264-269]

