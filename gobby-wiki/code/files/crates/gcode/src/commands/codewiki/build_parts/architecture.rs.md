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

`crates/gcode/src/commands/codewiki/build_parts/architecture.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `build_architecture_doc` | function | The 'build_architecture_doc' function compiles an 'ArchitectureDoc' by clustering workspace files and modules into subsystem roots, aggregating file and child module summaries, and optionally generating system topology and runtime-flow diagrams from a provided 'SystemModel'. [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:5-170] |
| `module_dependency_edges` | function | This function extracts a unique set of directed module-to-module dependency pairs from import graph edges by resolving source and target component IDs to their respective module names, filtering out self-dependencies, and ensuring both modules exist in the allowed set. [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:176-191] |
| `dependency_topology` | function | This function calculates a topological ordering of modules based on a set of dependency edges using a modified Kahn's algorithm, returning a map of module names to their sequential evaluation rank and appending any remaining cyclic or unreached modules to the end of the order. [crates/gcode/src/commands/codewiki/build_parts/architecture.rs:194-244] |

