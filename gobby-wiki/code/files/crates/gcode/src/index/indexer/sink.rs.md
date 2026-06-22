---
title: crates/gcode/src/index/indexer/sink.rs
type: code_file
provenance:
- file: crates/gcode/src/index/indexer/sink.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/indexer/sink.rs

Module: [[code/modules/crates/gcode/src/index/indexer|crates/gcode/src/index/indexer]]

## Overview

`crates/gcode/src/index/indexer/sink.rs` exposes 11 indexed API symbols.

## How it fits

`crates/gcode/src/index/indexer/sink.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `CodeFactSink` | type | Indexed type `CodeFactSink` in `crates/gcode/src/index/indexer/sink.rs`. [crates/gcode/src/index/indexer/sink.rs:6-34] |
| `PostgresCodeFactSink` | class | 'PostgresCodeFactSink<'a, C>' is a 'pub(super)' sink wrapper that holds a mutable reference to a PostgreSQL connection-like value 'C' for writing code facts. [crates/gcode/src/index/indexer/sink.rs:36-38] |
| `new` | function | Constructs and returns a new instance by storing the provided mutable connection reference in the 'conn' field. [crates/gcode/src/index/indexer/sink.rs:41-43] |
| `delete_file_facts` | function | Delegates to 'api::delete_file_facts' to delete all fact records for the specified 'file_path' within 'project_id' using the current connection, returning the API result. [crates/gcode/src/index/indexer/sink.rs:50-52] |
| `delete_file_non_symbol_facts` | function | Deletes all non-symbol fact records for the specified 'project_id' and 'file_path' by delegating to 'api::delete_file_non_symbol_facts' and returning its 'anyhow::Result<()>'. [crates/gcode/src/index/indexer/sink.rs:54-60] |
| `delete_stale_file_symbols` | function | Deletes stale symbols for the specified 'project_id' and 'file_path' by delegating to 'api::delete_stale_file_symbols' with the current symbol IDs, returning the number of symbols removed. [crates/gcode/src/index/indexer/sink.rs:62-69] |
| `upsert_symbols` | function | Delegates to 'api::upsert_symbols(self.conn, symbols)' to insert or update the provided symbol records in the database, returning the number of affected rows as an 'anyhow::Result<usize>'. [crates/gcode/src/index/indexer/sink.rs:71-73] |
| `upsert_file` | function | Forwards the given 'IndexedFile' to 'api::upsert_file' using 'self.conn', returning its 'anyhow::Result<()>' to insert or update the file record in the backing store. [crates/gcode/src/index/indexer/sink.rs:75-77] |
| `upsert_imports` | function | Forwards the provided 'project_id', 'file_path', and 'imports' slice to 'api::upsert_imports' using 'self.conn', returning the resulting 'usize' count or an 'anyhow::Error'. [crates/gcode/src/index/indexer/sink.rs:79-86] |
| `upsert_calls` | function | For a given 'project_id', 'file_path', and slice of 'CallRelation' values, this method delegates to 'api::upsert_calls' to insert or update the call records in the database and returns the number of affected rows. [crates/gcode/src/index/indexer/sink.rs:88-95] |
| `upsert_content_chunks` | function | Delegates to 'api::upsert_content_chunks(self.conn, chunks)' to upsert the provided 'ContentChunk' slice into the underlying connection and returns the resulting count as an 'anyhow::Result<usize>'. [crates/gcode/src/index/indexer/sink.rs:97-99] |

