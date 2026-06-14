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

This file defines the shared search primitives used by the `search` feature: a trusted wrapper for SQL row identifiers, helpers for building BM25 score expressions, result and explanation structs for fused search output, and a degradation record for missing sources. It also implements Reciprocal Rank Fusion and Postgres search-query sanitization, with tests that verify RRF preserves metadata, deduplicates and orders sources deterministically, BM25 wiring matches the runtime schema, and sanitized queries follow the project’s rules.
[crates/gcore/src/search.rs:20]
[crates/gcore/src/search.rs:22-36]
[crates/gcore/src/search.rs:29-31]
[crates/gcore/src/search.rs:33-35]
[crates/gcore/src/search.rs:39-41]

## API Symbols

- `TrustedRowId` (class) component `TrustedRowId [class]` (`6b6d7ea6-1665-54ad-92d3-cda4fb74a9a2`) lines 20-20 [crates/gcore/src/search.rs:20]
  - Signature: `pub struct TrustedRowId(String);`
  - Purpose: Indexed class `TrustedRowId` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:20]
- `TrustedRowId` (class) component `TrustedRowId [class]` (`42f399c8-050e-5e50-aeba-252cf6f1cdde`) lines 22-36 [crates/gcore/src/search.rs:22-36]
  - Signature: `impl TrustedRowId {`
  - Purpose: Indexed class `TrustedRowId` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:22-36]
- `TrustedRowId.new_unchecked` (method) component `TrustedRowId.new_unchecked [method]` (`456a4229-469f-5475-8609-d5513a22647f`) lines 29-31 [crates/gcore/src/search.rs:29-31]
  - Signature: `pub unsafe fn new_unchecked(row_id: &str) -> Self {`
  - Purpose: Indexed method `TrustedRowId.new_unchecked` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:29-31]
- `TrustedRowId.as_str` (method) component `TrustedRowId.as_str [method]` (`60276e52-789e-5944-b65e-7c61c8db4d41`) lines 33-35 [crates/gcore/src/search.rs:33-35]
  - Signature: `fn as_str(&self) -> &str {`
  - Purpose: Indexed method `TrustedRowId.as_str` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:33-35]
- `bm25_score_expr` (function) component `bm25_score_expr [function]` (`743dd9ed-014e-5ce0-b05d-3888f89cdd3c`) lines 39-41 [crates/gcore/src/search.rs:39-41]
  - Signature: `pub fn bm25_score_expr(row_id: &TrustedRowId) -> String {`
  - Purpose: Indexed function `bm25_score_expr` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:39-41]
- `SearchResult` (class) component `SearchResult [class]` (`38438a32-6f57-5afc-bf99-9e50787dad03`) lines 45-55 [crates/gcore/src/search.rs:45-55]
  - Signature: `pub struct SearchResult {`
  - Purpose: Indexed class `SearchResult` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:45-55]
- `SourceExplanation` (class) component `SourceExplanation [class]` (`f52f7839-76db-5945-999b-b9fef1946bd5`) lines 59-63 [crates/gcore/src/search.rs:59-63]
  - Signature: `pub struct SourceExplanation {`
  - Purpose: Indexed class `SourceExplanation` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:59-63]
- `SearchDegradation` (class) component `SearchDegradation [class]` (`2c2fdb79-fed4-58c4-8187-878f382b6d5e`) lines 67-70 [crates/gcore/src/search.rs:67-70]
  - Signature: `pub struct SearchDegradation {`
  - Purpose: Indexed class `SearchDegradation` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:67-70]
- `rrf_merge` (function) component `rrf_merge [function]` (`d6f78ad9-e0bf-5b96-a950-a9f97036120f`) lines 76-130 [crates/gcore/src/search.rs:76-130]
  - Signature: `pub fn rrf_merge(sources: Vec<(&str, Vec<String>)>) -> Vec<SearchResult> {`
  - Purpose: Indexed function `rrf_merge` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:76-130]
- `sanitize_pg_search_query` (function) component `sanitize_pg_search_query [function]` (`a1d5a6ae-42e4-56b3-b81a-7d3bdd3b2bf7`) lines 133-156 [crates/gcore/src/search.rs:133-156]
  - Signature: `pub fn sanitize_pg_search_query(query: &str) -> String {`
  - Purpose: Indexed function `sanitize_pg_search_query` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:133-156]
- `rrf_preserves_explanations_and_degradation` (function) component `rrf_preserves_explanations_and_degradation [function]` (`96857ca0-6f76-5496-9eb4-81d73f3b65f7`) lines 163-183 [crates/gcore/src/search.rs:163-183]
  - Signature: `fn rrf_preserves_explanations_and_degradation() {`
  - Purpose: Indexed function `rrf_preserves_explanations_and_degradation` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:163-183]
- `sanitize_pg_search_query_matches_gobby_rules` (function) component `sanitize_pg_search_query_matches_gobby_rules [function]` (`bfde36af-4923-5ee3-af74-234f6dc84eac`) lines 186-201 [crates/gcore/src/search.rs:186-201]
  - Signature: `fn sanitize_pg_search_query_matches_gobby_rules() {`
  - Purpose: Indexed function `sanitize_pg_search_query_matches_gobby_rules` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:186-201]
- `search_result_is_cli_independent` (function) component `search_result_is_cli_independent [function]` (`6d6b8f24-6495-547f-9c9c-645a6b0c585f`) lines 204-223 [crates/gcore/src/search.rs:204-223]
  - Signature: `fn search_result_is_cli_independent() {`
  - Purpose: Indexed function `search_result_is_cli_independent` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:204-223]
- `bm25_score_expression_uses_pdb_score` (function) component `bm25_score_expression_uses_pdb_score [function]` (`64ba3101-6054-5019-aea8-991bafda14ae`) lines 226-230 [crates/gcore/src/search.rs:226-230]
  - Signature: `fn bm25_score_expression_uses_pdb_score() {`
  - Purpose: Indexed function `bm25_score_expression_uses_pdb_score` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:226-230]
- `bm25_score_regprocedure_matches_runtime_schema_contract` (function) component `bm25_score_regprocedure_matches_runtime_schema_contract [function]` (`95de4f15-d0e3-5f5e-a7a1-9ff724b6af17`) lines 233-235 [crates/gcore/src/search.rs:233-235]
  - Signature: `fn bm25_score_regprocedure_matches_runtime_schema_contract() {`
  - Purpose: Indexed function `bm25_score_regprocedure_matches_runtime_schema_contract` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:233-235]
- `search_core_has_no_domain_queries` (function) component `search_core_has_no_domain_queries [function]` (`ae95463b-3662-5869-af9f-449ad5887356`) lines 238-246 [crates/gcore/src/search.rs:238-246]
  - Signature: `fn search_core_has_no_domain_queries() {`
  - Purpose: Indexed function `search_core_has_no_domain_queries` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:238-246]
- `forbidden_domain_fragments` (function) component `forbidden_domain_fragments [function]` (`09043369-2eb3-5cc2-828f-584a26f092db`) lines 248-268 [crates/gcore/src/search.rs:248-268]
  - Signature: `fn forbidden_domain_fragments() -> Vec<String> {`
  - Purpose: Indexed function `forbidden_domain_fragments` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:248-268]
- `rrf_deduplicates_within_source` (function) component `rrf_deduplicates_within_source [function]` (`bba02767-4c01-5ab6-8106-c9efaa1ec621`) lines 271-280 [crates/gcore/src/search.rs:271-280]
  - Signature: `fn rrf_deduplicates_within_source() {`
  - Purpose: Indexed function `rrf_deduplicates_within_source` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:271-280]
- `rrf_sorts_sources_deterministically` (function) component `rrf_sorts_sources_deterministically [function]` (`602ec722-2326-5d08-83fc-4f46d6138d51`) lines 283-296 [crates/gcore/src/search.rs:283-296]
  - Signature: `fn rrf_sorts_sources_deterministically() {`
  - Purpose: Indexed function `rrf_sorts_sources_deterministically` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:283-296]

