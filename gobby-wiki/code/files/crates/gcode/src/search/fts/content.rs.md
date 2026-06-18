---
title: crates/gcode/src/search/fts/content.rs
type: code_file
provenance:
- file: crates/gcode/src/search/fts/content.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/search/fts/content.rs

Module: [[code/modules/crates/gcode/src/search/fts|crates/gcode/src/search/fts]]

## Overview

`crates/gcode/src/search/fts/content.rs` exposes 12 indexed API symbols.

## How it fits

`crates/gcode/src/search/fts/content.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `content_bm25_order_by_sql` | function | Constructs an SQL 'ORDER BY' fragment that sorts by the content BM25 score in descending order for 'c.id', then appends each supplied tiebreaker expression in sequence. [crates/gcode/src/search/fts/content.rs:13-21] |
| `search_content` | function | 'search_content' runs a parameterized BM25/pg_search-backed SQL query over 'code_content_chunks' joined to 'code_indexed_files', filtering by project, optional language, and path list, then returns mapped 'ContentSearchHit' rows up to 'limit', or an empty vector on invalid input, no searchable terms, or query failure. [crates/gcode/src/search/fts/content.rs:24-81] |
| `search_content_visible` | function | Performs a BM25-backed full-text search over visible 'code_content_chunks', optionally filtering by language and paths, ordering by content relevance and stable tie-breakers, and returning parsed 'ContentSearchHit's or an empty vector on invalid input, no searchable terms, or query failure. [crates/gcode/src/search/fts/content.rs:83-138] |
| `visible_files_sql` | function | Builds a parameterized SQL query that returns visible 'file_path'/'project_id' rows from 'code_indexed_files' for either a single project or an overlay project plus inherited parent files not shadowed by the overlay, excluding rows whose 'language' equals 'TOMBSTONE_LANGUAGE'. [crates/gcode/src/search/fts/content.rs:140-178] |
| `content_hits_from_rows` | function | Converts database 'Row' values into 'ContentSearchHit' records by extracting 'content', 'file_path', 'language', and line bounds, generating a token-highlighted snippet from 'query', and skipping any row that fails a required field or type conversion. [crates/gcode/src/search/fts/content.rs:180-196] |
| `make_snippet` | function | Creates a snippet from 'content' by tokenizing 'query' with 'snippet_tokens' and delegating to 'make_snippet_with_tokens' using the resulting token slice. [crates/gcode/src/search/fts/content.rs:199-202] |
| `snippet_tokens` | function | Splits the input string on whitespace, lowercases each token, filters out any empty tokens, and returns the resulting 'Vec<String>'. [crates/gcode/src/search/fts/content.rs:204-210] |
| `make_snippet_with_tokens` | function | Returns a snippet of 'content' by case-insensitively locating the earliest occurrence of any token, mapping that match back to the original character index, and extracting up to 60 characters before and 120 characters after that position (or from the start if no token matches). [crates/gcode/src/search/fts/content.rs:212-227] |
| `lowercase_with_original_char_map` | function | Returns a Unicode-lowercased copy of 'content' and a byte-level mapping from each byte in the lowercased string back to the index of the originating character in the original input, repeating the original character index across any lowercase expansion bytes. [crates/gcode/src/search/fts/content.rs:229-244] |
| `assert_uses_pdb_score` | function | Asserts that the SQL string references 'pdb.score(c.id)' and does not reference 'pg_search.score'. [crates/gcode/src/search/fts/content.rs:250-253] |
| `content_bm25_order_by_uses_pdb_score` | function | Verifies that 'content_bm25_order_by_sql(&["c.id ASC"])' prepends 'pdb.score(c.id) DESC' to the ORDER BY clause and contains a 'pdb.score' call. [crates/gcode/src/search/fts/content.rs:256-261] |
| `visible_content_bm25_order_by_uses_pdb_score` | function | Verifies that 'content_bm25_order_by_sql(&["c.project_id ASC", "c.id ASC"])' prepends 'pdb.score(c.id) DESC' to the ORDER BY clause and that the generated SQL uses 'pdb.score'. [crates/gcode/src/search/fts/content.rs:264-269] |

