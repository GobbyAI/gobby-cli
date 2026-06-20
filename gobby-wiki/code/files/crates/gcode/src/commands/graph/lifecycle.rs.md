---
title: crates/gcode/src/commands/graph/lifecycle.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/graph/lifecycle.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/graph/lifecycle.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

`crates/gcode/src/commands/graph/lifecycle.rs` exposes 25 indexed API symbols.

## How it fits

`crates/gcode/src/commands/graph/lifecycle.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `GraphSyncContractError` | class | 'GraphSyncContractError' is a Rust struct that encapsulates a 'serde_json::Value' payload representing contract error data. [crates/gcode/src/commands/graph/lifecycle.rs:12-14] |
| `GraphSyncContractError::project_not_indexed` | method | Constructs and returns a failure response payload for a non-indexed project, embedding the current 'project_id', the given 'file_path', an '"error"' status, the '"project_not_indexed"' reason, and a formatted message stating that the project is not indexed. [crates/gcode/src/commands/graph/lifecycle.rs:17-28] |
| `GraphSyncContractError::indexed_file_not_found` | method | Constructs an error response payload with 'success: false', the current 'project_id', the missing 'file_path', status '"error"', reason '"indexed_file_not_found"', and a formatted message stating the indexed file was not found for the project. [crates/gcode/src/commands/graph/lifecycle.rs:30-41] |
| `GraphSyncContractError::exit_code` | method | Returns the 'GRAPH_SYNC_CONTRACT_EXIT_CODE' constant as a 'u8' exit code. [crates/gcode/src/commands/graph/lifecycle.rs:43-45] |
| `GraphSyncContractError::print` | method | Serializes and prints 'self.payload' as JSON by delegating to 'output::print_json(&self.payload)', returning an 'anyhow::Result<()>'. [crates/gcode/src/commands/graph/lifecycle.rs:47-49] |
| `GraphSyncContractError::payload` | method | Returns an immutable reference to the method’s stored 'serde_json::Value' payload. [crates/gcode/src/commands/graph/lifecycle.rs:51-53] |
| `GraphSyncContractError::fmt` | method | Formats the value as 'graph sync-file contract error: {reason}', where 'reason' is read from 'self.payload["reason"]' as a string or defaults to 'graph_sync_contract_error' if absent or non-string. [crates/gcode/src/commands/graph/lifecycle.rs:57-64] |
| `format_success_text` | function | Formats a success message string by concatenating the action’s success prefix, the project ID, and the output summary in the form '"<prefix> for project <project_id>: <summary>"'. [crates/gcode/src/commands/graph/lifecycle.rs:69-76] |
| `LifecycleBackend` | type | Indexed type `LifecycleBackend` in `crates/gcode/src/commands/graph/lifecycle.rs`. [crates/gcode/src/commands/graph/lifecycle.rs:78-84] |
| `CodeGraphLifecycleBackend` | class | 'CodeGraphLifecycleBackend' is a backend abstraction for managing the lifecycle of a code graph, represented here as an opaque 'struct' with no exposed fields or methods. [crates/gcode/src/commands/graph/lifecycle.rs:86] |
| `CodeGraphLifecycleBackend::run` | method | Dispatches 'GraphLifecycleAction::Clear' to 'clear_project_graph(ctx)' and 'GraphLifecycleAction::Rebuild' to 'rebuild_project_graph(ctx)', returning the resulting 'anyhow::Result<GraphLifecycleOutput>'. [crates/gcode/src/commands/graph/lifecycle.rs:89-98] |
| `run_lifecycle_action_with_backend` | function | Runs a lifecycle action via the provided backend, then renders the result as JSON only for 'Format::Json' or prints success text plus compact JSON payload for 'Format::Text', propagating any backend or output errors. [crates/gcode/src/commands/graph/lifecycle.rs:101-115] |
| `lifecycle_output` | function | 'lifecycle_output' constructs a 'GraphLifecycleOutput' by cloning the current 'project_id', preserving the supplied 'action' and 'payload', and deriving 'summary' from 'code_graph::extract_summary_text(&payload)' or falling back to 'payload.to_string()'. [crates/gcode/src/commands/graph/lifecycle.rs:117-129] |
| `GraphFileSyncOutcome` | type | Indexed type `GraphFileSyncOutcome` in `crates/gcode/src/commands/graph/lifecycle.rs`. [crates/gcode/src/commands/graph/lifecycle.rs:131-140] |
| `skipped_missing_indexed_file_payload` | function | Returns a JSON 'Value' reporting a successful but skipped graph-sync for a missing indexed file, including zeroed sync counters, an 'indexed_file_not_found' reason, and an optional 'projection_reconcile_failed' error aggregated from any reconcile failures. [crates/gcode/src/commands/graph/lifecycle.rs:142-179] |
| `skipped_no_graph_facts_payload` | function | Returns a JSON 'Value' marking the given 'file_path' as a successful skipped graph-sync operation for the current project, with fixed counters ('synced_files' 1, 'synced_symbols' 0, 'skipped_files' 1, 'failed_files' 0, 'relationships_written' 0), 'reason' set to '"no_graph_facts"', 'degraded' false, 'error' null, and a formatted summary string. [crates/gcode/src/commands/graph/lifecycle.rs:181-197] |
| `has_no_graph_facts` | function | Returns 'true' only when all three slices, 'imports', 'definitions', and 'calls', are empty, indicating there are no graph facts present. [crates/gcode/src/commands/graph/lifecycle.rs:199-201] |
| `sync_file_graph` | function | Synchronizes a single file’s code graph from indexed database facts into the in-memory graph after verifying the project is indexed and graph reads are permitted, handling missing or fact-less files by skipping or deleting their graph records, then marking the file as synced and returning a 'GraphFileSyncOutcome'. [crates/gcode/src/commands/graph/lifecycle.rs:203-249] |
| `clear_project_graph` | function | Requires graph-read access, resets the project’s graph-sync state in the database, clears the project’s code graph projection, and returns a 'GraphLifecycleOutput' reporting success with the number of files marked pending. [crates/gcode/src/commands/graph/lifecycle.rs:251-274] |
| `rebuild_project_graph` | function | Rebuilds the project graph by requiring graph reads, scanning all indexed file paths, and then for each file attempting a sync that either reconciles deletions, removes graph state when no graph facts exist, or updates the graph and database while collecting per-file sync failures and counters. [crates/gcode/src/commands/graph/lifecycle.rs:276-387] |
| `clear` | function | Invokes 'run_lifecycle_action_with_backend' to execute the 'GraphLifecycleAction::Clear' operation on the given 'Context' using 'CodeGraphLifecycleBackend', returning its 'anyhow::Result<()>'. [crates/gcode/src/commands/graph/lifecycle.rs:389-396] |
| `rebuild` | function | Invokes 'run_lifecycle_action_with_backend' to execute the 'GraphLifecycleAction::Rebuild' lifecycle operation on 'ctx' using the provided 'format' and the 'CodeGraphLifecycleBackend', returning its 'anyhow::Result<()>'. [crates/gcode/src/commands/graph/lifecycle.rs:398-405] |
| `cleanup_orphans` | function | Requires graph-read access, deletes stale code-graph files and file-scoped graph nodes for the current project via 'cleanup_deleted_project_graph', and emits either JSON or text plus compact JSON with the deletion counts. [crates/gcode/src/commands/graph/lifecycle.rs:412-432] |
| `cleanup_deleted_project_graph` | function | Connects to the database in read-only mode, loads the project’s indexed file paths into a 'HashSet', and delegates to 'code_graph::cleanup_deleted_files' to produce a 'GraphOrphanCleanup' for files that have been deleted. [crates/gcode/src/commands/graph/lifecycle.rs:434-442] |

_1 more symbol(s) not shown — run `gcode outline crates/gcode/src/commands/graph/lifecycle.rs` for the full list._

