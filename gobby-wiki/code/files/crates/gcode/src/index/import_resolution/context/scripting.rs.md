---
title: crates/gcode/src/index/import_resolution/context/scripting.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/context/scripting.rs
  ranges:
  - 11-55
  - 57-66
  - 68-77
  - 79-84
  - 86-150
  - 152-218
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/import_resolution/context/scripting.rs:11-55](crates/gcode/src/index/import_resolution/context/scripting.rs#L11-L55), [crates/gcode/src/index/import_resolution/context/scripting.rs:57-66](crates/gcode/src/index/import_resolution/context/scripting.rs#L57-L66), [crates/gcode/src/index/import_resolution/context/scripting.rs:68-77](crates/gcode/src/index/import_resolution/context/scripting.rs#L68-L77), [crates/gcode/src/index/import_resolution/context/scripting.rs:79-84](crates/gcode/src/index/import_resolution/context/scripting.rs#L79-L84), [crates/gcode/src/index/import_resolution/context/scripting.rs:86-150](crates/gcode/src/index/import_resolution/context/scripting.rs#L86-L150), [crates/gcode/src/index/import_resolution/context/scripting.rs:152-218](crates/gcode/src/index/import_resolution/context/scripting.rs#L152-L218)

</details>

# crates/gcode/src/index/import_resolution/context/scripting.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]

## Purpose

This file builds import-resolution lookup tables for scripting languages. It collects Lua module paths from candidate `.lua` files, normalizes and deduplicates module names, and maps each module name to the files that provide it; it also includes separate builders for PHP symbol files and Ruby constant files, using shared helpers to recognize valid names and extract indexable entries.
[crates/gcode/src/index/import_resolution/context/scripting.rs:11-55]
[crates/gcode/src/index/import_resolution/context/scripting.rs:57-66]
[crates/gcode/src/index/import_resolution/context/scripting.rs:68-77]
[crates/gcode/src/index/import_resolution/context/scripting.rs:79-84]
[crates/gcode/src/index/import_resolution/context/scripting.rs:86-150]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `build_lua_module_files` | function | `pub(super) fn build_lua_module_files(` | `build_lua_module_files [function]` | `41161186-3cff-5f2e-b053-c11865fd81c4` | 11-55 [crates/gcode/src/index/import_resolution/context/scripting.rs:11-55] | Indexed function `build_lua_module_files` in `crates/gcode/src/index/import_resolution/context/scripting.rs`. [crates/gcode/src/index/import_resolution/context/scripting.rs:11-55] |
| `lua_module_names_for_path` | function | `fn lua_module_names_for_path(without_ext: &str) -> HashSet<String> {` | `lua_module_names_for_path [function]` | `775d37d7-d0a1-5090-afd2-4aef5a6074b9` | 57-66 [crates/gcode/src/index/import_resolution/context/scripting.rs:57-66] | Indexed function `lua_module_names_for_path` in `crates/gcode/src/index/import_resolution/context/scripting.rs`. [crates/gcode/src/index/import_resolution/context/scripting.rs:57-66] |
| `add_lua_module_names` | function | `fn add_lua_module_names(modules: &mut HashSet<String>, without_ext: &str) {` | `add_lua_module_names [function]` | `958c5635-6fb3-5e99-a793-0e6b908eda10` | 68-77 [crates/gcode/src/index/import_resolution/context/scripting.rs:68-77] | Indexed function `add_lua_module_names` in `crates/gcode/src/index/import_resolution/context/scripting.rs`. [crates/gcode/src/index/import_resolution/context/scripting.rs:68-77] |
| `insert_lua_module_name` | function | `fn insert_lua_module_name(modules: &mut HashSet<String>, module: &str) {` | `insert_lua_module_name [function]` | `25b068c4-4c5f-579d-be90-8361637cf23b` | 79-84 [crates/gcode/src/index/import_resolution/context/scripting.rs:79-84] | Indexed function `insert_lua_module_name` in `crates/gcode/src/index/import_resolution/context/scripting.rs`. [crates/gcode/src/index/import_resolution/context/scripting.rs:79-84] |
| `build_php_symbol_files` | function | `pub(in crate::index::import_resolution) fn build_php_symbol_files(` | `build_php_symbol_files [function]` | `6f9ca47e-d796-54c3-804c-8bd03c379ea7` | 86-150 [crates/gcode/src/index/import_resolution/context/scripting.rs:86-150] | Indexed function `build_php_symbol_files` in `crates/gcode/src/index/import_resolution/context/scripting.rs`. [crates/gcode/src/index/import_resolution/context/scripting.rs:86-150] |
| `build_ruby_constant_files` | function | `pub(super) fn build_ruby_constant_files(` | `build_ruby_constant_files [function]` | `af1a3f99-86c4-512e-aab2-5170d66212a2` | 152-218 [crates/gcode/src/index/import_resolution/context/scripting.rs:152-218] | Indexed function `build_ruby_constant_files` in `crates/gcode/src/index/import_resolution/context/scripting.rs`. [crates/gcode/src/index/import_resolution/context/scripting.rs:152-218] |
