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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/search/rrf.rs:8-92](crates/gwiki/src/search/rrf.rs#L8-L92), [crates/gwiki/src/search/rrf.rs:94-96](crates/gwiki/src/search/rrf.rs#L94-L96), [crates/gwiki/src/search/rrf.rs:98-108](crates/gwiki/src/search/rrf.rs#L98-L108), [crates/gwiki/src/search/rrf.rs:119-180](crates/gwiki/src/search/rrf.rs#L119-L180), [crates/gwiki/src/search/rrf.rs:183-225](crates/gwiki/src/search/rrf.rs#L183-L225), [crates/gwiki/src/search/rrf.rs:229-240](crates/gwiki/src/search/rrf.rs#L229-L240), [crates/gwiki/src/search/rrf.rs:242-267](crates/gwiki/src/search/rrf.rs#L242-L267)

</details>

# crates/gwiki/src/search/rrf.rs

Module: [[code/modules/crates/gwiki/src/search|crates/gwiki/src/search]]

## Purpose

Implements reciprocal-rank fusion for wiki search results. `fuse_sources` takes BM25, semantic, and graph hit lists plus degradations and a result limit, normalizes each hit to a fusion key, merges duplicate metadata in a `BTreeMap`, runs `gobby_core::search::rrf_merge`, and then rehydrates fused scores, sources, and explanations back onto the original `WikiSearchResult` entries. The helper functions support that flow by extracting ranked keys, merging per-hit metadata, and constructing search results, while the tests verify source preservation, canonical page-key handling, and rejection of invalid UTF-8 paths.
[crates/gwiki/src/search/rrf.rs:8-92]
[crates/gwiki/src/search/rrf.rs:94-96]
[crates/gwiki/src/search/rrf.rs:98-108]
[crates/gwiki/src/search/rrf.rs:119-180]
[crates/gwiki/src/search/rrf.rs:183-225]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `fuse_sources` | function | `pub fn fuse_sources(` | `fuse_sources [function]` | `4eca450f-d42b-5051-b76f-64bbcfd6a47a` | 8-92 [crates/gwiki/src/search/rrf.rs:8-92] | Indexed function `fuse_sources` in `crates/gwiki/src/search/rrf.rs`. [crates/gwiki/src/search/rrf.rs:8-92] |
| `ranked_keys` | function | `fn ranked_keys(hits: &[WikiSearchResult]) -> Result<Vec<String>, SearchError> {` | `ranked_keys [function]` | `e622f5b9-e60b-5d5c-8c70-6991229b985a` | 94-96 [crates/gwiki/src/search/rrf.rs:94-96] | Indexed function `ranked_keys` in `crates/gwiki/src/search/rrf.rs`. [crates/gwiki/src/search/rrf.rs:94-96] |
| `merge_hit_metadata` | function | `fn merge_hit_metadata(existing: &mut WikiSearchResult, hit: &WikiSearchResult) {` | `merge_hit_metadata [function]` | `075bf38b-fb30-5918-b746-c1c9254303ba` | 98-108 [crates/gwiki/src/search/rrf.rs:98-108] | Indexed function `merge_hit_metadata` in `crates/gwiki/src/search/rrf.rs`. [crates/gwiki/src/search/rrf.rs:98-108] |
| `fusion_preserves_sources` | function | `fn fusion_preserves_sources() {` | `fusion_preserves_sources [function]` | `110023b3-89ee-5be2-925e-e4d64a6705cc` | 119-180 [crates/gwiki/src/search/rrf.rs:119-180] | Indexed function `fusion_preserves_sources` in `crates/gwiki/src/search/rrf.rs`. [crates/gwiki/src/search/rrf.rs:119-180] |
| `fusion_uses_canonical_page_key` | function | `fn fusion_uses_canonical_page_key() {` | `fusion_uses_canonical_page_key [function]` | `dbf76817-ee41-55ac-a8cb-9ed7bb0c1559` | 183-225 [crates/gwiki/src/search/rrf.rs:183-225] | Indexed function `fusion_uses_canonical_page_key` in `crates/gwiki/src/search/rrf.rs`. [crates/gwiki/src/search/rrf.rs:183-225] |
| `fusion_rejects_invalid_utf8_paths` | function | `fn fusion_rejects_invalid_utf8_paths() {` | `fusion_rejects_invalid_utf8_paths [function]` | `92abeb5a-b0ae-58e1-8850-acb5b03c331a` | 229-240 [crates/gwiki/src/search/rrf.rs:229-240] | Indexed function `fusion_rejects_invalid_utf8_paths` in `crates/gwiki/src/search/rrf.rs`. [crates/gwiki/src/search/rrf.rs:229-240] |
| `search_result` | function | `fn search_result(id: &str, source: SearchSource) -> WikiSearchResult {` | `search_result [function]` | `c7c9774d-0fd0-51de-93df-b76b8da72b79` | 242-267 [crates/gwiki/src/search/rrf.rs:242-267] | Indexed function `search_result` in `crates/gwiki/src/search/rrf.rs`. [crates/gwiki/src/search/rrf.rs:242-267] |
