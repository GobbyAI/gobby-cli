---
title: crates/gcode/src/index/indexer/file.rs
type: code_file
provenance:
- file: crates/gcode/src/index/indexer/file.rs
  ranges:
  - 15-91
  - 93-102
  - 104-111
  - 114-118
  - 120-130
  - 133-180
  - 182-232
  - 234-267
  - 278-284
  - 287-293
  - 296-302
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/indexer/file.rs:15-91](crates/gcode/src/index/indexer/file.rs#L15-L91), [crates/gcode/src/index/indexer/file.rs:93-102](crates/gcode/src/index/indexer/file.rs#L93-L102), [crates/gcode/src/index/indexer/file.rs:104-111](crates/gcode/src/index/indexer/file.rs#L104-L111), [crates/gcode/src/index/indexer/file.rs:114-118](crates/gcode/src/index/indexer/file.rs#L114-L118), [crates/gcode/src/index/indexer/file.rs:120-130](crates/gcode/src/index/indexer/file.rs#L120-L130), [crates/gcode/src/index/indexer/file.rs:133-180](crates/gcode/src/index/indexer/file.rs#L133-L180), [crates/gcode/src/index/indexer/file.rs:182-232](crates/gcode/src/index/indexer/file.rs#L182-L232), [crates/gcode/src/index/indexer/file.rs:234-267](crates/gcode/src/index/indexer/file.rs#L234-L267), [crates/gcode/src/index/indexer/file.rs:278-284](crates/gcode/src/index/indexer/file.rs#L278-L284), [crates/gcode/src/index/indexer/file.rs:287-293](crates/gcode/src/index/indexer/file.rs#L287-L293), [crates/gcode/src/index/indexer/file.rs:296-302](crates/gcode/src/index/indexer/file.rs#L296-L302)

</details>

# crates/gcode/src/index/indexer/file.rs

Module: [[code/modules/crates/gcode/src/index/indexer|crates/gcode/src/index/indexer]]

## Purpose

Implements file-level indexing for code ingestion. `index_file` resolves a file’s relative path, parses it with optional semantic call resolution, checks language, hash, and size, then writes indexed facts through a PostgreSQL sink inside a transaction; if parsing or file checks fail, it skips the file cleanly.

The rest of the file supports that flow: `create_semantic_resolver_if_needed` decides when to build a semantic resolver, `has_cpp_semantic_candidate` and `ExplicitFileRoute` help classify files and overrides, `explicit_file_route` maps explicit routing decisions, `index_content_only` handles files that should be indexed without AST parsing, and the `write_*_file_facts` helpers persist either parsed or content-only results. The C/C++/Objective-C candidate helpers control whether header files should enable C++ semantic resolution.
[crates/gcode/src/index/indexer/file.rs:15-91]
[crates/gcode/src/index/indexer/file.rs:93-102]
[crates/gcode/src/index/indexer/file.rs:104-111]
[crates/gcode/src/index/indexer/file.rs:114-118]
[crates/gcode/src/index/indexer/file.rs:120-130]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `index_file` | function | `pub(super) fn index_file(` | `index_file [function]` | `4b12832a-8119-5965-b9c6-d91d8cb4122e` | 15-91 [crates/gcode/src/index/indexer/file.rs:15-91] | Indexed function `index_file` in `crates/gcode/src/index/indexer/file.rs`. [crates/gcode/src/index/indexer/file.rs:15-91] |
| `create_semantic_resolver_if_needed` | function | `pub(super) fn create_semantic_resolver_if_needed(` | `create_semantic_resolver_if_needed [function]` | `c13ce350-3af8-5341-ba85-f91321f40cb2` | 93-102 [crates/gcode/src/index/indexer/file.rs:93-102] | Indexed function `create_semantic_resolver_if_needed` in `crates/gcode/src/index/indexer/file.rs`. [crates/gcode/src/index/indexer/file.rs:93-102] |
| `has_cpp_semantic_candidate` | function | `fn has_cpp_semantic_candidate(candidates: &[std::path::PathBuf]) -> bool {` | `has_cpp_semantic_candidate [function]` | `7846536d-02de-5352-9f00-328031a1f920` | 104-111 [crates/gcode/src/index/indexer/file.rs:104-111] | Indexed function `has_cpp_semantic_candidate` in `crates/gcode/src/index/indexer/file.rs`. [crates/gcode/src/index/indexer/file.rs:104-111] |
| `ExplicitFileRoute` | type | `pub(super) enum ExplicitFileRoute {` | `ExplicitFileRoute [type]` | `eab781bf-02a4-5af2-afd4-8040649b42c1` | 114-118 [crates/gcode/src/index/indexer/file.rs:114-118] | Indexed type `ExplicitFileRoute` in `crates/gcode/src/index/indexer/file.rs`. [crates/gcode/src/index/indexer/file.rs:114-118] |
| `explicit_file_route` | function | `pub(super) fn explicit_file_route(` | `explicit_file_route [function]` | `b2ae4aeb-cc2b-5288-b6f3-6c506cb6ea5f` | 120-130 [crates/gcode/src/index/indexer/file.rs:120-130] | Indexed function `explicit_file_route` in `crates/gcode/src/index/indexer/file.rs`. [crates/gcode/src/index/indexer/file.rs:120-130] |
| `index_content_only` | function | `pub(super) fn index_content_only(` | `index_content_only [function]` | `69dcf621-868a-5c80-b628-145cf500f3e8` | 133-180 [crates/gcode/src/index/indexer/file.rs:133-180] | Indexed function `index_content_only` in `crates/gcode/src/index/indexer/file.rs`. [crates/gcode/src/index/indexer/file.rs:133-180] |
| `write_parsed_file_facts` | function | `pub(super) fn write_parsed_file_facts(` | `write_parsed_file_facts [function]` | `92da3e5e-475e-5ff7-9971-5300dae54f89` | 182-232 [crates/gcode/src/index/indexer/file.rs:182-232] | Indexed function `write_parsed_file_facts` in `crates/gcode/src/index/indexer/file.rs`. [crates/gcode/src/index/indexer/file.rs:182-232] |
| `write_content_only_file_facts` | function | `pub(super) fn write_content_only_file_facts(` | `write_content_only_file_facts [function]` | `3cf1724d-1083-5537-9820-ad2a02c4378f` | 234-267 [crates/gcode/src/index/indexer/file.rs:234-267] | Indexed function `write_content_only_file_facts` in `crates/gcode/src/index/indexer/file.rs`. [crates/gcode/src/index/indexer/file.rs:234-267] |
| `c_header_candidates_enable_cpp_semantic_resolution` | function | `fn c_header_candidates_enable_cpp_semantic_resolution() {` | `c_header_candidates_enable_cpp_semantic_resolution [function]` | `e163b6fe-4e79-58d6-baaf-cc8d1fb5962e` | 278-284 [crates/gcode/src/index/indexer/file.rs:278-284] | Indexed function `c_header_candidates_enable_cpp_semantic_resolution` in `crates/gcode/src/index/indexer/file.rs`. [crates/gcode/src/index/indexer/file.rs:278-284] |
| `cpp_header_candidates_enable_cpp_semantic_resolution` | function | `fn cpp_header_candidates_enable_cpp_semantic_resolution() {` | `cpp_header_candidates_enable_cpp_semantic_resolution [function]` | `8cb8fe31-b5f9-58c5-9672-bb8a82437609` | 287-293 [crates/gcode/src/index/indexer/file.rs:287-293] | Indexed function `cpp_header_candidates_enable_cpp_semantic_resolution` in `crates/gcode/src/index/indexer/file.rs`. [crates/gcode/src/index/indexer/file.rs:287-293] |
| `objc_header_candidates_do_not_enable_cpp_semantic_resolution` | function | `fn objc_header_candidates_do_not_enable_cpp_semantic_resolution() {` | `objc_header_candidates_do_not_enable_cpp_semantic_resolution [function]` | `dc6a07a0-f110-5275-a17e-30d1ef9aa9b9` | 296-302 [crates/gcode/src/index/indexer/file.rs:296-302] | Indexed function `objc_header_candidates_do_not_enable_cpp_semantic_resolution` in `crates/gcode/src/index/indexer/file.rs`. [crates/gcode/src/index/indexer/file.rs:296-302] |
