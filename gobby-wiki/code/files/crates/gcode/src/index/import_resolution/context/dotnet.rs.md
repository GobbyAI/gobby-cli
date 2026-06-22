---
title: crates/gcode/src/index/import_resolution/context/dotnet.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/context/dotnet.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/import_resolution/context/dotnet.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]

## Overview

`crates/gcode/src/index/import_resolution/context/dotnet.rs` exposes 2 indexed API symbols.

## How it fits

`crates/gcode/src/index/import_resolution/context/dotnet.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `CsharpIndex` | class | 'CsharpIndex' is a C# symbol index that tracks locally declared namespace roots and type names for externality classification, and maps fully qualified type names to their project-relative source files for resolving member calls. [crates/gcode/src/index/import_resolution/context/dotnet.rs:10-17] |
| `build_csharp_index` | function | Builds a C# index by parallel-scanning '.cs' candidate files, extracting namespace/type information keyed by fully qualified names, and collecting root namespace segments into a 'CsharpIndex'. [crates/gcode/src/index/import_resolution/context/dotnet.rs:19-88] |

