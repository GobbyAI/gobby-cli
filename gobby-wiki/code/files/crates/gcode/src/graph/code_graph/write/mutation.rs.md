---
title: crates/gcode/src/graph/code_graph/write/mutation.rs
type: code_file
provenance:
- file: crates/gcode/src/graph/code_graph/write/mutation.rs
  ranges:
  - 89-96
  - 99-102
  - 105-112
  - 115-119
  - 121-128
  - 130-145
  - 147-152
  - 154-182
  - 184-197
  - 199-207
  - 209-227
  - 229-259
  - 261-295
  - 297-301
  - 304-321
  - 323-327
  - 329-334
  - 337-343
  - 345-364
  - 366-377
  - 379-390
  - 392-403
  - 411-435
  - 438-450
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/graph/code_graph/write/mutation.rs:89-96](crates/gcode/src/graph/code_graph/write/mutation.rs#L89-L96), [crates/gcode/src/graph/code_graph/write/mutation.rs:99-102](crates/gcode/src/graph/code_graph/write/mutation.rs#L99-L102), [crates/gcode/src/graph/code_graph/write/mutation.rs:105-112](crates/gcode/src/graph/code_graph/write/mutation.rs#L105-L112), [crates/gcode/src/graph/code_graph/write/mutation.rs:115-119](crates/gcode/src/graph/code_graph/write/mutation.rs#L115-L119), [crates/gcode/src/graph/code_graph/write/mutation.rs:121-128](crates/gcode/src/graph/code_graph/write/mutation.rs#L121-L128), [crates/gcode/src/graph/code_graph/write/mutation.rs:130-145](crates/gcode/src/graph/code_graph/write/mutation.rs#L130-L145), [crates/gcode/src/graph/code_graph/write/mutation.rs:147-152](crates/gcode/src/graph/code_graph/write/mutation.rs#L147-L152), [crates/gcode/src/graph/code_graph/write/mutation.rs:154-182](crates/gcode/src/graph/code_graph/write/mutation.rs#L154-L182), [crates/gcode/src/graph/code_graph/write/mutation.rs:184-197](crates/gcode/src/graph/code_graph/write/mutation.rs#L184-L197), [crates/gcode/src/graph/code_graph/write/mutation.rs:199-207](crates/gcode/src/graph/code_graph/write/mutation.rs#L199-L207), [crates/gcode/src/graph/code_graph/write/mutation.rs:209-227](crates/gcode/src/graph/code_graph/write/mutation.rs#L209-L227), [crates/gcode/src/graph/code_graph/write/mutation.rs:229-259](crates/gcode/src/graph/code_graph/write/mutation.rs#L229-L259), [crates/gcode/src/graph/code_graph/write/mutation.rs:261-295](crates/gcode/src/graph/code_graph/write/mutation.rs#L261-L295), [crates/gcode/src/graph/code_graph/write/mutation.rs:297-301](crates/gcode/src/graph/code_graph/write/mutation.rs#L297-L301), [crates/gcode/src/graph/code_graph/write/mutation.rs:304-321](crates/gcode/src/graph/code_graph/write/mutation.rs#L304-L321), [crates/gcode/src/graph/code_graph/write/mutation.rs:323-327](crates/gcode/src/graph/code_graph/write/mutation.rs#L323-L327), [crates/gcode/src/graph/code_graph/write/mutation.rs:329-334](crates/gcode/src/graph/code_graph/write/mutation.rs#L329-L334), [crates/gcode/src/graph/code_graph/write/mutation.rs:337-343](crates/gcode/src/graph/code_graph/write/mutation.rs#L337-L343), [crates/gcode/src/graph/code_graph/write/mutation.rs:345-364](crates/gcode/src/graph/code_graph/write/mutation.rs#L345-L364), [crates/gcode/src/graph/code_graph/write/mutation.rs:366-377](crates/gcode/src/graph/code_graph/write/mutation.rs#L366-L377), [crates/gcode/src/graph/code_graph/write/mutation.rs:379-390](crates/gcode/src/graph/code_graph/write/mutation.rs#L379-L390), [crates/gcode/src/graph/code_graph/write/mutation.rs:392-403](crates/gcode/src/graph/code_graph/write/mutation.rs#L392-L403), [crates/gcode/src/graph/code_graph/write/mutation.rs:411-435](crates/gcode/src/graph/code_graph/write/mutation.rs#L411-L435), [crates/gcode/src/graph/code_graph/write/mutation.rs:438-450](crates/gcode/src/graph/code_graph/write/mutation.rs#L438-L450)

</details>

# crates/gcode/src/graph/code_graph/write/mutation.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

Builds Cypher mutations for syncing a code graph into the database. The file centralizes shared constants and helpers for provenance and sync-token generation, then assembles query fragments for imports, definitions, and call relationships. `SyncFileMutation` and `ensure_file_node_query` support file-level upserts, `add_imports_query` and `add_definitions_query` write import and symbol-definition edges, and the `GraphCallTarget`/`call_rows` helpers split calls into symbol, external, and unresolved targets so the three call mutation queries can write the right `CALLS` relationships.
[crates/gcode/src/graph/code_graph/write/mutation.rs:89-96]
[crates/gcode/src/graph/code_graph/write/mutation.rs:99-102]
[crates/gcode/src/graph/code_graph/write/mutation.rs:105-112]
[crates/gcode/src/graph/code_graph/write/mutation.rs:115-119]
[crates/gcode/src/graph/code_graph/write/mutation.rs:121-128]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `new_sync_token` | function | `pub(super) fn new_sync_token(file_path: &str) -> String {` | `new_sync_token [function]` | `a8869846-a57f-5abe-b587-24741c8f8413` | 89-96 [crates/gcode/src/graph/code_graph/write/mutation.rs:89-96] | Indexed function `new_sync_token` in `crates/gcode/src/graph/code_graph/write/mutation.rs`. [crates/gcode/src/graph/code_graph/write/mutation.rs:89-96] |
| `ImportGraphItem` | class | `pub(in crate::graph::code_graph) struct ImportGraphItem {` | `ImportGraphItem [class]` | `e3e21d69-34de-5bf8-ae87-3af3bb621bf4` | 99-102 [crates/gcode/src/graph/code_graph/write/mutation.rs:99-102] | Indexed class `ImportGraphItem` in `crates/gcode/src/graph/code_graph/write/mutation.rs`. [crates/gcode/src/graph/code_graph/write/mutation.rs:99-102] |
| `CallGraphItem` | class | `pub(in crate::graph::code_graph) struct CallGraphItem {` | `CallGraphItem [class]` | `8216b71e-91cc-5459-a595-ef65977a27c2` | 105-112 [crates/gcode/src/graph/code_graph/write/mutation.rs:105-112] | Indexed class `CallGraphItem` in `crates/gcode/src/graph/code_graph/write/mutation.rs`. [crates/gcode/src/graph/code_graph/write/mutation.rs:105-112] |
| `CallGraphItems` | class | `pub(in crate::graph::code_graph) struct CallGraphItems {` | `CallGraphItems [class]` | `ad9a643c-cae1-5944-b160-e3c7e4145c8b` | 115-119 [crates/gcode/src/graph/code_graph/write/mutation.rs:115-119] | Indexed class `CallGraphItems` in `crates/gcode/src/graph/code_graph/write/mutation.rs`. [crates/gcode/src/graph/code_graph/write/mutation.rs:115-119] |
| `map_value` | function | `fn map_value(values: impl IntoIterator<Item = (&'static str, TypedValue)>) -> TypedValue {` | `map_value [function]` | `8b3d881e-e34f-545a-9757-873171c9dc1c` | 121-128 [crates/gcode/src/graph/code_graph/write/mutation.rs:121-128] | Indexed function `map_value` in `crates/gcode/src/graph/code_graph/write/mutation.rs`. [crates/gcode/src/graph/code_graph/write/mutation.rs:121-128] |
| `import_graph_items` | function | `pub(in crate::graph::code_graph) fn import_graph_items(` | `import_graph_items [function]` | `fe32193e-e656-514f-a57c-f045363d9b2b` | 130-145 [crates/gcode/src/graph/code_graph/write/mutation.rs:130-145] | Indexed function `import_graph_items` in `crates/gcode/src/graph/code_graph/write/mutation.rs`. [crates/gcode/src/graph/code_graph/write/mutation.rs:130-145] |
| `definition_graph_symbols` | function | `pub(super) fn definition_graph_symbols(definitions: &[Symbol]) -> Vec<&Symbol> {` | `definition_graph_symbols [function]` | `eef347a6-d2c4-5db3-bbca-9ccdbd799044` | 147-152 [crates/gcode/src/graph/code_graph/write/mutation.rs:147-152] | Indexed function `definition_graph_symbols` in `crates/gcode/src/graph/code_graph/write/mutation.rs`. [crates/gcode/src/graph/code_graph/write/mutation.rs:147-152] |
| `partition_call_graph_items` | function | `pub(in crate::graph::code_graph) fn partition_call_graph_items(` | `partition_call_graph_items [function]` | `40662a74-88c2-596a-82a7-59ee84497227` | 154-182 [crates/gcode/src/graph/code_graph/write/mutation.rs:154-182] | Indexed function `partition_call_graph_items` in `crates/gcode/src/graph/code_graph/write/mutation.rs`. [crates/gcode/src/graph/code_graph/write/mutation.rs:154-182] |
| `metadata_params` | function | `fn metadata_params(sync_token: &str) -> Vec<(&'static str, TypedValue)> {` | `metadata_params [function]` | `d728f3c4-1807-51af-b706-28a7394d375d` | 184-197 [crates/gcode/src/graph/code_graph/write/mutation.rs:184-197] | Indexed function `metadata_params` in `crates/gcode/src/graph/code_graph/write/mutation.rs`. [crates/gcode/src/graph/code_graph/write/mutation.rs:184-197] |
| `SyncFileMutation` | class | `pub(super) struct SyncFileMutation<'a> {` | `SyncFileMutation [class]` | `015f1eff-b334-5337-a893-bad0353001c2` | 199-207 [crates/gcode/src/graph/code_graph/write/mutation.rs:199-207] | Indexed class `SyncFileMutation` in `crates/gcode/src/graph/code_graph/write/mutation.rs`. [crates/gcode/src/graph/code_graph/write/mutation.rs:199-207] |
| `ensure_file_node_query` | function | `pub(super) fn ensure_file_node_query(` | `ensure_file_node_query [function]` | `d596eb39-fdeb-594f-9cc0-ec5a6e6a740f` | 209-227 [crates/gcode/src/graph/code_graph/write/mutation.rs:209-227] | Indexed function `ensure_file_node_query` in `crates/gcode/src/graph/code_graph/write/mutation.rs`. [crates/gcode/src/graph/code_graph/write/mutation.rs:209-227] |
| `add_imports_query` | function | `pub(super) fn add_imports_query(` | `add_imports_query [function]` | `49f95909-a463-50da-9751-9357d42e4a2f` | 229-259 [crates/gcode/src/graph/code_graph/write/mutation.rs:229-259] | Indexed function `add_imports_query` in `crates/gcode/src/graph/code_graph/write/mutation.rs`. [crates/gcode/src/graph/code_graph/write/mutation.rs:229-259] |
| `add_definitions_query` | function | `pub(super) fn add_definitions_query(` | `add_definitions_query [function]` | `9562a0f8-11b8-5d5e-b3bb-b654cbd0572f` | 261-295 [crates/gcode/src/graph/code_graph/write/mutation.rs:261-295] | Indexed function `add_definitions_query` in `crates/gcode/src/graph/code_graph/write/mutation.rs`. [crates/gcode/src/graph/code_graph/write/mutation.rs:261-295] |
| `GraphCallTarget` | type | `enum GraphCallTarget {` | `GraphCallTarget [type]` | `a9c5b35c-0d08-53bc-a4a5-99529cc5ef5d` | 297-301 [crates/gcode/src/graph/code_graph/write/mutation.rs:297-301] | Indexed type `GraphCallTarget` in `crates/gcode/src/graph/code_graph/write/mutation.rs`. [crates/gcode/src/graph/code_graph/write/mutation.rs:297-301] |
| `GraphCallTarget::from_call` | method | `fn from_call(project_id: &str, call: &CallRelation) -> Option<Self> {` | `GraphCallTarget::from_call [method]` | `f301e8b4-d050-5e98-98c3-a2e160c9bdef` | 304-321 [crates/gcode/src/graph/code_graph/write/mutation.rs:304-321] | Indexed method `GraphCallTarget::from_call` in `crates/gcode/src/graph/code_graph/write/mutation.rs`. [crates/gcode/src/graph/code_graph/write/mutation.rs:304-321] |
| `GraphCallTarget::id` | method | `fn id(&self) -> &str {` | `GraphCallTarget::id [method]` | `1dc09ea5-212b-5bf0-a7f1-5f2eef72080a` | 323-327 [crates/gcode/src/graph/code_graph/write/mutation.rs:323-327] | Indexed method `GraphCallTarget::id` in `crates/gcode/src/graph/code_graph/write/mutation.rs`. [crates/gcode/src/graph/code_graph/write/mutation.rs:323-327] |
| `GraphCallTarget::module` | method | `fn module(&self) -> Option<&str> {` | `GraphCallTarget::module [method]` | `fb33098b-c1b2-5dc2-b9a4-3cbd8c6bc2ff` | 329-334 [crates/gcode/src/graph/code_graph/write/mutation.rs:329-334] | Indexed method `GraphCallTarget::module` in `crates/gcode/src/graph/code_graph/write/mutation.rs`. [crates/gcode/src/graph/code_graph/write/mutation.rs:329-334] |
| `call_target_id` | function | `pub fn call_target_id(project_id: &str, call: &CallRelation) -> Option<String> {` | `call_target_id [function]` | `ce402677-421b-5686-b1eb-4949c37daeff` | 337-343 [crates/gcode/src/graph/code_graph/write/mutation.rs:337-343] | Indexed function `call_target_id` in `crates/gcode/src/graph/code_graph/write/mutation.rs`. [crates/gcode/src/graph/code_graph/write/mutation.rs:337-343] |
| `call_rows` | function | `fn call_rows(calls: &[CallGraphItem]) -> anyhow::Result<TypedValue> {` | `call_rows [function]` | `ad187869-a667-5a5e-9799-d546b2844cb5` | 345-364 [crates/gcode/src/graph/code_graph/write/mutation.rs:345-364] | Indexed function `call_rows` in `crates/gcode/src/graph/code_graph/write/mutation.rs`. [crates/gcode/src/graph/code_graph/write/mutation.rs:345-364] |
| `add_symbol_calls_query` | function | `pub(super) fn add_symbol_calls_query(` | `add_symbol_calls_query [function]` | `4e2fbd55-4044-59e2-9786-dde50ef49b0c` | 366-377 [crates/gcode/src/graph/code_graph/write/mutation.rs:366-377] | Indexed function `add_symbol_calls_query` in `crates/gcode/src/graph/code_graph/write/mutation.rs`. [crates/gcode/src/graph/code_graph/write/mutation.rs:366-377] |
| `add_external_calls_query` | function | `pub(super) fn add_external_calls_query(` | `add_external_calls_query [function]` | `725a13c0-675c-5b80-9cc9-dc1245885fa9` | 379-390 [crates/gcode/src/graph/code_graph/write/mutation.rs:379-390] | Indexed function `add_external_calls_query` in `crates/gcode/src/graph/code_graph/write/mutation.rs`. [crates/gcode/src/graph/code_graph/write/mutation.rs:379-390] |
| `add_unresolved_calls_query` | function | `pub(super) fn add_unresolved_calls_query(` | `add_unresolved_calls_query [function]` | `9d5c3fe6-de55-5101-a01d-48284fc003ee` | 392-403 [crates/gcode/src/graph/code_graph/write/mutation.rs:392-403] | Indexed function `add_unresolved_calls_query` in `crates/gcode/src/graph/code_graph/write/mutation.rs`. [crates/gcode/src/graph/code_graph/write/mutation.rs:392-403] |
| `unresolved_local_import_projects_as_unresolved_not_external` | function | `fn unresolved_local_import_projects_as_unresolved_not_external() {` | `unresolved_local_import_projects_as_unresolved_not_external [function]` | `6173c6c5-4bce-5e4c-bab7-cf7edac33923` | 411-435 [crates/gcode/src/graph/code_graph/write/mutation.rs:411-435] | Indexed function `unresolved_local_import_projects_as_unresolved_not_external` in `crates/gcode/src/graph/code_graph/write/mutation.rs`. [crates/gcode/src/graph/code_graph/write/mutation.rs:411-435] |
| `resolved_local_import_projects_as_symbol` | function | `fn resolved_local_import_projects_as_symbol() {` | `resolved_local_import_projects_as_symbol [function]` | `01fb036d-0ff2-505b-8df6-18332cc72a82` | 438-450 [crates/gcode/src/graph/code_graph/write/mutation.rs:438-450] | Indexed function `resolved_local_import_projects_as_symbol` in `crates/gcode/src/graph/code_graph/write/mutation.rs`. [crates/gcode/src/graph/code_graph/write/mutation.rs:438-450] |
