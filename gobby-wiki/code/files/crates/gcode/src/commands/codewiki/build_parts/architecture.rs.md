---
title: crates/gcode/src/commands/codewiki/build_parts/architecture.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/architecture.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/build_parts/architecture.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]]

## Overview

`crates/gcode/src/commands/codewiki/build_parts/architecture.rs` exposes 3 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/build_parts/architecture.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `build_architecture_doc` | function | Constructs an 'ArchitectureDoc' by identifying subsystem roots from file paths, marking graph data as degraded when truncated or unavailable, and then iterating over matching subsystem modules to assemble subsystem-level summaries and structure for the document. [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:5-169] |
| `module_dependency_edges` | function | Returns the deduplicated set of '(source_module, target_module)' pairs for import edges whose source and target components both map to distinct module names present in 'module_names'. [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:175-190] |
| `dependency_topology` | function | Computes a deterministic topological ordering map from module name to rank by performing a Kahn-style traversal over the directed dependency edges, then assigning any remaining modules after the traversal to ensure every input module is ranked. [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:193-243] |

