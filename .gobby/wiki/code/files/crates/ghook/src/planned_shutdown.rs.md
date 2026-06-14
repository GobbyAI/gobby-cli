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

This file implements planned shutdown handling for Gobby’s Stop hooks. It detects short-lived shutdown markers in the Gobby home directory, checks whether they are fresh and allowed, probes daemon reachability, and uses that combination to decide when a Stop hook should skip dispatch or suppress a failed post. The helper functions work together to parse and validate marker JSON, derive the freshness window from an environment override, read the current time, probe `/api/admin/health`, and delete enqueued items when suppression is warranted. The tests cover stop-hook matching, marker validation rules, daemon probing behavior, environment parsing, and the suppression/skip decision paths.
[crates/ghook/src/planned_shutdown.rs:21-27]
[crates/ghook/src/planned_shutdown.rs:29-37]
[crates/ghook/src/planned_shutdown.rs:39-50]
[crates/ghook/src/planned_shutdown.rs:52-54]
[crates/ghook/src/planned_shutdown.rs:56-62]

## API Symbols

- `should_skip_dispatch` (function) component `should_skip_dispatch [function]` (`e42c0c01-e1ab-56b4-87ca-42cd184ae834`) lines 21-27 [crates/ghook/src/planned_shutdown.rs:21-27]
  - Signature: `pub fn should_skip_dispatch(hook_type: &str) -> bool {`
  - Purpose: Returns the result of 'should_skip_dispatch_with', using a fresh shutdown marker in 'marker_home()' as the skip condition and daemon reachability at 'gobby_core::daemon_url::daemon_url()' as the dispatch check. [crates/ghook/src/planned_shutdown.rs:21-27]
- `suppress_after_failed_post` (function) component `suppress_after_failed_post [function]` (`480a97fa-f382-56de-81d6-231456e02757`) lines 29-37 [crates/ghook/src/planned_shutdown.rs:29-37]
  - Signature: `pub fn suppress_after_failed_post(`
  - Purpose: Returns a boolean by delegating to 'suppress_after_failed_post_with_marker', using the hook type, optional delivery failure kind, and enqueued path, with suppression driven by whether a fresh shutdown marker exists under 'marker_home()'. [crates/ghook/src/planned_shutdown.rs:29-37]
- `suppress_after_failed_post_with_marker` (function) component `suppress_after_failed_post_with_marker [function]` (`915605ab-403f-5ea7-919f-0d8b79d6bfdc`) lines 39-50 [crates/ghook/src/planned_shutdown.rs:39-50]
  - Signature: `fn suppress_after_failed_post_with_marker(`
  - Purpose: Returns 'false' unless 'should_suppress_failed_post' says to suppress the failed post for the given hook, failure kind, and marker state, in which case it deletes the enqueued item at 'enqueued_path' and returns that deletion result. [crates/ghook/src/planned_shutdown.rs:39-50]
- `is_stop_hook` (function) component `is_stop_hook [function]` (`8ede0f52-e4f0-5d0b-b223-36bd5ea11bb2`) lines 52-54 [crates/ghook/src/planned_shutdown.rs:52-54]
  - Signature: `pub fn is_stop_hook(hook_type: &str) -> bool {`
  - Purpose: Returns 'true' when 'hook_type' matches '"stop"' case-insensitively, and 'false' otherwise. [crates/ghook/src/planned_shutdown.rs:52-54]
- `should_skip_dispatch_with` (function) component `should_skip_dispatch_with [function]` (`f74d3a29-061a-5f08-a9ba-0d9e26b44077`) lines 56-62 [crates/ghook/src/planned_shutdown.rs:56-62]
  - Signature: `fn should_skip_dispatch_with(`
  - Purpose: Returns 'true' only for stop hooks when the marker is active and the daemon is unreachable, otherwise 'false'. [crates/ghook/src/planned_shutdown.rs:56-62]
- `should_suppress_failed_post` (function) component `should_suppress_failed_post [function]` (`85b48489-0263-565e-bf19-5a18845e3c2d`) lines 64-75 [crates/ghook/src/planned_shutdown.rs:64-75]
  - Signature: `fn should_suppress_failed_post(`
  - Purpose: Returns 'true' only when the hook is a stop hook, the delivery failure is either 'Connect' or 'Timeout', and the provided marker predicate evaluates to 'true'; otherwise it returns 'false'. [crates/ghook/src/planned_shutdown.rs:64-75]
- `fresh_shutdown_marker` (function) component `fresh_shutdown_marker [function]` (`fd6c5466-4319-59b8-b435-fd161c8b2405`) lines 77-79 [crates/ghook/src/planned_shutdown.rs:77-79]
  - Signature: `fn fresh_shutdown_marker(home: &Path) -> bool {`
  - Purpose: Returns whether the shutdown marker is fresh for the given 'home' directory by delegating to 'fresh_shutdown_marker_at(home, now_secs(), allow_seconds())'. [crates/ghook/src/planned_shutdown.rs:77-79]
- `fresh_shutdown_marker_at` (function) component `fresh_shutdown_marker_at [function]` (`ccb6214b-2a4e-5530-8a2b-9302a356ea6f`) lines 81-84 [crates/ghook/src/planned_shutdown.rs:81-84]
  - Signature: `fn fresh_shutdown_marker_at(home: &Path, now: f64, allow_seconds: f64) -> bool {`
  - Purpose: Returns 'true' if 'home/ACTIVE_MARKER' exists and its contents satisfy 'marker_is_allowed_and_fresh' for the given 'now' and 'allow_seconds', otherwise 'false'. [crates/ghook/src/planned_shutdown.rs:81-84]
- `marker_is_allowed_and_fresh` (function) component `marker_is_allowed_and_fresh [function]` (`b3c3b5d5-6d52-5c9e-91f7-aa4dfaa3b406`) lines 86-113 [crates/ghook/src/planned_shutdown.rs:86-113]
  - Signature: `fn marker_is_allowed_and_fresh(marker: &Value, now: f64, allow_seconds: f64) -> bool {`
  - Purpose: Returns 'true' only when 'marker' contains a valid 'timestamp' not in the future and within 'allow_seconds' of 'now', and either its 'intent' is 'stop' or 'restart' or its lowercase 'source' starts with one of 'ALLOWED_SOURCES'; otherwise it returns 'false'. [crates/ghook/src/planned_shutdown.rs:86-113]
- `read_marker` (function) component `read_marker [function]` (`05688997-63c0-5bf0-9083-978328be448d`) lines 115-119 [crates/ghook/src/planned_shutdown.rs:115-119]
  - Signature: `fn read_marker(path: &Path) -> Option<Value> {`
  - Purpose: Reads the file at 'path', parses it as JSON, and returns the 'Value' only if parsing succeeds and the top-level JSON value is an object; otherwise it returns 'None'. [crates/ghook/src/planned_shutdown.rs:115-119]
- `daemon_is_reachable` (function) component `daemon_is_reachable [function]` (`7a9b0033-3751-5d7e-9d9e-5665b2b2f174`) lines 121-130 [crates/ghook/src/planned_shutdown.rs:121-130]
  - Signature: `fn daemon_is_reachable(daemon_url: &str) -> bool {`
  - Purpose: Builds the daemon health-check URL by appending 'HEALTH_ENDPOINT' to 'daemon_url' without a trailing slash, performs a GET with 'HEALTH_TIMEOUT', and returns 'true' for any HTTP response status or non-transport 'ureq' error, but 'false' only on transport failures after logging a debug message. [crates/ghook/src/planned_shutdown.rs:121-130]
- `marker_home` (function) component `marker_home [function]` (`fea7a275-648e-59e3-a686-39b888fc347c`) lines 132-134 [crates/ghook/src/planned_shutdown.rs:132-134]
  - Signature: `fn marker_home() -> Option<PathBuf> {`
  - Purpose: Returns the Gobby home directory as an optional 'PathBuf' by calling 'gobby_core::gobby_home()' and discarding any error with '.ok()'. [crates/ghook/src/planned_shutdown.rs:132-134]
- `allow_seconds` (function) component `allow_seconds [function]` (`933ab78d-939e-52d0-983c-8e96010de45e`) lines 136-142 [crates/ghook/src/planned_shutdown.rs:136-142]
  - Signature: `fn allow_seconds() -> f64 {`
  - Purpose: Returns the shutdown-hook allow time in seconds as an 'f64' by reading the 'GOBBY_SHUTDOWN_HOOK_ALLOW_SECONDS' environment variable and passing its optional string value to 'allow_seconds_from_env'. [crates/ghook/src/planned_shutdown.rs:136-142]
- `allow_seconds_from_env` (function) component `allow_seconds_from_env [function]` (`fbf08e40-b0bd-5487-8b9d-5305c01947b5`) lines 144-152 [crates/ghook/src/planned_shutdown.rs:144-152]
  - Signature: `fn allow_seconds_from_env(value: Option<&str>) -> f64 {`
  - Purpose: Returns the parsed positive finite 'f64' from the optional environment string, or 'DEFAULT_ALLOW_SECONDS' if the value is absent, invalid, non-finite, or non-positive. [crates/ghook/src/planned_shutdown.rs:144-152]
- `optional_float` (function) component `optional_float [function]` (`76bb012b-1464-5bec-b7e2-edf391fe3245`) lines 154-160 [crates/ghook/src/planned_shutdown.rs:154-160]
  - Signature: `fn optional_float(value: &Value) -> Option<f64> {`
  - Purpose: Returns 'Some(f64)' when the input 'Value' is a JSON number convertible to 'f64' or a string that parses as 'f64', and 'None' for all other variants or parse failures. [crates/ghook/src/planned_shutdown.rs:154-160]
- `value_as_text` (function) component `value_as_text [function]` (`aa1adcdc-a165-5be2-9dbb-a77535328a6a`) lines 162-169 [crates/ghook/src/planned_shutdown.rs:162-169]
  - Signature: `fn value_as_text(value: &Value) -> Option<String> {`
  - Purpose: Converts a 'serde_json::Value' to 'Some(String)' when it is a string, number, or boolean by cloning or formatting the primitive, and returns 'None' for all other variants. [crates/ghook/src/planned_shutdown.rs:162-169]
- `now_secs` (function) component `now_secs [function]` (`4c480cc4-6019-53b3-94ee-887000152de5`) lines 171-176 [crates/ghook/src/planned_shutdown.rs:171-176]
  - Signature: `fn now_secs() -> f64 {`
  - Purpose: Returns the current Unix epoch time as an 'f64' in seconds, or '0.0' if the system clock is earlier than 'UNIX_EPOCH'. [crates/ghook/src/planned_shutdown.rs:171-176]
- `delete_enqueued` (function) component `delete_enqueued [function]` (`34768c55-e686-5b08-adf7-aff1710edf15`) lines 178-184 [crates/ghook/src/planned_shutdown.rs:178-184]
  - Signature: `fn delete_enqueued(enqueued_path: &Path) -> bool {`
  - Purpose: Deletes the file at 'enqueued_path' and returns 'true' if removal succeeds or the file is already missing, otherwise returns 'false' on any other I/O error. [crates/ghook/src/planned_shutdown.rs:178-184]
- `write_marker` (function) component `write_marker [function]` (`b790b565-784f-5385-819b-858e1b4a29e2`) lines 195-198 [crates/ghook/src/planned_shutdown.rs:195-198]
  - Signature: `fn write_marker(home: &Path, name: &str, value: Value) {`
  - Purpose: Creates the 'home' directory if needed, then serializes 'value' to JSON bytes and writes it to the file 'home.join(name)', panicking on any I/O or serialization error. [crates/ghook/src/planned_shutdown.rs:195-198]
- `stop_hook_matching_is_case_insensitive` (function) component `stop_hook_matching_is_case_insensitive [function]` (`d476cae5-ff6f-533a-89f8-0243ac580704`) lines 201-206 [crates/ghook/src/planned_shutdown.rs:201-206]
  - Signature: `fn stop_hook_matching_is_case_insensitive() {`
  - Purpose: Verifies that 'is_stop_hook' matches the stop hook name case-insensitively for 'stop' variants and rejects non-matching strings like 'SubagentStop'. [crates/ghook/src/planned_shutdown.rs:201-206]
- `marker_accepts_fresh_allowed_intents` (function) component `marker_accepts_fresh_allowed_intents [function]` (`00c45c9b-0377-5f2c-b12f-360c8d9afc3b`) lines 209-219 [crates/ghook/src/planned_shutdown.rs:209-219]
  - Signature: `fn marker_accepts_fresh_allowed_intents() {`
  - Purpose: Verifies that a shutdown marker with an unknown source but a fresh allowed intent ('restart') is accepted as fresh when its timestamp is within the freshness window. [crates/ghook/src/planned_shutdown.rs:209-219]
- `marker_accepts_allowed_source_prefixes` (function) component `marker_accepts_allowed_source_prefixes [function]` (`d1dd9125-6864-56f1-8c1e-591cbfa00739`) lines 222-237 [crates/ghook/src/planned_shutdown.rs:222-237]
  - Signature: `fn marker_accepts_allowed_source_prefixes() {`
  - Purpose: Verifies that 'fresh_shutdown_marker_at' treats active markers written with any allowed 'source' prefix ('cli_stop', 'http_shutdown', 'service_restart', 'mcp_stop') as valid when their timestamp is within the freshness window. [crates/ghook/src/planned_shutdown.rs:222-237]
- `marker_rejects_stale_missing_invalid_and_disallowed_markers` (function) component `marker_rejects_stale_missing_invalid_and_disallowed_markers [function]` (`802d8af0-fd5f-5b8d-bf55-0390ca79e58a`) lines 240-282 [crates/ghook/src/planned_shutdown.rs:240-282]
  - Signature: `fn marker_rejects_stale_missing_invalid_and_disallowed_markers() {`
  - Purpose: Verifies that 'fresh_shutdown_marker_at' returns 'false' for shutdown markers that are stale, future-dated, missing a timestamp, contain invalid JSON, or use a disallowed source/intent. [crates/ghook/src/planned_shutdown.rs:240-282]
- `env_freshness_override_uses_positive_parseable_values` (function) component `env_freshness_override_uses_positive_parseable_values [function]` (`ed9a3e23-bd1a-5304-a8c2-6f0f950b52b2`) lines 285-291 [crates/ghook/src/planned_shutdown.rs:285-291]
  - Signature: `fn env_freshness_override_uses_positive_parseable_values() {`
  - Purpose: Verifies that 'allow_seconds_from_env' returns 'DEFAULT_ALLOW_SECONDS' when unset, zero, negative, or non-numeric, and accepts a positive parseable value like '2.5'. [crates/ghook/src/planned_shutdown.rs:285-291]
- `skip_dispatch_requires_stop_marker_and_unreachable_daemon` (function) component `skip_dispatch_requires_stop_marker_and_unreachable_daemon [function]` (`b577a8e8-f1b6-529d-8a11-72c75c04442b`) lines 294-304 [crates/ghook/src/planned_shutdown.rs:294-304]
  - Signature: `fn skip_dispatch_requires_stop_marker_and_unreachable_daemon() {`
  - Purpose: Verifies that 'should_skip_dispatch_with' returns true only for a case-insensitive '"Stop"' marker when the daemon is unreachable, and does not invoke the daemon probe or skip dispatch for non-'Stop' markers or when the daemon is reachable. [crates/ghook/src/planned_shutdown.rs:294-304]
- `daemon_probe_treats_http_responses_as_reachable` (function) component `daemon_probe_treats_http_responses_as_reachable [function]` (`2ae06111-955d-5553-ae00-03de7532c146`) lines 307-323 [crates/ghook/src/planned_shutdown.rs:307-323]
  - Signature: `fn daemon_probe_treats_http_responses_as_reachable() {`
  - Purpose: Verifies that 'daemon_is_reachable' treats any successful HTTP response from 'GET /api/admin/health' as reachable, even when the server returns '503 Service Unavailable'. [crates/ghook/src/planned_shutdown.rs:307-323]
- `daemon_probe_treats_transport_failure_as_unreachable` (function) component `daemon_probe_treats_transport_failure_as_unreachable [function]` (`3e883e54-ca3d-5068-a0b0-6f68e377453f`) lines 326-328 [crates/ghook/src/planned_shutdown.rs:326-328]
  - Signature: `fn daemon_probe_treats_transport_failure_as_unreachable() {`
  - Purpose: Verifies that 'daemon_is_reachable("file:///tmp/not-a-daemon")' returns 'false' when the probe encounters a transport-level failure. [crates/ghook/src/planned_shutdown.rs:326-328]
- `post_enqueue_suppression_deletes_stop_envelope_for_connect_or_timeout` (function) component `post_enqueue_suppression_deletes_stop_envelope_for_connect_or_timeout [function]` (`f43f8514-eb6e-5720-bc7d-240d40a86ae2`) lines 331-353 [crates/ghook/src/planned_shutdown.rs:331-353]
  - Signature: `fn post_enqueue_suppression_deletes_stop_envelope_for_connect_or_timeout() {`
  - Purpose: Verifies that 'suppress_after_failed_post_with_marker' deletes the marker file and returns 'true' when the envelope text is 'Stop'/'STOP' and the delivery failure kind is 'Connect' or 'Timeout'. [crates/ghook/src/planned_shutdown.rs:331-353]
- `post_enqueue_suppression_accepts_already_deleted_envelope` (function) component `post_enqueue_suppression_accepts_already_deleted_envelope [function]` (`a6e7ff0c-3d6c-5139-9be1-d9e3b7673cdc`) lines 356-366 [crates/ghook/src/planned_shutdown.rs:356-366]
  - Signature: `fn post_enqueue_suppression_accepts_already_deleted_envelope() {`
  - Purpose: Verifies that 'suppress_after_failed_post_with_marker' returns 'true' when a post-enqueue failure for a 'Connect' delivery error targets an already missing marker file path. [crates/ghook/src/planned_shutdown.rs:356-366]
- `post_enqueue_suppression_rejects_http_non_stop_and_stale_marker` (function) component `post_enqueue_suppression_rejects_http_non_stop_and_stale_marker [function]` (`c17e17be-8228-5d89-99cf-f00b69e83031`) lines 369-399 [crates/ghook/src/planned_shutdown.rs:369-399]
  - Signature: `fn post_enqueue_suppression_rejects_http_non_stop_and_stale_marker() {`
  - Purpose: Verifies that 'suppress_after_failed_post_with_marker' does not suppress and preserves the marker files for 'Stop' with 'Http', 'PreToolUse' with 'Connect', and 'Stop' with 'Connect' when the marker is stale. [crates/ghook/src/planned_shutdown.rs:369-399]
- `post_enqueue_suppression_rejects_delete_failure` (function) component `post_enqueue_suppression_rejects_delete_failure [function]` (`3f702f5f-5ce6-5a7b-b47b-8ed9c339a049`) lines 402-408 [crates/ghook/src/planned_shutdown.rs:402-408]
  - Signature: `fn post_enqueue_suppression_rejects_delete_failure() {`
  - Purpose: Verifies that 'delete_enqueued(&path)' returns 'false' when the target path is a directory rather than a file. [crates/ghook/src/planned_shutdown.rs:402-408]

