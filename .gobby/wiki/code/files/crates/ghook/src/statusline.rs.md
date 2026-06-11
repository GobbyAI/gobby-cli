---
title: crates/ghook/src/statusline.rs
type: code_file
provenance:
- file: crates/ghook/src/statusline.rs
  ranges:
  - 21-23
  - 25-31
  - 33-63
  - 65-100
  - 102-115
  - 117-130
  - 132-165
  - 168-172
  - 175-179
  - 193-229
  - 232-237
  - 240-244
  - 247-251
  - 254-260
  - 263-268
  - 271-298
  - 301-312
  - 315-335
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/ghook/src/statusline.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Purpose

`crates/ghook/src/statusline.rs` exposes 18 indexed API symbols.
[crates/ghook/src/statusline.rs:21-23]
[crates/ghook/src/statusline.rs:25-31]
[crates/ghook/src/statusline.rs:33-63]
[crates/ghook/src/statusline.rs:65-100]
[crates/ghook/src/statusline.rs:102-115]

## API Symbols

- `is_statusline_hook` (function) component `is_statusline_hook [function]` (`c86d2f6b-5515-5743-b08b-d9d2e3b61de3`) lines 21-23 [crates/ghook/src/statusline.rs:21-23]
  - Signature: `pub(crate) fn is_statusline_hook(cli: &str, hook_type: &str) -> bool {`
  - Purpose: Returns `true` if the `cli` parameter matches "claude" (case-insensitive) and the `hook_type` parameter exactly equals "statusline", otherwise returns `false`. [crates/ghook/src/statusline.rs:21-23]
- `handle` (function) component `handle [function]` (`f34e8831-6c29-5cc7-b206-1f7145e32db1`) lines 25-31 [crates/ghook/src/statusline.rs:25-31]
  - Signature: `pub(crate) fn handle(stdin_raw: &[u8]) -> ExitCode {`
  - Purpose: Wrapper that retrieves the optional GOBBY_STATUSLINE_DOWNSTREAM environment variable and daemon URL, then delegates to handle_with with raw stdin and locked stdout. [crates/ghook/src/statusline.rs:25-31]
- `handle_with` (function) component `handle_with [function]` (`c716be06-8973-5a77-9c3f-04bb18b56d1a`) lines 33-63 [crates/ghook/src/statusline.rs:33-63]
  - Signature: `fn handle_with(`
  - Purpose: This function deserializes raw stdin as JSON, extracts and posts a payload to a specified daemon URL via best-effort delivery, and optionally executes a downstream command whose output is piped to stdout before returning success. [crates/ghook/src/statusline.rs:33-63]
- `extract_payload` (function) component `extract_payload [function]` (`b2fff304-4d67-5c5e-9a9c-d7b28b247e89`) lines 65-100 [crates/ghook/src/statusline.rs:65-100]
  - Signature: `fn extract_payload(input: &Value) -> Option<Value> {`
  - Purpose: Validates that the input contains a truthy `session_id`, then extracts and flattens a JSON payload containing the session_id, model_id, and token metrics (input/output/cache tokens) from nested cost and model objects, returning `None` on validation failure. [crates/ghook/src/statusline.rs:65-100]
- `python_truthy` (function) component `python_truthy [function]` (`bb0f9094-20a7-56b8-a842-d9aa79367388`) lines 102-115 [crates/ghook/src/statusline.rs:102-115]
  - Signature: `fn python_truthy(value: &Value) -> bool {`
  - Purpose: This function evaluates the truthiness of a Value according to Python semantics, returning false for null, boolean false, zero-valued numbers, and empty strings/arrays/objects, and true otherwise. [crates/ghook/src/statusline.rs:102-115]
- `post_to_daemon_best_effort` (function) component `post_to_daemon_best_effort [function]` (`efd40423-19fa-51cd-b821-f5d4ac126fa9`) lines 117-130 [crates/ghook/src/statusline.rs:117-130]
  - Signature: `fn post_to_daemon_best_effort(payload: Value, daemon_url: &str) {`
  - Purpose: Spawns a non-blocking thread to POST a JSON payload to a daemon endpoint with separate request and join timeouts, silently discarding all results. [crates/ghook/src/statusline.rs:117-130]
- `forward_downstream` (function) component `forward_downstream [function]` (`e6350b14-b8f1-5d41-8650-8a0bcc0d4e27`) lines 132-165 [crates/ghook/src/statusline.rs:132-165]
  - Signature: `fn forward_downstream(command: &OsStr, stdin_raw: &[u8]) -> Option<Vec<u8>> {`
  - Purpose: Spawns a downstream shell command with piped stdin, waits for completion with a timeout, and returns non-empty stdout or None on timeout/failure. [crates/ghook/src/statusline.rs:132-165]
- `downstream_shell_command` (function) component `downstream_shell_command [function]` (`eff88548-f744-5010-a18d-685cf0a2b5f8`) lines 168-172 [crates/ghook/src/statusline.rs:168-172]
  - Signature: `fn downstream_shell_command(command: &OsStr) -> Command {`
  - Purpose: Returns a `Command` configured to execute the provided `OsStr` argument via `sh -c`. [crates/ghook/src/statusline.rs:168-172]
- `downstream_shell_command` (function) component `downstream_shell_command [function]` (`e9d171c7-d04b-54e2-8579-4003deb4a67c`) lines 175-179 [crates/ghook/src/statusline.rs:175-179]
  - Signature: `fn downstream_shell_command(command: &OsStr) -> Command {`
  - Purpose: This function constructs a `std::process::Command` that invokes the Windows command shell (`cmd.exe`) with the `/C` flag to execute a provided `OsStr` command string. [crates/ghook/src/statusline.rs:175-179]
- `read_http_request` (function) component `read_http_request [function]` (`8ef4d920-11b6-52d1-a1cd-e7ffa9737cc2`) lines 193-229 [crates/ghook/src/statusline.rs:193-229]
  - Signature: `fn read_http_request(stream: &mut impl Read) -> String {`
  - Purpose: Reads an HTTP request from a stream by buffering chunks until headers are parsed to extract the Content-Length value, then continues reading until the complete message (headers plus body) is received, returning it as a String. [crates/ghook/src/statusline.rs:193-229]
- `recognizes_only_claude_statusline_hook` (function) component `recognizes_only_claude_statusline_hook [function]` (`afdebd6b-cdb6-5532-a5ea-7abc0ecee51c`) lines 232-237 [crates/ghook/src/statusline.rs:232-237]
  - Signature: `fn recognizes_only_claude_statusline_hook() {`
  - Purpose: This test verifies that `is_statusline_hook()` returns `true` exclusively when the model parameter is "claude" (case-insensitive) and the hook type is "statusline". [crates/ghook/src/statusline.rs:232-237]
- `extract_payload_matches_full_golden_fixture` (function) component `extract_payload_matches_full_golden_fixture [function]` (`6a903184-0148-5a84-a0ca-fe4decb59eb3`) lines 240-244 [crates/ghook/src/statusline.rs:240-244]
  - Signature: `fn extract_payload_matches_full_golden_fixture() {`
  - Purpose: This unit test validates that the `extract_payload` function correctly extracts and returns the expected JSON payload from a valid input string, asserting equality against a golden fixture reference value. [crates/ghook/src/statusline.rs:240-244]
- `extract_payload_matches_default_golden_fixture` (function) component `extract_payload_matches_default_golden_fixture [function]` (`0b85c3d4-8668-5075-9015-6b01e23eb192`) lines 247-251 [crates/ghook/src/statusline.rs:247-251]
  - Signature: `fn extract_payload_matches_default_golden_fixture() {`
  - Purpose: A unit test that asserts `extract_payload()` correctly returns the expected JSON payload when given a default input, verified against a golden fixture. [crates/ghook/src/statusline.rs:247-251]
- `extract_payload_returns_none_without_session_id` (function) component `extract_payload_returns_none_without_session_id [function]` (`19e06d55-2033-57e4-88db-c47e61f80e05`) lines 254-260 [crates/ghook/src/statusline.rs:254-260]
  - Signature: `fn extract_payload_returns_none_without_session_id() {`
  - Purpose: This unit test function verifies that `extract_payload()` returns `None` when the input JSON lacks a valid `session_id` field or contains a `session_id` with an empty string, null, numeric, or boolean value. [crates/ghook/src/statusline.rs:254-260]
- `malformed_json_exits_success_without_stdout` (function) component `malformed_json_exits_success_without_stdout [function]` (`73c893e2-a9a8-5ae2-b5b7-389f29b9d17c`) lines 263-268 [crates/ghook/src/statusline.rs:263-268]
  - Signature: `fn malformed_json_exits_success_without_stdout() {`
  - Purpose: This test function verifies that the `handle_with` function returns an exit code of `SUCCESS` and produces no stdout output when invoked with malformed JSON input. [crates/ghook/src/statusline.rs:263-268]
- `posts_statusline_payload_to_daemon_endpoint` (function) component `posts_statusline_payload_to_daemon_endpoint [function]` (`e0adf029-e6a7-557a-9778-da87cd6b6591`) lines 271-298 [crates/ghook/src/statusline.rs:271-298]
  - Signature: `fn posts_statusline_payload_to_daemon_endpoint() {`
  - Purpose: This integration test verifies that the application POSTs a validated JSON statusline payload to the `/api/sessions/statusline` endpoint, receives an HTTP 200 response, and exits successfully. [crates/ghook/src/statusline.rs:271-298]
- `downstream_stdout_passthrough_preserves_bytes` (function) component `downstream_stdout_passthrough_preserves_bytes [function]` (`2f4590de-7f5c-58eb-b7ab-cc8ec1b0cb39`) lines 301-312 [crates/ghook/src/statusline.rs:301-312]
  - Signature: `fn downstream_stdout_passthrough_preserves_bytes() {`
  - Purpose: This unit test verifies that the `handle_with` function preserves the exact raw bytes of downstream stdout output without modification when processing a session request. [crates/ghook/src/statusline.rs:301-312]
- `downstream_timeout_returns_before_six_seconds` (function) component `downstream_timeout_returns_before_six_seconds [function]` (`0b6ddeff-5237-5374-b110-0e230f57d481`) lines 315-335 [crates/ghook/src/statusline.rs:315-335]
  - Signature: `fn downstream_timeout_returns_before_six_seconds() {`
  - Purpose: This test verifies that a downstream timeout handler successfully terminates a long-running subprocess before six seconds elapse, preventing indefinite CI hangs. [crates/ghook/src/statusline.rs:315-335]

