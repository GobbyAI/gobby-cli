---
title: crates/gcode/src/commands/codewiki/build_parts/architecture.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/architecture.rs
  ranges:
  - 5-168
  - 174-189
  - 192-242
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/build_parts/architecture.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]]

## Purpose

This file builds architecture documentation for the codewiki system by analyzing code structure and module relationships. The main function `build_architecture_doc` orchestrates the process: it identifies subsystem roots from file paths, tracks graph availability states, collects module and file summaries, and generates architectural narratives. Supporting functions `module_dependency_edges` and `dependency_topology` analyze how modules depend on each other and their structural relationships. Together, these functions transform raw code structure data into coherent architecture documentation that describes subsystems, their internal organization, and cross-subsystem dependencies at the workspace crate level.
[crates/gcode/src/commands/codewiki/build_parts/architecture.rs:5-168]
[crates/gcode/src/commands/codewiki/build_parts/architecture.rs:174-189]
[crates/gcode/src/commands/codewiki/build_parts/architecture.rs:192-242]

## API Symbols

- `build_architecture_doc` (function) component `build_architecture_doc [function]` (`729c6797-7c1f-54df-9e47-ac5f3dbaf7b3`) lines 5-168 [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:5-168]
  - Signature: `pub(crate) fn build_architecture_doc(`
  - Purpose: Indexed function `build_architecture_doc` in `crates/gcode/src/commands/codewiki/build_parts/architecture.rs`. [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:5-168]
- `module_dependency_edges` (function) component `module_dependency_edges [function]` (`ca2df816-0c56-5c43-8920-351df8f54065`) lines 174-189 [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:174-189]
  - Signature: `pub(super) fn module_dependency_edges(`
  - Purpose: Indexed function `module_dependency_edges` in `crates/gcode/src/commands/codewiki/build_parts/architecture.rs`. [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:174-189]
- `dependency_topology` (function) component `dependency_topology [function]` (`60c5fe3d-c130-5e4a-b2f8-93f4b55dacd0`) lines 192-242 [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:192-242]
  - Signature: `pub(super) fn dependency_topology(`
  - Purpose: Indexed function `dependency_topology` in `crates/gcode/src/commands/codewiki/build_parts/architecture.rs`. [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:192-242]

