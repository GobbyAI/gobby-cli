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

# crates/gcode/src/search/fts/counts.rs

Module: [[code/modules/crates/gcode/src/search/fts|crates/gcode/src/search/fts]]

## Purpose

`crates/gcode/src/search/fts/counts.rs` exposes 13 indexed API symbols.
[crates/gcode/src/search/fts/counts.rs:10-66]
[crates/gcode/src/search/fts/counts.rs:69-113]
[crates/gcode/src/search/fts/counts.rs:115-146]
[crates/gcode/src/search/fts/counts.rs:148-164]
[crates/gcode/src/search/fts/counts.rs:166-191]

## API Symbols

- `count_text` (function) component `count_text [function]` (`96b90155-4bc1-5422-9216-4edffe1168c7`) lines 10-66 [crates/gcode/src/search/fts/counts.rs:10-66]
  - Signature: `pub fn count_text(`
  - Purpose: This function returns the count of code symbols matching a BM25 full-text search query against multiple symbol metadata fields (name, qualified name, signature, docstring, summary), filtered by project ID, language, and file paths using PostgreSQL full-text search. [crates/gcode/src/search/fts/counts.rs:10-66]
- `count_content` (function) component `count_content [function]` (`2db20335-3547-5506-bdc9-a382173a22f6`) lines 69-113 [crates/gcode/src/search/fts/counts.rs:69-113]
  - Signature: `pub fn count_content(`
  - Purpose: Counts code content chunks matching a BM25 full-text search query, filtered by project ID, optional language, and file paths in a PostgreSQL database. [crates/gcode/src/search/fts/counts.rs:69-113]
- `count_visible_symbols_by_conditions` (function) component `count_visible_symbols_by_conditions [function]` (`0d0fec52-b764-59a1-8b21-62c58911c683`) lines 115-146 [crates/gcode/src/search/fts/counts.rs:115-146]
  - Signature: `fn count_visible_symbols_by_conditions(`
  - Purpose: Counts code symbols matching specified language and file path filters that are visible to the current project context, using either direct SQL aggregation or post-processed path filtering. [crates/gcode/src/search/fts/counts.rs:115-146]
- `count_symbol_file_path_rows` (function) component `count_symbol_file_path_rows [function]` (`8e85ae6a-f520-5f17-afd9-754b8de3432f`) lines 148-164 [crates/gcode/src/search/fts/counts.rs:148-164]
  - Signature: `fn count_symbol_file_path_rows(`
  - Purpose: Counts code symbol records filtered by specified file paths and additional SQL conditions via a parameterized PostgreSQL query against the code_symbols and code_indexed_files tables. [crates/gcode/src/search/fts/counts.rs:148-164]
- `push_pg_regex_path_filter` (function) component `push_pg_regex_path_filter [function]` (`bd9b91b7-a8f6-5c63-a256-05af4bf9efca`) lines 166-191 [crates/gcode/src/search/fts/counts.rs:166-191]
  - Signature: `fn push_pg_regex_path_filter(`
  - Purpose: Appends a parameterized PostgreSQL WHERE condition that filters rows where a file_path column matches any of the supplied glob patterns converted to regular expressions using the `~ ANY()` operator. [crates/gcode/src/search/fts/counts.rs:166-191]
- `glob_to_pg_regex` (function) component `glob_to_pg_regex [function]` (`baedf168-7509-5fc4-b62e-47be6ec62ace`) lines 193-243 [crates/gcode/src/search/fts/counts.rs:193-243]
  - Signature: `fn glob_to_pg_regex(pattern: &str) -> Option<String> {`
  - Purpose: Converts a glob pattern to an anchored PostgreSQL regular expression by mapping path wildcards (`*` → `[^/]*`, `**` → `.*`, `?` → `[^/]`) and bracket character classes while escaping regex metacharacters, or returns `None` if a bracket class is unclosed. [crates/gcode/src/search/fts/counts.rs:193-243]
- `count_symbols_fts_visible` (function) component `count_symbols_fts_visible [function]` (`d3ee1ca5-ab0b-56bc-931e-148ce45b4a3e`) lines 245-259 [crates/gcode/src/search/fts/counts.rs:245-259]
  - Signature: `fn count_symbols_fts_visible(`
  - Purpose: Counts visible code symbols matching a BM25 full-text search query across multiple symbol attributes (name, qualified_name, signature, docstring, summary), filtered by context, language, and file paths. [crates/gcode/src/search/fts/counts.rs:245-259]
- `push_content_filters` (function) component `push_content_filters [function]` (`23214880-b18a-5115-928e-c8df175c75cc`) lines 261-273 [crates/gcode/src/search/fts/counts.rs:261-273]
  - Signature: `fn push_content_filters(`
  - Purpose: Appends SQL WHERE clause conditions and PostgreSQL parameters to filter content by optional language and provided file paths. [crates/gcode/src/search/fts/counts.rs:261-273]
- `count_visible_content_by_conditions` (function) component `count_visible_content_by_conditions [function]` (`bc13a11f-4797-55ab-96a8-f7c8e4eb57e2`) lines 275-294 [crates/gcode/src/search/fts/counts.rs:275-294]
  - Signature: `fn count_visible_content_by_conditions(`
  - Purpose: Counts code content chunks visible to the current context that match provided conditions, language filters, and file paths via a SQL JOIN query. [crates/gcode/src/search/fts/counts.rs:275-294]
- `count_content_bm25_visible` (function) component `count_content_bm25_visible [function]` (`36b6335a-ba3c-5adf-bbdd-5cce7c9bf895`) lines 296-307 [crates/gcode/src/search/fts/counts.rs:296-307]
  - Signature: `fn count_content_bm25_visible(`
  - Purpose: This function executes a BM25 full-text search query against visible PostgreSQL content filtered by context, language, and file paths, returning the count of matching records. [crates/gcode/src/search/fts/counts.rs:296-307]
- `count_text_visible` (function) component `count_text_visible [function]` (`23475bad-2efa-5961-a13d-5721256c2451`) lines 309-333 [crates/gcode/src/search/fts/counts.rs:309-333]
  - Signature: `pub fn count_text_visible(`
  - Purpose: Counts visible symbols matching a sanitized PostgreSQL BM25 full-text search query across specified file paths and optional language filter, with error handling. [crates/gcode/src/search/fts/counts.rs:309-333]
- `count_content_visible` (function) component `count_content_visible [function]` (`4caa4356-8cdc-53b0-9188-cb53dd79e859`) lines 335-359 [crates/gcode/src/search/fts/counts.rs:335-359]
  - Signature: `pub fn count_content_visible(`
  - Purpose: Counts visible content matching a BM25 full-text search query against a PostgreSQL database, sanitizing the input and returning zero for invalid queries or search failures. [crates/gcode/src/search/fts/counts.rs:335-359]
- `glob_to_pg_regex_anchors_and_escapes_patterns` (function) component `glob_to_pg_regex_anchors_and_escapes_patterns [function]` (`12d3a313-a917-5b4b-a086-596f05d19f5e`) lines 366-385 [crates/gcode/src/search/fts/counts.rs:366-385]
  - Signature: `fn glob_to_pg_regex_anchors_and_escapes_patterns() {`
  - Purpose: This test function verifies that `glob_to_pg_regex` correctly converts POSIX glob patterns into anchored PostgreSQL regular expressions with proper escape handling, wildcard expansion (`*` and `?`), recursive directory matching (`**`), and invalid pattern detection. [crates/gcode/src/search/fts/counts.rs:366-385]

