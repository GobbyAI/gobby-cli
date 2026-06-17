---
title: crates/gcode/src/index/indexer/local_imports.rs
type: code_file
provenance:
- file: crates/gcode/src/index/indexer/local_imports.rs
  ranges:
  - 31-38
  - 43-49
  - 51-79
  - 83-91
  - 95-102
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/indexer/local_imports.rs:31-38](crates/gcode/src/index/indexer/local_imports.rs#L31-L38), [crates/gcode/src/index/indexer/local_imports.rs:43-49](crates/gcode/src/index/indexer/local_imports.rs#L43-L49), [crates/gcode/src/index/indexer/local_imports.rs:51-79](crates/gcode/src/index/indexer/local_imports.rs#L51-L79), [crates/gcode/src/index/indexer/local_imports.rs:83-91](crates/gcode/src/index/indexer/local_imports.rs#L83-L91), [crates/gcode/src/index/indexer/local_imports.rs:95-102](crates/gcode/src/index/indexer/local_imports.rs#L95-L102)

</details>

# crates/gcode/src/index/indexer/local_imports.rs

Module: [[code/modules/crates/gcode/src/index/indexer|crates/gcode/src/index/indexer]]

## Purpose

This file performs post-write resolution for cross-file `local_import` call relations. The public entry points, `resolve_local_import_calls` and `resolve_project_local_import_calls`, load pending rows from the database for a changed-file set or the whole project, then hand them to a shared resolver that rewrites each call to either a concrete `Symbol` target or `Unresolved`. The helper constructors `resolved_symbol_call` and `unresolved_call` build the updated `CallRelation` rows, including the conservative JavaScript default-import fallback when exactly one matching top-level callable/type symbol exists.
[crates/gcode/src/index/indexer/local_imports.rs:31-38]
[crates/gcode/src/index/indexer/local_imports.rs:43-49]
[crates/gcode/src/index/indexer/local_imports.rs:51-79]
[crates/gcode/src/index/indexer/local_imports.rs:83-91]
[crates/gcode/src/index/indexer/local_imports.rs:95-102]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `resolve_local_import_calls` | function | `pub(super) fn resolve_local_import_calls(` | `resolve_local_import_calls [function]` | `e9d7b8d0-066c-5821-9a9e-5042e6a80789` | 31-38 [crates/gcode/src/index/indexer/local_imports.rs:31-38] | Indexed function `resolve_local_import_calls` in `crates/gcode/src/index/indexer/local_imports.rs`. [crates/gcode/src/index/indexer/local_imports.rs:31-38] |
| `resolve_project_local_import_calls` | function | `pub(super) fn resolve_project_local_import_calls(` | `resolve_project_local_import_calls [function]` | `113fc65e-249b-5c1f-95bc-b22819bfaa7a` | 43-49 [crates/gcode/src/index/indexer/local_imports.rs:43-49] | Indexed function `resolve_project_local_import_calls` in `crates/gcode/src/index/indexer/local_imports.rs`. [crates/gcode/src/index/indexer/local_imports.rs:43-49] |
| `resolve_pending_local_import_calls` | function | `fn resolve_pending_local_import_calls(` | `resolve_pending_local_import_calls [function]` | `e4a84591-5199-569b-b27c-711aacab52ae` | 51-79 [crates/gcode/src/index/indexer/local_imports.rs:51-79] | Indexed function `resolve_pending_local_import_calls` in `crates/gcode/src/index/indexer/local_imports.rs`. [crates/gcode/src/index/indexer/local_imports.rs:51-79] |
| `resolved_symbol_call` | function | `fn resolved_symbol_call(original: &CallRelation, callee_symbol_id: String) -> CallRelation {` | `resolved_symbol_call [function]` | `f22a85a7-077e-5ea2-b356-900d6edd5db7` | 83-91 [crates/gcode/src/index/indexer/local_imports.rs:83-91] | Indexed function `resolved_symbol_call` in `crates/gcode/src/index/indexer/local_imports.rs`. [crates/gcode/src/index/indexer/local_imports.rs:83-91] |
| `unresolved_call` | function | `fn unresolved_call(original: &CallRelation) -> CallRelation {` | `unresolved_call [function]` | `58f99b18-a1b3-5f28-b3c0-c7ce97cda3fb` | 95-102 [crates/gcode/src/index/indexer/local_imports.rs:95-102] | Indexed function `unresolved_call` in `crates/gcode/src/index/indexer/local_imports.rs`. [crates/gcode/src/index/indexer/local_imports.rs:95-102] |
