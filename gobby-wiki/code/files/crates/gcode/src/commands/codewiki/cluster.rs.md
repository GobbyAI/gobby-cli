---
title: crates/gcode/src/commands/codewiki/cluster.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/cluster.rs
  ranges:
  - 8-43
  - 46-55
  - 57-61
  - 63-123
  - 125-149
  - 158-199
  - 201-225
  - 227-237
  - 239-247
  - 249-265
  - 267-275
  - 277-295
  - 297-302
  - 308-310
  - 313-329
  - 332-336
  - 339-350
  - 353-413
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/codewiki/cluster.rs:8-43](crates/gcode/src/commands/codewiki/cluster.rs#L8-L43), [crates/gcode/src/commands/codewiki/cluster.rs:46-55](crates/gcode/src/commands/codewiki/cluster.rs#L46-L55), [crates/gcode/src/commands/codewiki/cluster.rs:57-61](crates/gcode/src/commands/codewiki/cluster.rs#L57-L61), [crates/gcode/src/commands/codewiki/cluster.rs:63-123](crates/gcode/src/commands/codewiki/cluster.rs#L63-L123), [crates/gcode/src/commands/codewiki/cluster.rs:125-149](crates/gcode/src/commands/codewiki/cluster.rs#L125-L149), [crates/gcode/src/commands/codewiki/cluster.rs:158-199](crates/gcode/src/commands/codewiki/cluster.rs#L158-L199), [crates/gcode/src/commands/codewiki/cluster.rs:201-225](crates/gcode/src/commands/codewiki/cluster.rs#L201-L225), [crates/gcode/src/commands/codewiki/cluster.rs:227-237](crates/gcode/src/commands/codewiki/cluster.rs#L227-L237), [crates/gcode/src/commands/codewiki/cluster.rs:239-247](crates/gcode/src/commands/codewiki/cluster.rs#L239-L247), [crates/gcode/src/commands/codewiki/cluster.rs:249-265](crates/gcode/src/commands/codewiki/cluster.rs#L249-L265), [crates/gcode/src/commands/codewiki/cluster.rs:267-275](crates/gcode/src/commands/codewiki/cluster.rs#L267-L275), [crates/gcode/src/commands/codewiki/cluster.rs:277-295](crates/gcode/src/commands/codewiki/cluster.rs#L277-L295), [crates/gcode/src/commands/codewiki/cluster.rs:297-302](crates/gcode/src/commands/codewiki/cluster.rs#L297-L302), [crates/gcode/src/commands/codewiki/cluster.rs:308-310](crates/gcode/src/commands/codewiki/cluster.rs#L308-L310), [crates/gcode/src/commands/codewiki/cluster.rs:313-329](crates/gcode/src/commands/codewiki/cluster.rs#L313-L329), [crates/gcode/src/commands/codewiki/cluster.rs:332-336](crates/gcode/src/commands/codewiki/cluster.rs#L332-L336), [crates/gcode/src/commands/codewiki/cluster.rs:339-350](crates/gcode/src/commands/codewiki/cluster.rs#L339-L350), [crates/gcode/src/commands/codewiki/cluster.rs:353-413](crates/gcode/src/commands/codewiki/cluster.rs#L353-L413)

</details>

# crates/gcode/src/commands/codewiki/cluster.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

This file computes subsystem-level clusters for the codewiki view. It derives top-level roots from file paths, expands container directories one level when they only contain nested children, maps each file to the subsystem root that owns it, and then uses module/path/component helpers to cluster files and their symbols into shared groups. It also builds unions and common-module relationships from import targets and path components, and enforces that call-edge merging never crosses subsystem-root boundaries.
[crates/gcode/src/commands/codewiki/cluster.rs:8-43]
[crates/gcode/src/commands/codewiki/cluster.rs:46-55]
[crates/gcode/src/commands/codewiki/cluster.rs:57-61]
[crates/gcode/src/commands/codewiki/cluster.rs:63-123]
[crates/gcode/src/commands/codewiki/cluster.rs:125-149]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `subsystem_roots` | function | `pub(crate) fn subsystem_roots(files: &[String]) -> BTreeSet<String> {` | `subsystem_roots [function]` | `1162d4f9-5626-571f-89ec-a1251b313bd7` | 8-43 [crates/gcode/src/commands/codewiki/cluster.rs:8-43] | Indexed function `subsystem_roots` in `crates/gcode/src/commands/codewiki/cluster.rs`. [crates/gcode/src/commands/codewiki/cluster.rs:8-43] |
| `subsystem_root_for_file` | function | `pub(crate) fn subsystem_root_for_file<'a>(` | `subsystem_root_for_file [function]` | `cd08cbab-e272-5dfb-a306-6728aeacea18` | 46-55 [crates/gcode/src/commands/codewiki/cluster.rs:46-55] | Indexed function `subsystem_root_for_file` in `crates/gcode/src/commands/codewiki/cluster.rs`. [crates/gcode/src/commands/codewiki/cluster.rs:46-55] |
| `module_is_within` | function | `fn module_is_within(module: &str, root: &str) -> bool {` | `module_is_within [function]` | `b5d6567b-87b1-59a7-8894-5a2df2ce8d6f` | 57-61 [crates/gcode/src/commands/codewiki/cluster.rs:57-61] | Indexed function `module_is_within` in `crates/gcode/src/commands/codewiki/cluster.rs`. [crates/gcode/src/commands/codewiki/cluster.rs:57-61] |
| `cluster_file_modules` | function | `pub(crate) fn cluster_file_modules(` | `cluster_file_modules [function]` | `d05bc055-1ab7-54e0-880f-8ae763200521` | 63-123 [crates/gcode/src/commands/codewiki/cluster.rs:63-123] | Indexed function `cluster_file_modules` in `crates/gcode/src/commands/codewiki/cluster.rs`. [crates/gcode/src/commands/codewiki/cluster.rs:63-123] |
| `union_files` | function | `pub(crate) fn union_files(` | `union_files [function]` | `69836486-d6f1-5a42-9d07-abfd020e0cb2` | 125-149 [crates/gcode/src/commands/codewiki/cluster.rs:125-149] | Indexed function `union_files` in `crates/gcode/src/commands/codewiki/cluster.rs`. [crates/gcode/src/commands/codewiki/cluster.rs:125-149] |
| `find_file_root` | function | `pub(crate) fn find_file_root(parents: &mut HashMap<String, String>, file: &str) -> String {` | `find_file_root [function]` | `9e38315c-b59c-5c60-9533-218af1e5e89f` | 158-199 [crates/gcode/src/commands/codewiki/cluster.rs:158-199] | Indexed function `find_file_root` in `crates/gcode/src/commands/codewiki/cluster.rs`. [crates/gcode/src/commands/codewiki/cluster.rs:158-199] |
| `common_module_for_files` | function | `pub(crate) fn common_module_for_files(files: &[String]) -> String {` | `common_module_for_files [function]` | `921214d7-ccfc-5fad-9c90-f94f966ffb06` | 201-225 [crates/gcode/src/commands/codewiki/cluster.rs:201-225] | Indexed function `common_module_for_files` in `crates/gcode/src/commands/codewiki/cluster.rs`. [crates/gcode/src/commands/codewiki/cluster.rs:201-225] |
| `symbols_by_file_component` | function | `pub(crate) fn symbols_by_file_component(symbols: &[Symbol]) -> BTreeMap<String, Vec<String>> {` | `symbols_by_file_component [function]` | `15b839b6-5065-5891-af35-45ed8ba699c4` | 227-237 [crates/gcode/src/commands/codewiki/cluster.rs:227-237] | Indexed function `symbols_by_file_component` in `crates/gcode/src/commands/codewiki/cluster.rs`. [crates/gcode/src/commands/codewiki/cluster.rs:227-237] |
| `first_component_for_file` | function | `pub(crate) fn first_component_for_file(` | `first_component_for_file [function]` | `6926a399-46b2-5fc0-86de-ccd09751f171` | 239-247 [crates/gcode/src/commands/codewiki/cluster.rs:239-247] | Indexed function `first_component_for_file` in `crates/gcode/src/commands/codewiki/cluster.rs`. [crates/gcode/src/commands/codewiki/cluster.rs:239-247] |
| `files_for_import_target` | function | `pub(crate) fn files_for_import_target<'a>(` | `files_for_import_target [function]` | `b5b4658b-fe51-54b2-94ab-c763bbd85b77` | 249-265 [crates/gcode/src/commands/codewiki/cluster.rs:249-265] | Indexed function `files_for_import_target` in `crates/gcode/src/commands/codewiki/cluster.rs`. [crates/gcode/src/commands/codewiki/cluster.rs:249-265] |
| `module_components` | function | `fn module_components(value: &str) -> Vec<String> {` | `module_components [function]` | `07e3fb63-606b-5d7d-926b-0080b561c941` | 267-275 [crates/gcode/src/commands/codewiki/cluster.rs:267-275] | Indexed function `module_components` in `crates/gcode/src/commands/codewiki/cluster.rs`. [crates/gcode/src/commands/codewiki/cluster.rs:267-275] |
| `path_components` | function | `fn path_components(file: &str) -> Vec<String> {` | `path_components [function]` | `984bc8c7-5466-54dc-a75f-6d345529eb0d` | 277-295 [crates/gcode/src/commands/codewiki/cluster.rs:277-295] | Indexed function `path_components` in `crates/gcode/src/commands/codewiki/cluster.rs`. [crates/gcode/src/commands/codewiki/cluster.rs:277-295] |
| `contains_component_sequence` | function | `fn contains_component_sequence(components: &[String], target: &[String]) -> bool {` | `contains_component_sequence [function]` | `8ee1a096-f2bb-5fa2-8c7c-9d52c5a1b472` | 297-302 [crates/gcode/src/commands/codewiki/cluster.rs:297-302] | Indexed function `contains_component_sequence` in `crates/gcode/src/commands/codewiki/cluster.rs`. [crates/gcode/src/commands/codewiki/cluster.rs:297-302] |
| `paths` | function | `fn paths(values: &[&str]) -> Vec<String> {` | `paths [function]` | `b80a607d-786c-5c72-a0f6-b9bceb73d0e7` | 308-310 [crates/gcode/src/commands/codewiki/cluster.rs:308-310] | Indexed function `paths` in `crates/gcode/src/commands/codewiki/cluster.rs`. [crates/gcode/src/commands/codewiki/cluster.rs:308-310] |
| `subsystem_roots_expand_container_directories_one_level` | function | `fn subsystem_roots_expand_container_directories_one_level() {` | `subsystem_roots_expand_container_directories_one_level [function]` | `eba3f9fc-4edb-508b-9d88-599114e469ed` | 313-329 [crates/gcode/src/commands/codewiki/cluster.rs:313-329] | Indexed function `subsystem_roots_expand_container_directories_one_level` in `crates/gcode/src/commands/codewiki/cluster.rs`. [crates/gcode/src/commands/codewiki/cluster.rs:313-329] |
| `subsystem_roots_keep_top_level_directories_with_direct_files` | function | `fn subsystem_roots_keep_top_level_directories_with_direct_files() {` | `subsystem_roots_keep_top_level_directories_with_direct_files [function]` | `5e0da510-1ba6-5e2f-ab68-a592e2284a91` | 332-336 [crates/gcode/src/commands/codewiki/cluster.rs:332-336] | Indexed function `subsystem_roots_keep_top_level_directories_with_direct_files` in `crates/gcode/src/commands/codewiki/cluster.rs`. [crates/gcode/src/commands/codewiki/cluster.rs:332-336] |
| `subsystem_root_for_file_matches_whole_components_only` | function | `fn subsystem_root_for_file_matches_whole_components_only() {` | `subsystem_root_for_file_matches_whole_components_only [function]` | `8d84bd95-4e0d-5bb0-98f8-b22ff265a5b7` | 339-350 [crates/gcode/src/commands/codewiki/cluster.rs:339-350] | Indexed function `subsystem_root_for_file_matches_whole_components_only` in `crates/gcode/src/commands/codewiki/cluster.rs`. [crates/gcode/src/commands/codewiki/cluster.rs:339-350] |
| `call_edges_never_merge_clusters_across_subsystem_roots` | function | `fn call_edges_never_merge_clusters_across_subsystem_roots() {` | `call_edges_never_merge_clusters_across_subsystem_roots [function]` | `c7422994-ec4b-5acb-a19d-1bfb95d95df8` | 353-413 [crates/gcode/src/commands/codewiki/cluster.rs:353-413] | Indexed function `call_edges_never_merge_clusters_across_subsystem_roots` in `crates/gcode/src/commands/codewiki/cluster.rs`. [crates/gcode/src/commands/codewiki/cluster.rs:353-413] |
