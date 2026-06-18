---
title: crates/gcode/src/commands/codewiki/build_parts/architecture.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/architecture.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/src/commands/codewiki/build_parts/architecture.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]]

## Overview

This file is responsible for constructing high-level architectural documentation for a codebase in the form of an ArchitectureDoc. It analyzes files, modules, and dependency relationships to map out how the system is organized.

The main driver in this file is build_architecture_doc crates/gcode/src/commands/codewiki/build_parts/architecture.rs:5-169. It groups files into logical subsystems, compiles subsystem-level summaries, and tracks the availability of dependency graph data, flagging the documentation as degraded if graph data is truncated or unavailable.

## How it fits

This file is a key component of the codewiki documentation-generation engine. It takes raw file listings, module definitions, and dependency edges, and refines them into a structured representation of the system layout and hierarchy.
[crates/gcode/src/commands/codewiki/build_parts/architecture.rs:5-169]
[crates/gcode/src/commands/codewiki/build_parts/architecture.rs:175-190]
[crates/gcode/src/commands/codewiki/build_parts/architecture.rs:193-243]

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `build_architecture_doc` | function | Constructs an 'ArchitectureDoc' by identifying subsystem roots from file paths, marking graph data as degraded when truncated or unavailable, and then iterating over matching subsystem modules to assemble subsystem-level summaries and structure for the document. [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:5-169] |
| `module_dependency_edges` | function | Returns the deduplicated set of '(source_module, target_module)' pairs for import edges whose source and target components both map to distinct module names present in 'module_names'. [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:175-190] |
| `dependency_topology` | function | Computes a deterministic topological ordering map from module name to rank by performing a Kahn-style traversal over the directed dependency edges, then assigning any remaining modules after the traversal to ensure every input module is ranked. [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:193-243] |

