---
title: crates/gcode/src/commands/codewiki/build_parts/architecture.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/architecture.rs
  ranges:
  - 5-169
  - 175-190
  - 193-243
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:5-169](crates/gcode/src/commands/codewiki/build_parts/architecture.rs#L5-L169), [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:175-190](crates/gcode/src/commands/codewiki/build_parts/architecture.rs#L175-L190), [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:193-243](crates/gcode/src/commands/codewiki/build_parts/architecture.rs#L193-L243)

</details>

# crates/gcode/src/commands/codewiki/build_parts/architecture.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]]

## Purpose

Builds the architecture section of a codewiki by turning the input file/module inventory, graph edges, graph availability state, and leading chunks into an `ArchitectureDoc`. It groups work around subsystem roots, assembles per-subsystem summaries with fallbacks and prompt-driven content, and tracks degraded graph sources when dependency data is truncated or unavailable. The helper functions `module_dependency_edges` and `dependency_topology` derive module-to-module edge information and organize it into a dependency structure used by the main document builder.
[crates/gcode/src/commands/codewiki/build_parts/architecture.rs:5-169]
[crates/gcode/src/commands/codewiki/build_parts/architecture.rs:175-190]
[crates/gcode/src/commands/codewiki/build_parts/architecture.rs:193-243]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `build_architecture_doc` | function | `pub(crate) fn build_architecture_doc(` | `build_architecture_doc [function]` | `729c6797-7c1f-54df-9e47-ac5f3dbaf7b3` | 5-169 [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:5-169] | Indexed function `build_architecture_doc` in `crates/gcode/src/commands/codewiki/build_parts/architecture.rs`. [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:5-169] |
| `module_dependency_edges` | function | `pub(super) fn module_dependency_edges(` | `module_dependency_edges [function]` | `bfe8ab44-8347-510d-9e01-f0adaa6662a0` | 175-190 [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:175-190] | Indexed function `module_dependency_edges` in `crates/gcode/src/commands/codewiki/build_parts/architecture.rs`. [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:175-190] |
| `dependency_topology` | function | `pub(super) fn dependency_topology(` | `dependency_topology [function]` | `9bcbb1c9-3d40-5d3d-9e99-29a73cf7fc7c` | 193-243 [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:193-243] | Indexed function `dependency_topology` in `crates/gcode/src/commands/codewiki/build_parts/architecture.rs`. [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:193-243] |
