---
title: crates/gcode/src/index/indexer/file.rs
type: code_file
provenance:
- file: crates/gcode/src/index/indexer/file.rs
  ranges:
  - 15-91
  - 93-108
  - 111-115
  - 117-127
  - 130-177
  - 179-223
  - 225-258
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/indexer/file.rs

Module: [[code/modules/crates/gcode/src/index/indexer|crates/gcode/src/index/indexer]]

## Purpose

`crates/gcode/src/index/indexer/file.rs` exposes 7 indexed API symbols.
[crates/gcode/src/index/indexer/file.rs:15-91]
[crates/gcode/src/index/indexer/file.rs:93-108]
[crates/gcode/src/index/indexer/file.rs:111-115]
[crates/gcode/src/index/indexer/file.rs:117-127]
[crates/gcode/src/index/indexer/file.rs:130-177]
[crates/gcode/src/index/indexer/file.rs:179-223]
[crates/gcode/src/index/indexer/file.rs:225-258]

## API Symbols

- `index_file` (function) component `index_file [function]` (`4b12832a-8119-5965-b9c6-d91d8cb4122e`) lines 15-91 [crates/gcode/src/index/indexer/file.rs:15-91]
  - Signature: `pub(super) fn index_file(`
  - Purpose: Parses a source file with semantic analysis and transactionally writes the extracted code facts to a PostgreSQL database, returning index operation counts. [crates/gcode/src/index/indexer/file.rs:15-91]
- `create_semantic_resolver_if_needed` (function) component `create_semantic_resolver_if_needed [function]` (`c13ce350-3af8-5341-ba85-f91321f40cb2`) lines 93-108 [crates/gcode/src/index/indexer/file.rs:93-108]
  - Signature: `pub(super) fn create_semantic_resolver_if_needed(`
  - Purpose: Conditionally instantiates a C++ semantic call resolver by detecting C/C++ source files among candidate paths and delegating to `create_cpp_semantic_resolver` if found, returning `None` otherwise. [crates/gcode/src/index/indexer/file.rs:93-108]
- `ExplicitFileRoute` (type) component `ExplicitFileRoute [type]` (`e0425afb-6091-5f4b-8ed8-0077a7cbdbc8`) lines 111-115 [crates/gcode/src/index/indexer/file.rs:111-115]
  - Signature: `pub(super) enum ExplicitFileRoute {`
  - Purpose: Indexed type `ExplicitFileRoute` in `crates/gcode/src/index/indexer/file.rs`. [crates/gcode/src/index/indexer/file.rs:111-115]
- `explicit_file_route` (function) component `explicit_file_route [function]` (`a46733a5-8a30-596e-a98c-6214e9693bde`) lines 117-127 [crates/gcode/src/index/indexer/file.rs:117-127]
  - Signature: `pub(super) fn explicit_file_route(`
  - Purpose: Classifies a file against exclude patterns and returns an `ExplicitFileRoute` enum variant indicating whether the file should be processed for AST parsing, content-only access, or skipped. [crates/gcode/src/index/indexer/file.rs:117-127]
- `index_content_only` (function) component `index_content_only [function]` (`b07b2215-4ef6-53de-9d92-eef5f90e3aec`) lines 130-177 [crates/gcode/src/index/indexer/file.rs:130-177]
  - Signature: `pub(super) fn index_content_only(`
  - Purpose: Indexes a file's content to PostgreSQL by validating it against exclusion patterns, computing its language and content hash, and transactionally writing content-only metadata. [crates/gcode/src/index/indexer/file.rs:130-177]
- `write_parsed_file_facts` (function) component `write_parsed_file_facts [function]` (`8db19430-dba8-52b8-b94c-ebd14b9c1b71`) lines 179-223 [crates/gcode/src/index/indexer/file.rs:179-223]
  - Signature: `pub(super) fn write_parsed_file_facts(`
  - Purpose: Persists parsed code analysis results (symbols, imports, function calls, and content chunks) to a fact sink and returns aggregated indexing counts. [crates/gcode/src/index/indexer/file.rs:179-223]
- `write_content_only_file_facts` (function) component `write_content_only_file_facts [function]` (`12e0f099-e3f9-5b7a-92a8-df26816e0fb7`) lines 225-258 [crates/gcode/src/index/indexer/file.rs:225-258]
  - Signature: `pub(super) fn write_content_only_file_facts(`
  - Purpose: Replaces a file's prior index facts by upserting updated metadata and content chunks to a code fact sink, returning indexing statistics. [crates/gcode/src/index/indexer/file.rs:225-258]

