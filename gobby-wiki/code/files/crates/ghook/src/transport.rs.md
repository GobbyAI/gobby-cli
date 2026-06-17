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

<details>
<summary>Relevant source files</summary>

- [crates/ghook/src/transport.rs:31-36](crates/ghook/src/transport.rs#L31-L36), [crates/ghook/src/transport.rs:40-45](crates/ghook/src/transport.rs#L40-L45), [crates/ghook/src/transport.rs:49-55](crates/ghook/src/transport.rs#L49-L55), [crates/ghook/src/transport.rs:58-60](crates/ghook/src/transport.rs#L58-L60), [crates/ghook/src/transport.rs:63-65](crates/ghook/src/transport.rs#L63-L65), [crates/ghook/src/transport.rs:68-74](crates/ghook/src/transport.rs#L68-L74), [crates/ghook/src/transport.rs:77-81](crates/ghook/src/transport.rs#L77-L81), [crates/ghook/src/transport.rs:87-114](crates/ghook/src/transport.rs#L87-L114), [crates/ghook/src/transport.rs:119-125](crates/ghook/src/transport.rs#L119-L125), [crates/ghook/src/transport.rs:127-129](crates/ghook/src/transport.rs#L127-L129), [crates/ghook/src/transport.rs:137-204](crates/ghook/src/transport.rs#L137-L204), [crates/ghook/src/transport.rs:206-221](crates/ghook/src/transport.rs#L206-L221), [crates/ghook/src/transport.rs:225-232](crates/ghook/src/transport.rs#L225-L232), [crates/ghook/src/transport.rs:242-273](crates/ghook/src/transport.rs#L242-L273), [crates/ghook/src/transport.rs:286-290](crates/ghook/src/transport.rs#L286-L290), [crates/ghook/src/transport.rs:293-296](crates/ghook/src/transport.rs#L293-L296), [crates/ghook/src/transport.rs:299-305](crates/ghook/src/transport.rs#L299-L305), [crates/ghook/src/transport.rs:308-314](crates/ghook/src/transport.rs#L308-L314), [crates/ghook/src/transport.rs:317-332](crates/ghook/src/transport.rs#L317-L332), [crates/ghook/src/transport.rs:335-348](crates/ghook/src/transport.rs#L335-L348), [crates/ghook/src/transport.rs:351-404](crates/ghook/src/transport.rs#L351-L404), [crates/ghook/src/transport.rs:407-458](crates/ghook/src/transport.rs#L407-L458), [crates/ghook/src/transport.rs:461-493](crates/ghook/src/transport.rs#L461-L493)

</details>

# crates/ghook/src/transport.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Purpose

Implements the enqueue-first transport for `ghook`: it writes each envelope atomically into `~/.gobby/hooks/inbox/` with a sortable `<prefix>-<ts13>-<uuid>.json` name, then attempts the daemon POST and deletes the inbox file only on 2xx responses. The rest of the module supports that flow with path/timestamp/filename helpers, atomic write and enqueue utilities, error classification, quarantine handling for malformed envelopes, and `DeliveryOutcome`/`DeliveryReport` types that record whether delivery succeeded or was left for replay.
[crates/ghook/src/transport.rs:31-36]
[crates/ghook/src/transport.rs:40-45]
[crates/ghook/src/transport.rs:49-55]
[crates/ghook/src/transport.rs:58-60]
[crates/ghook/src/transport.rs:63-65]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `DeliveryOutcome` | type | `pub enum DeliveryOutcome {` | `DeliveryOutcome [type]` | `e7612d20-b3e0-50e1-a2b4-6e0c0d469eeb` | 31-36 [crates/ghook/src/transport.rs:31-36] | Indexed type `DeliveryOutcome` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:31-36] |
| `DeliveryFailureKind` | type | `pub enum DeliveryFailureKind {` | `DeliveryFailureKind [type]` | `635a2244-471a-578e-9431-93796af5a5e6` | 40-45 [crates/ghook/src/transport.rs:40-45] | Indexed type `DeliveryFailureKind` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:40-45] |
| `DeliveryReport` | class | `pub struct DeliveryReport {` | `DeliveryReport [class]` | `fa9467a0-9921-538e-9ec3-9369b2376355` | 49-55 [crates/ghook/src/transport.rs:49-55] | Indexed class `DeliveryReport` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:49-55] |
| `inbox_dir` | function | `pub fn inbox_dir() -> Result<PathBuf> {` | `inbox_dir [function]` | `337d52ed-6f16-5d5e-94ad-35a16cc183d4` | 58-60 [crates/ghook/src/transport.rs:58-60] | Indexed function `inbox_dir` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:58-60] |
| `quarantine_dir` | function | `pub fn quarantine_dir() -> Result<PathBuf> {` | `quarantine_dir [function]` | `93cab374-71c7-5c68-b724-03dd57695d10` | 63-65 [crates/ghook/src/transport.rs:63-65] | Indexed function `quarantine_dir` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:63-65] |
| `ts13` | function | `pub fn ts13() -> String {` | `ts13 [function]` | `14549333-a1e5-5a38-976d-6535683526f7` | 68-74 [crates/ghook/src/transport.rs:68-74] | Indexed function `ts13` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:68-74] |
| `envelope_filename` | function | `pub fn envelope_filename(critical: bool) -> String {` | `envelope_filename [function]` | `f8be23e4-18cd-503a-8b93-098037bc2130` | 77-81 [crates/ghook/src/transport.rs:77-81] | Indexed function `envelope_filename` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:77-81] |
| `atomic_write` | function | `pub fn atomic_write(final_path: &Path, bytes: &[u8]) -> Result<()> {` | `atomic_write [function]` | `eaac2601-001e-5287-8c77-829087ecf84b` | 87-114 [crates/ghook/src/transport.rs:87-114] | Indexed function `atomic_write` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:87-114] |
| `enqueue_to` | function | `pub fn enqueue_to(envelope: &Envelope, inbox: &Path) -> Result<PathBuf> {` | `enqueue_to [function]` | `6b11eb8c-bf8a-56d0-9e90-68449253a47a` | 119-125 [crates/ghook/src/transport.rs:119-125] | Indexed function `enqueue_to` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:119-125] |
| `envelope_id_from_path` | function | `fn envelope_id_from_path(enqueued_path: &Path) -> Option<&str> {` | `envelope_id_from_path [function]` | `4d3ecd62-3b6c-5674-ae84-3d766ad79d69` | 127-129 [crates/ghook/src/transport.rs:127-129] | Indexed function `envelope_id_from_path` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:127-129] |
| `post_and_cleanup` | function | `pub fn post_and_cleanup(` | `post_and_cleanup [function]` | `e58a7860-6a72-5954-a5c8-645a64bc7581` | 137-204 [crates/ghook/src/transport.rs:137-204] | Indexed function `post_and_cleanup` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:137-204] |
| `classify_transport_error` | function | `fn classify_transport_error(err: &ureq::Transport, error_text: &str) -> DeliveryFailureKind {` | `classify_transport_error [function]` | `36a2f566-753b-51b7-bb72-507b303b984a` | 206-221 [crates/ghook/src/transport.rs:206-221] | Indexed function `classify_transport_error` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:206-221] |
| `quarantine_malformed` | function | `pub fn quarantine_malformed(` | `quarantine_malformed [function]` | `8ccef319-bc5e-5ef7-bd04-a2d1e5b39563` | 225-232 [crates/ghook/src/transport.rs:225-232] | Indexed function `quarantine_malformed` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:225-232] |
| `quarantine_malformed_at` | function | `pub fn quarantine_malformed_at(` | `quarantine_malformed_at [function]` | `3f58ad50-ce04-5837-8138-d0c2fadd711a` | 242-273 [crates/ghook/src/transport.rs:242-273] | Indexed function `quarantine_malformed_at` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:242-273] |
| `ts13_is_13_digits` | function | `fn ts13_is_13_digits() {` | `ts13_is_13_digits [function]` | `3bbefc82-9169-5a99-878b-abfaec512d8a` | 286-290 [crates/ghook/src/transport.rs:286-290] | Indexed function `ts13_is_13_digits` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:286-290] |
| `filename_prefix_reflects_critical` | function | `fn filename_prefix_reflects_critical() {` | `filename_prefix_reflects_critical [function]` | `6e376850-c377-5833-bbc5-e3762b9e6922` | 293-296 [crates/ghook/src/transport.rs:293-296] | Indexed function `filename_prefix_reflects_critical` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:293-296] |
| `atomic_write_creates_parent_dirs` | function | `fn atomic_write_creates_parent_dirs() {` | `atomic_write_creates_parent_dirs [function]` | `95ba8874-a2df-5675-8004-9ade63a041ff` | 299-305 [crates/ghook/src/transport.rs:299-305] | Indexed function `atomic_write_creates_parent_dirs` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:299-305] |
| `atomic_write_leaves_no_tmp_on_success` | function | `fn atomic_write_leaves_no_tmp_on_success() {` | `atomic_write_leaves_no_tmp_on_success [function]` | `f513006f-b922-5b80-a39e-51e07d4a26b8` | 308-314 [crates/ghook/src/transport.rs:308-314] | Indexed function `atomic_write_leaves_no_tmp_on_success` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:308-314] |
| `enqueue_writes_envelope_to_inbox` | function | `fn enqueue_writes_envelope_to_inbox() {` | `enqueue_writes_envelope_to_inbox [function]` | `450dc9d4-6e70-57cd-b566-b7e4d5ac9030` | 317-332 [crates/ghook/src/transport.rs:317-332] | Indexed function `enqueue_writes_envelope_to_inbox` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:317-332] |
| `quarantine_writes_pair` | function | `fn quarantine_writes_pair() {` | `quarantine_writes_pair [function]` | `4adfa98a-3583-511e-90ce-99668ccedfc8` | 335-348 [crates/ghook/src/transport.rs:335-348] | Indexed function `quarantine_writes_pair` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:335-348] |
| `post_and_cleanup_captures_success_response_body` | function | `fn post_and_cleanup_captures_success_response_body() {` | `post_and_cleanup_captures_success_response_body [function]` | `ff6541be-441d-5821-a3bf-1ebf8f60f50d` | 351-404 [crates/ghook/src/transport.rs:351-404] | Indexed function `post_and_cleanup_captures_success_response_body` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:351-404] |
| `post_and_cleanup_sends_droid_source_to_unified_hooks_endpoint` | function | `fn post_and_cleanup_sends_droid_source_to_unified_hooks_endpoint() {` | `post_and_cleanup_sends_droid_source_to_unified_hooks_endpoint [function]` | `50a4ebc4-a089-5f1d-9955-f2da9deda388` | 407-458 [crates/ghook/src/transport.rs:407-458] | Indexed function `post_and_cleanup_sends_droid_source_to_unified_hooks_endpoint` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:407-458] |
| `post_and_cleanup_captures_http_error_body` | function | `fn post_and_cleanup_captures_http_error_body() {` | `post_and_cleanup_captures_http_error_body [function]` | `a1fa1f5d-8e49-5552-b64d-3aa8a5efb504` | 461-493 [crates/ghook/src/transport.rs:461-493] | Indexed function `post_and_cleanup_captures_http_error_body` in `crates/ghook/src/transport.rs`. [crates/ghook/src/transport.rs:461-493] |
