---
title: crates/gcode/src/index/import_resolution/context/bindings.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/context/bindings.rs
  ranges:
  - 6-9
  - 12-15
  - 22-29
  - 32-38
  - 40-46
  - 48-50
  - 54-90
  - 93-96
  - 99-102
  - 105-108
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/import_resolution/context/bindings.rs:6-9](crates/gcode/src/index/import_resolution/context/bindings.rs#L6-L9), [crates/gcode/src/index/import_resolution/context/bindings.rs:12-15](crates/gcode/src/index/import_resolution/context/bindings.rs#L12-L15), [crates/gcode/src/index/import_resolution/context/bindings.rs:22-29](crates/gcode/src/index/import_resolution/context/bindings.rs#L22-L29), [crates/gcode/src/index/import_resolution/context/bindings.rs:32-38](crates/gcode/src/index/import_resolution/context/bindings.rs#L32-L38), [crates/gcode/src/index/import_resolution/context/bindings.rs:40-46](crates/gcode/src/index/import_resolution/context/bindings.rs#L40-L46), [crates/gcode/src/index/import_resolution/context/bindings.rs:48-50](crates/gcode/src/index/import_resolution/context/bindings.rs#L48-L50), [crates/gcode/src/index/import_resolution/context/bindings.rs:54-90](crates/gcode/src/index/import_resolution/context/bindings.rs#L54-L90), [crates/gcode/src/index/import_resolution/context/bindings.rs:93-96](crates/gcode/src/index/import_resolution/context/bindings.rs#L93-L96), [crates/gcode/src/index/import_resolution/context/bindings.rs:99-102](crates/gcode/src/index/import_resolution/context/bindings.rs#L99-L102), [crates/gcode/src/index/import_resolution/context/bindings.rs:105-108](crates/gcode/src/index/import_resolution/context/bindings.rs#L105-L108)

</details>

# crates/gcode/src/index/import_resolution/context/bindings.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution/context|crates/gcode/src/index/import_resolution/context]]

## Purpose

This file defines the data structures used by import-resolution indexing to represent how imported names map to call targets. It distinguishes external imports from local imports, tracks whether a local call came from a named import or a default export, and bundles these mappings in `ImportBindings` so later passes can resolve bare imports, namespace/member imports, external roots, extracted imports, and external call targets against indexed symbols.
[crates/gcode/src/index/import_resolution/context/bindings.rs:6-9]
[crates/gcode/src/index/import_resolution/context/bindings.rs:12-15]
[crates/gcode/src/index/import_resolution/context/bindings.rs:22-29]
[crates/gcode/src/index/import_resolution/context/bindings.rs:32-38]
[crates/gcode/src/index/import_resolution/context/bindings.rs:40-46]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `ExternalImportBinding` | class | `pub(crate) struct ExternalImportBinding {` | `ExternalImportBinding [class]` | `5c863f89-7912-5c2b-9877-68ea90ad360a` | 6-9 [crates/gcode/src/index/import_resolution/context/bindings.rs:6-9] | Indexed class `ExternalImportBinding` in `crates/gcode/src/index/import_resolution/context/bindings.rs`. [crates/gcode/src/index/import_resolution/context/bindings.rs:6-9] |
| `LocalCallResolution` | type | `pub(crate) enum LocalCallResolution {` | `LocalCallResolution [type]` | `476b71b5-8ff7-5003-bf63-56d386452e9e` | 12-15 [crates/gcode/src/index/import_resolution/context/bindings.rs:12-15] | Indexed type `LocalCallResolution` in `crates/gcode/src/index/import_resolution/context/bindings.rs`. [crates/gcode/src/index/import_resolution/context/bindings.rs:12-15] |
| `LocalCallBinding` | class | `pub(crate) struct LocalCallBinding {` | `LocalCallBinding [class]` | `ed6da5df-f2c9-52d5-a128-ea6fc7426497` | 22-29 [crates/gcode/src/index/import_resolution/context/bindings.rs:22-29] | Indexed class `LocalCallBinding` in `crates/gcode/src/index/import_resolution/context/bindings.rs`. [crates/gcode/src/index/import_resolution/context/bindings.rs:22-29] |
| `LocalCallBinding::named` | method | `pub(crate) fn named(candidate_files: Vec<String>, callee_name: String) -> Self {` | `LocalCallBinding::named [method]` | `cb6877cf-1fb9-5d32-82c8-b331a6801598` | 32-38 [crates/gcode/src/index/import_resolution/context/bindings.rs:32-38] | Indexed method `LocalCallBinding::named` in `crates/gcode/src/index/import_resolution/context/bindings.rs`. [crates/gcode/src/index/import_resolution/context/bindings.rs:32-38] |
| `LocalCallBinding::default_export` | method | `pub(crate) fn default_export(candidate_files: Vec<String>, local_alias: String) -> Self {` | `LocalCallBinding::default_export [method]` | `96894dd3-953b-5bf8-880e-42771591faf2` | 40-46 [crates/gcode/src/index/import_resolution/context/bindings.rs:40-46] | Indexed method `LocalCallBinding::default_export` in `crates/gcode/src/index/import_resolution/context/bindings.rs`. [crates/gcode/src/index/import_resolution/context/bindings.rs:40-46] |
| `LocalCallBinding::is_default_export` | method | `pub(crate) fn is_default_export(&self) -> bool {` | `LocalCallBinding::is_default_export [method]` | `08f40ebc-3f88-5c21-9620-89fe6b0a55e6` | 48-50 [crates/gcode/src/index/import_resolution/context/bindings.rs:48-50] | Indexed method `LocalCallBinding::is_default_export` in `crates/gcode/src/index/import_resolution/context/bindings.rs`. [crates/gcode/src/index/import_resolution/context/bindings.rs:48-50] |
| `ImportBindings` | class | `pub(crate) struct ImportBindings {` | `ImportBindings [class]` | `baa11c50-42e1-5933-9eb4-b7dd105a0949` | 54-90 [crates/gcode/src/index/import_resolution/context/bindings.rs:54-90] | Indexed class `ImportBindings` in `crates/gcode/src/index/import_resolution/context/bindings.rs`. [crates/gcode/src/index/import_resolution/context/bindings.rs:54-90] |
| `ExternalRootBinding` | class | `pub(crate) struct ExternalRootBinding {` | `ExternalRootBinding [class]` | `d8210213-126f-5dfb-8f3c-4176b22717bc` | 93-96 [crates/gcode/src/index/import_resolution/context/bindings.rs:93-96] | Indexed class `ExternalRootBinding` in `crates/gcode/src/index/import_resolution/context/bindings.rs`. [crates/gcode/src/index/import_resolution/context/bindings.rs:93-96] |
| `ExtractedImports` | class | `pub(crate) struct ExtractedImports {` | `ExtractedImports [class]` | `4891d8e1-65b2-5970-aac0-7676a2cf6ac3` | 99-102 [crates/gcode/src/index/import_resolution/context/bindings.rs:99-102] | Indexed class `ExtractedImports` in `crates/gcode/src/index/import_resolution/context/bindings.rs`. [crates/gcode/src/index/import_resolution/context/bindings.rs:99-102] |
| `ExternalCallTarget` | class | `pub(crate) struct ExternalCallTarget {` | `ExternalCallTarget [class]` | `18e1b21b-4a5c-5360-9dea-e06024071ea2` | 105-108 [crates/gcode/src/index/import_resolution/context/bindings.rs:105-108] | Indexed class `ExternalCallTarget` in `crates/gcode/src/index/import_resolution/context/bindings.rs`. [crates/gcode/src/index/import_resolution/context/bindings.rs:105-108] |
