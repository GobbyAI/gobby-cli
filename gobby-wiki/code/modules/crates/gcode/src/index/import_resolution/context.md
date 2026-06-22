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

## crates/gcode/src/index/import_resolution/context

This module is the pre-resolution context layer for the import-resolution subsystem. Before any import statement in a source file can be matched to a symbol, the indexer must know which packages are external to the project, what the project's own name or module path is, and how local files are laid out. Every file in this module answers one of those questions for a specific ecosystem. The results are collected into the binding and index types defined in `bindings.rs` and consumed downstream by the per-language resolution passes.

`bindings.rs` is the structural core of the module. It defines the runtime vocabulary that the rest of the resolution pipeline works with: `ExternalImportBinding` records a resolved external module and callee name; `LocalCallBinding` records candidate files and the originally imported name for a cross-file local reference, deferring UUID assignment to a post-write pass once `code_symbols` is fully populated (bindings.rs:21–30); `LocalCallResolution` distinguishes named from default-export imports (bindings.rs:14–18); and `ImportBindings` aggregates all of these into a single per-file state bag (bindings.rs:55–68). `ExtractedImports` and `ExternalCallTarget` complete the public API surface exposed to callers outside this module.

`package_metadata.rs` provides the ecosystem-specific manifest readers. `load_js_external_packages` reads all six standard `package.json` dependency fields (package_metadata.rs:14–22); `load_js_self_package_name` extracts the package's own `name` field; `load_go_module_path` parses the `module` directive from `go.mod`; and `build_go_package_files` maps every discovered Go source file to its package directory so that a `pkg.Fn()` selector call can be resolved against any file in that directory (package_metadata.rs:62–68). Parallel counterparts exist for Rust (`load_rust_external_crates`, `rust_manifest_paths`, `load_rust_self_crate_name`, `collect_rust_dependency_keys`, `normalize_rust_crate_name`), Dart (`load_dart_external_packages`, `load_dart_self_package_name`), and Python (`build_python_module_index`, `python_candidate_files`, `python_module_names_for_path`). All functions carry `pub(in crate::index::import_resolution)` visibility, making them available only to sibling resolution modules.

The language-specific files (`apple.rs`, `elixir.rs`, `jvm.rs`, `dotnet.rs`, `python.rs`, `scripting.rs`) each build in-memory lookup indexes by scanning candidate source files in parallel with Rayon. `apple.rs` produces `ObjcIndex` — three maps from header-path keys to the types and functions declared in each `.h`/`.m`/`.mm` file (apple.rs:7–12, 14–56). `elixir.rs` scans `defmodule` declarations because Elixir modules need not follow path-from-name conventions and a single file may declare several modules (elixir.rs:53–58). `python.rs` emits `build_python_module_index` and handles the three common Python layout styles (top-level module, `src/`, and package directory) via dedicated helpers. All indexes are purely additive structures built at context-construction time and passed as read-only references into the resolution passes.

### Public API symbols

| Symbol | Kind | File |
|---|---|---|
| `ExternalImportBinding` | struct | bindings.rs |
| `LocalCallBinding` | struct | bindings.rs |
| `LocalCallResolution` | enum | bindings.rs |
| `ImportBindings` | struct | bindings.rs |
| `ExternalRootBinding` | struct | bindings.rs |
| `ExtractedImports` | struct | bindings.rs |
| `ExternalCallTarget` | struct | bindings.rs |
| `LocalCallBinding::named` | method | bindings.rs |
| `LocalCallBinding::default_export` | method | bindings.rs |
| `LocalCallBinding::is_default_export` | method | bindings.rs |

### Package-metadata loaders (all `pub(in crate::index::import_resolution)`)

| Function | Ecosystem | Manifest read |
|---|---|---|
| `load_js_external_packages` | JavaScript/TypeScript | `package.json` |
| `load_js_self_package_name` | JavaScript/TypeScript | `package.json` |
| `load_go_module_path` | Go | `go.mod` |
| `build_go_package_files` | Go | filesystem walk |
| `load_rust_external_crates` | Rust | `Cargo.toml` |
| `rust_manifest_paths` | Rust | filesystem walk |
| `load_rust_self_crate_name` | Rust | `Cargo.toml` |
| `collect_rust_dependency_keys` | Rust | `Cargo.toml` |
| `normalize_rust_crate_name` | Rust | — (pure transform) |
| `load_dart_external_packages` | Dart | `pubspec.yaml` |
| `load_dart_self_package_name` | Dart | `pubspec.yaml` |
| `build_python_module_index` | Python | filesystem walk |
| `python_candidate_files` | Python | filesystem walk |
| `python_module_names_for_path` | Python | — (pure transform) |
| `canonical_relative_path` | all | — (pure transform) |
[crates/gcode/src/index/import_resolution/context/package_metadata.rs:4-38]
[crates/gcode/src/index/import_resolution/context/apple.rs:8-12]
[crates/gcode/src/index/import_resolution/context/bindings.rs:6-9]
[crates/gcode/src/index/import_resolution/context/dotnet.rs:10-17]
[crates/gcode/src/index/import_resolution/context/elixir.rs:13-49]

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

