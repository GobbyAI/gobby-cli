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
| `build_module_docs_with_filter` | function | # Summary Constructs and emits a filtered collection of ModuleDoc structures from source files and code graph edges, resolving symbol references and processing modules in reverse-depth order. [crates/gcode/src/commands/codewiki/build_parts/modules.rs:27-201] |
| `file_is_direct_module_member` | function | Returns 'true' if the file's stored module field equals the given module string, or if the module computed from the file's path equals the given module string. [crates/gcode/src/commands/codewiki/build_parts/modules.rs:203-205] |
| `prompt_component_ids_for_module` | function | This function filters 'FileDoc' entries by module membership (including descendant modules) and returns a vector of formatted strings pairing each symbol's component label with its ID. [crates/gcode/src/commands/codewiki/build_parts/modules.rs:207-217] |

_Verified by 1 in-file unit test._

