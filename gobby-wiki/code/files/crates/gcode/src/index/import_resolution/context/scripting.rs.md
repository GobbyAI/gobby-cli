---
title: crates/gcode/src/index/import_resolution/context/scripting.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/context/scripting.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/import_resolution/context/scripting.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]

## Overview

`crates/gcode/src/index/import_resolution/context/scripting.rs` exposes 6 indexed API symbols.

## How it fits

`crates/gcode/src/index/import_resolution/context/scripting.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `build_lua_module_files` | function | Scans the given candidate paths in parallel for '.lua' files under 'root_path', derives Lua module names from each file’s path, aggregates a 'HashMap' from module name to sorted, deduplicated relative file paths, and returns that mapping. [crates/gcode/src/index/import_resolution/context/scripting.rs:11-55] |
| `lua_module_names_for_path` | function | Returns a 'HashSet<String>' of Lua module name candidates derived from 'without_ext', adding names for the full path and, if present, for versions with leading 'lua/' or 'src/' stripped. [crates/gcode/src/index/import_resolution/context/scripting.rs:57-66] |
| `add_lua_module_names` | function | Adds the trimmed, slash-delimited path as a Lua module name to 'modules', and if the path ends with '/init' it also adds the parent package name, ignoring empty paths. [crates/gcode/src/index/import_resolution/context/scripting.rs:68-77] |
| `insert_lua_module_name` | function | Normalizes a Lua module path by replacing '/' with '.' and inserts the resulting non-empty string into the provided 'HashSet<String>'. [crates/gcode/src/index/import_resolution/context/scripting.rs:79-84] |
| `build_php_symbol_files` | function | Builds a 'HashMap' from each readable '.php' file’s relative path to the set of lowercased PHP symbols it declares, including both bare and namespace-qualified names when a namespace is present. [crates/gcode/src/index/import_resolution/context/scripting.rs:86-150] |
| `build_ruby_constant_files` | function | Scans candidate '.rb', '.rake', and '.gemspec' files in parallel, extracts valid top-level constant roots from every 'class'/'module' declaration line, and builds a 'HashMap' from each root constant name to the relative file paths that define it. [crates/gcode/src/index/import_resolution/context/scripting.rs:152-218] |

