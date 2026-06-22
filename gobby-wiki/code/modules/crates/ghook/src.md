---
title: crates/ghook/src
type: code_module
provenance:
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

# crates/ghook/src

Parent: [[code/modules/crates/ghook|crates/ghook]]

## Overview

## Module: crates/ghook/src

`ghook` is the Gobby hook relay binary. It sits between AI coding assistant CLIs (Claude, Codex, Gemini, Grok, Droid) and the Gobby daemon, intercepting every hook invocation the host CLI fires. Its central responsibility is an enqueue-first delivery guarantee: before attempting a live daemon POST, it writes the hook envelope atomically to `~/.gobby/hooks/inbox/<prefix>-<ts13>-<uuid>.json` so the daemon's drain worker can replay any delivery that races a transient outage (transport.rs:1–16). On a 2xx response the inbox file is deleted immediately; on any other outcome — connection refused, timeout, 5xx — the file persists. Each invocation also detects the active AI CLI via `CliConfig::for_cli` (cli_config.rs), which governs which hook types are considered *critical* (exit-blocking) versus non-critical (best-effort JSON), and carries per-CLI quirks such as Gemini treating JSON-parse errors as exit-1, Grok using native snake_case hook names, and Droid having no critical hooks at all.

The main dispatch path reads stdin, injects terminal and tmux context through `terminal_context::inject` (terminal_context.rs), wraps the payload in an `Envelope` (envelope.rs), enqueues and POSTs via `transport::post_and_cleanup`, then converts the daemon's response into a `HookAction` (action.rs). `action_from_success_response` applies per-source rules: Claude's `stopReason: HARD_STOP` becomes exit 2; Codex `pretool_deny` is surfaced as a JSON block; Droid's `continue: false` maps to exit 2 with JSON; generic `is_blocked` matches the dispatcher's blocking patterns for remaining sources (action.rs:36–100). The Claude *statusline* hook takes a separate, latency-sensitive path in `statusline.rs` that posts to `/api/sessions/statusline` with a 2-second timeout on a background thread, then passes stdin bytes through to an optional `GOBBY_STATUSLINE_DOWNSTREAM` subprocess with a 5-second deadline, never surfacing transport failures to Claude as hook errors (statusline.rs:1–80).

Intentional daemon restarts are handled by `planned_shutdown.rs`. If a Stop hook fires while a fresh `shutdown_intent_active.json` marker is present in the marker home directory and the daemon health check returns nothing within 350 ms, `should_skip_dispatch` returns `true` and the Stop hook is silently passed through (planned_shutdown.rs:21–64). A parallel `suppress_after_failed_post` path cleans up an already-enqueued file when a Stop hook's live POST fails with a connect or timeout error during the same window — preventing spurious inbox accumulation during planned restarts. Freshness is configurable via `GOBBY_SHUTDOWN_ALLOW_SECONDS`.

The `diagnose` subcommand (`diagnose.rs`) emits a schema-v2 JSON report that includes install provenance read from a sidecar file, recognized CLI name, and whether terminal context is enabled for the current hook — useful for support and CI validation. Source detection (`source.rs`) infers the originating Gobby source from environment variables and writes a `SourceEnvGuard` that restores env state on drop, supporting nested hook scenarios.

### CLI entry points

| Subcommand / flag | File | Description |
|---|---|---|
| *(default / no subcommand)* | main.rs | Normal hook dispatch |
| `diagnose` | main.rs, diagnose.rs | Emit v2 JSON diagnostic report |
| `--gobby-owned` | args.rs | Activate enqueue-first transport path |

### Environment variables

| Variable | Module | Purpose |
|---|---|---|
| `GOBBY_DAEMON_URL` | transport.rs, statusline.rs | Override daemon base URL |
| `GOBBY_STATUSLINE_DOWNSTREAM` | statusline.rs | Shell command to exec for statusline passthrough |
| `GOBBY_SHUTDOWN_ALLOW_SECONDS` | planned_shutdown.rs | Override freshness window for shutdown markers (default 120 s) |
| `GOBBY_HOOKS_DISABLED` | dispatch.rs | Disable all hook dispatch when set to a truthy value |
| `TMUX_PANE` | terminal_context.rs | tmux pane ID injected into session-start envelopes |

### Public transport types (transport.rs)

| Type | Variants / shape | Purpose |
|---|---|---|
| `DeliveryOutcome` | `Delivered`, `Enqueued` | Whether the daemon ACKed and the inbox file was removed |
| `DeliveryFailureKind` | `Http`, `Connect`, `Timeout`, `Other` | Classification of a failed live POST |
| `DeliveryReport` | outcome, failure\_kind, status\_code, response\_body, transport\_error | Full delivery details returned to caller |

### Per-CLI criticality rules (cli_config.rs)

| CLI | Critical hooks | Notes |
|---|---|---|
| `claude` | `PreToolUse`, `PostToolUse`, `Stop`, `SessionStart` (when terminal context enabled) | JSON-parse errors are non-critical |
| `codex` | `Stop` | `PreToolUse` is non-critical without terminal context |
| `gemini` | *(none critical)* | JSON-parse errors produce exit 1 |
| `grok` | `session_start` (snake_case, terminal context enabled) | Uses native snake_case hook names |
| `droid` | *(none)* | All hooks non-critical; Pascal-case hook names preserved |
| unknown | falls back to Claude rules for dispatch | `for_cli` returns `None`; `for_dispatch` returns Claude config |
[crates/ghook/src/cli_config.rs:11-18]
[crates/ghook/src/json_value.rs:3-20]
[crates/ghook/src/planned_shutdown.rs:21-27]
[crates/ghook/src/terminal_context.rs:18-23]
[crates/ghook/src/action.rs:9-13]

## Files

| File | Summary |
| --- | --- |
| [[code/files/crates/ghook/src/action.rs\|crates/ghook/src/action.rs]] | `crates/ghook/src/action.rs` exposes 28 indexed API symbols. |
| [[code/files/crates/ghook/src/args.rs\|crates/ghook/src/args.rs]] | `crates/ghook/src/args.rs` exposes 1 indexed API symbol. |
| [[code/files/crates/ghook/src/cli_config.rs\|crates/ghook/src/cli_config.rs]] | `crates/ghook/src/cli_config.rs` exposes 12 indexed API symbols. |
| [[code/files/crates/ghook/src/detach.rs\|crates/ghook/src/detach.rs]] | `crates/ghook/src/detach.rs` exposes 1 indexed API symbol. |
| [[code/files/crates/ghook/src/diagnose.rs\|crates/ghook/src/diagnose.rs]] | `crates/ghook/src/diagnose.rs` exposes 20 indexed API symbols. |
| [[code/files/crates/ghook/src/dispatch.rs\|crates/ghook/src/dispatch.rs]] | `crates/ghook/src/dispatch.rs` exposes 8 indexed API symbols. |
| [[code/files/crates/ghook/src/envelope.rs\|crates/ghook/src/envelope.rs]] | `crates/ghook/src/envelope.rs` exposes 8 indexed API symbols. |
| [[code/files/crates/ghook/src/json_value.rs\|crates/ghook/src/json_value.rs]] | `crates/ghook/src/json_value.rs` exposes 2 indexed API symbols. |
| [[code/files/crates/ghook/src/main.rs\|crates/ghook/src/main.rs]] | `crates/ghook/src/main.rs` exposes 2 indexed API symbols. |
| [[code/files/crates/ghook/src/output.rs\|crates/ghook/src/output.rs]] | `crates/ghook/src/output.rs` exposes 2 indexed API symbols. |
| [[code/files/crates/ghook/src/planned_shutdown.rs\|crates/ghook/src/planned_shutdown.rs]] | `crates/ghook/src/planned_shutdown.rs` exposes 31 indexed API symbols. |
| [[code/files/crates/ghook/src/runtime.rs\|crates/ghook/src/runtime.rs]] | `crates/ghook/src/runtime.rs` exposes 1 indexed API symbol. |
| [[code/files/crates/ghook/src/source.rs\|crates/ghook/src/source.rs]] | `crates/ghook/src/source.rs` exposes 7 indexed API symbols. |
| [[code/files/crates/ghook/src/statusline.rs\|crates/ghook/src/statusline.rs]] | `crates/ghook/src/statusline.rs` exposes 22 indexed API symbols. |
| [[code/files/crates/ghook/src/terminal_context.rs\|crates/ghook/src/terminal_context.rs]] | `crates/ghook/src/terminal_context.rs` exposes 17 indexed API symbols. |
| [[code/files/crates/ghook/src/transport.rs\|crates/ghook/src/transport.rs]] | `crates/ghook/src/transport.rs` exposes 23 indexed API symbols. |

