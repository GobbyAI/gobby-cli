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
[crates/ghook/src/main.rs:261-267]
[crates/ghook/src/main.rs:269-271]
[crates/ghook/src/main.rs:273-301]
[crates/ghook/src/main.rs:303-317]
[crates/ghook/src/main.rs:319-327]
[crates/ghook/src/main.rs:329-399]
[crates/ghook/src/main.rs:401-420]
[crates/ghook/src/main.rs:422-482]
[crates/ghook/src/main.rs:484-506]
[crates/ghook/src/main.rs:508-536]
[crates/ghook/src/main.rs:538-555]
[crates/ghook/src/main.rs:557-570]
[crates/ghook/src/main.rs:581-584]
[crates/ghook/src/main.rs:587-599]
[crates/ghook/src/main.rs:602-610]
[crates/ghook/src/main.rs:613-653]
[crates/ghook/src/main.rs:656-677]
[crates/ghook/src/main.rs:680-696]
[crates/ghook/src/main.rs:699-715]
[crates/ghook/src/main.rs:718-735]
[crates/ghook/src/main.rs:738-756]
[crates/ghook/src/main.rs:759-775]
[crates/ghook/src/main.rs:778-794]
[crates/ghook/src/main.rs:797-808]
[crates/ghook/src/main.rs:811-817]
[crates/ghook/src/main.rs:820-836]
[crates/ghook/src/main.rs:839-853]
[crates/ghook/src/main.rs:856-871]
[crates/ghook/src/main.rs:874-887]
[crates/ghook/src/main.rs:890-900]
[crates/ghook/src/main.rs:903-916]
[crates/ghook/src/main.rs:919-932]
[crates/ghook/src/main.rs:935-967]
[crates/ghook/src/main.rs:970-979]

## API Symbols

- `HookAction` (class) component `HookAction [class]` (`621b3717-b526-5256-b568-1fe551b4cc35`) lines 38-42 [crates/ghook/src/main.rs:38-42]
  - Signature: `struct HookAction {`
  - Purpose: Indexed class `HookAction` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:38-42]
- `Args` (class) component `Args [class]` (`fd4cad88-5526-5a34-aeda-24b4397cbc24`) lines 50-74 [crates/ghook/src/main.rs:50-74]
  - Signature: `struct Args {`
  - Purpose: Indexed class `Args` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:50-74]
- `main` (function) component `main [function]` (`938b2354-40c9-5831-b1ef-55074d23b6dc`) lines 76-99 [crates/ghook/src/main.rs:76-99]
  - Signature: `fn main() -> ExitCode {`
  - Purpose: Indexed function `main` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:76-99]
- `run_diagnose` (function) component `run_diagnose [function]` (`0c1a1e6c-7edb-5845-a6f1-14169f776367`) lines 101-117 [crates/ghook/src/main.rs:101-117]
  - Signature: `fn run_diagnose(args: &Args) -> ExitCode {`
  - Purpose: Indexed function `run_diagnose` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:101-117]
- `run_gobby_owned` (function) component `run_gobby_owned [function]` (`eb63dfc4-2dcb-576f-82c0-777e7a3b8df5`) lines 119-259 [crates/ghook/src/main.rs:119-259]
  - Signature: `fn run_gobby_owned(args: &Args) -> ExitCode {`
  - Purpose: Indexed function `run_gobby_owned` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:119-259]
- `continue_action` (function) component `continue_action [function]` (`56d0517b-3b9f-5ecd-b481-815b11372cd1`) lines 261-267 [crates/ghook/src/main.rs:261-267]
  - Signature: `fn continue_action() -> HookAction {`
  - Purpose: Indexed function `continue_action` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:261-267]
- `hooks_disabled_by_env` (function) component `hooks_disabled_by_env [function]` (`03a51f93-89d4-54da-96d6-45db1bcc2dc7`) lines 269-271 [crates/ghook/src/main.rs:269-271]
  - Signature: `fn hooks_disabled_by_env() -> bool {`
  - Purpose: Indexed function `hooks_disabled_by_env` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:269-271]
- `build_dispatch_envelope` (function) component `build_dispatch_envelope [function]` (`c643761b-bc69-5517-86cd-0c5f27aa1a43`) lines 273-301 [crates/ghook/src/main.rs:273-301]
  - Signature: `fn build_dispatch_envelope(`
  - Purpose: Indexed function `build_dispatch_envelope` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:273-301]
- `detect_source` (function) component `detect_source [function]` (`310d3663-4164-5dbe-bb05-79931467c260`) lines 303-317 [crates/ghook/src/main.rs:303-317]
  - Signature: `fn detect_source(cfg: &CliConfig) -> String {`
  - Purpose: Indexed function `detect_source` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:303-317]
- `emit_action` (function) component `emit_action [function]` (`14279e14-6377-5c12-b42f-e25a648a2f3d`) lines 319-327 [crates/ghook/src/main.rs:319-327]
  - Signature: `fn emit_action(action: HookAction) -> ExitCode {`
  - Purpose: Indexed function `emit_action` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:319-327]
- `action_from_success_response` (function) component `action_from_success_response [function]` (`a9fac95f-a9f0-58ec-8c35-6a786112a062`) lines 329-399 [crates/ghook/src/main.rs:329-399]
  - Signature: `fn action_from_success_response(`
  - Purpose: Indexed function `action_from_success_response` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:329-399]
- `action_from_droid_success` (function) component `action_from_droid_success [function]` (`e575a823-1f9b-53c9-a297-1b995e22151e`) lines 401-420 [crates/ghook/src/main.rs:401-420]
  - Signature: `fn action_from_droid_success(result: Value, serialized: String) -> HookAction {`
  - Purpose: Indexed function `action_from_droid_success` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:401-420]
- `action_from_failure` (function) component `action_from_failure [function]` (`6ea37017-9105-5175-909e-08e70807c6ec`) lines 422-482 [crates/ghook/src/main.rs:422-482]
  - Signature: `fn action_from_failure(`
  - Purpose: Indexed function `action_from_failure` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:422-482]
- `is_blocked` (function) component `is_blocked [function]` (`a340b258-6c6d-57b4-814c-77096f5a1ec6`) lines 484-506 [crates/ghook/src/main.rs:484-506]
  - Signature: `fn is_blocked(result: &Value) -> bool {`
  - Purpose: Indexed function `is_blocked` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:484-506]
- `extract_reason` (function) component `extract_reason [function]` (`86105f7e-8f0d-51e3-9bb5-9397b02be28d`) lines 508-536 [crates/ghook/src/main.rs:508-536]
  - Signature: `fn extract_reason(result: &Value) -> String {`
  - Purpose: Indexed function `extract_reason` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:508-536]
- `json_value_is_meaningful` (function) component `json_value_is_meaningful [function]` (`50e3aebd-d3e2-5d93-b997-d5898f82a59b`) lines 538-555 [crates/ghook/src/main.rs:538-555]
  - Signature: `fn json_value_is_meaningful(value: &Value) -> bool {`
  - Purpose: Indexed function `json_value_is_meaningful` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:538-555]
- `write_runtime_stamp` (function) component `write_runtime_stamp [function]` (`b36f51c1-d253-57a3-9e4d-1d657a376c42`) lines 557-570 [crates/ghook/src/main.rs:557-570]
  - Signature: `fn write_runtime_stamp() -> Result<()> {`
  - Purpose: Indexed function `write_runtime_stamp` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:557-570]
- `with_tmux_env` (function) component `with_tmux_env [function]` (`145db008-637c-502d-8768-904b7dd210a5`) lines 581-584 [crates/ghook/src/main.rs:581-584]
  - Signature: `fn with_tmux_env<T>(tmux: Option<&str>, tmux_pane: Option<&str>, f: impl FnOnce() -> T) -> T {`
  - Purpose: Indexed function `with_tmux_env` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:581-584]
- `dispatch_envelope_injects_valid_tmux_pane_for_session_start` (function) component `dispatch_envelope_injects_valid_tmux_pane_for_session_start [function]` (`311d2266-9504-5fdd-a07a-05a6b773ff4b`) lines 587-599 [crates/ghook/src/main.rs:587-599]
  - Signature: `fn dispatch_envelope_injects_valid_tmux_pane_for_session_start() {`
  - Purpose: Indexed function `dispatch_envelope_injects_valid_tmux_pane_for_session_start` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:587-599]
- `dispatch_envelope_omits_terminal_context_for_tool_hooks` (function) component `dispatch_envelope_omits_terminal_context_for_tool_hooks [function]` (`02fe120f-bbe6-5058-8da4-83f7270fb883`) lines 602-610 [crates/ghook/src/main.rs:602-610]
  - Signature: `fn dispatch_envelope_omits_terminal_context_for_tool_hooks() {`
  - Purpose: Indexed function `dispatch_envelope_omits_terminal_context_for_tool_hooks` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:602-610]
- `dispatch_envelope_nulls_tmux_fields_for_missing_or_invalid_tmux_pane` (function) component `dispatch_envelope_nulls_tmux_fields_for_missing_or_invalid_tmux_pane [function]` (`52733481-aeac-51c2-b59f-41bdd673a847`) lines 613-653 [crates/ghook/src/main.rs:613-653]
  - Signature: `fn dispatch_envelope_nulls_tmux_fields_for_missing_or_invalid_tmux_pane() {`
  - Purpose: Indexed function `dispatch_envelope_nulls_tmux_fields_for_missing_or_invalid_tmux_pane` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:613-653]
- `action_from_success_forwards_sessionstart_context_json` (function) component `action_from_success_forwards_sessionstart_context_json [function]` (`11c12b39-7c36-5880-ae5a-6d032193d9a3`) lines 656-677 [crates/ghook/src/main.rs:656-677]
  - Signature: `fn action_from_success_forwards_sessionstart_context_json() {`
  - Purpose: Indexed function `action_from_success_forwards_sessionstart_context_json` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:656-677]
- `action_from_success_treats_codex_pretool_deny_as_json_block` (function) component `action_from_success_treats_codex_pretool_deny_as_json_block [function]` (`88f07f01-1c68-5207-bbb4-84ca9b0cd0f2`) lines 680-696 [crates/ghook/src/main.rs:680-696]
  - Signature: `fn action_from_success_treats_codex_pretool_deny_as_json_block() {`
  - Purpose: Indexed function `action_from_success_treats_codex_pretool_deny_as_json_block` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:680-696]
- `action_from_success_surfaces_nested_permission_decision_reason` (function) component `action_from_success_surfaces_nested_permission_decision_reason [function]` (`62c41969-5376-57de-9f0f-b89df3b921fb`) lines 699-715 [crates/ghook/src/main.rs:699-715]
  - Signature: `fn action_from_success_surfaces_nested_permission_decision_reason() {`
  - Purpose: Indexed function `action_from_success_surfaces_nested_permission_decision_reason` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:699-715]
- `action_from_success_preserves_additional_context_on_claude_block` (function) component `action_from_success_preserves_additional_context_on_claude_block [function]` (`ad4cea8f-4c11-5546-962b-18aa80dd45db`) lines 718-735 [crates/ghook/src/main.rs:718-735]
  - Signature: `fn action_from_success_preserves_additional_context_on_claude_block() {`
  - Purpose: Indexed function `action_from_success_preserves_additional_context_on_claude_block` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:718-735]
- `action_from_success_preserves_user_prompt_submit_block_json` (function) component `action_from_success_preserves_user_prompt_submit_block_json [function]` (`c9cbc63e-d037-5daf-9add-0d07a149bb56`) lines 738-756 [crates/ghook/src/main.rs:738-756]
  - Signature: `fn action_from_success_preserves_user_prompt_submit_block_json() {`
  - Purpose: Indexed function `action_from_success_preserves_user_prompt_submit_block_json` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:738-756]
- `action_from_success_treats_stop_block_as_exit_two` (function) component `action_from_success_treats_stop_block_as_exit_two [function]` (`70959c9c-3990-551b-ada0-21bb3f2c5db0`) lines 759-775 [crates/ghook/src/main.rs:759-775]
  - Signature: `fn action_from_success_treats_stop_block_as_exit_two() {`
  - Purpose: Indexed function `action_from_success_treats_stop_block_as_exit_two` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:759-775]
- `action_from_success_claude_hard_stop_exits_two` (function) component `action_from_success_claude_hard_stop_exits_two [function]` (`64a0ed27-aa71-549c-b4b7-1831867f6be3`) lines 778-794 [crates/ghook/src/main.rs:778-794]
  - Signature: `fn action_from_success_claude_hard_stop_exits_two() {`
  - Purpose: Indexed function `action_from_success_claude_hard_stop_exits_two` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:778-794]
- `action_from_success_claude_stop_with_permission_deny_no_exit_two` (function) component `action_from_success_claude_stop_with_permission_deny_no_exit_two [function]` (`205aef13-ce50-5aed-bbb2-909865a58378`) lines 797-808 [crates/ghook/src/main.rs:797-808]
  - Signature: `fn action_from_success_claude_stop_with_permission_deny_no_exit_two() {`
  - Purpose: Indexed function `action_from_success_claude_stop_with_permission_deny_no_exit_two` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:797-808]
- `action_from_success_claude_continue_false_without_reason_does_not_exit_two` (function) component `action_from_success_claude_continue_false_without_reason_does_not_exit_two [function]` (`043503d8-8428-5b6f-96e3-e9b560a59add`) lines 811-817 [crates/ghook/src/main.rs:811-817]
  - Signature: `fn action_from_success_claude_continue_false_without_reason_does_not_exit_two() {`
  - Purpose: Indexed function `action_from_success_claude_continue_false_without_reason_does_not_exit_two` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:811-817]
- `action_from_success_treats_droid_continue_false_as_exit_two_with_json` (function) component `action_from_success_treats_droid_continue_false_as_exit_two_with_json [function]` (`7408971b-126e-5740-af8a-3e2ca9513b4e`) lines 820-836 [crates/ghook/src/main.rs:820-836]
  - Signature: `fn action_from_success_treats_droid_continue_false_as_exit_two_with_json() {`
  - Purpose: Indexed function `action_from_success_treats_droid_continue_false_as_exit_two_with_json` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:820-836]
- `action_from_success_preserves_droid_block_json_without_exit_two` (function) component `action_from_success_preserves_droid_block_json_without_exit_two [function]` (`a5ac24a2-fb0b-50b7-8285-42f35daf096e`) lines 839-853 [crates/ghook/src/main.rs:839-853]
  - Signature: `fn action_from_success_preserves_droid_block_json_without_exit_two() {`
  - Purpose: Indexed function `action_from_success_preserves_droid_block_json_without_exit_two` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:839-853]
- `action_from_failure_blocks_critical_hooks` (function) component `action_from_failure_blocks_critical_hooks [function]` (`ae46af86-f0c8-5ba0-9273-2e40676812aa`) lines 856-871 [crates/ghook/src/main.rs:856-871]
  - Signature: `fn action_from_failure_blocks_critical_hooks() {`
  - Purpose: Indexed function `action_from_failure_blocks_critical_hooks` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:856-871]
- `action_from_failure_returns_json_for_noncritical_hooks` (function) component `action_from_failure_returns_json_for_noncritical_hooks [function]` (`248f4cae-e108-54d3-b664-5de59bf05c6e`) lines 874-887 [crates/ghook/src/main.rs:874-887]
  - Signature: `fn action_from_failure_returns_json_for_noncritical_hooks() {`
  - Purpose: Indexed function `action_from_failure_returns_json_for_noncritical_hooks` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:874-887]
- `action_from_failure_treats_timeout_like_python` (function) component `action_from_failure_treats_timeout_like_python [function]` (`0f786741-84f9-57f5-b8f5-0cfe84ea4db4`) lines 890-900 [crates/ghook/src/main.rs:890-900]
  - Signature: `fn action_from_failure_treats_timeout_like_python() {`
  - Purpose: Indexed function `action_from_failure_treats_timeout_like_python` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:890-900]
- `action_from_failure_treats_connect_on_critical_hook_as_exit_two` (function) component `action_from_failure_treats_connect_on_critical_hook_as_exit_two [function]` (`6c5919b0-f639-5e4e-b974-b4c7b0039f4e`) lines 903-916 [crates/ghook/src/main.rs:903-916]
  - Signature: `fn action_from_failure_treats_connect_on_critical_hook_as_exit_two() {`
  - Purpose: Indexed function `action_from_failure_treats_connect_on_critical_hook_as_exit_two` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:903-916]
- `action_from_failure_returns_stderr_for_droid_transport_errors` (function) component `action_from_failure_returns_stderr_for_droid_transport_errors [function]` (`ddb4aa4b-6a10-571a-9144-ba099470899d`) lines 919-932 [crates/ghook/src/main.rs:919-932]
  - Signature: `fn action_from_failure_returns_stderr_for_droid_transport_errors() {`
  - Purpose: Indexed function `action_from_failure_returns_stderr_for_droid_transport_errors` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:919-932]
- `hooks_disabled_by_env_reads_env_var` (function) component `hooks_disabled_by_env_reads_env_var [function]` (`86f7722c-f5bd-5494-b665-6e3583e145f5`) lines 935-967 [crates/ghook/src/main.rs:935-967]
  - Signature: `fn hooks_disabled_by_env_reads_env_var() {`
  - Purpose: Indexed function `hooks_disabled_by_env_reads_env_var` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:935-967]
- `is_blocked_matches_dispatcher_patterns` (function) component `is_blocked_matches_dispatcher_patterns [function]` (`cdf4abcc-14c2-5bdf-ab47-85be2998ac0b`) lines 970-979 [crates/ghook/src/main.rs:970-979]
  - Signature: `fn is_blocked_matches_dispatcher_patterns() {`
  - Purpose: Indexed function `is_blocked_matches_dispatcher_patterns` in `crates/ghook/src/main.rs`. [crates/ghook/src/main.rs:970-979]

