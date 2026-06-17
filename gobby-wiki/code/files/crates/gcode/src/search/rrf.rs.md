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

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/search/rrf.rs:7](crates/gcode/src/search/rrf.rs#L7), [crates/gcode/src/search/rrf.rs:15-20](crates/gcode/src/search/rrf.rs#L15-L20), [crates/gcode/src/search/rrf.rs:27-34](crates/gcode/src/search/rrf.rs#L27-L34), [crates/gcode/src/search/rrf.rs:37-49](crates/gcode/src/search/rrf.rs#L37-L49), [crates/gcode/src/search/rrf.rs:52-64](crates/gcode/src/search/rrf.rs#L52-L64), [crates/gcode/src/search/rrf.rs:67-75](crates/gcode/src/search/rrf.rs#L67-L75), [crates/gcode/src/search/rrf.rs:78-81](crates/gcode/src/search/rrf.rs#L78-L81), [crates/gcode/src/search/rrf.rs:84-87](crates/gcode/src/search/rrf.rs#L84-L87), [crates/gcode/src/search/rrf.rs:90-113](crates/gcode/src/search/rrf.rs#L90-L113)

</details>

# crates/gcode/src/search/rrf.rs

Module: [[code/modules/crates/gcode/src/search|crates/gcode/src/search]]

## Purpose

This file defines the `MergedResult` tuple type and a `merge` wrapper for Reciprocal Rank Fusion over multiple ranked result lists. `merge` accepts `(source_name, ranked_ids)` inputs, delegates the actual fusion to `gobby_core::search::rrf_merge`, and converts the core result objects into `(id, score, sources)` tuples sorted by descending score. The test module verifies single-source ranking, combining duplicate ids across sources, deterministic ordering of equal-score sources, disjoint inputs, empty inputs, and delegation behavior.
[crates/gcode/src/search/rrf.rs:7]
[crates/gcode/src/search/rrf.rs:15-20]
[crates/gcode/src/search/rrf.rs:27-34]
[crates/gcode/src/search/rrf.rs:37-49]
[crates/gcode/src/search/rrf.rs:52-64]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `MergedResult` | type | `pub type MergedResult = (String, f64, Vec<String>);` | `MergedResult [type]` | `4f252f0f-f18a-5b74-97a4-740bcaaa731d` | 7-7 [crates/gcode/src/search/rrf.rs:7] | Indexed type `MergedResult` in `crates/gcode/src/search/rrf.rs`. [crates/gcode/src/search/rrf.rs:7] |
| `merge` | function | `pub fn merge(sources: Vec<(&str, Vec<String>)>) -> Vec<MergedResult> {` | `merge [function]` | `ee7eabc0-8008-50d8-9fde-f2a283bc7fe5` | 15-20 [crates/gcode/src/search/rrf.rs:15-20] | Indexed function `merge` in `crates/gcode/src/search/rrf.rs`. [crates/gcode/src/search/rrf.rs:15-20] |
| `test_merge_single_source` | function | `fn test_merge_single_source() {` | `test_merge_single_source [function]` | `22a35146-0b3d-5a8b-a030-3da3a66883cd` | 27-34 [crates/gcode/src/search/rrf.rs:27-34] | Indexed function `test_merge_single_source` in `crates/gcode/src/search/rrf.rs`. [crates/gcode/src/search/rrf.rs:27-34] |
| `test_merge_two_sources_same_ids` | function | `fn test_merge_two_sources_same_ids() {` | `test_merge_two_sources_same_ids [function]` | `873d4c1e-dd07-58fe-a832-e784dabd9689` | 37-49 [crates/gcode/src/search/rrf.rs:37-49] | Indexed function `test_merge_two_sources_same_ids` in `crates/gcode/src/search/rrf.rs`. [crates/gcode/src/search/rrf.rs:37-49] |
| `test_merge_sorts_sources_deterministically` | function | `fn test_merge_sorts_sources_deterministically() {` | `test_merge_sorts_sources_deterministically [function]` | `58647f00-fd39-5646-bad7-155c0cbd79f2` | 52-64 [crates/gcode/src/search/rrf.rs:52-64] | Indexed function `test_merge_sorts_sources_deterministically` in `crates/gcode/src/search/rrf.rs`. [crates/gcode/src/search/rrf.rs:52-64] |
| `test_merge_two_sources_disjoint` | function | `fn test_merge_two_sources_disjoint() {` | `test_merge_two_sources_disjoint [function]` | `84046dbc-3560-568e-a490-df5f55d17f96` | 67-75 [crates/gcode/src/search/rrf.rs:67-75] | Indexed function `test_merge_two_sources_disjoint` in `crates/gcode/src/search/rrf.rs`. [crates/gcode/src/search/rrf.rs:67-75] |
| `test_merge_empty_sources` | function | `fn test_merge_empty_sources() {` | `test_merge_empty_sources [function]` | `76109a10-3a96-55e7-bf6b-0ebfdd2fcb4a` | 78-81 [crates/gcode/src/search/rrf.rs:78-81] | Indexed function `test_merge_empty_sources` in `crates/gcode/src/search/rrf.rs`. [crates/gcode/src/search/rrf.rs:78-81] |
| `test_merge_empty_id_lists` | function | `fn test_merge_empty_id_lists() {` | `test_merge_empty_id_lists [function]` | `8cb6830f-e7a6-5d3f-b87c-ad56c1e35dd1` | 84-87 [crates/gcode/src/search/rrf.rs:84-87] | Indexed function `test_merge_empty_id_lists` in `crates/gcode/src/search/rrf.rs`. [crates/gcode/src/search/rrf.rs:84-87] |
| `merge_delegates_to_gobby_core_rrf` | function | `fn merge_delegates_to_gobby_core_rrf() {` | `merge_delegates_to_gobby_core_rrf [function]` | `239158ff-3daf-584d-b001-791e25c54319` | 90-113 [crates/gcode/src/search/rrf.rs:90-113] | Indexed function `merge_delegates_to_gobby_core_rrf` in `crates/gcode/src/search/rrf.rs`. [crates/gcode/src/search/rrf.rs:90-113] |
