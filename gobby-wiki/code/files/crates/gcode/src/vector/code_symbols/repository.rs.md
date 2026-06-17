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

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/vector/code_symbols/repository.rs:6-18](crates/gcode/src/vector/code_symbols/repository.rs#L6-L18), [crates/gcode/src/vector/code_symbols/repository.rs:20-25](crates/gcode/src/vector/code_symbols/repository.rs#L20-L25), [crates/gcode/src/vector/code_symbols/repository.rs:27-35](crates/gcode/src/vector/code_symbols/repository.rs#L27-L35), [crates/gcode/src/vector/code_symbols/repository.rs:38-43](crates/gcode/src/vector/code_symbols/repository.rs#L38-L43), [crates/gcode/src/vector/code_symbols/repository.rs:45-56](crates/gcode/src/vector/code_symbols/repository.rs#L45-L56), [crates/gcode/src/vector/code_symbols/repository.rs:59-77](crates/gcode/src/vector/code_symbols/repository.rs#L59-L77)

</details>

# crates/gcode/src/vector/code_symbols/repository.rs

Module: [[code/modules/crates/gcode/src/vector/code_symbols|crates/gcode/src/vector/code_symbols]]

## Purpose

Provides database repository helpers for loading `Symbol` records from `code_symbols` either for an entire project or a single file. The two public entry points build a `SymbolPredicate` and delegate to a shared `fetch_symbols_where` helper, which derives the SQL `WHERE` clause and bound parameters from the predicate, selects the standard symbol columns, orders results by `file_path`, `byte_start`, and `id`, and converts each returned row into a `Symbol`.
[crates/gcode/src/vector/code_symbols/repository.rs:6-18]
[crates/gcode/src/vector/code_symbols/repository.rs:20-25]
[crates/gcode/src/vector/code_symbols/repository.rs:27-35]
[crates/gcode/src/vector/code_symbols/repository.rs:38-43]
[crates/gcode/src/vector/code_symbols/repository.rs:45-56]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `fetch_symbols_for_file` | function | `pub fn fetch_symbols_for_file(` | `fetch_symbols_for_file [function]` | `900254d8-e0ac-5da2-8534-6625be83a1b7` | 6-18 [crates/gcode/src/vector/code_symbols/repository.rs:6-18] | Indexed function `fetch_symbols_for_file` in `crates/gcode/src/vector/code_symbols/repository.rs`. [crates/gcode/src/vector/code_symbols/repository.rs:6-18] |
| `fetch_symbols_for_project` | function | `pub fn fetch_symbols_for_project(` | `fetch_symbols_for_project [function]` | `24dee124-d569-52ac-a227-d502192f3000` | 20-25 [crates/gcode/src/vector/code_symbols/repository.rs:20-25] | Indexed function `fetch_symbols_for_project` in `crates/gcode/src/vector/code_symbols/repository.rs`. [crates/gcode/src/vector/code_symbols/repository.rs:20-25] |
| `SymbolPredicate` | type | `enum SymbolPredicate<'a> {` | `SymbolPredicate [type]` | `f099144b-c3ae-5799-bc8d-0636b2b55e49` | 27-35 [crates/gcode/src/vector/code_symbols/repository.rs:27-35] | Indexed type `SymbolPredicate` in `crates/gcode/src/vector/code_symbols/repository.rs`. [crates/gcode/src/vector/code_symbols/repository.rs:27-35] |
| `where_clause` | function | `fn where_clause(&self) -> &'static str {` | `where_clause [function]` | `c547315e-db62-5fc6-a76c-6bd5eec4890b` | 38-43 [crates/gcode/src/vector/code_symbols/repository.rs:38-43] | Indexed function `where_clause` in `crates/gcode/src/vector/code_symbols/repository.rs`. [crates/gcode/src/vector/code_symbols/repository.rs:38-43] |
| `params` | function | `fn params(&self) -> Vec<&(dyn ToSql + Sync)> {` | `params [function]` | `9da68607-8d69-53d0-9f28-0de943e3f0a5` | 45-56 [crates/gcode/src/vector/code_symbols/repository.rs:45-56] | Indexed function `params` in `crates/gcode/src/vector/code_symbols/repository.rs`. [crates/gcode/src/vector/code_symbols/repository.rs:45-56] |
| `fetch_symbols_where` | function | `fn fetch_symbols_where(` | `fetch_symbols_where [function]` | `bb5add13-83d0-5d5f-97a5-b318647215f4` | 59-77 [crates/gcode/src/vector/code_symbols/repository.rs:59-77] | Indexed function `fetch_symbols_where` in `crates/gcode/src/vector/code_symbols/repository.rs`. [crates/gcode/src/vector/code_symbols/repository.rs:59-77] |
