---
title: crates/gcode/src/index/api.rs
type: code_file
provenance:
- file: crates/gcode/src/index/api.rs
  ranges:
  - 16-23
  - 26-34
  - 36-48
  - 37-47
  - 50-76
  - 78-93
  - 95-209
  - 211-237
  - 239-266
  - 268-293
  - 295-314
  - 316-349
  - 351-353
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/api.rs

Module: [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]

## Purpose

`crates/gcode/src/index/api.rs` exposes 13 indexed API symbols.
[crates/gcode/src/index/api.rs:16-23]
[crates/gcode/src/index/api.rs:26-34]
[crates/gcode/src/index/api.rs:36-48]
[crates/gcode/src/index/api.rs:37-47]
[crates/gcode/src/index/api.rs:50-76]
[crates/gcode/src/index/api.rs:78-93]
[crates/gcode/src/index/api.rs:95-209]
[crates/gcode/src/index/api.rs:211-237]
[crates/gcode/src/index/api.rs:239-266]
[crates/gcode/src/index/api.rs:268-293]
[crates/gcode/src/index/api.rs:295-314]
[crates/gcode/src/index/api.rs:316-349]
[crates/gcode/src/index/api.rs:351-353]

## API Symbols

- `CodeFactWriteRequest` (class) component `CodeFactWriteRequest [class]` (`999fd758-5ee6-565b-b3fc-05ece84767a6`) lines 16-23 [crates/gcode/src/index/api.rs:16-23]
  - Signature: `pub struct CodeFactWriteRequest {`
  - Purpose: CodeFactWriteRequest is a struct that aggregates static code analysis metrics (symbol, import, call, and chunk counts) for a specified file within a project. [crates/gcode/src/index/api.rs:16-23]
- `CodeFactWriteSummary` (class) component `CodeFactWriteSummary [class]` (`2a187c49-b0c7-5c33-9cff-0423155e25d3`) lines 26-34 [crates/gcode/src/index/api.rs:26-34]
  - Signature: `pub struct CodeFactWriteSummary {`
  - Purpose: `CodeFactWriteSummary` is a metrics struct that aggregates write counts for code facts (files, symbols, imports, calls, chunks) and tracks pending synchronization flags for graph and vector indexes. [crates/gcode/src/index/api.rs:26-34]
- `CodeFactWriteSummary` (class) component `CodeFactWriteSummary [class]` (`c2c04fa1-0607-55ee-9c89-5e5655282072`) lines 36-48 [crates/gcode/src/index/api.rs:36-48]
  - Signature: `impl CodeFactWriteSummary {`
  - Purpose: `CodeFactWriteSummary::for_file` is a factory constructor that creates a single-file summary with specified counts of symbols, imports, calls, and chunks, initializing both graph and vector synchronization flags as pending. [crates/gcode/src/index/api.rs:36-48]
- `CodeFactWriteSummary.for_file` (method) component `CodeFactWriteSummary.for_file [method]` (`404ecb9a-f4ec-5e4a-9eb6-0f0088f2b397`) lines 37-47 [crates/gcode/src/index/api.rs:37-47]
  - Signature: `pub fn for_file(symbols: usize, imports: usize, calls: usize, chunks: usize) -> Self {`
  - Purpose: Constructs a metrics struct for a single file with specified symbol, import, call, and chunk counts, initializing graph and vector synchronization flags as pending. [crates/gcode/src/index/api.rs:37-47]
- `delete_file_facts` (function) component `delete_file_facts [function]` (`4f7daf79-3a6f-5f10-b235-168a2bb29944`) lines 50-76 [crates/gcode/src/index/api.rs:50-76]
  - Signature: `pub fn delete_file_facts(`
  - Purpose: Removes all code analysis metadata (symbols, chunks, imports, and calls) associated with a file from a project's database. [crates/gcode/src/index/api.rs:50-76]
- `file_facts_exist` (function) component `file_facts_exist [function]` (`54839e09-5fc4-5e76-b690-d0fe0bf8c568`) lines 78-93 [crates/gcode/src/index/api.rs:78-93]
  - Signature: `pub fn file_facts_exist(`
  - Purpose: Returns whether a file has indexed code facts by checking for its existence across five code analysis database tables: code_indexed_files, code_symbols, code_content_chunks, code_imports, and code_calls. [crates/gcode/src/index/api.rs:78-93]
- `upsert_symbols` (function) component `upsert_symbols [function]` (`571e0ce4-5896-556e-9cc2-9e2348b9e541`) lines 95-209 [crates/gcode/src/index/api.rs:95-209]
  - Signature: `pub fn upsert_symbols(conn: &mut impl GenericClient, symbols: &[Symbol]) -> anyhow::Result<usize> {`
  - Purpose: Batches and upserts Symbol records into a database by extracting symbol attributes into columnar vectors for bulk insert-or-update operations. [crates/gcode/src/index/api.rs:95-209]
- `upsert_file` (function) component `upsert_file [function]` (`5bd27f49-a67d-555a-9142-d6f04a44e631`) lines 211-237 [crates/gcode/src/index/api.rs:211-237]
  - Signature: `pub fn upsert_file(conn: &mut impl GenericClient, file: &IndexedFile) -> anyhow::Result<()> {`
  - Purpose: Executes an SQL UPSERT operation to insert or update an indexed file record in the database, resetting synchronization flags when a conflict occurs. [crates/gcode/src/index/api.rs:211-237]
- `upsert_content_chunks` (function) component `upsert_content_chunks [function]` (`86cee32a-87d0-5a66-8e59-78a2df7b46b9`) lines 239-266 [crates/gcode/src/index/api.rs:239-266]
  - Signature: `pub fn upsert_content_chunks(`
  - Purpose: Performs batch UPSERT of ContentChunk records into the code_content_chunks table using INSERT...ON CONFLICT(id) DO UPDATE semantics, returning the count of processed chunks. [crates/gcode/src/index/api.rs:239-266]
- `upsert_project_stats` (function) component `upsert_project_stats [function]` (`010d7ed5-bb30-52e4-80f1-821b6810d900`) lines 268-293 [crates/gcode/src/index/api.rs:268-293]
  - Signature: `pub fn upsert_project_stats(`
  - Purpose: Performs an UPSERT operation to insert or update a project's indexing statistics (file count, symbol count, indexing duration, and timestamp) in the `code_indexed_projects` table, keyed on project ID. [crates/gcode/src/index/api.rs:268-293]
- `upsert_imports` (function) component `upsert_imports [function]` (`dee039e1-55f0-5a5d-ab8c-5e2f843600d6`) lines 295-314 [crates/gcode/src/index/api.rs:295-314]
  - Signature: `pub fn upsert_imports(`
  - Purpose: Deletes all existing code imports for a given project file and re-inserts the provided import relations, returning the count of imports. [crates/gcode/src/index/api.rs:295-314]
- `upsert_calls` (function) component `upsert_calls [function]` (`d5bdfe77-83ca-58c2-aa48-7fbf0ec62445`) lines 316-349 [crates/gcode/src/index/api.rs:316-349]
  - Signature: `pub fn upsert_calls(`
  - Purpose: Replaces all code call relations for a specified project file by deleting existing entries and bulk-inserting new CallRelation records with conflict handling, returning the count of inserted calls. [crates/gcode/src/index/api.rs:316-349]
- `to_i32` (function) component `to_i32 [function]` (`93268314-0647-5ec1-ad56-ee395a6a4491`) lines 351-353 [crates/gcode/src/index/api.rs:351-353]
  - Signature: `fn to_i32(value: usize) -> i32 {`
  - Purpose: Converts a `usize` to an `i32` by clamping the input to `i32::MAX` before casting to prevent overflow. [crates/gcode/src/index/api.rs:351-353]

