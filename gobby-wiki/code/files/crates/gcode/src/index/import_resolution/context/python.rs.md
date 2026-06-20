---
title: crates/gcode/src/index/import_resolution/context/python.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/context/python.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/import_resolution/context/python.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution/context|crates/gcode/src/index/import_resolution/context]]

## Overview

`crates/gcode/src/index/import_resolution/context/python.rs` exposes 5 indexed API symbols.

## How it fits

`crates/gcode/src/index/import_resolution/context/python.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `build_python_module_index` | function | Builds and returns a 'HashSet<String>' of Python module names by iterating over each candidate file path and unioning the module names produced by 'python_module_names_for_path(root_path, path)'. [crates/gcode/src/index/import_resolution/context/python.rs:4-15] |
| `python_candidate_files` | function | Constructs and returns the ordered set of Python source and package-path candidate filenames for a dotted module name by mapping dots to slashes and combining both the module root and 'src/'-prefixed paths with '.py'/'.pyi' file and '__init__' variants. [crates/gcode/src/index/import_resolution/context/python.rs:22-32] |
| `python_module_names_for_path` | function | Returns the Python module names for a file under 'root_path' by accepting only '.py'/'.pyi' paths, converting the relative path to dotted module notation, stripping a trailing '.__init__', and additionally returning a 'src.'-stripped alias when applicable. [crates/gcode/src/index/import_resolution/context/python.rs:34-63] |

_Verified by 2 in-file unit tests._

