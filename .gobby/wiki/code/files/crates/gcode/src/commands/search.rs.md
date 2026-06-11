---
title: crates/gcode/src/commands/search.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/search.rs
  ranges:
  - 13-21
  - 25-200
  - 202-292
  - 294-299
  - 301-405
  - 407-485
  - 488-511
  - 513-593
  - 595-605
  - 607-613
  - 615-617
  - 619-631
  - 633-643
  - 645-647
  - 649-654
  - 656-659
  - 661-663
  - 665-667
  - 669-679
  - 681-685
  - 687-698
  - 700-702
  - 704-712
  - 714-716
  - 718-725
  - 727-733
  - 735-750
  - 752-754
  - 756-767
  - 769-778
  - 784-805
  - 808-819
  - 822-836
  - 839-848
  - 851-860
  - 863-874
  - 877-879
  - 882-887
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/search.rs

Module: [[code/modules/crates/gcode/src/commands|crates/gcode/src/commands]]

## Purpose

`crates/gcode/src/commands/search.rs` exposes 38 indexed API symbols.
[crates/gcode/src/commands/search.rs:13-21]
[crates/gcode/src/commands/search.rs:25-200]
[crates/gcode/src/commands/search.rs:202-292]
[crates/gcode/src/commands/search.rs:294-299]
[crates/gcode/src/commands/search.rs:301-405]

## API Symbols

- `SearchOptions` (class) component `SearchOptions [class]` (`aa4212ee-e929-5006-96a2-b59bc3ee2286`) lines 13-21 [crates/gcode/src/commands/search.rs:13-21]
  - Signature: `pub struct SearchOptions<'a> {`
  - Purpose: SearchOptions<'a> configures a search operation with pagination parameters (limit/offset), optional kind and language filters, target paths, output format, and a boolean flag for graph inclusion. [crates/gcode/src/commands/search.rs:13-21]
- `search` (function) component `search [function]` (`6ef435c9-dafa-51d5-9b0d-b55d16ced45a`) lines 25-200 [crates/gcode/src/commands/search.rs:25-200]
  - Signature: `pub fn search(ctx: &Context, query: &str, options: SearchOptions<'_>) -> anyhow::Result<()> {`
  - Purpose: Searches code symbols by merging results from exact matching, BM25 full-text indexing, and Qdrant semantic embeddings using reciprocal rank fusion with visibility-based filtering. [crates/gcode/src/commands/search.rs:25-200]
- `search_symbol` (function) component `search_symbol [function]` (`74908035-4858-5737-977e-a580cce813d4`) lines 202-292 [crates/gcode/src/commands/search.rs:202-292]
  - Signature: `pub fn search_symbol(ctx: &Context, query: &str, options: SearchOptions<'_>) -> anyhow::Result<()> {`
  - Purpose: Executes a full-text symbol database search with exact-match prioritization, multi-criteria filtering (paths, kind, language), optional graph enrichment, and paginated result formatting. [crates/gcode/src/commands/search.rs:202-292]
- `SymbolGraphSearchContext` (class) component `SymbolGraphSearchContext [class]` (`889b6e00-6968-54ad-8fb3-3b1fed6a3870`) lines 294-299 [crates/gcode/src/commands/search.rs:294-299]
  - Signature: `struct SymbolGraphSearchContext<'a> {`
  - Purpose: A borrowed context struct encapsulating a mutable PostgreSQL client connection, glob path patterns, expanded paths, and a boolean flag indicating degraded search visibility for symbol graph queries. [crates/gcode/src/commands/search.rs:294-299]
- `search_symbol_with_graph` (function) component `search_symbol_with_graph [function]` (`379056cb-d5a1-5a5b-8a61-cac91578453e`) lines 301-405 [crates/gcode/src/commands/search.rs:301-405]
  - Signature: `fn search_symbol_with_graph(`
  - Purpose: # Summary

Merges exact symbol search results with graph-boosted and graph-expanded candidates using reciprocal rank fusion, filters by visibility and search criteria, then sorts by relevance tier and RRF score. [crates/gcode/src/commands/search.rs:301-405]
- `search_text` (function) component `search_text [function]` (`35da9588-ed2d-52ee-a34c-c772bf37f38f`) lines 407-485 [crates/gcode/src/commands/search.rs:407-485]
  - Signature: `pub fn search_text(`
  - Purpose: Executes a paginated full-text search against a read-only database with visibility control, optional language filtering, and path-based result filtering, returning results in the specified format. [crates/gcode/src/commands/search.rs:407-485]
- `extract_seed_ids` (function) component `extract_seed_ids [function]` (`1db6f618-bf89-5472-8ff5-12728b7d8947`) lines 488-511 [crates/gcode/src/commands/search.rs:488-511]
  - Signature: `fn extract_seed_ids(`
  - Purpose: # Summary

Merges and deduplicates the top `per_source` symbol IDs from BM25 full-text search results and semantic search results into a single vector. [crates/gcode/src/commands/search.rs:488-511]
- `search_content` (function) component `search_content [function]` (`6ef79c20-f6e6-56d0-896e-a5ac41456140`) lines 513-593 [crates/gcode/src/commands/search.rs:513-593]
  - Signature: `pub fn search_content(`
  - Purpose: Executes a full-text search on indexed database content with visibility checks and optional path/language filtering, returning paginated results in the specified output format. [crates/gcode/src/commands/search.rs:513-593]
- `exact_tier` (function) component `exact_tier [function]` (`e72a997f-4906-5194-8c0a-29356028c4d8`) lines 595-605 [crates/gcode/src/commands/search.rs:595-605]
  - Signature: `fn exact_tier(query: &str, symbol: &Symbol) -> u8 {`
  - Purpose: Returns a tier value (0 for exact match, 1 for case-insensitive match, 2 for no match) comparing the query string against a symbol's `name` and `qualified_name` fields. [crates/gcode/src/commands/search.rs:595-605]
- `exact_tier_score` (function) component `exact_tier_score [function]` (`ca602825-8f65-5de3-99c1-29daa83d8dbb`) lines 607-613 [crates/gcode/src/commands/search.rs:607-613]
  - Signature: `fn exact_tier_score(query: &str, symbol: &Symbol) -> f64 {`
  - Purpose: Returns a normalized relevance score based on the exact matching tier between a query and symbol: tier 0 yields 1.0, tier 1 yields 0.9, and all other tiers yield 0.5. [crates/gcode/src/commands/search.rs:607-613]
- `final_rank_score` (function) component `final_rank_score [function]` (`f46cca62-82c6-5d85-b4ba-259e4ceee9ef`) lines 615-617 [crates/gcode/src/commands/search.rs:615-617]
  - Signature: `fn final_rank_score(query: &str, symbol: &Symbol, rrf_score: f64) -> f64 {`
  - Purpose: Returns the sum of the exact tier score and reciprocal rank fusion (RRF) score for a given query-symbol pair. [crates/gcode/src/commands/search.rs:615-617]
- `symbol_matches_filters` (function) component `symbol_matches_filters [function]` (`c2450c17-975f-5e70-bcd3-336256fbe3be`) lines 619-631 [crates/gcode/src/commands/search.rs:619-631]
  - Signature: `fn symbol_matches_filters(`
  - Purpose: Returns true if a symbol matches the optional kind and language filters, its file path matches the provided glob patterns, and its indexed path is valid in the current scope. [crates/gcode/src/commands/search.rs:619-631]
- `search_result_matches_filters` (function) component `search_result_matches_filters [function]` (`74b2e23a-421e-5eb7-b607-d67e02635110`) lines 633-643 [crates/gcode/src/commands/search.rs:633-643]
  - Signature: `fn search_result_matches_filters(`
  - Purpose: Determines whether a search result satisfies all three filtering criteria: optional language match, glob path pattern match, and indexed scope validity. [crates/gcode/src/commands/search.rs:633-643]
- `path_matches_filters` (function) component `path_matches_filters [function]` (`5e33dbe2-5a13-55b7-b4bf-457370d9b177`) lines 645-647 [crates/gcode/src/commands/search.rs:645-647]
  - Signature: `fn path_matches_filters(path_patterns: &[glob::Pattern], file_path: &str) -> bool {`
  - Purpose: Returns `true` if the file path matches any glob pattern in the provided slice, or if no patterns are specified (treating an empty filter list as a match-all). [crates/gcode/src/commands/search.rs:645-647]
- `filtered_fetch_cap_hint` (function) component `filtered_fetch_cap_hint [function]` (`b228b6c9-797b-534c-92ac-4c7d14e8a4b6`) lines 649-654 [crates/gcode/src/commands/search.rs:649-654]
  - Signature: `fn filtered_fetch_cap_hint() -> String {`
  - Purpose: Constructs a formatted string notifying the user that a path-filtered search operation reached the `fts::FILTERED_FETCH_CAP` limit and recommending query or path refinement for complete results. [crates/gcode/src/commands/search.rs:649-654]
- `path_filter_post_filter_hint` (function) component `path_filter_post_filter_hint [function]` (`03a03125-048b-5ed1-82b7-066222cec1b8`) lines 656-659 [crates/gcode/src/commands/search.rs:656-659]
  - Signature: `fn path_filter_post_filter_hint() -> String {`
  - Purpose: Returns a static hint string indicating that path filters unable to be pushed into SQL were applied as post-filters on results fetched with a broader database query. [crates/gcode/src/commands/search.rs:656-659]
- `visible_search_degraded_hint` (function) component `visible_search_degraded_hint [function]` (`115472dd-65b2-5bf9-a910-4fc5d7f4d553`) lines 661-663 [crates/gcode/src/commands/search.rs:661-663]
  - Signature: `fn visible_search_degraded_hint() -> String {`
  - Purpose: Returns a string warning that visible-project filtering failed and search results may be incomplete. [crates/gcode/src/commands/search.rs:661-663]
- `literal_query_hint` (function) component `literal_query_hint [function]` (`3379d553-112b-51b8-947b-46e1db935074`) lines 665-667 [crates/gcode/src/commands/search.rs:665-667]
  - Signature: `fn literal_query_hint(query: &str) -> Option<String> {`
  - Purpose: Returns an Option containing the `LITERAL_QUERY_HINT` constant as a String if the input query satisfies literal-like query criteria, otherwise returns None. [crates/gcode/src/commands/search.rs:665-667]
- `literal_like_query` (function) component `literal_like_query [function]` (`7abf7dfd-3a04-5d86-87a6-70974eb5cf01`) lines 669-679 [crates/gcode/src/commands/search.rs:669-679]
  - Signature: `fn literal_like_query(query: &str) -> bool {`
  - Purpose: Determines whether a query string exhibits literal-like characteristics by checking for the presence of quoted literals, call site syntax, path separators, or dotted notation patterns. [crates/gcode/src/commands/search.rs:669-679]
- `contains_quoted_literal` (function) component `contains_quoted_literal [function]` (`5d96ffe1-c82d-5799-ace0-1ac373da6f7d`) lines 681-685 [crates/gcode/src/commands/search.rs:681-685]
  - Signature: `fn contains_quoted_literal(query: &str) -> bool {`
  - Purpose: Returns true if the input string contains double quotes, backticks, or is enclosed by single quotes with at least one character between them. [crates/gcode/src/commands/search.rs:681-685]
- `contains_call_site_syntax` (function) component `contains_call_site_syntax [function]` (`19cf9c57-fe70-55e6-92f8-5c5f7059e12b`) lines 687-698 [crates/gcode/src/commands/search.rs:687-698]
  - Signature: `fn contains_call_site_syntax(query: &str) -> bool {`
  - Purpose: Returns true if the query contains an opening parenthesis immediately preceded by an alphanumeric character, underscore, dot, or colon (indicating function call syntax). [crates/gcode/src/commands/search.rs:687-698]
- `contains_path_separator` (function) component `contains_path_separator [function]` (`123bdeae-c055-5673-b8d6-8bbfb5dbd456`) lines 700-702 [crates/gcode/src/commands/search.rs:700-702]
  - Signature: `fn contains_path_separator(query: &str) -> bool {`
  - Purpose: Returns true if the query string contains either a forward slash or backslash path separator character. [crates/gcode/src/commands/search.rs:700-702]
- `is_dotted_literal` (function) component `is_dotted_literal [function]` (`1679faf9-8659-5bb3-856c-ec376633b1ce`) lines 704-712 [crates/gcode/src/commands/search.rs:704-712]
  - Signature: `fn is_dotted_literal(query: &str) -> bool {`
  - Purpose: Returns `true` if the query is a valid dotted-notation literal: non-empty dot-separated segments containing only valid identifier characters with no whitespace. [crates/gcode/src/commands/search.rs:704-712]
- `is_dotted_literal_char` (function) component `is_dotted_literal_char [function]` (`c92f0122-1a7e-5107-8b6e-e5d7c958f16d`) lines 714-716 [crates/gcode/src/commands/search.rs:714-716]
  - Signature: `fn is_dotted_literal_char(ch: char) -> bool {`
  - Purpose: This function returns `true` if the input character is ASCII alphanumeric or one of `_` or `-`; otherwise returns `false`. [crates/gcode/src/commands/search.rs:714-716]
- `combine_hints` (function) component `combine_hints [function]` (`192027e9-7fae-5ea7-a07b-3502514bf8ec`) lines 718-725 [crates/gcode/src/commands/search.rs:718-725]
  - Signature: `fn combine_hints(first: Option<String>, second: Option<String>) -> Option<String> {`
  - Purpose: Concatenates two optional strings with a space separator if both are `Some`, otherwise returns whichever single value is `Some` or `None` if both are absent. [crates/gcode/src/commands/search.rs:718-725]
- `print_search_warning` (function) component `print_search_warning [function]` (`d4ae90d6-cfad-5bc9-b170-57d40fcb579f`) lines 727-733 [crates/gcode/src/commands/search.rs:727-733]
  - Signature: `fn print_search_warning(ctx: &Context, hint: Option<&str>) {`
  - Purpose: Prints a formatted warning message to stderr if an optional hint string is provided and the context's quiet mode is disabled. [crates/gcode/src/commands/search.rs:727-733]
- `format_symbol_lookup_text` (function) component `format_symbol_lookup_text [function]` (`fc2918fc-0c26-5533-8638-792f40a98dee`) lines 735-750 [crates/gcode/src/commands/search.rs:735-750]
  - Signature: `fn format_symbol_lookup_text(symbol: &Symbol) -> String {`
  - Purpose: Formats a Symbol's metadata into a delimited single-line string containing file path, line range, kind, qualified name, ID, and optional signature. [crates/gcode/src/commands/search.rs:735-750]
- `compact_snippet` (function) component `compact_snippet [function]` (`36376181-c760-58fe-bc8d-eb281f27b8e8`) lines 752-754 [crates/gcode/src/commands/search.rs:752-754]
  - Signature: `fn compact_snippet(snippet: &str) -> String {`
  - Purpose: Collapses all contiguous whitespace sequences into single spaces while trimming leading and trailing whitespace. [crates/gcode/src/commands/search.rs:752-754]
- `print_empty_diagnostic` (function) component `print_empty_diagnostic [function]` (`3055b36e-32ba-58e9-b0f2-f81aa3835185`) lines 756-767 [crates/gcode/src/commands/search.rs:756-767]
  - Signature: `fn print_empty_diagnostic(ctx: &Context, is_empty: bool, offset: usize, total: usize) {`
  - Purpose: Prints context-specific diagnostic messages to stderr when search results are empty and quiet mode is disabled, with message content determined by whether a project identity file exists and the current result offset. [crates/gcode/src/commands/search.rs:756-767]
- `print_pagination_hint` (function) component `print_pagination_hint [function]` (`1a5c6d95-29e5-5a7c-84fb-c60e4231f426`) lines 769-778 [crates/gcode/src/commands/search.rs:769-778]
  - Signature: `fn print_pagination_hint(total: usize, offset: usize, result_count: usize) {`
  - Purpose: Prints a pagination hint to stderr when additional results exist beyond the current offset range, displaying the current result count, total count, and the next offset parameter needed to fetch more results. [crates/gcode/src/commands/search.rs:769-778]
- `symbol` (function) component `symbol [function]` (`7651cc50-d67f-5295-bb0d-adadd055d16f`) lines 784-805 [crates/gcode/src/commands/search.rs:784-805]
  - Signature: `fn symbol(file_path: &str, kind: &str, language: &str) -> Symbol {`
  - Purpose: Constructs a `Symbol` struct instance with the provided `file_path`, `kind`, and `language` parameters, while initializing all remaining fields with hardcoded or default values. [crates/gcode/src/commands/search.rs:784-805]
- `symbol_filter_rejects_language_kind_path_and_missing_disk_file` (function) component `symbol_filter_rejects_language_kind_path_and_missing_disk_file [function]` (`3328e414-1ea8-5b2a-b27a-d3bd774f1798`) lines 808-819 [crates/gcode/src/commands/search.rs:808-819]
  - Signature: `fn symbol_filter_rejects_language_kind_path_and_missing_disk_file() {`
  - Purpose: # Summary

Tests that a symbol with Rust language, function kind, and path `src/lib.rs` matches all filter criteria (language, kind, and glob pattern). [crates/gcode/src/commands/search.rs:808-819]
- `exact_tier_prefers_case_sensitive_match` (function) component `exact_tier_prefers_case_sensitive_match [function]` (`8f7de53d-f744-5ce8-ba1a-5150ffe112c9`) lines 822-836 [crates/gcode/src/commands/search.rs:822-836]
  - Signature: `fn exact_tier_prefers_case_sensitive_match() {`
  - Purpose: This test validates that `exact_tier()` returns progressively higher tier scores for weaker matches: 0 for exact case-sensitive match, 1 for case-variant match, and 2 for substring match. [crates/gcode/src/commands/search.rs:822-836]
- `final_score_preserves_display_tier_before_rrf_score` (function) component `final_score_preserves_display_tier_before_rrf_score [function]` (`c6b768ca-b1ec-5d4f-b33d-4168d0df98c8`) lines 839-848 [crates/gcode/src/commands/search.rs:839-848]
  - Signature: `fn final_score_preserves_display_tier_before_rrf_score() {`
  - Purpose: This test verifies that the final ranking algorithm prioritizes display tier (exact vs. fuzzy match) over the reciprocal rank fusion (RRF) score, ensuring an exact-match symbol ranks higher than a fuzzy-match symbol regardless of RRF score magnitude. [crates/gcode/src/commands/search.rs:839-848]
- `combines_fetch_cap_and_path_post_filter_hints` (function) component `combines_fetch_cap_and_path_post_filter_hints [function]` (`fdc8df80-f598-5d05-9109-d1ae7ece53ab`) lines 851-860 [crates/gcode/src/commands/search.rs:851-860]
  - Signature: `fn combines_fetch_cap_and_path_post_filter_hints() {`
  - Purpose: Tests that `combine_hints()` successfully merges a fetch cap hint with a path post-filter hint, producing a combined result containing both 'fetch cap' and 'post-filtered' substrings. [crates/gcode/src/commands/search.rs:851-860]
- `literal_query_hint_detects_literal_like_queries` (function) component `literal_query_hint_detects_literal_like_queries [function]` (`ef6bb305-e6fe-52d8-b05c-c0a87a1f78b8`) lines 863-874 [crates/gcode/src/commands/search.rs:863-874]
  - Signature: `fn literal_query_hint_detects_literal_like_queries() {`
  - Purpose: A unit test that verifies `literal_query_hint` correctly identifies literal-like queries (function calls, config paths, quoted strings, file paths) and returns hints containing both "gcode grep" and "search-content". [crates/gcode/src/commands/search.rs:863-874]
- `literal_query_hint_skips_natural_language_queries` (function) component `literal_query_hint_skips_natural_language_queries [function]` (`0b3551b1-bfe2-5050-92ae-e64ec8a3824b`) lines 877-879 [crates/gcode/src/commands/search.rs:877-879]
  - Signature: `fn literal_query_hint_skips_natural_language_queries() {`
  - Purpose: This test asserts that `literal_query_hint()` returns `None` when passed a natural language query string, verifying that the function correctly rejects non-literal input. [crates/gcode/src/commands/search.rs:877-879]
- `content_snippet_compaction_collapses_whitespace` (function) component `content_snippet_compaction_collapses_whitespace [function]` (`8ba7a954-d687-5dbb-9ef3-595885f1989e`) lines 882-887 [crates/gcode/src/commands/search.rs:882-887]
  - Signature: `fn content_snippet_compaction_collapses_whitespace() {`
  - Purpose: This test asserts that the `compact_snippet` function collapses all consecutive whitespace characters (spaces, newlines, tabs, carriage returns) into single spaces while removing leading and trailing whitespace. [crates/gcode/src/commands/search.rs:882-887]

