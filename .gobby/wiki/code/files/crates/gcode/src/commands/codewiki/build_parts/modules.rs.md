---
title: crates/gcode/src/commands/codewiki/build_parts/modules.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/modules.rs
  ranges:
  - 4-114
  - 116-126
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/build_parts/modules.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]]

## Purpose

`crates/gcode/src/commands/codewiki/build_parts/modules.rs` exposes 2 indexed API symbols. [crates/gcode/src/commands/codewiki/build_parts/modules.rs:4-114] [crates/gcode/src/commands/codewiki/build_parts/modules.rs:116-126]

## API Symbols

- `build_module_docs` (function) component `build_module_docs [function]` (`40915297-eb8e-5839-abd6-a5e1ef5cdb2f`) lines 4-114 [crates/gcode/src/commands/codewiki/build_parts/modules.rs:4-114]
  - Signature: `pub(crate) fn build_module_docs(`
  - Purpose: # Summary

`build_module_docs` builds a hierarchical collection of module documentation by aggregating input files into their parent modules, identifying child module relationships, and constructing ModuleDoc structures for each module sorted by depth. [crates/gcode/src/commands/codewiki/build_parts/modules.rs:4-114]
- `prompt_component_ids_for_module` (function) component `prompt_component_ids_for_module [function]` (`ca21e93d-eabf-56cd-8d68-9915e2d4e83b`) lines 116-126 [crates/gcode/src/commands/codewiki/build_parts/modules.rs:116-126]
  - Signature: `pub(super) fn prompt_component_ids_for_module(files: &[FileDoc], module: &str) -> Vec<String> {`
  - Purpose: This function filters files matching a specified module (or its ancestors) and returns a vector of formatted strings pairing component labels with their IDs from the symbols in those files. [crates/gcode/src/commands/codewiki/build_parts/modules.rs:116-126]

