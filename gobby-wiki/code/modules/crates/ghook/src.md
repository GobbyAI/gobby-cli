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

`crates/ghook/src` implements the hook-side CLI/runtime for forwarding host-agent hook invocations into Gobby. Its normal path builds a hook envelope, writes it to the local inbox first, then attempts a daemon POST; `transport` documents the durability contract as atomic write to `~/.gobby/hooks/inbox/<p>-<ts13>-<uuid>.json`, deletion on 2xx, and replay by the daemon drain worker on timeout, connection failure, or HTTP failure (`crates/ghook/src/transport.rs:1-18`). `action` translates daemon responses into hook-visible stdout/stderr/exit behavior through `HookAction`, importing CLI policy, Python-style truthiness, Stop-hook handling, output, and transport collaborators (`crates/ghook/src/action.rs:1-29`).

The main hook flow is policy-driven by source and CLI configuration: `CliConfig` decides recognized CLIs and critical hooks, `source` detects canonical sources, `dispatch` builds and sends envelopes, `terminal_context` can inject tmux/TTY/process context, and `transport` records delivery reports. The response path preserves daemon JSON on stdout when appropriate, emits stderr for blocking errors, and maps special cases such as Claude hard stops, Droid semantics, transport failures, and critical-hook failures into exit codes (`crates/ghook/src/action.rs:31-100`). Planned shutdown handling is a narrow Stop-hook escape hatch: it accepts only fresh shutdown markers, checks daemon reachability, and suppresses only connection/timeout races for Stop hooks so intentional Gobby restarts do not block the host CLI (`crates/ghook/src/planned_shutdown.rs:1-58`).

Statusline handling is intentionally outside the enqueue-first path because Claude consumes statusline stdout on every tick. `statusline` recognizes only Claude `statusline` hooks, extracts a session payload when possible, posts it best-effort to `/api/sessions/statusline`, optionally runs a downstream command from `GOBBY_STATUSLINE_DOWNSTREAM`, preserves downstream stdout bytes, and always exits successfully so daemon or parsing problems do not surface as hook failures (`crates/ghook/src/statusline.rs:1-65`). Diagnostics and support modules round out the binary: `diagnose` reports CLI/install/schema state, `envelope` defines serialized hook payloads, `json_value` centralizes Python truthiness compatibility, `output` wraps stdout/stderr emission, `detach` and `runtime` support process/runtime setup, and `main` dispatches the CLI entry points.

| Area | Public symbols |
| --- | --- |
| Action emission | `HookAction`, `continue_action`, `emit_empty_json`, `emit_action`, `action_from_success_response`, `action_from_failure` |
| CLI policy | `Args`, `CliConfig`, `CliConfig::for_cli`, `CliConfig::for_dispatch`, `CliConfig::is_critical_hook` |
| Dispatch/envelope | `run_gobby_owned`, `build_dispatch_envelope`, `Envelope`, `Envelope::new` |
| Transport | `DeliveryOutcome`, `DeliveryFailureKind`, `DeliveryReport`, `inbox_dir`, `quarantine_dir`, `enqueue_to`, `post_and_cleanup` |
| Shutdown/statusline | `should_skip_dispatch`, `suppress_after_failed_post`, `is_stop_hook`, `is_statusline_hook`, `handle` |
| Context/source | `detect_source`, `SourceEnvGuard`, `capture`, `enabled_for_hook`, `build_context`, `inject` |

| Environment/config fact | Meaning |
| --- | --- |
| `GOBBY_STATUSLINE_DOWNSTREAM` | Optional downstream statusline command; when set, its stdout is passed through exactly (`crates/ghook/src/statusline.rs:24-62`). |
| `~/.gobby/hooks/inbox/` | Durable hook inbox used before live daemon POST (`crates/ghook/src/transport.rs:1-18`, `crates/ghook/src/transport.rs:54-57`). |
| `~/.gobby/hooks/inbox/quarantine/` | Quarantine directory for malformed inbox entries (`crates/ghook/src/transport.rs:59-62`). |
| `shutdown_intent_active.json` | Short-lived planned-shutdown marker checked for Stop-hook suppression (`crates/ghook/src/planned_shutdown.rs:10-17`). |
| `/api/hooks/execute` | Normal daemon hook endpoint (`crates/ghook/src/transport.rs:21-24`). |
| `/api/sessions/statusline` | Best-effort statusline endpoint (`crates/ghook/src/statusline.rs:14-18`). |
| `/api/admin/health` | Planned-shutdown reachability probe endpoint (`crates/ghook/src/planned_shutdown.rs:10-13`). |
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

