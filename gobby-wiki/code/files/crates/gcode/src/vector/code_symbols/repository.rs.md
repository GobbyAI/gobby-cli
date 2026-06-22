---
title: crates/gcode/src/vector/code_symbols/repository.rs
type: code_file
provenance:
- file: crates/gcode/src/vector/code_symbols/repository.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/vector/code_symbols/repository.rs

Module: [[code/modules/crates/gcode/src/vector/code_symbols|crates/gcode/src/vector/code_symbols]]

## Overview

`crates/gcode/src/vector/code_symbols/repository.rs` exposes 6 indexed API symbols.

## How it fits

`crates/gcode/src/vector/code_symbols/repository.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `fetch_symbols_for_file` | function | Returns the list of 'Symbol' records for a given 'project_id' and 'file_path' by delegating to 'fetch_symbols_where' with a 'SymbolPredicate::File' filter. [crates/gcode/src/vector/code_symbols/repository.rs:6-18] |
| `fetch_symbols_for_project` | function | Fetches all 'Symbol' records for the specified 'project_id' by delegating to 'fetch_symbols_where' with a 'SymbolPredicate::Project' filter on the provided mutable 'GenericClient'. [crates/gcode/src/vector/code_symbols/repository.rs:20-25] |
| `SymbolPredicate` | type | Indexed type `SymbolPredicate` in `crates/gcode/src/vector/code_symbols/repository.rs`. [crates/gcode/src/vector/code_symbols/repository.rs:27-35] |
| `where_clause` | function | Returns a static SQL 'WHERE' predicate string for the enum variant, using 'project_id = $1' for 'Project' and 'project_id = $1 AND file_path = $2' for 'File'. [crates/gcode/src/vector/code_symbols/repository.rs:38-43] |
| `params` | function | Returns a vector of 'ToSql + Sync' trait-object references for the enum variant’s bound parameters, yielding 'project_id' alone for 'Project' and 'project_id' plus 'file_path' for 'File'. [crates/gcode/src/vector/code_symbols/repository.rs:45-56] |
| `fetch_symbols_where` | function | Queries 'code_symbols' with a predicate-derived 'WHERE' clause and bound parameters, orders results by 'file_path', 'byte_start', and 'id', and returns the rows mapped into 'Symbol' values. [crates/gcode/src/vector/code_symbols/repository.rs:59-77] |

