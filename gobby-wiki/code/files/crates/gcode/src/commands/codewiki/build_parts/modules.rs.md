---
title: crates/gcode/src/commands/codewiki/build_parts/modules.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/modules.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/build_parts/modules.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]]

## Overview

`crates/gcode/src/commands/codewiki/build_parts/modules.rs` exposes 4 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/build_parts/modules.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `build_module_docs` | function | 'build_module_docs' is a thin wrapper that delegates to 'build_module_docs_with_filter', passing an always-true module filter to build 'ModuleDoc' values from the provided files, graph metadata, leading chunks, generator/reuse state, and progress tracker while emitting each generated doc via the supplied callback. [crates/gcode/src/commands/codewiki/build_parts/modules.rs:6-27] |
| `build_module_docs_with_filter` | function | Builds 'ModuleDoc' entries for all filtered modules discovered from the input files, ordered from deepest to shallowest, by collecting direct file and child-module links, tracking per-module summaries/source spans, and emitting each generated document through the provided callback while returning the full list. [crates/gcode/src/commands/codewiki/build_parts/modules.rs:30-175] |
| `file_is_direct_module_member` | function | Returns 'true' when the file’s recorded 'module' matches the given module name or when the module inferred from 'file.path' equals that name. [crates/gcode/src/commands/codewiki/build_parts/modules.rs:177-179] |
| `prompt_component_ids_for_module` | function | Returns a 'Vec<String>' containing '"label (id)"' strings for every symbol in each 'FileDoc' whose 'module' matches the target module or is a descendant of it. [crates/gcode/src/commands/codewiki/build_parts/modules.rs:181-191] |

