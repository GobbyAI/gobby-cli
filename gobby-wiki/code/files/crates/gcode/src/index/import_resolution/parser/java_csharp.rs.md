---
title: crates/gcode/src/index/import_resolution/parser/java_csharp.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/parser/java_csharp.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/import_resolution/parser/java_csharp.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]

## Overview

`crates/gcode/src/index/import_resolution/parser/java_csharp.rs` exposes 4 indexed API symbols.

## How it fits

`crates/gcode/src/index/import_resolution/parser/java_csharp.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `parse_java_import_statement` | function | Normalizes a Java 'import' statement, records the imported target for 'rel_path', and, when possible, creates external or local bindings for statically imported members or class aliases, skipping wildcard imports. [crates/gcode/src/index/import_resolution/parser/java_csharp.rs:9-91] |
| `parse_csharp_import_statement` | function | Parses a C# 'using' import statement by normalizing it, recording the imported target, and populating either wildcard, member-alias, or local-type alias bindings depending on whether it is a 'using static', alias assignment, or namespace import. [crates/gcode/src/index/import_resolution/parser/java_csharp.rs:93-169] |
| `normalize_csharp_global_alias` | function | Returns the input path unchanged unless it starts with 'global::', in which case it strips that prefix and returns the remainder as a 'String'. [crates/gcode/src/index/import_resolution/parser/java_csharp.rs:171-173] |
| `csharp_global_qualifier_parts` | function | Returns 'Some((root_alias, qualifier_path))' only when 'root_alias == "global"' and 'qualifier_path' starts with '"global::"', using the first non-empty '.'-separated segment of the stripped path as 'root_alias'; otherwise it returns 'None'. [crates/gcode/src/index/import_resolution/parser/java_csharp.rs:175-188] |

