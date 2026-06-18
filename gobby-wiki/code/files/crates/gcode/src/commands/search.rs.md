---
title: crates/gcode/src/commands/search.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/search.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/src/commands/search.rs

Module: [[code/modules/crates/gcode/src/commands|crates/gcode/src/commands]]

## Overview

## How it fits

This file acts as the command-layer controller for searching within the `crates/gcode/src/commands/` module. It interacts directly with the database layer to execute searches and retrieves settings via the `Context` [crates/gcode/src/commands/search.rs:13] configuration. It relies on the database wrapper `db`  to establish connections, such as in `db::connect_readonly` [crates/gcode/src/commands/search.rs:28].

Data flows into this file via `SearchOptions` [crates/gcode/src/commands/search.rs:13-22], which encapsulates pagination limits, offsets, language/kind filters, and path whitelists. The search processes use the `fts` module  to expand path lists and compile glob patterns. They then fetch candidate results from the PostgreSQL database using BM25, and optional graph databases or semantic indices.

## Key components

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
| `print_search_warning` | function | Prints 'warning: {hint}' to standard error only when 'hint' is 'Some' and 'ctx.quiet' is false. [crates/gcode/src/commands/search.rs:729-735] |
| `format_search_result_line` | function | Formats a 'SearchResult' into a single display line containing its file path, starting line, kind, qualified name, score to four decimal places, and joined source list (or empty string if absent). [crates/gcode/src/commands/search.rs:737-752] |
| `format_symbol_lookup_text` | function | Returns a formatted single-line lookup string containing the symbol’s file path, line range, kind, qualified name, and id, optionally appending 'sig=<signature>' when a non-empty signature is present. [crates/gcode/src/commands/search.rs:754-769] |
| `compact_snippet` | function | 'compact_snippet' normalizes a string by removing all extra whitespace and joining the whitespace-delimited tokens with single ASCII spaces. [crates/gcode/src/commands/search.rs:771-773] |
| `print_empty_diagnostic` | function | Prints a quiet-suppressed diagnostic to stderr only when 'is_empty' is true, emitting a project-index warning at offset 0 without an identity file, an offset-specific no-results message when 'offset > 0', or a generic “No results.” otherwise. [crates/gcode/src/commands/search.rs:775-786] |
| `print_pagination_hint` | function | Prints a pagination hint to stderr showing 'result_count' of 'total' results and the next '--offset' value, but only when more results remain beyond 'offset + result_count'. [crates/gcode/src/commands/search.rs:788-797] |
| `symbol` | function | Constructs and returns a 'Symbol' with fixed placeholder metadata and default ranges, filling 'file_path', 'kind', and 'language' from the arguments while leaving optional fields unset and string fields empty or hardcoded. [crates/gcode/src/commands/search.rs:803-824] |
| `symbol_filter_rejects_language_kind_path_and_missing_disk_file` | function | Verifies that a symbol filter excludes a symbol when its kind, language, or file-path glob do not match the expected criteria, including the case where the referenced file is missing on disk. [crates/gcode/src/commands/search.rs:827-838] |
| `exact_tier_prefers_case_sensitive_match` | function | Verifies that 'exact_tier' ranks a case-sensitive exact name match as tier '0', a case-insensitive exact match as tier '1', and a matching prefix/subsequence variant like 'outline_helper' as tier '2'. [crates/gcode/src/commands/search.rs:841-855] |
| `final_score_preserves_display_tier_before_rrf_score` | function | Verifies that 'final_rank_score' ranks an exact symbol match with a better display tier above a fuzzy match even when the fuzzy candidate has a higher reciprocal-rank-factor score. [crates/gcode/src/commands/search.rs:858-867] |
| `combines_fetch_cap_and_path_post_filter_hints` | function | Verifies that 'token_budget::combine_hints' merges a filtered fetch-cap hint with a path-filter post-filter hint into a combined hint string containing both “fetch cap” and “post-filtered”. [crates/gcode/src/commands/search.rs:870-879] |
| `search_result_token_budget_uses_text_row_estimate` | function | Verifies that 'trim_results' uses the token estimate of a formatted search-result row to keep exactly one result under the budget and emits a refinement hint indicating “1 of 2 results” with '--kind', '--language', and 'PATH' filters. [crates/gcode/src/commands/search.rs:882-904] |
| `literal_query_hint_detects_literal_like_queries` | function | This test verifies that 'literal_query_hint' returns a hint for several literal-like queries and that each hint contains both 'gcode grep' and 'search-content'. [crates/gcode/src/commands/search.rs:907-918] |
| `literal_query_hint_skips_natural_language_queries` | function | Verifies that 'literal_query_hint' returns 'None' for the natural-language phrase '"database connection pool"'. [crates/gcode/src/commands/search.rs:921-923] |
| `content_snippet_compaction_collapses_whitespace` | function | Verifies that 'compact_snippet' trims leading/trailing whitespace and normalizes internal whitespace sequences, including spaces, tabs, and newlines, into single spaces. [crates/gcode/src/commands/search.rs:926-931] |

