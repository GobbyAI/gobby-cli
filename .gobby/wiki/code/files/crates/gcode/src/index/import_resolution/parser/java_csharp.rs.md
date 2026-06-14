---
title: crates/gcode/src/index/import_resolution/parser/java_csharp.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/parser/java_csharp.rs
  ranges:
  - 8-60
  - 62-118
  - 120-122
  - 124-137
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/import_resolution/parser/java_csharp.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution/parser|crates/gcode/src/index/import_resolution/parser]]

## Purpose

Parses Java `import` statements and C# `using` directives into import relations plus binding metadata for the import-resolution index. The Java parser records each import, handles static versus regular imports, skips wildcards, and binds external class members or class aliases; the C# parser does the same for `using` forms, including static imports, aliases, and external namespace roots, with helpers to strip and validate the `global::` qualifier before binding.
[crates/gcode/src/index/import_resolution/parser/java_csharp.rs:8-60]
[crates/gcode/src/index/import_resolution/parser/java_csharp.rs:62-118]
[crates/gcode/src/index/import_resolution/parser/java_csharp.rs:120-122]
[crates/gcode/src/index/import_resolution/parser/java_csharp.rs:124-137]

## API Symbols

- `parse_java_import_statement` (function) component `parse_java_import_statement [function]` (`31904d91-9f4c-54e0-8a86-8056b5df3716`) lines 8-60 [crates/gcode/src/index/import_resolution/parser/java_csharp.rs:8-60]
  - Signature: `pub(crate) fn parse_java_import_statement(`
  - Purpose: Parses a Java import statement and extracts import relations and bindings for external classes, distinguishing between static imports and regular imports while handling wildcard syntax. [crates/gcode/src/index/import_resolution/parser/java_csharp.rs:8-60]
- `parse_csharp_import_statement` (function) component `parse_csharp_import_statement [function]` (`e5cc9588-90a6-5344-94bb-ac47901275cc`) lines 62-118 [crates/gcode/src/index/import_resolution/parser/java_csharp.rs:62-118]
  - Signature: `pub(crate) fn parse_csharp_import_statement(`
  - Purpose: Parses C# `using` statements to extract import relations and populate bindings for static imports, alias definitions, and external namespace roots based on the import resolution context. [crates/gcode/src/index/import_resolution/parser/java_csharp.rs:62-118]
- `normalize_csharp_global_alias` (function) component `normalize_csharp_global_alias [function]` (`b2225e6f-4ecd-5924-89de-8bfcb35cca75`) lines 120-122 [crates/gcode/src/index/import_resolution/parser/java_csharp.rs:120-122]
  - Signature: `fn normalize_csharp_global_alias(path: &str) -> String {`
  - Purpose: Removes the "global::" C# namespace alias prefix from a path string, returning the original string unchanged if the prefix is not present. [crates/gcode/src/index/import_resolution/parser/java_csharp.rs:120-122]
- `csharp_global_qualifier_parts` (function) component `csharp_global_qualifier_parts [function]` (`c0a263fb-60f4-5921-ac79-71d39e7bd81e`) lines 124-137 [crates/gcode/src/index/import_resolution/parser/java_csharp.rs:124-137]
  - Signature: `pub(crate) fn csharp_global_qualifier_parts<'a>(`
  - Purpose: # Summary

Parses a C# global-qualified identifier into the root namespace component and complete unprefixed path, validating that the root_alias is "global" and stripping the "global::" prefix from the qualifier_path. [crates/gcode/src/index/import_resolution/parser/java_csharp.rs:124-137]

