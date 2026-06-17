---
title: crates/gcore/src/search.rs
type: code_file
provenance:
- file: crates/gcore/src/search.rs
  ranges:
  - '20'
  - 29-31
  - 33-35
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

<details>
<summary>Relevant source files</summary>

- [crates/gcore/src/search.rs:20](crates/gcore/src/search.rs#L20), [crates/gcore/src/search.rs:29-31](crates/gcore/src/search.rs#L29-L31), [crates/gcore/src/search.rs:33-35](crates/gcore/src/search.rs#L33-L35), [crates/gcore/src/search.rs:39-41](crates/gcore/src/search.rs#L39-L41), [crates/gcore/src/search.rs:45-55](crates/gcore/src/search.rs#L45-L55), [crates/gcore/src/search.rs:59-63](crates/gcore/src/search.rs#L59-L63), [crates/gcore/src/search.rs:67-70](crates/gcore/src/search.rs#L67-L70), [crates/gcore/src/search.rs:76-130](crates/gcore/src/search.rs#L76-L130), [crates/gcore/src/search.rs:133-156](crates/gcore/src/search.rs#L133-L156), [crates/gcore/src/search.rs:163-183](crates/gcore/src/search.rs#L163-L183), [crates/gcore/src/search.rs:186-201](crates/gcore/src/search.rs#L186-L201), [crates/gcore/src/search.rs:204-223](crates/gcore/src/search.rs#L204-L223), [crates/gcore/src/search.rs:226-230](crates/gcore/src/search.rs#L226-L230), [crates/gcore/src/search.rs:233-235](crates/gcore/src/search.rs#L233-L235), [crates/gcore/src/search.rs:238-246](crates/gcore/src/search.rs#L238-L246), [crates/gcore/src/search.rs:248-268](crates/gcore/src/search.rs#L248-L268), [crates/gcore/src/search.rs:271-280](crates/gcore/src/search.rs#L271-L280), [crates/gcore/src/search.rs:283-296](crates/gcore/src/search.rs#L283-L296)

</details>

# crates/gcore/src/search.rs

Module: [[code/modules/crates/gcore/src|crates/gcore/src]]

## Purpose

Defines generic search utilities for the `search` feature: a trusted SQL row identifier wrapper, helpers for rendering the Postgres BM25 score expression, and shared result types for fused search output, source-level explanations, and degradation metadata. It also implements Reciprocal Rank Fusion merging and PostgreSQL query sanitization, with tests covering explanation/degradation preservation, domain-query filtering, deduplication, deterministic ordering, and schema-contract assumptions.
[crates/gcore/src/search.rs:20]
[crates/gcore/src/search.rs:29-31]
[crates/gcore/src/search.rs:33-35]
[crates/gcore/src/search.rs:39-41]
[crates/gcore/src/search.rs:45-55]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `TrustedRowId` | class | `pub struct TrustedRowId(String);` | `TrustedRowId [class]` | `6b6d7ea6-1665-54ad-92d3-cda4fb74a9a2` | 20-20 [crates/gcore/src/search.rs:20] | Indexed class `TrustedRowId` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:20] |
| `TrustedRowId::new_unchecked` | method | `pub unsafe fn new_unchecked(row_id: &str) -> Self {` | `TrustedRowId::new_unchecked [method]` | `456a4229-469f-5475-8609-d5513a22647f` | 29-31 [crates/gcore/src/search.rs:29-31] | Indexed method `TrustedRowId::new_unchecked` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:29-31] |
| `TrustedRowId::as_str` | method | `fn as_str(&self) -> &str {` | `TrustedRowId::as_str [method]` | `60276e52-789e-5944-b65e-7c61c8db4d41` | 33-35 [crates/gcore/src/search.rs:33-35] | Indexed method `TrustedRowId::as_str` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:33-35] |
| `bm25_score_expr` | function | `pub fn bm25_score_expr(row_id: &TrustedRowId) -> String {` | `bm25_score_expr [function]` | `743dd9ed-014e-5ce0-b05d-3888f89cdd3c` | 39-41 [crates/gcore/src/search.rs:39-41] | Indexed function `bm25_score_expr` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:39-41] |
| `SearchResult` | class | `pub struct SearchResult {` | `SearchResult [class]` | `38438a32-6f57-5afc-bf99-9e50787dad03` | 45-55 [crates/gcore/src/search.rs:45-55] | Indexed class `SearchResult` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:45-55] |
| `SourceExplanation` | class | `pub struct SourceExplanation {` | `SourceExplanation [class]` | `f52f7839-76db-5945-999b-b9fef1946bd5` | 59-63 [crates/gcore/src/search.rs:59-63] | Indexed class `SourceExplanation` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:59-63] |
| `SearchDegradation` | class | `pub struct SearchDegradation {` | `SearchDegradation [class]` | `2c2fdb79-fed4-58c4-8187-878f382b6d5e` | 67-70 [crates/gcore/src/search.rs:67-70] | Indexed class `SearchDegradation` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:67-70] |
| `rrf_merge` | function | `pub fn rrf_merge(sources: Vec<(&str, Vec<String>)>) -> Vec<SearchResult> {` | `rrf_merge [function]` | `d6f78ad9-e0bf-5b96-a950-a9f97036120f` | 76-130 [crates/gcore/src/search.rs:76-130] | Indexed function `rrf_merge` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:76-130] |
| `sanitize_pg_search_query` | function | `pub fn sanitize_pg_search_query(query: &str) -> String {` | `sanitize_pg_search_query [function]` | `a1d5a6ae-42e4-56b3-b81a-7d3bdd3b2bf7` | 133-156 [crates/gcore/src/search.rs:133-156] | Indexed function `sanitize_pg_search_query` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:133-156] |
| `rrf_preserves_explanations_and_degradation` | function | `fn rrf_preserves_explanations_and_degradation() {` | `rrf_preserves_explanations_and_degradation [function]` | `96857ca0-6f76-5496-9eb4-81d73f3b65f7` | 163-183 [crates/gcore/src/search.rs:163-183] | Indexed function `rrf_preserves_explanations_and_degradation` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:163-183] |
| `sanitize_pg_search_query_matches_gobby_rules` | function | `fn sanitize_pg_search_query_matches_gobby_rules() {` | `sanitize_pg_search_query_matches_gobby_rules [function]` | `bfde36af-4923-5ee3-af74-234f6dc84eac` | 186-201 [crates/gcore/src/search.rs:186-201] | Indexed function `sanitize_pg_search_query_matches_gobby_rules` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:186-201] |
| `search_result_is_cli_independent` | function | `fn search_result_is_cli_independent() {` | `search_result_is_cli_independent [function]` | `6d6b8f24-6495-547f-9c9c-645a6b0c585f` | 204-223 [crates/gcore/src/search.rs:204-223] | Indexed function `search_result_is_cli_independent` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:204-223] |
| `bm25_score_expression_uses_pdb_score` | function | `fn bm25_score_expression_uses_pdb_score() {` | `bm25_score_expression_uses_pdb_score [function]` | `64ba3101-6054-5019-aea8-991bafda14ae` | 226-230 [crates/gcore/src/search.rs:226-230] | Indexed function `bm25_score_expression_uses_pdb_score` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:226-230] |
| `bm25_score_regprocedure_matches_runtime_schema_contract` | function | `fn bm25_score_regprocedure_matches_runtime_schema_contract() {` | `bm25_score_regprocedure_matches_runtime_schema_contract [function]` | `95de4f15-d0e3-5f5e-a7a1-9ff724b6af17` | 233-235 [crates/gcore/src/search.rs:233-235] | Indexed function `bm25_score_regprocedure_matches_runtime_schema_contract` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:233-235] |
| `search_core_has_no_domain_queries` | function | `fn search_core_has_no_domain_queries() {` | `search_core_has_no_domain_queries [function]` | `ae95463b-3662-5869-af9f-449ad5887356` | 238-246 [crates/gcore/src/search.rs:238-246] | Indexed function `search_core_has_no_domain_queries` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:238-246] |
| `forbidden_domain_fragments` | function | `fn forbidden_domain_fragments() -> Vec<String> {` | `forbidden_domain_fragments [function]` | `09043369-2eb3-5cc2-828f-584a26f092db` | 248-268 [crates/gcore/src/search.rs:248-268] | Indexed function `forbidden_domain_fragments` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:248-268] |
| `rrf_deduplicates_within_source` | function | `fn rrf_deduplicates_within_source() {` | `rrf_deduplicates_within_source [function]` | `bba02767-4c01-5ab6-8106-c9efaa1ec621` | 271-280 [crates/gcore/src/search.rs:271-280] | Indexed function `rrf_deduplicates_within_source` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:271-280] |
| `rrf_sorts_sources_deterministically` | function | `fn rrf_sorts_sources_deterministically() {` | `rrf_sorts_sources_deterministically [function]` | `602ec722-2326-5d08-83fc-4f46d6138d51` | 283-296 [crates/gcore/src/search.rs:283-296] | Indexed function `rrf_sorts_sources_deterministically` in `crates/gcore/src/search.rs`. [crates/gcore/src/search.rs:283-296] |
