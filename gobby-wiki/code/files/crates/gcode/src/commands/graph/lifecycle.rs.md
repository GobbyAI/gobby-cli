---
title: crates/gcode/src/commands/graph/lifecycle.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/graph/lifecycle.rs
  ranges:
  - 12-14
  - 17-28
  - 30-41
  - 43-45
  - 47-49
  - 51-53
  - 57-64
  - 69-76
  - 78-84
  - '86'
  - 89-98
  - 101-115
  - 117-129
  - 131-138
  - 140-147
  - 149-161
  - 163-165
  - 167-211
  - 213-234
  - 236-320
  - 322-329
  - 331-338
  - 345-365
  - 367-375
  - 377-440
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/graph/lifecycle.rs:12-14](crates/gcode/src/commands/graph/lifecycle.rs#L12-L14), [crates/gcode/src/commands/graph/lifecycle.rs:17-28](crates/gcode/src/commands/graph/lifecycle.rs#L17-L28), [crates/gcode/src/commands/graph/lifecycle.rs:30-41](crates/gcode/src/commands/graph/lifecycle.rs#L30-L41), [crates/gcode/src/commands/graph/lifecycle.rs:43-45](crates/gcode/src/commands/graph/lifecycle.rs#L43-L45), [crates/gcode/src/commands/graph/lifecycle.rs:47-49](crates/gcode/src/commands/graph/lifecycle.rs#L47-L49), [crates/gcode/src/commands/graph/lifecycle.rs:51-53](crates/gcode/src/commands/graph/lifecycle.rs#L51-L53), [crates/gcode/src/commands/graph/lifecycle.rs:57-64](crates/gcode/src/commands/graph/lifecycle.rs#L57-L64), [crates/gcode/src/commands/graph/lifecycle.rs:69-76](crates/gcode/src/commands/graph/lifecycle.rs#L69-L76), [crates/gcode/src/commands/graph/lifecycle.rs:78-84](crates/gcode/src/commands/graph/lifecycle.rs#L78-L84), [crates/gcode/src/commands/graph/lifecycle.rs:86](crates/gcode/src/commands/graph/lifecycle.rs#L86), [crates/gcode/src/commands/graph/lifecycle.rs:89-98](crates/gcode/src/commands/graph/lifecycle.rs#L89-L98), [crates/gcode/src/commands/graph/lifecycle.rs:101-115](crates/gcode/src/commands/graph/lifecycle.rs#L101-L115), [crates/gcode/src/commands/graph/lifecycle.rs:117-129](crates/gcode/src/commands/graph/lifecycle.rs#L117-L129), [crates/gcode/src/commands/graph/lifecycle.rs:131-138](crates/gcode/src/commands/graph/lifecycle.rs#L131-L138), [crates/gcode/src/commands/graph/lifecycle.rs:140-147](crates/gcode/src/commands/graph/lifecycle.rs#L140-L147), [crates/gcode/src/commands/graph/lifecycle.rs:149-161](crates/gcode/src/commands/graph/lifecycle.rs#L149-L161), [crates/gcode/src/commands/graph/lifecycle.rs:163-165](crates/gcode/src/commands/graph/lifecycle.rs#L163-L165), [crates/gcode/src/commands/graph/lifecycle.rs:167-211](crates/gcode/src/commands/graph/lifecycle.rs#L167-L211), [crates/gcode/src/commands/graph/lifecycle.rs:213-234](crates/gcode/src/commands/graph/lifecycle.rs#L213-L234), [crates/gcode/src/commands/graph/lifecycle.rs:236-320](crates/gcode/src/commands/graph/lifecycle.rs#L236-L320), [crates/gcode/src/commands/graph/lifecycle.rs:322-329](crates/gcode/src/commands/graph/lifecycle.rs#L322-L329), [crates/gcode/src/commands/graph/lifecycle.rs:331-338](crates/gcode/src/commands/graph/lifecycle.rs#L331-L338), [crates/gcode/src/commands/graph/lifecycle.rs:345-365](crates/gcode/src/commands/graph/lifecycle.rs#L345-L365), [crates/gcode/src/commands/graph/lifecycle.rs:367-375](crates/gcode/src/commands/graph/lifecycle.rs#L367-L375), [crates/gcode/src/commands/graph/lifecycle.rs:377-440](crates/gcode/src/commands/graph/lifecycle.rs#L377-L440)

</details>

# crates/gcode/src/commands/graph/lifecycle.rs

Module: [[code/modules/crates/gcode/src/commands/graph|crates/gcode/src/commands/graph]]

## Purpose

Implements the graph lifecycle command flow for the code graph: it defines a contract error type for sync failures, formats success/error output, and exposes a backend abstraction plus the high-level entry points for running lifecycle actions. The helper functions coordinate file-level sync, project graph clearing/rebuilding, orphan and deleted-project cleanup, and the sync/rebuild wrappers so the command layer can return structured JSON or human-readable status consistently.
[crates/gcode/src/commands/graph/lifecycle.rs:12-14]
[crates/gcode/src/commands/graph/lifecycle.rs:17-28]
[crates/gcode/src/commands/graph/lifecycle.rs:30-41]
[crates/gcode/src/commands/graph/lifecycle.rs:43-45]
[crates/gcode/src/commands/graph/lifecycle.rs:47-49]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `GraphSyncContractError` | class | `pub struct GraphSyncContractError {` | `GraphSyncContractError [class]` | `95cb25f4-e1f7-5eea-af0c-64c37790e5b9` | 12-14 [crates/gcode/src/commands/graph/lifecycle.rs:12-14] | Indexed class `GraphSyncContractError` in `crates/gcode/src/commands/graph/lifecycle.rs`. [crates/gcode/src/commands/graph/lifecycle.rs:12-14] |
| `GraphSyncContractError::project_not_indexed` | method | `pub(super) fn project_not_indexed(ctx: &Context, file_path: &str) -> Self {` | `GraphSyncContractError::project_not_indexed [method]` | `3aa2684d-396b-57d6-81db-823ce9abf938` | 17-28 [crates/gcode/src/commands/graph/lifecycle.rs:17-28] | Indexed method `GraphSyncContractError::project_not_indexed` in `crates/gcode/src/commands/graph/lifecycle.rs`. [crates/gcode/src/commands/graph/lifecycle.rs:17-28] |
| `GraphSyncContractError::indexed_file_not_found` | method | `pub(super) fn indexed_file_not_found(ctx: &Context, file_path: &str) -> Self {` | `GraphSyncContractError::indexed_file_not_found [method]` | `f8d135df-c390-5217-a73d-cd34d187be0f` | 30-41 [crates/gcode/src/commands/graph/lifecycle.rs:30-41] | Indexed method `GraphSyncContractError::indexed_file_not_found` in `crates/gcode/src/commands/graph/lifecycle.rs`. [crates/gcode/src/commands/graph/lifecycle.rs:30-41] |
| `GraphSyncContractError::exit_code` | method | `pub fn exit_code(&self) -> u8 {` | `GraphSyncContractError::exit_code [method]` | `eae964ca-8fdf-5d8a-913a-0cf46102e75f` | 43-45 [crates/gcode/src/commands/graph/lifecycle.rs:43-45] | Indexed method `GraphSyncContractError::exit_code` in `crates/gcode/src/commands/graph/lifecycle.rs`. [crates/gcode/src/commands/graph/lifecycle.rs:43-45] |
| `GraphSyncContractError::print` | method | `pub fn print(&self) -> anyhow::Result<()> {` | `GraphSyncContractError::print [method]` | `71bea680-d940-53c1-9aa5-03725ed26611` | 47-49 [crates/gcode/src/commands/graph/lifecycle.rs:47-49] | Indexed method `GraphSyncContractError::print` in `crates/gcode/src/commands/graph/lifecycle.rs`. [crates/gcode/src/commands/graph/lifecycle.rs:47-49] |
| `GraphSyncContractError::payload` | method | `pub fn payload(&self) -> &Value {` | `GraphSyncContractError::payload [method]` | `0109de40-7324-5f91-99e9-6fd1ba08e599` | 51-53 [crates/gcode/src/commands/graph/lifecycle.rs:51-53] | Indexed method `GraphSyncContractError::payload` in `crates/gcode/src/commands/graph/lifecycle.rs`. [crates/gcode/src/commands/graph/lifecycle.rs:51-53] |
| `GraphSyncContractError::fmt` | method | `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {` | `GraphSyncContractError::fmt [method]` | `71ed0210-42e4-56e8-a5ba-944001bfa546` | 57-64 [crates/gcode/src/commands/graph/lifecycle.rs:57-64] | Indexed method `GraphSyncContractError::fmt` in `crates/gcode/src/commands/graph/lifecycle.rs`. [crates/gcode/src/commands/graph/lifecycle.rs:57-64] |
| `format_success_text` | function | `pub(super) fn format_success_text(output: &GraphLifecycleOutput) -> String {` | `format_success_text [function]` | `14a613ca-e60f-5141-b5e0-cb157a7ca83d` | 69-76 [crates/gcode/src/commands/graph/lifecycle.rs:69-76] | Indexed function `format_success_text` in `crates/gcode/src/commands/graph/lifecycle.rs`. [crates/gcode/src/commands/graph/lifecycle.rs:69-76] |
| `LifecycleBackend` | type | `pub(super) trait LifecycleBackend {` | `LifecycleBackend [type]` | `2d492478-1988-5e01-9da7-4dbc99adc638` | 78-84 [crates/gcode/src/commands/graph/lifecycle.rs:78-84] | Indexed type `LifecycleBackend` in `crates/gcode/src/commands/graph/lifecycle.rs`. [crates/gcode/src/commands/graph/lifecycle.rs:78-84] |
| `CodeGraphLifecycleBackend` | class | `struct CodeGraphLifecycleBackend;` | `CodeGraphLifecycleBackend [class]` | `4d7bf3ce-41fb-5d3a-95a5-c71856a19da3` | 86-86 [crates/gcode/src/commands/graph/lifecycle.rs:86] | Indexed class `CodeGraphLifecycleBackend` in `crates/gcode/src/commands/graph/lifecycle.rs`. [crates/gcode/src/commands/graph/lifecycle.rs:86] |
| `CodeGraphLifecycleBackend::run` | method | `fn run(` | `CodeGraphLifecycleBackend::run [method]` | `695f7fd4-361e-5210-a0b2-5129e506f4d3` | 89-98 [crates/gcode/src/commands/graph/lifecycle.rs:89-98] | Indexed method `CodeGraphLifecycleBackend::run` in `crates/gcode/src/commands/graph/lifecycle.rs`. [crates/gcode/src/commands/graph/lifecycle.rs:89-98] |
| `run_lifecycle_action_with_backend` | function | `pub(super) fn run_lifecycle_action_with_backend(` | `run_lifecycle_action_with_backend [function]` | `d1f7ee77-88a6-5ae8-a267-120a6efe9b93` | 101-115 [crates/gcode/src/commands/graph/lifecycle.rs:101-115] | Indexed function `run_lifecycle_action_with_backend` in `crates/gcode/src/commands/graph/lifecycle.rs`. [crates/gcode/src/commands/graph/lifecycle.rs:101-115] |
| `lifecycle_output` | function | `fn lifecycle_output(` | `lifecycle_output [function]` | `d5e3a602-cee7-596d-8bad-4eec33f4b381` | 117-129 [crates/gcode/src/commands/graph/lifecycle.rs:117-129] | Indexed function `lifecycle_output` in `crates/gcode/src/commands/graph/lifecycle.rs`. [crates/gcode/src/commands/graph/lifecycle.rs:117-129] |
| `GraphFileSyncOutcome` | type | `enum GraphFileSyncOutcome {` | `GraphFileSyncOutcome [type]` | `5a6558a1-f41d-5c2f-801e-781a9cedc834` | 131-138 [crates/gcode/src/commands/graph/lifecycle.rs:131-138] | Indexed type `GraphFileSyncOutcome` in `crates/gcode/src/commands/graph/lifecycle.rs`. [crates/gcode/src/commands/graph/lifecycle.rs:131-138] |
| `skipped_missing_indexed_file_payload` | function | `pub(super) fn skipped_missing_indexed_file_payload(ctx: &Context, file_path: &str) -> Value {` | `skipped_missing_indexed_file_payload [function]` | `52ece424-9c84-5199-ac7d-5d3ff5d3322d` | 140-147 [crates/gcode/src/commands/graph/lifecycle.rs:140-147] | Indexed function `skipped_missing_indexed_file_payload` in `crates/gcode/src/commands/graph/lifecycle.rs`. [crates/gcode/src/commands/graph/lifecycle.rs:140-147] |
| `skipped_no_graph_facts_payload` | function | `pub(super) fn skipped_no_graph_facts_payload(ctx: &Context, file_path: &str) -> Value {` | `skipped_no_graph_facts_payload [function]` | `f6fb9a38-c7e7-538f-910b-c9aaf7cc197a` | 149-161 [crates/gcode/src/commands/graph/lifecycle.rs:149-161] | Indexed function `skipped_no_graph_facts_payload` in `crates/gcode/src/commands/graph/lifecycle.rs`. [crates/gcode/src/commands/graph/lifecycle.rs:149-161] |
| `has_no_graph_facts` | function | `pub(super) fn has_no_graph_facts<I, D, C>(imports: &[I], definitions: &[D], calls: &[C]) -> bool {` | `has_no_graph_facts [function]` | `a43cb306-e69a-52a2-8edd-1be74a962e82` | 163-165 [crates/gcode/src/commands/graph/lifecycle.rs:163-165] | Indexed function `has_no_graph_facts` in `crates/gcode/src/commands/graph/lifecycle.rs`. [crates/gcode/src/commands/graph/lifecycle.rs:163-165] |
| `sync_file_graph` | function | `fn sync_file_graph(` | `sync_file_graph [function]` | `a23f30e5-ed7a-5f1a-b189-db940072bad9` | 167-211 [crates/gcode/src/commands/graph/lifecycle.rs:167-211] | Indexed function `sync_file_graph` in `crates/gcode/src/commands/graph/lifecycle.rs`. [crates/gcode/src/commands/graph/lifecycle.rs:167-211] |
| `clear_project_graph` | function | `fn clear_project_graph(ctx: &Context) -> anyhow::Result<GraphLifecycleOutput> {` | `clear_project_graph [function]` | `4825b611-0875-5fa0-af2e-f2af16d203d5` | 213-234 [crates/gcode/src/commands/graph/lifecycle.rs:213-234] | Indexed function `clear_project_graph` in `crates/gcode/src/commands/graph/lifecycle.rs`. [crates/gcode/src/commands/graph/lifecycle.rs:213-234] |
| `rebuild_project_graph` | function | `fn rebuild_project_graph(ctx: &Context) -> anyhow::Result<GraphLifecycleOutput> {` | `rebuild_project_graph [function]` | `0daae913-bbc7-51cf-aa40-e6223b20d7fa` | 236-320 [crates/gcode/src/commands/graph/lifecycle.rs:236-320] | Indexed function `rebuild_project_graph` in `crates/gcode/src/commands/graph/lifecycle.rs`. [crates/gcode/src/commands/graph/lifecycle.rs:236-320] |
| `clear` | function | `pub fn clear(ctx: &Context, format: Format) -> anyhow::Result<()> {` | `clear [function]` | `2f46e8c3-ac41-5f5d-b926-c23f48d0e8f5` | 322-329 [crates/gcode/src/commands/graph/lifecycle.rs:322-329] | Indexed function `clear` in `crates/gcode/src/commands/graph/lifecycle.rs`. [crates/gcode/src/commands/graph/lifecycle.rs:322-329] |
| `rebuild` | function | `pub fn rebuild(ctx: &Context, format: Format) -> anyhow::Result<()> {` | `rebuild [function]` | `b869c442-314a-53c6-9871-1ac8e9db210d` | 331-338 [crates/gcode/src/commands/graph/lifecycle.rs:331-338] | Indexed function `rebuild` in `crates/gcode/src/commands/graph/lifecycle.rs`. [crates/gcode/src/commands/graph/lifecycle.rs:331-338] |
| `cleanup_orphans` | function | `pub fn cleanup_orphans(ctx: &Context, format: Format) -> anyhow::Result<()> {` | `cleanup_orphans [function]` | `3bfcfd68-522a-527e-89c3-76e697ae0cd0` | 345-365 [crates/gcode/src/commands/graph/lifecycle.rs:345-365] | Indexed function `cleanup_orphans` in `crates/gcode/src/commands/graph/lifecycle.rs`. [crates/gcode/src/commands/graph/lifecycle.rs:345-365] |
| `cleanup_deleted_project_graph` | function | `pub(crate) fn cleanup_deleted_project_graph(` | `cleanup_deleted_project_graph [function]` | `2c406a81-3008-5ad8-b1c6-f175350676ab` | 367-375 [crates/gcode/src/commands/graph/lifecycle.rs:367-375] | Indexed function `cleanup_deleted_project_graph` in `crates/gcode/src/commands/graph/lifecycle.rs`. [crates/gcode/src/commands/graph/lifecycle.rs:367-375] |
| `sync_file` | function | `pub fn sync_file(` | `sync_file [function]` | `7d04aa32-043b-56fc-a044-3359ec5b303d` | 377-440 [crates/gcode/src/commands/graph/lifecycle.rs:377-440] | Indexed function `sync_file` in `crates/gcode/src/commands/graph/lifecycle.rs`. [crates/gcode/src/commands/graph/lifecycle.rs:377-440] |
