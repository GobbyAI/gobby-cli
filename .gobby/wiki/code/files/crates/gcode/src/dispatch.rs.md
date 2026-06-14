---
title: crates/gcode/src/dispatch.rs
type: code_file
provenance:
- file: crates/gcode/src/dispatch.rs
  ranges:
  - '8'
  - 10-22
  - 24-28
  - 30-37
  - 39-47
  - 49-61
  - 63-65
  - 67-72
  - 74-78
  - 80-123
  - 125-206
  - 208-234
  - 236-558
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/dispatch.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

This file is the CLI dispatch layer for `gcode`: it sets up stderr logging, checks index freshness, chooses the minimal service configuration for each command, and routes parsed commands to their handlers. `StderrLogger` provides a simple `log::Log` implementation that prints enabled messages as `LEVEL: message` to stderr, while `init_logger` and `stderr_log_level` control global verbosity from `quiet` and `RUST_LOG`. The freshness helpers wrap project, file, and symbol refresh checks and surface a non-fatal warning when the index is already busy. `dispatch_early_command` handles startup-style commands that can exit before full context resolution, `run_with_exit_code` translates `run()` results into process exit codes with specialized error reporting, and `run` ties everything together by parsing the CLI, initializing output, resolving context, and dispatching the selected subcommand.
[crates/gcode/src/dispatch.rs:8]
[crates/gcode/src/dispatch.rs:10-22]
[crates/gcode/src/dispatch.rs:11-13]
[crates/gcode/src/dispatch.rs:15-19]
[crates/gcode/src/dispatch.rs:21]

## API Symbols

- `StderrLogger` (class) component `StderrLogger [class]` (`2d71eb13-2869-5f4a-920c-da64de430437`) lines 8-8 [crates/gcode/src/dispatch.rs:8]
  - Signature: `struct StderrLogger;`
  - Purpose: 'StderrLogger' is a zero-sized struct that serves as a logger implementation or handle for emitting log output to standard error. [crates/gcode/src/dispatch.rs:8]
- `StderrLogger` (class) component `StderrLogger [class]` (`a777337a-8ad5-5616-8c21-649766f70339`) lines 10-22 [crates/gcode/src/dispatch.rs:10-22]
  - Signature: `impl log::Log for StderrLogger {`
  - Purpose: 'StderrLogger' is a 'log::Log' implementation that emits enabled log records to standard error in the format 'LEVEL: message' and performs no flush action. [crates/gcode/src/dispatch.rs:10-22]
- `StderrLogger.enabled` (method) component `StderrLogger.enabled [method]` (`2383f1c4-c756-5611-8934-d7cb282e6e22`) lines 11-13 [crates/gcode/src/dispatch.rs:11-13]
  - Signature: `fn enabled(&self, metadata: &log::Metadata<'_>) -> bool {`
  - Purpose: Returns 'true' when the record’s log level is at or below the current global maximum log level, and 'false' otherwise. [crates/gcode/src/dispatch.rs:11-13]
- `StderrLogger.log` (method) component `StderrLogger.log [method]` (`396f55d1-22db-5f92-9b10-c8908210073f`) lines 15-19 [crates/gcode/src/dispatch.rs:15-19]
  - Signature: `fn log(&self, record: &log::Record<'_>) {`
  - Purpose: Writes an enabled log record to standard error as '"<level>: <formatted message>"' using 'eprintln!', and ignores records that fail 'self.enabled(record.metadata())'. [crates/gcode/src/dispatch.rs:15-19]
- `StderrLogger.flush` (method) component `StderrLogger.flush [method]` (`1bbd68fd-8e89-55da-9283-3e831c777121`) lines 21-21 [crates/gcode/src/dispatch.rs:21]
  - Signature: `fn flush(&self) {}`
  - Purpose: 'flush' is a no-op instance method that takes an immutable reference to 'self' and performs no side effects. [crates/gcode/src/dispatch.rs:21]
- `init_logger` (function) component `init_logger [function]` (`ab252d2e-fc3b-5ad8-b1f0-b7241e7efa2f`) lines 24-28 [crates/gcode/src/dispatch.rs:24-28]
  - Signature: `fn init_logger(quiet: bool) {`
  - Purpose: Initializes the global logger by installing 'STDERR_LOGGER' and setting the maximum log level from 'quiet' plus the optional 'RUST_LOG' environment variable. [crates/gcode/src/dispatch.rs:24-28]
- `stderr_log_level` (function) component `stderr_log_level [function]` (`370f2735-75cf-5a9e-ab25-f05cb782fe67`) lines 30-37 [crates/gcode/src/dispatch.rs:30-37]
  - Signature: `fn stderr_log_level(quiet: bool, rust_log: Option<&str>) -> log::LevelFilter {`
  - Purpose: Returns 'Off' when 'quiet' is true; otherwise it tries to parse 'rust_log' as a 'log::LevelFilter' after trimming whitespace and falls back to 'Warn' if parsing fails or the value is absent. [crates/gcode/src/dispatch.rs:30-37]
- `ensure_project_fresh` (function) component `ensure_project_fresh [function]` (`bc6b40ac-1c6f-5750-b1a5-34a9f37b8158`) lines 39-47 [crates/gcode/src/dispatch.rs:39-47]
  - Signature: `fn ensure_project_fresh(ctx: &config::Context, disabled: bool) -> anyhow::Result<()> {`
  - Purpose: If freshness checks are not disabled, it invokes 'freshness::ensure_fresh' for 'FreshnessScope::Project' and passes any returned busy warning to 'warn_if_busy', then returns 'Ok(())'. [crates/gcode/src/dispatch.rs:39-47]
- `ensure_files_fresh` (function) component `ensure_files_fresh [function]` (`029a8312-9dd7-5dc3-a5bb-b810ceecb892`) lines 49-61 [crates/gcode/src/dispatch.rs:49-61]
  - Signature: `fn ensure_files_fresh(`
  - Purpose: Calls 'freshness::ensure_fresh' for the given file paths and passes any resulting busy warning to 'warn_if_busy' when 'disabled' is false, otherwise returns 'Ok(())' without checking freshness. [crates/gcode/src/dispatch.rs:49-61]
- `ensure_file_fresh` (function) component `ensure_file_fresh [function]` (`998c5487-2667-5815-bdbd-1f410e0c2781`) lines 63-65 [crates/gcode/src/dispatch.rs:63-65]
  - Signature: `fn ensure_file_fresh(ctx: &config::Context, disabled: bool, file: &str) -> anyhow::Result<()> {`
  - Purpose: 'ensure_file_fresh' wraps 'ensure_files_fresh' to validate freshness for a single file path by converting 'file' into a 'PathBuf' and passing it in a one-element vector, returning the resulting 'anyhow::Result<()>'. [crates/gcode/src/dispatch.rs:63-65]
- `ensure_symbol_fresh` (function) component `ensure_symbol_fresh [function]` (`eec2bd7d-b774-5d4f-ba03-72ca48b941da`) lines 67-72 [crates/gcode/src/dispatch.rs:67-72]
  - Signature: `fn ensure_symbol_fresh(ctx: &config::Context, disabled: bool, id: &str) -> anyhow::Result<()> {`
  - Purpose: Returns 'Ok(())' after, when 'disabled' is false, invoking 'freshness::ensure_symbol_fresh(ctx, id)?' and passing its result to 'warn_if_busy(ctx, ...)', otherwise it no-ops. [crates/gcode/src/dispatch.rs:67-72]
- `warn_if_busy` (function) component `warn_if_busy [function]` (`842ac6aa-35d2-5a1b-b8bd-f032a923d79f`) lines 74-78 [crates/gcode/src/dispatch.rs:74-78]
  - Signature: `fn warn_if_busy(ctx: &config::Context, status: freshness::FreshnessStatus) {`
  - Purpose: 'warn_if_busy' emits a stderr warning that the gcode index refresh is already running and the existing index will be used when 'status' is 'SkippedBusy' and the context is not quiet. [crates/gcode/src/dispatch.rs:74-78]
- `service_config_selection` (function) component `service_config_selection [function]` (`9d1a225e-8c4f-53b5-ba2f-eba4be26d2cc`) lines 80-123 [crates/gcode/src/dispatch.rs:80-123]
  - Signature: `fn service_config_selection(command: &Command) -> config::ServiceConfigSelection {`
  - Purpose: 'service_config_selection' maps a 'Command' variant to the minimal 'ServiceConfigSelection' needed for that operation, enabling all services for 'Index', a fixed 'falkordb'/'qdrant' subset for 'Status', graph-related commands to use 'falkordb_only', vector commands to use 'vectors', search commands to use 'hybrid_search', 'SearchSymbol' to choose 'falkordb_only' or 'database_only' based on 'with_graph', and all remaining commands to use 'database_only'. [crates/gcode/src/dispatch.rs:80-123]
- `dispatch_early_command` (function) component `dispatch_early_command [function]` (`4c5d2289-f073-5c8c-8abe-ac9ea025d43d`) lines 125-206 [crates/gcode/src/dispatch.rs:125-206]
  - Signature: `fn dispatch_early_command<F>(`
  - Purpose: 'dispatch_early_command' inspects 'cli.command' and immediately handles early-exit commands like 'init', 'contract', and 'setup' by performing the corresponding side effects and returning 'Ok(true)', otherwise returning 'Ok(false)' so normal command dispatch can continue. [crates/gcode/src/dispatch.rs:125-206]
- `run_with_exit_code` (function) component `run_with_exit_code [function]` (`6e24412f-9c28-5c50-8b1c-fb4912a11590`) lines 208-234 [crates/gcode/src/dispatch.rs:208-234]
  - Signature: `pub(crate) fn run_with_exit_code() -> std::process::ExitCode {`
  - Purpose: 'run_with_exit_code' executes 'run()', returns 'ExitCode::SUCCESS' on success, and on error prints specialized diagnostics for 'GraphSyncContractError' or 'EmbeddingsDoctorExit' before returning their mapped exit codes, otherwise logs the error and returns 'ExitCode::FAILURE'. [crates/gcode/src/dispatch.rs:208-234]
- `run` (function) component `run [function]` (`4a61f40b-a283-5ffb-a53e-5a742cabacfd`) lines 236-558 [crates/gcode/src/dispatch.rs:236-558]
  - Signature: `fn run() -> anyhow::Result<()> {`
  - Purpose: Parses the CLI, initializes logging and output format, optionally handles early commands before context resolution, resolves a project/service context, and dispatches the selected subcommand to its corresponding handler or no-op path. [crates/gcode/src/dispatch.rs:236-558]

