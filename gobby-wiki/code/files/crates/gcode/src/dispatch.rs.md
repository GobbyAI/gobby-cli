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

`crates/gcode/src/dispatch.rs` exposes 16 indexed API symbols.

## How it fits

`crates/gcode/src/dispatch.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

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
| `codewiki_ai_options` | function | The 'codewiki_ai_options' function constructs and returns a 'commands::codewiki::CodewikiAiOptions' configuration struct by converting and mapping CLI arguments for routing, search depths, registers, and profile settings while initializing the verification model and API key fields as 'None'. [crates/gcode/src/dispatch.rs:124-142] |
| `dispatch_early_command` | function | The 'dispatch_early_command' function evaluates parsed CLI arguments to execute early-lifecycle commands—specifically project initialization ('Init'), contract schema output ('Contract'), or standalone setup configuration ('Setup')—returning 'Ok(true)' if one of these commands is successfully handled, or propagating an execution error. [crates/gcode/src/dispatch.rs:144-229] |
| `run_with_exit_code` | function | The 'run_with_exit_code' function executes the application's 'run' routine, returning 'std::process::ExitCode::SUCCESS' upon success, or formatting diagnostics and returning designated exit codes for downcastable 'GraphSyncContractError' and 'EmbeddingsDoctorExit' errors, otherwise printing the error and returning 'std::process::ExitCode::FAILURE'. [crates/gcode/src/dispatch.rs:231-257] |
| `run` | function | The 'run' function serves as the CLI's main entry point, parsing command-line arguments, initializing logging, dispatching uninitialized commands, resolving the project context, and delegating execution to specific subcommand handlers. [crates/gcode/src/dispatch.rs:259-624] |

