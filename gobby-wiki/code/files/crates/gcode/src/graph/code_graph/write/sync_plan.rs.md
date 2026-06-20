---
title: crates/gcode/src/graph/code_graph/write/sync_plan.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/code_graph/write/sync_plan.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/graph/code_graph/write/sync_plan.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

`crates/gcode/src/graph/code_graph/write/sync_plan.rs` exposes 4 indexed API symbols.

## How it fits

`crates/gcode/src/graph/code_graph/write/sync_plan.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `plan_sync_batches` | function | Plans and returns a 'Vec<TypedQuery>' that first updates the file node with the final 'symbol_count' and 'sync_token', then appends chunked import, definition, and call insertion queries for the given 'SyncFileMutation', omitting any empty chunks. [crates/gcode/src/graph/code_graph/write/sync_plan.rs:30-81] |
| `test_symbol` | function | Constructs and returns a 'Symbol' test fixture populated with fixed project/file metadata, 'function'/'rust' kind and language, zero byte offsets, line numbers set to 'i', formatted identifiers derived from 'i', and all optional/text fields left empty or 'None'. [crates/gcode/src/graph/code_graph/write/sync_plan.rs:89-110] |

_Verified by 2 in-file unit tests._

