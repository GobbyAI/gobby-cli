---
title: crates/gcode/src/index/import_resolution/context/dotnet.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/context/dotnet.rs
  ranges:
  - 10-17
  - 19-88
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/import_resolution/context/dotnet.rs:10-17](crates/gcode/src/index/import_resolution/context/dotnet.rs#L10-L17), [crates/gcode/src/index/import_resolution/context/dotnet.rs:19-88](crates/gcode/src/index/import_resolution/context/dotnet.rs#L19-L88)

</details>

# crates/gcode/src/index/import_resolution/context/dotnet.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]

## Purpose

Builds a lightweight C# import-resolution index for a set of candidate files. `CsharpIndex` stores two lookup tables: `local_roots` for namespace/type-name roots seen in local source, and `type_files` for mapping fully qualified type names to the project-relative files that declare them. `build_csharp_index` scans `.cs` files in parallel, skips unreadable or non-C# paths, normalizes each file’s relative path, tracks the current `namespace` while reading lines, and uses declared-type detection plus namespace context to populate the index for later local-vs-external `using` classification and member-to-file resolution.
[crates/gcode/src/index/import_resolution/context/dotnet.rs:10-17]
[crates/gcode/src/index/import_resolution/context/dotnet.rs:19-88]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `CsharpIndex` | class | `pub(super) struct CsharpIndex {` | `CsharpIndex [class]` | `954fb125-2e43-5b1c-9c94-6b86053e2277` | 10-17 [crates/gcode/src/index/import_resolution/context/dotnet.rs:10-17] | Indexed class `CsharpIndex` in `crates/gcode/src/index/import_resolution/context/dotnet.rs`. [crates/gcode/src/index/import_resolution/context/dotnet.rs:10-17] |
| `build_csharp_index` | function | `pub(super) fn build_csharp_index(root_path: &Path, candidate_files: &[PathBuf]) -> CsharpIndex {` | `build_csharp_index [function]` | `cfdbfd1d-51c6-5a97-9f0e-5bcc0367144f` | 19-88 [crates/gcode/src/index/import_resolution/context/dotnet.rs:19-88] | Indexed function `build_csharp_index` in `crates/gcode/src/index/import_resolution/context/dotnet.rs`. [crates/gcode/src/index/import_resolution/context/dotnet.rs:19-88] |
