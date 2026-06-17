---
title: crates/gcode/src/index/import_resolution/context/package_metadata.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/context/package_metadata.rs
  ranges:
  - 4-38
  - 40-49
  - 51-60
  - 66-97
  - 99-102
  - 104-130
  - 132-172
  - 174-185
  - 187-197
  - 199-201
  - 203-224
  - 226-234
  - 242-244
  - 247-249
  - 252-270
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/import_resolution/context/package_metadata.rs:4-38](crates/gcode/src/index/import_resolution/context/package_metadata.rs#L4-L38), [crates/gcode/src/index/import_resolution/context/package_metadata.rs:40-49](crates/gcode/src/index/import_resolution/context/package_metadata.rs#L40-L49), [crates/gcode/src/index/import_resolution/context/package_metadata.rs:51-60](crates/gcode/src/index/import_resolution/context/package_metadata.rs#L51-L60), [crates/gcode/src/index/import_resolution/context/package_metadata.rs:66-97](crates/gcode/src/index/import_resolution/context/package_metadata.rs#L66-L97), [crates/gcode/src/index/import_resolution/context/package_metadata.rs:99-102](crates/gcode/src/index/import_resolution/context/package_metadata.rs#L99-L102), [crates/gcode/src/index/import_resolution/context/package_metadata.rs:104-130](crates/gcode/src/index/import_resolution/context/package_metadata.rs#L104-L130), [crates/gcode/src/index/import_resolution/context/package_metadata.rs:132-172](crates/gcode/src/index/import_resolution/context/package_metadata.rs#L132-L172), [crates/gcode/src/index/import_resolution/context/package_metadata.rs:174-185](crates/gcode/src/index/import_resolution/context/package_metadata.rs#L174-L185), [crates/gcode/src/index/import_resolution/context/package_metadata.rs:187-197](crates/gcode/src/index/import_resolution/context/package_metadata.rs#L187-L197), [crates/gcode/src/index/import_resolution/context/package_metadata.rs:199-201](crates/gcode/src/index/import_resolution/context/package_metadata.rs#L199-L201), [crates/gcode/src/index/import_resolution/context/package_metadata.rs:203-224](crates/gcode/src/index/import_resolution/context/package_metadata.rs#L203-L224), [crates/gcode/src/index/import_resolution/context/package_metadata.rs:226-234](crates/gcode/src/index/import_resolution/context/package_metadata.rs#L226-L234), [crates/gcode/src/index/import_resolution/context/package_metadata.rs:242-244](crates/gcode/src/index/import_resolution/context/package_metadata.rs#L242-L244), [crates/gcode/src/index/import_resolution/context/package_metadata.rs:247-249](crates/gcode/src/index/import_resolution/context/package_metadata.rs#L247-L249), [crates/gcode/src/index/import_resolution/context/package_metadata.rs:252-270](crates/gcode/src/index/import_resolution/context/package_metadata.rs#L252-L270)

</details>

# crates/gcode/src/index/import_resolution/context/package_metadata.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution/context|crates/gcode/src/index/import_resolution/context]]

## Purpose

This file gathers package metadata needed by import resolution across multiple languages. It reads JavaScript `package.json` files to collect dependency package names and the current package name, parses Go `go.mod` to find the module path, indexes Go source files by project-relative package directory and normalizes candidate paths, scans Rust manifests to collect dependency crate keys and the local crate name, and reads Dart package metadata for external and self package names. The symlink helpers and canonicalization logic support resolving Go package files when paths are linked or duplicated on disk.
[crates/gcode/src/index/import_resolution/context/package_metadata.rs:4-38]
[crates/gcode/src/index/import_resolution/context/package_metadata.rs:40-49]
[crates/gcode/src/index/import_resolution/context/package_metadata.rs:51-60]
[crates/gcode/src/index/import_resolution/context/package_metadata.rs:66-97]
[crates/gcode/src/index/import_resolution/context/package_metadata.rs:99-102]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `load_js_external_packages` | function | `pub(in crate::index::import_resolution) fn load_js_external_packages(` | `load_js_external_packages [function]` | `deb828fc-6466-57a9-ab7a-de9d29f70c45` | 4-38 [crates/gcode/src/index/import_resolution/context/package_metadata.rs:4-38] | Indexed function `load_js_external_packages` in `crates/gcode/src/index/import_resolution/context/package_metadata.rs`. [crates/gcode/src/index/import_resolution/context/package_metadata.rs:4-38] |
| `load_js_self_package_name` | function | `pub(in crate::index::import_resolution) fn load_js_self_package_name(` | `load_js_self_package_name [function]` | `dde94bc4-0197-5ee0-a034-8ed64255201e` | 40-49 [crates/gcode/src/index/import_resolution/context/package_metadata.rs:40-49] | Indexed function `load_js_self_package_name` in `crates/gcode/src/index/import_resolution/context/package_metadata.rs`. [crates/gcode/src/index/import_resolution/context/package_metadata.rs:40-49] |
| `load_go_module_path` | function | `pub(in crate::index::import_resolution) fn load_go_module_path(root_path: &Path) -> Option<String> {` | `load_go_module_path [function]` | `f2a71e65-83d7-53b2-ba1d-c1a8520a21c2` | 51-60 [crates/gcode/src/index/import_resolution/context/package_metadata.rs:51-60] | Indexed function `load_go_module_path` in `crates/gcode/src/index/import_resolution/context/package_metadata.rs`. [crates/gcode/src/index/import_resolution/context/package_metadata.rs:51-60] |
| `build_go_package_files` | function | `pub(in crate::index::import_resolution) fn build_go_package_files(` | `build_go_package_files [function]` | `d5c3096d-b3d1-5c58-83f3-65040daf029a` | 66-97 [crates/gcode/src/index/import_resolution/context/package_metadata.rs:66-97] | Indexed function `build_go_package_files` in `crates/gcode/src/index/import_resolution/context/package_metadata.rs`. [crates/gcode/src/index/import_resolution/context/package_metadata.rs:66-97] |
| `canonical_relative_path` | function | `fn canonical_relative_path(path: &Path, root_abs: &Path) -> Option<PathBuf> {` | `canonical_relative_path [function]` | `ec1f9dec-00a5-5f94-921d-1b4e26c7155b` | 99-102 [crates/gcode/src/index/import_resolution/context/package_metadata.rs:99-102] | Indexed function `canonical_relative_path` in `crates/gcode/src/index/import_resolution/context/package_metadata.rs`. [crates/gcode/src/index/import_resolution/context/package_metadata.rs:99-102] |
| `load_rust_external_crates` | function | `pub(in crate::index::import_resolution) fn load_rust_external_crates(` | `load_rust_external_crates [function]` | `ff228364-cba4-5b08-8a0d-370db5c8904d` | 104-130 [crates/gcode/src/index/import_resolution/context/package_metadata.rs:104-130] | Indexed function `load_rust_external_crates` in `crates/gcode/src/index/import_resolution/context/package_metadata.rs`. [crates/gcode/src/index/import_resolution/context/package_metadata.rs:104-130] |
| `rust_manifest_paths` | function | `fn rust_manifest_paths(root_path: &Path) -> Vec<PathBuf> {` | `rust_manifest_paths [function]` | `d75960f0-a756-509c-be94-e5109ef257a0` | 132-172 [crates/gcode/src/index/import_resolution/context/package_metadata.rs:132-172] | Indexed function `rust_manifest_paths` in `crates/gcode/src/index/import_resolution/context/package_metadata.rs`. [crates/gcode/src/index/import_resolution/context/package_metadata.rs:132-172] |
| `load_rust_self_crate_name` | function | `pub(in crate::index::import_resolution) fn load_rust_self_crate_name(` | `load_rust_self_crate_name [function]` | `aace62ec-bb59-53e9-b666-5f2f18504b03` | 174-185 [crates/gcode/src/index/import_resolution/context/package_metadata.rs:174-185] | Indexed function `load_rust_self_crate_name` in `crates/gcode/src/index/import_resolution/context/package_metadata.rs`. [crates/gcode/src/index/import_resolution/context/package_metadata.rs:174-185] |
| `collect_rust_dependency_keys` | function | `fn collect_rust_dependency_keys(value: Option<&toml::Value>, crates: &mut HashSet<String>) {` | `collect_rust_dependency_keys [function]` | `5240d61a-50c5-5e8d-9179-0e1641165de7` | 187-197 [crates/gcode/src/index/import_resolution/context/package_metadata.rs:187-197] | Indexed function `collect_rust_dependency_keys` in `crates/gcode/src/index/import_resolution/context/package_metadata.rs`. [crates/gcode/src/index/import_resolution/context/package_metadata.rs:187-197] |
| `normalize_rust_crate_name` | function | `fn normalize_rust_crate_name(name: &str) -> String {` | `normalize_rust_crate_name [function]` | `a0c1b7b1-23f4-5c79-9edc-e21217c8323a` | 199-201 [crates/gcode/src/index/import_resolution/context/package_metadata.rs:199-201] | Indexed function `normalize_rust_crate_name` in `crates/gcode/src/index/import_resolution/context/package_metadata.rs`. [crates/gcode/src/index/import_resolution/context/package_metadata.rs:199-201] |
| `load_dart_external_packages` | function | `pub(in crate::index::import_resolution) fn load_dart_external_packages(` | `load_dart_external_packages [function]` | `e8681366-95aa-5281-bedd-e89d884cf927` | 203-224 [crates/gcode/src/index/import_resolution/context/package_metadata.rs:203-224] | Indexed function `load_dart_external_packages` in `crates/gcode/src/index/import_resolution/context/package_metadata.rs`. [crates/gcode/src/index/import_resolution/context/package_metadata.rs:203-224] |
| `load_dart_self_package_name` | function | `pub(in crate::index::import_resolution) fn load_dart_self_package_name(` | `load_dart_self_package_name [function]` | `ed7f8ca0-1eea-5efc-9460-51aa9db6d528` | 226-234 [crates/gcode/src/index/import_resolution/context/package_metadata.rs:226-234] | Indexed function `load_dart_self_package_name` in `crates/gcode/src/index/import_resolution/context/package_metadata.rs`. [crates/gcode/src/index/import_resolution/context/package_metadata.rs:226-234] |
| `symlink_dir` | function | `fn symlink_dir(target: &Path, link: &Path) -> std::io::Result<()> {` | `symlink_dir [function]` | `a10d47b3-c789-52d3-80d2-08ad0fadd78b` | 242-244 [crates/gcode/src/index/import_resolution/context/package_metadata.rs:242-244] | Indexed function `symlink_dir` in `crates/gcode/src/index/import_resolution/context/package_metadata.rs`. [crates/gcode/src/index/import_resolution/context/package_metadata.rs:242-244] |
| `symlink_dir` | function | `fn symlink_dir(target: &Path, link: &Path) -> std::io::Result<()> {` | `symlink_dir [function]` | `7c5c3bbd-e9ed-5d68-b929-0fd764e41806` | 247-249 [crates/gcode/src/index/import_resolution/context/package_metadata.rs:247-249] | Indexed function `symlink_dir` in `crates/gcode/src/index/import_resolution/context/package_metadata.rs`. [crates/gcode/src/index/import_resolution/context/package_metadata.rs:247-249] |
| `go_package_files_canonicalize_symlinked_candidates` | function | `fn go_package_files_canonicalize_symlinked_candidates() {` | `go_package_files_canonicalize_symlinked_candidates [function]` | `e49f4ccd-64e4-514f-addb-29f08bf3394e` | 252-270 [crates/gcode/src/index/import_resolution/context/package_metadata.rs:252-270] | Indexed function `go_package_files_canonicalize_symlinked_candidates` in `crates/gcode/src/index/import_resolution/context/package_metadata.rs`. [crates/gcode/src/index/import_resolution/context/package_metadata.rs:252-270] |
