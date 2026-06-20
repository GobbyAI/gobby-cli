---
title: crates/gcode/src/index/api.rs
type: code_file
provenance:
- file: crates/gcode/src/index/api.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/api.rs

Module: [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]

## Overview

`crates/gcode/src/index/api.rs` exposes 16 indexed API symbols.

## How it fits

`crates/gcode/src/index/api.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `CodeFactWriteRequest` | class | 'CodeFactWriteRequest' is a request payload containing a project identifier, a file path, and four 'usize' counters for symbols, imports, calls, and chunks to be written as code facts. [crates/gcode/src/index/api.rs:16-23] |
| `CodeFactWriteSummary` | class | 'CodeFactWriteSummary' is a write-operation summary struct that counts how many files, symbols, imports, calls, and chunks were written and indicates whether graph and vector synchronization is still pending. [crates/gcode/src/index/api.rs:26-34] |
| `CodeFactWriteSummary::for_file` | method | Constructs a new 'Self' value representing a single written file with the given symbol, import, call, and chunk counts, and marks both graph and vector synchronization as pending. [crates/gcode/src/index/api.rs:37-47] |
| `delete_file_facts` | function | Deletes all 'code_symbols' rows for the given 'project_id' and 'file_path', then removes the file’s non-symbol facts via 'delete_file_non_symbol_facts', returning any database error as 'anyhow::Result<()>'. [crates/gcode/src/index/api.rs:50-60] |
| `delete_file_non_symbol_facts` | function | Deletes all non-symbol fact records for a given 'project_id' and 'file_path' from 'code_indexed_files', 'code_content_chunks', 'code_imports' (by 'source_file'), and 'code_calls', returning 'Ok(())' if all SQL deletions succeed. [crates/gcode/src/index/api.rs:62-84] |
| `delete_stale_file_symbols` | function | Deletes 'code_symbols' rows for the given 'project_id' and 'file_path' that are no longer present in 'current_symbol_ids' (or all rows for that file when the list is empty) and returns the number of deleted rows as a 'usize', failing if the count overflows. [crates/gcode/src/index/api.rs:86-108] |
| `file_facts_exist` | function | Returns 'true' if any indexed code metadata exists for the given 'project_id' and file path across 'code_indexed_files', 'code_symbols', 'code_content_chunks', 'code_imports' (matched on 'source_file'), or 'code_calls', otherwise 'false'. [crates/gcode/src/index/api.rs:110-125] |
| `upsert_symbols` | function | Upserts the provided 'Symbol' records into the database in fixed-size batches by column-vectorizing each chunk’s fields and executing a batched insert/update, returning the total number of rows processed. [crates/gcode/src/index/api.rs:127-241] |
| `upsert_file` | function | Inserts a row for 'IndexedFile' into 'code_indexed_files' or, on 'id' conflict, updates its 'content_hash', 'symbol_count', and 'byte_size' while resetting sync flags/timestamps and refreshing 'indexed_at' to 'NOW()'. [crates/gcode/src/index/api.rs:243-269] |
| `upsert_content_chunks` | function | Inserts each 'ContentChunk' into 'code_content_chunks', upserting on 'id' to update 'content', 'line_start', and 'line_end' on conflict, and returns the number of chunks processed. [crates/gcode/src/index/api.rs:271-298] |
| `upsert_project_stats` | function | Inserts or updates a 'code_indexed_projects' row for the given project ID, storing its root path, file and symbol counts, index duration, and current timestamps for 'last_indexed_at' and 'updated_at'. [crates/gcode/src/index/api.rs:300-325] |
| `upsert_imports` | function | Deletes all 'code_imports' rows for the given 'project_id' and 'source_file', then inserts each provided 'ImportRelation' as a 'code_imports' record with 'ON CONFLICT DO NOTHING', returning the number of successfully inserted rows. [crates/gcode/src/index/api.rs:327-347] |
| `upsert_calls` | function | Deletes all 'code_calls' rows for the given 'project_id' and 'file_path', then reinserts each 'CallRelation' via 'insert_call', returning the total number of inserted rows. [crates/gcode/src/index/api.rs:349-364] |
| `insert_call` | function | Inserts a 'CallRelation' into the 'code_calls' table for a given 'project_id', using 'ON CONFLICT DO NOTHING' on the full call identity key and returning the number of rows inserted as 'usize'. [crates/gcode/src/index/api.rs:366-392] |
| `promote_local_import_call` | function | Deletes the 'code_calls' row for a 'local_import'-typed unresolved call matching 'original' in the given project, then inserts the corresponding resolved call relation via 'insert_call'. [crates/gcode/src/index/api.rs:398-420] |
| `to_i32` | function | Converts a 'usize' to 'i32' by clamping any value above 'i32::MAX' down to 'i32::MAX' before casting. [crates/gcode/src/index/api.rs:422-424] |

