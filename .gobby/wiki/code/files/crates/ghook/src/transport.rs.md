---
title: crates/ghook/src/transport.rs
type: code_file
provenance:
- file: crates/ghook/src/transport.rs
  ranges:
  - 30-35
  - 39-44
  - 48-54
  - 57-60
  - 63-65
  - 68-74
  - 77-81
  - 87-110
  - 115-121
  - 129-193
  - 195-210
  - 214-221
  - 231-262
  - 273-309
  - 312-316
  - 319-322
  - 325-331
  - 334-340
  - 343-358
  - 361-374
  - 377-423
  - 426-470
  - 473-505
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/ghook/src/transport.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Purpose

`crates/ghook/src/transport.rs` exposes 23 indexed API symbols.
[crates/ghook/src/transport.rs:30-35]
[crates/ghook/src/transport.rs:39-44]
[crates/ghook/src/transport.rs:48-54]
[crates/ghook/src/transport.rs:57-60]
[crates/ghook/src/transport.rs:63-65]

## API Symbols

- `DeliveryOutcome` (type) component `DeliveryOutcome [type]` (`38278f8f-3021-5bd9-8ed4-1f1387e2a390`) lines 30-35 [crates/ghook/src/transport.rs:30-35]
  - Signature: `pub enum DeliveryOutcome {`
  - Purpose: Indexed type `DeliveryOutcome` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:30-35]
- `DeliveryFailureKind` (type) component `DeliveryFailureKind [type]` (`32df425a-3c69-555c-ae3e-5bd748c44be0`) lines 39-44 [crates/ghook/src/transport.rs:39-44]
  - Signature: `pub enum DeliveryFailureKind {`
  - Purpose: Indexed type `DeliveryFailureKind` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:39-44]
- `DeliveryReport` (class) component `DeliveryReport [class]` (`bef39da5-469f-5842-844b-f79c0a36424c`) lines 48-54 [crates/ghook/src/transport.rs:48-54]
  - Signature: `pub struct DeliveryReport {`
  - Purpose: `DeliveryReport` is a struct that captures the outcome of a delivery operation along with optional diagnostic details including failure classification, HTTP status code, response body, and transport errors. [crates/ghook/src/transport.rs:48-54]
- `inbox_dir` (function) component `inbox_dir [function]` (`e9c9467c-3919-5ae6-a767-25f37486596a`) lines 57-60 [crates/ghook/src/transport.rs:57-60]
  - Signature: `pub fn inbox_dir() -> Result<PathBuf> {`
  - Purpose: Returns a `Result<PathBuf>` pointing to the inbox directory located at `~/.gobby/hooks/inbox`, or an error if the home directory cannot be resolved. [crates/ghook/src/transport.rs:57-60]
- `quarantine_dir` (function) component `quarantine_dir [function]` (`e30f98d5-dc3f-5260-b87a-b1f3d6c21c01`) lines 63-65 [crates/ghook/src/transport.rs:63-65]
  - Signature: `pub fn quarantine_dir() -> Result<PathBuf> {`
  - Purpose: Returns a `Result<PathBuf>` pointing to the "quarantine" subdirectory within the inbox directory. [crates/ghook/src/transport.rs:63-65]
- `ts13` (function) component `ts13 [function]` (`be182237-20f0-51c1-b2bf-0e056dc95225`) lines 68-74 [crates/ghook/src/transport.rs:68-74]
  - Signature: `pub fn ts13() -> String {`
  - Purpose: Returns the current Unix timestamp in milliseconds as a 13-character zero-padded string. [crates/ghook/src/transport.rs:68-74]
- `envelope_filename` (function) component `envelope_filename [function]` (`b8998a77-d05c-5c56-aaa3-0935481e7673`) lines 77-81 [crates/ghook/src/transport.rs:77-81]
  - Signature: `pub fn envelope_filename(critical: bool) -> String {`
  - Purpose: Generates a JSON filename with a single-character priority prefix ('c' for critical, 'n' for non-critical), followed by a 13-digit timestamp and a UUID v4. [crates/ghook/src/transport.rs:77-81]
- `atomic_write` (function) component `atomic_write [function]` (`49bff09d-bc80-5330-8686-0613201dd747`) lines 87-110 [crates/ghook/src/transport.rs:87-110]
  - Signature: `pub fn atomic_write(final_path: &Path, bytes: &[u8]) -> Result<()> {`
  - Purpose: Atomically writes bytes to a file by creating a temporary file with explicit fsync, then atomically renaming it to the final path to ensure durability and prevent partial writes. [crates/ghook/src/transport.rs:87-110]
- `enqueue_to` (function) component `enqueue_to [function]` (`2fac1832-5b2f-5dd0-84ab-3d93aac08250`) lines 115-121 [crates/ghook/src/transport.rs:115-121]
  - Signature: `pub fn enqueue_to(envelope: &Envelope, inbox: &Path) -> Result<PathBuf> {`
  - Purpose: Atomically serializes an envelope to pretty-printed JSON and writes it to the inbox directory using a filename derived from the envelope's critical field, returning the output path. [crates/ghook/src/transport.rs:115-121]
- `post_and_cleanup` (function) component `post_and_cleanup [function]` (`5d8fb49f-6dc3-5cca-9131-8f4261403cc5`) lines 129-193 [crates/ghook/src/transport.rs:129-193]
  - Signature: `pub fn post_and_cleanup(`
  - Purpose: # Summary

This function POSTs an envelope serialized to JSON to a daemon HTTP endpoint, returns a `DeliveryReport` indicating delivery success/failure with status and error details, and deletes the enqueued file upon successful (2xx) response. [crates/ghook/src/transport.rs:129-193]
- `classify_transport_error` (function) component `classify_transport_error [function]` (`50593f01-6912-515a-b617-06d70e91b067`) lines 195-210 [crates/ghook/src/transport.rs:195-210]
  - Signature: `fn classify_transport_error(err: &ureq::Transport, error_text: &str) -> DeliveryFailureKind {`
  - Purpose: Classifies ureq HTTP transport errors into DeliveryFailureKind variants by mapping connection/DNS/proxy failures to `Connect`, timeout error text patterns to `Timeout`, and remaining errors to `Other`. [crates/ghook/src/transport.rs:195-210]
- `quarantine_malformed` (function) component `quarantine_malformed [function]` (`57ed436a-45e3-5078-b368-7f0dc18ee728`) lines 214-221 [crates/ghook/src/transport.rs:214-221]
  - Signature: `pub fn quarantine_malformed(`
  - Purpose: Quarantines malformed input bytes in the system quarantine directory and returns the resulting file path. [crates/ghook/src/transport.rs:214-221]
- `quarantine_malformed_at` (function) component `quarantine_malformed_at [function]` (`0db3487f-e809-5e04-ae32-d1667ef5597a`) lines 231-262 [crates/ghook/src/transport.rs:231-262]
  - Signature: `pub fn quarantine_malformed_at(`
  - Purpose: Quarantines malformed JSON input by atomically writing base64-encoded stdin and error metadata to uniquely timestamped JSON file pairs, using a critical/non-critical prefix for file identification. [crates/ghook/src/transport.rs:231-262]
- `read_http_request` (function) component `read_http_request [function]` (`d39b7862-21d6-558f-9857-a24f36805ba8`) lines 273-309 [crates/ghook/src/transport.rs:273-309]
  - Signature: `fn read_http_request(stream: &mut impl Read) -> String {`
  - Purpose: Buffers chunks from a stream until a complete HTTP request is accumulated by detecting the header terminator (`\r\n\r\n`) and reading the message body according to the Content-Length header. [crates/ghook/src/transport.rs:273-309]
- `ts13_is_13_digits` (function) component `ts13_is_13_digits [function]` (`c09fdab3-394e-53cf-898d-ed135e57e61e`) lines 312-316 [crates/ghook/src/transport.rs:312-316]
  - Signature: `fn ts13_is_13_digits() {`
  - Purpose: This test function asserts that `ts13()` returns a string of exactly 13 ASCII digit characters. [crates/ghook/src/transport.rs:312-316]
- `filename_prefix_reflects_critical` (function) component `filename_prefix_reflects_critical [function]` (`1370c7e3-5e85-52e2-a8ff-92d4aef7c330`) lines 319-322 [crates/ghook/src/transport.rs:319-322]
  - Signature: `fn filename_prefix_reflects_critical() {`
  - Purpose: This test asserts that `envelope_filename()` returns filenames prefixed with 'c' when called with `true` (critical) and 'n' when called with `false` (non-critical). [crates/ghook/src/transport.rs:319-322]
- `atomic_write_creates_parent_dirs` (function) component `atomic_write_creates_parent_dirs [function]` (`4cc397ae-18b1-5e5f-9882-a97fa76e6b8c`) lines 325-331 [crates/ghook/src/transport.rs:325-331]
  - Signature: `fn atomic_write_creates_parent_dirs() {`
  - Purpose: This test verifies that the `atomic_write` function automatically creates all required parent directories when writing to a nested file path. [crates/ghook/src/transport.rs:325-331]
- `atomic_write_leaves_no_tmp_on_success` (function) component `atomic_write_leaves_no_tmp_on_success [function]` (`df821fda-6169-52e1-a191-2eb3dbc89baa`) lines 334-340 [crates/ghook/src/transport.rs:334-340]
  - Signature: `fn atomic_write_leaves_no_tmp_on_success() {`
  - Purpose: Verifies that `atomic_write` removes its temporary staging file (`.json.tmp`) after successfully writing content to disk. [crates/ghook/src/transport.rs:334-340]
- `enqueue_writes_envelope_to_inbox` (function) component `enqueue_writes_envelope_to_inbox [function]` (`483e7067-05ae-587c-a968-e41f0b49966c`) lines 343-358 [crates/ghook/src/transport.rs:343-358]
  - Signature: `fn enqueue_writes_envelope_to_inbox() {`
  - Purpose: Tests that the `enqueue_to` function correctly persists an Envelope to a temporary directory with a filename starting with 'c' and ending in '.json' (excluding temporary files). [crates/ghook/src/transport.rs:343-358]
- `quarantine_writes_pair` (function) component `quarantine_writes_pair [function]` (`c0610617-b66f-5776-958f-59a401d6f8bb`) lines 361-374 [crates/ghook/src/transport.rs:361-374]
  - Signature: `fn quarantine_writes_pair() {`
  - Purpose: This test verifies that `quarantine_malformed_at()` creates a paired quarantine file and metadata JSON file containing the malformation reason, JSON parsing error, and base64-encoded input bytes when given invalid JSON input. [crates/ghook/src/transport.rs:361-374]
- `post_and_cleanup_captures_success_response_body` (function) component `post_and_cleanup_captures_success_response_body [function]` (`3db7c052-d1e7-5e52-82a7-0f4b05967021`) lines 377-423 [crates/ghook/src/transport.rs:377-423]
  - Signature: `fn post_and_cleanup_captures_success_response_body() {`
  - Purpose: Tests that `post_and_cleanup` successfully delivers an Envelope via HTTP POST to a mock server and correctly captures the 200 OK response before cleanup. [crates/ghook/src/transport.rs:377-423]
- `post_and_cleanup_sends_droid_source_to_unified_hooks_endpoint` (function) component `post_and_cleanup_sends_droid_source_to_unified_hooks_endpoint [function]` (`59f76343-6d99-550b-9247-2d45a5e29323`) lines 426-470 [crates/ghook/src/transport.rs:426-470]
  - Signature: `fn post_and_cleanup_sends_droid_source_to_unified_hooks_endpoint() {`
  - Purpose: This test validates that `post_and_cleanup` successfully POSTs a droid-sourced envelope containing PreToolUse hook metadata to the unified hooks endpoint (`/api/hooks/execute`) and deletes the local enqueued message file upon HTTP 200 delivery confirmation. [crates/ghook/src/transport.rs:426-470]
- `post_and_cleanup_captures_http_error_body` (function) component `post_and_cleanup_captures_http_error_body [function]` (`d906a088-ddc9-574a-8f53-12ca2bacbb63`) lines 473-505 [crates/ghook/src/transport.rs:473-505]
  - Signature: `fn post_and_cleanup_captures_http_error_body() {`
  - Purpose: Tests that `post_and_cleanup` captures HTTP error response bodies, records delivery failures with status code 500, and preserves the enqueued envelope file when posting to a failing endpoint. [crates/ghook/src/transport.rs:473-505]

