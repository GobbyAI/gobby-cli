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

# crates/gcode/src/search/graph_boost.rs

Module: [[code/modules/crates/gcode/src/search|crates/gcode/src/search]]

## Purpose

`crates/gcode/src/search/graph_boost.rs` exposes 9 indexed API symbols.
[crates/gcode/src/search/graph_boost.rs:21-47]
[crates/gcode/src/search/graph_boost.rs:55-86]
[crates/gcode/src/search/graph_boost.rs:88-106]
[crates/gcode/src/search/graph_boost.rs:113-127]
[crates/gcode/src/search/graph_boost.rs:129-153]
[crates/gcode/src/search/graph_boost.rs:156-160]
[crates/gcode/src/search/graph_boost.rs:163-167]
[crates/gcode/src/search/graph_boost.rs:170-174]
[crates/gcode/src/search/graph_boost.rs:177-223]

## API Symbols

- `graph_boost` (function) component `graph_boost [function]` (`821967f5-60ed-567d-b11d-f9cfb2726a60`) lines 21-47 [crates/gcode/src/search/graph_boost.rs:21-47]
  - Signature: `pub fn graph_boost(ctx: &Context, conn: Option<&mut postgres::Client>, query: &str) -> Vec<String> {`
  - Purpose: Indexed function `graph_boost` in `crates/gcode/src/search/graph_boost.rs`. [crates/gcode/src/search/graph_boost.rs:21-47]
- `graph_expand` (function) component `graph_expand [function]` (`2cd40db1-4e53-5de4-be24-7b59e0b83a43`) lines 55-86 [crates/gcode/src/search/graph_boost.rs:55-86]
  - Signature: `pub fn graph_expand(`
  - Purpose: Indexed function `graph_expand` in `crates/gcode/src/search/graph_boost.rs`. [crates/gcode/src/search/graph_boost.rs:55-86]
- `graph_expand_grouped` (function) component `graph_expand_grouped [function]` (`cdbdd7fb-61d4-5e31-b2bb-b1e42758c75a`) lines 88-106 [crates/gcode/src/search/graph_boost.rs:88-106]
  - Signature: `fn graph_expand_grouped(`
  - Purpose: Indexed function `graph_expand_grouped` in `crates/gcode/src/search/graph_boost.rs`. [crates/gcode/src/search/graph_boost.rs:88-106]
- `make_ctx_no_falkordb` (function) component `make_ctx_no_falkordb [function]` (`fce20da6-a98f-553e-bfa7-bec5b8685476`) lines 113-127 [crates/gcode/src/search/graph_boost.rs:113-127]
  - Signature: `fn make_ctx_no_falkordb() -> Context {`
  - Purpose: Indexed function `make_ctx_no_falkordb` in `crates/gcode/src/search/graph_boost.rs`. [crates/gcode/src/search/graph_boost.rs:113-127]
- `make_ctx_with_overlay` (function) component `make_ctx_with_overlay [function]` (`8e07f24c-1345-5ff2-b99b-fa4256b92f7a`) lines 129-153 [crates/gcode/src/search/graph_boost.rs:129-153]
  - Signature: `fn make_ctx_with_overlay() -> Context {`
  - Purpose: Indexed function `make_ctx_with_overlay` in `crates/gcode/src/search/graph_boost.rs`. [crates/gcode/src/search/graph_boost.rs:129-153]
- `test_graph_boost_no_falkordb` (function) component `test_graph_boost_no_falkordb [function]` (`d2b29a0f-7fa5-5865-a104-83fe2cdd3eef`) lines 156-160 [crates/gcode/src/search/graph_boost.rs:156-160]
  - Signature: `fn test_graph_boost_no_falkordb() {`
  - Purpose: Indexed function `test_graph_boost_no_falkordb` in `crates/gcode/src/search/graph_boost.rs`. [crates/gcode/src/search/graph_boost.rs:156-160]
- `test_graph_expand_no_falkordb` (function) component `test_graph_expand_no_falkordb [function]` (`8e475747-c493-5cc6-a3e7-f86a684ba506`) lines 163-167 [crates/gcode/src/search/graph_boost.rs:163-167]
  - Signature: `fn test_graph_expand_no_falkordb() {`
  - Purpose: Indexed function `test_graph_expand_no_falkordb` in `crates/gcode/src/search/graph_boost.rs`. [crates/gcode/src/search/graph_boost.rs:163-167]
- `test_graph_expand_empty_seeds` (function) component `test_graph_expand_empty_seeds [function]` (`d0070db0-0756-5591-97c0-c2b4fa4bd3f2`) lines 170-174 [crates/gcode/src/search/graph_boost.rs:170-174]
  - Signature: `fn test_graph_expand_empty_seeds() {`
  - Purpose: Indexed function `test_graph_expand_empty_seeds` in `crates/gcode/src/search/graph_boost.rs`. [crates/gcode/src/search/graph_boost.rs:170-174]
- `graph_expand_grouped_expands_each_project_scope_and_dedupes` (function) component `graph_expand_grouped_expands_each_project_scope_and_dedupes [function]` (`752226a9-8b51-5e80-97ec-354312b73330`) lines 177-223 [crates/gcode/src/search/graph_boost.rs:177-223]
  - Signature: `fn graph_expand_grouped_expands_each_project_scope_and_dedupes() {`
  - Purpose: Indexed function `graph_expand_grouped_expands_each_project_scope_and_dedupes` in `crates/gcode/src/search/graph_boost.rs`. [crates/gcode/src/search/graph_boost.rs:177-223]

