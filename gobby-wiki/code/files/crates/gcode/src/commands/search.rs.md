---
title: crates/gcode/src/commands/search.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/search.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/search.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

`crates/gcode/src/commands/search.rs` exposes 39 indexed API symbols.

## How it fits

`crates/gcode/src/commands/search.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `SearchOptions` | class | 'SearchOptions<'a>' is a parameter bundle for configuring a search query, including pagination ('limit', 'offset'), optional filters by 'kind' and 'language', a path whitelist, output 'format', graph inclusion toggle, and an optional 'token_budget' cap. [crates/gcode/src/commands/search.rs:13-22] |
| `search` | function | Performs a visible symbol search by opening a readonly DB connection, expanding and compiling path filters, fetching candidate results from exact, BM25/full-text, fallback name, and semantic sources with an overfetch budget, and preparing them for merged ranking with degradation tracking, returning 'anyhow::Result<()>'. [crates/gcode/src/commands/search.rs:28-211] |
| `search_symbol` | function | Searches for symbols in the database with optional kind/language/path filters, applies pagination and visibility-aware filtering, and either prints JSON/text results or delegates to graph-based search when 'with_graph' is set. [crates/gcode/src/commands/search.rs:213-303] |
| `SymbolGraphSearchContext` | class | 'SymbolGraphSearchContext<'a>' is a borrowed search-state struct that carries a mutable PostgreSQL client, glob path filters, expanded path strings, and a flag indicating whether visible search is degraded. [crates/gcode/src/commands/search.rs:305-310] |
| `search_symbol_with_graph` | function | Merges exact, graph-boosted, and graph-expanded symbol candidates via reciprocal-rank fusion, resolves visibility and filter constraints, then ranks the surviving symbols by exact-match tier, fused score, and file path. [crates/gcode/src/commands/search.rs:312-416] |
| `search_text` | function | Performs a paginated full-text search over visible results with optional language and path filtering, applies post-filters and diagnostics, computes total counts and hints, and emits the response in the requested format. [crates/gcode/src/commands/search.rs:418-496] |
| `extract_seed_ids` | function | Returns a deduplicated list of non-empty symbol IDs by taking up to 'per_source' IDs from BM25 'fts_results' and then up to 'per_source' canonical semantic IDs, preserving first-seen order. [crates/gcode/src/commands/search.rs:499-522] |
| `search_content` | function | Searches visible full-text content in a readonly database with optional language and path filters, applies post-filtering and pagination, computes a total and hint metadata, emits an empty-result diagnostic if needed, and prints the paged response as JSON or text. [crates/gcode/src/commands/search.rs:524-604] |
| `exact_tier` | function | Returns '0' for an exact case-sensitive match on 'symbol.name' or 'symbol.qualified_name', '1' for a case-insensitive match on either, and '2' otherwise. [crates/gcode/src/commands/search.rs:606-616] |
| `exact_tier_score` | function | 'exact_tier_score' maps the 'exact_tier(query, symbol)' result to a confidence score, returning '1.0' for tier '0', '0.9' for tier '1', and '0.5' for any other tier. [crates/gcode/src/commands/search.rs:618-624] |
| `final_rank_score` | function | Computes the final ranking score by adding the symbol’s exact-tier match score for 'query' to its 'rrf_score'. [crates/gcode/src/commands/search.rs:626-628] |
| `symbol_matches_filters` | function | Returns 'true' only when the symbol’s 'kind' and 'language' match the optional filters, its 'file_path' matches the provided glob patterns, and the path is currently valid according to 'scope::current_indexed_path_is_valid'. [crates/gcode/src/commands/search.rs:630-642] |
| `search_result_matches_filters` | function | Returns 'true' only when the search result’s language matches the optional language filter, its file path matches the provided glob patterns, and the path is still valid in the current indexed scope. [crates/gcode/src/commands/search.rs:644-654] |
| `path_matches_filters` | function | Returns 'true' when no glob patterns are provided or when at least one pattern in 'path_patterns' matches 'file_path', otherwise 'false'. [crates/gcode/src/commands/search.rs:656-658] |
| `filtered_fetch_cap_hint` | function | Returns a formatted hint string indicating that path-filtered search reached 'fts::FILTERED_FETCH_CAP' and that the query or paths should be refined to obtain complete totals. [crates/gcode/src/commands/search.rs:660-665] |
| `path_filter_post_filter_hint` | function | Returns a 'String' explaining that some path filters could not be expressed in SQL, so the results were filtered after fetching a broader candidate set. [crates/gcode/src/commands/search.rs:667-670] |
| `visible_search_degraded_hint` | function | Returns the fixed string '"Visible-project filtering failed; results may be incomplete."' as a 'String'. [crates/gcode/src/commands/search.rs:672-674] |
| `literal_query_hint` | function | Returns 'Some(LITERAL_QUERY_HINT.to_string())' when 'literal_like_query(query)' is true, otherwise returns 'None'. [crates/gcode/src/commands/search.rs:676-678] |
| `literal_like_query` | function | Returns 'true' for a non-empty trimmed query if it contains a quoted literal, call-site syntax, a path separator, or represents a dotted literal; otherwise returns 'false'. [crates/gcode/src/commands/search.rs:680-690] |
| `contains_quoted_literal` | function | Returns 'true' if the query contains a double quote or single quote character, or if it is at least two characters long and both starts and ends with a single quote. [crates/gcode/src/commands/search.rs:692-696] |
| `contains_call_site_syntax` | function | Returns 'true' if 'query' contains a '(' that is not at index 0 and is immediately preceded by an ASCII alphanumeric, '_', '.', or ':', indicating call-site-like syntax. [crates/gcode/src/commands/search.rs:698-709] |
| `contains_path_separator` | function | Returns 'true' if 'query' contains either a forward slash ('/') or a backslash ('\'), otherwise 'false'. [crates/gcode/src/commands/search.rs:711-713] |
| `is_dotted_literal` | function | Returns 'true' exactly when 'query' has at least one '.' , contains no whitespace, and every '.'-separated segment is non-empty and consists only of characters accepted by 'is_dotted_literal_char'. [crates/gcode/src/commands/search.rs:715-723] |
| `is_dotted_literal_char` | function | Returns 'true' if 'ch' is an ASCII alphanumeric character, underscore, or hyphen, and 'false' otherwise. [crates/gcode/src/commands/search.rs:725-727] |

_7 more symbol(s) not shown — run `gcode outline crates/gcode/src/commands/search.rs` for the full list._

_Verified by 8 in-file unit tests._

