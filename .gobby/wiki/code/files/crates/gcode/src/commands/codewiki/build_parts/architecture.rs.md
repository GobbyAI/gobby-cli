---
title: crates/gcode/src/commands/codewiki/build_parts/architecture.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/architecture.rs
  ranges:
  - 5-110
  - 112-127
  - 129-179
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/build_parts/architecture.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]]

## Purpose

`crates/gcode/src/commands/codewiki/build_parts/architecture.rs` exposes 3 indexed API symbols. [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:5-110] [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:112-127] [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:129-179]

## API Symbols

- `build_architecture_doc` (function) component `build_architecture_doc [function]` (`729c6797-7c1f-54df-9e47-ac5f3dbaf7b3`) lines 5-110 [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:5-110]
  - Signature: `pub(crate) fn build_architecture_doc(`
  - Purpose: Constructs an ArchitectureDoc by aggregating file and module metadata into subsystems while tracking graph availability degradation. [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:5-110]
- `module_dependency_edges` (function) component `module_dependency_edges [function]` (`53db5b0d-9c4d-52fc-8815-7e45d2be6887`) lines 112-127 [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:112-127]
  - Signature: `pub(super) fn module_dependency_edges(`
  - Purpose: Filters import-kind graph edges to produce a set of directed module-to-module dependency pairs by resolving component IDs to their module names and excluding intra-module imports. [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:112-127]
- `dependency_topology` (function) component `dependency_topology [function]` (`7a466ae9-8489-558b-85c4-182313d08bb5`) lines 129-179 [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:129-179]
  - Signature: `pub(super) fn dependency_topology(`
  - Purpose: Computes a topological rank for each module using Kahn's algorithm, where modules with no dependencies receive lower ranks and dependent modules receive progressively higher ranks. [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:129-179]

