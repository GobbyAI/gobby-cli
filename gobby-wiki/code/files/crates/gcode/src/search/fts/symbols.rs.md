---
title: crates/gcode/src/search/fts/symbols.rs
type: code_file
provenance:
- file: crates/gcode/src/search/fts/symbols.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/search/fts/symbols.rs

Module: [[code/modules/crates/gcode/src/search/fts|crates/gcode/src/search/fts]]

## Overview

`crates/gcode/src/search/fts/symbols.rs` exposes 12 indexed API symbols.

## How it fits

`crates/gcode/src/search/fts/symbols.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `VisibleSearchOutcome` | class | 'VisibleSearchOutcome<T>' is a generic result container holding a vector of search results of type 'T' plus a 'degraded' flag indicating whether the search operated in a degraded mode. [crates/gcode/src/search/fts/symbols.rs:15-18] |
| `ok` | function | Constructs a new 'Self' instance with the provided 'results' vector and sets 'degraded' to 'false'. [crates/gcode/src/search/fts/symbols.rs:21-26] |
| `degraded` | function | Constructs and returns a 'Self' instance with the given 'results' vector and the 'degraded' flag set to 'true'. [crates/gcode/src/search/fts/symbols.rs:28-33] |
| `search_symbols_fts` | function | Sanitizes a full-text query, returns an empty vector for empty input or zero limit, then searches symbols in the specified project by BM25 match against 'name', 'qualified_name', 'signature', 'docstring', and 'summary', applying optional 'kind', 'language', and path filters and ordering results by BM25 score. [crates/gcode/src/search/fts/symbols.rs:36-73] |
| `search_symbols_by_name` | function | Returns up to 'limit' symbols for a given 'project_id' whose 'name' or 'qualified_name' contains 'query' as an escaped SQL 'LIKE' substring, delegating the filtered, name-ordered lookup to 'query_symbols_by_conditions' with optional 'kind', 'language', and 'paths' constraints. [crates/gcode/src/search/fts/symbols.rs:76-112] |
| `search_symbols_exact_first` | function | Searches symbols within a project by returning exact and case-insensitive exact matches first, then prefix matches, then falling back to broader name search, while applying optional kind/language/path filters, deduplicating results, and enforcing the requested limit. [crates/gcode/src/search/fts/symbols.rs:114-190] |
| `search_symbols_fts_visible` | function | Sanitizes the input query for PostgreSQL full-text search, returns an empty visible search result if the query is blank or 'limit' is zero, and otherwise searches visible symbols where any of 'name', 'qualified_name', 'signature', 'docstring', or 'summary' matches the BM25 query, applying optional kind/language/path filters and ordering by BM25 score. [crates/gcode/src/search/fts/symbols.rs:192-225] |
| `search_symbols_by_name_visible` | function | Returns visible symbols whose 'name' or 'qualified_name' contains the escaped 'query' substring, applying optional 'kind', 'language', and 'paths' filters, ordering by name, and yielding an empty result immediately for blank queries or zero 'limit'. [crates/gcode/src/search/fts/symbols.rs:227-260] |
| `search_symbols_exact_first_visible` | function | Searches visible symbols with optional kind/language/path filters by returning exact name or qualified-name matches first, then prefix matches, deduplicating results up to 'limit' while propagating any degraded-query flags. [crates/gcode/src/search/fts/symbols.rs:262-337] |
| `query_visible_symbols_by_conditions` | function | Queries symbols constrained to the current context’s visible project IDs, fetches up to 'limit.max(FILTERED_FETCH_CAP)', applies a visibility filter against the database, truncates to 'limit', and returns an empty or degraded 'VisibleSearchOutcome' if there are no visible projects, 'limit == 0', or filtering fails. [crates/gcode/src/search/fts/symbols.rs:339-371] |
| `search_text` | function | 'search_text' performs a full-text symbol search by delegating to 'search_symbols_fts' with the given query, project, optional language, path filters, and limit, then converts each returned symbol into a brief 'SearchResult' and returns the collected vector. [crates/gcode/src/search/fts/symbols.rs:374-386] |
| `search_text_visible` | function | Runs a visible full-text symbol search via 'search_symbols_fts_visible' and returns a 'VisibleSearchOutcome<SearchResult>' whose results are converted to brief form while preserving the 'degraded' flag. [crates/gcode/src/search/fts/symbols.rs:388-401] |

