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

## API Symbols

- `graph_boost` (function) component `graph_boost [function]` (`821967f5-60ed-567d-b11d-f9cfb2726a60`) lines 21-47 [crates/gcode/src/search/graph_boost.rs:21-47]
  - Signature: `pub fn graph_boost(ctx: &Context, conn: Option<&mut postgres::Client>, query: &str) -> Vec<String> {`
  - Purpose: Resolves a query to a symbol via full-text search and returns up to 20 deduplicated caller and usage identifier references from the code graph. [crates/gcode/src/search/graph_boost.rs:21-47]
- `graph_expand` (function) component `graph_expand [function]` (`2cd40db1-4e53-5de4-be24-7b59e0b83a43`) lines 55-86 [crates/gcode/src/search/graph_boost.rs:55-86]
  - Signature: `pub fn graph_expand(`
  - Purpose: Expands seed symbol IDs by querying the code graph for their visible callees and callers, batched by project up to 30 per direction. [crates/gcode/src/search/graph_boost.rs:55-86]
- `graph_expand_grouped` (function) component `graph_expand_grouped [function]` (`cdbdd7fb-61d4-5e31-b2bb-b1e42758c75a`) lines 88-106 [crates/gcode/src/search/graph_boost.rs:88-106]
  - Signature: `fn graph_expand_grouped(`
  - Purpose: Expands grouped identifiers by retrieving all unique callee and caller nodes in a call graph across multiple projects with project-specific visibility contexts. [crates/gcode/src/search/graph_boost.rs:88-106]
- `make_ctx_no_falkordb` (function) component `make_ctx_no_falkordb [function]` (`fce20da6-a98f-553e-bfa7-bec5b8685476`) lines 113-127 [crates/gcode/src/search/graph_boost.rs:113-127]
  - Signature: `fn make_ctx_no_falkordb() -> Context {`
  - Purpose: Instantiates a Context struct with invalid PostgreSQL/filesystem paths and None-valued optional vector database and embedding fields for isolated unit testing. [crates/gcode/src/search/graph_boost.rs:113-127]
- `make_ctx_with_overlay` (function) component `make_ctx_with_overlay [function]` (`8e07f24c-1345-5ff2-b99b-fa4256b92f7a`) lines 129-153 [crates/gcode/src/search/graph_boost.rs:129-153]
  - Signature: `fn make_ctx_with_overlay() -> Context {`
  - Purpose: Instantiates a `Context` struct configured for overlay-mode code indexing with FalkorDB as the graph database backend. [crates/gcode/src/search/graph_boost.rs:129-153]
- `test_graph_boost_no_falkordb` (function) component `test_graph_boost_no_falkordb [function]` (`d2b29a0f-7fa5-5865-a104-83fe2cdd3eef`) lines 156-160 [crates/gcode/src/search/graph_boost.rs:156-160]
  - Signature: `fn test_graph_boost_no_falkordb() {`
  - Purpose: This test verifies that `graph_boost` returns an empty result when invoked on a context without FalkorDB available. [crates/gcode/src/search/graph_boost.rs:156-160]
- `test_graph_expand_no_falkordb` (function) component `test_graph_expand_no_falkordb [function]` (`8e475747-c493-5cc6-a3e7-f86a684ba506`) lines 163-167 [crates/gcode/src/search/graph_boost.rs:163-167]
  - Signature: `fn test_graph_expand_no_falkordb() {`
  - Purpose: This test asserts that `graph_expand()` returns an empty result when called with a context that lacks FalkorDB. [crates/gcode/src/search/graph_boost.rs:163-167]
- `test_graph_expand_empty_seeds` (function) component `test_graph_expand_empty_seeds [function]` (`d0070db0-0756-5591-97c0-c2b4fa4bd3f2`) lines 170-174 [crates/gcode/src/search/graph_boost.rs:170-174]
  - Signature: `fn test_graph_expand_empty_seeds() {`
  - Purpose: Tests that `graph_expand` returns an empty collection when invoked with an empty seeds array. [crates/gcode/src/search/graph_boost.rs:170-174]
- `graph_expand_grouped_expands_each_project_scope_and_dedupes` (function) component `graph_expand_grouped_expands_each_project_scope_and_dedupes [function]` (`752226a9-8b51-5e80-97ec-354312b73330`) lines 177-223 [crates/gcode/src/search/graph_boost.rs:177-223]
  - Signature: `fn graph_expand_grouped_expands_each_project_scope_and_dedupes() {`
  - Purpose: This test validates that `graph_expand_grouped` invokes the provided callback once per project with its respective seed identifiers and returns a deduplicated union of all combined implementation and caller results across projects. [crates/gcode/src/search/graph_boost.rs:177-223]

