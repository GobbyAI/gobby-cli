---
title: crates/ghook
type: code_module
provenance:
- file: crates/ghook/schemas/diagnose-output.v2.schema.json
- file: crates/ghook/schemas/inbox-envelope.v1.schema.json
- file: crates/ghook/src/action.rs
- file: crates/ghook/src/args.rs
- file: crates/ghook/src/cli_config.rs
- file: crates/ghook/src/detach.rs
- file: crates/ghook/src/diagnose.rs
- file: crates/ghook/src/dispatch.rs
- file: crates/ghook/src/envelope.rs
- file: crates/ghook/src/json_value.rs
- file: crates/ghook/src/main.rs
- file: crates/ghook/src/output.rs
- file: crates/ghook/src/planned_shutdown.rs
- file: crates/ghook/src/runtime.rs
- file: crates/ghook/src/source.rs
- file: crates/ghook/src/statusline.rs
- file: crates/ghook/src/terminal_context.rs
- file: crates/ghook/src/transport.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/ghook

Parent: [[code/modules/crates|crates]]

## Overview

## crates/ghook

`ghook` is the Git-hook client binary that bridges AI coding-assistant CLIs to the Gobby daemon. It is invoked directly by hook scripts installed into a repository and is responsible for the full lifecycle of a single hook event: detecting which CLI fired the hook, capturing terminal context, building and validating a JSON envelope, dispatching it to the local daemon, interpreting the daemon's response, and emitting the exit code or JSON payload that the CLI expects. The crate is split into two child modules — `schemas`, which hosts versioned JSON Schema files used for contract validation, and `src`, which contains all Rust logic.

### CLI Registry and Criticality

`CliConfig` (component `dfe7d451`) is the central registry that maps a CLI name to its hook grammar and criticality rules. `CliConfig::for_cli` returns `None` for unrecognised CLIs; `CliConfig::for_dispatch` falls back to Claude semantics so that unknown callers still get a well-formed dispatch. `CliConfig::is_critical_hook` decides whether a failure should block the AI tool entirely (exit 2) or merely emit JSON feedback.

| CLI | Critical hooks | Hook name style | Notes |
|---|---|---|---|
| `claude` | `session_start` (when terminal context enabled) | snake_case | Hard-stop exits 2 |
| `codex` | `pre_tool_use` excluded without terminal context | snake_case | JSON parse errors exit 1 |
| `gemini` | varies | snake_case | JSON parse errors exit 1 |
| `grok` | `session_start` (terminal context) | native snake_case | Non-stop blocks stay JSON |
| `droid` | none | PascalCase preserved | Recognised; no critical hooks |

### Hook Dispatch Flow

The top-level `handle` / `handle_with` functions (components `4e51d57c`, `e54362c6`) orchestrate dispatch. `detect_source` (component `32182b88`) reads environment variables to determine which AI CLI owns the invocation, respecting an override only for Claude. `build_dispatch_envelope` (component `cedf4a3a`) assembles the `Envelope` struct (`134b0274`) — which includes `hook_type`, `source`, `critical`, session headers (`X-Gobby-Project-Id`, `X-Gobby-Session-Id`), and an optional `terminal_context` block drawn from tmux environment variables. The `terminal_context` module's `capture` / `inject` functions (`032ab45d`, `d242772e`) populate tmux pane, socket-path, parent PID, and TTY fields only for hooks where it is enabled. The completed envelope is then serialised and handed to `post_to_daemon_best_effort` (`64d25050`) which calls `enqueue_to` / `post_and_cleanup` (`6b11eb8c`, `e58a7860`) to atomically write the envelope to an inbox directory before attempting an HTTP POST to the daemon.

### Response Interpretation and Action Emission

After receiving a daemon response, `action_from_success_response` (`19b8fd80`) converts the body into a `HookAction` (`0f8bb650`). Specific rules handle each CLI's conventions: a `stop` / `STOP` decision field triggers exit 2 for critical hooks (`02f0d3f1`, `ddaf2ecb`); a `permission_decision` block surfaces nested reasons (`cd50d851`); Droid's `continue: false` is treated as a JSON block rather than an exit-2 hard stop (`a7d527f0`). `action_from_failure` (`9660e3d6`) classifies transport errors — timeout and connection failures on critical hooks exit 2, while non-critical hooks emit a JSON error envelope (`2df71ac8`). `emit_action` (`7ae0ac51`) writes the result to stdout/stderr and sets the process exit code.

### Suppression, Diagnose, and Schemas

`should_skip_dispatch` (`e42c0c01`) skips the HTTP leg when a filesystem shutdown marker is present and the daemon is unreachable, avoiding blocking the developer after a daemon crash. `suppress_after_failed_post` (`480a97fa`) writes such a marker when a stop-hook POST fails with a transport error, and `delete_enqueued` (`34768c55`) cleans up the pending inbox file. `hooks_disabled_by_env` (`f2c73a2d`) provides an escape hatch via an environment variable. The `diagnose` function (`a992c00e`) inspects the running binary's install provenance (read by `read_install_provenance` / `install_provenance_for_running_binary`, components `8ad675ee`, `fc376df5`) and emits a `DiagnoseOutput` (`ea8d006f`) object validated against the V2 JSON Schema. `run_diagnose` (`80fd2295`) drives this from `main` (`dee4d56b`).

### Schema Contracts

| Schema | `schema_version` const | Key required fields |
|---|---|---|
| V1 (Envelope) | `1` | `schema_version`, `ghook_version`, `cli`, `hook_type`, `source`, `critical`, `daemon_url`, `daemon_host`, `daemon_port`, `project_root`, `project_id` |
| V2 (DiagnoseOutput) | `2` | `schema_version`, `enqueued_at`, `critical`, `hook_type`, `source`, `headers`, `input_data` |

The V1 schema (components `bacf0899`–`e935415a`) also constrains headers as an object whose `X-Gobby-Project-Id` and `X-Gobby-Session-Id` values must be non-empty strings. The V2 schema (components `17f7907d`–`560fb369`) adds `enqueued_at` in `date-time` format and a free-form `input_data` field for the raw hook payload.
[crates/ghook/src/terminal_context.rs:18-23]
[crates/ghook/src/action.rs:9-13]
[crates/ghook/src/cli_config.rs:11-18]
[crates/ghook/src/diagnose.rs:15-32]
[crates/ghook/src/dispatch.rs:16-179]

## Child Modules

| Module | Summary |
| --- | --- |
| [[code/modules/crates/ghook/schemas\|crates/ghook/schemas]] | ## crates/ghook/schemas |
| [[code/modules/crates/ghook/src\|crates/ghook/src]] | ## Module: crates/ghook/src |

