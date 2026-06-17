---
title: crates/gcode/src/search/fts/counts.rs
type: code_file
provenance:
- file: crates/gcode/src/search/fts/counts.rs
  ranges:
  - 10-66
  - 69-113
  - 115-146
  - 148-164
  - 166-191
  - 193-243
  - 245-259
  - 261-273
  - 275-294
  - 296-307
  - 309-333
  - 335-359
  - 366-385
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/search/fts/counts.rs:10-66](crates/gcode/src/search/fts/counts.rs#L10-L66), [crates/gcode/src/search/fts/counts.rs:69-113](crates/gcode/src/search/fts/counts.rs#L69-L113), [crates/gcode/src/search/fts/counts.rs:115-146](crates/gcode/src/search/fts/counts.rs#L115-L146), [crates/gcode/src/search/fts/counts.rs:148-164](crates/gcode/src/search/fts/counts.rs#L148-L164), [crates/gcode/src/search/fts/counts.rs:166-191](crates/gcode/src/search/fts/counts.rs#L166-L191), [crates/gcode/src/search/fts/counts.rs:193-243](crates/gcode/src/search/fts/counts.rs#L193-L243), [crates/gcode/src/search/fts/counts.rs:245-259](crates/gcode/src/search/fts/counts.rs#L245-L259), [crates/gcode/src/search/fts/counts.rs:261-273](crates/gcode/src/search/fts/counts.rs#L261-L273), [crates/gcode/src/search/fts/counts.rs:275-294](crates/gcode/src/search/fts/counts.rs#L275-L294), [crates/gcode/src/search/fts/counts.rs:296-307](crates/gcode/src/search/fts/counts.rs#L296-L307), [crates/gcode/src/search/fts/counts.rs:309-333](crates/gcode/src/search/fts/counts.rs#L309-L333), [crates/gcode/src/search/fts/counts.rs:335-359](crates/gcode/src/search/fts/counts.rs#L335-L359), [crates/gcode/src/search/fts/counts.rs:366-385](crates/gcode/src/search/fts/counts.rs#L366-L385)

</details>

# crates/gcode/src/search/fts/counts.rs

Module: [[code/modules/crates/gcode/src/search/fts|crates/gcode/src/search/fts]]

## Purpose

This file implements PostgreSQL-backed count queries for search results over symbols, content chunks, and visible project files. `count_text` and `count_content` sanitize the user query into pg_search/BM25 terms, build SQL predicates from symbol/content filters, and either run a direct `COUNT(*)` query or fall back to a file-path row count when path filtering has to be applied post-query. The helper functions split the filtering work: `push_pg_regex_path_filter` and `glob_to_pg_regex` translate glob path constraints into PostgreSQL regex conditions, `push_content_filters` and `count_visible_content_by_conditions` build and execute content-count predicates, and `count_visible_symbols_by_conditions`, `count_symbols_fts_visible`, `count_text_visible`, and `count_content_visible` are the visible-result variants that combine project, language, and path restrictions into count queries.
[crates/gcode/src/search/fts/counts.rs:10-66]
[crates/gcode/src/search/fts/counts.rs:69-113]
[crates/gcode/src/search/fts/counts.rs:115-146]
[crates/gcode/src/search/fts/counts.rs:148-164]
[crates/gcode/src/search/fts/counts.rs:166-191]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `count_text` | function | `pub fn count_text(` | `count_text [function]` | `96b90155-4bc1-5422-9216-4edffe1168c7` | 10-66 [crates/gcode/src/search/fts/counts.rs:10-66] | Indexed function `count_text` in `crates/gcode/src/search/fts/counts.rs`. [crates/gcode/src/search/fts/counts.rs:10-66] |
| `count_content` | function | `pub fn count_content(` | `count_content [function]` | `2db20335-3547-5506-bdc9-a382173a22f6` | 69-113 [crates/gcode/src/search/fts/counts.rs:69-113] | Indexed function `count_content` in `crates/gcode/src/search/fts/counts.rs`. [crates/gcode/src/search/fts/counts.rs:69-113] |
| `count_visible_symbols_by_conditions` | function | `fn count_visible_symbols_by_conditions(` | `count_visible_symbols_by_conditions [function]` | `0d0fec52-b764-59a1-8b21-62c58911c683` | 115-146 [crates/gcode/src/search/fts/counts.rs:115-146] | Indexed function `count_visible_symbols_by_conditions` in `crates/gcode/src/search/fts/counts.rs`. [crates/gcode/src/search/fts/counts.rs:115-146] |
| `count_symbol_file_path_rows` | function | `fn count_symbol_file_path_rows(` | `count_symbol_file_path_rows [function]` | `8e85ae6a-f520-5f17-afd9-754b8de3432f` | 148-164 [crates/gcode/src/search/fts/counts.rs:148-164] | Indexed function `count_symbol_file_path_rows` in `crates/gcode/src/search/fts/counts.rs`. [crates/gcode/src/search/fts/counts.rs:148-164] |
| `push_pg_regex_path_filter` | function | `fn push_pg_regex_path_filter(` | `push_pg_regex_path_filter [function]` | `bd9b91b7-a8f6-5c63-a256-05af4bf9efca` | 166-191 [crates/gcode/src/search/fts/counts.rs:166-191] | Indexed function `push_pg_regex_path_filter` in `crates/gcode/src/search/fts/counts.rs`. [crates/gcode/src/search/fts/counts.rs:166-191] |
| `glob_to_pg_regex` | function | `fn glob_to_pg_regex(pattern: &str) -> Option<String> {` | `glob_to_pg_regex [function]` | `baedf168-7509-5fc4-b62e-47be6ec62ace` | 193-243 [crates/gcode/src/search/fts/counts.rs:193-243] | Indexed function `glob_to_pg_regex` in `crates/gcode/src/search/fts/counts.rs`. [crates/gcode/src/search/fts/counts.rs:193-243] |
| `count_symbols_fts_visible` | function | `fn count_symbols_fts_visible(` | `count_symbols_fts_visible [function]` | `d3ee1ca5-ab0b-56bc-931e-148ce45b4a3e` | 245-259 [crates/gcode/src/search/fts/counts.rs:245-259] | Indexed function `count_symbols_fts_visible` in `crates/gcode/src/search/fts/counts.rs`. [crates/gcode/src/search/fts/counts.rs:245-259] |
| `push_content_filters` | function | `fn push_content_filters(` | `push_content_filters [function]` | `23214880-b18a-5115-928e-c8df175c75cc` | 261-273 [crates/gcode/src/search/fts/counts.rs:261-273] | Indexed function `push_content_filters` in `crates/gcode/src/search/fts/counts.rs`. [crates/gcode/src/search/fts/counts.rs:261-273] |
| `count_visible_content_by_conditions` | function | `fn count_visible_content_by_conditions(` | `count_visible_content_by_conditions [function]` | `bc13a11f-4797-55ab-96a8-f7c8e4eb57e2` | 275-294 [crates/gcode/src/search/fts/counts.rs:275-294] | Indexed function `count_visible_content_by_conditions` in `crates/gcode/src/search/fts/counts.rs`. [crates/gcode/src/search/fts/counts.rs:275-294] |
| `count_content_bm25_visible` | function | `fn count_content_bm25_visible(` | `count_content_bm25_visible [function]` | `36b6335a-ba3c-5adf-bbdd-5cce7c9bf895` | 296-307 [crates/gcode/src/search/fts/counts.rs:296-307] | Indexed function `count_content_bm25_visible` in `crates/gcode/src/search/fts/counts.rs`. [crates/gcode/src/search/fts/counts.rs:296-307] |
| `count_text_visible` | function | `pub fn count_text_visible(` | `count_text_visible [function]` | `23475bad-2efa-5961-a13d-5721256c2451` | 309-333 [crates/gcode/src/search/fts/counts.rs:309-333] | Indexed function `count_text_visible` in `crates/gcode/src/search/fts/counts.rs`. [crates/gcode/src/search/fts/counts.rs:309-333] |
| `count_content_visible` | function | `pub fn count_content_visible(` | `count_content_visible [function]` | `4caa4356-8cdc-53b0-9188-cb53dd79e859` | 335-359 [crates/gcode/src/search/fts/counts.rs:335-359] | Indexed function `count_content_visible` in `crates/gcode/src/search/fts/counts.rs`. [crates/gcode/src/search/fts/counts.rs:335-359] |
| `glob_to_pg_regex_anchors_and_escapes_patterns` | function | `fn glob_to_pg_regex_anchors_and_escapes_patterns() {` | `glob_to_pg_regex_anchors_and_escapes_patterns [function]` | `12d3a313-a917-5b4b-a086-596f05d19f5e` | 366-385 [crates/gcode/src/search/fts/counts.rs:366-385] | Indexed function `glob_to_pg_regex_anchors_and_escapes_patterns` in `crates/gcode/src/search/fts/counts.rs`. [crates/gcode/src/search/fts/counts.rs:366-385] |
