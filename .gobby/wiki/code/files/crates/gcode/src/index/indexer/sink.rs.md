---
title: crates/gcode/src/index/indexer/sink.rs
type: code_file
provenance:
- file: crates/gcode/src/index/indexer/sink.rs
  ranges:
  - 6-23
  - 25-27
  - 30-32
  - 39-41
  - 43-45
  - 47-49
  - 51-58
  - 60-67
  - 69-71
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/indexer/sink.rs

Module: [[code/modules/crates/gcode/src/index/indexer|crates/gcode/src/index/indexer]]

## Purpose

`crates/gcode/src/index/indexer/sink.rs` exposes 9 indexed API symbols.
[crates/gcode/src/index/indexer/sink.rs:6-23]
[crates/gcode/src/index/indexer/sink.rs:25-27]
[crates/gcode/src/index/indexer/sink.rs:30-32]
[crates/gcode/src/index/indexer/sink.rs:39-41]
[crates/gcode/src/index/indexer/sink.rs:43-45]

## API Symbols

- `CodeFactSink` (type) component `CodeFactSink [type]` (`4beb9119-9fd1-58f8-95af-7e14c1d44a43`) lines 6-23 [crates/gcode/src/index/indexer/sink.rs:6-23]
  - Signature: `pub(super) trait CodeFactSink {`
  - Purpose: Indexed type `CodeFactSink` in `crates/gcode/src/index/indexer/sink.rs`. [crates/gcode/src/index/indexer/sink.rs:6-23]
- `PostgresCodeFactSink` (class) component `PostgresCodeFactSink [class]` (`6578a9d1-4e4d-5d6d-9197-c64ec5e16239`) lines 25-27 [crates/gcode/src/index/indexer/sink.rs:25-27]
  - Signature: `pub(super) struct PostgresCodeFactSink<'a, C> {`
  - Purpose: `PostgresCodeFactSink` is a generic struct that wraps a mutable borrow of a connection type to serve as a consumer/writer for PostgreSQL code facts. [crates/gcode/src/index/indexer/sink.rs:25-27]
- `new` (function) component `new [function]` (`ec5def8c-dc52-5a92-a864-1dfcd015079c`) lines 30-32 [crates/gcode/src/index/indexer/sink.rs:30-32]
  - Signature: `pub(super) fn new(conn: &'a mut C) -> Self {`
  - Purpose: A `pub(super)` constructor that initializes a new `Self` instance by storing a mutable reference to a generic connection parameter with lifetime `'a`. [crates/gcode/src/index/indexer/sink.rs:30-32]
- `delete_file_facts` (function) component `delete_file_facts [function]` (`0825fe8c-547a-555c-9c93-4a0d561197b1`) lines 39-41 [crates/gcode/src/index/indexer/sink.rs:39-41]
  - Signature: `fn delete_file_facts(&mut self, project_id: &str, file_path: &str) -> anyhow::Result<()> {`
  - Purpose: Deletes file facts (metadata) associated with a specified file path in a given project by delegating to the API layer, returning a Result indicating success or error. [crates/gcode/src/index/indexer/sink.rs:39-41]
- `upsert_symbols` (function) component `upsert_symbols [function]` (`164a66d5-f445-53a0-9684-3bb76f632df8`) lines 43-45 [crates/gcode/src/index/indexer/sink.rs:43-45]
  - Signature: `fn upsert_symbols(&mut self, symbols: &[Symbol]) -> anyhow::Result<usize> {`
  - Purpose: Inserts or updates the provided symbols in the database via a delegated API call, returning the count of affected rows or an error. [crates/gcode/src/index/indexer/sink.rs:43-45]
- `upsert_file` (function) component `upsert_file [function]` (`f083153c-891f-56c8-8041-85b5b6ab3aad`) lines 47-49 [crates/gcode/src/index/indexer/sink.rs:47-49]
  - Signature: `fn upsert_file(&mut self, file: &IndexedFile) -> anyhow::Result<()> {`
  - Purpose: This method delegates insertion or updating of an `IndexedFile` record to an API function via the instance's database connection, returning `Result<()>` to indicate success or error. [crates/gcode/src/index/indexer/sink.rs:47-49]
- `upsert_imports` (function) component `upsert_imports [function]` (`48c56b0d-0f92-5092-b4c2-aabab24faf1c`) lines 51-58 [crates/gcode/src/index/indexer/sink.rs:51-58]
  - Signature: `fn upsert_imports(`
  - Purpose: Upserts import relations for a specified file path within a project and returns the count of affected records. [crates/gcode/src/index/indexer/sink.rs:51-58]
- `upsert_calls` (function) component `upsert_calls [function]` (`7994087e-2ee8-58f6-a08d-3e1acc77e01b`) lines 60-67 [crates/gcode/src/index/indexer/sink.rs:60-67]
  - Signature: `fn upsert_calls(`
  - Purpose: This method performs an upsert operation on CallRelation records for a specified project and file, returning the count of affected rows. [crates/gcode/src/index/indexer/sink.rs:60-67]
- `upsert_content_chunks` (function) component `upsert_content_chunks [function]` (`edcbd19f-2047-5f44-a1f1-7ef1ae944e71`) lines 69-71 [crates/gcode/src/index/indexer/sink.rs:69-71]
  - Signature: `fn upsert_content_chunks(&mut self, chunks: &[ContentChunk]) -> anyhow::Result<usize> {`
  - Purpose: Upserts a slice of ContentChunk objects and returns the count of affected rows or an error. [crates/gcode/src/index/indexer/sink.rs:69-71]

