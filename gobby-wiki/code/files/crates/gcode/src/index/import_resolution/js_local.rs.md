---
title: crates/gcode/src/index/import_resolution/js_local.rs
type: code_file
provenance:
- file: crates/gcode/src/index/import_resolution/js_local.rs
  ranges:
  - 7-24
  - 26-69
  - 71-84
  - 86-99
  - 101-115
  - 117-124
  - 126-134
  - 140-142
  - 145-150
  - 153-156
  - 159-162
  - 165-169
  - 172-174
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/import_resolution/js_local.rs:7-24](crates/gcode/src/index/import_resolution/js_local.rs#L7-L24), [crates/gcode/src/index/import_resolution/js_local.rs:26-69](crates/gcode/src/index/import_resolution/js_local.rs#L26-L69), [crates/gcode/src/index/import_resolution/js_local.rs:71-84](crates/gcode/src/index/import_resolution/js_local.rs#L71-L84), [crates/gcode/src/index/import_resolution/js_local.rs:86-99](crates/gcode/src/index/import_resolution/js_local.rs#L86-L99), [crates/gcode/src/index/import_resolution/js_local.rs:101-115](crates/gcode/src/index/import_resolution/js_local.rs#L101-L115), [crates/gcode/src/index/import_resolution/js_local.rs:117-124](crates/gcode/src/index/import_resolution/js_local.rs#L117-L124), [crates/gcode/src/index/import_resolution/js_local.rs:126-134](crates/gcode/src/index/import_resolution/js_local.rs#L126-L134), [crates/gcode/src/index/import_resolution/js_local.rs:140-142](crates/gcode/src/index/import_resolution/js_local.rs#L140-L142), [crates/gcode/src/index/import_resolution/js_local.rs:145-150](crates/gcode/src/index/import_resolution/js_local.rs#L145-L150), [crates/gcode/src/index/import_resolution/js_local.rs:153-156](crates/gcode/src/index/import_resolution/js_local.rs#L153-L156), [crates/gcode/src/index/import_resolution/js_local.rs:159-162](crates/gcode/src/index/import_resolution/js_local.rs#L159-L162), [crates/gcode/src/index/import_resolution/js_local.rs:165-169](crates/gcode/src/index/import_resolution/js_local.rs#L165-L169), [crates/gcode/src/index/import_resolution/js_local.rs:172-174](crates/gcode/src/index/import_resolution/js_local.rs#L172-L174)

</details>

# crates/gcode/src/index/import_resolution/js_local.rs

Module: [[code/modules/crates/gcode/src/index/import_resolution|crates/gcode/src/index/import_resolution]]

## Purpose

Builds candidate file paths for local JS/TS import resolution. `js_candidate_files` turns a specifier into possible project-relative module files by expanding each resolved module key into supported source extensions plus `index.*` variants, then deduplicating. The helper chain normalizes paths and keys, strips JS extensions, and maps specifiers from relative paths, root paths, `@/` or `~/` aliases, and self-package names; bare external specifiers return no candidates.
[crates/gcode/src/index/import_resolution/js_local.rs:7-24]
[crates/gcode/src/index/import_resolution/js_local.rs:26-69]
[crates/gcode/src/index/import_resolution/js_local.rs:71-84]
[crates/gcode/src/index/import_resolution/js_local.rs:86-99]
[crates/gcode/src/index/import_resolution/js_local.rs:101-115]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `js_candidate_files` | function | `pub(crate) fn js_candidate_files(` | `js_candidate_files [function]` | `60079bd7-7b38-5b0a-a56a-b4348a2355c2` | 7-24 [crates/gcode/src/index/import_resolution/js_local.rs:7-24] | Indexed function `js_candidate_files` in `crates/gcode/src/index/import_resolution/js_local.rs`. [crates/gcode/src/index/import_resolution/js_local.rs:7-24] |
| `js_import_target_keys` | function | `pub(crate) fn js_import_target_keys(` | `js_import_target_keys [function]` | `c0eeedc2-9a46-526b-9d13-d40a0a5845af` | 26-69 [crates/gcode/src/index/import_resolution/js_local.rs:26-69] | Indexed function `js_import_target_keys` in `crates/gcode/src/index/import_resolution/js_local.rs`. [crates/gcode/src/index/import_resolution/js_local.rs:26-69] |
| `module_key_variants` | function | `fn module_key_variants(key: &str) -> Vec<String> {` | `module_key_variants [function]` | `6ef332bb-0e5c-5959-a868-2e118e20b38b` | 71-84 [crates/gcode/src/index/import_resolution/js_local.rs:71-84] | Indexed function `module_key_variants` in `crates/gcode/src/index/import_resolution/js_local.rs`. [crates/gcode/src/index/import_resolution/js_local.rs:71-84] |
| `normalize_module_path` | function | `fn normalize_module_path(path: &Path) -> String {` | `normalize_module_path [function]` | `cb3cde90-05b4-5ad9-88ed-e4bfa73df05f` | 86-99 [crates/gcode/src/index/import_resolution/js_local.rs:86-99] | Indexed function `normalize_module_path` in `crates/gcode/src/index/import_resolution/js_local.rs`. [crates/gcode/src/index/import_resolution/js_local.rs:86-99] |
| `normalize_module_key` | function | `fn normalize_module_key(key: &str) -> String {` | `normalize_module_key [function]` | `5be11925-2e6d-59ea-ac80-16c94b3b828c` | 101-115 [crates/gcode/src/index/import_resolution/js_local.rs:101-115] | Indexed function `normalize_module_key` in `crates/gcode/src/index/import_resolution/js_local.rs`. [crates/gcode/src/index/import_resolution/js_local.rs:101-115] |
| `strip_js_extension` | function | `fn strip_js_extension(module: &str) -> String {` | `strip_js_extension [function]` | `764005fa-01d7-534c-91d6-b12b5d37a391` | 117-124 [crates/gcode/src/index/import_resolution/js_local.rs:117-124] | Indexed function `strip_js_extension` in `crates/gcode/src/index/import_resolution/js_local.rs`. [crates/gcode/src/index/import_resolution/js_local.rs:117-124] |
| `dedupe` | function | `fn dedupe(values: Vec<String>) -> Vec<String> {` | `dedupe [function]` | `5d8a1f04-9693-56fb-bee7-eaf84fee3b0b` | 126-134 [crates/gcode/src/index/import_resolution/js_local.rs:126-134] | Indexed function `dedupe` in `crates/gcode/src/index/import_resolution/js_local.rs`. [crates/gcode/src/index/import_resolution/js_local.rs:126-134] |
| `contains` | function | `fn contains(files: &[String], expected: &str) -> bool {` | `contains [function]` | `271da826-9aff-56a8-8efc-9aab42f2bf77` | 140-142 [crates/gcode/src/index/import_resolution/js_local.rs:140-142] | Indexed function `contains` in `crates/gcode/src/index/import_resolution/js_local.rs`. [crates/gcode/src/index/import_resolution/js_local.rs:140-142] |
| `relative_specifier_resolves_to_sibling_file_and_index` | function | `fn relative_specifier_resolves_to_sibling_file_and_index() {` | `relative_specifier_resolves_to_sibling_file_and_index [function]` | `c518a74d-bb5b-51dd-b1ba-9e98e27ea73a` | 145-150 [crates/gcode/src/index/import_resolution/js_local.rs:145-150] | Indexed function `relative_specifier_resolves_to_sibling_file_and_index` in `crates/gcode/src/index/import_resolution/js_local.rs`. [crates/gcode/src/index/import_resolution/js_local.rs:145-150] |
| `parent_specifier_walks_up_one_directory` | function | `fn parent_specifier_walks_up_one_directory() {` | `parent_specifier_walks_up_one_directory [function]` | `19cb83a7-2cd2-5cd4-bdbd-b7e46ecc9c33` | 153-156 [crates/gcode/src/index/import_resolution/js_local.rs:153-156] | Indexed function `parent_specifier_walks_up_one_directory` in `crates/gcode/src/index/import_resolution/js_local.rs`. [crates/gcode/src/index/import_resolution/js_local.rs:153-156] |
| `at_alias_maps_to_src_root` | function | `fn at_alias_maps_to_src_root() {` | `at_alias_maps_to_src_root [function]` | `d871d3f9-bc04-50ae-b6ac-c2a43c6c624b` | 159-162 [crates/gcode/src/index/import_resolution/js_local.rs:159-162] | Indexed function `at_alias_maps_to_src_root` in `crates/gcode/src/index/import_resolution/js_local.rs`. [crates/gcode/src/index/import_resolution/js_local.rs:159-162] |
| `self_package_specifier_resolves_with_and_without_src` | function | `fn self_package_specifier_resolves_with_and_without_src() {` | `self_package_specifier_resolves_with_and_without_src [function]` | `ddbb7b0e-55d0-578c-b3df-ec52da832183` | 165-169 [crates/gcode/src/index/import_resolution/js_local.rs:165-169] | Indexed function `self_package_specifier_resolves_with_and_without_src` in `crates/gcode/src/index/import_resolution/js_local.rs`. [crates/gcode/src/index/import_resolution/js_local.rs:165-169] |
| `bare_external_specifier_yields_no_candidates` | function | `fn bare_external_specifier_yields_no_candidates() {` | `bare_external_specifier_yields_no_candidates [function]` | `d89f6692-05fd-55c1-a106-ed0ac2e9831a` | 172-174 [crates/gcode/src/index/import_resolution/js_local.rs:172-174] | Indexed function `bare_external_specifier_yields_no_candidates` in `crates/gcode/src/index/import_resolution/js_local.rs`. [crates/gcode/src/index/import_resolution/js_local.rs:172-174] |
