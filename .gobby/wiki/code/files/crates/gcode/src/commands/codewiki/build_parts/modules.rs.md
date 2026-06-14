---
title: crates/gcode/src/commands/codewiki/build_parts/modules.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/modules.rs
  ranges:
  - 6-27
  - 30-175
  - 177-188
  - 190-192
  - 194-204
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/build_parts/modules.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]]

## Purpose

Builds `ModuleDoc` entries for codewiki by collecting all module names implied by the input files, ordering them from deepest to shallowest, and emitting documentation for each module through a provided callback. `build_module_docs` is a test-only convenience wrapper that forwards to `build_module_docs_with_filter` with no filtering, while the main function coordinates module selection, summary/source accumulation, progress tracking, and reuse/generation plumbing.

The helper functions identify direct module membership, derive direct component IDs for a module, and prompt for component IDs when needed, so the builder can connect files and graph edges to the correct module-level documentation.
[crates/gcode/src/commands/codewiki/build_parts/modules.rs:6-27]
[crates/gcode/src/commands/codewiki/build_parts/modules.rs:30-175]
[crates/gcode/src/commands/codewiki/build_parts/modules.rs:177-188]
[crates/gcode/src/commands/codewiki/build_parts/modules.rs:190-192]
[crates/gcode/src/commands/codewiki/build_parts/modules.rs:194-204]

## API Symbols

- `build_module_docs` (function) component `build_module_docs [function]` (`8bc13251-cd9e-5d69-983c-eaec9f15fc96`) lines 6-27 [crates/gcode/src/commands/codewiki/build_parts/modules.rs:6-27]
  - Signature: `pub(crate) fn build_module_docs(`
  - Purpose: Indexed function `build_module_docs` in `crates/gcode/src/commands/codewiki/build_parts/modules.rs`. [crates/gcode/src/commands/codewiki/build_parts/modules.rs:6-27]
- `build_module_docs_with_filter` (function) component `build_module_docs_with_filter [function]` (`ffb67d2b-e3dd-56ba-86e4-3d7ac7863637`) lines 30-175 [crates/gcode/src/commands/codewiki/build_parts/modules.rs:30-175]
  - Signature: `pub(crate) fn build_module_docs_with_filter(`
  - Purpose: Indexed function `build_module_docs_with_filter` in `crates/gcode/src/commands/codewiki/build_parts/modules.rs`. [crates/gcode/src/commands/codewiki/build_parts/modules.rs:30-175]
- `direct_component_ids_for_module` (function) component `direct_component_ids_for_module [function]` (`93f406d5-ffea-5952-a944-498a82dc1b40`) lines 177-188 [crates/gcode/src/commands/codewiki/build_parts/modules.rs:177-188]
  - Signature: `fn direct_component_ids_for_module(files: &[FileDoc], module: &str) -> Vec<String> {`
  - Purpose: Indexed function `direct_component_ids_for_module` in `crates/gcode/src/commands/codewiki/build_parts/modules.rs`. [crates/gcode/src/commands/codewiki/build_parts/modules.rs:177-188]
- `file_is_direct_module_member` (function) component `file_is_direct_module_member [function]` (`28b95157-57d6-51ac-a399-87cfae755efe`) lines 190-192 [crates/gcode/src/commands/codewiki/build_parts/modules.rs:190-192]
  - Signature: `fn file_is_direct_module_member(file: &FileDoc, module: &str) -> bool {`
  - Purpose: Indexed function `file_is_direct_module_member` in `crates/gcode/src/commands/codewiki/build_parts/modules.rs`. [crates/gcode/src/commands/codewiki/build_parts/modules.rs:190-192]
- `prompt_component_ids_for_module` (function) component `prompt_component_ids_for_module [function]` (`1746e430-bb76-57d2-b659-5b84683e553c`) lines 194-204 [crates/gcode/src/commands/codewiki/build_parts/modules.rs:194-204]
  - Signature: `pub(super) fn prompt_component_ids_for_module(files: &[FileDoc], module: &str) -> Vec<String> {`
  - Purpose: Indexed function `prompt_component_ids_for_module` in `crates/gcode/src/commands/codewiki/build_parts/modules.rs`. [crates/gcode/src/commands/codewiki/build_parts/modules.rs:194-204]

