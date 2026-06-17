---
title: crates/gcode/src/index/import_resolution/context/apple.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/context/apple.rs
  ranges:
  - 8-12
  - 14-110
  - 112-123
  - 125-149
  - 151-169
  - 171-187
  - 189-196
  - 203-225
  - 232-274
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/import_resolution/context/apple.rs:8-12](crates/gcode/src/index/import_resolution/context/apple.rs#L8-L12), [crates/gcode/src/index/import_resolution/context/apple.rs:14-110](crates/gcode/src/index/import_resolution/context/apple.rs#L14-L110), [crates/gcode/src/index/import_resolution/context/apple.rs:112-123](crates/gcode/src/index/import_resolution/context/apple.rs#L112-L123), [crates/gcode/src/index/import_resolution/context/apple.rs:125-149](crates/gcode/src/index/import_resolution/context/apple.rs#L125-L149), [crates/gcode/src/index/import_resolution/context/apple.rs:151-169](crates/gcode/src/index/import_resolution/context/apple.rs#L151-L169), [crates/gcode/src/index/import_resolution/context/apple.rs:171-187](crates/gcode/src/index/import_resolution/context/apple.rs#L171-L187), [crates/gcode/src/index/import_resolution/context/apple.rs:189-196](crates/gcode/src/index/import_resolution/context/apple.rs#L189-L196), [crates/gcode/src/index/import_resolution/context/apple.rs:203-225](crates/gcode/src/index/import_resolution/context/apple.rs#L203-L225), [crates/gcode/src/index/import_resolution/context/apple.rs:232-274](crates/gcode/src/index/import_resolution/context/apple.rs#L232-L274)

</details>

# crates/gcode/src/index/import_resolution/context/apple.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]

## Purpose

Builds Apple-specific import-resolution indexes for Objective-C and Swift source trees. `ObjcIndex` stores lookup tables from file keys to declared Objective-C types and functions, and `build_objc_indexes` scans candidate `.h`, `.m`, and `.mm` files in parallel, derives several path-based keys for each file, parses the file contents for declarations, deduplicates the results, and populates the index maps. The helper functions recognize declared type and function names, normalize project-relative paths, resolve Objective-C relative imports, validate identifiers, and collect Swift module/file mappings so import resolution can match symbols to the right Apple source files.
[crates/gcode/src/index/import_resolution/context/apple.rs:8-12]
[crates/gcode/src/index/import_resolution/context/apple.rs:14-110]
[crates/gcode/src/index/import_resolution/context/apple.rs:112-123]
[crates/gcode/src/index/import_resolution/context/apple.rs:125-149]
[crates/gcode/src/index/import_resolution/context/apple.rs:151-169]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `ObjcIndex` | class | `pub(super) struct ObjcIndex {` | `ObjcIndex [class]` | `ae95d61d-ce92-581d-951e-a803c8af98e4` | 8-12 [crates/gcode/src/index/import_resolution/context/apple.rs:8-12] | Indexed class `ObjcIndex` in `crates/gcode/src/index/import_resolution/context/apple.rs`. [crates/gcode/src/index/import_resolution/context/apple.rs:8-12] |
| `build_objc_indexes` | function | `pub(super) fn build_objc_indexes(root_path: &Path, candidate_files: &[PathBuf]) -> ObjcIndex {` | `build_objc_indexes [function]` | `853db043-d547-536d-af16-ddd8f095e73a` | 14-110 [crates/gcode/src/index/import_resolution/context/apple.rs:14-110] | Indexed function `build_objc_indexes` in `crates/gcode/src/index/import_resolution/context/apple.rs`. [crates/gcode/src/index/import_resolution/context/apple.rs:14-110] |
| `objc_declared_type_name` | function | `fn objc_declared_type_name(line: &str) -> Option<String> {` | `objc_declared_type_name [function]` | `2354a7d7-4593-56e9-9c32-e1be39cf4a9c` | 112-123 [crates/gcode/src/index/import_resolution/context/apple.rs:112-123] | Indexed function `objc_declared_type_name` in `crates/gcode/src/index/import_resolution/context/apple.rs`. [crates/gcode/src/index/import_resolution/context/apple.rs:112-123] |
| `objc_declared_function_name` | function | `fn objc_declared_function_name(line: &str) -> Option<String> {` | `objc_declared_function_name [function]` | `b3f78005-5f4d-5ed3-9b77-b9c89bc23cfd` | 125-149 [crates/gcode/src/index/import_resolution/context/apple.rs:125-149] | Indexed function `objc_declared_function_name` in `crates/gcode/src/index/import_resolution/context/apple.rs`. [crates/gcode/src/index/import_resolution/context/apple.rs:125-149] |
| `objc_relative_import_file` | function | `pub(super) fn objc_relative_import_file(rel_path: &str, import_path: &str) -> Option<String> {` | `objc_relative_import_file [function]` | `10230e44-e0ec-594f-a015-2111758deef9` | 151-169 [crates/gcode/src/index/import_resolution/context/apple.rs:151-169] | Indexed function `objc_relative_import_file` in `crates/gcode/src/index/import_resolution/context/apple.rs`. [crates/gcode/src/index/import_resolution/context/apple.rs:151-169] |
| `normalize_objc_project_path` | function | `fn normalize_objc_project_path(path: &Path) -> Option<String> {` | `normalize_objc_project_path [function]` | `dcd60620-1662-59d6-a7d9-41704070b0a7` | 171-187 [crates/gcode/src/index/import_resolution/context/apple.rs:171-187] | Indexed function `normalize_objc_project_path` in `crates/gcode/src/index/import_resolution/context/apple.rs`. [crates/gcode/src/index/import_resolution/context/apple.rs:171-187] |
| `is_objc_identifier` | function | `fn is_objc_identifier(name: &str) -> bool {` | `is_objc_identifier [function]` | `3f387802-94a4-5fe2-8528-ffa5e084474e` | 189-196 [crates/gcode/src/index/import_resolution/context/apple.rs:189-196] | Indexed function `is_objc_identifier` in `crates/gcode/src/index/import_resolution/context/apple.rs`. [crates/gcode/src/index/import_resolution/context/apple.rs:189-196] |
| `swift_modules_for_rel` | function | `pub(super) fn swift_modules_for_rel(rel: &Path) -> HashSet<String> {` | `swift_modules_for_rel [function]` | `19cc2dda-196b-546a-89fb-454a0aa94e8d` | 203-225 [crates/gcode/src/index/import_resolution/context/apple.rs:203-225] | Indexed function `swift_modules_for_rel` in `crates/gcode/src/index/import_resolution/context/apple.rs`. [crates/gcode/src/index/import_resolution/context/apple.rs:203-225] |
| `build_swift_module_files` | function | `pub(in crate::index::import_resolution) fn build_swift_module_files(` | `build_swift_module_files [function]` | `0283c33f-3cc3-5ba4-8f2d-5e29ee90f85e` | 232-274 [crates/gcode/src/index/import_resolution/context/apple.rs:232-274] | Indexed function `build_swift_module_files` in `crates/gcode/src/index/import_resolution/context/apple.rs`. [crates/gcode/src/index/import_resolution/context/apple.rs:232-274] |
