---
title: crates/gcode/src/commands/graph/lifecycle.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/graph/lifecycle.rs
  ranges:
  - 11-13
  - 15-53
  - 55-64
  - '66'
  - 68-75
  - 77-83
  - '85'
  - 87-98
  - 100-114
  - 116-128
  - 130-137
  - 139-146
  - 148-160
  - 162-164
  - 166-204
  - 206-227
  - 229-307
  - 309-316
  - 318-325
  - 327-390
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/graph/lifecycle.rs

Module: [[code/modules/crates/gcode/src/commands/graph|crates/gcode/src/commands/graph]]

## Purpose

This file implements the command-side lifecycle flow for code graphs: it defines `GraphSyncContractError` for JSON-formatted contract failures, helpers for success/error output shaping, and a `LifecycleBackend` abstraction with `CodeGraphLifecycleBackend` as the concrete dispatcher. The backend routes `GraphLifecycleAction` variants to clear, rebuild, or sync operations, while `run_lifecycle_action_with_backend` and related helpers package the result into either JSON or formatted text.
[crates/gcode/src/commands/graph/lifecycle.rs:11-13]
[crates/gcode/src/commands/graph/lifecycle.rs:15-53]
[crates/gcode/src/commands/graph/lifecycle.rs:16-27]
[crates/gcode/src/commands/graph/lifecycle.rs:29-40]
[crates/gcode/src/commands/graph/lifecycle.rs:42-44]

## API Symbols

- `GraphSyncContractError` (class) component `GraphSyncContractError [class]` (`f408e6ee-9e37-5222-9f4a-97e83ab4ef79`) lines 11-13 [crates/gcode/src/commands/graph/lifecycle.rs:11-13]
  - Signature: `pub struct GraphSyncContractError {`
  - Purpose: `GraphSyncContractError` is a Rust struct that encapsulates arbitrary error payloads as JSON `Value`s for GraphSync contract violations. [crates/gcode/src/commands/graph/lifecycle.rs:11-13]
- `GraphSyncContractError` (class) component `GraphSyncContractError [class]` (`6a10a7ef-2f67-5752-9496-a02b1c6e8878`) lines 15-53 [crates/gcode/src/commands/graph/lifecycle.rs:15-53]
  - Signature: `impl GraphSyncContractError {`
  - Purpose: `GraphSyncContractError` is an error type that constructs JSON-formatted error responses for graph synchronization contract failures (missing project indexing or indexed files) and provides methods for payload serialization and exit code retrieval. [crates/gcode/src/commands/graph/lifecycle.rs:15-53]
- `GraphSyncContractError.project_not_indexed` (method) component `GraphSyncContractError.project_not_indexed [method]` (`e61b355b-e387-5510-a122-2476709e1ca4`) lines 16-27 [crates/gcode/src/commands/graph/lifecycle.rs:16-27]
  - Signature: `pub(super) fn project_not_indexed(ctx: &Context, file_path: &str) -> Self {`
  - Purpose: Constructs and returns a Self instance containing a JSON error payload indicating the specified project is not indexed, including the project ID, file path, and explanatory error message. [crates/gcode/src/commands/graph/lifecycle.rs:16-27]
- `GraphSyncContractError.indexed_file_not_found` (method) component `GraphSyncContractError.indexed_file_not_found [method]` (`ae650cad-6cda-5fa3-9148-d5ebdc6ea6d6`) lines 29-40 [crates/gcode/src/commands/graph/lifecycle.rs:29-40]
  - Signature: `pub(super) fn indexed_file_not_found(ctx: &Context, file_path: &str) -> Self {`
  - Purpose: Creates an error response payload indicating that the indexed file at the specified path was not found for the given project. [crates/gcode/src/commands/graph/lifecycle.rs:29-40]
- `GraphSyncContractError.exit_code` (method) component `GraphSyncContractError.exit_code [method]` (`b21d67eb-1f56-54de-bcdf-0134c438955e`) lines 42-44 [crates/gcode/src/commands/graph/lifecycle.rs:42-44]
  - Signature: `pub fn exit_code(&self) -> u8 {`
  - Purpose: This method returns the `GRAPH_SYNC_CONTRACT_EXIT_CODE` constant as a `u8` exit code value. [crates/gcode/src/commands/graph/lifecycle.rs:42-44]
- `GraphSyncContractError.print` (method) component `GraphSyncContractError.print [method]` (`87a60057-f56e-55c4-8a92-504dddd268d9`) lines 46-48 [crates/gcode/src/commands/graph/lifecycle.rs:46-48]
  - Signature: `pub fn print(&self) -> anyhow::Result<()> {`
  - Purpose: This method serializes and outputs the instance's payload as JSON, returning an `anyhow::Result` to indicate success or error. [crates/gcode/src/commands/graph/lifecycle.rs:46-48]
- `GraphSyncContractError.payload` (method) component `GraphSyncContractError.payload [method]` (`8935ff8f-44f6-5ec6-adb0-7bfe253eed4c`) lines 50-52 [crates/gcode/src/commands/graph/lifecycle.rs:50-52]
  - Signature: `pub fn payload(&self) -> &Value {`
  - Purpose: Returns an immutable reference to the `payload` field of type `Value`. [crates/gcode/src/commands/graph/lifecycle.rs:50-52]
- `GraphSyncContractError` (class) component `GraphSyncContractError [class]` (`c43650c1-dd83-55e1-abde-3068f935b61c`) lines 55-64 [crates/gcode/src/commands/graph/lifecycle.rs:55-64]
  - Signature: `impl std::fmt::Display for GraphSyncContractError {`
  - Purpose: Implements the `Display` trait for `GraphSyncContractError` to format error messages by extracting an optional `"reason"` field from a JSON payload object, defaulting to `"graph_sync_contract_error"` if absent. [crates/gcode/src/commands/graph/lifecycle.rs:55-64]
- `GraphSyncContractError.fmt` (method) component `GraphSyncContractError.fmt [method]` (`7efe44a7-e662-5fe1-8572-35021f46ee22`) lines 56-63 [crates/gcode/src/commands/graph/lifecycle.rs:56-63]
  - Signature: `fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {`
  - Purpose: This method implements the `Display` formatter to output a graph sync-file contract error message, extracting a reason field from the payload object and defaulting to "graph_sync_contract_error" if not present. [crates/gcode/src/commands/graph/lifecycle.rs:56-63]
- `GraphSyncContractError` (class) component `GraphSyncContractError [class]` (`e3a73218-b774-5088-8fa2-bf7cb062a0e0`) lines 66-66 [crates/gcode/src/commands/graph/lifecycle.rs:66]
  - Signature: `impl std::error::Error for GraphSyncContractError {}`
  - Purpose: `GraphSyncContractError` implements the `std::error::Error` trait, making it a standard Rust error type for graph synchronization contract violations. [crates/gcode/src/commands/graph/lifecycle.rs:66]
- `format_success_text` (function) component `format_success_text [function]` (`7eb80600-b72c-54d5-8a48-5df3e060db3e`) lines 68-75 [crates/gcode/src/commands/graph/lifecycle.rs:68-75]
  - Signature: `pub(super) fn format_success_text(output: &GraphLifecycleOutput) -> String {`
  - Purpose: Constructs a formatted success message string by combining the `GraphLifecycleOutput`'s action success prefix, project ID, and summary into a templated format. [crates/gcode/src/commands/graph/lifecycle.rs:68-75]
- `LifecycleBackend` (type) component `LifecycleBackend [type]` (`4342ff37-f20b-5c4f-b35d-f3cd002c6de8`) lines 77-83 [crates/gcode/src/commands/graph/lifecycle.rs:77-83]
  - Signature: `pub(super) trait LifecycleBackend {`
  - Purpose: Indexed type `LifecycleBackend` in `crates/gcode/src/commands/graph/lifecycle.rs`. [crates/gcode/src/commands/graph/lifecycle.rs:77-83]
- `CodeGraphLifecycleBackend` (class) component `CodeGraphLifecycleBackend [class]` (`947a81f1-a4e7-5882-9300-39550e9e1ca6`) lines 85-85 [crates/gcode/src/commands/graph/lifecycle.rs:85]
  - Signature: `struct CodeGraphLifecycleBackend;`
  - Purpose: # Summary

`CodeGraphLifecycleBackend` is a unit struct serving as a backend abstraction for managing the lifecycle operations of code graphs. [crates/gcode/src/commands/graph/lifecycle.rs:85]
- `CodeGraphLifecycleBackend` (class) component `CodeGraphLifecycleBackend [class]` (`6a419f48-0344-5014-aa8c-c4aab948eb78`) lines 87-98 [crates/gcode/src/commands/graph/lifecycle.rs:87-98]
  - Signature: `impl LifecycleBackend for CodeGraphLifecycleBackend {`
  - Purpose: `CodeGraphLifecycleBackend` is a `LifecycleBackend` implementation that dispatches code graph lifecycle operations by pattern-matching on `GraphLifecycleAction` variants to either clear or rebuild the project graph. [crates/gcode/src/commands/graph/lifecycle.rs:87-98]
- `CodeGraphLifecycleBackend.run` (method) component `CodeGraphLifecycleBackend.run [method]` (`fa45bf46-0cc5-583c-915d-73a47381f4b4`) lines 88-97 [crates/gcode/src/commands/graph/lifecycle.rs:88-97]
  - Signature: `fn run(`
  - Purpose: # Summary

This method routes a `GraphLifecycleAction` enum variant to either clear or rebuild the project graph by delegating to the corresponding operation function. [crates/gcode/src/commands/graph/lifecycle.rs:88-97]
- `run_lifecycle_action_with_backend` (function) component `run_lifecycle_action_with_backend [function]` (`40b17f53-5fae-58a5-9895-e56ca7f153be`) lines 100-114 [crates/gcode/src/commands/graph/lifecycle.rs:100-114]
  - Signature: `pub(super) fn run_lifecycle_action_with_backend(`
  - Purpose: Executes a `GraphLifecycleAction` through a provided `LifecycleBackend` and outputs the result in either JSON format or formatted text with compact JSON payload based on the specified `Format`. [crates/gcode/src/commands/graph/lifecycle.rs:100-114]
- `lifecycle_output` (function) component `lifecycle_output [function]` (`c53a32d7-43a2-5c19-b3e5-3aafb3902d5d`) lines 116-128 [crates/gcode/src/commands/graph/lifecycle.rs:116-128]
  - Signature: `fn lifecycle_output(`
  - Purpose: This function constructs a `GraphLifecycleOutput` struct containing a lifecycle action, its associated project ID, and an extracted or stringified summary of the provided payload. [crates/gcode/src/commands/graph/lifecycle.rs:116-128]
- `GraphFileSyncOutcome` (type) component `GraphFileSyncOutcome [type]` (`072f681f-19cb-55b6-b525-dd0ea38472ac`) lines 130-137 [crates/gcode/src/commands/graph/lifecycle.rs:130-137]
  - Signature: `enum GraphFileSyncOutcome {`
  - Purpose: Indexed type `GraphFileSyncOutcome` in `crates/gcode/src/commands/graph/lifecycle.rs`. [crates/gcode/src/commands/graph/lifecycle.rs:130-137]
- `skipped_missing_indexed_file_payload` (function) component `skipped_missing_indexed_file_payload [function]` (`430cb271-d063-54c4-8bed-9d55ac16e6d0`) lines 139-146 [crates/gcode/src/commands/graph/lifecycle.rs:139-146]
  - Signature: `pub(super) fn skipped_missing_indexed_file_payload(ctx: &Context, file_path: &str) -> Value {`
  - Purpose: Returns a JSON value marking the given file path as 'skipped' for the current project with reason 'indexed_file_not_found'. [crates/gcode/src/commands/graph/lifecycle.rs:139-146]
- `skipped_no_graph_facts_payload` (function) component `skipped_no_graph_facts_payload [function]` (`805d6a74-75a2-58c9-8312-701a4294d130`) lines 148-160 [crates/gcode/src/commands/graph/lifecycle.rs:148-160]
  - Signature: `pub(super) fn skipped_no_graph_facts_payload(ctx: &Context, file_path: &str) -> Value {`
  - Purpose: Returns a JSON 'Value' marking the file sync as successfully skipped for 'no_graph_facts', including the project ID, file path, zero written symbols/relationships, one synced file, and a formatted summary message. [crates/gcode/src/commands/graph/lifecycle.rs:148-160]
- `has_no_graph_facts` (function) component `has_no_graph_facts [function]` (`ed99b437-50e8-50cc-80ee-6bdd442fd1d2`) lines 162-164 [crates/gcode/src/commands/graph/lifecycle.rs:162-164]
  - Signature: `pub(super) fn has_no_graph_facts<I, D, C>(imports: &[I], definitions: &[D], calls: &[C]) -> bool {`
  - Purpose: Indexed function `has_no_graph_facts` in `crates/gcode/src/commands/graph/lifecycle.rs`. [crates/gcode/src/commands/graph/lifecycle.rs:162-164]
- `sync_file_graph` (function) component `sync_file_graph [function]` (`4ff376f4-d80f-5b7f-b3b2-e61a4cd1e71b`) lines 166-204 [crates/gcode/src/commands/graph/lifecycle.rs:166-204]
  - Signature: `fn sync_file_graph(`
  - Purpose: Indexed function `sync_file_graph` in `crates/gcode/src/commands/graph/lifecycle.rs`. [crates/gcode/src/commands/graph/lifecycle.rs:166-204]
- `clear_project_graph` (function) component `clear_project_graph [function]` (`eccf3bf4-37e8-5b8f-a537-d5310af2cbc5`) lines 206-227 [crates/gcode/src/commands/graph/lifecycle.rs:206-227]
  - Signature: `fn clear_project_graph(ctx: &Context) -> anyhow::Result<GraphLifecycleOutput> {`
  - Purpose: Indexed function `clear_project_graph` in `crates/gcode/src/commands/graph/lifecycle.rs`. [crates/gcode/src/commands/graph/lifecycle.rs:206-227]
- `rebuild_project_graph` (function) component `rebuild_project_graph [function]` (`1312cd99-2d27-5fac-b353-a18cb2ce9ba6`) lines 229-307 [crates/gcode/src/commands/graph/lifecycle.rs:229-307]
  - Signature: `fn rebuild_project_graph(ctx: &Context) -> anyhow::Result<GraphLifecycleOutput> {`
  - Purpose: Indexed function `rebuild_project_graph` in `crates/gcode/src/commands/graph/lifecycle.rs`. [crates/gcode/src/commands/graph/lifecycle.rs:229-307]
- `clear` (function) component `clear [function]` (`fa4bcfeb-225c-50e9-adec-d64525c4b162`) lines 309-316 [crates/gcode/src/commands/graph/lifecycle.rs:309-316]
  - Signature: `pub fn clear(ctx: &Context, format: Format) -> anyhow::Result<()> {`
  - Purpose: Indexed function `clear` in `crates/gcode/src/commands/graph/lifecycle.rs`. [crates/gcode/src/commands/graph/lifecycle.rs:309-316]
- `rebuild` (function) component `rebuild [function]` (`ec55216b-5ceb-531f-8f67-7acaadf762e4`) lines 318-325 [crates/gcode/src/commands/graph/lifecycle.rs:318-325]
  - Signature: `pub fn rebuild(ctx: &Context, format: Format) -> anyhow::Result<()> {`
  - Purpose: Indexed function `rebuild` in `crates/gcode/src/commands/graph/lifecycle.rs`. [crates/gcode/src/commands/graph/lifecycle.rs:318-325]
- `sync_file` (function) component `sync_file [function]` (`39f592a9-5a73-58fc-afd8-f179f4e324ff`) lines 327-390 [crates/gcode/src/commands/graph/lifecycle.rs:327-390]
  - Signature: `pub fn sync_file(`
  - Purpose: Indexed function `sync_file` in `crates/gcode/src/commands/graph/lifecycle.rs`. [crates/gcode/src/commands/graph/lifecycle.rs:327-390]

