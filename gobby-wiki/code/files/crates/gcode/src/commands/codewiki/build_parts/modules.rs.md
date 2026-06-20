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

`crates/gcode/src/commands/codewiki/build_parts/modules.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `build_module_docs_with_filter` | function | Builds 'ModuleDoc' records for all module names derived from the input files, filtered by 'module_filter' and processed deepest-first, while resolving symbol IDs for cross-module citations, aggregating per-module direct files and source spans, optionally driving generation/reuse/progress state, and invoking 'emit' for each generated document before returning the collected docs or an error. [crates/gcode/src/commands/codewiki/build_parts/modules.rs:27-201] |
| `file_is_direct_module_member` | function | Returns 'true' when the file’s own 'module' field matches the given module name or when the module inferred from 'file.path' equals that name, otherwise 'false'. [crates/gcode/src/commands/codewiki/build_parts/modules.rs:203-205] |
| `prompt_component_ids_for_module` | function | Returns a 'Vec<String>' containing each symbol’s 'component_label' and 'component_id' formatted as '"label (id)"' for all 'files' whose 'module' is either exactly the requested 'module' or a descendant of it, preserving the iteration order. [crates/gcode/src/commands/codewiki/build_parts/modules.rs:207-217] |

_Verified by 1 in-file unit test._

