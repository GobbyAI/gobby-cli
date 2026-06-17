---
title: crates/gcode/src/index/import_resolution/parser/objc.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/parser/objc.rs
  ranges:
  - 8-69
  - 71-85
  - 87-95
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/import_resolution/parser/objc.rs:8-69](crates/gcode/src/index/import_resolution/parser/objc.rs#L8-L69), [crates/gcode/src/index/import_resolution/parser/objc.rs:71-85](crates/gcode/src/index/import_resolution/parser/objc.rs#L71-L85), [crates/gcode/src/index/import_resolution/parser/objc.rs:87-95](crates/gcode/src/index/import_resolution/parser/objc.rs#L87-L95)

</details>

# crates/gcode/src/index/import_resolution/parser/objc.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]

## Purpose

This file parses Objective-C `#import` and `#include` statements for import resolution. `parse_objc_import_statement` identifies import lines, extracts the import path and whether it is a system import, records the import relation, and for non-system imports asks the import context for candidate files so it can populate Objective-C import-file bindings plus function and type lookup bindings, then deduplicates them. `resolve_objc_local_callee` uses those bindings together with the current symbol set to decide whether a bare call should be resolved to an imported local Objective-C declaration. `objc_import_path` is the small parser that extracts the path and import kind from the directive text.
[crates/gcode/src/index/import_resolution/parser/objc.rs:8-69]
[crates/gcode/src/index/import_resolution/parser/objc.rs:71-85]
[crates/gcode/src/index/import_resolution/parser/objc.rs:87-95]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `parse_objc_import_statement` | function | `pub(crate) fn parse_objc_import_statement(` | `parse_objc_import_statement [function]` | `14dccfb5-4820-5c32-9ea6-8059e9fe8b97` | 8-69 [crates/gcode/src/index/import_resolution/parser/objc.rs:8-69] | Indexed function `parse_objc_import_statement` in `crates/gcode/src/index/import_resolution/parser/objc.rs`. [crates/gcode/src/index/import_resolution/parser/objc.rs:8-69] |
| `resolve_objc_local_callee` | function | `pub(crate) fn resolve_objc_local_callee(` | `resolve_objc_local_callee [function]` | `457f1187-702e-5f4e-8474-9b55fd09533a` | 71-85 [crates/gcode/src/index/import_resolution/parser/objc.rs:71-85] | Indexed function `resolve_objc_local_callee` in `crates/gcode/src/index/import_resolution/parser/objc.rs`. [crates/gcode/src/index/import_resolution/parser/objc.rs:71-85] |
| `objc_import_path` | function | `fn objc_import_path(text: &str) -> Option<(String, bool)> {` | `objc_import_path [function]` | `a42e632d-2288-5577-b4a9-99897008b77b` | 87-95 [crates/gcode/src/index/import_resolution/parser/objc.rs:87-95] | Indexed function `objc_import_path` in `crates/gcode/src/index/import_resolution/parser/objc.rs`. [crates/gcode/src/index/import_resolution/parser/objc.rs:87-95] |
