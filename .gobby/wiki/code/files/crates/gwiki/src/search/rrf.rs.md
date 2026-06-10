---
title: crates/gwiki/src/search/rrf.rs
type: code_file
provenance:
- file: crates/gwiki/src/search/rrf.rs
  ranges:
  - 8-92
  - 94-96
  - 98-108
  - 119-180
  - 183-225
  - 229-240
  - 242-267
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/search/rrf.rs

Module: [[code/modules/crates/gwiki/src/search|crates/gwiki/src/search]]

## Purpose

`crates/gwiki/src/search/rrf.rs` exposes 7 indexed API symbols.
[crates/gwiki/src/search/rrf.rs:8-92]
[crates/gwiki/src/search/rrf.rs:94-96]
[crates/gwiki/src/search/rrf.rs:98-108]
[crates/gwiki/src/search/rrf.rs:119-180]
[crates/gwiki/src/search/rrf.rs:183-225]
[crates/gwiki/src/search/rrf.rs:229-240]
[crates/gwiki/src/search/rrf.rs:242-267]

## API Symbols

- `fuse_sources` (function) component `fuse_sources [function]` (`4eca450f-d42b-5051-b76f-64bbcfd6a47a`) lines 8-92 [crates/gwiki/src/search/rrf.rs:8-92]
  - Signature: `pub fn fuse_sources(`
  - Purpose: `fuse_sources` deduplicates and merges BM25, semantic, and graph `WikiSearchResult`s by fusion key, applies reciprocal-rank fusion to the ranked source key lists to assign final scores and source/explanation metadata, and returns up to `limit` fused results with the provided degradations (or an empty result set when `limit == 0`). [crates/gwiki/src/search/rrf.rs:8-92]
- `ranked_keys` (function) component `ranked_keys [function]` (`e622f5b9-e60b-5d5c-8c70-6991229b985a`) lines 94-96 [crates/gwiki/src/search/rrf.rs:94-96]
  - Signature: `fn ranked_keys(hits: &[WikiSearchResult]) -> Result<Vec<String>, SearchError> {`
  - Purpose: Transforms a slice of `WikiSearchResult` values into a `Result<Vec<String>, SearchError>` by calling `WikiSearchResult::fusion_key` on each hit and collecting the results, propagating the first error encountered. [crates/gwiki/src/search/rrf.rs:94-96]
- `merge_hit_metadata` (function) component `merge_hit_metadata [function]` (`075bf38b-fb30-5918-b746-c1c9254303ba`) lines 98-108 [crates/gwiki/src/search/rrf.rs:98-108]
  - Signature: `fn merge_hit_metadata(existing: &mut WikiSearchResult, hit: &WikiSearchResult) {`
  - Purpose: `merge_hit_metadata` updates `existing` in place by backfilling missing `title` and `chunk` from `hit`, and replacing an empty `snippet` with `hit.snippet` only when the source snippet is non-empty. [crates/gwiki/src/search/rrf.rs:98-108]
- `fusion_preserves_sources` (function) component `fusion_preserves_sources [function]` (`110023b3-89ee-5be2-925e-e4d64a6705cc`) lines 119-180 [crates/gwiki/src/search/rrf.rs:119-180]
  - Signature: `fn fusion_preserves_sources() {`
  - Purpose: Verifies that `fuse_sources` coalesces duplicate hits for the same document across BM25, graph, and semantic inputs while preserving the fused result’s source/provenance order and retaining the `PartialSearch` degradation metadata. [crates/gwiki/src/search/rrf.rs:119-180]
- `fusion_uses_canonical_page_key` (function) component `fusion_uses_canonical_page_key [function]` (`dbf76817-ee41-55ac-a8cb-9ed7bb0c1559`) lines 183-225 [crates/gwiki/src/search/rrf.rs:183-225]
  - Signature: `fn fusion_uses_canonical_page_key() {`
  - Purpose: Verifies that `fuse_sources` collapses BM25, graph, and semantic matches for the same Rust document into one fused result keyed by the canonical page key `project:project-1:knowledge/topics/rust.md`, preserving the source and explanation order as BM25, Graph, then Semantic. [crates/gwiki/src/search/rrf.rs:183-225]
- `fusion_rejects_invalid_utf8_paths` (function) component `fusion_rejects_invalid_utf8_paths [function]` (`92abeb5a-b0ae-58e1-8850-acb5b03c331a`) lines 229-240 [crates/gwiki/src/search/rrf.rs:229-240]
  - Signature: `fn fusion_rejects_invalid_utf8_paths() {`
  - Purpose: This test verifies that `fuse_sources` rejects a search hit whose `path` contains invalid UTF-8 bytes by returning a `SearchError::InvalidPath` error. [crates/gwiki/src/search/rrf.rs:229-240]
- `search_result` (function) component `search_result [function]` (`c7c9774d-0fd0-51de-93df-b76b8da72b79`) lines 242-267 [crates/gwiki/src/search/rrf.rs:242-267]
  - Signature: `fn search_result(id: &str, source: SearchSource) -> WikiSearchResult {`
  - Purpose: Constructs a `WikiSearchResult` with the provided `id` and single `source`, filling in fixed Rust document metadata, snippet, score, chunk provenance, and provenance fields. [crates/gwiki/src/search/rrf.rs:242-267]

