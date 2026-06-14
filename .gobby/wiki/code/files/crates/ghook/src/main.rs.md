---
title: crates/ghook/src/main.rs
type: code_file
provenance:
- file: crates/ghook/src/main.rs
  ranges:
  - 45-49
  - 57-81
  - 83-106
  - 108-124
  - 126-289
  - 291-297
  - 299-301
  - 303-305
  - 307-335
  - 337-345
  - 347-417
  - 419-438
  - 440-500
  - 502-524
  - 526-554
  - 556-568
  - 579-582
  - 585-597
  - 600-608
  - 611-651
  - 654-675
  - 678-694
  - 697-713
  - 716-733
  - 736-754
  - 757-773
  - 776-792
  - 795-806
  - 809-815
  - 818-834
  - 837-851
  - 854-869
  - 872-885
  - 888-898
  - 901-914
  - 917-930
  - 933-965
  - 968-977
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/ghook/src/main.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Purpose

`crates/ghook/src/main.rs` is the `ghook` CLI entry point for Gobby’s sandbox-tolerant hook dispatcher. It parses hook-runtime flags, routes into version, diagnose, or normal `gobby_owned` execution, writes the runtime stamp, builds dispatch envelopes with project/session and terminal context, and converts successful or failed daemon responses into `HookAction` exit codes plus stdout/stderr output, with helpers handling blocked decisions, disabled hooks, tmux environment, and related integration tests.
[crates/ghook/src/main.rs:45-49]
[crates/ghook/src/main.rs:57-81]
[crates/ghook/src/main.rs:83-106]
[crates/ghook/src/main.rs:108-124]
[crates/ghook/src/main.rs:126-289]

## API Symbols

- `HookAction` (class) component `HookAction [class]` (`b7deea92-b69e-59db-b0f9-aa74c3168cf2`) lines 45-49 [crates/ghook/src/main.rs:45-49]
  - Signature: `struct HookAction {`
  - Purpose: 'HookAction' is a struct that records a hook execution result with an 8-bit 'exit_code', an optional JSON-encoded 'stdout_json' string, and an optional 'stderr_message' string. [crates/ghook/src/main.rs:45-49]
- `Args` (class) component `Args [class]` (`6aae9f18-b7ef-5eef-b421-a457b7ea5592`) lines 57-81 [crates/ghook/src/main.rs:57-81]
  - Signature: `struct Args {`
  - Purpose: 'Args' is a CLI argument struct for a hook runtime that controls execution mode and metadata via flags for 'gobby_owned', 'diagnose', 'version', 'cli', 'hook_type', and 'detach'. [crates/ghook/src/main.rs:57-81]
- `main` (function) component `main [function]` (`18168f09-19dd-51df-a93c-0d919181cb35`) lines 83-106 [crates/ghook/src/main.rs:83-106]
  - Signature: `fn main() -> ExitCode {`
  - Purpose: Parses CLI arguments and dispatches to '--version', '--diagnose', or '--gobby-owned' mode, otherwise prints a usage error to stderr and exits with code 2. [crates/ghook/src/main.rs:83-106]
- `run_diagnose` (function) component `run_diagnose [function]` (`a7cdbeb5-469f-58f0-9dc7-5f4cc7a9b8ea`) lines 108-124 [crates/ghook/src/main.rs:108-124]
  - Signature: `fn run_diagnose(args: &Args) -> ExitCode {`
  - Purpose: Validates that '--cli' and '--type' are present, runs 'diagnose::diagnose(cli, hook_type)', then pretty-prints the result as JSON to stdout or returns exit code '2' on missing arguments or serialization failure. [crates/ghook/src/main.rs:108-124]
- `run_gobby_owned` (function) component `run_gobby_owned [function]` (`beb7d475-755e-535a-943d-7f52fdafdee3`) lines 126-289 [crates/ghook/src/main.rs:126-289]
  - Signature: `fn run_gobby_owned(args: &Args) -> ExitCode {`
  - Purpose: 'run_gobby_owned' validates that 'args.cli' and 'args.hook_type' are present, short-circuits for disabled hooks or planned shutdown, handles statusline hooks by reading stdin and delegating to 'statusline::handle', and otherwise resolves the project context and captures stdin in preparation for normal hook dispatch, returning an appropriate 'ExitCode' on early exits. [crates/ghook/src/main.rs:126-289]
- `continue_action` (function) component `continue_action [function]` (`2d8783f2-188c-535b-baf8-4e63d7a73614`) lines 291-297 [crates/ghook/src/main.rs:291-297]
  - Signature: `fn continue_action() -> HookAction {`
  - Purpose: Returns a 'HookAction' with 'exit_code' set to '0', 'stdout_json' containing '{"continue": true}', and no 'stderr_message', signaling that execution should continue. [crates/ghook/src/main.rs:291-297]
- `emit_empty_json` (function) component `emit_empty_json [function]` (`b5520f3a-fb3a-5d17-9567-35b8f83eec78`) lines 299-301 [crates/ghook/src/main.rs:299-301]
  - Signature: `fn emit_empty_json() {`
  - Purpose: Writes an empty JSON object followed by a newline to standard output. [crates/ghook/src/main.rs:299-301]
- `hooks_disabled_by_env` (function) component `hooks_disabled_by_env [function]` (`40e9878e-caeb-5d05-a21a-48bc8e156a0c`) lines 303-305 [crates/ghook/src/main.rs:303-305]
  - Signature: `fn hooks_disabled_by_env() -> bool {`
  - Purpose: Returns 'true' only when the 'GOBBY_HOOKS_DISABLED' environment variable is set to the exact string '"1"', and 'false' otherwise. [crates/ghook/src/main.rs:303-305]
- `build_dispatch_envelope` (function) component `build_dispatch_envelope [function]` (`dfe102a7-844a-58d7-a61a-2ddfd8af78c5`) lines 307-335 [crates/ghook/src/main.rs:307-335]
  - Signature: `fn build_dispatch_envelope(`
  - Purpose: Builds an 'Envelope' for a hook invocation by optionally injecting terminal context into the JSON input, populating 'X-Gobby-Project-Id' and non-empty 'X-Gobby-Session-Id' headers, and setting the critical flag from 'CliConfig' before calling 'Envelope::new' with the detected source. [crates/ghook/src/main.rs:307-335]
- `emit_action` (function) component `emit_action [function]` (`d8b40289-d659-593d-bd9c-72f619ffc3bb`) lines 337-345 [crates/ghook/src/main.rs:337-345]
  - Signature: `fn emit_action(action: HookAction) -> ExitCode {`
  - Purpose: 'emit_action' writes an optional JSON payload to stdout, writes an optional trimmed stderr message surrounded by newlines, and returns an 'ExitCode' constructed from 'action.exit_code'. [crates/ghook/src/main.rs:337-345]
- `action_from_success_response` (function) component `action_from_success_response [function]` (`094be0ed-401a-5f46-9e62-a10b029f7c39`) lines 347-417 [crates/ghook/src/main.rs:347-417]
  - Signature: `fn action_from_success_response(`
  - Purpose: Parses a successful hook response body into a 'HookAction', returning a no-op for blank input, JSON-parsing and canonicalizing nonempty output, and then applying source-specific rules for 'droid', 'claude', and blocked results to decide the exit code, stdout JSON, and stderr message. [crates/ghook/src/main.rs:347-417]
- `action_from_droid_success` (function) component `action_from_droid_success [function]` (`528d15bd-7d26-5e92-8a1d-9898be9c4048`) lines 419-438 [crates/ghook/src/main.rs:419-438]
  - Signature: `fn action_from_droid_success(result: Value, serialized: String) -> HookAction {`
  - Purpose: Returns a 'HookAction' that exits with code '2' and emits the serialized JSON plus an extracted error reason when 'result.continue == false', otherwise exits '0' and includes the serialized JSON on stdout only if 'result' is Python-truthy. [crates/ghook/src/main.rs:419-438]
- `action_from_failure` (function) component `action_from_failure [function]` (`bd3daea7-e3c6-5498-87b0-2b83a2eec2af`) lines 440-500 [crates/ghook/src/main.rs:440-500]
  - Signature: `fn action_from_failure(`
  - Purpose: Maps a 'transport::DeliveryFailureKind' to a failing 'HookAction', emitting source- and error-specific stderr text, returning exit code '1' for 'droid' failures, and returning exit code '2' with fail-safe blocking messages for critical hooks. [crates/ghook/src/main.rs:440-500]
- `is_blocked` (function) component `is_blocked [function]` (`568e6201-8996-51fe-80e1-fd4a9426321f`) lines 502-524 [crates/ghook/src/main.rs:502-524]
  - Signature: `fn is_blocked(result: &Value) -> bool {`
  - Purpose: Returns 'true' when 'result' is an object whose 'continue' field is 'false', whose 'decision' is '"deny"' or '"block"', whose top-level 'permissionDecision' is '"deny"', or whose nested 'hookSpecificOutput.permissionDecision' is '"deny"'; otherwise returns 'false'. [crates/ghook/src/main.rs:502-524]
- `extract_reason` (function) component `extract_reason [function]` (`4fa09064-905f-5260-a275-4a70fd4ea731`) lines 526-554 [crates/ghook/src/main.rs:526-554]
  - Signature: `fn extract_reason(result: &Value) -> String {`
  - Purpose: Returns the first non-empty reason string found in 'result' under 'stopReason', 'user_message', 'reason', or nested 'hookSpecificOutput.permissionDecisionReason'/'reason', otherwise defaults to '"Blocked by hook"'. [crates/ghook/src/main.rs:526-554]
- `write_runtime_stamp` (function) component `write_runtime_stamp [function]` (`8574adfe-9f39-5b74-82f7-ad71301bd635`) lines 556-568 [crates/ghook/src/main.rs:556-568]
  - Signature: `fn write_runtime_stamp() -> Result<()> {`
  - Purpose: Creates '~/.gobby/bin/.ghook-runtime.json' with pretty-printed schema and 'ghook' version metadata, atomically writes it, prints 'ghook <version>' to stdout, and returns success or any I/O/serialization error. [crates/ghook/src/main.rs:556-568]
- `with_tmux_env` (function) component `with_tmux_env [function]` (`0d89e513-ac43-50de-a5a4-d4fdd54101ea`) lines 579-582 [crates/ghook/src/main.rs:579-582]
  - Signature: `fn with_tmux_env<T>(tmux: Option<&str>, tmux_pane: Option<&str>, f: impl FnOnce() -> T) -> T {`
  - Purpose: Acquires a global environment lock and executes 'f' with 'TMUX' and 'TMUX_PANE' temporarily set to the provided optional values via 'temp_env::with_vars'. [crates/ghook/src/main.rs:579-582]
- `dispatch_envelope_injects_valid_tmux_pane_for_session_start` (function) component `dispatch_envelope_injects_valid_tmux_pane_for_session_start [function]` (`0be42067-4564-5016-b8ad-82238c6b08cb`) lines 585-597 [crates/ghook/src/main.rs:585-597]
  - Signature: `fn dispatch_envelope_injects_valid_tmux_pane_for_session_start() {`
  - Purpose: Verifies that 'build_dispatch_envelope' populates 'terminal_context.tmux_pane' with the current tmux pane ID ('%17') when dispatching a 'SessionStart' envelope under a tmux environment. [crates/ghook/src/main.rs:585-597]
- `dispatch_envelope_omits_terminal_context_for_tool_hooks` (function) component `dispatch_envelope_omits_terminal_context_for_tool_hooks [function]` (`23d1368a-e0f1-511f-8973-6a04cbe0fc05`) lines 600-608 [crates/ghook/src/main.rs:600-608]
  - Signature: `fn dispatch_envelope_omits_terminal_context_for_tool_hooks() {`
  - Purpose: Verifies that 'build_dispatch_envelope' omits the 'terminal_context' field when constructing a 'PreToolUse' dispatch envelope for a tool hook. [crates/ghook/src/main.rs:600-608]
- `dispatch_envelope_nulls_tmux_fields_for_missing_or_invalid_tmux_pane` (function) component `dispatch_envelope_nulls_tmux_fields_for_missing_or_invalid_tmux_pane [function]` (`c1b47df2-70e8-5f71-ad8e-80786ead4fc9`) lines 611-651 [crates/ghook/src/main.rs:611-651]
  - Signature: `fn dispatch_envelope_nulls_tmux_fields_for_missing_or_invalid_tmux_pane() {`
  - Purpose: Verifies that 'build_dispatch_envelope' sets 'terminal_context.tmux_pane' and 'terminal_context.tmux_socket_path' to 'null' when the tmux pane value is missing or invalid, including when the tmux environment itself is absent. [crates/ghook/src/main.rs:611-651]
- `action_from_success_forwards_sessionstart_context_json` (function) component `action_from_success_forwards_sessionstart_context_json [function]` (`ac6569ae-6f86-5e82-8370-849fe970183a`) lines 654-675 [crates/ghook/src/main.rs:654-675]
  - Signature: `fn action_from_success_forwards_sessionstart_context_json() {`
  - Purpose: Verifies that 'action_from_success_response' for a 'SessionStart' hook preserves the 'hookSpecificOutput' JSON, including 'hookEventName' and 'additionalContext', while returning a successful action with exit code 0 and no stderr. [crates/ghook/src/main.rs:654-675]
- `action_from_success_treats_codex_pretool_deny_as_json_block` (function) component `action_from_success_treats_codex_pretool_deny_as_json_block [function]` (`11ef1c20-6ac4-5c90-82fd-b8ed5c6e2dd2`) lines 678-694 [crates/ghook/src/main.rs:678-694]
  - Signature: `fn action_from_success_treats_codex_pretool_deny_as_json_block() {`
  - Purpose: Verifies that 'action_from_success_response' converts a Codex 'PreToolUse' success payload with 'permissionDecision:"deny"' into a zero-exit action whose parsed 'stdout_json' preserves the deny decision and whose 'stderr_message' is 'None'. [crates/ghook/src/main.rs:678-694]
- `action_from_success_surfaces_nested_permission_decision_reason` (function) component `action_from_success_surfaces_nested_permission_decision_reason [function]` (`e18a39e3-96c8-54b4-a254-e8f9746a3826`) lines 697-713 [crates/ghook/src/main.rs:697-713]
  - Signature: `fn action_from_success_surfaces_nested_permission_decision_reason() {`
  - Purpose: Verifies that 'action_from_success_response' returns a successful action with exit code 0 and preserves a nested 'hookSpecificOutput.permissionDecisionReason' field in the emitted stdout JSON while leaving 'stderr_message' unset. [crates/ghook/src/main.rs:697-713]
- `action_from_success_preserves_additional_context_on_claude_block` (function) component `action_from_success_preserves_additional_context_on_claude_block [function]` (`c1f2a53d-2ed2-519d-8ee3-ed1b31b2e341`) lines 716-733 [crates/ghook/src/main.rs:716-733]
  - Signature: `fn action_from_success_preserves_additional_context_on_claude_block() {`
  - Purpose: Verifies that 'action_from_success_response' for a Claude 'PreToolUse' hook preserves 'hookSpecificOutput.additionalContext' in the returned stdout JSON while yielding exit code 0 and no stderr message. [crates/ghook/src/main.rs:716-733]
- `action_from_success_preserves_user_prompt_submit_block_json` (function) component `action_from_success_preserves_user_prompt_submit_block_json [function]` (`cca571b4-04b3-5e30-8816-4128d1e7af44`) lines 736-754 [crates/ghook/src/main.rs:736-754]
  - Signature: `fn action_from_success_preserves_user_prompt_submit_block_json() {`
  - Purpose: Verifies that 'action_from_success_response' preserves a 'UserPromptSubmit' JSON block response’s 'decision', 'reason', and nested 'hookSpecificOutput.additionalContext' fields in 'stdout_json' while producing 'exit_code' 0 and no 'stderr_message'. [crates/ghook/src/main.rs:736-754]
- `action_from_success_treats_stop_block_as_exit_two` (function) component `action_from_success_treats_stop_block_as_exit_two [function]` (`61ca3292-9088-5897-966a-8615c61d1415`) lines 757-773 [crates/ghook/src/main.rs:757-773]
  - Signature: `fn action_from_success_treats_stop_block_as_exit_two() {`
  - Purpose: Verifies that 'action_from_success_response' maps a '"Stop"' decision with a '"block"' JSON result to a 'HookAction' with 'exit_code: 2', no 'stdout_json', and 'stderr_message' set to the block reason. [crates/ghook/src/main.rs:757-773]
- `action_from_success_claude_hard_stop_exits_two` (function) component `action_from_success_claude_hard_stop_exits_two [function]` (`5edf6eae-00a3-51fb-a7b9-5a3c805ba829`) lines 776-792 [crates/ghook/src/main.rs:776-792]
  - Signature: `fn action_from_success_claude_hard_stop_exits_two() {`
  - Purpose: Verifies that 'action_from_success_response("claude", "Stop", ...)' maps a hard-stop JSON response with 'continue:false' and stop reason '"Daemon halted run"' to a 'HookAction' with 'exit_code: 2', no stdout JSON, and 'stderr_message' set to that reason. [crates/ghook/src/main.rs:776-792]
- `action_from_success_claude_stop_with_permission_deny_no_exit_two` (function) component `action_from_success_claude_stop_with_permission_deny_no_exit_two [function]` (`30a4cf12-d637-5607-8d0a-9d8520bc3b95`) lines 795-806 [crates/ghook/src/main.rs:795-806]
  - Signature: `fn action_from_success_claude_stop_with_permission_deny_no_exit_two() {`
  - Purpose: Verifies that a successful 'claude' 'Stop' response with a 'permissionDecision' of 'deny' and no exit override still yields an action with 'exit_code == 0', populated 'stdout_json', and no 'stderr_message'. [crates/ghook/src/main.rs:795-806]
- `action_from_success_claude_continue_false_without_reason_does_not_exit_two` (function) component `action_from_success_claude_continue_false_without_reason_does_not_exit_two [function]` (`cc9082e3-997d-5d3a-b1f6-7edcc3da3471`) lines 809-815 [crates/ghook/src/main.rs:809-815]
  - Signature: `fn action_from_success_claude_continue_false_without_reason_does_not_exit_two() {`
  - Purpose: Verifies that 'action_from_success_response("claude", "Stop", {"continue":false})' produces an action with 'exit_code == 0' and no 'stderr_message', rather than exiting with code 2. [crates/ghook/src/main.rs:809-815]
- `action_from_success_treats_droid_continue_false_as_exit_two_with_json` (function) component `action_from_success_treats_droid_continue_false_as_exit_two_with_json [function]` (`39462197-82e3-502a-802a-f1a5f1a173b5`) lines 818-834 [crates/ghook/src/main.rs:818-834]
  - Signature: `fn action_from_success_treats_droid_continue_false_as_exit_two_with_json() {`
  - Purpose: Verifies that 'action_from_success_response' maps a Droid 'PreToolUse' success payload with 'continue:false' and 'stopReason:"Create a task first"' to an action with exit code '2', preserves the JSON stdout with 'continue' false, and sets the stderr message to 'Create a task first'. [crates/ghook/src/main.rs:818-834]
- `action_from_success_preserves_droid_block_json_without_exit_two` (function) component `action_from_success_preserves_droid_block_json_without_exit_two [function]` (`e783c0c2-0253-555f-a8b2-a868f36fd9a7`) lines 837-851 [crates/ghook/src/main.rs:837-851]
  - Signature: `fn action_from_success_preserves_droid_block_json_without_exit_two() {`
  - Purpose: Verifies that 'action_from_success_response' for a 'droid' '"Stop"' success payload preserves the JSON 'block' decision and reason in 'stdout_json', sets 'exit_code' to '0', and leaves 'stderr_message' unset. [crates/ghook/src/main.rs:837-851]
- `action_from_failure_blocks_critical_hooks` (function) component `action_from_failure_blocks_critical_hooks [function]` (`a31fb368-b0a5-5c99-9e21-f286d81af118`) lines 854-869 [crates/ghook/src/main.rs:854-869]
  - Signature: `fn action_from_failure_blocks_critical_hooks() {`
  - Purpose: Verifies that 'action_from_failure' for the critical 'SessionStart' hook on an HTTP failure returns exit code '2', produces no 'stdout_json', and emits a 'stderr_message' containing 'Hook error on critical hook 'SessionStart''. [crates/ghook/src/main.rs:854-869]
- `action_from_failure_returns_json_for_noncritical_hooks` (function) component `action_from_failure_returns_json_for_noncritical_hooks [function]` (`804d5e24-a7e0-52b8-b29c-8c4618af6521`) lines 872-885 [crates/ghook/src/main.rs:872-885]
  - Signature: `fn action_from_failure_returns_json_for_noncritical_hooks() {`
  - Purpose: Verifies that 'action_from_failure' returns a JSON stdout error payload for a noncritical 'PostToolUse' hook connect failure, with exit code '1', 'status' set to '"error"', message '"Daemon unreachable"', and no stderr message. [crates/ghook/src/main.rs:872-885]
- `action_from_failure_treats_timeout_like_python` (function) component `action_from_failure_treats_timeout_like_python [function]` (`b51d61f6-7bcb-5340-ab70-87c7ea88bc96`) lines 888-898 [crates/ghook/src/main.rs:888-898]
  - Signature: `fn action_from_failure_treats_timeout_like_python() {`
  - Purpose: Verifies that 'action_from_failure' maps a 'DeliveryFailureKind::Timeout' during 'PreToolUse' for 'claude' to exit code '1' and a JSON stdout message of '"Hook execution timeout"'. [crates/ghook/src/main.rs:888-898]
- `action_from_failure_treats_connect_on_critical_hook_as_exit_two` (function) component `action_from_failure_treats_connect_on_critical_hook_as_exit_two [function]` (`9a5f8dc2-b6f0-57bd-ab50-2d67d3fa5a14`) lines 901-914 [crates/ghook/src/main.rs:901-914]
  - Signature: `fn action_from_failure_treats_connect_on_critical_hook_as_exit_two() {`
  - Purpose: Verifies that 'action_from_failure' maps a 'DeliveryFailureKind::Connect' occurring on the critical 'Stop' hook to an exit code of '2', emits no stdout JSON, and returns the expected fail-safe stderr message. [crates/ghook/src/main.rs:901-914]
- `action_from_failure_returns_stderr_for_droid_transport_errors` (function) component `action_from_failure_returns_stderr_for_droid_transport_errors [function]` (`0e95b086-3657-5dd3-82a6-4b6591f5b018`) lines 917-930 [crates/ghook/src/main.rs:917-930]
  - Signature: `fn action_from_failure_returns_stderr_for_droid_transport_errors() {`
  - Purpose: Verifies that 'action_from_failure' maps a Droid 'Http' delivery failure in 'PreToolUse' to a nonzero exit code with no JSON stdout and a stderr message of 'Daemon error: Internal Server Error'. [crates/ghook/src/main.rs:917-930]
- `hooks_disabled_by_env_reads_env_var` (function) component `hooks_disabled_by_env_reads_env_var [function]` (`bf61da7f-1260-5c67-9825-5f6ac4fa364f`) lines 933-965 [crates/ghook/src/main.rs:933-965]
  - Signature: `fn hooks_disabled_by_env_reads_env_var() {`
  - Purpose: This test manipulates 'GOBBY_HOOKS_DISABLED' in the process environment to verify that 'hooks_disabled_by_env()' returns 'true' only when the variable is exactly '"1"' and 'false' when it is unset, '"0"', or empty. [crates/ghook/src/main.rs:933-965]
- `is_blocked_matches_dispatcher_patterns` (function) component `is_blocked_matches_dispatcher_patterns [function]` (`cbd0ca63-2a53-549c-8040-49c22eb9e129`) lines 968-977 [crates/ghook/src/main.rs:968-977]
  - Signature: `fn is_blocked_matches_dispatcher_patterns() {`
  - Purpose: Verifies that 'is_blocked' returns 'true' for dispatcher-style payloads indicating denial or continuation refusal, including nested 'hookSpecificOutput.permissionDecision', and 'false' for an approval decision. [crates/ghook/src/main.rs:968-977]

