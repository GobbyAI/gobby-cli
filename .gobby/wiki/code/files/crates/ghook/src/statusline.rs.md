---
title: crates/ghook/src/statusline.rs
type: code_file
provenance:
- file: crates/ghook/src/statusline.rs
  ranges:
  - 25-27
  - 29-35
  - 37-67
  - 69-104
  - 106-119
  - 121-168
  - 170-174
  - 177-183
  - '186'
  - 189-194
  - 197-201
  - 217-222
  - 225-229
  - 232-236
  - 239-245
  - 248-253
  - 256-283
  - 286-310
  - 313-324
  - 327-344
  - 347-371
  - 374-397
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/ghook/src/statusline.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Purpose

Claude Code statusline hook handler that reads JSON from stdin, extracts a statusline payload when the input looks like a valid session event, and best-effort posts it to the daemon’s `/api/sessions/statusline` endpoint without surfacing transport failures as hook errors. It also optionally runs a downstream command and mirrors its stdout back to Claude exactly, with timeout and process-group termination helpers to keep the pipeline responsive and to clean up surviving child processes; the tests cover hook recognition, payload extraction, daemon posting, stdout passthrough, and timeout/kill behavior.
[crates/ghook/src/statusline.rs:25-27]
[crates/ghook/src/statusline.rs:29-35]
[crates/ghook/src/statusline.rs:37-67]
[crates/ghook/src/statusline.rs:69-104]
[crates/ghook/src/statusline.rs:106-119]

## API Symbols

- `is_statusline_hook` (function) component `is_statusline_hook [function]` (`98676496-c1ef-5e62-abc3-2f6fc510fe89`) lines 25-27 [crates/ghook/src/statusline.rs:25-27]
  - Signature: `pub(crate) fn is_statusline_hook(cli: &str, hook_type: &str) -> bool {`
  - Purpose: Indexed function `is_statusline_hook` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:25-27]
- `handle` (function) component `handle [function]` (`4e51d57c-e47d-5e20-9b1a-797318e05011`) lines 29-35 [crates/ghook/src/statusline.rs:29-35]
  - Signature: `pub(crate) fn handle(stdin_raw: &[u8]) -> ExitCode {`
  - Purpose: Indexed function `handle` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:29-35]
- `handle_with` (function) component `handle_with [function]` (`e54362c6-30f4-5525-be69-4cd83ede2126`) lines 37-67 [crates/ghook/src/statusline.rs:37-67]
  - Signature: `fn handle_with(`
  - Purpose: Indexed function `handle_with` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:37-67]
- `extract_payload` (function) component `extract_payload [function]` (`1882ec9f-4e36-53f4-8a85-0c963aecb5d2`) lines 69-104 [crates/ghook/src/statusline.rs:69-104]
  - Signature: `fn extract_payload(input: &Value) -> Option<Value> {`
  - Purpose: Indexed function `extract_payload` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:69-104]
- `post_to_daemon_best_effort` (function) component `post_to_daemon_best_effort [function]` (`64d25050-ccb7-542a-b7ed-11466794a09d`) lines 106-119 [crates/ghook/src/statusline.rs:106-119]
  - Signature: `fn post_to_daemon_best_effort(payload: Value, daemon_url: &str) {`
  - Purpose: Indexed function `post_to_daemon_best_effort` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:106-119]
- `forward_downstream` (function) component `forward_downstream [function]` (`e9041adc-57e0-5c61-abfa-09da545cfb15`) lines 121-168 [crates/ghook/src/statusline.rs:121-168]
  - Signature: `fn forward_downstream(command: &OsStr, stdin_raw: &[u8]) -> Option<Vec<u8>> {`
  - Purpose: Indexed function `forward_downstream` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:121-168]
- `terminate_downstream` (function) component `terminate_downstream [function]` (`a7f90096-675f-571f-aa5d-17a83ae432b4`) lines 170-174 [crates/ghook/src/statusline.rs:170-174]
  - Signature: `fn terminate_downstream(child: &mut std::process::Child) {`
  - Purpose: Indexed function `terminate_downstream` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:170-174]
- `terminate_downstream_group` (function) component `terminate_downstream_group [function]` (`c351cb94-5e68-5bd1-a037-d29a05326bb1`) lines 177-183 [crates/ghook/src/statusline.rs:177-183]
  - Signature: `fn terminate_downstream_group(child: &std::process::Child) {`
  - Purpose: Indexed function `terminate_downstream_group` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:177-183]
- `terminate_downstream_group` (function) component `terminate_downstream_group [function]` (`e15fa213-5637-5db1-ac26-36f0a4297e0e`) lines 186-186 [crates/ghook/src/statusline.rs:186]
  - Signature: `fn terminate_downstream_group(_child: &std::process::Child) {}`
  - Purpose: Indexed function `terminate_downstream_group` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:186]
- `downstream_shell_command` (function) component `downstream_shell_command [function]` (`6d0eb7ae-9c75-53bc-a774-7f796ccc373d`) lines 189-194 [crates/ghook/src/statusline.rs:189-194]
  - Signature: `fn downstream_shell_command(command: &OsStr) -> Command {`
  - Purpose: Indexed function `downstream_shell_command` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:189-194]
- `downstream_shell_command` (function) component `downstream_shell_command [function]` (`87a58021-b993-5d39-a0e8-807db949e60c`) lines 197-201 [crates/ghook/src/statusline.rs:197-201]
  - Signature: `fn downstream_shell_command(command: &OsStr) -> Command {`
  - Purpose: Indexed function `downstream_shell_command` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:197-201]
- `recognizes_only_claude_statusline_hook` (function) component `recognizes_only_claude_statusline_hook [function]` (`d16adccf-b71e-51da-97ab-a58600962b23`) lines 217-222 [crates/ghook/src/statusline.rs:217-222]
  - Signature: `fn recognizes_only_claude_statusline_hook() {`
  - Purpose: Indexed function `recognizes_only_claude_statusline_hook` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:217-222]
- `extract_payload_matches_full_golden_fixture` (function) component `extract_payload_matches_full_golden_fixture [function]` (`9dba13dd-a22d-57dd-b8a5-3170edbc2eba`) lines 225-229 [crates/ghook/src/statusline.rs:225-229]
  - Signature: `fn extract_payload_matches_full_golden_fixture() {`
  - Purpose: Indexed function `extract_payload_matches_full_golden_fixture` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:225-229]
- `extract_payload_matches_default_golden_fixture` (function) component `extract_payload_matches_default_golden_fixture [function]` (`db5c0de8-9839-514c-a360-ff8080d86db9`) lines 232-236 [crates/ghook/src/statusline.rs:232-236]
  - Signature: `fn extract_payload_matches_default_golden_fixture() {`
  - Purpose: Indexed function `extract_payload_matches_default_golden_fixture` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:232-236]
- `extract_payload_returns_none_without_session_id` (function) component `extract_payload_returns_none_without_session_id [function]` (`56fd7a3f-2596-5a55-8c97-fe480a524e27`) lines 239-245 [crates/ghook/src/statusline.rs:239-245]
  - Signature: `fn extract_payload_returns_none_without_session_id() {`
  - Purpose: Indexed function `extract_payload_returns_none_without_session_id` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:239-245]
- `malformed_json_exits_success_without_stdout` (function) component `malformed_json_exits_success_without_stdout [function]` (`f97e1ca5-361f-52f8-ae46-40bd7f64464d`) lines 248-253 [crates/ghook/src/statusline.rs:248-253]
  - Signature: `fn malformed_json_exits_success_without_stdout() {`
  - Purpose: Indexed function `malformed_json_exits_success_without_stdout` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:248-253]
- `posts_statusline_payload_to_daemon_endpoint` (function) component `posts_statusline_payload_to_daemon_endpoint [function]` (`122bbc33-3e69-5b6e-8aef-f4faf1b67741`) lines 256-283 [crates/ghook/src/statusline.rs:256-283]
  - Signature: `fn posts_statusline_payload_to_daemon_endpoint() {`
  - Purpose: Indexed function `posts_statusline_payload_to_daemon_endpoint` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:256-283]
- `statusline_post_honors_gobby_daemon_url_override` (function) component `statusline_post_honors_gobby_daemon_url_override [function]` (`271dfe9e-f471-5360-abc1-ec4df58efec4`) lines 286-310 [crates/ghook/src/statusline.rs:286-310]
  - Signature: `fn statusline_post_honors_gobby_daemon_url_override() {`
  - Purpose: Indexed function `statusline_post_honors_gobby_daemon_url_override` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:286-310]
- `downstream_stdout_passthrough_preserves_bytes` (function) component `downstream_stdout_passthrough_preserves_bytes [function]` (`35e38e77-8f95-5c4a-8954-a88f78b669b9`) lines 313-324 [crates/ghook/src/statusline.rs:313-324]
  - Signature: `fn downstream_stdout_passthrough_preserves_bytes() {`
  - Purpose: Indexed function `downstream_stdout_passthrough_preserves_bytes` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:313-324]
- `downstream_large_stdout_returns_full_output_quickly` (function) component `downstream_large_stdout_returns_full_output_quickly [function]` (`d26f134a-9fb4-5e18-b6c6-c8879a1dd32e`) lines 327-344 [crates/ghook/src/statusline.rs:327-344]
  - Signature: `fn downstream_large_stdout_returns_full_output_quickly() {`
  - Purpose: Indexed function `downstream_large_stdout_returns_full_output_quickly` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:327-344]
- `downstream_timeout_returns_before_six_seconds` (function) component `downstream_timeout_returns_before_six_seconds [function]` (`895005c4-92ea-51d5-bf58-1e4ed0df9f23`) lines 347-371 [crates/ghook/src/statusline.rs:347-371]
  - Signature: `fn downstream_timeout_returns_before_six_seconds() {`
  - Purpose: Indexed function `downstream_timeout_returns_before_six_seconds` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:347-371]
- `downstream_timeout_kills_pipeline_survivors_holding_stdout` (function) component `downstream_timeout_kills_pipeline_survivors_holding_stdout [function]` (`c510a3d0-3fd9-5ee1-8a95-e2b3c4523b86`) lines 374-397 [crates/ghook/src/statusline.rs:374-397]
  - Signature: `fn downstream_timeout_kills_pipeline_survivors_holding_stdout() {`
  - Purpose: Indexed function `downstream_timeout_kills_pipeline_survivors_holding_stdout` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:374-397]

