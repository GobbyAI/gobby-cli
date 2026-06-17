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

<details>
<summary>Relevant source files</summary>

- [crates/ghook/src/statusline.rs:25-27](crates/ghook/src/statusline.rs#L25-L27), [crates/ghook/src/statusline.rs:29-35](crates/ghook/src/statusline.rs#L29-L35), [crates/ghook/src/statusline.rs:37-67](crates/ghook/src/statusline.rs#L37-L67), [crates/ghook/src/statusline.rs:69-104](crates/ghook/src/statusline.rs#L69-L104), [crates/ghook/src/statusline.rs:106-119](crates/ghook/src/statusline.rs#L106-L119), [crates/ghook/src/statusline.rs:121-168](crates/ghook/src/statusline.rs#L121-L168), [crates/ghook/src/statusline.rs:170-174](crates/ghook/src/statusline.rs#L170-L174), [crates/ghook/src/statusline.rs:177-183](crates/ghook/src/statusline.rs#L177-L183), [crates/ghook/src/statusline.rs:186](crates/ghook/src/statusline.rs#L186), [crates/ghook/src/statusline.rs:189-194](crates/ghook/src/statusline.rs#L189-L194), [crates/ghook/src/statusline.rs:197-201](crates/ghook/src/statusline.rs#L197-L201), [crates/ghook/src/statusline.rs:217-222](crates/ghook/src/statusline.rs#L217-L222), [crates/ghook/src/statusline.rs:225-229](crates/ghook/src/statusline.rs#L225-L229), [crates/ghook/src/statusline.rs:232-236](crates/ghook/src/statusline.rs#L232-L236), [crates/ghook/src/statusline.rs:239-245](crates/ghook/src/statusline.rs#L239-L245), [crates/ghook/src/statusline.rs:248-253](crates/ghook/src/statusline.rs#L248-L253), [crates/ghook/src/statusline.rs:256-283](crates/ghook/src/statusline.rs#L256-L283), [crates/ghook/src/statusline.rs:286-310](crates/ghook/src/statusline.rs#L286-L310), [crates/ghook/src/statusline.rs:313-324](crates/ghook/src/statusline.rs#L313-L324), [crates/ghook/src/statusline.rs:327-344](crates/ghook/src/statusline.rs#L327-L344), [crates/ghook/src/statusline.rs:347-371](crates/ghook/src/statusline.rs#L347-L371), [crates/ghook/src/statusline.rs:374-397](crates/ghook/src/statusline.rs#L374-L397)

</details>

# crates/ghook/src/statusline.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Purpose

Implements the Claude Code statusline hook path. It recognizes only `claude` `statusline` hooks, parses the hook JSON, extracts and posts a session payload to the daemon best-effort, and optionally forwards the original stdin bytes to a downstream command while preserving stdout exactly; all error paths return success so transport failures do not propagate back to Claude.
[crates/ghook/src/statusline.rs:25-27]
[crates/ghook/src/statusline.rs:29-35]
[crates/ghook/src/statusline.rs:37-67]
[crates/ghook/src/statusline.rs:69-104]
[crates/ghook/src/statusline.rs:106-119]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `is_statusline_hook` | function | `pub(crate) fn is_statusline_hook(cli: &str, hook_type: &str) -> bool {` | `is_statusline_hook [function]` | `98676496-c1ef-5e62-abc3-2f6fc510fe89` | 25-27 [crates/ghook/src/statusline.rs:25-27] | Indexed function `is_statusline_hook` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:25-27] |
| `handle` | function | `pub(crate) fn handle(stdin_raw: &[u8]) -> ExitCode {` | `handle [function]` | `4e51d57c-e47d-5e20-9b1a-797318e05011` | 29-35 [crates/ghook/src/statusline.rs:29-35] | Indexed function `handle` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:29-35] |
| `handle_with` | function | `fn handle_with(` | `handle_with [function]` | `e54362c6-30f4-5525-be69-4cd83ede2126` | 37-67 [crates/ghook/src/statusline.rs:37-67] | Indexed function `handle_with` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:37-67] |
| `extract_payload` | function | `fn extract_payload(input: &Value) -> Option<Value> {` | `extract_payload [function]` | `1882ec9f-4e36-53f4-8a85-0c963aecb5d2` | 69-104 [crates/ghook/src/statusline.rs:69-104] | Indexed function `extract_payload` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:69-104] |
| `post_to_daemon_best_effort` | function | `fn post_to_daemon_best_effort(payload: Value, daemon_url: &str) {` | `post_to_daemon_best_effort [function]` | `64d25050-ccb7-542a-b7ed-11466794a09d` | 106-119 [crates/ghook/src/statusline.rs:106-119] | Indexed function `post_to_daemon_best_effort` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:106-119] |
| `forward_downstream` | function | `fn forward_downstream(command: &OsStr, stdin_raw: &[u8]) -> Option<Vec<u8>> {` | `forward_downstream [function]` | `e9041adc-57e0-5c61-abfa-09da545cfb15` | 121-168 [crates/ghook/src/statusline.rs:121-168] | Indexed function `forward_downstream` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:121-168] |
| `terminate_downstream` | function | `fn terminate_downstream(child: &mut std::process::Child) {` | `terminate_downstream [function]` | `a7f90096-675f-571f-aa5d-17a83ae432b4` | 170-174 [crates/ghook/src/statusline.rs:170-174] | Indexed function `terminate_downstream` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:170-174] |
| `terminate_downstream_group` | function | `fn terminate_downstream_group(child: &std::process::Child) {` | `terminate_downstream_group [function]` | `c351cb94-5e68-5bd1-a037-d29a05326bb1` | 177-183 [crates/ghook/src/statusline.rs:177-183] | Indexed function `terminate_downstream_group` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:177-183] |
| `terminate_downstream_group` | function | `fn terminate_downstream_group(_child: &std::process::Child) {}` | `terminate_downstream_group [function]` | `e15fa213-5637-5db1-ac26-36f0a4297e0e` | 186-186 [crates/ghook/src/statusline.rs:186] | Indexed function `terminate_downstream_group` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:186] |
| `downstream_shell_command` | function | `fn downstream_shell_command(command: &OsStr) -> Command {` | `downstream_shell_command [function]` | `6d0eb7ae-9c75-53bc-a774-7f796ccc373d` | 189-194 [crates/ghook/src/statusline.rs:189-194] | Indexed function `downstream_shell_command` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:189-194] |
| `downstream_shell_command` | function | `fn downstream_shell_command(command: &OsStr) -> Command {` | `downstream_shell_command [function]` | `87a58021-b993-5d39-a0e8-807db949e60c` | 197-201 [crates/ghook/src/statusline.rs:197-201] | Indexed function `downstream_shell_command` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:197-201] |
| `recognizes_only_claude_statusline_hook` | function | `fn recognizes_only_claude_statusline_hook() {` | `recognizes_only_claude_statusline_hook [function]` | `d16adccf-b71e-51da-97ab-a58600962b23` | 217-222 [crates/ghook/src/statusline.rs:217-222] | Indexed function `recognizes_only_claude_statusline_hook` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:217-222] |
| `extract_payload_matches_full_golden_fixture` | function | `fn extract_payload_matches_full_golden_fixture() {` | `extract_payload_matches_full_golden_fixture [function]` | `9dba13dd-a22d-57dd-b8a5-3170edbc2eba` | 225-229 [crates/ghook/src/statusline.rs:225-229] | Indexed function `extract_payload_matches_full_golden_fixture` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:225-229] |
| `extract_payload_matches_default_golden_fixture` | function | `fn extract_payload_matches_default_golden_fixture() {` | `extract_payload_matches_default_golden_fixture [function]` | `db5c0de8-9839-514c-a360-ff8080d86db9` | 232-236 [crates/ghook/src/statusline.rs:232-236] | Indexed function `extract_payload_matches_default_golden_fixture` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:232-236] |
| `extract_payload_returns_none_without_session_id` | function | `fn extract_payload_returns_none_without_session_id() {` | `extract_payload_returns_none_without_session_id [function]` | `56fd7a3f-2596-5a55-8c97-fe480a524e27` | 239-245 [crates/ghook/src/statusline.rs:239-245] | Indexed function `extract_payload_returns_none_without_session_id` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:239-245] |
| `malformed_json_exits_success_without_stdout` | function | `fn malformed_json_exits_success_without_stdout() {` | `malformed_json_exits_success_without_stdout [function]` | `f97e1ca5-361f-52f8-ae46-40bd7f64464d` | 248-253 [crates/ghook/src/statusline.rs:248-253] | Indexed function `malformed_json_exits_success_without_stdout` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:248-253] |
| `posts_statusline_payload_to_daemon_endpoint` | function | `fn posts_statusline_payload_to_daemon_endpoint() {` | `posts_statusline_payload_to_daemon_endpoint [function]` | `122bbc33-3e69-5b6e-8aef-f4faf1b67741` | 256-283 [crates/ghook/src/statusline.rs:256-283] | Indexed function `posts_statusline_payload_to_daemon_endpoint` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:256-283] |
| `statusline_post_honors_gobby_daemon_url_override` | function | `fn statusline_post_honors_gobby_daemon_url_override() {` | `statusline_post_honors_gobby_daemon_url_override [function]` | `271dfe9e-f471-5360-abc1-ec4df58efec4` | 286-310 [crates/ghook/src/statusline.rs:286-310] | Indexed function `statusline_post_honors_gobby_daemon_url_override` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:286-310] |
| `downstream_stdout_passthrough_preserves_bytes` | function | `fn downstream_stdout_passthrough_preserves_bytes() {` | `downstream_stdout_passthrough_preserves_bytes [function]` | `35e38e77-8f95-5c4a-8954-a88f78b669b9` | 313-324 [crates/ghook/src/statusline.rs:313-324] | Indexed function `downstream_stdout_passthrough_preserves_bytes` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:313-324] |
| `downstream_large_stdout_returns_full_output_quickly` | function | `fn downstream_large_stdout_returns_full_output_quickly() {` | `downstream_large_stdout_returns_full_output_quickly [function]` | `d26f134a-9fb4-5e18-b6c6-c8879a1dd32e` | 327-344 [crates/ghook/src/statusline.rs:327-344] | Indexed function `downstream_large_stdout_returns_full_output_quickly` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:327-344] |
| `downstream_timeout_returns_before_six_seconds` | function | `fn downstream_timeout_returns_before_six_seconds() {` | `downstream_timeout_returns_before_six_seconds [function]` | `895005c4-92ea-51d5-bf58-1e4ed0df9f23` | 347-371 [crates/ghook/src/statusline.rs:347-371] | Indexed function `downstream_timeout_returns_before_six_seconds` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:347-371] |
| `downstream_timeout_kills_pipeline_survivors_holding_stdout` | function | `fn downstream_timeout_kills_pipeline_survivors_holding_stdout() {` | `downstream_timeout_kills_pipeline_survivors_holding_stdout [function]` | `c510a3d0-3fd9-5ee1-8a95-e2b3c4523b86` | 374-397 [crates/ghook/src/statusline.rs:374-397] | Indexed function `downstream_timeout_kills_pipeline_survivors_holding_stdout` in `crates/ghook/src/statusline.rs`. [crates/ghook/src/statusline.rs:374-397] |
