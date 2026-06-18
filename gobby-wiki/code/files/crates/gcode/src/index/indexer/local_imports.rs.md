---
title: crates/gcode/src/index/indexer/local_imports.rs
type: code_file
provenance:
- file: crates/gcode/src/index/indexer/local_imports.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/indexer/local_imports.rs

Module: [[code/modules/crates/gcode/src/index/indexer|crates/gcode/src/index/indexer]]

## Overview

`crates/gcode/src/index/indexer/local_imports.rs` exposes 5 indexed API symbols.

## How it fits

`crates/gcode/src/index/indexer/local_imports.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `resolve_local_import_calls` | function | Reads pending local import call records for the given project and file paths from the database, then resolves them via 'resolve_pending_local_import_calls', returning the number processed. [crates/gcode/src/index/indexer/local_imports.rs:31-38] |
| `resolve_project_local_import_calls` | function | Fetches the pending local import calls for the given project from the database and delegates them to 'resolve_pending_local_import_calls', returning the resulting 'usize' count or error. [crates/gcode/src/index/indexer/local_imports.rs:43-49] |
| `resolve_pending_local_import_calls` | function | Resolves each pending 'CallRelation' against candidate local-import symbols in the database, promotes the call as resolved or unresolved via the API, and returns the number of calls successfully resolved. [crates/gcode/src/index/indexer/local_imports.rs:51-79] |
| `resolved_symbol_call` | function | Creates a new 'CallRelation' by cloning the caller symbol ID, callee name, file path, and line from 'original', then assigns 'callee_symbol_id' as the resolved symbol target. [crates/gcode/src/index/indexer/local_imports.rs:83-91] |
| `unresolved_call` | function | Constructs and returns a new 'CallRelation' that preserves the original caller symbol ID, callee name, file path, and line number, effectively recreating the call as unresolved. [crates/gcode/src/index/indexer/local_imports.rs:95-102] |

