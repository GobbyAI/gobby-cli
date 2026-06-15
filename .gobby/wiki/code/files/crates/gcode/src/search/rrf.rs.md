---
title: crates/gcode/src/search/rrf.rs
type: code_file
provenance:
- file: crates/gcode/src/search/rrf.rs
  ranges:
  - '7'
  - 15-20
  - 27-34
  - 37-49
  - 52-64
  - 67-75
  - 78-81
  - 84-87
  - 90-113
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/search/rrf.rs

Module: [[code/modules/crates/gcode/src/search|crates/gcode/src/search]]

## Purpose

This file provides a thin Reciprocal Rank Fusion wrapper for search results. It defines `MergedResult` as `(symbol_id, combined_score, source_names)` and exposes `merge`, which delegates to `gobby_core::search::rrf_merge` and converts the returned fused items into that tuple form; the tests exercise single-source ordering, duplicate and disjoint source merging, empty input handling, deterministic source ordering, and delegation behavior.
[crates/gcode/src/search/rrf.rs:7]
[crates/gcode/src/search/rrf.rs:15-20]
[crates/gcode/src/search/rrf.rs:27-34]
[crates/gcode/src/search/rrf.rs:37-49]
[crates/gcode/src/search/rrf.rs:52-64]

## API Symbols

- `MergedResult` (type) component `MergedResult [type]` (`4f252f0f-f18a-5b74-97a4-740bcaaa731d`) lines 7-7 [crates/gcode/src/search/rrf.rs:7]
  - Signature: `pub type MergedResult = (String, f64, Vec<String>);`
  - Purpose: Indexed type `MergedResult` in `crates/gcode/src/search/rrf.rs`. [crates/gcode/src/search/rrf.rs:7]
- `merge` (function) component `merge [function]` (`ee7eabc0-8008-50d8-9fde-f2a283bc7fe5`) lines 15-20 [crates/gcode/src/search/rrf.rs:15-20]
  - Signature: `pub fn merge(sources: Vec<(&str, Vec<String>)>) -> Vec<MergedResult> {`
  - Purpose: Calls 'gobby_core::search::rrf_merge' on the provided '(source_name, results)' pairs and converts each merged item into a 'MergedResult' by collecting its 'id', 'score', and 'sources'. [crates/gcode/src/search/rrf.rs:15-20]
- `test_merge_single_source` (function) component `test_merge_single_source [function]` (`22a35146-0b3d-5a8b-a030-3da3a66883cd`) lines 27-34 [crates/gcode/src/search/rrf.rs:27-34]
  - Signature: `fn test_merge_single_source() {`
  - Purpose: Verifies that merging a single source returns all three items in descending score order, with 'a' ranked first and each subsequent result having a lower score than the previous one. [crates/gcode/src/search/rrf.rs:27-34]
- `test_merge_two_sources_same_ids` (function) component `test_merge_two_sources_same_ids [function]` (`873d4c1e-dd07-58fe-a832-e784dabd9689`) lines 37-49 [crates/gcode/src/search/rrf.rs:37-49]
  - Signature: `fn test_merge_two_sources_same_ids() {`
  - Purpose: Verifies that merging two ranked sources with the same top result assigns that item the combined rank-zero score from both sources, records both contributing ranks, and orders it first in the merged results. [crates/gcode/src/search/rrf.rs:37-49]
- `test_merge_sorts_sources_deterministically` (function) component `test_merge_sorts_sources_deterministically [function]` (`58647f00-fd39-5646-bad7-155c0cbd79f2`) lines 52-64 [crates/gcode/src/search/rrf.rs:52-64]
  - Signature: `fn test_merge_sorts_sources_deterministically() {`
  - Purpose: Verifies that 'merge' produces a deterministic ordering by sorting results by key and, for equal keys, ordering source labels consistently as 'fts' before 'semantic'. [crates/gcode/src/search/rrf.rs:52-64]
- `test_merge_two_sources_disjoint` (function) component `test_merge_two_sources_disjoint [function]` (`84046dbc-3560-568e-a490-df5f55d17f96`) lines 67-75 [crates/gcode/src/search/rrf.rs:67-75]
  - Signature: `fn test_merge_two_sources_disjoint() {`
  - Purpose: Verifies that merging two disjoint source result sets preserves both entries, assigns them equal scores, and keeps each result associated with exactly one source. [crates/gcode/src/search/rrf.rs:67-75]
- `test_merge_empty_sources` (function) component `test_merge_empty_sources [function]` (`76109a10-3a96-55e7-bf6b-0ebfdd2fcb4a`) lines 78-81 [crates/gcode/src/search/rrf.rs:78-81]
  - Signature: `fn test_merge_empty_sources() {`
  - Purpose: Verifies that 'merge' returns an empty collection when called with an empty vector of sources. [crates/gcode/src/search/rrf.rs:78-81]
- `test_merge_empty_id_lists` (function) component `test_merge_empty_id_lists [function]` (`8cb6830f-e7a6-5d3f-b87c-ad56c1e35dd1`) lines 84-87 [crates/gcode/src/search/rrf.rs:84-87]
  - Signature: `fn test_merge_empty_id_lists() {`
  - Purpose: Verifies that 'merge' returns an empty result when given multiple sources whose ID lists are all empty. [crates/gcode/src/search/rrf.rs:84-87]
- `merge_delegates_to_gobby_core_rrf` (function) component `merge_delegates_to_gobby_core_rrf [function]` (`239158ff-3daf-584d-b001-791e25c54319`) lines 90-113 [crates/gcode/src/search/rrf.rs:90-113]
  - Signature: `fn merge_delegates_to_gobby_core_rrf() {`
  - Purpose: Verifies that 'merge' produces the same ranked-reciprocal-fusion results as 'gobby_core::search::rrf_merge' for duplicate-containing search-source inputs, matching item IDs, scores within '1e-10', and source provenance, while asserting the implementation delegates to 'gobby_core' and does not define a local 'RRF_K' constant. [crates/gcode/src/search/rrf.rs:90-113]

