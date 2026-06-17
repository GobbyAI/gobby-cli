---
title: crates/gcode/src/graph/code_graph/read/payload_queries.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/code_graph/read/payload_queries.rs
  ranges:
  - 10-29
  - 31-47
  - 49-68
  - 70-90
  - 92-106
  - 108-130
  - 132-153
  - 155-169
  - 171-195
  - 197-219
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/graph/code_graph/read/payload_queries.rs:10-29](crates/gcode/src/graph/code_graph/read/payload_queries.rs#L10-L29), [crates/gcode/src/graph/code_graph/read/payload_queries.rs:31-47](crates/gcode/src/graph/code_graph/read/payload_queries.rs#L31-L47), [crates/gcode/src/graph/code_graph/read/payload_queries.rs:49-68](crates/gcode/src/graph/code_graph/read/payload_queries.rs#L49-L68), [crates/gcode/src/graph/code_graph/read/payload_queries.rs:70-90](crates/gcode/src/graph/code_graph/read/payload_queries.rs#L70-L90), [crates/gcode/src/graph/code_graph/read/payload_queries.rs:92-106](crates/gcode/src/graph/code_graph/read/payload_queries.rs#L92-L106), [crates/gcode/src/graph/code_graph/read/payload_queries.rs:108-130](crates/gcode/src/graph/code_graph/read/payload_queries.rs#L108-L130), [crates/gcode/src/graph/code_graph/read/payload_queries.rs:132-153](crates/gcode/src/graph/code_graph/read/payload_queries.rs#L132-L153), [crates/gcode/src/graph/code_graph/read/payload_queries.rs:155-169](crates/gcode/src/graph/code_graph/read/payload_queries.rs#L155-L169), [crates/gcode/src/graph/code_graph/read/payload_queries.rs:171-195](crates/gcode/src/graph/code_graph/read/payload_queries.rs#L171-L195), [crates/gcode/src/graph/code_graph/read/payload_queries.rs:197-219](crates/gcode/src/graph/code_graph/read/payload_queries.rs#L197-L219)

</details>

# crates/gcode/src/graph/code_graph/read/payload_queries.rs

Module: [[code/modules/crates/gcode/src/graph/code_graph/read|crates/gcode/src/graph/code_graph/read]]

## Purpose

Builds Cypher query strings and parameter maps for read-side code graph payloads. The functions cover project-wide overview queries for files, imports, defines, and calls, plus file-scoped symbol and call queries, symbol-neighbor lookup, and blast-radius queries centered on a symbol or file. They share helpers from `support` to clamp limits and reuse common return/typing fragments, while `typed_query` is used to format safe parameter literals and string maps for the caller.
[crates/gcode/src/graph/code_graph/read/payload_queries.rs:10-29]
[crates/gcode/src/graph/code_graph/read/payload_queries.rs:31-47]
[crates/gcode/src/graph/code_graph/read/payload_queries.rs:49-68]
[crates/gcode/src/graph/code_graph/read/payload_queries.rs:70-90]
[crates/gcode/src/graph/code_graph/read/payload_queries.rs:92-106]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `project_overview_files_query` | function | `pub(super) fn project_overview_files_query(` | `project_overview_files_query [function]` | `6d014b62-6981-513f-b630-77e05091f813` | 10-29 [crates/gcode/src/graph/code_graph/read/payload_queries.rs:10-29] | Indexed function `project_overview_files_query` in `crates/gcode/src/graph/code_graph/read/payload_queries.rs`. [crates/gcode/src/graph/code_graph/read/payload_queries.rs:10-29] |
| `project_overview_imports_query` | function | `pub(super) fn project_overview_imports_query(` | `project_overview_imports_query [function]` | `01a3ccf5-d2d1-5ce6-92bc-687095e11869` | 31-47 [crates/gcode/src/graph/code_graph/read/payload_queries.rs:31-47] | Indexed function `project_overview_imports_query` in `crates/gcode/src/graph/code_graph/read/payload_queries.rs`. [crates/gcode/src/graph/code_graph/read/payload_queries.rs:31-47] |
| `project_overview_defines_query` | function | `pub(super) fn project_overview_defines_query(` | `project_overview_defines_query [function]` | `a4367271-426d-590f-824a-9556d7c192fa` | 49-68 [crates/gcode/src/graph/code_graph/read/payload_queries.rs:49-68] | Indexed function `project_overview_defines_query` in `crates/gcode/src/graph/code_graph/read/payload_queries.rs`. [crates/gcode/src/graph/code_graph/read/payload_queries.rs:49-68] |
| `project_overview_calls_query` | function | `pub(super) fn project_overview_calls_query(` | `project_overview_calls_query [function]` | `8b0c237a-fa1b-5ee8-9f21-555cc8d45e29` | 70-90 [crates/gcode/src/graph/code_graph/read/payload_queries.rs:70-90] | Indexed function `project_overview_calls_query` in `crates/gcode/src/graph/code_graph/read/payload_queries.rs`. [crates/gcode/src/graph/code_graph/read/payload_queries.rs:70-90] |
| `file_symbols_query` | function | `pub(super) fn file_symbols_query(` | `file_symbols_query [function]` | `87eb1231-cd2e-5a60-9d83-4356b3705e94` | 92-106 [crates/gcode/src/graph/code_graph/read/payload_queries.rs:92-106] | Indexed function `file_symbols_query` in `crates/gcode/src/graph/code_graph/read/payload_queries.rs`. [crates/gcode/src/graph/code_graph/read/payload_queries.rs:92-106] |
| `file_calls_query` | function | `pub(in crate::graph::code_graph) fn file_calls_query(` | `file_calls_query [function]` | `93cf4493-2000-50a1-becc-4b8c376941d3` | 108-130 [crates/gcode/src/graph/code_graph/read/payload_queries.rs:108-130] | Indexed function `file_calls_query` in `crates/gcode/src/graph/code_graph/read/payload_queries.rs`. [crates/gcode/src/graph/code_graph/read/payload_queries.rs:108-130] |
| `symbol_neighbors_query` | function | `pub(super) fn symbol_neighbors_query(` | `symbol_neighbors_query [function]` | `8a178b30-5b98-5d1f-9c0f-cac8cbeb7df0` | 132-153 [crates/gcode/src/graph/code_graph/read/payload_queries.rs:132-153] | Indexed function `symbol_neighbors_query` in `crates/gcode/src/graph/code_graph/read/payload_queries.rs`. [crates/gcode/src/graph/code_graph/read/payload_queries.rs:132-153] |
| `blast_radius_center_query` | function | `pub(super) fn blast_radius_center_query(` | `blast_radius_center_query [function]` | `bb1959b0-6d27-550f-86b0-1cc6f1059b6a` | 155-169 [crates/gcode/src/graph/code_graph/read/payload_queries.rs:155-169] | Indexed function `blast_radius_center_query` in `crates/gcode/src/graph/code_graph/read/payload_queries.rs`. [crates/gcode/src/graph/code_graph/read/payload_queries.rs:155-169] |
| `blast_radius_file_call_query` | function | `pub(super) fn blast_radius_file_call_query(` | `blast_radius_file_call_query [function]` | `30c5026a-d8e4-5662-b7e2-8b88703b58e1` | 171-195 [crates/gcode/src/graph/code_graph/read/payload_queries.rs:171-195] | Indexed function `blast_radius_file_call_query` in `crates/gcode/src/graph/code_graph/read/payload_queries.rs`. [crates/gcode/src/graph/code_graph/read/payload_queries.rs:171-195] |
| `blast_radius_file_import_query` | function | `pub(in crate::graph::code_graph) fn blast_radius_file_import_query(` | `blast_radius_file_import_query [function]` | `523340bd-a63d-5155-9cd2-fd5554f1c20c` | 197-219 [crates/gcode/src/graph/code_graph/read/payload_queries.rs:197-219] | Indexed function `blast_radius_file_import_query` in `crates/gcode/src/graph/code_graph/read/payload_queries.rs`. [crates/gcode/src/graph/code_graph/read/payload_queries.rs:197-219] |
