---
title: crates/gcode/src/commands/graph/lifecycle.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/graph/lifecycle.rs
  ranges:
  - 12-14
  - 16-54
  - 56-65
  - '67'
  - 69-76
  - 78-84
  - '86'
  - 88-99
  - 101-115
  - 117-129
  - 131-138
  - 140-147
  - 149-161
  - 163-165
  - 167-211
  - 213-234
  - 236-314
  - 316-323
  - 325-332
  - 339-359
  - 361-369
  - 371-434
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/graph/lifecycle.rs

Module: [[code/modules/crates/gcode/src/commands/graph|crates/gcode/src/commands/graph]]

## Purpose

Implements the code-graph lifecycle command layer for a project: syncing individual files, clearing the graph, rebuilding it, and cleaning up orphaned graph data. It uses a `LifecycleBackend` abstraction so lifecycle actions can be dispatched to the concrete code-graph operations, then formats the resulting `GraphLifecycleOutput` as either JSON or success text.

The file also defines `GraphSyncContractError`, a JSON-backed error type for contract failures such as “project not indexed” and “indexed file not found,” with a fixed exit code and printable payload. Helper functions build skip/success payloads, detect files with no graph facts, and assemble per-file sync results and orphan cleanup reports.
[crates/gcode/src/commands/graph/lifecycle.rs:12-14]
[crates/gcode/src/commands/graph/lifecycle.rs:16-54]
[crates/gcode/src/commands/graph/lifecycle.rs:17-28]
[crates/gcode/src/commands/graph/lifecycle.rs:30-41]
[crates/gcode/src/commands/graph/lifecycle.rs:43-45]

## API Symbols

- `GraphSyncContractError` (class) component `GraphSyncContractError [class]` (`95cb25f4-e1f7-5eea-af0c-64c37790e5b9`) lines 12-14 [crates/gcode/src/commands/graph/lifecycle.rs:12-14]
  - Signature: `pub struct GraphSyncContractError {`
  - Purpose: 'GraphSyncContractError' is a Rust struct that encapsulates a 'serde_json::Value' payload representing a GraphSync contract error. [crates/gcode/src/commands/graph/lifecycle.rs:12-14]
- `GraphSyncContractError` (class) component `GraphSyncContractError [class]` (`89bc6492-53fc-52b2-907c-2dd79e2c3210`) lines 16-54 [crates/gcode/src/commands/graph/lifecycle.rs:16-54]
  - Signature: `impl GraphSyncContractError {`
  - Purpose: 'GraphSyncContractError' is a JSON-backed error wrapper for graph-sync contract failures that constructs structured payloads for “project not indexed” and “indexed file not found” cases, exposes a fixed exit code, and can print or return the serialized error payload. [crates/gcode/src/commands/graph/lifecycle.rs:16-54]
- `GraphSyncContractError.project_not_indexed` (method) component `GraphSyncContractError.project_not_indexed [method]` (`3aa2684d-396b-57d6-81db-823ce9abf938`) lines 17-28 [crates/gcode/src/commands/graph/lifecycle.rs:17-28]
  - Signature: `pub(super) fn project_not_indexed(ctx: &Context, file_path: &str) -> Self {`
  - Purpose: Constructs a 'Self' value whose JSON payload marks the operation as unsuccessful and reports an error indicating that the current 'ctx.project_id' is not indexed for the given 'file_path'. [crates/gcode/src/commands/graph/lifecycle.rs:17-28]
- `GraphSyncContractError.indexed_file_not_found` (method) component `GraphSyncContractError.indexed_file_not_found [method]` (`f8d135df-c390-5217-a73d-cd34d187be0f`) lines 30-41 [crates/gcode/src/commands/graph/lifecycle.rs:30-41]
  - Signature: `pub(super) fn indexed_file_not_found(ctx: &Context, file_path: &str) -> Self {`
  - Purpose: Constructs a 'Self' error response whose JSON payload marks failure for the given project and file path, sets 'status' to '"error"' and 'reason' to '"indexed_file_not_found"', and includes a formatted message indicating the indexed file was not found for 'ctx.project_id'. [crates/gcode/src/commands/graph/lifecycle.rs:30-41]
- `GraphSyncContractError.exit_code` (method) component `GraphSyncContractError.exit_code [method]` (`eae964ca-8fdf-5d8a-913a-0cf46102e75f`) lines 43-45 [crates/gcode/src/commands/graph/lifecycle.rs:43-45]
  - Signature: `pub fn exit_code(&self) -> u8 {`
  - Purpose: Returns the constant 'GRAPH_SYNC_CONTRACT_EXIT_CODE' as the contract’s exit code, with the return type 'u8'. [crates/gcode/src/commands/graph/lifecycle.rs:43-45]
- `GraphSyncContractError.print` (method) component `GraphSyncContractError.print [method]` (`71bea680-d940-53c1-9aa5-03725ed26611`) lines 47-49 [crates/gcode/src/commands/graph/lifecycle.rs:47-49]
  - Signature: `pub fn print(&self) -> anyhow::Result<()> {`
  - Purpose: Prints 'self.payload' as JSON via 'output::print_json' and returns its 'anyhow::Result<()>'. [crates/gcode/src/commands/graph/lifecycle.rs:47-49]
- `GraphSyncContractError.payload` (method) component `GraphSyncContractError.payload [method]` (`0109de40-7324-5f91-99e9-6fd1ba08e599`) lines 51-53 [crates/gcode/src/commands/graph/lifecycle.rs:51-53]
  - Signature: `pub fn payload(&self) -> &Value {`
  - Purpose: Returns an immutable shared reference to the method’s internal 'payload' field as a '&Value'. [crates/gcode/src/commands/graph/lifecycle.rs:51-53]
- `GraphSyncContractError` (class) component `GraphSyncContractError [class]` (`6e74b847-7897-5195-95e7-636950a5a575`) lines 56-65 [crates/gcode/src/commands/graph/lifecycle.rs:56-65]
  - Signature: `impl std::fmt::Display for GraphSyncContractError {`
  - Purpose: Formats a 'GraphSyncContractError' by reading the 'payload["reason"]' string if present, defaulting to '"graph_sync_contract_error"', and emitting 'graph sync-file contract error: {reason}'. [crates/gcode/src/commands/graph/lifecycle.rs:56-65]
- `GraphSyncContractError.fmt` (method) component `GraphSyncContractError.fmt [method]` (`71ed0210-42e4-56e8-a5ba-944001bfa546`) lines 57-64 [crates/gcode/src/commands/graph/lifecycle.rs:57-64]
  - Signature: `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {`
  - Purpose: Formats the value as 'graph sync-file contract error: {reason}', where 'reason' is read from 'self.payload["reason"]' as a string or defaults to '"graph_sync_contract_error"'. [crates/gcode/src/commands/graph/lifecycle.rs:57-64]
- `GraphSyncContractError` (class) component `GraphSyncContractError [class]` (`903d9eca-7459-5870-968d-02badf67b6f9`) lines 67-67 [crates/gcode/src/commands/graph/lifecycle.rs:67]
  - Signature: `impl std::error::Error for GraphSyncContractError {}`
  - Purpose: 'GraphSyncContractError' is a Rust error type that implements 'std::error::Error', indicating it represents failures in GraphSync contract validation or enforcement. [crates/gcode/src/commands/graph/lifecycle.rs:67]
- `format_success_text` (function) component `format_success_text [function]` (`14a613ca-e60f-5141-b5e0-cb157a7ca83d`) lines 69-76 [crates/gcode/src/commands/graph/lifecycle.rs:69-76]
  - Signature: `pub(super) fn format_success_text(output: &GraphLifecycleOutput) -> String {`
  - Purpose: Formats a success-status message by concatenating the action’s success prefix, the project ID, and the output summary into the string '"{prefix} for project {project_id}: {summary}"'. [crates/gcode/src/commands/graph/lifecycle.rs:69-76]
- `LifecycleBackend` (type) component `LifecycleBackend [type]` (`2d492478-1988-5e01-9da7-4dbc99adc638`) lines 78-84 [crates/gcode/src/commands/graph/lifecycle.rs:78-84]
  - Signature: `pub(super) trait LifecycleBackend {`
  - Purpose: Indexed type `LifecycleBackend` in `crates/gcode/src/commands/graph/lifecycle.rs`. [crates/gcode/src/commands/graph/lifecycle.rs:78-84]
- `CodeGraphLifecycleBackend` (class) component `CodeGraphLifecycleBackend [class]` (`4d7bf3ce-41fb-5d3a-95a5-c71856a19da3`) lines 86-86 [crates/gcode/src/commands/graph/lifecycle.rs:86]
  - Signature: `struct CodeGraphLifecycleBackend;`
  - Purpose: 'CodeGraphLifecycleBackend' is an empty struct type that serves as a backend handle or tag for code-graph lifecycle management. [crates/gcode/src/commands/graph/lifecycle.rs:86]
- `CodeGraphLifecycleBackend` (class) component `CodeGraphLifecycleBackend [class]` (`c5832706-13d5-584e-9bed-38536a1da44f`) lines 88-99 [crates/gcode/src/commands/graph/lifecycle.rs:88-99]
  - Signature: `impl LifecycleBackend for CodeGraphLifecycleBackend {`
  - Purpose: 'CodeGraphLifecycleBackend' is a 'LifecycleBackend' implementation that dispatches 'GraphLifecycleAction::Clear' to 'clear_project_graph(ctx)' and 'GraphLifecycleAction::Rebuild' to 'rebuild_project_graph(ctx)', returning the resulting 'GraphLifecycleOutput' as an 'anyhow::Result'. [crates/gcode/src/commands/graph/lifecycle.rs:88-99]
- `CodeGraphLifecycleBackend.run` (method) component `CodeGraphLifecycleBackend.run [method]` (`695f7fd4-361e-5210-a0b2-5129e506f4d3`) lines 89-98 [crates/gcode/src/commands/graph/lifecycle.rs:89-98]
  - Signature: `fn run(`
  - Purpose: Dispatches a 'GraphLifecycleAction' to either 'clear_project_graph(ctx)' or 'rebuild_project_graph(ctx)' and returns the resulting 'anyhow::Result<GraphLifecycleOutput>'. [crates/gcode/src/commands/graph/lifecycle.rs:89-98]
- `run_lifecycle_action_with_backend` (function) component `run_lifecycle_action_with_backend [function]` (`d1f7ee77-88a6-5ae8-a267-120a6efe9b93`) lines 101-115 [crates/gcode/src/commands/graph/lifecycle.rs:101-115]
  - Signature: `pub(super) fn run_lifecycle_action_with_backend(`
  - Purpose: Runs a lifecycle action through the provided backend, then prints the backend output as JSON in 'Json' mode or as success text followed by compact JSON in 'Text' mode. [crates/gcode/src/commands/graph/lifecycle.rs:101-115]
- `lifecycle_output` (function) component `lifecycle_output [function]` (`d5e3a602-cee7-596d-8bad-4eec33f4b381`) lines 117-129 [crates/gcode/src/commands/graph/lifecycle.rs:117-129]
  - Signature: `fn lifecycle_output(`
  - Purpose: Constructs a 'GraphLifecycleOutput' by deriving a text 'summary' from 'payload' via 'code_graph::extract_summary_text' with a fallback to 'payload.to_string()', then cloning 'ctx.project_id' and storing the supplied 'action' and original 'payload'. [crates/gcode/src/commands/graph/lifecycle.rs:117-129]
- `GraphFileSyncOutcome` (type) component `GraphFileSyncOutcome [type]` (`5a6558a1-f41d-5c2f-801e-781a9cedc834`) lines 131-138 [crates/gcode/src/commands/graph/lifecycle.rs:131-138]
  - Signature: `enum GraphFileSyncOutcome {`
  - Purpose: Indexed type `GraphFileSyncOutcome` in `crates/gcode/src/commands/graph/lifecycle.rs`. [crates/gcode/src/commands/graph/lifecycle.rs:131-138]
- `skipped_missing_indexed_file_payload` (function) component `skipped_missing_indexed_file_payload [function]` (`52ece424-9c84-5199-ac7d-5d3ff5d3322d`) lines 140-147 [crates/gcode/src/commands/graph/lifecycle.rs:140-147]
  - Signature: `pub(super) fn skipped_missing_indexed_file_payload(ctx: &Context, file_path: &str) -> Value {`
  - Purpose: Returns a JSON value describing a skipped file-processing event for a missing indexed file, including the current project ID, the file path, a '"skipped"' status, and the reason '"indexed_file_not_found"'. [crates/gcode/src/commands/graph/lifecycle.rs:140-147]
- `skipped_no_graph_facts_payload` (function) component `skipped_no_graph_facts_payload [function]` (`f6fb9a38-c7e7-538f-910b-c9aaf7cc197a`) lines 149-161 [crates/gcode/src/commands/graph/lifecycle.rs:149-161]
  - Signature: `pub(super) fn skipped_no_graph_facts_payload(ctx: &Context, file_path: &str) -> Value {`
  - Purpose: Builds and returns a JSON 'Value' marking the file as a successful skipped sync due to '"no_graph_facts"', including the project ID, file path, zeroed relationship/symbol counts, 'synced_files: 1', and a formatted summary string. [crates/gcode/src/commands/graph/lifecycle.rs:149-161]
- `has_no_graph_facts` (function) component `has_no_graph_facts [function]` (`a43cb306-e69a-52a2-8edd-1be74a962e82`) lines 163-165 [crates/gcode/src/commands/graph/lifecycle.rs:163-165]
  - Signature: `pub(super) fn has_no_graph_facts<I, D, C>(imports: &[I], definitions: &[D], calls: &[C]) -> bool {`
  - Purpose: Returns 'true' only when all three slices ('imports', 'definitions', and 'calls') are empty, indicating there are no graph facts present. [crates/gcode/src/commands/graph/lifecycle.rs:163-165]
- `sync_file_graph` (function) component `sync_file_graph [function]` (`a23f30e5-ed7a-5f1a-b189-db940072bad9`) lines 167-211 [crates/gcode/src/commands/graph/lifecycle.rs:167-211]
  - Signature: `fn sync_file_graph(`
  - Purpose: Synchronizes a single indexed file’s code graph by validating project/index state, recording a sync attempt, deleting graph data when the file has no imports/definitions/calls, otherwise syncing the file’s graph relationships without project-wide orphan cleanup, marking the file synced, and returning an outcome indicating skip or success. [crates/gcode/src/commands/graph/lifecycle.rs:167-211]
- `clear_project_graph` (function) component `clear_project_graph [function]` (`4825b611-0875-5fa0-af2e-f2af16d203d5`) lines 213-234 [crates/gcode/src/commands/graph/lifecycle.rs:213-234]
  - Signature: `fn clear_project_graph(ctx: &Context) -> anyhow::Result<GraphLifecycleOutput> {`
  - Purpose: Requires graph-read access, resets the project’s graph sync state in the database, clears the project’s graph projection, and returns a 'GraphLifecycleOutput' reporting success with the number of files marked pending. [crates/gcode/src/commands/graph/lifecycle.rs:213-234]
- `rebuild_project_graph` (function) component `rebuild_project_graph [function]` (`0daae913-bbc7-51cf-aa40-e6223b20d7fa`) lines 236-314 [crates/gcode/src/commands/graph/lifecycle.rs:236-314]
  - Signature: `fn rebuild_project_graph(ctx: &Context) -> anyhow::Result<GraphLifecycleOutput> {`
  - Purpose: Rebuilds the project’s code graph by iterating all indexed file paths, marking each sync attempt, loading file facts, syncing imports/definitions/calls into the graph, marking successful syncs, collecting per-file errors, and optionally running orphan cleanup before returning a 'GraphLifecycleOutput'. [crates/gcode/src/commands/graph/lifecycle.rs:236-314]
- `clear` (function) component `clear [function]` (`df581428-dbb1-5074-b8bd-7a28c79f67f0`) lines 316-323 [crates/gcode/src/commands/graph/lifecycle.rs:316-323]
  - Signature: `pub fn clear(ctx: &Context, format: Format) -> anyhow::Result<()> {`
  - Purpose: Invokes 'run_lifecycle_action_with_backend' to execute the 'GraphLifecycleAction::Clear' lifecycle operation against 'CodeGraphLifecycleBackend' using the provided 'ctx' and 'format', returning the resulting 'anyhow::Result<()>'. [crates/gcode/src/commands/graph/lifecycle.rs:316-323]
- `rebuild` (function) component `rebuild [function]` (`b016447a-9065-54a6-8a96-1c6c12ab8a50`) lines 325-332 [crates/gcode/src/commands/graph/lifecycle.rs:325-332]
  - Signature: `pub fn rebuild(ctx: &Context, format: Format) -> anyhow::Result<()> {`
  - Purpose: Invokes 'run_lifecycle_action_with_backend' to execute the 'GraphLifecycleAction::Rebuild' lifecycle action for the given 'Context' and 'Format' using 'CodeGraphLifecycleBackend', returning its 'anyhow::Result<()>'. [crates/gcode/src/commands/graph/lifecycle.rs:325-332]
- `cleanup_orphans` (function) component `cleanup_orphans [function]` (`d5560d58-e40c-579f-a5bc-54ef690f4a64`) lines 339-359 [crates/gcode/src/commands/graph/lifecycle.rs:339-359]
  - Signature: `pub fn cleanup_orphans(ctx: &Context, format: Format) -> anyhow::Result<()> {`
  - Purpose: Performs graph-read validation, deletes orphaned stale code-graph files and file-scoped graph nodes for the current project via 'cleanup_deleted_project_graph', and emits either JSON or text output summarizing the deletion counts. [crates/gcode/src/commands/graph/lifecycle.rs:339-359]
- `cleanup_deleted_project_graph` (function) component `cleanup_deleted_project_graph [function]` (`c4ad36b1-0fb2-5705-ae09-525c0925b01b`) lines 361-369 [crates/gcode/src/commands/graph/lifecycle.rs:361-369]
  - Signature: `pub(crate) fn cleanup_deleted_project_graph(`
  - Purpose: Opens a readonly database connection, loads the set of indexed file paths for the current project into a 'HashSet', and delegates to 'code_graph::cleanup_deleted_files' to remove graph entries for files no longer indexed, returning a 'GraphOrphanCleanup' result. [crates/gcode/src/commands/graph/lifecycle.rs:361-369]
- `sync_file` (function) component `sync_file [function]` (`a134a0d0-6853-5961-b973-f3d6727efa59`) lines 371-434 [crates/gcode/src/commands/graph/lifecycle.rs:371-434]
  - Signature: `pub fn sync_file(`
  - Purpose: Synchronizes a file’s code-index graph facts via 'sync_file_graph', then emits either a success JSON/text report with relationship and symbol counts or a skip payload when the file has no graph facts or is missing from the index. [crates/gcode/src/commands/graph/lifecycle.rs:371-434]

