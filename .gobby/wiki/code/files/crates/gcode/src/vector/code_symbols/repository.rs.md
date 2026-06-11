---
title: crates/gcode/src/vector/code_symbols/repository.rs
type: code_file
provenance:
- file: crates/gcode/src/vector/code_symbols/repository.rs
  ranges:
  - 6-18
  - 20-25
  - 27-35
  - 38-43
  - 45-56
  - 59-77
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/vector/code_symbols/repository.rs

Module: [[code/modules/crates/gcode/src/vector/code_symbols|crates/gcode/src/vector/code_symbols]]

## Purpose

`crates/gcode/src/vector/code_symbols/repository.rs` exposes 6 indexed API symbols.
[crates/gcode/src/vector/code_symbols/repository.rs:6-18]
[crates/gcode/src/vector/code_symbols/repository.rs:20-25]
[crates/gcode/src/vector/code_symbols/repository.rs:27-35]
[crates/gcode/src/vector/code_symbols/repository.rs:38-43]
[crates/gcode/src/vector/code_symbols/repository.rs:45-56]

## API Symbols

- `fetch_symbols_for_file` (function) component `fetch_symbols_for_file [function]` (`900254d8-e0ac-5da2-8534-6625be83a1b7`) lines 6-18 [crates/gcode/src/vector/code_symbols/repository.rs:6-18]
  - Signature: `pub fn fetch_symbols_for_file(`
  - Purpose: Fetches all Symbol records from the database that match the specified project ID and file path. [crates/gcode/src/vector/code_symbols/repository.rs:6-18]
- `fetch_symbols_for_project` (function) component `fetch_symbols_for_project [function]` (`24dee124-d569-52ac-a227-d502192f3000`) lines 20-25 [crates/gcode/src/vector/code_symbols/repository.rs:20-25]
  - Signature: `pub fn fetch_symbols_for_project(`
  - Purpose: Fetches and returns a vector of symbols for a specified project ID from a database connection, wrapped in a Result type for error handling. [crates/gcode/src/vector/code_symbols/repository.rs:20-25]
- `SymbolPredicate` (type) component `SymbolPredicate [type]` (`f099144b-c3ae-5799-bc8d-0636b2b55e49`) lines 27-35 [crates/gcode/src/vector/code_symbols/repository.rs:27-35]
  - Signature: `enum SymbolPredicate<'a> {`
  - Purpose: Indexed type `SymbolPredicate` in `crates/gcode/src/vector/code_symbols/repository.rs`. [crates/gcode/src/vector/code_symbols/repository.rs:27-35]
- `where_clause` (function) component `where_clause [function]` (`c547315e-db62-5fc6-a76c-6bd5eec4890b`) lines 38-43 [crates/gcode/src/vector/code_symbols/repository.rs:38-43]
  - Signature: `fn where_clause(&self) -> &'static str {`
  - Purpose: This method returns a static SQL WHERE clause string that conditionally filters by `project_id` alone for `Project` variants or by both `project_id` and `file_path` for `File` variants. [crates/gcode/src/vector/code_symbols/repository.rs:38-43]
- `params` (function) component `params [function]` (`9da68607-8d69-53d0-9f28-0de943e3f0a5`) lines 45-56 [crates/gcode/src/vector/code_symbols/repository.rs:45-56]
  - Signature: `fn params(&self) -> Vec<&(dyn ToSql + Sync)> {`
  - Purpose: Returns the enum variant's fields as a vector of trait object references implementing `ToSql + Sync` for SQL parameterization. [crates/gcode/src/vector/code_symbols/repository.rs:45-56]
- `fetch_symbols_where` (function) component `fetch_symbols_where [function]` (`bb5add13-83d0-5d5f-97a5-b318647215f4`) lines 59-77 [crates/gcode/src/vector/code_symbols/repository.rs:59-77]
  - Signature: `fn fetch_symbols_where(`
  - Purpose: Executes a parameterized SQL query against the code_symbols table using a WHERE clause derived from the SymbolPredicate, maps result rows to Symbol domain objects, and returns them ordered by file path and byte offset. [crates/gcode/src/vector/code_symbols/repository.rs:59-77]

