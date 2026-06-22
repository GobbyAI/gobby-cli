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

## crates/gcode/src/dispatch

The dispatch module is the central routing layer for the `gcode` CLI. It translates a parsed `Cli` struct into executable work by deciding which services are required, configuring the stderr logger, and either handling a command immediately (before any project context is resolved) or delegating to a later stage that can depend on a fully loaded configuration. The two key public functions surfaced by the tests are `service_config_selection`, which maps each subcommand to the set of service configs it needs, and `dispatch_early_command`, which runs commands like `setup` that must execute before a project context is available tests.rs:4–8, tests.rs:37–65.

Logging configuration is handled through `stderr_log_level`, a small but well-tested function that enforces three modes: a default `Warn` floor when no override is given, promotion to an arbitrary `log::LevelFilter` when `RUST_LOG` (or an equivalent flag) supplies a level string, and an unconditional `Off` when the `--quiet` flag is active, regardless of any other level hint tests.rs:11–27. This layered priority ensures that machine-readable output modes and human-facing noise can be controlled independently.

Service config selection (`service_config_selection`) implements a demand-driven service model: lookup and navigation commands (`grep`, `tree`, `symbol-at`, `search-*`) resolve to `None`, skipping all service-config resolution entirely, while graph and AI commands request only the specific service slices they need tests.rs:67–83. A further routing rule verified by `codewiki_ai_options_routes_verify_profile_override` ensures that AI option subcommands honour a profile override flag tests.rs component `98191bc0`. This keeps startup cost proportional to actual command needs.

The module imports directly from the sibling `crate::cli` module (`Cli`, `effective_format`) and from a `config` module for `ServiceConfigSelection` tests.rs:1–3. The test suite drives all public entry points through `clap::Parser::try_parse_from`, making CLI argument strings the authoritative integration surface for this module.

| Public Symbol | Role |
|---|---|
| `service_config_selection(cmd)` | Maps a subcommand variant to the required `ServiceConfigSelection` |
| `dispatch_early_command(cli, fmt, cb)` | Runs context-free commands (e.g. `setup`) before project resolution |
| `stderr_log_level(quiet, level_str)` | Derives the effective `log::LevelFilter` from quiet flag and optional level hint |

| Test | What It Verifies |
|---|---|
| `stderr_logger_defaults_to_warnings_for_non_quiet_runs` | Default level is `Warn` tests.rs:11–13 |
| `stderr_logger_respects_plain_rust_log_level` | Explicit level string overrides default tests.rs:15–21 |
| `stderr_logger_uses_quiet_as_hard_mute` | `quiet=true` forces `Off` regardless of level hint tests.rs:23–25 |
| `setup_early_dispatch_uses_parsed_request_without_context` | `setup` subcommand dispatches without a resolved project tests.rs:28–65 |
| `lookup_commands_skip_service_config_resolution` | File/symbol lookup commands return `None` service selection tests.rs:67–83 |
| `graph_and_ai_commands_request_only_needed_services` | Graph/AI commands request only their required services |
| `codewiki_ai_options_routes_verify_profile_override` | AI option routes honour `--profile` override |
[crates/gcode/src/dispatch/tests.rs:5-9]
[crates/gcode/src/dispatch/tests.rs:12-14]
[crates/gcode/src/dispatch/tests.rs:17-22]
[crates/gcode/src/dispatch/tests.rs:25-27]
[crates/gcode/src/dispatch/tests.rs:30-70]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/gcode/src/dispatch/tests.rs\|crates/gcode/src/dispatch/tests.rs]] | `crates/gcode/src/dispatch/tests.rs` exposes 8 indexed API symbols. |

