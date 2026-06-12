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
  - 303-331
  - 333-341
  - 343-413
  - 415-434
  - 436-496
  - 498-520
  - 522-550
  - 552-564
  - 575-578
  - 581-593
  - 596-604
  - 607-647
  - 650-671
  - 674-690
  - 693-709
  - 712-729
  - 732-750
  - 753-769
  - 772-788
  - 791-802
  - 805-811
  - 814-830
  - 833-847
  - 850-865
  - 868-881
  - 884-894
  - 897-910
  - 913-926
  - 929-961
  - 964-973
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/ghook/src/main.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Purpose

`crates/ghook/src/main.rs` exposes 37 indexed API symbols.
[crates/ghook/src/main.rs:45-49]
[crates/ghook/src/main.rs:57-81]
[crates/ghook/src/main.rs:83-106]
[crates/ghook/src/main.rs:108-124]
[crates/ghook/src/main.rs:126-289]

## API Symbols

- `HookAction` (class) component `HookAction [class]` (`b7deea92-b69e-59db-b0f9-aa74c3168cf2`) lines 45-49 [crates/ghook/src/main.rs:45-49]
  - Signature: `struct HookAction {`
  - Purpose: Indexed class `HookAction` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:45-49]
- `Args` (class) component `Args [class]` (`6aae9f18-b7ef-5eef-b421-a457b7ea5592`) lines 57-81 [crates/ghook/src/main.rs:57-81]
  - Signature: `struct Args {`
  - Purpose: Indexed class `Args` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:57-81]
- `main` (function) component `main [function]` (`18168f09-19dd-51df-a93c-0d919181cb35`) lines 83-106 [crates/ghook/src/main.rs:83-106]
  - Signature: `fn main() -> ExitCode {`
  - Purpose: Indexed function `main` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:83-106]
- `run_diagnose` (function) component `run_diagnose [function]` (`a7cdbeb5-469f-58f0-9dc7-5f4cc7a9b8ea`) lines 108-124 [crates/ghook/src/main.rs:108-124]
  - Signature: `fn run_diagnose(args: &Args) -> ExitCode {`
  - Purpose: Indexed function `run_diagnose` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:108-124]
- `run_gobby_owned` (function) component `run_gobby_owned [function]` (`c6003e4b-082c-5bc3-b50c-64efd6160f60`) lines 126-289 [crates/ghook/src/main.rs:126-289]
  - Signature: `fn run_gobby_owned(args: &Args) -> ExitCode {`
  - Purpose: Indexed function `run_gobby_owned` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:126-289]
- `continue_action` (function) component `continue_action [function]` (`3cd667d6-af11-5d99-ac5f-ea3c1428080e`) lines 291-297 [crates/ghook/src/main.rs:291-297]
  - Signature: `fn continue_action() -> HookAction {`
  - Purpose: Indexed function `continue_action` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:291-297]
- `hooks_disabled_by_env` (function) component `hooks_disabled_by_env [function]` (`f1d23afb-d11b-58d8-b164-792b4be9e3f0`) lines 299-301 [crates/ghook/src/main.rs:299-301]
  - Signature: `fn hooks_disabled_by_env() -> bool {`
  - Purpose: Indexed function `hooks_disabled_by_env` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:299-301]
- `build_dispatch_envelope` (function) component `build_dispatch_envelope [function]` (`81abe270-a6b5-564e-8a5f-3493c0488684`) lines 303-331 [crates/ghook/src/main.rs:303-331]
  - Signature: `fn build_dispatch_envelope(`
  - Purpose: Indexed function `build_dispatch_envelope` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:303-331]
- `emit_action` (function) component `emit_action [function]` (`78c5e172-6548-5c83-89ec-babdf0ae6618`) lines 333-341 [crates/ghook/src/main.rs:333-341]
  - Signature: `fn emit_action(action: HookAction) -> ExitCode {`
  - Purpose: Indexed function `emit_action` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:333-341]
- `action_from_success_response` (function) component `action_from_success_response [function]` (`7bc923b0-648a-5ef1-a7d8-92e8050e90db`) lines 343-413 [crates/ghook/src/main.rs:343-413]
  - Signature: `fn action_from_success_response(`
  - Purpose: Indexed function `action_from_success_response` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:343-413]
- `action_from_droid_success` (function) component `action_from_droid_success [function]` (`7c600128-f2e8-5b0d-bc49-719f2707b958`) lines 415-434 [crates/ghook/src/main.rs:415-434]
  - Signature: `fn action_from_droid_success(result: Value, serialized: String) -> HookAction {`
  - Purpose: Indexed function `action_from_droid_success` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:415-434]
- `action_from_failure` (function) component `action_from_failure [function]` (`f557d416-7896-54a3-bb7e-eeb234f11ba0`) lines 436-496 [crates/ghook/src/main.rs:436-496]
  - Signature: `fn action_from_failure(`
  - Purpose: Indexed function `action_from_failure` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:436-496]
- `is_blocked` (function) component `is_blocked [function]` (`0e8fcaab-3029-5db8-b659-74d952fc6699`) lines 498-520 [crates/ghook/src/main.rs:498-520]
  - Signature: `fn is_blocked(result: &Value) -> bool {`
  - Purpose: Indexed function `is_blocked` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:498-520]
- `extract_reason` (function) component `extract_reason [function]` (`b3f37854-7e1d-58e2-b717-80d127e732f4`) lines 522-550 [crates/ghook/src/main.rs:522-550]
  - Signature: `fn extract_reason(result: &Value) -> String {`
  - Purpose: Indexed function `extract_reason` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:522-550]
- `write_runtime_stamp` (function) component `write_runtime_stamp [function]` (`8eb8af78-9ba0-5380-9259-bb31386939fd`) lines 552-564 [crates/ghook/src/main.rs:552-564]
  - Signature: `fn write_runtime_stamp() -> Result<()> {`
  - Purpose: Indexed function `write_runtime_stamp` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:552-564]
- `with_tmux_env` (function) component `with_tmux_env [function]` (`28ed3bc1-d502-5e4f-86c3-35da4990e90b`) lines 575-578 [crates/ghook/src/main.rs:575-578]
  - Signature: `fn with_tmux_env<T>(tmux: Option<&str>, tmux_pane: Option<&str>, f: impl FnOnce() -> T) -> T {`
  - Purpose: Indexed function `with_tmux_env` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:575-578]
- `dispatch_envelope_injects_valid_tmux_pane_for_session_start` (function) component `dispatch_envelope_injects_valid_tmux_pane_for_session_start [function]` (`0ef43db4-c8e2-5ba0-97fd-b8c92d8e432d`) lines 581-593 [crates/ghook/src/main.rs:581-593]
  - Signature: `fn dispatch_envelope_injects_valid_tmux_pane_for_session_start() {`
  - Purpose: Indexed function `dispatch_envelope_injects_valid_tmux_pane_for_session_start` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:581-593]
- `dispatch_envelope_omits_terminal_context_for_tool_hooks` (function) component `dispatch_envelope_omits_terminal_context_for_tool_hooks [function]` (`de1fbc6b-8bdf-5eb0-9645-1e6b00d62370`) lines 596-604 [crates/ghook/src/main.rs:596-604]
  - Signature: `fn dispatch_envelope_omits_terminal_context_for_tool_hooks() {`
  - Purpose: Indexed function `dispatch_envelope_omits_terminal_context_for_tool_hooks` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:596-604]
- `dispatch_envelope_nulls_tmux_fields_for_missing_or_invalid_tmux_pane` (function) component `dispatch_envelope_nulls_tmux_fields_for_missing_or_invalid_tmux_pane [function]` (`097bff57-1207-5c8f-8998-0a73eb840ae8`) lines 607-647 [crates/ghook/src/main.rs:607-647]
  - Signature: `fn dispatch_envelope_nulls_tmux_fields_for_missing_or_invalid_tmux_pane() {`
  - Purpose: Indexed function `dispatch_envelope_nulls_tmux_fields_for_missing_or_invalid_tmux_pane` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:607-647]
- `action_from_success_forwards_sessionstart_context_json` (function) component `action_from_success_forwards_sessionstart_context_json [function]` (`50718e31-2e10-5ee3-a281-0dd4e9f891b9`) lines 650-671 [crates/ghook/src/main.rs:650-671]
  - Signature: `fn action_from_success_forwards_sessionstart_context_json() {`
  - Purpose: Indexed function `action_from_success_forwards_sessionstart_context_json` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:650-671]
- `action_from_success_treats_codex_pretool_deny_as_json_block` (function) component `action_from_success_treats_codex_pretool_deny_as_json_block [function]` (`a3b57140-e96a-5a48-859c-30363bdf7774`) lines 674-690 [crates/ghook/src/main.rs:674-690]
  - Signature: `fn action_from_success_treats_codex_pretool_deny_as_json_block() {`
  - Purpose: Indexed function `action_from_success_treats_codex_pretool_deny_as_json_block` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:674-690]
- `action_from_success_surfaces_nested_permission_decision_reason` (function) component `action_from_success_surfaces_nested_permission_decision_reason [function]` (`a5d84a8a-b133-5da7-9011-c1a73acc3f8a`) lines 693-709 [crates/ghook/src/main.rs:693-709]
  - Signature: `fn action_from_success_surfaces_nested_permission_decision_reason() {`
  - Purpose: Indexed function `action_from_success_surfaces_nested_permission_decision_reason` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:693-709]
- `action_from_success_preserves_additional_context_on_claude_block` (function) component `action_from_success_preserves_additional_context_on_claude_block [function]` (`a273a2c4-e22f-5d4c-93c3-cf32660743d1`) lines 712-729 [crates/ghook/src/main.rs:712-729]
  - Signature: `fn action_from_success_preserves_additional_context_on_claude_block() {`
  - Purpose: Indexed function `action_from_success_preserves_additional_context_on_claude_block` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:712-729]
- `action_from_success_preserves_user_prompt_submit_block_json` (function) component `action_from_success_preserves_user_prompt_submit_block_json [function]` (`5e09f940-fd41-596e-b679-e0c0e03ec591`) lines 732-750 [crates/ghook/src/main.rs:732-750]
  - Signature: `fn action_from_success_preserves_user_prompt_submit_block_json() {`
  - Purpose: Indexed function `action_from_success_preserves_user_prompt_submit_block_json` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:732-750]
- `action_from_success_treats_stop_block_as_exit_two` (function) component `action_from_success_treats_stop_block_as_exit_two [function]` (`3bc38d23-725d-53ec-af28-b26995e83717`) lines 753-769 [crates/ghook/src/main.rs:753-769]
  - Signature: `fn action_from_success_treats_stop_block_as_exit_two() {`
  - Purpose: Indexed function `action_from_success_treats_stop_block_as_exit_two` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:753-769]
- `action_from_success_claude_hard_stop_exits_two` (function) component `action_from_success_claude_hard_stop_exits_two [function]` (`4b488b1f-5617-5f1e-87f8-92e3dd3d35b7`) lines 772-788 [crates/ghook/src/main.rs:772-788]
  - Signature: `fn action_from_success_claude_hard_stop_exits_two() {`
  - Purpose: Indexed function `action_from_success_claude_hard_stop_exits_two` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:772-788]
- `action_from_success_claude_stop_with_permission_deny_no_exit_two` (function) component `action_from_success_claude_stop_with_permission_deny_no_exit_two [function]` (`6ed23c5f-4a01-5e74-99d5-57bcbb565750`) lines 791-802 [crates/ghook/src/main.rs:791-802]
  - Signature: `fn action_from_success_claude_stop_with_permission_deny_no_exit_two() {`
  - Purpose: Indexed function `action_from_success_claude_stop_with_permission_deny_no_exit_two` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:791-802]
- `action_from_success_claude_continue_false_without_reason_does_not_exit_two` (function) component `action_from_success_claude_continue_false_without_reason_does_not_exit_two [function]` (`00c5f153-9c2c-56fc-979f-9a99a53fbe15`) lines 805-811 [crates/ghook/src/main.rs:805-811]
  - Signature: `fn action_from_success_claude_continue_false_without_reason_does_not_exit_two() {`
  - Purpose: Indexed function `action_from_success_claude_continue_false_without_reason_does_not_exit_two` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:805-811]
- `action_from_success_treats_droid_continue_false_as_exit_two_with_json` (function) component `action_from_success_treats_droid_continue_false_as_exit_two_with_json [function]` (`edc2b916-083b-5bdb-a6ac-32fa81db9d72`) lines 814-830 [crates/ghook/src/main.rs:814-830]
  - Signature: `fn action_from_success_treats_droid_continue_false_as_exit_two_with_json() {`
  - Purpose: Indexed function `action_from_success_treats_droid_continue_false_as_exit_two_with_json` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:814-830]
- `action_from_success_preserves_droid_block_json_without_exit_two` (function) component `action_from_success_preserves_droid_block_json_without_exit_two [function]` (`de65aea7-54d9-577b-a6b2-a51e5bd422cf`) lines 833-847 [crates/ghook/src/main.rs:833-847]
  - Signature: `fn action_from_success_preserves_droid_block_json_without_exit_two() {`
  - Purpose: Indexed function `action_from_success_preserves_droid_block_json_without_exit_two` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:833-847]
- `action_from_failure_blocks_critical_hooks` (function) component `action_from_failure_blocks_critical_hooks [function]` (`71752248-8bf5-5c9c-bbe4-51353d6b010a`) lines 850-865 [crates/ghook/src/main.rs:850-865]
  - Signature: `fn action_from_failure_blocks_critical_hooks() {`
  - Purpose: Indexed function `action_from_failure_blocks_critical_hooks` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:850-865]
- `action_from_failure_returns_json_for_noncritical_hooks` (function) component `action_from_failure_returns_json_for_noncritical_hooks [function]` (`f400851f-9095-5f48-814d-2f6055123c6d`) lines 868-881 [crates/ghook/src/main.rs:868-881]
  - Signature: `fn action_from_failure_returns_json_for_noncritical_hooks() {`
  - Purpose: Indexed function `action_from_failure_returns_json_for_noncritical_hooks` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:868-881]
- `action_from_failure_treats_timeout_like_python` (function) component `action_from_failure_treats_timeout_like_python [function]` (`e36c40a4-a579-5a44-852d-9d1c411eecc3`) lines 884-894 [crates/ghook/src/main.rs:884-894]
  - Signature: `fn action_from_failure_treats_timeout_like_python() {`
  - Purpose: Indexed function `action_from_failure_treats_timeout_like_python` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:884-894]
- `action_from_failure_treats_connect_on_critical_hook_as_exit_two` (function) component `action_from_failure_treats_connect_on_critical_hook_as_exit_two [function]` (`589f7555-91ba-55fd-ab93-f5c80507857a`) lines 897-910 [crates/ghook/src/main.rs:897-910]
  - Signature: `fn action_from_failure_treats_connect_on_critical_hook_as_exit_two() {`
  - Purpose: Indexed function `action_from_failure_treats_connect_on_critical_hook_as_exit_two` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:897-910]
- `action_from_failure_returns_stderr_for_droid_transport_errors` (function) component `action_from_failure_returns_stderr_for_droid_transport_errors [function]` (`92a4c9ca-3cd2-5360-b9d2-e03f5917449d`) lines 913-926 [crates/ghook/src/main.rs:913-926]
  - Signature: `fn action_from_failure_returns_stderr_for_droid_transport_errors() {`
  - Purpose: Indexed function `action_from_failure_returns_stderr_for_droid_transport_errors` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:913-926]
- `hooks_disabled_by_env_reads_env_var` (function) component `hooks_disabled_by_env_reads_env_var [function]` (`75293c20-7800-58c1-bd4a-29b484058eb7`) lines 929-961 [crates/ghook/src/main.rs:929-961]
  - Signature: `fn hooks_disabled_by_env_reads_env_var() {`
  - Purpose: Indexed function `hooks_disabled_by_env_reads_env_var` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:929-961]
- `is_blocked_matches_dispatcher_patterns` (function) component `is_blocked_matches_dispatcher_patterns [function]` (`feddd93c-bed0-50e0-8ffd-4128c2677d50`) lines 964-973 [crates/ghook/src/main.rs:964-973]
  - Signature: `fn is_blocked_matches_dispatcher_patterns() {`
  - Purpose: Indexed function `is_blocked_matches_dispatcher_patterns` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:964-973]

