---
title: crates/gcode/src/index/import_resolution/context/python.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/context/python.rs
  ranges:
  - 4-15
  - 22-32
  - 34-63
  - 70-80
  - 83-90
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/import_resolution/context/python.rs:4-15](crates/gcode/src/index/import_resolution/context/python.rs#L4-L15), [crates/gcode/src/index/import_resolution/context/python.rs:22-32](crates/gcode/src/index/import_resolution/context/python.rs#L22-L32), [crates/gcode/src/index/import_resolution/context/python.rs:34-63](crates/gcode/src/index/import_resolution/context/python.rs#L34-L63), [crates/gcode/src/index/import_resolution/context/python.rs:70-80](crates/gcode/src/index/import_resolution/context/python.rs#L70-L80), [crates/gcode/src/index/import_resolution/context/python.rs:83-90](crates/gcode/src/index/import_resolution/context/python.rs#L83-L90)

</details>

# crates/gcode/src/index/import_resolution/context/python.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution/context|crates/gcode/src/index/import_resolution/context]]

## Purpose

This file builds a Python import index and the file-path candidates needed for resolution. `build_python_module_index` walks a set of candidate files, converts each Python source or stub path into one or more dotted module names, and collects them into a `HashSet`. `python_module_names_for_path` does the path-to-module conversion for `.py` and `.pyi` files under the project root, handling package `__init__` files and also emitting a de-`src.`-prefixed module name for `src/` layouts. `python_candidate_files` performs the inverse lookup for a dotted module name, generating possible `pkg/mod.py`, `pkg/mod/__init__.py`, stub variants, and `src/` equivalents without checking the filesystem, while the tests confirm it covers package and top-level module layouts.
[crates/gcode/src/index/import_resolution/context/python.rs:4-15]
[crates/gcode/src/index/import_resolution/context/python.rs:22-32]
[crates/gcode/src/index/import_resolution/context/python.rs:34-63]
[crates/gcode/src/index/import_resolution/context/python.rs:70-80]
[crates/gcode/src/index/import_resolution/context/python.rs:83-90]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `build_python_module_index` | function | `pub(in crate::index::import_resolution) fn build_python_module_index(` | `build_python_module_index [function]` | `92f05e19-4811-510b-8515-28f75f57f4ac` | 4-15 [crates/gcode/src/index/import_resolution/context/python.rs:4-15] | Indexed function `build_python_module_index` in `crates/gcode/src/index/import_resolution/context/python.rs`. [crates/gcode/src/index/import_resolution/context/python.rs:4-15] |
| `python_candidate_files` | function | `pub(in crate::index::import_resolution) fn python_candidate_files(module: &str) -> Vec<String> {` | `python_candidate_files [function]` | `77bbc96c-4ea8-5d15-bb0a-d8625140515a` | 22-32 [crates/gcode/src/index/import_resolution/context/python.rs:22-32] | Indexed function `python_candidate_files` in `crates/gcode/src/index/import_resolution/context/python.rs`. [crates/gcode/src/index/import_resolution/context/python.rs:22-32] |
| `python_module_names_for_path` | function | `fn python_module_names_for_path(root_path: &Path, path: &Path) -> Vec<String> {` | `python_module_names_for_path [function]` | `fe3e1957-1fa0-5923-84ec-651a898a7a4b` | 34-63 [crates/gcode/src/index/import_resolution/context/python.rs:34-63] | Indexed function `python_module_names_for_path` in `crates/gcode/src/index/import_resolution/context/python.rs`. [crates/gcode/src/index/import_resolution/context/python.rs:34-63] |
| `python_candidate_files_cover_module_package_and_src_layouts` | function | `fn python_candidate_files_cover_module_package_and_src_layouts() {` | `python_candidate_files_cover_module_package_and_src_layouts [function]` | `40cea3e4-1cfa-58fc-99a5-d77ebe78318a` | 70-80 [crates/gcode/src/index/import_resolution/context/python.rs:70-80] | Indexed function `python_candidate_files_cover_module_package_and_src_layouts` in `crates/gcode/src/index/import_resolution/context/python.rs`. [crates/gcode/src/index/import_resolution/context/python.rs:70-80] |
| `python_candidate_files_handle_top_level_module` | function | `fn python_candidate_files_handle_top_level_module() {` | `python_candidate_files_handle_top_level_module [function]` | `d8af4275-54a4-58ac-8836-66f58d38010b` | 83-90 [crates/gcode/src/index/import_resolution/context/python.rs:83-90] | Indexed function `python_candidate_files_handle_top_level_module` in `crates/gcode/src/index/import_resolution/context/python.rs`. [crates/gcode/src/index/import_resolution/context/python.rs:83-90] |
