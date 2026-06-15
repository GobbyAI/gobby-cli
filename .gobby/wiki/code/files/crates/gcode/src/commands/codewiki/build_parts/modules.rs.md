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

Builds `ModuleDoc` entries for modules related to a set of files, then emits and returns the completed docs. The main workflow gathers every ancestor module from each file’s recorded module and inferred path module, filters and processes modules deepest-first, and uses accumulated summaries/sources plus direct file and child-module links to assemble each document; the test-only `build_module_docs` wrapper just calls that path with an always-true filter. The helper functions extract unique direct component IDs, test whether a file is a direct member of a module, and format prompt component IDs for a module’s descendant symbols.
[crates/gcode/src/commands/codewiki/build_parts/modules.rs:6-27]
[crates/gcode/src/commands/codewiki/build_parts/modules.rs:30-175]
[crates/gcode/src/commands/codewiki/build_parts/modules.rs:177-188]
[crates/gcode/src/commands/codewiki/build_parts/modules.rs:190-192]
[crates/gcode/src/commands/codewiki/build_parts/modules.rs:194-204]

## API Symbols

- `build_module_docs` (function) component `build_module_docs [function]` (`8bc13251-cd9e-5d69-983c-eaec9f15fc96`) lines 6-27 [crates/gcode/src/commands/codewiki/build_parts/modules.rs:6-27]
  - Signature: `pub(crate) fn build_module_docs(`
  - Purpose: 'build_module_docs' is a thin wrapper that forwards all inputs to 'build_module_docs_with_filter' with an always-true path filter, emitting each produced 'ModuleDoc' and returning the collected 'Vec<ModuleDoc>' or an error. [crates/gcode/src/commands/codewiki/build_parts/modules.rs:6-27]
- `build_module_docs_with_filter` (function) component `build_module_docs_with_filter [function]` (`ffb67d2b-e3dd-56ba-86e4-3d7ac7863637`) lines 30-175 [crates/gcode/src/commands/codewiki/build_parts/modules.rs:30-175]
  - Signature: `pub(crate) fn build_module_docs_with_filter(`
  - Purpose: Builds 'ModuleDoc' entries for all ancestor modules referenced by 'files', filters them through 'module_filter', processes them deepest-first while aggregating direct file links and child module links from prior summaries/sources, emits each generated doc via 'emit', and returns the full list. [crates/gcode/src/commands/codewiki/build_parts/modules.rs:30-175]
- `direct_component_ids_for_module` (function) component `direct_component_ids_for_module [function]` (`93f406d5-ffea-5952-a944-498a82dc1b40`) lines 177-188 [crates/gcode/src/commands/codewiki/build_parts/modules.rs:177-188]
  - Signature: `fn direct_component_ids_for_module(files: &[FileDoc], module: &str) -> Vec<String> {`
  - Purpose: Collects and returns the unique 'component_id' values from symbols in files that are direct members of the given module, preserving first-seen iteration order by de-duplicating with a 'BTreeSet'. [crates/gcode/src/commands/codewiki/build_parts/modules.rs:177-188]
- `file_is_direct_module_member` (function) component `file_is_direct_module_member [function]` (`28b95157-57d6-51ac-a399-87cfae755efe`) lines 190-192 [crates/gcode/src/commands/codewiki/build_parts/modules.rs:190-192]
  - Signature: `fn file_is_direct_module_member(file: &FileDoc, module: &str) -> bool {`
  - Purpose: Returns 'true' when the file’s recorded module matches 'module' or when the module inferred from 'file.path' equals 'module'. [crates/gcode/src/commands/codewiki/build_parts/modules.rs:190-192]
- `prompt_component_ids_for_module` (function) component `prompt_component_ids_for_module [function]` (`1746e430-bb76-57d2-b659-5b84683e553c`) lines 194-204 [crates/gcode/src/commands/codewiki/build_parts/modules.rs:194-204]
  - Signature: `pub(super) fn prompt_component_ids_for_module(files: &[FileDoc], module: &str) -> Vec<String> {`
  - Purpose: Returns a 'Vec<String>' of formatted '"label (id)"' entries for every symbol in 'files' whose 'module' exactly matches the requested module or is a descendant of it. [crates/gcode/src/commands/codewiki/build_parts/modules.rs:194-204]

