---
title: crates/gcode/src/dispatch
type: code_module
provenance:
- file: crates/gcode/src/dispatch/tests.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/dispatch

Parent: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

The `dispatch` module is responsible for turning parsed CLI commands into early execution decisions, service-configuration requirements, and stderr logging behavior. Its tests exercise dispatch internals via `use super::*`, while collaborating with CLI parsing and format resolution through `crate::cli::{Cli, effective_format}` and `clap::Parser` (`crates/gcode/src/dispatch/tests.rs:1-3`).

A key flow is service selection from parsed commands: `services_for` parses `gcode` arguments into `Cli`, then delegates to `service_config_selection(&cli.command)` (`crates/gcode/src/dispatch/tests.rs:5-9`). Lookup-style commands such as `grep`, `tree`, `symbol-at`, `search-content`, `search-text`, and `search-symbol` are expected to skip service configuration resolution (`crates/gcode/src/dispatch/tests.rs:64-75`).

Early dispatch is also covered for `setup`: the test builds a parsed CLI request with project, database, schema-default, overwrite, standalone, and embedding API options, then verifies `dispatch_early_command` invokes the supplied handler without requiring full project context (`crates/gcode/src/dispatch/tests.rs:31-62`). Logging policy is compact: non-quiet runs default to warnings, explicit Rust log levels are respected, and `quiet` acts as a hard mute (`crates/gcode/src/dispatch/tests.rs:11-29`).

| Public/test symbol | Responsibility |
| --- | --- |
| `services_for` | Parses CLI args and returns `ServiceConfigSelection` (`crates/gcode/src/dispatch/tests.rs:5-9`) |
| `stderr_logger_defaults_to_warnings_for_non_quiet_runs` | Verifies default stderr level is `Warn` (`crates/gcode/src/dispatch/tests.rs:11-14`) |
| `stderr_logger_respects_plain_rust_log_level` | Verifies explicit log level parsing (`crates/gcode/src/dispatch/tests.rs:16-23`) |
| `stderr_logger_uses_quiet_as_hard_mute` | Verifies quiet maps to `Off` (`crates/gcode/src/dispatch/tests.rs:25-28`) |
| `setup_early_dispatch_uses_parsed_request_without_context` | Verifies early setup dispatch uses the parsed request directly (`crates/gcode/src/dispatch/tests.rs:31-62`) |
| `lookup_commands_skip_service_config_resolution` | Verifies lookup commands avoid service config resolution (`crates/gcode/src/dispatch/tests.rs:64-75`) |

| CLI surface | Dispatch behavior covered |
| --- | --- |
| `setup --standalone --database-url ... --overwrite-code-index --embedding-api-base ...` | Early-dispatched from parsed request without resolving project context (`crates/gcode/src/dispatch/tests.rs:35-62`) |
| `grep -F`, `tree`, `symbol-at`, `search-content`, `search-text`, `search-symbol` | Treated as lookup commands that skip service config resolution (`crates/gcode/src/dispatch/tests.rs:66-75`) |
| `--project` | Parsed into the setup CLI used for early dispatch (`crates/gcode/src/dispatch/tests.rs:35-38`) |

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/dispatch/tests.rs\|crates/gcode/src/dispatch/tests.rs]] | `crates/gcode/src/dispatch/tests.rs` exposes 8 indexed API symbols. |

