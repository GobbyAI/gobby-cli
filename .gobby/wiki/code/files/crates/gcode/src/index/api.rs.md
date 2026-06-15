---
title: crates/gcode/src/index/api.rs
type: code_file
provenance:
- file: crates/gcode/src/index/api.rs
  ranges:
  - 16-23
  - 26-34
  - 36-48
  - 50-60
  - 62-84
  - 86-108
  - 110-125
  - 127-241
  - 243-269
  - 271-298
  - 300-325
  - 327-347
  - 349-383
  - 385-387
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/api.rs

Module: [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]

## Purpose

This file defines the API for writing and cleaning up code-index facts for a single file or project. It exposes request and summary types for tracking how many symbols, imports, calls, and chunks were processed, plus whether graph/vector sync still needs to happen, and provides helpers to delete stale or complete file facts, check whether any facts exist, and upsert the underlying database records for symbols, indexed files, content chunks, imports, calls, and project stats. The pieces work together around a `GenericClient` by clearing old rows where needed, batching symbol writes, using conflict-aware inserts/updates, and converting oversized counts safely with `to_i32`.
[crates/gcode/src/index/api.rs:16-23]
[crates/gcode/src/index/api.rs:26-34]
[crates/gcode/src/index/api.rs:36-48]
[crates/gcode/src/index/api.rs:37-47]
[crates/gcode/src/index/api.rs:50-60]

## API Symbols

- `CodeFactWriteRequest` (class) component `CodeFactWriteRequest [class]` (`999fd758-5ee6-565b-b3fc-05ece84767a6`) lines 16-23 [crates/gcode/src/index/api.rs:16-23]
  - Signature: `pub struct CodeFactWriteRequest {`
  - Purpose: 'CodeFactWriteRequest' is a request payload containing a 'project_id', 'file_path', and four 'usize' counters ('symbols', 'imports', 'calls', 'chunks') used to record code-fact write metrics for a file. [crates/gcode/src/index/api.rs:16-23]
- `CodeFactWriteSummary` (class) component `CodeFactWriteSummary [class]` (`2a187c49-b0c7-5c33-9cff-0423155e25d3`) lines 26-34 [crates/gcode/src/index/api.rs:26-34]
  - Signature: `pub struct CodeFactWriteSummary {`
  - Purpose: 'CodeFactWriteSummary' is a struct that reports counts of written files, symbols, imports, calls, and chunks, plus boolean flags indicating whether graph and vector synchronization are still pending. [crates/gcode/src/index/api.rs:26-34]
- `CodeFactWriteSummary` (class) component `CodeFactWriteSummary [class]` (`c2c04fa1-0607-55ee-9c89-5e5655282072`) lines 36-48 [crates/gcode/src/index/api.rs:36-48]
  - Signature: `impl CodeFactWriteSummary {`
  - Purpose: 'CodeFactWriteSummary' is a constructor helper that produces a summary for writing a single file, populating symbol/import/call/chunk counts and marking both graph and vector synchronization as pending. [crates/gcode/src/index/api.rs:36-48]
- `CodeFactWriteSummary.for_file` (method) component `CodeFactWriteSummary.for_file [method]` (`404ecb9a-f4ec-5e4a-9eb6-0f0088f2b397`) lines 37-47 [crates/gcode/src/index/api.rs:37-47]
  - Signature: `pub fn for_file(symbols: usize, imports: usize, calls: usize, chunks: usize) -> Self {`
  - Purpose: Constructs a new state with 'files_written' fixed to '1', the provided 'symbols', 'imports', 'calls', and 'chunks' counts assigned to their respective written fields, and both 'graph_sync_pending' and 'vectors_sync_pending' set to 'true'. [crates/gcode/src/index/api.rs:37-47]
- `delete_file_facts` (function) component `delete_file_facts [function]` (`4f7daf79-3a6f-5f10-b235-168a2bb29944`) lines 50-60 [crates/gcode/src/index/api.rs:50-60]
  - Signature: `pub fn delete_file_facts(`
  - Purpose: Deletes all symbol rows for the given 'project_id' and 'file_path' from 'code_symbols', then removes the file’s non-symbol facts via 'delete_file_non_symbol_facts', returning any database or cleanup error as 'anyhow::Result<()>'. [crates/gcode/src/index/api.rs:50-60]
- `delete_file_non_symbol_facts` (function) component `delete_file_non_symbol_facts [function]` (`b4986145-e045-52e0-b8f2-645b158e4435`) lines 62-84 [crates/gcode/src/index/api.rs:62-84]
  - Signature: `pub fn delete_file_non_symbol_facts(`
  - Purpose: Deletes all non-symbol indexing records for a given 'project_id' and 'file_path' by issuing 'DELETE' statements against 'code_indexed_files', 'code_content_chunks', 'code_imports' (matching 'source_file'), and 'code_calls', then returns 'Ok(())' if all database operations succeed. [crates/gcode/src/index/api.rs:62-84]
- `delete_stale_file_symbols` (function) component `delete_stale_file_symbols [function]` (`3dc60508-0219-5081-9294-638784b75dde`) lines 86-108 [crates/gcode/src/index/api.rs:86-108]
  - Signature: `pub fn delete_stale_file_symbols(`
  - Purpose: Deletes stale 'code_symbols' rows for the given 'project_id' and 'file_path', either removing all symbols when 'current_symbol_ids' is empty or deleting only rows whose 'id' is not in 'current_symbol_ids', then returns the deleted row count as 'usize' with overflow checked. [crates/gcode/src/index/api.rs:86-108]
- `file_facts_exist` (function) component `file_facts_exist [function]` (`815e371c-69c6-5070-a5fd-fe1b0fb501b6`) lines 110-125 [crates/gcode/src/index/api.rs:110-125]
  - Signature: `pub fn file_facts_exist(`
  - Purpose: Returns 'true' if any indexed facts exist for the given 'project_id' and 'file_path' across 'code_indexed_files', 'code_symbols', 'code_content_chunks', 'code_imports' (matched on 'source_file'), or 'code_calls', otherwise 'false'. [crates/gcode/src/index/api.rs:110-125]
- `upsert_symbols` (function) component `upsert_symbols [function]` (`79b66ff9-5fe5-5fcc-bf68-660114849caa`) lines 127-241 [crates/gcode/src/index/api.rs:127-241]
  - Signature: `pub fn upsert_symbols(conn: &mut impl GenericClient, symbols: &[Symbol]) -> anyhow::Result<usize> {`
  - Purpose: Upserts the provided 'Symbol' records into the database in fixed-size batches by collecting each field into column-oriented vectors, converting positional offsets to 'i32', and returning the total number of affected rows or an error. [crates/gcode/src/index/api.rs:127-241]
- `upsert_file` (function) component `upsert_file [function]` (`3fdcfdc6-7eaf-548d-8d3f-9aad31d16fc2`) lines 243-269 [crates/gcode/src/index/api.rs:243-269]
  - Signature: `pub fn upsert_file(conn: &mut impl GenericClient, file: &IndexedFile) -> anyhow::Result<()> {`
  - Purpose: 'upsert_file' inserts a row for an 'IndexedFile' into 'code_indexed_files', or on 'id' conflict updates its content metadata and counters while resetting sync flags and timestamps to force reindexing. [crates/gcode/src/index/api.rs:243-269]
- `upsert_content_chunks` (function) component `upsert_content_chunks [function]` (`d4ea5d25-98d9-569f-8fc0-8a31c0d4d468`) lines 271-298 [crates/gcode/src/index/api.rs:271-298]
  - Signature: `pub fn upsert_content_chunks(`
  - Purpose: Inserts each 'ContentChunk' into 'code_content_chunks' and, on 'id' conflict, updates the stored 'content', 'line_start', and 'line_end', returning the number of chunks processed. [crates/gcode/src/index/api.rs:271-298]
- `upsert_project_stats` (function) component `upsert_project_stats [function]` (`93f41710-4909-52e1-9c6f-483de6e5c739`) lines 300-325 [crates/gcode/src/index/api.rs:300-325]
  - Signature: `pub fn upsert_project_stats(`
  - Purpose: Inserts or updates a 'code_indexed_projects' row for the given project by 'id', storing its root path, file and symbol counts, indexing duration, and current 'last_indexed_at'/'updated_at' timestamps. [crates/gcode/src/index/api.rs:300-325]
- `upsert_imports` (function) component `upsert_imports [function]` (`e336b793-2d4c-5620-baeb-f25375077ace`) lines 327-347 [crates/gcode/src/index/api.rs:327-347]
  - Signature: `pub fn upsert_imports(`
  - Purpose: Deletes all 'code_imports' rows for the given 'project_id' and 'source_file', then inserts the provided import relations with conflict suppression and returns the number of rows actually inserted. [crates/gcode/src/index/api.rs:327-347]
- `upsert_calls` (function) component `upsert_calls [function]` (`43190ed3-8515-59d2-a699-288a839e5f70`) lines 349-383 [crates/gcode/src/index/api.rs:349-383]
  - Signature: `pub fn upsert_calls(`
  - Purpose: Deletes all 'code_calls' rows for the given 'project_id' and 'file_path', then inserts the provided 'CallRelation' records with conflict-avoiding upserts, returning the number of inserted rows. [crates/gcode/src/index/api.rs:349-383]
- `to_i32` (function) component `to_i32 [function]` (`b858b861-c078-5168-9ba2-2363bd9617eb`) lines 385-387 [crates/gcode/src/index/api.rs:385-387]
  - Signature: `fn to_i32(value: usize) -> i32 {`
  - Purpose: Converts a 'usize' to 'i32' by clamping values above 'i32::MAX' to 'i32::MAX' before casting. [crates/gcode/src/index/api.rs:385-387]

