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

Builds the architecture section of a codewiki by turning file and module data into subsystem-level documentation. `build_architecture_doc` identifies subsystem roots from file paths, marks the result as degraded when dependency graph data is truncated or missing, then iterates the relevant modules to assemble summaries from direct files, child modules, link spans, prompts, and fallback structural summaries while tracking progress. `module_dependency_edges` extracts unique inter-module dependency pairs from graph edges, ignoring intra-module imports, and `dependency_topology` uses those edges to produce a deterministic module ordering that prioritizes modules with fewer unresolved dependencies and appends cyclic or disconnected ones last.
[crates/gcode/src/commands/codewiki/build_parts/architecture.rs:5-168]
[crates/gcode/src/commands/codewiki/build_parts/architecture.rs:174-189]
[crates/gcode/src/commands/codewiki/build_parts/architecture.rs:192-242]

## API Symbols

- `build_architecture_doc` (function) component `build_architecture_doc [function]` (`729c6797-7c1f-54df-9e47-ac5f3dbaf7b3`) lines 5-168 [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:5-168]
  - Signature: `pub(crate) fn build_architecture_doc(`
  - Purpose: Builds an 'ArchitectureDoc' by identifying subsystem-root modules from file paths, marking degraded graph sources when graph data is truncated or unavailable, and assembling subsystem-level summaries from the supplied files, modules, graph edges, leading chunks, generator, and progress state. [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:5-168]
- `module_dependency_edges` (function) component `module_dependency_edges [function]` (`ca2df816-0c56-5c43-8920-351df8f54065`) lines 174-189 [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:174-189]
  - Signature: `pub(super) fn module_dependency_edges(`
  - Purpose: Returns the set of unique '(source_module, target_module)' pairs for import edges whose source and target components both map to known modules, excluding intra-module imports. [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:174-189]
- `dependency_topology` (function) component `dependency_topology [function]` (`60c5fe3d-c130-5e4a-b2f8-93f4b55dacd0`) lines 192-242 [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:192-242]
  - Signature: `pub(super) fn dependency_topology(`
  - Purpose: Computes a deterministic topological ranking of the given module set by Kahn-style traversal over the directed edge set, assigning lower indices to modules with fewer unresolved dependencies and appending any remaining cyclic or disconnected modules afterward. [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:192-242]

