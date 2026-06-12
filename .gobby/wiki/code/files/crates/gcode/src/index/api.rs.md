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

`crates/gcode/src/index/api.rs` exposes 15 indexed API symbols.
[crates/gcode/src/index/api.rs:16-23]
[crates/gcode/src/index/api.rs:26-34]
[crates/gcode/src/index/api.rs:36-48]
[crates/gcode/src/index/api.rs:37-47]
[crates/gcode/src/index/api.rs:50-60]

## API Symbols

- `CodeFactWriteRequest` (class) component `CodeFactWriteRequest [class]` (`999fd758-5ee6-565b-b3fc-05ece84767a6`) lines 16-23 [crates/gcode/src/index/api.rs:16-23]
  - Signature: `pub struct CodeFactWriteRequest {`
  - Purpose: Indexed class `CodeFactWriteRequest` in `crates/gcode/src/index/api.rs`. [crates/gcode/src/index/api.rs:16-23]
- `CodeFactWriteSummary` (class) component `CodeFactWriteSummary [class]` (`2a187c49-b0c7-5c33-9cff-0423155e25d3`) lines 26-34 [crates/gcode/src/index/api.rs:26-34]
  - Signature: `pub struct CodeFactWriteSummary {`
  - Purpose: Indexed class `CodeFactWriteSummary` in `crates/gcode/src/index/api.rs`. [crates/gcode/src/index/api.rs:26-34]
- `CodeFactWriteSummary` (class) component `CodeFactWriteSummary [class]` (`c2c04fa1-0607-55ee-9c89-5e5655282072`) lines 36-48 [crates/gcode/src/index/api.rs:36-48]
  - Signature: `impl CodeFactWriteSummary {`
  - Purpose: Indexed class `CodeFactWriteSummary` in `crates/gcode/src/index/api.rs`. [crates/gcode/src/index/api.rs:36-48]
- `CodeFactWriteSummary.for_file` (method) component `CodeFactWriteSummary.for_file [method]` (`404ecb9a-f4ec-5e4a-9eb6-0f0088f2b397`) lines 37-47 [crates/gcode/src/index/api.rs:37-47]
  - Signature: `pub fn for_file(symbols: usize, imports: usize, calls: usize, chunks: usize) -> Self {`
  - Purpose: Indexed method `CodeFactWriteSummary.for_file` in `crates/gcode/src/index/api.rs`. [crates/gcode/src/index/api.rs:37-47]
- `delete_file_facts` (function) component `delete_file_facts [function]` (`4f7daf79-3a6f-5f10-b235-168a2bb29944`) lines 50-60 [crates/gcode/src/index/api.rs:50-60]
  - Signature: `pub fn delete_file_facts(`
  - Purpose: Indexed function `delete_file_facts` in `crates/gcode/src/index/api.rs`. [crates/gcode/src/index/api.rs:50-60]
- `delete_file_non_symbol_facts` (function) component `delete_file_non_symbol_facts [function]` (`b4986145-e045-52e0-b8f2-645b158e4435`) lines 62-84 [crates/gcode/src/index/api.rs:62-84]
  - Signature: `pub fn delete_file_non_symbol_facts(`
  - Purpose: Indexed function `delete_file_non_symbol_facts` in `crates/gcode/src/index/api.rs`. [crates/gcode/src/index/api.rs:62-84]
- `delete_stale_file_symbols` (function) component `delete_stale_file_symbols [function]` (`3dc60508-0219-5081-9294-638784b75dde`) lines 86-108 [crates/gcode/src/index/api.rs:86-108]
  - Signature: `pub fn delete_stale_file_symbols(`
  - Purpose: Indexed function `delete_stale_file_symbols` in `crates/gcode/src/index/api.rs`. [crates/gcode/src/index/api.rs:86-108]
- `file_facts_exist` (function) component `file_facts_exist [function]` (`815e371c-69c6-5070-a5fd-fe1b0fb501b6`) lines 110-125 [crates/gcode/src/index/api.rs:110-125]
  - Signature: `pub fn file_facts_exist(`
  - Purpose: Indexed function `file_facts_exist` in `crates/gcode/src/index/api.rs`. [crates/gcode/src/index/api.rs:110-125]
- `upsert_symbols` (function) component `upsert_symbols [function]` (`79b66ff9-5fe5-5fcc-bf68-660114849caa`) lines 127-241 [crates/gcode/src/index/api.rs:127-241]
  - Signature: `pub fn upsert_symbols(conn: &mut impl GenericClient, symbols: &[Symbol]) -> anyhow::Result<usize> {`
  - Purpose: Indexed function `upsert_symbols` in `crates/gcode/src/index/api.rs`. [crates/gcode/src/index/api.rs:127-241]
- `upsert_file` (function) component `upsert_file [function]` (`3fdcfdc6-7eaf-548d-8d3f-9aad31d16fc2`) lines 243-269 [crates/gcode/src/index/api.rs:243-269]
  - Signature: `pub fn upsert_file(conn: &mut impl GenericClient, file: &IndexedFile) -> anyhow::Result<()> {`
  - Purpose: Indexed function `upsert_file` in `crates/gcode/src/index/api.rs`. [crates/gcode/src/index/api.rs:243-269]
- `upsert_content_chunks` (function) component `upsert_content_chunks [function]` (`d4ea5d25-98d9-569f-8fc0-8a31c0d4d468`) lines 271-298 [crates/gcode/src/index/api.rs:271-298]
  - Signature: `pub fn upsert_content_chunks(`
  - Purpose: Indexed function `upsert_content_chunks` in `crates/gcode/src/index/api.rs`. [crates/gcode/src/index/api.rs:271-298]
- `upsert_project_stats` (function) component `upsert_project_stats [function]` (`93f41710-4909-52e1-9c6f-483de6e5c739`) lines 300-325 [crates/gcode/src/index/api.rs:300-325]
  - Signature: `pub fn upsert_project_stats(`
  - Purpose: Indexed function `upsert_project_stats` in `crates/gcode/src/index/api.rs`. [crates/gcode/src/index/api.rs:300-325]
- `upsert_imports` (function) component `upsert_imports [function]` (`e336b793-2d4c-5620-baeb-f25375077ace`) lines 327-347 [crates/gcode/src/index/api.rs:327-347]
  - Signature: `pub fn upsert_imports(`
  - Purpose: Indexed function `upsert_imports` in `crates/gcode/src/index/api.rs`. [crates/gcode/src/index/api.rs:327-347]
- `upsert_calls` (function) component `upsert_calls [function]` (`43190ed3-8515-59d2-a699-288a839e5f70`) lines 349-383 [crates/gcode/src/index/api.rs:349-383]
  - Signature: `pub fn upsert_calls(`
  - Purpose: Indexed function `upsert_calls` in `crates/gcode/src/index/api.rs`. [crates/gcode/src/index/api.rs:349-383]
- `to_i32` (function) component `to_i32 [function]` (`b858b861-c078-5168-9ba2-2363bd9617eb`) lines 385-387 [crates/gcode/src/index/api.rs:385-387]
  - Signature: `fn to_i32(value: usize) -> i32 {`
  - Purpose: Indexed function `to_i32` in `crates/gcode/src/index/api.rs`. [crates/gcode/src/index/api.rs:385-387]

