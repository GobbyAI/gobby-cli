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

<details>
<summary>Relevant source files</summary>

- [crates/ghook/src/dispatch.rs:16-179](crates/ghook/src/dispatch.rs#L16-L179), [crates/ghook/src/dispatch.rs:181-183](crates/ghook/src/dispatch.rs#L181-L183), [crates/ghook/src/dispatch.rs:185-213](crates/ghook/src/dispatch.rs#L185-L213), [crates/ghook/src/dispatch.rs:223-226](crates/ghook/src/dispatch.rs#L223-L226), [crates/ghook/src/dispatch.rs:229-241](crates/ghook/src/dispatch.rs#L229-L241), [crates/ghook/src/dispatch.rs:244-252](crates/ghook/src/dispatch.rs#L244-L252), [crates/ghook/src/dispatch.rs:255-295](crates/ghook/src/dispatch.rs#L255-L295), [crates/ghook/src/dispatch.rs:298-330](crates/ghook/src/dispatch.rs#L298-L330)

</details>

# crates/ghook/src/dispatch.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Purpose

Dispatch entrypoint for `ghook`: `run_gobby_owned` coordinates hook processing from CLI args through several early exits, handling disabled hooks, planned-shutdown skips, and statusline hooks before gathering project/terminal context and dispatching the appropriate action. The helpers support that flow by checking `GOBBY_HOOKS_DISABLED`, building the dispatch envelope with optional tmux context, and preserving tmux-related fields only when a valid pane/session is available; the test functions verify those envelope and env-var behaviors.
[crates/ghook/src/dispatch.rs:16-179]
[crates/ghook/src/dispatch.rs:181-183]
[crates/ghook/src/dispatch.rs:185-213]
[crates/ghook/src/dispatch.rs:223-226]
[crates/ghook/src/dispatch.rs:229-241]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `run_gobby_owned` | function | `pub(crate) fn run_gobby_owned(args: &Args) -> ExitCode {` | `run_gobby_owned [function]` | `862baaa6-b74c-51be-a87d-4dcbb6f21965` | 16-179 [crates/ghook/src/dispatch.rs:16-179] | Indexed function `run_gobby_owned` in `crates/ghook/src/dispatch.rs`. [crates/ghook/src/dispatch.rs:16-179] |
| `hooks_disabled_by_env` | function | `fn hooks_disabled_by_env() -> bool {` | `hooks_disabled_by_env [function]` | `f2c73a2d-1c53-506d-a354-4e94eb6967f8` | 181-183 [crates/ghook/src/dispatch.rs:181-183] | Indexed function `hooks_disabled_by_env` in `crates/ghook/src/dispatch.rs`. [crates/ghook/src/dispatch.rs:181-183] |
| `build_dispatch_envelope` | function | `fn build_dispatch_envelope(` | `build_dispatch_envelope [function]` | `cedf4a3a-8ca0-5584-98f4-a65a36cf6613` | 185-213 [crates/ghook/src/dispatch.rs:185-213] | Indexed function `build_dispatch_envelope` in `crates/ghook/src/dispatch.rs`. [crates/ghook/src/dispatch.rs:185-213] |
| `with_tmux_env` | function | `fn with_tmux_env<T>(tmux: Option<&str>, tmux_pane: Option<&str>, f: impl FnOnce() -> T) -> T {` | `with_tmux_env [function]` | `f06761bf-55c8-50f1-a59b-de439e47366e` | 223-226 [crates/ghook/src/dispatch.rs:223-226] | Indexed function `with_tmux_env` in `crates/ghook/src/dispatch.rs`. [crates/ghook/src/dispatch.rs:223-226] |
| `dispatch_envelope_injects_valid_tmux_pane_for_session_start` | function | `fn dispatch_envelope_injects_valid_tmux_pane_for_session_start() {` | `dispatch_envelope_injects_valid_tmux_pane_for_session_start [function]` | `7a9c79a8-0887-5c95-bee8-9edbf5ad760c` | 229-241 [crates/ghook/src/dispatch.rs:229-241] | Indexed function `dispatch_envelope_injects_valid_tmux_pane_for_session_start` in `crates/ghook/src/dispatch.rs`. [crates/ghook/src/dispatch.rs:229-241] |
| `dispatch_envelope_omits_terminal_context_for_tool_hooks` | function | `fn dispatch_envelope_omits_terminal_context_for_tool_hooks() {` | `dispatch_envelope_omits_terminal_context_for_tool_hooks [function]` | `2f2bbcab-d802-53cd-a5ff-3df416ab975e` | 244-252 [crates/ghook/src/dispatch.rs:244-252] | Indexed function `dispatch_envelope_omits_terminal_context_for_tool_hooks` in `crates/ghook/src/dispatch.rs`. [crates/ghook/src/dispatch.rs:244-252] |
| `dispatch_envelope_nulls_tmux_fields_for_missing_or_invalid_tmux_pane` | function | `fn dispatch_envelope_nulls_tmux_fields_for_missing_or_invalid_tmux_pane() {` | `dispatch_envelope_nulls_tmux_fields_for_missing_or_invalid_tmux_pane [function]` | `93e5c8ff-70cd-5df6-9754-ff0e410415de` | 255-295 [crates/ghook/src/dispatch.rs:255-295] | Indexed function `dispatch_envelope_nulls_tmux_fields_for_missing_or_invalid_tmux_pane` in `crates/ghook/src/dispatch.rs`. [crates/ghook/src/dispatch.rs:255-295] |
| `hooks_disabled_by_env_reads_env_var` | function | `fn hooks_disabled_by_env_reads_env_var() {` | `hooks_disabled_by_env_reads_env_var [function]` | `abf502a8-9127-50c3-aa41-b3bcec08825b` | 298-330 [crates/ghook/src/dispatch.rs:298-330] | Indexed function `hooks_disabled_by_env_reads_env_var` in `crates/ghook/src/dispatch.rs`. [crates/ghook/src/dispatch.rs:298-330] |
