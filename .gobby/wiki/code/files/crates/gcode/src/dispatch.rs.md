---
title: crates/gcode/src/dispatch.rs
type: code_file
provenance:
- file: crates/gcode/src/dispatch.rs
  ranges:
  - 6-14
  - 16-28
  - 30-32
  - 34-39
  - 41-45
  - 47-90
  - 92-173
  - 175-201
  - 203-522
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/dispatch.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

`crates/gcode/src/dispatch.rs` exposes 9 indexed API symbols.
[crates/gcode/src/dispatch.rs:6-14]
[crates/gcode/src/dispatch.rs:16-28]
[crates/gcode/src/dispatch.rs:30-32]
[crates/gcode/src/dispatch.rs:34-39]
[crates/gcode/src/dispatch.rs:41-45]

## API Symbols

- `ensure_project_fresh` (function) component `ensure_project_fresh [function]` (`5f919b73-0a3c-5adc-b93f-9f0b96b8d9de`) lines 6-14 [crates/gcode/src/dispatch.rs:6-14]
  - Signature: `fn ensure_project_fresh(ctx: &config::Context, disabled: bool) -> anyhow::Result<()> {`
  - Purpose: Ensures project-scope freshness and warns if a busy status is detected, unless the disabled flag is true. [crates/gcode/src/dispatch.rs:6-14]
- `ensure_files_fresh` (function) component `ensure_files_fresh [function]` (`408ed3da-e4f8-55ca-89a6-7c3c3e37e0e7`) lines 16-28 [crates/gcode/src/dispatch.rs:16-28]
  - Signature: `fn ensure_files_fresh(`
  - Purpose: Indexed function `ensure_files_fresh` in `crates/gcode/src/dispatch.rs`. [crates/gcode/src/dispatch.rs:16-28]
- `ensure_file_fresh` (function) component `ensure_file_fresh [function]` (`deeb92ba-732c-5c22-9735-ed158c178c0e`) lines 30-32 [crates/gcode/src/dispatch.rs:30-32]
  - Signature: `fn ensure_file_fresh(ctx: &config::Context, disabled: bool, file: &str) -> anyhow::Result<()> {`
  - Purpose: Indexed function `ensure_file_fresh` in `crates/gcode/src/dispatch.rs`. [crates/gcode/src/dispatch.rs:30-32]
- `ensure_symbol_fresh` (function) component `ensure_symbol_fresh [function]` (`e4d587d4-4e76-5baf-a502-6612e009b54b`) lines 34-39 [crates/gcode/src/dispatch.rs:34-39]
  - Signature: `fn ensure_symbol_fresh(ctx: &config::Context, disabled: bool, id: &str) -> anyhow::Result<()> {`
  - Purpose: # Summary

Ensures a symbol is fresh and warns if the system is busy, unless the operation is disabled. [crates/gcode/src/dispatch.rs:34-39]
- `warn_if_busy` (function) component `warn_if_busy [function]` (`a99ed3f3-b60a-5894-afc7-f80b76deda10`) lines 41-45 [crates/gcode/src/dispatch.rs:41-45]
  - Signature: `fn warn_if_busy(ctx: &config::Context, status: freshness::FreshnessStatus) {`
  - Purpose: Prints a warning to stderr if the gcode index refresh was skipped due to an already-running refresh operation, unless quiet mode is enabled. [crates/gcode/src/dispatch.rs:41-45]
- `service_config_selection` (function) component `service_config_selection [function]` (`f3db92e1-b225-5ef1-9674-4a4a56395ebd`) lines 47-90 [crates/gcode/src/dispatch.rs:47-90]
  - Signature: `fn service_config_selection(command: &Command) -> config::ServiceConfigSelection {`
  - Purpose: Maps CLI command variants to their required backend service configurations, determining which services (FalkorDB, Qdrant, vector database, etc.) are needed for each command operation. [crates/gcode/src/dispatch.rs:47-90]
- `dispatch_early_command` (function) component `dispatch_early_command [function]` (`0783665a-0d72-5199-905c-7b1ff955da0a`) lines 92-173 [crates/gcode/src/dispatch.rs:92-173]
  - Signature: `fn dispatch_early_command<F>(`
  - Purpose: Dispatches early-stage CLI commands (Init, Contract, Setup) by pattern matching on command type and routing each to its corresponding handler, returning true if executed. [crates/gcode/src/dispatch.rs:92-173]
- `run_with_exit_code` (function) component `run_with_exit_code [function]` (`5e3c95b6-e1c2-581e-a6a0-0eb3016abc10`) lines 175-201 [crates/gcode/src/dispatch.rs:175-201]
  - Signature: `pub(crate) fn run_with_exit_code() -> std::process::ExitCode {`
  - Purpose: Wraps the `run()` function to convert its `Result` into a `std::process::ExitCode`, with specialized exit code handling for `GraphSyncContractError` and `EmbeddingsDoctorExit` error types. [crates/gcode/src/dispatch.rs:175-201]
- `run` (function) component `run [function]` (`351326c5-afa3-59cf-ae0a-9b4bcaaa0fa3`) lines 203-522 [crates/gcode/src/dispatch.rs:203-522]
  - Signature: `fn run() -> anyhow::Result<()> {`
  - Purpose: Orchestrates CLI argument parsing, dispatches early commands, resolves the application context with services, and routes execution to the appropriate command handler via pattern matching. [crates/gcode/src/dispatch.rs:203-522]

