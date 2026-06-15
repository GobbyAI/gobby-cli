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
  - 179-229
  - 231-264
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/indexer/file.rs

Module: [[code/modules/crates/gcode/src/index/indexer|crates/gcode/src/index/indexer]]

## Purpose

This file implements per-file indexing for the codebase. It decides whether a path should be skipped, parsed as an AST-backed file, or handled as content-only, then resolves relative paths, detects language, hashes content, reads size, and persists the resulting facts in PostgreSQL through transactional writes. The parsed-file path uses semantic import resolution when needed and writes symbols, imports, calls, metadata, and chunks; the content-only path skips parsing and stores raw file facts and chunks instead. Supporting helpers choose a C/C++ semantic resolver only when required and map walker classifications into the explicit file-routing mode used by the indexer.
[crates/gcode/src/index/indexer/file.rs:15-91]
[crates/gcode/src/index/indexer/file.rs:93-108]
[crates/gcode/src/index/indexer/file.rs:111-115]
[crates/gcode/src/index/indexer/file.rs:117-127]
[crates/gcode/src/index/indexer/file.rs:130-177]

## API Symbols

- `index_file` (function) component `index_file [function]` (`4b12832a-8119-5965-b9c6-d91d8cb4122e`) lines 15-91 [crates/gcode/src/index/indexer/file.rs:15-91]
  - Signature: `pub(super) fn index_file(`
  - Purpose: Indexes a file by resolving its relative path, parsing it with semantic import resolution, detecting its language, hashing its contents, reading its size, and then persisting parsed code facts in a PostgreSQL transaction, returning 'None' for skipped/unreadable/unparseable files or 'Some(FileIndexCounts)' on success. [crates/gcode/src/index/indexer/file.rs:15-91]
- `create_semantic_resolver_if_needed` (function) component `create_semantic_resolver_if_needed [function]` (`c13ce350-3af8-5341-ba85-f91321f40cb2`) lines 93-108 [crates/gcode/src/index/indexer/file.rs:93-108]
  - Signature: `pub(super) fn create_semantic_resolver_if_needed(`
  - Purpose: Returns 'Ok(None)' unless any candidate path is detected as C/C++, in which case it delegates to 'semantic::create_cpp_semantic_resolver(root_path, require_cpp_semantics)' and returns that result as an optional boxed 'SemanticCallResolver'. [crates/gcode/src/index/indexer/file.rs:93-108]
- `ExplicitFileRoute` (type) component `ExplicitFileRoute [type]` (`e0425afb-6091-5f4b-8ed8-0077a7cbdbc8`) lines 111-115 [crates/gcode/src/index/indexer/file.rs:111-115]
  - Signature: `pub(super) enum ExplicitFileRoute {`
  - Purpose: Indexed type `ExplicitFileRoute` in `crates/gcode/src/index/indexer/file.rs`. [crates/gcode/src/index/indexer/file.rs:111-115]
- `explicit_file_route` (function) component `explicit_file_route [function]` (`a46733a5-8a30-596e-a98c-6214e9693bde`) lines 117-127 [crates/gcode/src/index/indexer/file.rs:117-127]
  - Signature: `pub(super) fn explicit_file_route(`
  - Purpose: Maps 'walker::classify_file(root_path, path, exclude_patterns)' to an 'ExplicitFileRoute', returning 'Ast' for 'FileClassification::Ast', 'ContentOnly' for 'ContentOnly', and 'Skip' when the file is not classified. [crates/gcode/src/index/indexer/file.rs:117-127]
- `index_content_only` (function) component `index_content_only [function]` (`b07b2215-4ef6-53de-9d92-eef5f90e3aec`) lines 130-177 [crates/gcode/src/index/indexer/file.rs:130-177]
  - Signature: `pub(super) fn index_content_only(`
  - Purpose: 'index_content_only' conditionally indexes a file’s raw contents into Postgres by filtering against indexability rules, resolving its relative path, reading bytes, computing language and content hash, writing content-only facts in a transaction, and returning 'Some(FileIndexCounts)' or 'None' when skipped or unreadable. [crates/gcode/src/index/indexer/file.rs:130-177]
- `write_parsed_file_facts` (function) component `write_parsed_file_facts [function]` (`8db19430-dba8-52b8-b94c-ebd14b9c1b71`) lines 179-229 [crates/gcode/src/index/indexer/file.rs:179-229]
  - Signature: `pub(super) fn write_parsed_file_facts(`
  - Purpose: Updates the indexed facts for a parsed file by upserting symbols, imports, calls, file metadata, and content chunks, deleting stale symbol/non-symbol records first, and returning per-category indexing counts. [crates/gcode/src/index/indexer/file.rs:179-229]
- `write_content_only_file_facts` (function) component `write_content_only_file_facts [function]` (`30dacd9b-2dd5-5b96-ae60-f434036b7dca`) lines 231-264 [crates/gcode/src/index/indexer/file.rs:231-264]
  - Signature: `pub(super) fn write_content_only_file_facts(`
  - Purpose: Deletes any existing facts for the file, upserts an 'IndexedFile' record with zero symbols and the supplied metadata, chunks the file bytes for content indexing, writes those chunks if any, and returns 'FileIndexCounts' reflecting one indexed file and the number of chunks stored. [crates/gcode/src/index/indexer/file.rs:231-264]

