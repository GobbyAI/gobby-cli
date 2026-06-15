---
title: crates/gcode/src/index/indexer/sink.rs
type: code_file
provenance:
- file: crates/gcode/src/index/indexer/sink.rs
  ranges:
  - 6-34
  - 36-38
  - 41-43
  - 50-52
  - 54-60
  - 62-69
  - 71-73
  - 75-77
  - 79-86
  - 88-95
  - 97-99
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/indexer/sink.rs

Module: [[code/modules/crates/gcode/src/index/indexer|crates/gcode/src/index/indexer]]

## Purpose

Defines a `CodeFactSink` trait that abstracts the database operations needed by the indexer to remove and persist code facts for a file, including file-level cleanup, stale symbol deletion, and upserts for symbols, files, imports, calls, and content chunks. `PostgresCodeFactSink` is the Postgres-backed implementation: it stores a mutable generic `GenericClient` connection, is constructed with `new`, and each trait method simply forwards to the corresponding `crate::index::api` function using that connection.
[crates/gcode/src/index/indexer/sink.rs:6-34]
[crates/gcode/src/index/indexer/sink.rs:36-38]
[crates/gcode/src/index/indexer/sink.rs:41-43]
[crates/gcode/src/index/indexer/sink.rs:50-52]
[crates/gcode/src/index/indexer/sink.rs:54-60]

## API Symbols

- `CodeFactSink` (type) component `CodeFactSink [type]` (`4beb9119-9fd1-58f8-95af-7e14c1d44a43`) lines 6-34 [crates/gcode/src/index/indexer/sink.rs:6-34]
  - Signature: `pub(super) trait CodeFactSink {`
  - Purpose: Indexed type `CodeFactSink` in `crates/gcode/src/index/indexer/sink.rs`. [crates/gcode/src/index/indexer/sink.rs:6-34]
- `PostgresCodeFactSink` (class) component `PostgresCodeFactSink [class]` (`519b1645-56e3-50f6-bcf8-ece8c93623d0`) lines 36-38 [crates/gcode/src/index/indexer/sink.rs:36-38]
  - Signature: `pub(super) struct PostgresCodeFactSink<'a, C> {`
  - Purpose: 'PostgresCodeFactSink<'a, C>' is a 'pub(super)' wrapper that holds a mutable borrow of a generic connection 'C' ('conn: &'a mut C') for writing code facts to Postgres. [crates/gcode/src/index/indexer/sink.rs:36-38]
- `new` (function) component `new [function]` (`f66039bb-8d68-531b-96d3-7d0f7f01ee33`) lines 41-43 [crates/gcode/src/index/indexer/sink.rs:41-43]
  - Signature: `pub(super) fn new(conn: &'a mut C) -> Self {`
  - Purpose: Creates and returns a new wrapper instance by storing the provided mutable connection reference in 'conn'. [crates/gcode/src/index/indexer/sink.rs:41-43]
- `delete_file_facts` (function) component `delete_file_facts [function]` (`6f175061-24d5-5b38-9496-113a1f6e9a8f`) lines 50-52 [crates/gcode/src/index/indexer/sink.rs:50-52]
  - Signature: `fn delete_file_facts(&mut self, project_id: &str, file_path: &str) -> anyhow::Result<()> {`
  - Purpose: Deletes all stored facts associated with the specified 'file_path' in the given 'project_id' by delegating to 'api::delete_file_facts' on the current database connection. [crates/gcode/src/index/indexer/sink.rs:50-52]
- `delete_file_non_symbol_facts` (function) component `delete_file_non_symbol_facts [function]` (`e97c7665-91dc-5e5f-853e-c000add5a733`) lines 54-60 [crates/gcode/src/index/indexer/sink.rs:54-60]
  - Signature: `fn delete_file_non_symbol_facts(`
  - Purpose: Deletes all non-symbol fact records for the specified 'file_path' within the given 'project_id' by delegating to 'api::delete_file_non_symbol_facts' and returning its 'Result<()>'. [crates/gcode/src/index/indexer/sink.rs:54-60]
- `delete_stale_file_symbols` (function) component `delete_stale_file_symbols [function]` (`7a4de9ca-1c4c-5b93-b739-f5d7061ce532`) lines 62-69 [crates/gcode/src/index/indexer/sink.rs:62-69]
  - Signature: `fn delete_stale_file_symbols(`
  - Purpose: Deletes stale symbols for the given 'project_id' and 'file_path' that are not present in 'current_symbol_ids' by delegating to 'api::delete_stale_file_symbols', and returns the number of deleted symbols. [crates/gcode/src/index/indexer/sink.rs:62-69]
- `upsert_symbols` (function) component `upsert_symbols [function]` (`2039da60-88d9-5567-a021-f3c6b66cec2a`) lines 71-73 [crates/gcode/src/index/indexer/sink.rs:71-73]
  - Signature: `fn upsert_symbols(&mut self, symbols: &[Symbol]) -> anyhow::Result<usize> {`
  - Purpose: Delegates to 'api::upsert_symbols(self.conn, symbols)' to insert or update the provided 'Symbol' slice in the backing store and returns the number of affected records. [crates/gcode/src/index/indexer/sink.rs:71-73]
- `upsert_file` (function) component `upsert_file [function]` (`4fd617f2-fa69-5f18-b533-aafb5806be6d`) lines 75-77 [crates/gcode/src/index/indexer/sink.rs:75-77]
  - Signature: `fn upsert_file(&mut self, file: &IndexedFile) -> anyhow::Result<()> {`
  - Purpose: Delegates to 'api::upsert_file(self.conn, file)' to insert or update the given 'IndexedFile' in the underlying database connection and returns any resulting error. [crates/gcode/src/index/indexer/sink.rs:75-77]
- `upsert_imports` (function) component `upsert_imports [function]` (`5a0d366b-f54c-5559-a559-34ed1702125b`) lines 79-86 [crates/gcode/src/index/indexer/sink.rs:79-86]
  - Signature: `fn upsert_imports(`
  - Purpose: Delegates to 'api::upsert_imports' to persist the given 'ImportRelation' list for a specific 'project_id' and 'file_path' using 'self.conn', returning the number of affected rows as a 'usize' or an error. [crates/gcode/src/index/indexer/sink.rs:79-86]
- `upsert_calls` (function) component `upsert_calls [function]` (`e0e15eb2-cccd-5aa8-854e-8076d3687047`) lines 88-95 [crates/gcode/src/index/indexer/sink.rs:88-95]
  - Signature: `fn upsert_calls(`
  - Purpose: Forwards the provided 'project_id', 'file_path', and 'CallRelation' slice to 'api::upsert_calls' using the stored database connection, returning the number of upserted calls or an error. [crates/gcode/src/index/indexer/sink.rs:88-95]
- `upsert_content_chunks` (function) component `upsert_content_chunks [function]` (`0d1aa3ba-2660-51b7-946a-8e929bfccee1`) lines 97-99 [crates/gcode/src/index/indexer/sink.rs:97-99]
  - Signature: `fn upsert_content_chunks(&mut self, chunks: &[ContentChunk]) -> anyhow::Result<usize> {`
  - Purpose: Delegates to 'api::upsert_content_chunks(self.conn, chunks)' to upsert the provided 'ContentChunk' slice through the current connection and returns the number of affected records as an 'anyhow::Result<usize>'. [crates/gcode/src/index/indexer/sink.rs:97-99]

