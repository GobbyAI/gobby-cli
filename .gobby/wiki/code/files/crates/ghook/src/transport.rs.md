---
title: crates/ghook/src/transport.rs
type: code_file
provenance:
- file: crates/ghook/src/transport.rs
  ranges:
  - 31-36
  - 40-45
  - 49-55
  - 58-60
  - 63-65
  - 68-74
  - 77-81
  - 87-114
  - 119-125
  - 127-129
  - 137-204
  - 206-221
  - 225-232
  - 242-273
  - 286-290
  - 293-296
  - 299-305
  - 308-314
  - 317-332
  - 335-348
  - 351-404
  - 407-458
  - 461-493
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/ghook/src/transport.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Purpose

This file implements the enqueue-first transport path for `ghook`: it computes the inbox and quarantine locations under `~/.gobby/hooks/inbox`, generates lexicographically sortable envelope filenames with a critical/noncritical prefix, timestamp, and UUID, and persists envelopes atomically via temp-write, fsync, and rename before attempting delivery. It then posts the queued envelope to the daemon’s `/api/hooks/execute` endpoint, classifies failures as HTTP/connect/timeout/other, and deletes the inbox file only on a 2xx response; otherwise it leaves the file for replay and returns a `DeliveryReport` with diagnostics. It also provides quarantine helpers for malformed stdin, storing both the payload and metadata, plus tests that verify filename format, atomic writes, enqueueing, quarantine output, and post/cleanup behavior.
[crates/ghook/src/transport.rs:31-36]
[crates/ghook/src/transport.rs:40-45]
[crates/ghook/src/transport.rs:49-55]
[crates/ghook/src/transport.rs:58-60]
[crates/ghook/src/transport.rs:63-65]

## API Symbols

- `DeliveryOutcome` (type) component `DeliveryOutcome [type]` (`e7612d20-b3e0-50e1-a2b4-6e0c0d469eeb`) lines 31-36 [crates/ghook/src/transport.rs:31-36]
  - Signature: `pub enum DeliveryOutcome {`
  - Purpose: Indexed type `DeliveryOutcome` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:31-36]
- `DeliveryFailureKind` (type) component `DeliveryFailureKind [type]` (`635a2244-471a-578e-9431-93796af5a5e6`) lines 40-45 [crates/ghook/src/transport.rs:40-45]
  - Signature: `pub enum DeliveryFailureKind {`
  - Purpose: Indexed type `DeliveryFailureKind` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:40-45]
- `DeliveryReport` (class) component `DeliveryReport [class]` (`fa9467a0-9921-538e-9ec3-9369b2376355`) lines 49-55 [crates/ghook/src/transport.rs:49-55]
  - Signature: `pub struct DeliveryReport {`
  - Purpose: 'DeliveryReport' is a delivery result record that captures the overall 'DeliveryOutcome' plus optional failure classification, HTTP status code, response body, and transport error details for diagnostics. [crates/ghook/src/transport.rs:49-55]
- `inbox_dir` (function) component `inbox_dir [function]` (`337d52ed-6f16-5d5e-94ad-35a16cc183d4`) lines 58-60 [crates/ghook/src/transport.rs:58-60]
  - Signature: `pub fn inbox_dir() -> Result<PathBuf> {`
  - Purpose: Returns the 'gobby_home' path joined with 'hooks/inbox' as a 'PathBuf', propagating any error from 'gobby_core::gobby_home()'. [crates/ghook/src/transport.rs:58-60]
- `quarantine_dir` (function) component `quarantine_dir [function]` (`93cab374-71c7-5c68-b724-03dd57695d10`) lines 63-65 [crates/ghook/src/transport.rs:63-65]
  - Signature: `pub fn quarantine_dir() -> Result<PathBuf> {`
  - Purpose: Returns the 'inbox_dir()' path joined with '"quarantine"' as a 'PathBuf', propagating any error from 'inbox_dir()'. [crates/ghook/src/transport.rs:63-65]
- `ts13` (function) component `ts13 [function]` (`14549333-a1e5-5a38-976d-6535683526f7`) lines 68-74 [crates/ghook/src/transport.rs:68-74]
  - Signature: `pub fn ts13() -> String {`
  - Purpose: Returns the current system time as a 13-digit zero-padded string of milliseconds since the UNIX epoch, falling back to '0' if the clock is before the epoch. [crates/ghook/src/transport.rs:68-74]
- `envelope_filename` (function) component `envelope_filename [function]` (`f8be23e4-18cd-503a-8b93-098037bc2130`) lines 77-81 [crates/ghook/src/transport.rs:77-81]
  - Signature: `pub fn envelope_filename(critical: bool) -> String {`
  - Purpose: Returns a JSON filename of the form '<c|n>-<ts13>-<uuid>.json', using 'c' for critical envelopes and 'n' otherwise, with a fresh v4 UUID and the current 13-digit timestamp. [crates/ghook/src/transport.rs:77-81]
- `atomic_write` (function) component `atomic_write [function]` (`eaac2601-001e-5287-8c77-829087ecf84b`) lines 87-114 [crates/ghook/src/transport.rs:87-114]
  - Signature: `pub fn atomic_write(final_path: &Path, bytes: &[u8]) -> Result<()> {`
  - Purpose: Creates parent directories if needed, writes 'bytes' to a sibling '*.tmp' file, fsyncs it, atomically renames it over 'final_path', and best-effort fsyncs the parent directory to durably persist the update. [crates/ghook/src/transport.rs:87-114]
- `enqueue_to` (function) component `enqueue_to [function]` (`6b11eb8c-bf8a-56d0-9e90-68449253a47a`) lines 119-125 [crates/ghook/src/transport.rs:119-125]
  - Signature: `pub fn enqueue_to(envelope: &Envelope, inbox: &Path) -> Result<PathBuf> {`
  - Purpose: Serializes the given 'Envelope' to pretty-printed JSON, writes it atomically to 'inbox' under the filename derived from 'envelope.critical', and returns the resulting file path. [crates/ghook/src/transport.rs:119-125]
- `envelope_id_from_path` (function) component `envelope_id_from_path [function]` (`4d3ecd62-3b6c-5674-ae84-3d766ad79d69`) lines 127-129 [crates/ghook/src/transport.rs:127-129]
  - Signature: `fn envelope_id_from_path(enqueued_path: &Path) -> Option<&str> {`
  - Purpose: Returns the UTF-8 file stem of 'enqueued_path' as 'Some(&str)', or 'None' if the path has no stem or the stem is not valid UTF-8. [crates/ghook/src/transport.rs:127-129]
- `post_and_cleanup` (function) component `post_and_cleanup [function]` (`e58a7860-6a72-5954-a5c8-645a64bc7581`) lines 137-204 [crates/ghook/src/transport.rs:137-204]
  - Signature: `pub fn post_and_cleanup(`
  - Purpose: Posts the serialized 'Envelope' to '{daemon_url}{HOOKS_ENDPOINT}' with its headers and optional enqueue-derived envelope ID, deletes 'enqueued_path' only on a 2xx response, and otherwise returns a 'DeliveryReport' indicating the delivery failed or remains enqueued with HTTP or transport error details. [crates/ghook/src/transport.rs:137-204]
- `classify_transport_error` (function) component `classify_transport_error [function]` (`36a2f566-753b-51b7-bb72-507b303b984a`) lines 206-221 [crates/ghook/src/transport.rs:206-221]
  - Signature: `fn classify_transport_error(err: &ureq::Transport, error_text: &str) -> DeliveryFailureKind {`
  - Purpose: 'classify_transport_error' maps a 'ureq::Transport' to 'DeliveryFailureKind::Connect' for connection/DNS/proxy-connect failures, to 'DeliveryFailureKind::Timeout' when the error text contains “timed out” case-insensitively, and otherwise to 'DeliveryFailureKind::Other'. [crates/ghook/src/transport.rs:206-221]
- `quarantine_malformed` (function) component `quarantine_malformed [function]` (`8ccef319-bc5e-5ef7-bd04-a2d1e5b39563`) lines 225-232 [crates/ghook/src/transport.rs:225-232]
  - Signature: `pub fn quarantine_malformed(`
  - Purpose: Creates or resolves the quarantine directory and delegates to 'quarantine_malformed_at' to write the malformed 'stdin_bytes' along with 'json_error' into quarantine storage, returning the resulting 'PathBuf'. [crates/ghook/src/transport.rs:225-232]
- `quarantine_malformed_at` (function) component `quarantine_malformed_at [function]` (`3f58ad50-ce04-5837-8138-d0c2fadd711a`) lines 242-273 [crates/ghook/src/transport.rs:242-273]
  - Signature: `pub fn quarantine_malformed_at(`
  - Purpose: Creates a quarantined JSON record and accompanying metadata file under 'dir' using a critical/noncritical prefix plus timestamp and UUID, base64-encoding the provided stdin bytes and storing the JSON parse error as 'malformed_stdin', then returns the body file path. [crates/ghook/src/transport.rs:242-273]
- `ts13_is_13_digits` (function) component `ts13_is_13_digits [function]` (`3bbefc82-9169-5a99-878b-abfaec512d8a`) lines 286-290 [crates/ghook/src/transport.rs:286-290]
  - Signature: `fn ts13_is_13_digits() {`
  - Purpose: Verifies that 'ts13()' returns a 13-character string consisting entirely of ASCII digits. [crates/ghook/src/transport.rs:286-290]
- `filename_prefix_reflects_critical` (function) component `filename_prefix_reflects_critical [function]` (`6e376850-c377-5833-bbc5-e3762b9e6922`) lines 293-296 [crates/ghook/src/transport.rs:293-296]
  - Signature: `fn filename_prefix_reflects_critical() {`
  - Purpose: Verifies that 'envelope_filename(true)' begins with 'c' and 'envelope_filename(false)' begins with 'n', ensuring the filename prefix reflects the critical flag. [crates/ghook/src/transport.rs:293-296]
- `atomic_write_creates_parent_dirs` (function) component `atomic_write_creates_parent_dirs [function]` (`95ba8874-a2df-5675-8004-9ade63a041ff`) lines 299-305 [crates/ghook/src/transport.rs:299-305]
  - Signature: `fn atomic_write_creates_parent_dirs() {`
  - Purpose: Verifies that 'atomic_write' recursively creates missing parent directories before writing the file, and that the resulting file contains the expected bytes. [crates/ghook/src/transport.rs:299-305]
- `atomic_write_leaves_no_tmp_on_success` (function) component `atomic_write_leaves_no_tmp_on_success [function]` (`f513006f-b922-5b80-a39e-51e07d4a26b8`) lines 308-314 [crates/ghook/src/transport.rs:308-314]
  - Signature: `fn atomic_write_leaves_no_tmp_on_success() {`
  - Purpose: Verifies that 'atomic_write' successfully writes 'ok.json' without leaving the temporary 'ok.json.tmp' file behind. [crates/ghook/src/transport.rs:308-314]
- `enqueue_writes_envelope_to_inbox` (function) component `enqueue_writes_envelope_to_inbox [function]` (`450dc9d4-6e70-57cd-b566-b7e4d5ac9030`) lines 317-332 [crates/ghook/src/transport.rs:317-332]
  - Signature: `fn enqueue_writes_envelope_to_inbox() {`
  - Purpose: Creates a temporary 'Envelope', enqueues it to a directory, and asserts that the resulting persisted filename exists, starts with 'c', ends with '.json', and does not retain the '.tmp.json' suffix. [crates/ghook/src/transport.rs:317-332]
- `quarantine_writes_pair` (function) component `quarantine_writes_pair [function]` (`4adfa98a-3583-511e-90ce-99668ccedfc8`) lines 335-348 [crates/ghook/src/transport.rs:335-348]
  - Signature: `fn quarantine_writes_pair() {`
  - Purpose: Creates a quarantined body file and companion '.meta.json' for malformed stdin, then verifies both exist and that the metadata records 'reason = "malformed_stdin"', the JSON parse error, and a base64-encoded stdin payload. [crates/ghook/src/transport.rs:335-348]
- `post_and_cleanup_captures_success_response_body` (function) component `post_and_cleanup_captures_success_response_body [function]` (`ff6541be-441d-5821-a3bf-1ebf8f60f50d`) lines 351-404 [crates/ghook/src/transport.rs:351-404]
  - Signature: `fn post_and_cleanup_captures_success_response_body() {`
  - Purpose: Posts a queued envelope to '/api/hooks/execute', verifies the request payload and headers, and on a '200 OK' JSON response captures the response body while cleaning up the enqueued capture file. [crates/ghook/src/transport.rs:351-404]
- `post_and_cleanup_sends_droid_source_to_unified_hooks_endpoint` (function) component `post_and_cleanup_sends_droid_source_to_unified_hooks_endpoint [function]` (`50a4ebc4-a089-5f1d-9955-f2da9deda388`) lines 407-458 [crates/ghook/src/transport.rs:407-458]
  - Signature: `fn post_and_cleanup_sends_droid_source_to_unified_hooks_endpoint() {`
  - Purpose: Verifies that 'post_and_cleanup' sends a queued 'droid' hook envelope to the unified '/api/hooks/execute' endpoint with the expected envelope ID and normalized JSON payload, then cleans up the enqueued file after a successful '200 OK' response. [crates/ghook/src/transport.rs:407-458]
- `post_and_cleanup_captures_http_error_body` (function) component `post_and_cleanup_captures_http_error_body [function]` (`a1fa1f5d-8e49-5552-b64d-3aa8a5efb504`) lines 461-493 [crates/ghook/src/transport.rs:461-493]
  - Signature: `fn post_and_cleanup_captures_http_error_body() {`
  - Purpose: Tests that 'post_and_cleanup' records an HTTP delivery failure with status 500 and response body '"nope"' while leaving the enqueued file intact and reporting the outcome as 'Enqueued'. [crates/ghook/src/transport.rs:461-493]

