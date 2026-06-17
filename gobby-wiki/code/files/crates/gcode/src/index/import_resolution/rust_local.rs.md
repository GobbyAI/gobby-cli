---
title: crates/gcode/src/index/import_resolution/rust_local.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/rust_local.rs
  ranges:
  - 5-9
  - 12-15
  - 23-33
  - 35-55
  - 57-73
  - 75-93
  - 95-111
  - 113-123
  - 125-129
  - 131-136
  - 143-151
  - 154-159
  - 162-178
  - 181-194
  - 197-205
  - 208-216
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/import_resolution/rust_local.rs:5-9](crates/gcode/src/index/import_resolution/rust_local.rs#L5-L9), [crates/gcode/src/index/import_resolution/rust_local.rs:12-15](crates/gcode/src/index/import_resolution/rust_local.rs#L12-L15), [crates/gcode/src/index/import_resolution/rust_local.rs:23-33](crates/gcode/src/index/import_resolution/rust_local.rs#L23-L33), [crates/gcode/src/index/import_resolution/rust_local.rs:35-55](crates/gcode/src/index/import_resolution/rust_local.rs#L35-L55), [crates/gcode/src/index/import_resolution/rust_local.rs:57-73](crates/gcode/src/index/import_resolution/rust_local.rs#L57-L73), [crates/gcode/src/index/import_resolution/rust_local.rs:75-93](crates/gcode/src/index/import_resolution/rust_local.rs#L75-L93), [crates/gcode/src/index/import_resolution/rust_local.rs:95-111](crates/gcode/src/index/import_resolution/rust_local.rs#L95-L111), [crates/gcode/src/index/import_resolution/rust_local.rs:113-123](crates/gcode/src/index/import_resolution/rust_local.rs#L113-L123), [crates/gcode/src/index/import_resolution/rust_local.rs:125-129](crates/gcode/src/index/import_resolution/rust_local.rs#L125-L129), [crates/gcode/src/index/import_resolution/rust_local.rs:131-136](crates/gcode/src/index/import_resolution/rust_local.rs#L131-L136), [crates/gcode/src/index/import_resolution/rust_local.rs:143-151](crates/gcode/src/index/import_resolution/rust_local.rs#L143-L151), [crates/gcode/src/index/import_resolution/rust_local.rs:154-159](crates/gcode/src/index/import_resolution/rust_local.rs#L154-L159), [crates/gcode/src/index/import_resolution/rust_local.rs:162-178](crates/gcode/src/index/import_resolution/rust_local.rs#L162-L178), [crates/gcode/src/index/import_resolution/rust_local.rs:181-194](crates/gcode/src/index/import_resolution/rust_local.rs#L181-L194), [crates/gcode/src/index/import_resolution/rust_local.rs:197-205](crates/gcode/src/index/import_resolution/rust_local.rs#L197-L205), [crates/gcode/src/index/import_resolution/rust_local.rs:208-216](crates/gcode/src/index/import_resolution/rust_local.rs#L208-L216)

</details>

# crates/gcode/src/index/import_resolution/rust_local.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]

## Purpose

This file implements local Rust symbol resolution for imports and qualified calls. `RustLocalTarget` and `RustModuleContext` carry the crate source root, module path, and symbol name, while the helper functions translate between file paths and `::`-separated modules, generate candidate module files (`foo.rs` and `foo/mod.rs`, or `lib.rs`/`main.rs` at the crate root), and resolve paths relative to the current module, crate root, `self`/`super`, or bare non-external roots without resolving external crates.
[crates/gcode/src/index/import_resolution/rust_local.rs:5-9]
[crates/gcode/src/index/import_resolution/rust_local.rs:12-15]
[crates/gcode/src/index/import_resolution/rust_local.rs:23-33]
[crates/gcode/src/index/import_resolution/rust_local.rs:35-55]
[crates/gcode/src/index/import_resolution/rust_local.rs:57-73]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `RustLocalTarget` | class | `pub(crate) struct RustLocalTarget {` | `RustLocalTarget [class]` | `f2450d7f-ef5d-57b5-93ef-3fbf630497ab` | 5-9 [crates/gcode/src/index/import_resolution/rust_local.rs:5-9] | Indexed class `RustLocalTarget` in `crates/gcode/src/index/import_resolution/rust_local.rs`. [crates/gcode/src/index/import_resolution/rust_local.rs:5-9] |
| `RustModuleContext` | class | `struct RustModuleContext {` | `RustModuleContext [class]` | `89ae5f39-1411-5d4b-9a7d-e0a2c7bc9780` | 12-15 [crates/gcode/src/index/import_resolution/rust_local.rs:12-15] | Indexed class `RustModuleContext` in `crates/gcode/src/index/import_resolution/rust_local.rs`. [crates/gcode/src/index/import_resolution/rust_local.rs:12-15] |
| `rust_candidate_files` | function | `pub(crate) fn rust_candidate_files(source_root: &str, module: &str) -> Vec<String> {` | `rust_candidate_files [function]` | `faa8215e-a18d-529c-8d78-ff9c3856ceed` | 23-33 [crates/gcode/src/index/import_resolution/rust_local.rs:23-33] | Indexed function `rust_candidate_files` in `crates/gcode/src/index/import_resolution/rust_local.rs`. [crates/gcode/src/index/import_resolution/rust_local.rs:23-33] |
| `rust_import_target` | function | `pub(crate) fn rust_import_target(` | `rust_import_target [function]` | `9665856c-019c-5cba-a0cb-86fd748d8396` | 35-55 [crates/gcode/src/index/import_resolution/rust_local.rs:35-55] | Indexed function `rust_import_target` in `crates/gcode/src/index/import_resolution/rust_local.rs`. [crates/gcode/src/index/import_resolution/rust_local.rs:35-55] |
| `rust_qualified_call_target` | function | `pub(crate) fn rust_qualified_call_target(` | `rust_qualified_call_target [function]` | `5c56d04e-5a3c-5590-8803-e152cf8e0c08` | 57-73 [crates/gcode/src/index/import_resolution/rust_local.rs:57-73] | Indexed function `rust_qualified_call_target` in `crates/gcode/src/index/import_resolution/rust_local.rs`. [crates/gcode/src/index/import_resolution/rust_local.rs:57-73] |
| `rust_module_context_for_rel_path` | function | `fn rust_module_context_for_rel_path(rel_path: &str) -> Option<RustModuleContext> {` | `rust_module_context_for_rel_path [function]` | `cb2e5950-b6a0-58fa-82e9-8f1bdc517e99` | 75-93 [crates/gcode/src/index/import_resolution/rust_local.rs:75-93] | Indexed function `rust_module_context_for_rel_path` in `crates/gcode/src/index/import_resolution/rust_local.rs`. [crates/gcode/src/index/import_resolution/rust_local.rs:75-93] |
| `rust_module_for_segments` | function | `fn rust_module_for_segments(` | `rust_module_for_segments [function]` | `5f4115c5-47a0-5c25-ae20-9a157afacbfa` | 95-111 [crates/gcode/src/index/import_resolution/rust_local.rs:95-111] | Indexed function `rust_module_for_segments` in `crates/gcode/src/index/import_resolution/rust_local.rs`. [crates/gcode/src/index/import_resolution/rust_local.rs:95-111] |
| `rust_super_module` | function | `fn rust_super_module(current_module: &str, rest: &[&str]) -> String {` | `rust_super_module [function]` | `f238b9f3-4779-51a0-a33b-1dde3a51fc9d` | 113-123 [crates/gcode/src/index/import_resolution/rust_local.rs:113-123] | Indexed function `rust_super_module` in `crates/gcode/src/index/import_resolution/rust_local.rs`. [crates/gcode/src/index/import_resolution/rust_local.rs:113-123] |
| `join_rust_module` | function | `fn join_rust_module(base: &str, rest: &[&str]) -> String {` | `join_rust_module [function]` | `dc057fce-60b3-5e21-ad0a-9e08a1e74fa4` | 125-129 [crates/gcode/src/index/import_resolution/rust_local.rs:125-129] | Indexed function `join_rust_module` in `crates/gcode/src/index/import_resolution/rust_local.rs`. [crates/gcode/src/index/import_resolution/rust_local.rs:125-129] |
| `rust_path_segments` | function | `fn rust_path_segments(path: &str) -> Vec<&str> {` | `rust_path_segments [function]` | `0ddf9d24-4629-5a08-924d-d48719bcc58e` | 131-136 [crates/gcode/src/index/import_resolution/rust_local.rs:131-136] | Indexed function `rust_path_segments` in `crates/gcode/src/index/import_resolution/rust_local.rs`. [crates/gcode/src/index/import_resolution/rust_local.rs:131-136] |
| `candidate_files_cover_module_file_and_mod_rs` | function | `fn candidate_files_cover_module_file_and_mod_rs() {` | `candidate_files_cover_module_file_and_mod_rs [function]` | `a67be83f-be72-5f25-b90f-01ba45a7fd86` | 143-151 [crates/gcode/src/index/import_resolution/rust_local.rs:143-151] | Indexed function `candidate_files_cover_module_file_and_mod_rs` in `crates/gcode/src/index/import_resolution/rust_local.rs`. [crates/gcode/src/index/import_resolution/rust_local.rs:143-151] |
| `candidate_files_for_crate_root_are_lib_and_main` | function | `fn candidate_files_for_crate_root_are_lib_and_main() {` | `candidate_files_for_crate_root_are_lib_and_main [function]` | `75eb8032-2ded-5844-b50c-4c734f367b22` | 154-159 [crates/gcode/src/index/import_resolution/rust_local.rs:154-159] | Indexed function `candidate_files_for_crate_root_are_lib_and_main` in `crates/gcode/src/index/import_resolution/rust_local.rs`. [crates/gcode/src/index/import_resolution/rust_local.rs:154-159] |
| `import_target_resolves_crate_self_super_and_self_crate_roots` | function | `fn import_target_resolves_crate_self_super_and_self_crate_roots() {` | `import_target_resolves_crate_self_super_and_self_crate_roots [function]` | `d6a24d4e-6988-52d7-aab6-6cc17e073a8c` | 162-178 [crates/gcode/src/index/import_resolution/rust_local.rs:162-178] | Indexed function `import_target_resolves_crate_self_super_and_self_crate_roots` in `crates/gcode/src/index/import_resolution/rust_local.rs`. [crates/gcode/src/index/import_resolution/rust_local.rs:162-178] |
| `import_target_leaves_external_crate_paths_unresolved` | function | `fn import_target_leaves_external_crate_paths_unresolved() {` | `import_target_leaves_external_crate_paths_unresolved [function]` | `26c52108-43f9-5c5b-b8da-7549964e5e65` | 181-194 [crates/gcode/src/index/import_resolution/rust_local.rs:181-194] | Indexed function `import_target_leaves_external_crate_paths_unresolved` in `crates/gcode/src/index/import_resolution/rust_local.rs`. [crates/gcode/src/index/import_resolution/rust_local.rs:181-194] |
| `import_target_resolves_bare_non_external_root_relative_to_current_module` | function | `fn import_target_resolves_bare_non_external_root_relative_to_current_module() {` | `import_target_resolves_bare_non_external_root_relative_to_current_module [function]` | `449243fe-20ae-5caa-b8bc-c810558207e6` | 197-205 [crates/gcode/src/index/import_resolution/rust_local.rs:197-205] | Indexed function `import_target_resolves_bare_non_external_root_relative_to_current_module` in `crates/gcode/src/index/import_resolution/rust_local.rs`. [crates/gcode/src/index/import_resolution/rust_local.rs:197-205] |
| `qualified_call_resolves_bare_non_external_root_from_crate_root` | function | `fn qualified_call_resolves_bare_non_external_root_from_crate_root() {` | `qualified_call_resolves_bare_non_external_root_from_crate_root [function]` | `a78b1568-1084-5e1d-b7eb-5bcb2942fa3f` | 208-216 [crates/gcode/src/index/import_resolution/rust_local.rs:208-216] | Indexed function `qualified_call_resolves_bare_non_external_root_from_crate_root` in `crates/gcode/src/index/import_resolution/rust_local.rs`. [crates/gcode/src/index/import_resolution/rust_local.rs:208-216] |
