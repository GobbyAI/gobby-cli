---
title: crates/ghook/src/action.rs
type: code_file
provenance:
- file: crates/ghook/src/action.rs
  ranges:
  - 9-13
  - 15-21
  - 23-25
  - 27-35
  - 37-107
  - 109-128
  - 130-190
  - 192-214
  - 216-244
  - 253-274
  - 277-293
  - 296-312
  - 315-332
  - 335-353
  - 356-372
  - 375-391
  - 394-408
  - 411-427
  - 430-441
  - 444-450
  - 453-469
  - 472-486
  - 489-504
  - 507-520
  - 523-533
  - 536-549
  - 552-565
  - 568-577
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/ghook/src/action.rs:9-13](crates/ghook/src/action.rs#L9-L13), [crates/ghook/src/action.rs:15-21](crates/ghook/src/action.rs#L15-L21), [crates/ghook/src/action.rs:23-25](crates/ghook/src/action.rs#L23-L25), [crates/ghook/src/action.rs:27-35](crates/ghook/src/action.rs#L27-L35), [crates/ghook/src/action.rs:37-107](crates/ghook/src/action.rs#L37-L107), [crates/ghook/src/action.rs:109-128](crates/ghook/src/action.rs#L109-L128), [crates/ghook/src/action.rs:130-190](crates/ghook/src/action.rs#L130-L190), [crates/ghook/src/action.rs:192-214](crates/ghook/src/action.rs#L192-L214), [crates/ghook/src/action.rs:216-244](crates/ghook/src/action.rs#L216-L244), [crates/ghook/src/action.rs:253-274](crates/ghook/src/action.rs#L253-L274), [crates/ghook/src/action.rs:277-293](crates/ghook/src/action.rs#L277-L293), [crates/ghook/src/action.rs:296-312](crates/ghook/src/action.rs#L296-L312), [crates/ghook/src/action.rs:315-332](crates/ghook/src/action.rs#L315-L332), [crates/ghook/src/action.rs:335-353](crates/ghook/src/action.rs#L335-L353), [crates/ghook/src/action.rs:356-372](crates/ghook/src/action.rs#L356-L372), [crates/ghook/src/action.rs:375-391](crates/ghook/src/action.rs#L375-L391), [crates/ghook/src/action.rs:394-408](crates/ghook/src/action.rs#L394-L408), [crates/ghook/src/action.rs:411-427](crates/ghook/src/action.rs#L411-L427), [crates/ghook/src/action.rs:430-441](crates/ghook/src/action.rs#L430-L441), [crates/ghook/src/action.rs:444-450](crates/ghook/src/action.rs#L444-L450), [crates/ghook/src/action.rs:453-469](crates/ghook/src/action.rs#L453-L469), [crates/ghook/src/action.rs:472-486](crates/ghook/src/action.rs#L472-L486), [crates/ghook/src/action.rs:489-504](crates/ghook/src/action.rs#L489-L504), [crates/ghook/src/action.rs:507-520](crates/ghook/src/action.rs#L507-L520), [crates/ghook/src/action.rs:523-533](crates/ghook/src/action.rs#L523-L533), [crates/ghook/src/action.rs:536-549](crates/ghook/src/action.rs#L536-L549), [crates/ghook/src/action.rs:552-565](crates/ghook/src/action.rs#L552-L565), [crates/ghook/src/action.rs:568-577](crates/ghook/src/action.rs#L568-L577)

</details>

# crates/ghook/src/action.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Purpose

Builds `HookAction` values that translate hook execution outcomes into process exit codes plus optional JSON on stdout and messages on stderr. The helpers emit a default continue response, print actions, and parse success or failure responses with source-specific rules for `droid`, `claude`, and blocked hook cases so the file centralizes how hook results become `continue`, `exit 2`, or plain JSON output.
[crates/ghook/src/action.rs:9-13]
[crates/ghook/src/action.rs:15-21]
[crates/ghook/src/action.rs:23-25]
[crates/ghook/src/action.rs:27-35]
[crates/ghook/src/action.rs:37-107]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `HookAction` | class | `pub(crate) struct HookAction {` | `HookAction [class]` | `0f8bb650-4738-5f62-a891-6fc56dd117da` | 9-13 [crates/ghook/src/action.rs:9-13] | Indexed class `HookAction` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:9-13] |
| `continue_action` | function | `pub(crate) fn continue_action() -> HookAction {` | `continue_action [function]` | `159e8721-8963-5376-a81f-e39c9d46b9e4` | 15-21 [crates/ghook/src/action.rs:15-21] | Indexed function `continue_action` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:15-21] |
| `emit_empty_json` | function | `pub(crate) fn emit_empty_json() {` | `emit_empty_json [function]` | `c9f040c2-f303-5ccd-a221-a3f3913856d5` | 23-25 [crates/ghook/src/action.rs:23-25] | Indexed function `emit_empty_json` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:23-25] |
| `emit_action` | function | `pub(crate) fn emit_action(action: HookAction) -> ExitCode {` | `emit_action [function]` | `7ae0ac51-1f88-5b2c-82ec-b77e32d79471` | 27-35 [crates/ghook/src/action.rs:27-35] | Indexed function `emit_action` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:27-35] |
| `action_from_success_response` | function | `pub(crate) fn action_from_success_response(` | `action_from_success_response [function]` | `19b8fd80-56cb-5460-ba43-bfee664ac43c` | 37-107 [crates/ghook/src/action.rs:37-107] | Indexed function `action_from_success_response` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:37-107] |
| `action_from_droid_success` | function | `fn action_from_droid_success(result: Value, serialized: String) -> HookAction {` | `action_from_droid_success [function]` | `8c79e280-7ede-5763-9a7d-eabba4b5bb05` | 109-128 [crates/ghook/src/action.rs:109-128] | Indexed function `action_from_droid_success` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:109-128] |
| `action_from_failure` | function | `pub(crate) fn action_from_failure(` | `action_from_failure [function]` | `9660e3d6-4c8c-5854-b829-32a50d25d7c8` | 130-190 [crates/ghook/src/action.rs:130-190] | Indexed function `action_from_failure` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:130-190] |
| `is_blocked` | function | `fn is_blocked(result: &Value) -> bool {` | `is_blocked [function]` | `dea28ec4-ae02-5a60-9e32-9a8cb3720be4` | 192-214 [crates/ghook/src/action.rs:192-214] | Indexed function `is_blocked` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:192-214] |
| `extract_reason` | function | `fn extract_reason(result: &Value) -> String {` | `extract_reason [function]` | `ffd183bd-25d5-5f5a-b53a-9dd3e7e194a8` | 216-244 [crates/ghook/src/action.rs:216-244] | Indexed function `extract_reason` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:216-244] |
| `action_from_success_forwards_sessionstart_context_json` | function | `fn action_from_success_forwards_sessionstart_context_json() {` | `action_from_success_forwards_sessionstart_context_json [function]` | `1f7b9524-ce77-51ea-a5d9-770cda0de88d` | 253-274 [crates/ghook/src/action.rs:253-274] | Indexed function `action_from_success_forwards_sessionstart_context_json` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:253-274] |
| `action_from_success_treats_codex_pretool_deny_as_json_block` | function | `fn action_from_success_treats_codex_pretool_deny_as_json_block() {` | `action_from_success_treats_codex_pretool_deny_as_json_block [function]` | `94c0a3c0-0193-5902-8067-edab1f9e0847` | 277-293 [crates/ghook/src/action.rs:277-293] | Indexed function `action_from_success_treats_codex_pretool_deny_as_json_block` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:277-293] |
| `action_from_success_surfaces_nested_permission_decision_reason` | function | `fn action_from_success_surfaces_nested_permission_decision_reason() {` | `action_from_success_surfaces_nested_permission_decision_reason [function]` | `cd50d851-d6b6-544c-95be-817a6f41ad9d` | 296-312 [crates/ghook/src/action.rs:296-312] | Indexed function `action_from_success_surfaces_nested_permission_decision_reason` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:296-312] |
| `action_from_success_preserves_additional_context_on_claude_block` | function | `fn action_from_success_preserves_additional_context_on_claude_block() {` | `action_from_success_preserves_additional_context_on_claude_block [function]` | `3939bb6f-1d6b-559b-90f3-5f370fed484b` | 315-332 [crates/ghook/src/action.rs:315-332] | Indexed function `action_from_success_preserves_additional_context_on_claude_block` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:315-332] |
| `action_from_success_preserves_user_prompt_submit_block_json` | function | `fn action_from_success_preserves_user_prompt_submit_block_json() {` | `action_from_success_preserves_user_prompt_submit_block_json [function]` | `65283dd2-1131-5839-b527-713b94046fb5` | 335-353 [crates/ghook/src/action.rs:335-353] | Indexed function `action_from_success_preserves_user_prompt_submit_block_json` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:335-353] |
| `action_from_success_treats_stop_block_as_exit_two` | function | `fn action_from_success_treats_stop_block_as_exit_two() {` | `action_from_success_treats_stop_block_as_exit_two [function]` | `02f0d3f1-3036-5ade-b446-4c5d5cff3710` | 356-372 [crates/ghook/src/action.rs:356-372] | Indexed function `action_from_success_treats_stop_block_as_exit_two` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:356-372] |
| `action_from_success_treats_lowercase_stop_block_as_exit_two` | function | `fn action_from_success_treats_lowercase_stop_block_as_exit_two() {` | `action_from_success_treats_lowercase_stop_block_as_exit_two [function]` | `ddaf2ecb-537f-59e6-9cf6-3af3cee84471` | 375-391 [crates/ghook/src/action.rs:375-391] | Indexed function `action_from_success_treats_lowercase_stop_block_as_exit_two` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:375-391] |
| `action_from_success_keeps_non_stop_grok_block_as_json` | function | `fn action_from_success_keeps_non_stop_grok_block_as_json() {` | `action_from_success_keeps_non_stop_grok_block_as_json [function]` | `6bc8a672-c1ac-51bb-a835-17ff737446ae` | 394-408 [crates/ghook/src/action.rs:394-408] | Indexed function `action_from_success_keeps_non_stop_grok_block_as_json` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:394-408] |
| `action_from_success_claude_hard_stop_exits_two` | function | `fn action_from_success_claude_hard_stop_exits_two() {` | `action_from_success_claude_hard_stop_exits_two [function]` | `da92b39e-3a68-5eca-ba21-2ca8be495ba0` | 411-427 [crates/ghook/src/action.rs:411-427] | Indexed function `action_from_success_claude_hard_stop_exits_two` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:411-427] |
| `action_from_success_claude_stop_with_permission_deny_no_exit_two` | function | `fn action_from_success_claude_stop_with_permission_deny_no_exit_two() {` | `action_from_success_claude_stop_with_permission_deny_no_exit_two [function]` | `d7026395-2584-5669-8947-7a1b2ccd36f7` | 430-441 [crates/ghook/src/action.rs:430-441] | Indexed function `action_from_success_claude_stop_with_permission_deny_no_exit_two` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:430-441] |
| `action_from_success_claude_continue_false_without_reason_does_not_exit_two` | function | `fn action_from_success_claude_continue_false_without_reason_does_not_exit_two() {` | `action_from_success_claude_continue_false_without_reason_does_not_exit_two [function]` | `68347389-1528-5cd5-9955-6d8816420610` | 444-450 [crates/ghook/src/action.rs:444-450] | Indexed function `action_from_success_claude_continue_false_without_reason_does_not_exit_two` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:444-450] |
| `action_from_success_treats_droid_continue_false_as_exit_two_with_json` | function | `fn action_from_success_treats_droid_continue_false_as_exit_two_with_json() {` | `action_from_success_treats_droid_continue_false_as_exit_two_with_json [function]` | `a7d527f0-abc0-5bc1-aed3-4ba5a3211f88` | 453-469 [crates/ghook/src/action.rs:453-469] | Indexed function `action_from_success_treats_droid_continue_false_as_exit_two_with_json` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:453-469] |
| `action_from_success_preserves_droid_block_json_without_exit_two` | function | `fn action_from_success_preserves_droid_block_json_without_exit_two() {` | `action_from_success_preserves_droid_block_json_without_exit_two [function]` | `5e378ae3-4f9c-50de-9708-ace20ffa5823` | 472-486 [crates/ghook/src/action.rs:472-486] | Indexed function `action_from_success_preserves_droid_block_json_without_exit_two` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:472-486] |
| `action_from_failure_blocks_critical_hooks` | function | `fn action_from_failure_blocks_critical_hooks() {` | `action_from_failure_blocks_critical_hooks [function]` | `c0c2bd8b-9e21-5702-8d85-119947d32f69` | 489-504 [crates/ghook/src/action.rs:489-504] | Indexed function `action_from_failure_blocks_critical_hooks` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:489-504] |
| `action_from_failure_returns_json_for_noncritical_hooks` | function | `fn action_from_failure_returns_json_for_noncritical_hooks() {` | `action_from_failure_returns_json_for_noncritical_hooks [function]` | `2df71ac8-53da-5a11-94a5-e3596f29d1ea` | 507-520 [crates/ghook/src/action.rs:507-520] | Indexed function `action_from_failure_returns_json_for_noncritical_hooks` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:507-520] |
| `action_from_failure_treats_timeout_like_python` | function | `fn action_from_failure_treats_timeout_like_python() {` | `action_from_failure_treats_timeout_like_python [function]` | `531bbd7f-a0fa-5859-ac74-150650a133a7` | 523-533 [crates/ghook/src/action.rs:523-533] | Indexed function `action_from_failure_treats_timeout_like_python` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:523-533] |
| `action_from_failure_treats_connect_on_critical_hook_as_exit_two` | function | `fn action_from_failure_treats_connect_on_critical_hook_as_exit_two() {` | `action_from_failure_treats_connect_on_critical_hook_as_exit_two [function]` | `06f40ed8-b03c-5642-b13c-f17913879697` | 536-549 [crates/ghook/src/action.rs:536-549] | Indexed function `action_from_failure_treats_connect_on_critical_hook_as_exit_two` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:536-549] |
| `action_from_failure_returns_stderr_for_droid_transport_errors` | function | `fn action_from_failure_returns_stderr_for_droid_transport_errors() {` | `action_from_failure_returns_stderr_for_droid_transport_errors [function]` | `f0dd5971-63c8-5345-abb1-2f1a170a12a9` | 552-565 [crates/ghook/src/action.rs:552-565] | Indexed function `action_from_failure_returns_stderr_for_droid_transport_errors` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:552-565] |
| `is_blocked_matches_dispatcher_patterns` | function | `fn is_blocked_matches_dispatcher_patterns() {` | `is_blocked_matches_dispatcher_patterns [function]` | `435fdc85-db8f-58d6-a82c-490a88c605ef` | 568-577 [crates/ghook/src/action.rs:568-577] | Indexed function `is_blocked_matches_dispatcher_patterns` in `crates/ghook/src/action.rs`. [crates/ghook/src/action.rs:568-577] |
