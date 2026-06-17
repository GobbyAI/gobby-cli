---
title: crates/gcode/src/graph/code_graph/read/relationships.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/code_graph/read/relationships.rs
  ranges:
  - 24-27
  - 29-35
  - 37-48
  - 50-60
  - 62-72
  - 74-85
  - 87-98
  - 100-113
  - 115-124
  - 126-139
  - 141-157
  - 159-172
  - 174-190
  - 192-198
  - 200-225
  - 227-245
  - 247-263
  - 265-302
  - 304-342
  - 344-355
  - 361-366
  - 369-375
  - 378-386
  - 389-397
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/graph/code_graph/read/relationships.rs:24-27](crates/gcode/src/graph/code_graph/read/relationships.rs#L24-L27), [crates/gcode/src/graph/code_graph/read/relationships.rs:29-35](crates/gcode/src/graph/code_graph/read/relationships.rs#L29-L35), [crates/gcode/src/graph/code_graph/read/relationships.rs:37-48](crates/gcode/src/graph/code_graph/read/relationships.rs#L37-L48), [crates/gcode/src/graph/code_graph/read/relationships.rs:50-60](crates/gcode/src/graph/code_graph/read/relationships.rs#L50-L60), [crates/gcode/src/graph/code_graph/read/relationships.rs:62-72](crates/gcode/src/graph/code_graph/read/relationships.rs#L62-L72), [crates/gcode/src/graph/code_graph/read/relationships.rs:74-85](crates/gcode/src/graph/code_graph/read/relationships.rs#L74-L85), [crates/gcode/src/graph/code_graph/read/relationships.rs:87-98](crates/gcode/src/graph/code_graph/read/relationships.rs#L87-L98), [crates/gcode/src/graph/code_graph/read/relationships.rs:100-113](crates/gcode/src/graph/code_graph/read/relationships.rs#L100-L113), [crates/gcode/src/graph/code_graph/read/relationships.rs:115-124](crates/gcode/src/graph/code_graph/read/relationships.rs#L115-L124), [crates/gcode/src/graph/code_graph/read/relationships.rs:126-139](crates/gcode/src/graph/code_graph/read/relationships.rs#L126-L139), [crates/gcode/src/graph/code_graph/read/relationships.rs:141-157](crates/gcode/src/graph/code_graph/read/relationships.rs#L141-L157), [crates/gcode/src/graph/code_graph/read/relationships.rs:159-172](crates/gcode/src/graph/code_graph/read/relationships.rs#L159-L172), [crates/gcode/src/graph/code_graph/read/relationships.rs:174-190](crates/gcode/src/graph/code_graph/read/relationships.rs#L174-L190), [crates/gcode/src/graph/code_graph/read/relationships.rs:192-198](crates/gcode/src/graph/code_graph/read/relationships.rs#L192-L198), [crates/gcode/src/graph/code_graph/read/relationships.rs:200-225](crates/gcode/src/graph/code_graph/read/relationships.rs#L200-L225), [crates/gcode/src/graph/code_graph/read/relationships.rs:227-245](crates/gcode/src/graph/code_graph/read/relationships.rs#L227-L245), [crates/gcode/src/graph/code_graph/read/relationships.rs:247-263](crates/gcode/src/graph/code_graph/read/relationships.rs#L247-L263), [crates/gcode/src/graph/code_graph/read/relationships.rs:265-302](crates/gcode/src/graph/code_graph/read/relationships.rs#L265-L302), [crates/gcode/src/graph/code_graph/read/relationships.rs:304-342](crates/gcode/src/graph/code_graph/read/relationships.rs#L304-L342), [crates/gcode/src/graph/code_graph/read/relationships.rs:344-355](crates/gcode/src/graph/code_graph/read/relationships.rs#L344-L355), [crates/gcode/src/graph/code_graph/read/relationships.rs:361-366](crates/gcode/src/graph/code_graph/read/relationships.rs#L361-L366), [crates/gcode/src/graph/code_graph/read/relationships.rs:369-375](crates/gcode/src/graph/code_graph/read/relationships.rs#L369-L375), [crates/gcode/src/graph/code_graph/read/relationships.rs:378-386](crates/gcode/src/graph/code_graph/read/relationships.rs#L378-L386), [crates/gcode/src/graph/code_graph/read/relationships.rs:389-397](crates/gcode/src/graph/code_graph/read/relationships.rs#L389-L397)

</details>

# crates/gcode/src/graph/code_graph/read/relationships.rs

Module: [[code/modules/crates/gcode/src/graph/code_graph/read|crates/gcode/src/graph/code_graph/read]]

## Purpose

This file provides the read-side relationship queries for the code graph: it wraps typed graph queries to count and fetch callers/usages, fetch batch caller/callee data, read imports, resolve external call targets, and compute symbol paths and blast radius. The helpers support that workflow by formatting external call target names, choosing a single match or surfacing ambiguous candidates, and reconstructing path steps from graph results into `GraphResult`/`GraphPathStep` data.
[crates/gcode/src/graph/code_graph/read/relationships.rs:24-27]
[crates/gcode/src/graph/code_graph/read/relationships.rs:29-35]
[crates/gcode/src/graph/code_graph/read/relationships.rs:37-48]
[crates/gcode/src/graph/code_graph/read/relationships.rs:50-60]
[crates/gcode/src/graph/code_graph/read/relationships.rs:62-72]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `ResolvedExternalCallTarget` | class | `pub struct ResolvedExternalCallTarget {` | `ResolvedExternalCallTarget [class]` | `d5bff63a-6670-5001-9744-4ef4089b2f4b` | 24-27 [crates/gcode/src/graph/code_graph/read/relationships.rs:24-27] | Indexed class `ResolvedExternalCallTarget` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:24-27] |
| `external_call_target_display_name` | function | `fn external_call_target_display_name(name: &str, module: &str) -> String {` | `external_call_target_display_name [function]` | `be3f6ee0-e032-5698-b7e6-9c2883cbdbc9` | 29-35 [crates/gcode/src/graph/code_graph/read/relationships.rs:29-35] | Indexed function `external_call_target_display_name` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:29-35] |
| `select_external_call_target` | function | `fn select_external_call_target(` | `select_external_call_target [function]` | `5e974821-feb1-5476-b7c4-c9c004b36c15` | 37-48 [crates/gcode/src/graph/code_graph/read/relationships.rs:37-48] | Indexed function `select_external_call_target` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:37-48] |
| `count_callers` | function | `pub fn count_callers(ctx: &Context, symbol_id: &str) -> anyhow::Result<usize> {` | `count_callers [function]` | `3f888db5-854b-54e6-9367-46cc05941870` | 50-60 [crates/gcode/src/graph/code_graph/read/relationships.rs:50-60] | Indexed function `count_callers` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:50-60] |
| `count_usages` | function | `pub fn count_usages(ctx: &Context, symbol_id: &str) -> anyhow::Result<usize> {` | `count_usages [function]` | `cc5510f4-2999-5c9a-a977-58623e09acdd` | 62-72 [crates/gcode/src/graph/code_graph/read/relationships.rs:62-72] | Indexed function `count_usages` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:62-72] |
| `find_callers` | function | `pub fn find_callers(` | `find_callers [function]` | `0e09dfc9-bf94-5bef-ba43-a8bcbe253ab7` | 74-85 [crates/gcode/src/graph/code_graph/read/relationships.rs:74-85] | Indexed function `find_callers` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:74-85] |
| `find_usages` | function | `pub fn find_usages(` | `find_usages [function]` | `fb4ad421-3dbe-51e2-acaf-933a8bde3352` | 87-98 [crates/gcode/src/graph/code_graph/read/relationships.rs:87-98] | Indexed function `find_usages` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:87-98] |
| `find_caller_ids` | function | `pub fn find_caller_ids(` | `find_caller_ids [function]` | `5a549e59-1336-5c75-a8b0-ec2a96d71228` | 100-113 [crates/gcode/src/graph/code_graph/read/relationships.rs:100-113] | Indexed function `find_caller_ids` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:100-113] |
| `find_usage_ids` | function | `pub fn find_usage_ids(ctx: &Context, symbol_id: &str, limit: usize) -> anyhow::Result<Vec<String>> {` | `find_usage_ids [function]` | `7ed27d5c-87f9-59d9-9a32-7cde064e5215` | 115-124 [crates/gcode/src/graph/code_graph/read/relationships.rs:115-124] | Indexed function `find_usage_ids` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:115-124] |
| `find_callers_batch` | function | `pub fn find_callers_batch(` | `find_callers_batch [function]` | `013ba3fc-1ab0-5c4d-b432-2bb0c60d53f4` | 126-139 [crates/gcode/src/graph/code_graph/read/relationships.rs:126-139] | Indexed function `find_callers_batch` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:126-139] |
| `find_caller_ids_batch` | function | `pub fn find_caller_ids_batch(` | `find_caller_ids_batch [function]` | `ed26b4b4-bab2-5dc9-bb37-e2036f9b8b0d` | 141-157 [crates/gcode/src/graph/code_graph/read/relationships.rs:141-157] | Indexed function `find_caller_ids_batch` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:141-157] |
| `find_callees_batch` | function | `pub fn find_callees_batch(` | `find_callees_batch [function]` | `9930ba17-3467-5a8a-b64f-f4fcdee7a817` | 159-172 [crates/gcode/src/graph/code_graph/read/relationships.rs:159-172] | Indexed function `find_callees_batch` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:159-172] |
| `find_callee_ids_batch` | function | `pub fn find_callee_ids_batch(` | `find_callee_ids_batch [function]` | `c5700a76-f1ef-5ae5-b9af-55c3d65719af` | 174-190 [crates/gcode/src/graph/code_graph/read/relationships.rs:174-190] | Indexed function `find_callee_ids_batch` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:174-190] |
| `get_imports` | function | `pub fn get_imports(ctx: &Context, file_path: &str) -> anyhow::Result<Vec<GraphResult>> {` | `get_imports [function]` | `e709ff1f-3284-5206-8d00-c0f37a6c6de8` | 192-198 [crates/gcode/src/graph/code_graph/read/relationships.rs:192-198] | Indexed function `get_imports` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:192-198] |
| `resolve_external_call_target` | function | `pub fn resolve_external_call_target(` | `resolve_external_call_target [function]` | `02901a5e-07a1-54af-bc05-c28bda77249b` | 200-225 [crates/gcode/src/graph/code_graph/read/relationships.rs:200-225] | Indexed function `resolve_external_call_target` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:200-225] |
| `symbol_callee_edges` | function | `fn symbol_callee_edges(` | `symbol_callee_edges [function]` | `5bc30906-a5e6-5f75-8b1b-e5743e43fa09` | 227-245 [crates/gcode/src/graph/code_graph/read/relationships.rs:227-245] | Indexed function `symbol_callee_edges` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:227-245] |
| `reconstruct_symbol_path` | function | `fn reconstruct_symbol_path(` | `reconstruct_symbol_path [function]` | `708e658a-db9a-552c-b85e-0cb1e4bea998` | 247-263 [crates/gcode/src/graph/code_graph/read/relationships.rs:247-263] | Indexed function `reconstruct_symbol_path` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:247-263] |
| `symbol_path_steps` | function | `fn symbol_path_steps(` | `symbol_path_steps [function]` | `503b8dc1-e54d-52df-9bfc-b4ba1c6b5099` | 265-302 [crates/gcode/src/graph/code_graph/read/relationships.rs:265-302] | Indexed function `symbol_path_steps` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:265-302] |
| `shortest_symbol_path` | function | `pub fn shortest_symbol_path(` | `shortest_symbol_path [function]` | `267b692b-e811-5721-868e-30420c63f9d0` | 304-342 [crates/gcode/src/graph/code_graph/read/relationships.rs:304-342] | Indexed function `shortest_symbol_path` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:304-342] |
| `blast_radius` | function | `pub fn blast_radius(` | `blast_radius [function]` | `b938d31e-e6da-5d54-9f87-34db92a319e5` | 344-355 [crates/gcode/src/graph/code_graph/read/relationships.rs:344-355] | Indexed function `blast_radius` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:344-355] |
| `target` | function | `fn target(id: &str, display_name: &str) -> ResolvedExternalCallTarget {` | `target [function]` | `25b2c098-db35-55b8-a56b-be0e5c0fe83a` | 361-366 [crates/gcode/src/graph/code_graph/read/relationships.rs:361-366] | Indexed function `target` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:361-366] |
| `external_call_target_display_uses_module_when_present` | function | `fn external_call_target_display_uses_module_when_present() {` | `external_call_target_display_uses_module_when_present [function]` | `ad578b20-94b0-5129-9e72-d9014ff0d6ee` | 369-375 [crates/gcode/src/graph/code_graph/read/relationships.rs:369-375] | Indexed function `external_call_target_display_uses_module_when_present` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:369-375] |
| `select_external_call_target_resolves_single_candidate` | function | `fn select_external_call_target_resolves_single_candidate() {` | `select_external_call_target_resolves_single_candidate [function]` | `1a3800d6-02e5-53dc-98a8-3c77cdad2607` | 378-386 [crates/gcode/src/graph/code_graph/read/relationships.rs:378-386] | Indexed function `select_external_call_target_resolves_single_candidate` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:378-386] |
| `select_external_call_target_reports_ambiguous_candidates` | function | `fn select_external_call_target_reports_ambiguous_candidates() {` | `select_external_call_target_reports_ambiguous_candidates [function]` | `27f53e90-c28b-5060-b949-cdcd81a32d78` | 389-397 [crates/gcode/src/graph/code_graph/read/relationships.rs:389-397] | Indexed function `select_external_call_target_reports_ambiguous_candidates` in `crates/gcode/src/graph/code_graph/read/relationships.rs`. [crates/gcode/src/graph/code_graph/read/relationships.rs:389-397] |
