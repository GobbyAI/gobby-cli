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
[crates/ghook/src/transport.rs:68-74]
[crates/ghook/src/transport.rs:77-81]
[crates/ghook/src/transport.rs:87-110]
[crates/ghook/src/transport.rs:115-121]
[crates/ghook/src/transport.rs:129-193]
[crates/ghook/src/transport.rs:195-210]
[crates/ghook/src/transport.rs:214-221]
[crates/ghook/src/transport.rs:231-262]
[crates/ghook/src/transport.rs:273-309]
[crates/ghook/src/transport.rs:312-316]
[crates/ghook/src/transport.rs:319-322]
[crates/ghook/src/transport.rs:325-331]
[crates/ghook/src/transport.rs:334-340]
[crates/ghook/src/transport.rs:343-358]
[crates/ghook/src/transport.rs:361-374]
[crates/ghook/src/transport.rs:377-423]
[crates/ghook/src/transport.rs:426-470]
[crates/ghook/src/transport.rs:473-505]

## API Symbols

- `DeliveryOutcome` (type) component `DeliveryOutcome [type]` (`38278f8f-3021-5bd9-8ed4-1f1387e2a390`) lines 30-35 [crates/ghook/src/transport.rs:30-35]
  - Signature: `pub enum DeliveryOutcome {`
  - Purpose: Indexed type `DeliveryOutcome` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:30-35]
- `DeliveryFailureKind` (type) component `DeliveryFailureKind [type]` (`32df425a-3c69-555c-ae3e-5bd748c44be0`) lines 39-44 [crates/ghook/src/transport.rs:39-44]
  - Signature: `pub enum DeliveryFailureKind {`
  - Purpose: Indexed type `DeliveryFailureKind` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:39-44]
- `DeliveryReport` (class) component `DeliveryReport [class]` (`bef39da5-469f-5842-844b-f79c0a36424c`) lines 48-54 [crates/ghook/src/transport.rs:48-54]
  - Signature: `pub struct DeliveryReport {`
  - Purpose: `DeliveryReport` is a struct that encapsulates the outcome of a delivery attempt along with optional diagnostic fields for failure classification, HTTP status code, response body, and transport errors. [crates/ghook/src/transport.rs:48-54]
- `inbox_dir` (function) component `inbox_dir [function]` (`e9c9467c-3919-5ae6-a767-25f37486596a`) lines 57-60 [crates/ghook/src/transport.rs:57-60]
  - Signature: `pub fn inbox_dir() -> Result<PathBuf> {`
  - Purpose: Returns the file system path to `~/.gobby/hooks/inbox`, or an error if the home directory cannot be resolved. [crates/ghook/src/transport.rs:57-60]
- `quarantine_dir` (function) component `quarantine_dir [function]` (`e30f98d5-dc3f-5260-b87a-b1f3d6c21c01`) lines 63-65 [crates/ghook/src/transport.rs:63-65]
  - Signature: `pub fn quarantine_dir() -> Result<PathBuf> {`
  - Purpose: Constructs and returns the PathBuf for the 'quarantine' subdirectory nested within the inbox directory. [crates/ghook/src/transport.rs:63-65]
- `ts13` (function) component `ts13 [function]` (`be182237-20f0-51c1-b2bf-0e056dc95225`) lines 68-74 [crates/ghook/src/transport.rs:68-74]
  - Signature: `pub fn ts13() -> String {`
  - Purpose: Returns the current Unix timestamp in milliseconds formatted as a 13-digit zero-padded string. [crates/ghook/src/transport.rs:68-74]
- `envelope_filename` (function) component `envelope_filename [function]` (`b8998a77-d05c-5c56-aaa3-0935481e7673`) lines 77-81 [crates/ghook/src/transport.rs:77-81]
  - Signature: `pub fn envelope_filename(critical: bool) -> String {`
  - Purpose: Generates a JSON filename with a critical-status prefix ('c' or 'n'), a 13-digit timestamp, and a UUID v4 for unique identification. [crates/ghook/src/transport.rs:77-81]
- `atomic_write` (function) component `atomic_write [function]` (`49bff09d-bc80-5330-8686-0613201dd747`) lines 87-110 [crates/ghook/src/transport.rs:87-110]
  - Signature: `pub fn atomic_write(final_path: &Path, bytes: &[u8]) -> Result<()> {`
  - Purpose: Performs atomic file write by creating parent directories, writing bytes to a temporary file with fsync, then atomically renaming it to the final path, ensuring crash-safe durability. [crates/ghook/src/transport.rs:87-110]
- `enqueue_to` (function) component `enqueue_to [function]` (`2fac1832-5b2f-5dd0-84ab-3d93aac08250`) lines 115-121 [crates/ghook/src/transport.rs:115-121]
  - Signature: `pub fn enqueue_to(envelope: &Envelope, inbox: &Path) -> Result<PathBuf> {`
  - Purpose: Serializes an envelope to pretty-printed JSON and atomically writes it to a generated filename in the specified inbox directory, returning the resulting file path. [crates/ghook/src/transport.rs:115-121]
- `post_and_cleanup` (function) component `post_and_cleanup [function]` (`5d8fb49f-6dc3-5cca-9131-8f4261403cc5`) lines 129-193 [crates/ghook/src/transport.rs:129-193]
  - Signature: `pub fn post_and_cleanup(`
  - Purpose: Sends an HTTP POST request containing a JSON-serialized envelope to a daemon webhook endpoint and returns a DeliveryReport, removing the enqueued file only on successful (2xx) response. [crates/ghook/src/transport.rs:129-193]
- `classify_transport_error` (function) component `classify_transport_error [function]` (`50593f01-6912-515a-b617-06d70e91b067`) lines 195-210 [crates/ghook/src/transport.rs:195-210]
  - Signature: `fn classify_transport_error(err: &ureq::Transport, error_text: &str) -> DeliveryFailureKind {`
  - Purpose: Maps ureq transport errors to `DeliveryFailureKind` variants by classifying connection failures (including DNS and proxy errors) as `Connect`, timeout errors as `Timeout`, and all others as `Other`. [crates/ghook/src/transport.rs:195-210]
- `quarantine_malformed` (function) component `quarantine_malformed [function]` (`57ed436a-45e3-5078-b368-7f0dc18ee728`) lines 214-221 [crates/ghook/src/transport.rs:214-221]
  - Signature: `pub fn quarantine_malformed(`
  - Purpose: Quarantines malformed JSON input to the default quarantine directory, returning the resulting file path or an error. [crates/ghook/src/transport.rs:214-221]
- `quarantine_malformed_at` (function) component `quarantine_malformed_at [function]` (`0db3487f-e809-5e04-ae32-d1667ef5597a`) lines 231-262 [crates/ghook/src/transport.rs:231-262]
  - Signature: `pub fn quarantine_malformed_at(`
  - Purpose: Atomically writes base64-encoded malformed JSON input and error metadata to uniquely-timestamped quarantine files, returning the primary data file path. [crates/ghook/src/transport.rs:231-262]
- `read_http_request` (function) component `read_http_request [function]` (`d39b7862-21d6-558f-9857-a24f36805ba8`) lines 273-309 [crates/ghook/src/transport.rs:273-309]
  - Signature: `fn read_http_request(stream: &mut impl Read) -> String {`
  - Purpose: Reads HTTP request data from a stream in 1024-byte chunks, locates the header/body boundary (`\r\n\r\n`), extracts the `Content-Length` header value, and returns the complete request as a String once the full body is received. [crates/ghook/src/transport.rs:273-309]
- `ts13_is_13_digits` (function) component `ts13_is_13_digits [function]` (`c09fdab3-394e-53cf-898d-ed135e57e61e`) lines 312-316 [crates/ghook/src/transport.rs:312-316]
  - Signature: `fn ts13_is_13_digits() {`
  - Purpose: Tests that `ts13()` returns a string of exactly 13 ASCII digits. [crates/ghook/src/transport.rs:312-316]
- `filename_prefix_reflects_critical` (function) component `filename_prefix_reflects_critical [function]` (`1370c7e3-5e85-52e2-a8ff-92d4aef7c330`) lines 319-322 [crates/ghook/src/transport.rs:319-322]
  - Signature: `fn filename_prefix_reflects_critical() {`
  - Purpose: This test function verifies that `envelope_filename()` returns filenames prefixed with 'c' for critical envelopes and 'n' for non-critical envelopes based on a boolean critical flag. [crates/ghook/src/transport.rs:319-322]
- `atomic_write_creates_parent_dirs` (function) component `atomic_write_creates_parent_dirs [function]` (`4cc397ae-18b1-5e5f-9882-a97fa76e6b8c`) lines 325-331 [crates/ghook/src/transport.rs:325-331]
  - Signature: `fn atomic_write_creates_parent_dirs() {`
  - Purpose: This test verifies that the `atomic_write` function creates missing parent directories and atomically writes the specified byte content to a nested file path. [crates/ghook/src/transport.rs:325-331]
- `atomic_write_leaves_no_tmp_on_success` (function) component `atomic_write_leaves_no_tmp_on_success [function]` (`df821fda-6169-52e1-a191-2eb3dbc89baa`) lines 334-340 [crates/ghook/src/transport.rs:334-340]
  - Signature: `fn atomic_write_leaves_no_tmp_on_success() {`
  - Purpose: Tests that `atomic_write` successfully removes its temporary `.tmp` file after persisting data to the target file. [crates/ghook/src/transport.rs:334-340]
- `enqueue_writes_envelope_to_inbox` (function) component `enqueue_writes_envelope_to_inbox [function]` (`483e7067-05ae-587c-a968-e41f0b49966c`) lines 343-358 [crates/ghook/src/transport.rs:343-358]
  - Signature: `fn enqueue_writes_envelope_to_inbox() {`
  - Purpose: Verifies that `enqueue_to` persists an Envelope to a finalized (non-temporary) JSON file with a filename starting with 'c'. [crates/ghook/src/transport.rs:343-358]
- `quarantine_writes_pair` (function) component `quarantine_writes_pair [function]` (`c0610617-b66f-5776-958f-59a401d6f8bb`) lines 361-374 [crates/ghook/src/transport.rs:361-374]
  - Signature: `fn quarantine_writes_pair() {`
  - Purpose: Verifies that quarantining malformed JSON input creates both a body file and an accompanying metadata JSON file containing the error reason, JSON parse error message, and base64-encoded stdin bytes. [crates/ghook/src/transport.rs:361-374]
- `post_and_cleanup_captures_success_response_body` (function) component `post_and_cleanup_captures_success_response_body [function]` (`3db7c052-d1e7-5e52-82a7-0f4b05967021`) lines 377-423 [crates/ghook/src/transport.rs:377-423]
  - Signature: `fn post_and_cleanup_captures_success_response_body() {`
  - Purpose: This test validates that `post_and_cleanup()` correctly serializes and POSTs an Envelope with SessionStart event data to a remote HTTP endpoint, and properly reports successful delivery when receiving an HTTP 200 response. [crates/ghook/src/transport.rs:377-423]
- `post_and_cleanup_sends_droid_source_to_unified_hooks_endpoint` (function) component `post_and_cleanup_sends_droid_source_to_unified_hooks_endpoint [function]` (`59f76343-6d99-550b-9247-2d45a5e29323`) lines 426-470 [crates/ghook/src/transport.rs:426-470]
  - Signature: `fn post_and_cleanup_sends_droid_source_to_unified_hooks_endpoint() {`
  - Purpose: This test function verifies that `post_and_cleanup` correctly sends a droid-sourced PreToolUse hook envelope via HTTP POST to a unified hooks endpoint with proper request formatting, and successfully deletes the temporary file after receiving a 200 response. [crates/ghook/src/transport.rs:426-470]
- `post_and_cleanup_captures_http_error_body` (function) component `post_and_cleanup_captures_http_error_body [function]` (`d906a088-ddc9-574a-8f53-12ca2bacbb63`) lines 473-505 [crates/ghook/src/transport.rs:473-505]
  - Signature: `fn post_and_cleanup_captures_http_error_body() {`
  - Purpose: This test verifies that `post_and_cleanup` correctly captures HTTP error responses (status code and body), reports HTTP delivery failure, and preserves the enqueued envelope file when posting fails with a 500 error. [crates/ghook/src/transport.rs:473-505]

