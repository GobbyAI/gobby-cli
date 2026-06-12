---
title: crates/ghook/src/planned_shutdown.rs
type: code_file
provenance:
- file: crates/ghook/src/planned_shutdown.rs
  ranges:
  - 21-27
  - 29-37
  - 39-50
  - 52-54
  - 56-62
  - 64-75
  - 77-79
  - 81-84
  - 86-113
  - 115-119
  - 121-130
  - 132-134
  - 136-142
  - 144-152
  - 154-160
  - 162-169
  - 171-176
  - 178-184
  - 195-198
  - 201-206
  - 209-219
  - 222-237
  - 240-282
  - 285-291
  - 294-304
  - 307-323
  - 326-328
  - 331-353
  - 356-366
  - 369-399
  - 402-408
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/ghook/src/planned_shutdown.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Purpose

`crates/ghook/src/planned_shutdown.rs` exposes 31 indexed API symbols.
[crates/ghook/src/planned_shutdown.rs:21-27]
[crates/ghook/src/planned_shutdown.rs:29-37]
[crates/ghook/src/planned_shutdown.rs:39-50]
[crates/ghook/src/planned_shutdown.rs:52-54]
[crates/ghook/src/planned_shutdown.rs:56-62]

## API Symbols

- `should_skip_dispatch` (function) component `should_skip_dispatch [function]` (`e42c0c01-e1ab-56b4-87ca-42cd184ae834`) lines 21-27 [crates/ghook/src/planned_shutdown.rs:21-27]
  - Signature: `pub fn should_skip_dispatch(hook_type: &str) -> bool {`
  - Purpose: Indexed function `should_skip_dispatch` in `crates/ghook/src/planned_shutdown.rs`. [crates/ghook/src/planned_shutdown.rs:21-27]
- `suppress_after_failed_post` (function) component `suppress_after_failed_post [function]` (`480a97fa-f382-56de-81d6-231456e02757`) lines 29-37 [crates/ghook/src/planned_shutdown.rs:29-37]
  - Signature: `pub fn suppress_after_failed_post(`
  - Purpose: Indexed function `suppress_after_failed_post` in `crates/ghook/src/planned_shutdown.rs`. [crates/ghook/src/planned_shutdown.rs:29-37]
- `suppress_after_failed_post_with_marker` (function) component `suppress_after_failed_post_with_marker [function]` (`915605ab-403f-5ea7-919f-0d8b79d6bfdc`) lines 39-50 [crates/ghook/src/planned_shutdown.rs:39-50]
  - Signature: `fn suppress_after_failed_post_with_marker(`
  - Purpose: Indexed function `suppress_after_failed_post_with_marker` in `crates/ghook/src/planned_shutdown.rs`. [crates/ghook/src/planned_shutdown.rs:39-50]
- `is_stop_hook` (function) component `is_stop_hook [function]` (`8ede0f52-e4f0-5d0b-b223-36bd5ea11bb2`) lines 52-54 [crates/ghook/src/planned_shutdown.rs:52-54]
  - Signature: `pub fn is_stop_hook(hook_type: &str) -> bool {`
  - Purpose: Indexed function `is_stop_hook` in `crates/ghook/src/planned_shutdown.rs`. [crates/ghook/src/planned_shutdown.rs:52-54]
- `should_skip_dispatch_with` (function) component `should_skip_dispatch_with [function]` (`f74d3a29-061a-5f08-a9ba-0d9e26b44077`) lines 56-62 [crates/ghook/src/planned_shutdown.rs:56-62]
  - Signature: `fn should_skip_dispatch_with(`
  - Purpose: Indexed function `should_skip_dispatch_with` in `crates/ghook/src/planned_shutdown.rs`. [crates/ghook/src/planned_shutdown.rs:56-62]
- `should_suppress_failed_post` (function) component `should_suppress_failed_post [function]` (`85b48489-0263-565e-bf19-5a18845e3c2d`) lines 64-75 [crates/ghook/src/planned_shutdown.rs:64-75]
  - Signature: `fn should_suppress_failed_post(`
  - Purpose: Indexed function `should_suppress_failed_post` in `crates/ghook/src/planned_shutdown.rs`. [crates/ghook/src/planned_shutdown.rs:64-75]
- `fresh_shutdown_marker` (function) component `fresh_shutdown_marker [function]` (`fd6c5466-4319-59b8-b435-fd161c8b2405`) lines 77-79 [crates/ghook/src/planned_shutdown.rs:77-79]
  - Signature: `fn fresh_shutdown_marker(home: &Path) -> bool {`
  - Purpose: Indexed function `fresh_shutdown_marker` in `crates/ghook/src/planned_shutdown.rs`. [crates/ghook/src/planned_shutdown.rs:77-79]
- `fresh_shutdown_marker_at` (function) component `fresh_shutdown_marker_at [function]` (`ccb6214b-2a4e-5530-8a2b-9302a356ea6f`) lines 81-84 [crates/ghook/src/planned_shutdown.rs:81-84]
  - Signature: `fn fresh_shutdown_marker_at(home: &Path, now: f64, allow_seconds: f64) -> bool {`
  - Purpose: Indexed function `fresh_shutdown_marker_at` in `crates/ghook/src/planned_shutdown.rs`. [crates/ghook/src/planned_shutdown.rs:81-84]
- `marker_is_allowed_and_fresh` (function) component `marker_is_allowed_and_fresh [function]` (`b3c3b5d5-6d52-5c9e-91f7-aa4dfaa3b406`) lines 86-113 [crates/ghook/src/planned_shutdown.rs:86-113]
  - Signature: `fn marker_is_allowed_and_fresh(marker: &Value, now: f64, allow_seconds: f64) -> bool {`
  - Purpose: Indexed function `marker_is_allowed_and_fresh` in `crates/ghook/src/planned_shutdown.rs`. [crates/ghook/src/planned_shutdown.rs:86-113]
- `read_marker` (function) component `read_marker [function]` (`05688997-63c0-5bf0-9083-978328be448d`) lines 115-119 [crates/ghook/src/planned_shutdown.rs:115-119]
  - Signature: `fn read_marker(path: &Path) -> Option<Value> {`
  - Purpose: Indexed function `read_marker` in `crates/ghook/src/planned_shutdown.rs`. [crates/ghook/src/planned_shutdown.rs:115-119]
- `daemon_is_reachable` (function) component `daemon_is_reachable [function]` (`7a9b0033-3751-5d7e-9d9e-5665b2b2f174`) lines 121-130 [crates/ghook/src/planned_shutdown.rs:121-130]
  - Signature: `fn daemon_is_reachable(daemon_url: &str) -> bool {`
  - Purpose: Indexed function `daemon_is_reachable` in `crates/ghook/src/planned_shutdown.rs`. [crates/ghook/src/planned_shutdown.rs:121-130]
- `marker_home` (function) component `marker_home [function]` (`fea7a275-648e-59e3-a686-39b888fc347c`) lines 132-134 [crates/ghook/src/planned_shutdown.rs:132-134]
  - Signature: `fn marker_home() -> Option<PathBuf> {`
  - Purpose: Indexed function `marker_home` in `crates/ghook/src/planned_shutdown.rs`. [crates/ghook/src/planned_shutdown.rs:132-134]
- `allow_seconds` (function) component `allow_seconds [function]` (`933ab78d-939e-52d0-983c-8e96010de45e`) lines 136-142 [crates/ghook/src/planned_shutdown.rs:136-142]
  - Signature: `fn allow_seconds() -> f64 {`
  - Purpose: Indexed function `allow_seconds` in `crates/ghook/src/planned_shutdown.rs`. [crates/ghook/src/planned_shutdown.rs:136-142]
- `allow_seconds_from_env` (function) component `allow_seconds_from_env [function]` (`fbf08e40-b0bd-5487-8b9d-5305c01947b5`) lines 144-152 [crates/ghook/src/planned_shutdown.rs:144-152]
  - Signature: `fn allow_seconds_from_env(value: Option<&str>) -> f64 {`
  - Purpose: Indexed function `allow_seconds_from_env` in `crates/ghook/src/planned_shutdown.rs`. [crates/ghook/src/planned_shutdown.rs:144-152]
- `optional_float` (function) component `optional_float [function]` (`76bb012b-1464-5bec-b7e2-edf391fe3245`) lines 154-160 [crates/ghook/src/planned_shutdown.rs:154-160]
  - Signature: `fn optional_float(value: &Value) -> Option<f64> {`
  - Purpose: Indexed function `optional_float` in `crates/ghook/src/planned_shutdown.rs`. [crates/ghook/src/planned_shutdown.rs:154-160]
- `value_as_text` (function) component `value_as_text [function]` (`aa1adcdc-a165-5be2-9dbb-a77535328a6a`) lines 162-169 [crates/ghook/src/planned_shutdown.rs:162-169]
  - Signature: `fn value_as_text(value: &Value) -> Option<String> {`
  - Purpose: Indexed function `value_as_text` in `crates/ghook/src/planned_shutdown.rs`. [crates/ghook/src/planned_shutdown.rs:162-169]
- `now_secs` (function) component `now_secs [function]` (`4c480cc4-6019-53b3-94ee-887000152de5`) lines 171-176 [crates/ghook/src/planned_shutdown.rs:171-176]
  - Signature: `fn now_secs() -> f64 {`
  - Purpose: Indexed function `now_secs` in `crates/ghook/src/planned_shutdown.rs`. [crates/ghook/src/planned_shutdown.rs:171-176]
- `delete_enqueued` (function) component `delete_enqueued [function]` (`34768c55-e686-5b08-adf7-aff1710edf15`) lines 178-184 [crates/ghook/src/planned_shutdown.rs:178-184]
  - Signature: `fn delete_enqueued(enqueued_path: &Path) -> bool {`
  - Purpose: Indexed function `delete_enqueued` in `crates/ghook/src/planned_shutdown.rs`. [crates/ghook/src/planned_shutdown.rs:178-184]
- `write_marker` (function) component `write_marker [function]` (`b790b565-784f-5385-819b-858e1b4a29e2`) lines 195-198 [crates/ghook/src/planned_shutdown.rs:195-198]
  - Signature: `fn write_marker(home: &Path, name: &str, value: Value) {`
  - Purpose: Indexed function `write_marker` in `crates/ghook/src/planned_shutdown.rs`. [crates/ghook/src/planned_shutdown.rs:195-198]
- `stop_hook_matching_is_case_insensitive` (function) component `stop_hook_matching_is_case_insensitive [function]` (`d476cae5-ff6f-533a-89f8-0243ac580704`) lines 201-206 [crates/ghook/src/planned_shutdown.rs:201-206]
  - Signature: `fn stop_hook_matching_is_case_insensitive() {`
  - Purpose: Indexed function `stop_hook_matching_is_case_insensitive` in `crates/ghook/src/planned_shutdown.rs`. [crates/ghook/src/planned_shutdown.rs:201-206]
- `marker_accepts_fresh_allowed_intents` (function) component `marker_accepts_fresh_allowed_intents [function]` (`00c45c9b-0377-5f2c-b12f-360c8d9afc3b`) lines 209-219 [crates/ghook/src/planned_shutdown.rs:209-219]
  - Signature: `fn marker_accepts_fresh_allowed_intents() {`
  - Purpose: Indexed function `marker_accepts_fresh_allowed_intents` in `crates/ghook/src/planned_shutdown.rs`. [crates/ghook/src/planned_shutdown.rs:209-219]
- `marker_accepts_allowed_source_prefixes` (function) component `marker_accepts_allowed_source_prefixes [function]` (`d1dd9125-6864-56f1-8c1e-591cbfa00739`) lines 222-237 [crates/ghook/src/planned_shutdown.rs:222-237]
  - Signature: `fn marker_accepts_allowed_source_prefixes() {`
  - Purpose: Indexed function `marker_accepts_allowed_source_prefixes` in `crates/ghook/src/planned_shutdown.rs`. [crates/ghook/src/planned_shutdown.rs:222-237]
- `marker_rejects_stale_missing_invalid_and_disallowed_markers` (function) component `marker_rejects_stale_missing_invalid_and_disallowed_markers [function]` (`802d8af0-fd5f-5b8d-bf55-0390ca79e58a`) lines 240-282 [crates/ghook/src/planned_shutdown.rs:240-282]
  - Signature: `fn marker_rejects_stale_missing_invalid_and_disallowed_markers() {`
  - Purpose: Indexed function `marker_rejects_stale_missing_invalid_and_disallowed_markers` in `crates/ghook/src/planned_shutdown.rs`. [crates/ghook/src/planned_shutdown.rs:240-282]
- `env_freshness_override_uses_positive_parseable_values` (function) component `env_freshness_override_uses_positive_parseable_values [function]` (`ed9a3e23-bd1a-5304-a8c2-6f0f950b52b2`) lines 285-291 [crates/ghook/src/planned_shutdown.rs:285-291]
  - Signature: `fn env_freshness_override_uses_positive_parseable_values() {`
  - Purpose: Indexed function `env_freshness_override_uses_positive_parseable_values` in `crates/ghook/src/planned_shutdown.rs`. [crates/ghook/src/planned_shutdown.rs:285-291]
- `skip_dispatch_requires_stop_marker_and_unreachable_daemon` (function) component `skip_dispatch_requires_stop_marker_and_unreachable_daemon [function]` (`b577a8e8-f1b6-529d-8a11-72c75c04442b`) lines 294-304 [crates/ghook/src/planned_shutdown.rs:294-304]
  - Signature: `fn skip_dispatch_requires_stop_marker_and_unreachable_daemon() {`
  - Purpose: Indexed function `skip_dispatch_requires_stop_marker_and_unreachable_daemon` in `crates/ghook/src/planned_shutdown.rs`. [crates/ghook/src/planned_shutdown.rs:294-304]
- `daemon_probe_treats_http_responses_as_reachable` (function) component `daemon_probe_treats_http_responses_as_reachable [function]` (`2ae06111-955d-5553-ae00-03de7532c146`) lines 307-323 [crates/ghook/src/planned_shutdown.rs:307-323]
  - Signature: `fn daemon_probe_treats_http_responses_as_reachable() {`
  - Purpose: Indexed function `daemon_probe_treats_http_responses_as_reachable` in `crates/ghook/src/planned_shutdown.rs`. [crates/ghook/src/planned_shutdown.rs:307-323]
- `daemon_probe_treats_transport_failure_as_unreachable` (function) component `daemon_probe_treats_transport_failure_as_unreachable [function]` (`3e883e54-ca3d-5068-a0b0-6f68e377453f`) lines 326-328 [crates/ghook/src/planned_shutdown.rs:326-328]
  - Signature: `fn daemon_probe_treats_transport_failure_as_unreachable() {`
  - Purpose: Indexed function `daemon_probe_treats_transport_failure_as_unreachable` in `crates/ghook/src/planned_shutdown.rs`. [crates/ghook/src/planned_shutdown.rs:326-328]
- `post_enqueue_suppression_deletes_stop_envelope_for_connect_or_timeout` (function) component `post_enqueue_suppression_deletes_stop_envelope_for_connect_or_timeout [function]` (`f43f8514-eb6e-5720-bc7d-240d40a86ae2`) lines 331-353 [crates/ghook/src/planned_shutdown.rs:331-353]
  - Signature: `fn post_enqueue_suppression_deletes_stop_envelope_for_connect_or_timeout() {`
  - Purpose: Indexed function `post_enqueue_suppression_deletes_stop_envelope_for_connect_or_timeout` in `crates/ghook/src/planned_shutdown.rs`. [crates/ghook/src/planned_shutdown.rs:331-353]
- `post_enqueue_suppression_accepts_already_deleted_envelope` (function) component `post_enqueue_suppression_accepts_already_deleted_envelope [function]` (`a6e7ff0c-3d6c-5139-9be1-d9e3b7673cdc`) lines 356-366 [crates/ghook/src/planned_shutdown.rs:356-366]
  - Signature: `fn post_enqueue_suppression_accepts_already_deleted_envelope() {`
  - Purpose: Indexed function `post_enqueue_suppression_accepts_already_deleted_envelope` in `crates/ghook/src/planned_shutdown.rs`. [crates/ghook/src/planned_shutdown.rs:356-366]
- `post_enqueue_suppression_rejects_http_non_stop_and_stale_marker` (function) component `post_enqueue_suppression_rejects_http_non_stop_and_stale_marker [function]` (`c17e17be-8228-5d89-99cf-f00b69e83031`) lines 369-399 [crates/ghook/src/planned_shutdown.rs:369-399]
  - Signature: `fn post_enqueue_suppression_rejects_http_non_stop_and_stale_marker() {`
  - Purpose: Indexed function `post_enqueue_suppression_rejects_http_non_stop_and_stale_marker` in `crates/ghook/src/planned_shutdown.rs`. [crates/ghook/src/planned_shutdown.rs:369-399]
- `post_enqueue_suppression_rejects_delete_failure` (function) component `post_enqueue_suppression_rejects_delete_failure [function]` (`3f702f5f-5ce6-5a7b-b47b-8ed9c339a049`) lines 402-408 [crates/ghook/src/planned_shutdown.rs:402-408]
  - Signature: `fn post_enqueue_suppression_rejects_delete_failure() {`
  - Purpose: Indexed function `post_enqueue_suppression_rejects_delete_failure` in `crates/ghook/src/planned_shutdown.rs`. [crates/ghook/src/planned_shutdown.rs:402-408]

