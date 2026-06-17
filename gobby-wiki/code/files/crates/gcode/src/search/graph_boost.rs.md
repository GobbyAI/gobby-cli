---
title: crates/gcode/src/search/graph_boost.rs
type: code_file
provenance:
- file: crates/gcode/src/search/graph_boost.rs
  ranges:
  - 21-47
  - 55-86
  - 88-106
  - 113-127
  - 129-153
  - 156-160
  - 163-167
  - 170-174
  - 177-223
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/search/graph_boost.rs:21-47](crates/gcode/src/search/graph_boost.rs#L21-L47), [crates/gcode/src/search/graph_boost.rs:55-86](crates/gcode/src/search/graph_boost.rs#L55-L86), [crates/gcode/src/search/graph_boost.rs:88-106](crates/gcode/src/search/graph_boost.rs#L88-L106), [crates/gcode/src/search/graph_boost.rs:113-127](crates/gcode/src/search/graph_boost.rs#L113-L127), [crates/gcode/src/search/graph_boost.rs:129-153](crates/gcode/src/search/graph_boost.rs#L129-L153), [crates/gcode/src/search/graph_boost.rs:156-160](crates/gcode/src/search/graph_boost.rs#L156-L160), [crates/gcode/src/search/graph_boost.rs:163-167](crates/gcode/src/search/graph_boost.rs#L163-L167), [crates/gcode/src/search/graph_boost.rs:170-174](crates/gcode/src/search/graph_boost.rs#L170-L174), [crates/gcode/src/search/graph_boost.rs:177-223](crates/gcode/src/search/graph_boost.rs#L177-L223)

</details>

# crates/gcode/src/search/graph_boost.rs

Module: [[code/modules/crates/gcode/src/search|crates/gcode/src/search]]

## Purpose

This file implements FalkorDB-backed graph boosting for search ranking. `graph_boost` resolves a query to an exact visible symbol, then gathers related caller and usage IDs from the code graph to produce a deduplicated boost list, returning empty results when graph support or a connection is unavailable. `graph_expand` and `graph_expand_grouped` broaden FTS or semantic search seeds by walking the graph neighborhood, grouping by project scope and deduping symbol IDs so the graph results can be fed into RRF ranking. The `make_ctx_no_falkordb` and `make_ctx_with_overlay` helpers set up test contexts, and the tests verify degraded behavior without FalkorDB, empty-seed handling, and grouped expansion/deduplication.
[crates/gcode/src/search/graph_boost.rs:21-47]
[crates/gcode/src/search/graph_boost.rs:55-86]
[crates/gcode/src/search/graph_boost.rs:88-106]
[crates/gcode/src/search/graph_boost.rs:113-127]
[crates/gcode/src/search/graph_boost.rs:129-153]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `graph_boost` | function | `pub fn graph_boost(ctx: &Context, conn: Option<&mut postgres::Client>, query: &str) -> Vec<String> {` | `graph_boost [function]` | `821967f5-60ed-567d-b11d-f9cfb2726a60` | 21-47 [crates/gcode/src/search/graph_boost.rs:21-47] | Indexed function `graph_boost` in `crates/gcode/src/search/graph_boost.rs`. [crates/gcode/src/search/graph_boost.rs:21-47] |
| `graph_expand` | function | `pub fn graph_expand(` | `graph_expand [function]` | `2cd40db1-4e53-5de4-be24-7b59e0b83a43` | 55-86 [crates/gcode/src/search/graph_boost.rs:55-86] | Indexed function `graph_expand` in `crates/gcode/src/search/graph_boost.rs`. [crates/gcode/src/search/graph_boost.rs:55-86] |
| `graph_expand_grouped` | function | `fn graph_expand_grouped(` | `graph_expand_grouped [function]` | `cdbdd7fb-61d4-5e31-b2bb-b1e42758c75a` | 88-106 [crates/gcode/src/search/graph_boost.rs:88-106] | Indexed function `graph_expand_grouped` in `crates/gcode/src/search/graph_boost.rs`. [crates/gcode/src/search/graph_boost.rs:88-106] |
| `make_ctx_no_falkordb` | function | `fn make_ctx_no_falkordb() -> Context {` | `make_ctx_no_falkordb [function]` | `fce20da6-a98f-553e-bfa7-bec5b8685476` | 113-127 [crates/gcode/src/search/graph_boost.rs:113-127] | Indexed function `make_ctx_no_falkordb` in `crates/gcode/src/search/graph_boost.rs`. [crates/gcode/src/search/graph_boost.rs:113-127] |
| `make_ctx_with_overlay` | function | `fn make_ctx_with_overlay() -> Context {` | `make_ctx_with_overlay [function]` | `8e07f24c-1345-5ff2-b99b-fa4256b92f7a` | 129-153 [crates/gcode/src/search/graph_boost.rs:129-153] | Indexed function `make_ctx_with_overlay` in `crates/gcode/src/search/graph_boost.rs`. [crates/gcode/src/search/graph_boost.rs:129-153] |
| `test_graph_boost_no_falkordb` | function | `fn test_graph_boost_no_falkordb() {` | `test_graph_boost_no_falkordb [function]` | `d2b29a0f-7fa5-5865-a104-83fe2cdd3eef` | 156-160 [crates/gcode/src/search/graph_boost.rs:156-160] | Indexed function `test_graph_boost_no_falkordb` in `crates/gcode/src/search/graph_boost.rs`. [crates/gcode/src/search/graph_boost.rs:156-160] |
| `test_graph_expand_no_falkordb` | function | `fn test_graph_expand_no_falkordb() {` | `test_graph_expand_no_falkordb [function]` | `8e475747-c493-5cc6-a3e7-f86a684ba506` | 163-167 [crates/gcode/src/search/graph_boost.rs:163-167] | Indexed function `test_graph_expand_no_falkordb` in `crates/gcode/src/search/graph_boost.rs`. [crates/gcode/src/search/graph_boost.rs:163-167] |
| `test_graph_expand_empty_seeds` | function | `fn test_graph_expand_empty_seeds() {` | `test_graph_expand_empty_seeds [function]` | `d0070db0-0756-5591-97c0-c2b4fa4bd3f2` | 170-174 [crates/gcode/src/search/graph_boost.rs:170-174] | Indexed function `test_graph_expand_empty_seeds` in `crates/gcode/src/search/graph_boost.rs`. [crates/gcode/src/search/graph_boost.rs:170-174] |
| `graph_expand_grouped_expands_each_project_scope_and_dedupes` | function | `fn graph_expand_grouped_expands_each_project_scope_and_dedupes() {` | `graph_expand_grouped_expands_each_project_scope_and_dedupes [function]` | `752226a9-8b51-5e80-97ec-354312b73330` | 177-223 [crates/gcode/src/search/graph_boost.rs:177-223] | Indexed function `graph_expand_grouped_expands_each_project_scope_and_dedupes` in `crates/gcode/src/search/graph_boost.rs`. [crates/gcode/src/search/graph_boost.rs:177-223] |
