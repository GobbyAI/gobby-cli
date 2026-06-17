---
title: crates/gcode/src/index/import_resolution/context/elixir.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/context/elixir.rs
  ranges:
  - 13-49
  - 55-111
  - 113-124
  - 126-149
  - 151-156
  - 158-164
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/import_resolution/context/elixir.rs:13-49](crates/gcode/src/index/import_resolution/context/elixir.rs#L13-L49), [crates/gcode/src/index/import_resolution/context/elixir.rs:55-111](crates/gcode/src/index/import_resolution/context/elixir.rs#L55-L111), [crates/gcode/src/index/import_resolution/context/elixir.rs:113-124](crates/gcode/src/index/import_resolution/context/elixir.rs#L113-L124), [crates/gcode/src/index/import_resolution/context/elixir.rs:126-149](crates/gcode/src/index/import_resolution/context/elixir.rs#L126-L149), [crates/gcode/src/index/import_resolution/context/elixir.rs:151-156](crates/gcode/src/index/import_resolution/context/elixir.rs#L151-L156), [crates/gcode/src/index/import_resolution/context/elixir.rs:158-164](crates/gcode/src/index/import_resolution/context/elixir.rs#L158-L164)

</details>

# crates/gcode/src/index/import_resolution/context/elixir.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]

## Purpose

This file builds Elixir import-resolution context by discovering where modules come from in a project. It scans candidate `.ex` and `.exs` files to collect local module roots, maps fully qualified local module names to the files that declare them by reading `defmodule` headers, and loads external dependency roots and dependency names from Elixir project metadata. The regex helpers support parsing Mix and lock-file dependency entries, so the module can combine local source layout and dependency manifests into the lookup data needed for Elixir import resolution.
[crates/gcode/src/index/import_resolution/context/elixir.rs:13-49]
[crates/gcode/src/index/import_resolution/context/elixir.rs:55-111]
[crates/gcode/src/index/import_resolution/context/elixir.rs:113-124]
[crates/gcode/src/index/import_resolution/context/elixir.rs:126-149]
[crates/gcode/src/index/import_resolution/context/elixir.rs:151-156]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `build_elixir_local_module_roots` | function | `pub(super) fn build_elixir_local_module_roots(candidate_files: &[PathBuf]) -> HashSet<String> {` | `build_elixir_local_module_roots [function]` | `61c04045-64eb-55fd-b514-6be884ddd064` | 13-49 [crates/gcode/src/index/import_resolution/context/elixir.rs:13-49] | Indexed function `build_elixir_local_module_roots` in `crates/gcode/src/index/import_resolution/context/elixir.rs`. [crates/gcode/src/index/import_resolution/context/elixir.rs:13-49] |
| `build_elixir_local_module_files` | function | `pub(in crate::index::import_resolution) fn build_elixir_local_module_files(` | `build_elixir_local_module_files [function]` | `6d08e35c-e587-5f1d-b126-c26bb743e044` | 55-111 [crates/gcode/src/index/import_resolution/context/elixir.rs:55-111] | Indexed function `build_elixir_local_module_files` in `crates/gcode/src/index/import_resolution/context/elixir.rs`. [crates/gcode/src/index/import_resolution/context/elixir.rs:55-111] |
| `load_elixir_external_roots` | function | `pub(super) fn load_elixir_external_roots(root_path: &Path) -> HashMap<String, String> {` | `load_elixir_external_roots [function]` | `c0fc8c71-608a-5551-b1ea-ad1d6a4e5f4a` | 113-124 [crates/gcode/src/index/import_resolution/context/elixir.rs:113-124] | Indexed function `load_elixir_external_roots` in `crates/gcode/src/index/import_resolution/context/elixir.rs`. [crates/gcode/src/index/import_resolution/context/elixir.rs:113-124] |
| `load_elixir_dependency_names` | function | `pub(in crate::index::import_resolution) fn load_elixir_dependency_names(` | `load_elixir_dependency_names [function]` | `19041f3d-26e2-586c-a912-b72644d66166` | 126-149 [crates/gcode/src/index/import_resolution/context/elixir.rs:126-149] | Indexed function `load_elixir_dependency_names` in `crates/gcode/src/index/import_resolution/context/elixir.rs`. [crates/gcode/src/index/import_resolution/context/elixir.rs:126-149] |
| `elixir_mix_dependency_regex` | function | `fn elixir_mix_dependency_regex() -> &'static Regex {` | `elixir_mix_dependency_regex [function]` | `a8c1fb81-cb97-5d50-a2af-70f1a7f28448` | 151-156 [crates/gcode/src/index/import_resolution/context/elixir.rs:151-156] | Indexed function `elixir_mix_dependency_regex` in `crates/gcode/src/index/import_resolution/context/elixir.rs`. [crates/gcode/src/index/import_resolution/context/elixir.rs:151-156] |
| `elixir_lock_dependency_regex` | function | `fn elixir_lock_dependency_regex() -> &'static Regex {` | `elixir_lock_dependency_regex [function]` | `62b5a06d-c636-5d8a-8987-682069923fde` | 158-164 [crates/gcode/src/index/import_resolution/context/elixir.rs:158-164] | Indexed function `elixir_lock_dependency_regex` in `crates/gcode/src/index/import_resolution/context/elixir.rs`. [crates/gcode/src/index/import_resolution/context/elixir.rs:158-164] |
