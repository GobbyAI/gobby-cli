---
title: crates/gcode/src/index/import_resolution/context
type: code_module
provenance:
- file: crates/gcode/src/index/import_resolution/context/apple.rs
- file: crates/gcode/src/index/import_resolution/context/bindings.rs
- file: crates/gcode/src/index/import_resolution/context/dotnet.rs
- file: crates/gcode/src/index/import_resolution/context/elixir.rs
- file: crates/gcode/src/index/import_resolution/context/jvm.rs
- file: crates/gcode/src/index/import_resolution/context/package_metadata.rs
- file: crates/gcode/src/index/import_resolution/context/python.rs
- file: crates/gcode/src/index/import_resolution/context/scripting.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/import_resolution/context

Parent: [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]

## Overview

The `context` module supplies the language-specific lookup state used by import resolution. Its core binding types separate external imports from local cross-file candidates: `ExternalImportBinding` stores module/name pairs, while `LocalCallBinding` carries candidate target files plus either named or default-export resolution, deferring final symbol UUID matching to a later post-write pass .

A major flow is package and project metadata discovery. `package_metadata.rs` reads `package.json` dependency fields and self package names, parses `go.mod` module declarations, and builds Go package-directory indexes so selector calls like `pkg.Fn()` can resolve against any file in the imported package directory . Language scanners add richer local indexes: Objective-C indexes headers/implementations by import keys, declared types, and functions , while Elixir scans `defmodule` declarations because module names need not match paths and multiple modules may share a file .

The module collaborates with the wider import-resolution layer through restricted `pub(in crate::index::import_resolution)` APIs and `pub(super)` language helpers. It imports shared helpers and predicates for Elixir alias/dependency logic , uses `ImportRelation` from `crate::models` in the bindings layer , and relies on parallel scanning via `rayon` for filesystem-derived indexes in Apple and Elixir contexts  .

| Public API symbol | Role |
| --- | --- |
| `ExternalImportBinding` | External module/name binding |
| `LocalCallBinding` | Local import candidate binding |
| `ImportBindings` | Aggregated import-resolution maps |
| `load_js_external_packages` | Reads JS dependency package names |
| `load_js_self_package_name` | Reads package self name |
| `load_go_module_path` | Reads Go module path |
| `build_go_package_files` | Indexes Go files by package directory |
| `build_python_module_index` | Builds Python module lookup index |
| `build_elixir_local_module_files` | Maps Elixir modules to declaring files |
| `build_objc_indexes` | Builds Objective-C import/type/function indexes |
[crates/gcode/src/index/import_resolution/context/package_metadata.rs:4-38]
[crates/gcode/src/index/import_resolution/context/apple.rs:8-12]
[crates/gcode/src/index/import_resolution/context/bindings.rs:6-9]
[crates/gcode/src/index/import_resolution/context/elixir.rs:13-49]
[crates/gcode/src/index/import_resolution/context/python.rs:4-15]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/index/import_resolution/context/apple.rs\|crates/gcode/src/index/import_resolution/context/apple.rs]] | `crates/gcode/src/index/import_resolution/context/apple.rs` exposes 9 indexed API symbols. |
| [[code/files/crates/gcode/src/index/import_resolution/context/bindings.rs\|crates/gcode/src/index/import_resolution/context/bindings.rs]] | `crates/gcode/src/index/import_resolution/context/bindings.rs` exposes 10 indexed API symbols. |
| [[code/files/crates/gcode/src/index/import_resolution/context/dotnet.rs\|crates/gcode/src/index/import_resolution/context/dotnet.rs]] | `crates/gcode/src/index/import_resolution/context/dotnet.rs` exposes 2 indexed API symbols. |
| [[code/files/crates/gcode/src/index/import_resolution/context/elixir.rs\|crates/gcode/src/index/import_resolution/context/elixir.rs]] | `crates/gcode/src/index/import_resolution/context/elixir.rs` exposes 6 indexed API symbols. |
| [[code/files/crates/gcode/src/index/import_resolution/context/jvm.rs\|crates/gcode/src/index/import_resolution/context/jvm.rs]] | `crates/gcode/src/index/import_resolution/context/jvm.rs` exposes 4 indexed API symbols. |
| [[code/files/crates/gcode/src/index/import_resolution/context/package_metadata.rs\|crates/gcode/src/index/import_resolution/context/package_metadata.rs]] | `crates/gcode/src/index/import_resolution/context/package_metadata.rs` exposes 15 indexed API symbols. |
| [[code/files/crates/gcode/src/index/import_resolution/context/python.rs\|crates/gcode/src/index/import_resolution/context/python.rs]] | `crates/gcode/src/index/import_resolution/context/python.rs` exposes 5 indexed API symbols. |
| [[code/files/crates/gcode/src/index/import_resolution/context/scripting.rs\|crates/gcode/src/index/import_resolution/context/scripting.rs]] | `crates/gcode/src/index/import_resolution/context/scripting.rs` exposes 6 indexed API symbols. |

