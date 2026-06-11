---
title: crates/ghook/src/main.rs
type: code_file
provenance:
- file: crates/ghook/src/main.rs
  ranges:
  - 38-42
  - 50-74
  - 76-99
  - 101-117
  - 119-259
  - 261-267
  - 269-271
  - 273-301
  - 303-317
  - 319-327
  - 329-399
  - 401-420
  - 422-482
  - 484-506
  - 508-536
  - 538-555
  - 557-570
  - 581-584
  - 587-599
  - 602-610
  - 613-653
  - 656-677
  - 680-696
  - 699-715
  - 718-735
  - 738-756
  - 759-775
  - 778-794
  - 797-808
  - 811-817
  - 820-836
  - 839-853
  - 856-871
  - 874-887
  - 890-900
  - 903-916
  - 919-932
  - 935-967
  - 970-979
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/ghook/src/main.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Purpose

`crates/ghook/src/main.rs` exposes 39 indexed API symbols.
[crates/ghook/src/main.rs:38-42]
[crates/ghook/src/main.rs:50-74]
[crates/ghook/src/main.rs:76-99]
[crates/ghook/src/main.rs:101-117]
[crates/ghook/src/main.rs:119-259]

## API Symbols

- `HookAction` (class) component `HookAction [class]` (`621b3717-b526-5256-b568-1fe551b4cc35`) lines 38-42 [crates/ghook/src/main.rs:38-42]
  - Signature: `struct HookAction {`
  - Purpose: HookAction is a struct that encapsulates a hook execution result, containing an exit code (u8) and optional JSON-formatted stdout output and stderr message. [crates/ghook/src/main.rs:38-42]
- `Args` (class) component `Args [class]` (`fd4cad88-5526-5a34-aeda-24b4397cbc24`) lines 50-74 [crates/ghook/src/main.rs:50-74]
  - Signature: `struct Args {`
  - Purpose: Args is a command-line argument struct that configures gobby's hook runtime system with support for normal invocation mode, diagnostics, versioning, AI CLI selection (claude/codex/gemini/qwen/droid), hook-type targeting, and process detachment. [crates/ghook/src/main.rs:50-74]
- `main` (function) component `main [function]` (`938b2354-40c9-5831-b1ef-55074d23b6dc`) lines 76-99 [crates/ghook/src/main.rs:76-99]
  - Signature: `fn main() -> ExitCode {`
  - Purpose: Parses command-line arguments and dispatches to one of three modes (--version with runtime stamping, --diagnose, or --gobby-owned), returning exit code 2 if no mode is specified. [crates/ghook/src/main.rs:76-99]
- `run_diagnose` (function) component `run_diagnose [function]` (`0c1a1e6c-7edb-5845-a6f1-14169f776367`) lines 101-117 [crates/ghook/src/main.rs:101-117]
  - Signature: `fn run_diagnose(args: &Args) -> ExitCode {`
  - Purpose: Extracts required `--cli` and `--type` arguments, invokes the diagnostic function, and returns its serialized JSON output or an error exit code. [crates/ghook/src/main.rs:101-117]
- `run_gobby_owned` (function) component `run_gobby_owned [function]` (`eb63dfc4-2dcb-576f-82c0-777e7a3b8df5`) lines 119-259 [crates/ghook/src/main.rs:119-259]
  - Signature: `fn run_gobby_owned(args: &Args) -> ExitCode {`
  - Purpose: Validates hook invocation eligibility through environment and shutdown checks, routes hook types (statusline vs. standard), and discovers project context before processing downstream. [crates/ghook/src/main.rs:119-259]
- `continue_action` (function) component `continue_action [function]` (`56d0517b-3b9f-5ecd-b481-815b11372cd1`) lines 261-267 [crates/ghook/src/main.rs:261-267]
  - Signature: `fn continue_action() -> HookAction {`
  - Purpose: `continue_action` returns a `HookAction` with exit code 0 and JSON output `{"continue": true}`, signaling successful continuation. [crates/ghook/src/main.rs:261-267]
- `hooks_disabled_by_env` (function) component `hooks_disabled_by_env [function]` (`03a51f93-89d4-54da-96d6-45db1bcc2dc7`) lines 269-271 [crates/ghook/src/main.rs:269-271]
  - Signature: `fn hooks_disabled_by_env() -> bool {`
  - Purpose: Returns true if the environment variable `GOBBY_HOOKS_DISABLED` is set to exactly "1", false otherwise. [crates/ghook/src/main.rs:269-271]
- `build_dispatch_envelope` (function) component `build_dispatch_envelope [function]` (`c643761b-bc69-5517-86cd-0c5f27aa1a43`) lines 273-301 [crates/ghook/src/main.rs:273-301]
  - Signature: `fn build_dispatch_envelope(`
  - Purpose: Builds a webhook dispatch Envelope by conditionally injecting terminal context into the input data and populating HTTP headers with optional project and session identifiers. [crates/ghook/src/main.rs:273-301]
- `detect_source` (function) component `detect_source [function]` (`310d3663-4164-5dbe-bb05-79931467c260`) lines 303-317 [crates/ghook/src/main.rs:303-317]
  - Signature: `fn detect_source(cfg: &CliConfig) -> String {`
  - Purpose: Detects the execution source by prioritizing a non-"claude" config value, then the `GOBBY_SOURCE` environment variable, then `CLAUDE_CODE_ENTRYPOINT`, with fallback to the config default. [crates/ghook/src/main.rs:303-317]
- `emit_action` (function) component `emit_action [function]` (`14279e14-6377-5c12-b42f-e25a648a2f3d`) lines 319-327 [crates/ghook/src/main.rs:319-327]
  - Signature: `fn emit_action(action: HookAction) -> ExitCode {`
  - Purpose: Emits JSON and/or error messages from a `HookAction` to stdout and stderr respectively, then returns its exit code. [crates/ghook/src/main.rs:319-327]
- `action_from_success_response` (function) component `action_from_success_response [function]` (`a9fac95f-a9f0-58ec-8c35-6a786112a062`) lines 329-399 [crates/ghook/src/main.rs:329-399]
  - Signature: `fn action_from_success_response(`
  - Purpose: # Summary

Parses a JSON response body and routes it through source-specific handlers to produce a `HookAction` with exit codes determined by canonical source type (e.g., Claude's `continue`/`stopReason` fields) and block status. [crates/ghook/src/main.rs:329-399]
- `action_from_droid_success` (function) component `action_from_droid_success [function]` (`e575a823-1f9b-53c9-a297-1b995e22151e`) lines 401-420 [crates/ghook/src/main.rs:401-420]
  - Signature: `fn action_from_droid_success(result: Value, serialized: String) -> HookAction {`
  - Purpose: Converts a JSON result into a `HookAction` that signals failure (exit code 2) with an extracted error reason if the result's "continue" field is `false`, otherwise signals success (exit code 0) with the serialized output if meaningful. [crates/ghook/src/main.rs:401-420]
- `action_from_failure` (function) component `action_from_failure [function]` (`6ea37017-9105-5175-909e-08e70807c6ec`) lines 422-482 [crates/ghook/src/main.rs:422-482]
  - Signature: `fn action_from_failure(`
  - Purpose: Converts hook delivery failures into `HookAction` responses with exit codes and error messages determined by hook criticality and failure type—critical hooks fail with exit code 2, others with code 1, each with kind-specific diagnostics. [crates/ghook/src/main.rs:422-482]
- `is_blocked` (function) component `is_blocked [function]` (`a340b258-6c6d-57b4-814c-77096f5a1ec6`) lines 484-506 [crates/ghook/src/main.rs:484-506]
  - Signature: `fn is_blocked(result: &Value) -> bool {`
  - Purpose: # Summary

Returns true if the JSON object contains any deny or block indicator across the `continue`, `decision`, `permissionDecision`, or nested `hookSpecificOutput.permissionDecision` fields. [crates/ghook/src/main.rs:484-506]
- `extract_reason` (function) component `extract_reason [function]` (`86105f7e-8f0d-51e3-9bb5-9397b02be28d`) lines 508-536 [crates/ghook/src/main.rs:508-536]
  - Signature: `fn extract_reason(result: &Value) -> String {`
  - Purpose: Extracts a blocking reason string from a JSON object by searching top-level keys (stopReason, user_message, reason) and nested hookSpecificOutput fields in priority order, defaulting to "Blocked by hook" if none are found. [crates/ghook/src/main.rs:508-536]
- `json_value_is_meaningful` (function) component `json_value_is_meaningful [function]` (`50e3aebd-d3e2-5d93-b997-d5898f82a59b`) lines 538-555 [crates/ghook/src/main.rs:538-555]
  - Signature: `fn json_value_is_meaningful(value: &Value) -> bool {`
  - Purpose: Evaluates JSON values for semantic truthiness, returning true only for non-null, non-false, non-zero, and non-empty values. [crates/ghook/src/main.rs:538-555]
- `write_runtime_stamp` (function) component `write_runtime_stamp [function]` (`b36f51c1-d253-57a3-9e4d-1d657a376c42`) lines 557-570 [crates/ghook/src/main.rs:557-570]
  - Signature: `fn write_runtime_stamp() -> Result<()> {`
  - Purpose: Atomically writes a JSON metadata file containing ghook schema version and application version to `~/.gobby/bin/.ghook-runtime.json`. [crates/ghook/src/main.rs:557-570]
- `with_tmux_env` (function) component `with_tmux_env [function]` (`145db008-637c-502d-8768-904b7dd210a5`) lines 581-584 [crates/ghook/src/main.rs:581-584]
  - Signature: `fn with_tmux_env<T>(tmux: Option<&str>, tmux_pane: Option<&str>, f: impl FnOnce() -> T) -> T {`
  - Purpose: # Summary

Executes a closure with TMUX and TMUX_PANE environment variables temporarily set to provided values, guarded by an exclusive lock on ENV_LOCK. [crates/ghook/src/main.rs:581-584]
- `dispatch_envelope_injects_valid_tmux_pane_for_session_start` (function) component `dispatch_envelope_injects_valid_tmux_pane_for_session_start [function]` (`311d2266-9504-5fdd-a07a-05a6b773ff4b`) lines 587-599 [crates/ghook/src/main.rs:587-599]
  - Signature: `fn dispatch_envelope_injects_valid_tmux_pane_for_session_start() {`
  - Purpose: This test function verifies that `build_dispatch_envelope` correctly injects the active tmux pane identifier into the dispatch envelope's terminal context when constructing a SessionStart event. [crates/ghook/src/main.rs:587-599]
- `dispatch_envelope_omits_terminal_context_for_tool_hooks` (function) component `dispatch_envelope_omits_terminal_context_for_tool_hooks [function]` (`02fe120f-bbe6-5058-8da4-83f7270fb883`) lines 602-610 [crates/ghook/src/main.rs:602-610]
  - Signature: `fn dispatch_envelope_omits_terminal_context_for_tool_hooks() {`
  - Purpose: Verifies that dispatch envelopes for PreToolUse tool hooks exclude the `terminal_context` field from input data. [crates/ghook/src/main.rs:602-610]
- `dispatch_envelope_nulls_tmux_fields_for_missing_or_invalid_tmux_pane` (function) component `dispatch_envelope_nulls_tmux_fields_for_missing_or_invalid_tmux_pane [function]` (`52733481-aeac-51c2-b59f-41bdd673a847`) lines 613-653 [crates/ghook/src/main.rs:613-653]
  - Signature: `fn dispatch_envelope_nulls_tmux_fields_for_missing_or_invalid_tmux_pane() {`
  - Purpose: This test function verifies that `build_dispatch_envelope` correctly nullifies the `tmux_pane` and `tmux_socket_path` fields when provided with missing, empty, or malformed tmux pane identifiers or socket paths. [crates/ghook/src/main.rs:613-653]
- `action_from_success_forwards_sessionstart_context_json` (function) component `action_from_success_forwards_sessionstart_context_json [function]` (`11c12b39-7c36-5880-ae5a-6d032193d9a3`) lines 656-677 [crates/ghook/src/main.rs:656-677]
  - Signature: `fn action_from_success_forwards_sessionstart_context_json() {`
  - Purpose: This function tests that `action_from_success_response` correctly processes a SessionStart hook event, returning a zero-exit action with an "accept" decision and session-specific context metadata in the parsed JSON output. [crates/ghook/src/main.rs:656-677]
- `action_from_success_treats_codex_pretool_deny_as_json_block` (function) component `action_from_success_treats_codex_pretool_deny_as_json_block [function]` (`88f07f01-1c68-5207-bbb4-84ca9b0cd0f2`) lines 680-696 [crates/ghook/src/main.rs:680-696]
  - Signature: `fn action_from_success_treats_codex_pretool_deny_as_json_block() {`
  - Purpose: This test function asserts that a successful codex PreToolUse hook denial produces an exit code of 0, outputs the `"permissionDecision":"deny"` JSON value to stdout, and generates no stderr message. [crates/ghook/src/main.rs:680-696]
- `action_from_success_surfaces_nested_permission_decision_reason` (function) component `action_from_success_surfaces_nested_permission_decision_reason [function]` (`62c41969-5376-57de-9f0f-b89df3b921fb`) lines 699-715 [crates/ghook/src/main.rs:699-715]
  - Signature: `fn action_from_success_surfaces_nested_permission_decision_reason() {`
  - Purpose: This test function validates that a PreToolUse hook response with a deny permission decision correctly parses and surfaces the nested `permissionDecisionReason` field from the JSON output. [crates/ghook/src/main.rs:699-715]
- `action_from_success_preserves_additional_context_on_claude_block` (function) component `action_from_success_preserves_additional_context_on_claude_block [function]` (`ad4cea8f-4c11-5546-962b-18aa80dd45db`) lines 718-735 [crates/ghook/src/main.rs:718-735]
  - Signature: `fn action_from_success_preserves_additional_context_on_claude_block() {`
  - Purpose: This test verifies that `action_from_success_response` preserves the `additionalContext` and `permissionDecision` fields when parsing a Claude PreToolUse hook response JSON. [crates/ghook/src/main.rs:718-735]
- `action_from_success_preserves_user_prompt_submit_block_json` (function) component `action_from_success_preserves_user_prompt_submit_block_json [function]` (`c9cbc63e-d037-5daf-9add-0d07a149bb56`) lines 738-756 [crates/ghook/src/main.rs:738-756]
  - Signature: `fn action_from_success_preserves_user_prompt_submit_block_json() {`
  - Purpose: Tests that `action_from_success_response` correctly deserializes and preserves a UserPromptSubmit block decision JSON response with nested hookSpecificOutput metadata in the action's stdout. [crates/ghook/src/main.rs:738-756]
- `action_from_success_treats_stop_block_as_exit_two` (function) component `action_from_success_treats_stop_block_as_exit_two [function]` (`70959c9c-3990-551b-ada0-21bb3f2c5db0`) lines 759-775 [crates/ghook/src/main.rs:759-775]
  - Signature: `fn action_from_success_treats_stop_block_as_exit_two() {`
  - Purpose: This unit test asserts that `action_from_success_response` converts a "Stop" response with a "block" decision into a `HookAction` with exit code 2 and the reason string populated in stderr_message. [crates/ghook/src/main.rs:759-775]
- `action_from_success_claude_hard_stop_exits_two` (function) component `action_from_success_claude_hard_stop_exits_two [function]` (`64a0ed27-aa71-549c-b4b7-1831867f6be3`) lines 778-794 [crates/ghook/src/main.rs:778-794]
  - Signature: `fn action_from_success_claude_hard_stop_exits_two() {`
  - Purpose: This test function verifies that `action_from_success_response()` correctly transforms a Claude "Stop" response with `stopReason: "Daemon halted run"` into a `HookAction` with exit code 2, no stdout, and the stop reason message in stderr. [crates/ghook/src/main.rs:778-794]
- `action_from_success_claude_stop_with_permission_deny_no_exit_two` (function) component `action_from_success_claude_stop_with_permission_deny_no_exit_two [function]` (`205aef13-ce50-5aed-bbb2-909865a58378`) lines 797-808 [crates/ghook/src/main.rs:797-808]
  - Signature: `fn action_from_success_claude_stop_with_permission_deny_no_exit_two() {`
  - Purpose: Asserts that processing a Claude Stop action with a permission denial decision yields exit code 0, JSON stdout output, and no stderr message. [crates/ghook/src/main.rs:797-808]
- `action_from_success_claude_continue_false_without_reason_does_not_exit_two` (function) component `action_from_success_claude_continue_false_without_reason_does_not_exit_two [function]` (`043503d8-8428-5b6f-96e3-e9b560a59add`) lines 811-817 [crates/ghook/src/main.rs:811-817]
  - Signature: `fn action_from_success_claude_continue_false_without_reason_does_not_exit_two() {`
  - Purpose: Verifies that parsing a Claude agent's success response with `continue: false` produces an action with exit code 0 and no stderr message. [crates/ghook/src/main.rs:811-817]
- `action_from_success_treats_droid_continue_false_as_exit_two_with_json` (function) component `action_from_success_treats_droid_continue_false_as_exit_two_with_json [function]` (`7408971b-126e-5740-af8a-3e2ca9513b4e`) lines 820-836 [crates/ghook/src/main.rs:820-836]
  - Signature: `fn action_from_success_treats_droid_continue_false_as_exit_two_with_json() {`
  - Purpose: Tests that processing a droid PreToolUse response with `continue: false` yields an action with exit code 2 and extracts the `stopReason` to `stderr_message`. [crates/ghook/src/main.rs:820-836]
- `action_from_success_preserves_droid_block_json_without_exit_two` (function) component `action_from_success_preserves_droid_block_json_without_exit_two [function]` (`a5ac24a2-fb0b-50b7-8285-42f35daf096e`) lines 839-853 [crates/ghook/src/main.rs:839-853]
  - Signature: `fn action_from_success_preserves_droid_block_json_without_exit_two() {`
  - Purpose: This test verifies that `action_from_success_response` correctly preserves a droid block decision JSON payload in stdout while returning exit code 0 and no stderr message. [crates/ghook/src/main.rs:839-853]
- `action_from_failure_blocks_critical_hooks` (function) component `action_from_failure_blocks_critical_hooks [function]` (`ae46af86-f0c8-5ba0-9273-2e40676812aa`) lines 856-871 [crates/ghook/src/main.rs:856-871]
  - Signature: `fn action_from_failure_blocks_critical_hooks() {`
  - Purpose: This test verifies that `action_from_failure()` returns exit code 2 with no stdout and an appropriate stderr error message when an HTTP 500 failure occurs on the critical 'SessionStart' hook. [crates/ghook/src/main.rs:856-871]
- `action_from_failure_returns_json_for_noncritical_hooks` (function) component `action_from_failure_returns_json_for_noncritical_hooks [function]` (`248f4cae-e108-54d3-b664-5de59bf05c6e`) lines 874-887 [crates/ghook/src/main.rs:874-887]
  - Signature: `fn action_from_failure_returns_json_for_noncritical_hooks() {`
  - Purpose: Verifies that `action_from_failure` returns exit code 1 and serializes a connection failure into JSON-formatted error output (status: "error", message: "Daemon unreachable") without stderr for non-critical hooks. [crates/ghook/src/main.rs:874-887]
- `action_from_failure_treats_timeout_like_python` (function) component `action_from_failure_treats_timeout_like_python [function]` (`0f786741-84f9-57f5-b8f5-0cfe84ea4db4`) lines 890-900 [crates/ghook/src/main.rs:890-900]
  - Signature: `fn action_from_failure_treats_timeout_like_python() {`
  - Purpose: This function tests that `action_from_failure` handles a timeout delivery failure by returning exit code 1 and JSON output containing the message "Hook execution timeout". [crates/ghook/src/main.rs:890-900]
- `action_from_failure_treats_connect_on_critical_hook_as_exit_two` (function) component `action_from_failure_treats_connect_on_critical_hook_as_exit_two [function]` (`6c5919b0-f639-5e4e-b974-b4c7b0039f4e`) lines 903-916 [crates/ghook/src/main.rs:903-916]
  - Signature: `fn action_from_failure_treats_connect_on_critical_hook_as_exit_two() {`
  - Purpose: This test verifies that `action_from_failure` returns exit code 2 with a fail-safe error message when a daemon connection fails on the critical 'Stop' hook. [crates/ghook/src/main.rs:903-916]
- `action_from_failure_returns_stderr_for_droid_transport_errors` (function) component `action_from_failure_returns_stderr_for_droid_transport_errors [function]` (`ddb4aa4b-6a10-571a-9144-ba099470899d`) lines 919-932 [crates/ghook/src/main.rs:919-932]
  - Signature: `fn action_from_failure_returns_stderr_for_droid_transport_errors() {`
  - Purpose: Unit test verifying that `action_from_failure` returns an action with exit code 1 and stderr message "Daemon error: Internal Server Error" when handling HTTP delivery failures for droid dispatcher. [crates/ghook/src/main.rs:919-932]
- `hooks_disabled_by_env_reads_env_var` (function) component `hooks_disabled_by_env_reads_env_var [function]` (`86f7722c-f5bd-5494-b665-6e3583e145f5`) lines 935-967 [crates/ghook/src/main.rs:935-967]
  - Signature: `fn hooks_disabled_by_env_reads_env_var() {`
  - Purpose: Tests that `hooks_disabled_by_env()` returns true if and only if the `GOBBY_HOOKS_DISABLED` environment variable is set to exactly `"1"`. [crates/ghook/src/main.rs:935-967]
- `is_blocked_matches_dispatcher_patterns` (function) component `is_blocked_matches_dispatcher_patterns [function]` (`cdf4abcc-14c2-5bdf-ab47-85be2998ac0b`) lines 970-979 [crates/ghook/src/main.rs:970-979]
  - Signature: `fn is_blocked_matches_dispatcher_patterns() {`
  - Purpose: Unit test that validates the `is_blocked` function correctly identifies blocking/denying patterns across multiple dispatcher response JSON structures (including `decision`, `permissionDecision`, `continue`, and nested `hookSpecificOutput` fields) while returning false for approval decisions. [crates/ghook/src/main.rs:970-979]

