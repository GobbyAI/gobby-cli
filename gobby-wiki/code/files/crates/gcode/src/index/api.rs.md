---
title: crates/gcode/src/index/api.rs
type: code_file
provenance:
- file: crates/gcode/src/index/api.rs
  ranges:
  - 16-23
  - 26-34
  - 37-47
  - 50-60
  - 62-84
  - 86-108
  - 110-125
  - 127-241
  - 243-269
  - 271-298
  - 300-325
  - 327-347
  - 349-364
  - 366-392
  - 398-420
  - 422-424
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/api.rs:16-23](crates/gcode/src/index/api.rs#L16-L23), [crates/gcode/src/index/api.rs:26-34](crates/gcode/src/index/api.rs#L26-L34), [crates/gcode/src/index/api.rs:37-47](crates/gcode/src/index/api.rs#L37-L47), [crates/gcode/src/index/api.rs:50-60](crates/gcode/src/index/api.rs#L50-L60), [crates/gcode/src/index/api.rs:62-84](crates/gcode/src/index/api.rs#L62-L84), [crates/gcode/src/index/api.rs:86-108](crates/gcode/src/index/api.rs#L86-L108), [crates/gcode/src/index/api.rs:110-125](crates/gcode/src/index/api.rs#L110-L125), [crates/gcode/src/index/api.rs:127-241](crates/gcode/src/index/api.rs#L127-L241), [crates/gcode/src/index/api.rs:243-269](crates/gcode/src/index/api.rs#L243-L269), [crates/gcode/src/index/api.rs:271-298](crates/gcode/src/index/api.rs#L271-L298), [crates/gcode/src/index/api.rs:300-325](crates/gcode/src/index/api.rs#L300-L325), [crates/gcode/src/index/api.rs:327-347](crates/gcode/src/index/api.rs#L327-L347), [crates/gcode/src/index/api.rs:349-364](crates/gcode/src/index/api.rs#L349-L364), [crates/gcode/src/index/api.rs:366-392](crates/gcode/src/index/api.rs#L366-L392), [crates/gcode/src/index/api.rs:398-420](crates/gcode/src/index/api.rs#L398-L420), [crates/gcode/src/index/api.rs:422-424](crates/gcode/src/index/api.rs#L422-L424)

</details>

# crates/gcode/src/index/api.rs

Module: [[code/modules/crates/gcode/src/index|crates/gcode/src/index]]

## Purpose

This file provides the database-facing API for writing and cleaning up code-index facts for a project. It defines request/summary types for reporting per-file indexing writes, re-exports higher-level indexing types and functions from the indexer module, and implements the core PostgreSQL operations that delete stale file facts, check whether facts exist, and upsert symbols, files, content chunks, project stats, imports, and call relations. The helper functions work together to keep the code index synchronized when a file changes, including promoting local import calls and normalizing counts with `to_i32`.
[crates/gcode/src/index/api.rs:16-23]
[crates/gcode/src/index/api.rs:26-34]
[crates/gcode/src/index/api.rs:37-47]
[crates/gcode/src/index/api.rs:50-60]
[crates/gcode/src/index/api.rs:62-84]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `CodeFactWriteRequest` | class | `pub struct CodeFactWriteRequest {` | `CodeFactWriteRequest [class]` | `999fd758-5ee6-565b-b3fc-05ece84767a6` | 16-23 [crates/gcode/src/index/api.rs:16-23] | Indexed class `CodeFactWriteRequest` in `crates/gcode/src/index/api.rs`. [crates/gcode/src/index/api.rs:16-23] |
| `CodeFactWriteSummary` | class | `pub struct CodeFactWriteSummary {` | `CodeFactWriteSummary [class]` | `2a187c49-b0c7-5c33-9cff-0423155e25d3` | 26-34 [crates/gcode/src/index/api.rs:26-34] | Indexed class `CodeFactWriteSummary` in `crates/gcode/src/index/api.rs`. [crates/gcode/src/index/api.rs:26-34] |
| `CodeFactWriteSummary::for_file` | method | `pub fn for_file(symbols: usize, imports: usize, calls: usize, chunks: usize) -> Self {` | `CodeFactWriteSummary::for_file [method]` | `404ecb9a-f4ec-5e4a-9eb6-0f0088f2b397` | 37-47 [crates/gcode/src/index/api.rs:37-47] | Indexed method `CodeFactWriteSummary::for_file` in `crates/gcode/src/index/api.rs`. [crates/gcode/src/index/api.rs:37-47] |
| `delete_file_facts` | function | `pub fn delete_file_facts(` | `delete_file_facts [function]` | `4f7daf79-3a6f-5f10-b235-168a2bb29944` | 50-60 [crates/gcode/src/index/api.rs:50-60] | Indexed function `delete_file_facts` in `crates/gcode/src/index/api.rs`. [crates/gcode/src/index/api.rs:50-60] |
| `delete_file_non_symbol_facts` | function | `pub fn delete_file_non_symbol_facts(` | `delete_file_non_symbol_facts [function]` | `b4986145-e045-52e0-b8f2-645b158e4435` | 62-84 [crates/gcode/src/index/api.rs:62-84] | Indexed function `delete_file_non_symbol_facts` in `crates/gcode/src/index/api.rs`. [crates/gcode/src/index/api.rs:62-84] |
| `delete_stale_file_symbols` | function | `pub fn delete_stale_file_symbols(` | `delete_stale_file_symbols [function]` | `3dc60508-0219-5081-9294-638784b75dde` | 86-108 [crates/gcode/src/index/api.rs:86-108] | Indexed function `delete_stale_file_symbols` in `crates/gcode/src/index/api.rs`. [crates/gcode/src/index/api.rs:86-108] |
| `file_facts_exist` | function | `pub fn file_facts_exist(` | `file_facts_exist [function]` | `815e371c-69c6-5070-a5fd-fe1b0fb501b6` | 110-125 [crates/gcode/src/index/api.rs:110-125] | Indexed function `file_facts_exist` in `crates/gcode/src/index/api.rs`. [crates/gcode/src/index/api.rs:110-125] |
| `upsert_symbols` | function | `pub fn upsert_symbols(conn: &mut impl GenericClient, symbols: &[Symbol]) -> anyhow::Result<usize> {` | `upsert_symbols [function]` | `79b66ff9-5fe5-5fcc-bf68-660114849caa` | 127-241 [crates/gcode/src/index/api.rs:127-241] | Indexed function `upsert_symbols` in `crates/gcode/src/index/api.rs`. [crates/gcode/src/index/api.rs:127-241] |
| `upsert_file` | function | `pub fn upsert_file(conn: &mut impl GenericClient, file: &IndexedFile) -> anyhow::Result<()> {` | `upsert_file [function]` | `3fdcfdc6-7eaf-548d-8d3f-9aad31d16fc2` | 243-269 [crates/gcode/src/index/api.rs:243-269] | Indexed function `upsert_file` in `crates/gcode/src/index/api.rs`. [crates/gcode/src/index/api.rs:243-269] |
| `upsert_content_chunks` | function | `pub fn upsert_content_chunks(` | `upsert_content_chunks [function]` | `d4ea5d25-98d9-569f-8fc0-8a31c0d4d468` | 271-298 [crates/gcode/src/index/api.rs:271-298] | Indexed function `upsert_content_chunks` in `crates/gcode/src/index/api.rs`. [crates/gcode/src/index/api.rs:271-298] |
| `upsert_project_stats` | function | `pub fn upsert_project_stats(` | `upsert_project_stats [function]` | `93f41710-4909-52e1-9c6f-483de6e5c739` | 300-325 [crates/gcode/src/index/api.rs:300-325] | Indexed function `upsert_project_stats` in `crates/gcode/src/index/api.rs`. [crates/gcode/src/index/api.rs:300-325] |
| `upsert_imports` | function | `pub fn upsert_imports(` | `upsert_imports [function]` | `e336b793-2d4c-5620-baeb-f25375077ace` | 327-347 [crates/gcode/src/index/api.rs:327-347] | Indexed function `upsert_imports` in `crates/gcode/src/index/api.rs`. [crates/gcode/src/index/api.rs:327-347] |
| `upsert_calls` | function | `pub fn upsert_calls(` | `upsert_calls [function]` | `43190ed3-8515-59d2-a699-288a839e5f70` | 349-364 [crates/gcode/src/index/api.rs:349-364] | Indexed function `upsert_calls` in `crates/gcode/src/index/api.rs`. [crates/gcode/src/index/api.rs:349-364] |
| `insert_call` | function | `fn insert_call(` | `insert_call [function]` | `868126bb-9608-56ed-b232-af2e3ecc46ed` | 366-392 [crates/gcode/src/index/api.rs:366-392] | Indexed function `insert_call` in `crates/gcode/src/index/api.rs`. [crates/gcode/src/index/api.rs:366-392] |
| `promote_local_import_call` | function | `pub fn promote_local_import_call(` | `promote_local_import_call [function]` | `4b0bf40a-490b-5187-a2f8-3e7ae8085f82` | 398-420 [crates/gcode/src/index/api.rs:398-420] | Indexed function `promote_local_import_call` in `crates/gcode/src/index/api.rs`. [crates/gcode/src/index/api.rs:398-420] |
| `to_i32` | function | `fn to_i32(value: usize) -> i32 {` | `to_i32 [function]` | `fb3b0362-366c-521a-822f-43054737e8b5` | 422-424 [crates/gcode/src/index/api.rs:422-424] | Indexed function `to_i32` in `crates/gcode/src/index/api.rs`. [crates/gcode/src/index/api.rs:422-424] |
