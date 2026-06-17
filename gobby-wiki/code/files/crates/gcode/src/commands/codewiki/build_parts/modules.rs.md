---
title: crates/gcode/src/commands/codewiki/build_parts/modules.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/modules.rs
  ranges:
  - 6-27
  - 30-177
  - 179-190
  - 192-194
  - 196-206
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/codewiki/build_parts/modules.rs:6-27](crates/gcode/src/commands/codewiki/build_parts/modules.rs#L6-L27), [crates/gcode/src/commands/codewiki/build_parts/modules.rs:30-177](crates/gcode/src/commands/codewiki/build_parts/modules.rs#L30-L177), [crates/gcode/src/commands/codewiki/build_parts/modules.rs:179-190](crates/gcode/src/commands/codewiki/build_parts/modules.rs#L179-L190), [crates/gcode/src/commands/codewiki/build_parts/modules.rs:192-194](crates/gcode/src/commands/codewiki/build_parts/modules.rs#L192-L194), [crates/gcode/src/commands/codewiki/build_parts/modules.rs:196-206](crates/gcode/src/commands/codewiki/build_parts/modules.rs#L196-L206)

</details>

# crates/gcode/src/commands/codewiki/build_parts/modules.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]]

## Purpose

Builds `ModuleDoc` entries for codewiki modules by collecting all module names from the input files, ordering them from deepest to shallowest, and then emitting documentation for each module while tracking progress and reusing generated content where possible. `build_module_docs` is a test-only convenience wrapper that calls the filtered builder with a match-all predicate, while `build_module_docs_with_filter` does the real work: it groups direct files for each module, gathers summaries and source spans, and produces the final docs through the supplied `emit` callback. The helper functions support that pipeline by identifying direct module membership, deriving direct component IDs for a module, and listing prompt component IDs used when assembling module documentation.
[crates/gcode/src/commands/codewiki/build_parts/modules.rs:6-27]
[crates/gcode/src/commands/codewiki/build_parts/modules.rs:30-177]
[crates/gcode/src/commands/codewiki/build_parts/modules.rs:179-190]
[crates/gcode/src/commands/codewiki/build_parts/modules.rs:192-194]
[crates/gcode/src/commands/codewiki/build_parts/modules.rs:196-206]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `build_module_docs` | function | `pub(crate) fn build_module_docs(` | `build_module_docs [function]` | `8bc13251-cd9e-5d69-983c-eaec9f15fc96` | 6-27 [crates/gcode/src/commands/codewiki/build_parts/modules.rs:6-27] | Indexed function `build_module_docs` in `crates/gcode/src/commands/codewiki/build_parts/modules.rs`. [crates/gcode/src/commands/codewiki/build_parts/modules.rs:6-27] |
| `build_module_docs_with_filter` | function | `pub(crate) fn build_module_docs_with_filter(` | `build_module_docs_with_filter [function]` | `ffb67d2b-e3dd-56ba-86e4-3d7ac7863637` | 30-177 [crates/gcode/src/commands/codewiki/build_parts/modules.rs:30-177] | Indexed function `build_module_docs_with_filter` in `crates/gcode/src/commands/codewiki/build_parts/modules.rs`. [crates/gcode/src/commands/codewiki/build_parts/modules.rs:30-177] |
| `direct_component_ids_for_module` | function | `fn direct_component_ids_for_module(files: &[FileDoc], module: &str) -> Vec<String> {` | `direct_component_ids_for_module [function]` | `1ba07aa3-28a3-5b57-9dcc-97fb791bf04b` | 179-190 [crates/gcode/src/commands/codewiki/build_parts/modules.rs:179-190] | Indexed function `direct_component_ids_for_module` in `crates/gcode/src/commands/codewiki/build_parts/modules.rs`. [crates/gcode/src/commands/codewiki/build_parts/modules.rs:179-190] |
| `file_is_direct_module_member` | function | `fn file_is_direct_module_member(file: &FileDoc, module: &str) -> bool {` | `file_is_direct_module_member [function]` | `f5bfc909-c750-550b-815b-863f62a119e7` | 192-194 [crates/gcode/src/commands/codewiki/build_parts/modules.rs:192-194] | Indexed function `file_is_direct_module_member` in `crates/gcode/src/commands/codewiki/build_parts/modules.rs`. [crates/gcode/src/commands/codewiki/build_parts/modules.rs:192-194] |
| `prompt_component_ids_for_module` | function | `pub(super) fn prompt_component_ids_for_module(files: &[FileDoc], module: &str) -> Vec<String> {` | `prompt_component_ids_for_module [function]` | `d98f5a34-0a08-5d36-9f13-d3332cccfca1` | 196-206 [crates/gcode/src/commands/codewiki/build_parts/modules.rs:196-206] | Indexed function `prompt_component_ids_for_module` in `crates/gcode/src/commands/codewiki/build_parts/modules.rs`. [crates/gcode/src/commands/codewiki/build_parts/modules.rs:196-206] |
