---
title: crates/gcode/src/dispatch.rs
type: code_file
provenance:
- file: crates/gcode/src/dispatch.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/dispatch.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

`crates/gcode/src/dispatch.rs` exposes 15 indexed API symbols.

## How it fits

`crates/gcode/src/dispatch.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `StderrLogger` | class | 'StderrLogger' is an empty struct type declaration that serves as a named logger handle or marker type, with no fields or behavior specified in the provided source. [crates/gcode/src/dispatch.rs:8] |
| `StderrLogger::enabled` | method | Returns 'true' when the record’s 'log::Level' is less than or equal to the current global 'log::max_level()', otherwise 'false'. [crates/gcode/src/dispatch.rs:11-13] |
| `StderrLogger::log` | method | If the record’s metadata is enabled, it writes the record level and formatted arguments to standard error using 'eprintln!'. [crates/gcode/src/dispatch.rs:15-19] |
| `StderrLogger::flush` | method | 'flush' is a no-op method that takes '&self' and returns '()', performing no state changes or I/O. [crates/gcode/src/dispatch.rs:21] |
| `init_logger` | function | Initializes the global logger to 'STDERR_LOGGER' and sets the maximum log level based on 'quiet' and the optional 'RUST_LOG' environment variable. [crates/gcode/src/dispatch.rs:24-28] |
| `stderr_log_level` | function | Returns 'log::LevelFilter::Off' when 'quiet' is true, otherwise parses 'rust_log' as a 'LevelFilter' after trimming whitespace and falls back to 'log::LevelFilter::Warn' if absent or invalid. [crates/gcode/src/dispatch.rs:30-37] |
| `ensure_project_fresh` | function | If 'disabled' is false, it invokes 'freshness::ensure_fresh' with 'FreshnessScope::Project' on the given context and passes any returned warning to 'warn_if_busy', otherwise it returns 'Ok(())' immediately. [crates/gcode/src/dispatch.rs:39-47] |
| `ensure_files_fresh` | function | Calls 'freshness::ensure_fresh' on the provided file paths and passes any resulting busy warning to 'warn_if_busy' when freshness checks are enabled, otherwise returns 'Ok(())'. [crates/gcode/src/dispatch.rs:49-61] |
| `ensure_file_fresh` | function | Wraps 'file' in a single-element 'PathBuf' vector and delegates to 'ensure_files_fresh(ctx, disabled, ...)' to validate that one file is fresh, returning its 'anyhow::Result<()>'. [crates/gcode/src/dispatch.rs:63-65] |
| `ensure_symbol_fresh` | function | If 'disabled' is false, it calls 'freshness::ensure_symbol_fresh(ctx, id)' and passes the result to 'warn_if_busy(ctx, ...)', then returns 'Ok(())' regardless. [crates/gcode/src/dispatch.rs:67-72] |
| `warn_if_busy` | function | Prints a warning to stderr that the G-code index refresh is already running and the existing index will be used when 'status' is 'SkippedBusy' and 'ctx.quiet' is false. [crates/gcode/src/dispatch.rs:74-78] |
| `service_config_selection` | function | Returns the 'ServiceConfigSelection' variant required by a given 'Command' by pattern-matching the command and selecting the minimal service set needed for that operation, with 'SearchSymbol' further conditioned on 'with_graph'. [crates/gcode/src/dispatch.rs:80-122] |
| `dispatch_early_command` | function | 'dispatch_early_command' inspects 'cli.command' and, for early-exit commands ('Init', 'Contract', 'Setup'), either runs project initialization, prints the CLI contract, or constructs a 'StandaloneSetupRequest' from CLI options and passes it to 'setup_runner', returning 'Ok(true)' when handled. [crates/gcode/src/dispatch.rs:124-209] |
| `run_with_exit_code` | function | Runs 'run()' and converts its result into an 'ExitCode', returning 'SUCCESS' on 'Ok(())', printing and using specialized exit codes for 'GraphSyncContractError' and 'EmbeddingsDoctorExit' when present, and otherwise printing the error and returning 'FAILURE'. [crates/gcode/src/dispatch.rs:211-237] |
| `run` | function | Parses CLI arguments, initializes logging, computes the effective output format, runs any pre-context early commands, resolves project context with services, and then dispatches the requested subcommand to the appropriate handler or no-op for prehandled commands. [crates/gcode/src/dispatch.rs:239-601] |

