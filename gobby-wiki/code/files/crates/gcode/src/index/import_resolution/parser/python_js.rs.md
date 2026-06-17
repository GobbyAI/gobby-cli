---
title: crates/gcode/src/index/import_resolution/parser/python_js.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/parser/python_js.rs
  ranges:
  - 14-123
  - 125-155
  - 157-252
  - 254-319
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/import_resolution/parser/python_js.rs:14-123](crates/gcode/src/index/import_resolution/parser/python_js.rs#L14-L123), [crates/gcode/src/index/import_resolution/parser/python_js.rs:125-155](crates/gcode/src/index/import_resolution/parser/python_js.rs#L125-L155), [crates/gcode/src/index/import_resolution/parser/python_js.rs:157-252](crates/gcode/src/index/import_resolution/parser/python_js.rs#L157-L252), [crates/gcode/src/index/import_resolution/parser/python_js.rs:254-319](crates/gcode/src/index/import_resolution/parser/python_js.rs#L254-L319)

</details>

# crates/gcode/src/index/import_resolution/parser/python_js.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]

## Purpose

This file parses import statements for both Python and JavaScript and records them as `ImportRelation`s plus any derived bindings in `ExtractedImports`. `parse_python_import_statement` handles Python `import ...` and `from ... import ...` forms, splitting multiple entries, filtering malformed cases, and using `python_local_module_lookup` to decide when a Python import should resolve to a local module versus an external one. `parse_js_import_statement` does the same for JavaScript imports, delegating clause-specific work to `parse_js_local_import_clause` to extract local bindings from named, default, and namespace-style import clauses. Together, these helpers normalize import syntax into the index’s import graph and binding map, while falling back to unparsed handling for statements that do not match the expected patterns.
[crates/gcode/src/index/import_resolution/parser/python_js.rs:14-123]
[crates/gcode/src/index/import_resolution/parser/python_js.rs:125-155]
[crates/gcode/src/index/import_resolution/parser/python_js.rs:157-252]
[crates/gcode/src/index/import_resolution/parser/python_js.rs:254-319]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `parse_python_import_statement` | function | `pub(crate) fn parse_python_import_statement(` | `parse_python_import_statement [function]` | `83e93bc0-a2e3-5842-a6c3-96a01264515d` | 14-123 [crates/gcode/src/index/import_resolution/parser/python_js.rs:14-123] | Indexed function `parse_python_import_statement` in `crates/gcode/src/index/import_resolution/parser/python_js.rs`. [crates/gcode/src/index/import_resolution/parser/python_js.rs:14-123] |
| `python_local_module_lookup` | function | `fn python_local_module_lookup(module: &str, rel_path: &str) -> Option<String> {` | `python_local_module_lookup [function]` | `6f46dc14-ac5c-594b-a514-9869a5835a6f` | 125-155 [crates/gcode/src/index/import_resolution/parser/python_js.rs:125-155] | Indexed function `python_local_module_lookup` in `crates/gcode/src/index/import_resolution/parser/python_js.rs`. [crates/gcode/src/index/import_resolution/parser/python_js.rs:125-155] |
| `parse_js_import_statement` | function | `pub(crate) fn parse_js_import_statement(` | `parse_js_import_statement [function]` | `4fb31e49-91a9-5bac-967a-1e535de427b6` | 157-252 [crates/gcode/src/index/import_resolution/parser/python_js.rs:157-252] | Indexed function `parse_js_import_statement` in `crates/gcode/src/index/import_resolution/parser/python_js.rs`. [crates/gcode/src/index/import_resolution/parser/python_js.rs:157-252] |
| `parse_js_local_import_clause` | function | `fn parse_js_local_import_clause(` | `parse_js_local_import_clause [function]` | `52ab03a3-ed8c-562a-b77e-bec3aa0aa4f8` | 254-319 [crates/gcode/src/index/import_resolution/parser/python_js.rs:254-319] | Indexed function `parse_js_local_import_clause` in `crates/gcode/src/index/import_resolution/parser/python_js.rs`. [crates/gcode/src/index/import_resolution/parser/python_js.rs:254-319] |
