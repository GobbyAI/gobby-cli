---
title: crates/gcode/src/index/import_resolution/parser/java_csharp.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/parser/java_csharp.rs
  ranges:
  - 9-91
  - 93-169
  - 171-173
  - 175-188
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/import_resolution/parser/java_csharp.rs:9-91](crates/gcode/src/index/import_resolution/parser/java_csharp.rs#L9-L91), [crates/gcode/src/index/import_resolution/parser/java_csharp.rs:93-169](crates/gcode/src/index/import_resolution/parser/java_csharp.rs#L93-L169), [crates/gcode/src/index/import_resolution/parser/java_csharp.rs:171-173](crates/gcode/src/index/import_resolution/parser/java_csharp.rs#L171-L173), [crates/gcode/src/index/import_resolution/parser/java_csharp.rs:175-188](crates/gcode/src/index/import_resolution/parser/java_csharp.rs#L175-L188)

</details>

# crates/gcode/src/index/import_resolution/parser/java_csharp.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]

## Purpose

Parses Java and C# import statements into the import-resolution index, recording each import relation and building the bindings used later to resolve bare calls, member access, and namespace aliases. The Java parser handles static imports, wildcard imports, external-class detection, and local class/file candidates; the C# parser does the same for `using` directives, including global alias normalization and splitting qualified names so external and local imports are bound consistently.
[crates/gcode/src/index/import_resolution/parser/java_csharp.rs:9-91]
[crates/gcode/src/index/import_resolution/parser/java_csharp.rs:93-169]
[crates/gcode/src/index/import_resolution/parser/java_csharp.rs:171-173]
[crates/gcode/src/index/import_resolution/parser/java_csharp.rs:175-188]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `parse_java_import_statement` | function | `pub(crate) fn parse_java_import_statement(` | `parse_java_import_statement [function]` | `d77e8007-6ca0-51db-9118-2850c570d7e6` | 9-91 [crates/gcode/src/index/import_resolution/parser/java_csharp.rs:9-91] | Indexed function `parse_java_import_statement` in `crates/gcode/src/index/import_resolution/parser/java_csharp.rs`. [crates/gcode/src/index/import_resolution/parser/java_csharp.rs:9-91] |
| `parse_csharp_import_statement` | function | `pub(crate) fn parse_csharp_import_statement(` | `parse_csharp_import_statement [function]` | `69b9be96-05ec-5a63-924a-b6d650a9e909` | 93-169 [crates/gcode/src/index/import_resolution/parser/java_csharp.rs:93-169] | Indexed function `parse_csharp_import_statement` in `crates/gcode/src/index/import_resolution/parser/java_csharp.rs`. [crates/gcode/src/index/import_resolution/parser/java_csharp.rs:93-169] |
| `normalize_csharp_global_alias` | function | `fn normalize_csharp_global_alias(path: &str) -> String {` | `normalize_csharp_global_alias [function]` | `0887984d-837e-5b06-ad36-0a8ec474f36a` | 171-173 [crates/gcode/src/index/import_resolution/parser/java_csharp.rs:171-173] | Indexed function `normalize_csharp_global_alias` in `crates/gcode/src/index/import_resolution/parser/java_csharp.rs`. [crates/gcode/src/index/import_resolution/parser/java_csharp.rs:171-173] |
| `csharp_global_qualifier_parts` | function | `pub(crate) fn csharp_global_qualifier_parts<'a>(` | `csharp_global_qualifier_parts [function]` | `18f18117-8092-562d-867d-6d56874eb1a8` | 175-188 [crates/gcode/src/index/import_resolution/parser/java_csharp.rs:175-188] | Indexed function `csharp_global_qualifier_parts` in `crates/gcode/src/index/import_resolution/parser/java_csharp.rs`. [crates/gcode/src/index/import_resolution/parser/java_csharp.rs:175-188] |
