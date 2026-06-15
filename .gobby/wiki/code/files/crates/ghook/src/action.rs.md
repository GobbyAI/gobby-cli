---
title: crates/ghook/src/action.rs
type: code_file
provenance:
- file: crates/ghook/src/action.rs
  ranges:
  - 8-12
  - 14-20
  - 22-24
  - 26-34
  - 36-106
  - 108-127
  - 129-189
  - 191-213
  - 215-243
  - 252-273
  - 276-292
  - 295-311
  - 314-331
  - 334-352
  - 355-371
  - 374-390
  - 393-404
  - 407-413
  - 416-432
  - 435-449
  - 452-467
  - 470-483
  - 486-496
  - 499-512
  - 515-528
  - 531-540
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/ghook/src/action.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Purpose

Defines the hook-action layer for `ghook`: a small crate-visible `HookAction` record carries an exit code plus optional JSON stdout and stderr text, and helper functions build, emit, and translate hook outcomes into that form. Successful responses are trimmed, parsed as JSON, and mapped differently for `droid`, `claude`, and other sources, with special handling for blocked/denied payloads and extracted reasons; delivery failures are converted into fail-safe actions based on source, hook criticality, and failure kind. The rest of the file is a focused test suite that checks these mappings preserve the expected JSON fields, stderr messages, and exit codes.
[crates/ghook/src/action.rs:8-12]
[crates/ghook/src/action.rs:14-20]
[crates/ghook/src/action.rs:22-24]
[crates/ghook/src/action.rs:26-34]
[crates/ghook/src/action.rs:36-106]

## API Symbols

- `HookAction` (class) component `HookAction [class]` (`f5dd5560-82fb-5444-90ec-c52f14453103`) lines 8-12 [crates/ghook/src/action.rs:8-12]
  - Signature: `pub(crate) struct HookAction {`
  - Purpose: 'HookAction' is a crate-visible struct that captures a hook’s result as an 8-bit exit code plus optional JSON-formatted stdout and optional stderr message strings. [crates/ghook/src/action.rs:8-12]
- `continue_action` (function) component `continue_action [function]` (`f7f34afc-91e9-5d08-9c85-a1d2c956cfd8`) lines 14-20 [crates/ghook/src/action.rs:14-20]
  - Signature: `pub(crate) fn continue_action() -> HookAction {`
  - Purpose: Returns a 'HookAction' with 'exit_code' set to '0', 'stdout_json' containing '{"continue": true}', and no stderr message. [crates/ghook/src/action.rs:14-20]
- `emit_empty_json` (function) component `emit_empty_json [function]` (`a0e2dc98-470a-5a92-b323-c3897cdac1bd`) lines 22-24 [crates/ghook/src/action.rs:22-24]
  - Signature: `pub(crate) fn emit_empty_json() {`
  - Purpose: Writes an empty JSON object followed by a newline to standard output. [crates/ghook/src/action.rs:22-24]
- `emit_action` (function) component `emit_action [function]` (`53a2cebe-fa56-5b23-b6e2-aff808c32b5b`) lines 26-34 [crates/ghook/src/action.rs:26-34]
  - Signature: `pub(crate) fn emit_action(action: HookAction) -> ExitCode {`
  - Purpose: Writes the action’s optional JSON to stdout, its optional trimmed stderr message surrounded by newlines to stderr, and returns an 'ExitCode' constructed from 'action.exit_code'. [crates/ghook/src/action.rs:26-34]
- `action_from_success_response` (function) component `action_from_success_response [function]` (`7943af65-4575-5a6f-9788-0a7d2baa60b5`) lines 36-106 [crates/ghook/src/action.rs:36-106]
  - Signature: `pub(crate) fn action_from_success_response(`
  - Purpose: 'action_from_success_response' trims the response body, returns a no-op 'HookAction' for empty output, parses non-empty output as JSON, and then maps it into a source-specific 'HookAction' with special handling for 'droid', 'claude', and blocked responses (including 'continue:false'/'stopReason' on Claude). [crates/ghook/src/action.rs:36-106]
- `action_from_droid_success` (function) component `action_from_droid_success [function]` (`878d10af-1a06-51a8-8f6d-d3bba3752a2a`) lines 108-127 [crates/ghook/src/action.rs:108-127]
  - Signature: `fn action_from_droid_success(result: Value, serialized: String) -> HookAction {`
  - Purpose: Returns a 'HookAction' that exits with code '2' and emits the serialized result plus an extracted reason on stderr when 'result.continue == false', otherwise exits '0' and includes the serialized JSON on stdout only if the result is Python-truthy. [crates/ghook/src/action.rs:108-127]
- `action_from_failure` (function) component `action_from_failure [function]` (`f3e134e5-9f40-5b9e-80cc-5c148e09d975`) lines 129-189 [crates/ghook/src/action.rs:129-189]
  - Signature: `pub(crate) fn action_from_failure(`
  - Purpose: Maps a delivery failure into a 'HookAction', using 'exit_code = 1' with daemon-oriented messages for 'cfg.source == "droid"', 'exit_code = 2' with fail-safe critical-hook error text when 'cfg.is_critical_hook(hook_type)' is true, and otherwise formatting a non-critical failure message based on the 'DeliveryFailureKind'. [crates/ghook/src/action.rs:129-189]
- `is_blocked` (function) component `is_blocked [function]` (`7f389900-230b-5d25-9703-a26670c58474`) lines 191-213 [crates/ghook/src/action.rs:191-213]
  - Signature: `fn is_blocked(result: &Value) -> bool {`
  - Purpose: Returns 'true' when 'result' is a JSON object indicating denial or blocking via 'continue == false', 'decision' equal to '"deny"' or '"block"', 'permissionDecision == "deny"', or nested 'hookSpecificOutput.permissionDecision == "deny"'; otherwise returns 'false'. [crates/ghook/src/action.rs:191-213]
- `extract_reason` (function) component `extract_reason [function]` (`508c1c2e-6c93-5d01-9766-ce34b69ade39`) lines 215-243 [crates/ghook/src/action.rs:215-243]
  - Signature: `fn extract_reason(result: &Value) -> String {`
  - Purpose: Returns the first non-empty reason string found in 'result' by checking top-level 'stopReason', 'user_message', and 'reason', then nested 'hookSpecificOutput.permissionDecisionReason' or 'hookSpecificOutput.reason', and falls back to '"Blocked by hook"' if 'result' is not an object or no reason is present. [crates/ghook/src/action.rs:215-243]
- `action_from_success_forwards_sessionstart_context_json` (function) component `action_from_success_forwards_sessionstart_context_json [function]` (`b0f88c8a-e48b-5c3e-9a97-e372b2692a29`) lines 252-273 [crates/ghook/src/action.rs:252-273]
  - Signature: `fn action_from_success_forwards_sessionstart_context_json() {`
  - Purpose: Verifies that 'action_from_success_response' for a 'SessionStart' hook returns a successful action whose JSON stdout preserves the 'decision' and 'hookSpecificOutput' fields, including 'hookEventName' and 'additionalContext', with exit code 0 and no stderr. [crates/ghook/src/action.rs:252-273]
- `action_from_success_treats_codex_pretool_deny_as_json_block` (function) component `action_from_success_treats_codex_pretool_deny_as_json_block [function]` (`7f885d7d-c804-5a80-8084-03cd78960082`) lines 276-292 [crates/ghook/src/action.rs:276-292]
  - Signature: `fn action_from_success_treats_codex_pretool_deny_as_json_block() {`
  - Purpose: Verifies that 'action_from_success_response' treats a Codex 'PreToolUse' success payload with 'decision:"block"' and 'permissionDecision:"deny"' as a successful action with exit code '0', preserved JSON stdout containing the deny flag, and no stderr message. [crates/ghook/src/action.rs:276-292]
- `action_from_success_surfaces_nested_permission_decision_reason` (function) component `action_from_success_surfaces_nested_permission_decision_reason [function]` (`f62c6e5c-cd61-5335-b502-c6d8ec2b044f`) lines 295-311 [crates/ghook/src/action.rs:295-311]
  - Signature: `fn action_from_success_surfaces_nested_permission_decision_reason() {`
  - Purpose: Verifies that a successful 'action_from_success_response' for a 'PreToolUse' hook preserves and surfaces the nested 'hookSpecificOutput.permissionDecisionReason' in the parsed stdout JSON, while returning exit code '0' and no stderr message. [crates/ghook/src/action.rs:295-311]
- `action_from_success_preserves_additional_context_on_claude_block` (function) component `action_from_success_preserves_additional_context_on_claude_block [function]` (`4d4e6520-a366-57ba-816c-e2850ac098ed`) lines 314-331 [crates/ghook/src/action.rs:314-331]
  - Signature: `fn action_from_success_preserves_additional_context_on_claude_block() {`
  - Purpose: Verifies that 'action_from_success_response' for a Claude 'PreToolUse' success payload returns exit code '0', no stderr, and preserves 'hookSpecificOutput.additionalContext' unchanged in the emitted stdout JSON. [crates/ghook/src/action.rs:314-331]
- `action_from_success_preserves_user_prompt_submit_block_json` (function) component `action_from_success_preserves_user_prompt_submit_block_json [function]` (`386ef81c-1c92-53f0-9b74-7a8e9de97905`) lines 334-352 [crates/ghook/src/action.rs:334-352]
  - Signature: `fn action_from_success_preserves_user_prompt_submit_block_json() {`
  - Purpose: Verifies that 'action_from_success_response' for a 'UserPromptSubmit' hook returns exit code 0, preserves the JSON 'decision', 'reason', and nested 'hookSpecificOutput.additionalContext' fields in 'stdout_json', and produces no 'stderr_message'. [crates/ghook/src/action.rs:334-352]
- `action_from_success_treats_stop_block_as_exit_two` (function) component `action_from_success_treats_stop_block_as_exit_two [function]` (`6c09b433-2e48-5a35-8569-597437823e71`) lines 355-371 [crates/ghook/src/action.rs:355-371]
  - Signature: `fn action_from_success_treats_stop_block_as_exit_two() {`
  - Purpose: Verifies that 'action_from_success_response' converts a '"Stop"' response with '{"decision":"block"}' into a 'HookAction' with 'exit_code: 2', no 'stdout_json', and the provided reason in 'stderr_message'. [crates/ghook/src/action.rs:355-371]
- `action_from_success_claude_hard_stop_exits_two` (function) component `action_from_success_claude_hard_stop_exits_two [function]` (`d26f5a56-d6d1-5b4b-a9d4-bba1710f7a37`) lines 374-390 [crates/ghook/src/action.rs:374-390]
  - Signature: `fn action_from_success_claude_hard_stop_exits_two() {`
  - Purpose: Verifies that 'action_from_success_response("claude", "Stop", ...)' maps a success payload with 'continue:false' and stop reason 'Daemon halted run' to a 'HookAction' with 'exit_code: 2', 'stderr_message: Some("Daemon halted run")', and 'stdout_json: None'. [crates/ghook/src/action.rs:374-390]
- `action_from_success_claude_stop_with_permission_deny_no_exit_two` (function) component `action_from_success_claude_stop_with_permission_deny_no_exit_two [function]` (`01ba2b47-3993-5e79-a5c4-b1d9417b1295`) lines 393-404 [crates/ghook/src/action.rs:393-404]
  - Signature: `fn action_from_success_claude_stop_with_permission_deny_no_exit_two() {`
  - Purpose: Verifies that 'action_from_success_response' maps a Claude 'Stop' result with 'permissionDecision: "deny"' and no explicit exit data into a successful action with 'exit_code == 0', 'stdout_json' present, and no 'stderr_message'. [crates/ghook/src/action.rs:393-404]
- `action_from_success_claude_continue_false_without_reason_does_not_exit_two` (function) component `action_from_success_claude_continue_false_without_reason_does_not_exit_two [function]` (`81126c57-cc7f-59bc-a418-b5e6d245b775`) lines 407-413 [crates/ghook/src/action.rs:407-413]
  - Signature: `fn action_from_success_claude_continue_false_without_reason_does_not_exit_two() {`
  - Purpose: Verifies that 'action_from_success_response("claude", "Stop", {"continue":false})' produces a successful action with 'exit_code == 0' and no 'stderr_message', rather than exiting with code 2. [crates/ghook/src/action.rs:407-413]
- `action_from_success_treats_droid_continue_false_as_exit_two_with_json` (function) component `action_from_success_treats_droid_continue_false_as_exit_two_with_json [function]` (`b9db8a12-d623-524a-9dab-0ece537db020`) lines 416-432 [crates/ghook/src/action.rs:416-432]
  - Signature: `fn action_from_success_treats_droid_continue_false_as_exit_two_with_json() {`
  - Purpose: Verifies that 'action_from_success_response' maps a 'droid' 'PreToolUse' success payload with '{"continue":false,"stopReason":"Create a task first"}' to an action with 'exit_code' 2, preserves the JSON in 'stdout_json', and sets 'stderr_message' to the stop reason. [crates/ghook/src/action.rs:416-432]
- `action_from_success_preserves_droid_block_json_without_exit_two` (function) component `action_from_success_preserves_droid_block_json_without_exit_two [function]` (`ac7a2683-4f39-53e9-8fed-8bf949abe7b8`) lines 435-449 [crates/ghook/src/action.rs:435-449]
  - Signature: `fn action_from_success_preserves_droid_block_json_without_exit_two() {`
  - Purpose: Verifies that 'action_from_success_response("droid", "Stop", "{\"decision\":\"block\",\"reason\":\"Task still in progress\"}")' returns a successful action with 'exit_code == 0', preserves the JSON payload in 'stdout_json' with 'decision="block"' and the given reason, and leaves 'stderr_message' unset. [crates/ghook/src/action.rs:435-449]
- `action_from_failure_blocks_critical_hooks` (function) component `action_from_failure_blocks_critical_hooks [function]` (`0ebbc49b-d873-572f-b040-a9df9661de4d`) lines 452-467 [crates/ghook/src/action.rs:452-467]
  - Signature: `fn action_from_failure_blocks_critical_hooks() {`
  - Purpose: Verifies that an HTTP delivery failure for the critical 'SessionStart' hook produces an action with exit code '2', no JSON stdout, and a stderr message containing 'Hook error on critical hook 'SessionStart''. [crates/ghook/src/action.rs:452-467]
- `action_from_failure_returns_json_for_noncritical_hooks` (function) component `action_from_failure_returns_json_for_noncritical_hooks [function]` (`8c567c91-48d2-57b8-bf80-8b01cbf75b4e`) lines 470-483 [crates/ghook/src/action.rs:470-483]
  - Signature: `fn action_from_failure_returns_json_for_noncritical_hooks() {`
  - Purpose: Verifies that 'action_from_failure' for a noncritical 'PostToolUse' hook on 'DeliveryFailureKind::Connect' returns exit code '1', emits JSON to stdout with 'status: "error"' and message '"Daemon unreachable"', and produces no stderr message. [crates/ghook/src/action.rs:470-483]
- `action_from_failure_treats_timeout_like_python` (function) component `action_from_failure_treats_timeout_like_python [function]` (`b560222e-c106-56c2-b2d5-5767deb0befb`) lines 486-496 [crates/ghook/src/action.rs:486-496]
  - Signature: `fn action_from_failure_treats_timeout_like_python() {`
  - Purpose: Asserts that 'action_from_failure' maps a 'DeliveryFailureKind::Timeout' during 'PreToolUse' dispatch to exit code '1' and a JSON stdout message of '"Hook execution timeout"'. [crates/ghook/src/action.rs:486-496]
- `action_from_failure_treats_connect_on_critical_hook_as_exit_two` (function) component `action_from_failure_treats_connect_on_critical_hook_as_exit_two [function]` (`46b23092-7854-5a75-a3c3-64a9bb32ab49`) lines 499-512 [crates/ghook/src/action.rs:499-512]
  - Signature: `fn action_from_failure_treats_connect_on_critical_hook_as_exit_two() {`
  - Purpose: Verifies that 'action_from_failure' maps a 'DeliveryFailureKind::Connect' occurring on the critical 'Stop' hook to a fail-safe exit code of '2', emits no 'stdout_json', and sets the expected stderr message. [crates/ghook/src/action.rs:499-512]
- `action_from_failure_returns_stderr_for_droid_transport_errors` (function) component `action_from_failure_returns_stderr_for_droid_transport_errors [function]` (`8ecf33c0-a92d-5b09-9597-2c43d1f64282`) lines 515-528 [crates/ghook/src/action.rs:515-528]
  - Signature: `fn action_from_failure_returns_stderr_for_droid_transport_errors() {`
  - Purpose: Verifies that 'action_from_failure' maps a 'droid' dispatch HTTP failure to exit code '1', omits 'stdout_json', and sets 'stderr_message' to 'Daemon error: Internal Server Error'. [crates/ghook/src/action.rs:515-528]
- `is_blocked_matches_dispatcher_patterns` (function) component `is_blocked_matches_dispatcher_patterns [function]` (`8c4d5e40-b536-5aa5-85cf-cd46e8578cf5`) lines 531-540 [crates/ghook/src/action.rs:531-540]
  - Signature: `fn is_blocked_matches_dispatcher_patterns() {`
  - Purpose: Verifies that 'is_blocked' returns 'true' for dispatcher-style payloads indicating denial or a 'continue: false' flag, including nested 'hookSpecificOutput.permissionDecision', and 'false' for an approval decision. [crates/ghook/src/action.rs:531-540]

