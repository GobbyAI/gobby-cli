---
title: crates/gcore/src/search.rs
type: code_file
provenance:
- file: crates/gcore/src/search.rs
  ranges:
  - '20'
  - 22-36
  - 39-41
  - 45-55
  - 59-63
  - 67-70
  - 76-130
  - 133-156
  - 163-183
  - 186-201
  - 204-223
  - 226-230
  - 233-235
  - 238-246
  - 248-268
  - 271-280
  - 283-296
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcore/src/search.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

Defines generic search and rank-fusion helpers for the `search` feature, keeping domain-specific query logic in consuming crates. It provides a `TrustedRowId` wrapper for SQL-safe, caller-validated row identifiers and a `bm25_score_expr` formatter for building `pdb.score(...)` expressions, along with serde-serializable `SearchResult`, `SourceExplanation`, and `SearchDegradation` types for merged search output and availability metadata. The core `rrf_merge` logic combines per-source ranked IDs with reciprocal rank fusion, deduplicates and orders explanations deterministically, and `sanitize_pg_search_query` normalizes PostgreSQL full-text queries by collapsing whitespace and escaping leading negation. The tests lock down these behaviors, including fusion ordering, serialization, query sanitization rules, and the expected BM25/runtime schema contract.
[crates/gcore/src/search.rs:20]
[crates/gcore/src/search.rs:22-36]
[crates/gcore/src/search.rs:29-31]
[crates/gcore/src/search.rs:33-35]
[crates/gcore/src/search.rs:39-41]

## API Symbols

- `TrustedRowId` (class) component `TrustedRowId [class]` (`6b6d7ea6-1665-54ad-92d3-cda4fb74a9a2`) lines 20-20 [crates/gcore/src/search.rs:20]
  - Signature: `pub struct TrustedRowId(String);`
  - Purpose: 'TrustedRowId' is a Rust newtype wrapper around 'String' used to represent a row identifier that has been validated or otherwise marked as trusted. [crates/gcore/src/search.rs:20]
- `TrustedRowId` (class) component `TrustedRowId [class]` (`42f399c8-050e-5e50-aeba-252cf6f1cdde`) lines 22-36 [crates/gcore/src/search.rs:22-36]
  - Signature: `impl TrustedRowId {`
  - Purpose: 'TrustedRowId' is a thin wrapper around a string row identifier that provides an 'unsafe' constructor for trusted, SQL-interpolated identifiers and exposes the inner value as '&str' via a private accessor. [crates/gcore/src/search.rs:22-36]
- `TrustedRowId.new_unchecked` (method) component `TrustedRowId.new_unchecked [method]` (`456a4229-469f-5475-8609-d5513a22647f`) lines 29-31 [crates/gcore/src/search.rs:29-31]
  - Signature: `pub unsafe fn new_unchecked(row_id: &str) -> Self {`
  - Purpose: Constructs a new instance by cloning 'row_id' into the inner 'String' without performing any validation, so the caller must ensure the input satisfies the type’s invariants. [crates/gcore/src/search.rs:29-31]
- `TrustedRowId.as_str` (method) component `TrustedRowId.as_str [method]` (`60276e52-789e-5944-b65e-7c61c8db4d41`) lines 33-35 [crates/gcore/src/search.rs:33-35]
  - Signature: `fn as_str(&self) -> &str {`
  - Purpose: Returns an immutable string slice reference to the inner 'String' field 'self.0'. [crates/gcore/src/search.rs:33-35]
- `bm25_score_expr` (function) component `bm25_score_expr [function]` (`743dd9ed-014e-5ce0-b05d-3888f89cdd3c`) lines 39-41 [crates/gcore/src/search.rs:39-41]
  - Signature: `pub fn bm25_score_expr(row_id: &TrustedRowId) -> String {`
  - Purpose: Returns a 'String' containing a function-call expression that invokes 'BM25_SCORE_FUNCTION' with the trusted row ID’s string representation as its single argument. [crates/gcore/src/search.rs:39-41]
- `SearchResult` (class) component `SearchResult [class]` (`38438a32-6f57-5afc-bf99-9e50787dad03`) lines 45-55 [crates/gcore/src/search.rs:45-55]
  - Signature: `pub struct SearchResult {`
  - Purpose: 'SearchResult' is a serialized search/fusion output record containing an opaque result identifier, an aggregate score, the contributing source names, and optional per-source debug explanations. [crates/gcore/src/search.rs:45-55]
- `SourceExplanation` (class) component `SourceExplanation [class]` (`f52f7839-76db-5945-999b-b9fef1946bd5`) lines 59-63 [crates/gcore/src/search.rs:59-63]
  - Signature: `pub struct SourceExplanation {`
  - Purpose: 'SourceExplanation' is a data container that stores a source identifier along with its ordinal rank and floating-point score. [crates/gcore/src/search.rs:59-63]
- `SearchDegradation` (class) component `SearchDegradation [class]` (`2c2fdb79-fed4-58c4-8187-878f382b6d5e`) lines 67-70 [crates/gcore/src/search.rs:67-70]
  - Signature: `pub struct SearchDegradation {`
  - Purpose: 'SearchDegradation' is a data structure that records which search sources are unavailable versus available, each as a 'Vec<String>'. [crates/gcore/src/search.rs:67-70]
- `rrf_merge` (function) component `rrf_merge [function]` (`d6f78ad9-e0bf-5b96-a950-a9f97036120f`) lines 76-130 [crates/gcore/src/search.rs:76-130]
  - Signature: `pub fn rrf_merge(sources: Vec<(&str, Vec<String>)>) -> Vec<SearchResult> {`
  - Purpose: 'rrf_merge' aggregates per-source ranked ID lists using reciprocal rank fusion by deduplicating each source to its best rank per ID, assigning '1.0 / (RRF_K + rank)' scores, summing scores across sources into 'SearchResult's with sorted source explanations, and returning the results ordered by descending total score with ID tie-breaks. [crates/gcore/src/search.rs:76-130]
- `sanitize_pg_search_query` (function) component `sanitize_pg_search_query [function]` (`a1d5a6ae-42e4-56b3-b81a-7d3bdd3b2bf7`) lines 133-156 [crates/gcore/src/search.rs:133-156]
  - Signature: `pub fn sanitize_pg_search_query(query: &str) -> String {`
  - Purpose: Normalizes a PostgreSQL full-text search query by replacing control whitespace with spaces, collapsing whitespace to single separators, and escaping any token that starts with '-' so it is treated as a literal rather than a negation operator. [crates/gcore/src/search.rs:133-156]
- `rrf_preserves_explanations_and_degradation` (function) component `rrf_preserves_explanations_and_degradation [function]` (`96857ca0-6f76-5496-9eb4-81d73f3b65f7`) lines 163-183 [crates/gcore/src/search.rs:163-183]
  - Signature: `fn rrf_preserves_explanations_and_degradation() {`
  - Purpose: Verifies that 'rrf_merge' preserves per-source explanations and source ordering for merged results, and that 'SearchDegradation' correctly records unavailable versus available sources. [crates/gcore/src/search.rs:163-183]
- `sanitize_pg_search_query_matches_gobby_rules` (function) component `sanitize_pg_search_query_matches_gobby_rules [function]` (`bfde36af-4923-5ee3-af74-234f6dc84eac`) lines 186-201 [crates/gcore/src/search.rs:186-201]
  - Signature: `fn sanitize_pg_search_query_matches_gobby_rules() {`
  - Purpose: Verifies that 'sanitize_pg_search_query' preserves allowed search syntax like '::', '+', parentheses, hyphens inside terms, and quoted text while escaping leading negation and stripping control characters such as tabs and NULs. [crates/gcore/src/search.rs:186-201]
- `search_result_is_cli_independent` (function) component `search_result_is_cli_independent [function]` (`6d6b8f24-6495-547f-9c9c-645a6b0c585f`) lines 204-223 [crates/gcore/src/search.rs:204-223]
  - Signature: `fn search_result_is_cli_independent() {`
  - Purpose: Verifies that a 'SearchResult' with 'sources' and 'explanations' serializes to JSON and deserializes back without losing 'id', 'sources', or explanation source data, demonstrating CLI-independent serde behavior. [crates/gcore/src/search.rs:204-223]
- `bm25_score_expression_uses_pdb_score` (function) component `bm25_score_expression_uses_pdb_score [function]` (`64ba3101-6054-5019-aea8-991bafda14ae`) lines 226-230 [crates/gcore/src/search.rs:226-230]
  - Signature: `fn bm25_score_expression_uses_pdb_score() {`
  - Purpose: Verifies that 'bm25_score_expr' formats a 'TrustedRowId' into the SQL expression 'pdb.score(row.id)'. [crates/gcore/src/search.rs:226-230]
- `bm25_score_regprocedure_matches_runtime_schema_contract` (function) component `bm25_score_regprocedure_matches_runtime_schema_contract [function]` (`95de4f15-d0e3-5f5e-a7a1-9ff724b6af17`) lines 233-235 [crates/gcore/src/search.rs:233-235]
  - Signature: `fn bm25_score_regprocedure_matches_runtime_schema_contract() {`
  - Purpose: Verifies that 'BM25_SCORE_REGPROCEDURE' is set to the exact runtime schema contract string '"pdb.score(anyelement)"'. [crates/gcore/src/search.rs:233-235]
- `search_core_has_no_domain_queries` (function) component `search_core_has_no_domain_queries [function]` (`ae95463b-3662-5869-af9f-449ad5887356`) lines 238-246 [crates/gcore/src/search.rs:238-246]
  - Signature: `fn search_core_has_no_domain_queries() {`
  - Purpose: Verifies that the contents of 'search.rs' do not contain any strings returned by 'forbidden_domain_fragments()', failing if a domain-specific query fragment is present. [crates/gcore/src/search.rs:238-246]
- `forbidden_domain_fragments` (function) component `forbidden_domain_fragments [function]` (`09043369-2eb3-5cc2-828f-584a26f092db`) lines 248-268 [crates/gcore/src/search.rs:248-268]
  - Signature: `fn forbidden_domain_fragments() -> Vec<String> {`
  - Purpose: Constructs and returns a 'Vec<String>' of forbidden domain fragments by concatenating predefined string parts into blocked tokens such as SQL keywords and internal schema names. [crates/gcore/src/search.rs:248-268]
- `rrf_deduplicates_within_source` (function) component `rrf_deduplicates_within_source [function]` (`bba02767-4c01-5ab6-8106-c9efaa1ec621`) lines 271-280 [crates/gcore/src/search.rs:271-280]
  - Signature: `fn rrf_deduplicates_within_source() {`
  - Purpose: Verifies that 'rrf_merge' deduplicates duplicate item IDs within a single source list, producing one result for '"a"' with one 'fts' source, one explanation at rank 0, and an RRF score of '1/60'. [crates/gcore/src/search.rs:271-280]
- `rrf_sorts_sources_deterministically` (function) component `rrf_sorts_sources_deterministically [function]` (`602ec722-2326-5d08-83fc-4f46d6138d51`) lines 283-296 [crates/gcore/src/search.rs:283-296]
  - Signature: `fn rrf_sorts_sources_deterministically() {`
  - Purpose: Verifies that 'rrf_merge' produces deterministic source ordering for a tied result by ordering the merged item’s 'sources' and 'explanations' as 'fts' before 'semantic'. [crates/gcore/src/search.rs:283-296]

