---
title: crates/ghook/src/dispatch.rs
type: code_file
provenance:
- file: crates/ghook/src/dispatch.rs
  ranges:
  - 16-179
  - 181-183
  - 185-213
  - 223-226
  - 229-241
  - 244-252
  - 255-295
  - 298-330
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/ghook/src/dispatch.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Purpose

This file implements the owned gobby hook dispatch path: `run_gobby_owned` validates the CLI and hook type, handles special cases first (`GOBBY_HOOKS_DISABLED`, planned shutdown, and statusline hooks), then gathers project context and stdin so the hook can be dispatched safely. `build_dispatch_envelope` assembles the JSON envelope for that dispatch, enriching it with terminal context and project/session headers when available, while `with_tmux_env` provides a controlled way for tests to simulate tmux state. The tests verify the environment gate and the envelope’s tmux/terminal-context behavior across valid, missing, and malformed inputs.
[crates/ghook/src/dispatch.rs:16-179]
[crates/ghook/src/dispatch.rs:181-183]
[crates/ghook/src/dispatch.rs:185-213]
[crates/ghook/src/dispatch.rs:223-226]
[crates/ghook/src/dispatch.rs:229-241]

## API Symbols

- `run_gobby_owned` (function) component `run_gobby_owned [function]` (`862baaa6-b74c-51be-a87d-4dcbb6f21965`) lines 16-179 [crates/ghook/src/dispatch.rs:16-179]
  - Signature: `pub(crate) fn run_gobby_owned(args: &Args) -> ExitCode {`
  - Purpose: 'run_gobby_owned' validates 'cli' and 'hook_type', emits empty JSON and exits with code 2 if either is missing, short-circuits or handles special hook cases ('GOBBY_HOOKS_DISABLED', planned shutdown, and statusline hooks), otherwise resolves project context and reads stdin in preparation for dispatching the gobby hook action. [crates/ghook/src/dispatch.rs:16-179]
- `hooks_disabled_by_env` (function) component `hooks_disabled_by_env [function]` (`f2c73a2d-1c53-506d-a354-4e94eb6967f8`) lines 181-183 [crates/ghook/src/dispatch.rs:181-183]
  - Signature: `fn hooks_disabled_by_env() -> bool {`
  - Purpose: Returns 'true' only when the 'GOBBY_HOOKS_DISABLED' environment variable is set to the exact string '"1"', and 'false' otherwise. [crates/ghook/src/dispatch.rs:181-183]
- `build_dispatch_envelope` (function) component `build_dispatch_envelope [function]` (`cedf4a3a-8ca0-5584-98f4-a65a36cf6613`) lines 185-213 [crates/ghook/src/dispatch.rs:185-213]
  - Signature: `fn build_dispatch_envelope(`
  - Purpose: Builds an 'Envelope' for a hook by conditionally injecting terminal context into the JSON payload, deriving the source and criticality from 'cfg', and populating 'X-Gobby-Project-Id' and non-empty 'X-Gobby-Session-Id' headers when present. [crates/ghook/src/dispatch.rs:185-213]
- `with_tmux_env` (function) component `with_tmux_env [function]` (`f06761bf-55c8-50f1-a59b-de439e47366e`) lines 223-226 [crates/ghook/src/dispatch.rs:223-226]
  - Signature: `fn with_tmux_env<T>(tmux: Option<&str>, tmux_pane: Option<&str>, f: impl FnOnce() -> T) -> T {`
  - Purpose: Acquires a global environment lock and runs 'f' with 'TMUX' and 'TMUX_PANE' temporarily set to the provided optional values, restoring the prior environment afterward. [crates/ghook/src/dispatch.rs:223-226]
- `dispatch_envelope_injects_valid_tmux_pane_for_session_start` (function) component `dispatch_envelope_injects_valid_tmux_pane_for_session_start [function]` (`7a9c79a8-0887-5c95-bee8-9edbf5ad760c`) lines 229-241 [crates/ghook/src/dispatch.rs:229-241]
  - Signature: `fn dispatch_envelope_injects_valid_tmux_pane_for_session_start() {`
  - Purpose: Verifies that 'build_dispatch_envelope' includes the current tmux pane ID ('%17') in 'terminal_context.tmux_pane' when constructing a 'SessionStart' dispatch envelope. [crates/ghook/src/dispatch.rs:229-241]
- `dispatch_envelope_omits_terminal_context_for_tool_hooks` (function) component `dispatch_envelope_omits_terminal_context_for_tool_hooks [function]` (`2f2bbcab-d802-53cd-a5ff-3df416ab975e`) lines 244-252 [crates/ghook/src/dispatch.rs:244-252]
  - Signature: `fn dispatch_envelope_omits_terminal_context_for_tool_hooks() {`
  - Purpose: Verifies that 'build_dispatch_envelope' omits the 'terminal_context' field when constructing a 'PreToolUse' dispatch envelope for a tool hook session. [crates/ghook/src/dispatch.rs:244-252]
- `dispatch_envelope_nulls_tmux_fields_for_missing_or_invalid_tmux_pane` (function) component `dispatch_envelope_nulls_tmux_fields_for_missing_or_invalid_tmux_pane [function]` (`93e5c8ff-70cd-5df6-9754-ff0e410415de`) lines 255-295 [crates/ghook/src/dispatch.rs:255-295]
  - Signature: `fn dispatch_envelope_nulls_tmux_fields_for_missing_or_invalid_tmux_pane() {`
  - Purpose: Verifies that 'build_dispatch_envelope' populates 'terminal_context.tmux_pane' and 'terminal_context.tmux_socket_path' as 'null' when the tmux pane is missing or malformed, or when no tmux environment is present despite a pane value. [crates/ghook/src/dispatch.rs:255-295]
- `hooks_disabled_by_env_reads_env_var` (function) component `hooks_disabled_by_env_reads_env_var [function]` (`abf502a8-9127-50c3-aa41-b3bcec08825b`) lines 298-330 [crates/ghook/src/dispatch.rs:298-330]
  - Signature: `fn hooks_disabled_by_env_reads_env_var() {`
  - Purpose: Tests that 'hooks_disabled_by_env()' returns 'true' only when the 'GOBBY_HOOKS_DISABLED' environment variable is exactly '"1"', and 'false' when it is unset, '"0"', or empty. [crates/ghook/src/dispatch.rs:298-330]

