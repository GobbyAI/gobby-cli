---
title: crates/ghook/src/planned_shutdown.rs
type: code_file
provenance:
- file: crates/ghook/src/planned_shutdown.rs
  ranges:
  - 21-27
  - 29-37
  - 39-50
  - 52-56
  - 58-63
  - 65-67
  - 69-75
  - 77-88
  - 90-92
  - 94-97
  - 99-126
  - 128-132
  - 134-143
  - 145-153
  - 155-161
  - 163-171
  - 173-179
  - 181-188
  - 190-195
  - 197-203
  - 214-217
  - 220-225
  - 228-238
  - 241-256
  - 259-301
  - 304-310
  - 313-328
  - 331-341
  - 344-360
  - 363-365
  - 368-390
  - 393-403
  - 406-436
  - 439-445
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/ghook/src/planned_shutdown.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Purpose

`crates/ghook/src/planned_shutdown.rs` exposes 34 indexed API symbols.
[crates/ghook/src/planned_shutdown.rs:21-27]
[crates/ghook/src/planned_shutdown.rs:29-37]
[crates/ghook/src/planned_shutdown.rs:39-50]
[crates/ghook/src/planned_shutdown.rs:52-56]
[crates/ghook/src/planned_shutdown.rs:58-63]

## API Symbols

- `should_skip_dispatch` (function) component `should_skip_dispatch [function]` (`e42c0c01-e1ab-56b4-87ca-42cd184ae834`) lines 21-27 [crates/ghook/src/planned_shutdown.rs:21-27]
  - Signature: `pub fn should_skip_dispatch(hook_type: &str) -> bool {`
  - Purpose: This function determines whether to skip hook dispatch by delegating to `should_skip_dispatch_with`, checking for a fresh shutdown marker in the marker home directory and the daemon's reachability. [crates/ghook/src/planned_shutdown.rs:21-27]
- `suppress_after_failed_post` (function) component `suppress_after_failed_post [function]` (`d541982c-6ef2-56ed-b584-df8bb74dd5a1`) lines 29-37 [crates/ghook/src/planned_shutdown.rs:29-37]
  - Signature: `pub fn suppress_after_failed_post(`
  - Purpose: Determines whether to suppress post-delivery failure handling for a given hook type by delegating to `suppress_after_failed_post_with_marker` with a closure that checks for the presence of a fresh shutdown marker in the home directory. [crates/ghook/src/planned_shutdown.rs:29-37]
- `suppress_after_failed_post_with_marker` (function) component `suppress_after_failed_post_with_marker [function]` (`bac9852f-aa0b-5b74-89e7-c73228eb2ae4`) lines 39-50 [crates/ghook/src/planned_shutdown.rs:39-50]
  - Signature: `fn suppress_after_failed_post_with_marker(`
  - Purpose: Suppresses a failed post delivery by deleting the enqueued item if suppression criteria are met based on the hook type, failure kind, and marker condition. [crates/ghook/src/planned_shutdown.rs:39-50]
- `daemon_url` (function) component `daemon_url [function]` (`2b905a18-67ff-557f-82e8-63ba7d88d93d`) lines 52-56 [crates/ghook/src/planned_shutdown.rs:52-56]
  - Signature: `pub fn daemon_url() -> String {`
  - Purpose: Returns a daemon URL string sourced from the `GOBBY_DAEMON_URL` environment variable, falling back to `gobby_core::daemon_url::daemon_url()` if the variable is unset. [crates/ghook/src/planned_shutdown.rs:52-56]
- `daemon_url_from_env` (function) component `daemon_url_from_env [function]` (`3827b39c-3cbf-5927-87f0-148c3420e136`) lines 58-63 [crates/ghook/src/planned_shutdown.rs:58-63]
  - Signature: `fn daemon_url_from_env(value: Option<&str>, fallback: impl FnOnce() -> String) -> String {`
  - Purpose: Returns the provided string value if present and non-empty; otherwise invokes and returns the result of the fallback closure. [crates/ghook/src/planned_shutdown.rs:58-63]
- `is_stop_hook` (function) component `is_stop_hook [function]` (`72a4f88b-5c0e-50d6-8329-951cb386f035`) lines 65-67 [crates/ghook/src/planned_shutdown.rs:65-67]
  - Signature: `pub fn is_stop_hook(hook_type: &str) -> bool {`
  - Purpose: Returns a boolean indicating whether the provided hook type string equals "stop" using case-insensitive ASCII comparison. [crates/ghook/src/planned_shutdown.rs:65-67]
- `should_skip_dispatch_with` (function) component `should_skip_dispatch_with [function]` (`19ce34aa-ebab-52d6-9269-cf71840f9cc0`) lines 69-75 [crates/ghook/src/planned_shutdown.rs:69-75]
  - Signature: `fn should_skip_dispatch_with(`
  - Purpose: Returns `true` when the hook type is a stop hook with an active marker and the daemon is unreachable, indicating dispatch should be skipped. [crates/ghook/src/planned_shutdown.rs:69-75]
- `should_suppress_failed_post` (function) component `should_suppress_failed_post [function]` (`b13c2607-d734-59a0-a3e0-c2bb5a614908`) lines 77-88 [crates/ghook/src/planned_shutdown.rs:77-88]
  - Signature: `fn should_suppress_failed_post(`
  - Purpose: Suppresses a failed post delivery when the hook type is a stop hook, the failure is a connection or timeout error, and an active marker condition is satisfied. [crates/ghook/src/planned_shutdown.rs:77-88]
- `fresh_shutdown_marker` (function) component `fresh_shutdown_marker [function]` (`ed0d7e53-8e8b-5d63-8fe8-6b00ed2cda4c`) lines 90-92 [crates/ghook/src/planned_shutdown.rs:90-92]
  - Signature: `fn fresh_shutdown_marker(home: &Path) -> bool {`
  - Purpose: This function checks whether a fresh shutdown marker exists at the specified home directory path by delegating to `fresh_shutdown_marker_at` with the current Unix timestamp and a configured grace period. [crates/ghook/src/planned_shutdown.rs:90-92]
- `fresh_shutdown_marker_at` (function) component `fresh_shutdown_marker_at [function]` (`645cffad-4fb0-5bb7-9f67-682094a0bcb3`) lines 94-97 [crates/ghook/src/planned_shutdown.rs:94-97]
  - Signature: `fn fresh_shutdown_marker_at(home: &Path, now: f64, allow_seconds: f64) -> bool {`
  - Purpose: Returns true if an active shutdown marker file exists in the home directory and is both fresh and allowed within the specified time interval from the current timestamp. [crates/ghook/src/planned_shutdown.rs:94-97]
- `marker_is_allowed_and_fresh` (function) component `marker_is_allowed_and_fresh [function]` (`fdae92cd-6617-5035-8b64-a39633b6f82b`) lines 99-126 [crates/ghook/src/planned_shutdown.rs:99-126]
  - Signature: `fn marker_is_allowed_and_fresh(marker: &Value, now: f64, allow_seconds: f64) -> bool {`
  - Purpose: Validates that a marker has a fresh timestamp (within `allow_seconds` of `now`) and either has intent "stop"/"restart" or originates from an allowed source prefix. [crates/ghook/src/planned_shutdown.rs:99-126]
- `read_marker` (function) component `read_marker [function]` (`6d9b49fb-d93c-5fb3-b15a-eb82046eb984`) lines 128-132 [crates/ghook/src/planned_shutdown.rs:128-132]
  - Signature: `fn read_marker(path: &Path) -> Option<Value> {`
  - Purpose: Reads a file from the given path, deserializes it as JSON, and returns the parsed value only if it's a JSON object, otherwise `None`. [crates/ghook/src/planned_shutdown.rs:128-132]
- `daemon_is_reachable` (function) component `daemon_is_reachable [function]` (`dc459c52-db04-520e-8a7c-033dd68fb39b`) lines 134-143 [crates/ghook/src/planned_shutdown.rs:134-143]
  - Signature: `fn daemon_is_reachable(daemon_url: &str) -> bool {`
  - Purpose: Determines daemon reachability by issuing a GET request to its health endpoint and returning true if a response is received (success or HTTP status code) or false on transport errors. [crates/ghook/src/planned_shutdown.rs:134-143]
- `marker_home` (function) component `marker_home [function]` (`30fc2555-a324-5ad7-a6cd-073de8005d59`) lines 145-153 [crates/ghook/src/planned_shutdown.rs:145-153]
  - Signature: `fn marker_home() -> Option<PathBuf> {`
  - Purpose: Resolves the Gobby home directory path by checking the `GOBBY_HOME` environment variable first, falling back to `~/.gobby` if unset or empty, and returning `None` only if the home directory cannot be determined. [crates/ghook/src/planned_shutdown.rs:145-153]
- `allow_seconds` (function) component `allow_seconds [function]` (`75e46e71-1e00-5214-9cf5-282c2ffb2783`) lines 155-161 [crates/ghook/src/planned_shutdown.rs:155-161]
  - Signature: `fn allow_seconds() -> f64 {`
  - Purpose: Delegates the `GOBBY_SHUTDOWN_HOOK_ALLOW_SECONDS` environment variable to `allow_seconds_from_env` for parsing and returns the resulting `f64` timeout value. [crates/ghook/src/planned_shutdown.rs:155-161]
- `allow_seconds_from_env` (function) component `allow_seconds_from_env [function]` (`95d30a44-53bb-57e5-aed0-9e697ecc1166`) lines 163-171 [crates/ghook/src/planned_shutdown.rs:163-171]
  - Signature: `fn allow_seconds_from_env(value: Option<&str>) -> f64 {`
  - Purpose: Parses an optional string into a positive finite f64 seconds value, defaulting to DEFAULT_ALLOW_SECONDS if parsing fails or the result is non-positive or non-finite. [crates/ghook/src/planned_shutdown.rs:163-171]
- `optional_float` (function) component `optional_float [function]` (`18cc0f42-0eca-56e4-99fb-a04df18dcd71`) lines 173-179 [crates/ghook/src/planned_shutdown.rs:173-179]
  - Signature: `fn optional_float(value: &Value) -> Option<f64> {`
  - Purpose: Converts a `Value` enum variant to `Option<f64>` by extracting numeric values directly or parsing string representations, returning `None` for unsupported types. [crates/ghook/src/planned_shutdown.rs:173-179]
- `value_as_text` (function) component `value_as_text [function]` (`775d79fa-4724-52c1-b5af-c91a715d231e`) lines 181-188 [crates/ghook/src/planned_shutdown.rs:181-188]
  - Signature: `fn value_as_text(value: &Value) -> Option<String> {`
  - Purpose: Converts a Value enum to an Option<String> by stringifying String, Number, and Bool variants, returning None for all other variant types. [crates/ghook/src/planned_shutdown.rs:181-188]
- `now_secs` (function) component `now_secs [function]` (`67b324d0-657a-5bb8-b348-38eeab4501ec`) lines 190-195 [crates/ghook/src/planned_shutdown.rs:190-195]
  - Signature: `fn now_secs() -> f64 {`
  - Purpose: Returns the current Unix timestamp as a floating-point number representing seconds elapsed since the Unix epoch, or 0.0 if the system clock is unavailable. [crates/ghook/src/planned_shutdown.rs:190-195]
- `delete_enqueued` (function) component `delete_enqueued [function]` (`a2669e91-e8ba-5cb1-bbf6-9c154007fb4a`) lines 197-203 [crates/ghook/src/planned_shutdown.rs:197-203]
  - Signature: `fn delete_enqueued(enqueued_path: &Path) -> bool {`
  - Purpose: Removes the file at the given path and returns `true` if successful or the file doesn't exist, `false` on any other I/O error. [crates/ghook/src/planned_shutdown.rs:197-203]
- `write_marker` (function) component `write_marker [function]` (`5d7d6430-4f84-58f4-8d70-13674ca7526d`) lines 214-217 [crates/ghook/src/planned_shutdown.rs:214-217]
  - Signature: `fn write_marker(home: &Path, name: &str, value: Value) {`
  - Purpose: Recursively creates the directory at `home` and writes the JSON-serialized `value` to a file named `name` within it. [crates/ghook/src/planned_shutdown.rs:214-217]
- `stop_hook_matching_is_case_insensitive` (function) component `stop_hook_matching_is_case_insensitive [function]` (`733a2a04-d346-5365-86f6-171ac7396983`) lines 220-225 [crates/ghook/src/planned_shutdown.rs:220-225]
  - Signature: `fn stop_hook_matching_is_case_insensitive() {`
  - Purpose: A unit test verifying that `is_stop_hook()` performs case-insensitive matching on the exact string "stop" while rejecting partial matches containing "stop" as a substring. [crates/ghook/src/planned_shutdown.rs:220-225]
- `marker_accepts_fresh_allowed_intents` (function) component `marker_accepts_fresh_allowed_intents [function]` (`f003c293-a9d0-5d06-94f4-83dc6e772fa8`) lines 228-238 [crates/ghook/src/planned_shutdown.rs:228-238]
  - Signature: `fn marker_accepts_fresh_allowed_intents() {`
  - Purpose: This test asserts that `fresh_shutdown_marker_at` returns true for a shutdown marker with intent "restart" timestamped 10 seconds in the past, verifying it falls within the 120-second freshness threshold. [crates/ghook/src/planned_shutdown.rs:228-238]
- `marker_accepts_allowed_source_prefixes` (function) component `marker_accepts_allowed_source_prefixes [function]` (`1e5814c8-dc8c-5c92-b42c-d9dc9cd4701a`) lines 241-256 [crates/ghook/src/planned_shutdown.rs:241-256]
  - Signature: `fn marker_accepts_allowed_source_prefixes() {`
  - Purpose: Test that verifies `fresh_shutdown_marker_at` returns true for shutdown markers with any of four allowed source prefixes (cli_stop, http_shutdown, service_restart, mcp_stop) when the marker is within the freshness threshold. [crates/ghook/src/planned_shutdown.rs:241-256]
- `marker_rejects_stale_missing_invalid_and_disallowed_markers` (function) component `marker_rejects_stale_missing_invalid_and_disallowed_markers [function]` (`7e132ff3-7d41-5018-a8be-7fe6bb4e25cf`) lines 259-301 [crates/ghook/src/planned_shutdown.rs:259-301]
  - Signature: `fn marker_rejects_stale_missing_invalid_and_disallowed_markers() {`
  - Purpose: # Summary

This test validates that `fresh_shutdown_marker_at` correctly rejects shutdown marker files that exceed the time-to-live threshold, are future-dated, lack required fields, contain invalid JSON, or specify disallowed source/intent combinations. [crates/ghook/src/planned_shutdown.rs:259-301]
- `env_freshness_override_uses_positive_parseable_values` (function) component `env_freshness_override_uses_positive_parseable_values [function]` (`c0e83281-e423-5bac-adbc-ae250d922082`) lines 304-310 [crates/ghook/src/planned_shutdown.rs:304-310]
  - Signature: `fn env_freshness_override_uses_positive_parseable_values() {`
  - Purpose: This test validates that `allow_seconds_from_env` parses positive floating-point values from optional environment variable strings and falls back to DEFAULT_ALLOW_SECONDS for None, zero, negative, or unparseable inputs. [crates/ghook/src/planned_shutdown.rs:304-310]
- `daemon_url_prefers_non_empty_env_override` (function) component `daemon_url_prefers_non_empty_env_override [function]` (`366e42af-980f-5b67-b281-13355ffcd4e0`) lines 313-328 [crates/ghook/src/planned_shutdown.rs:313-328]
  - Signature: `fn daemon_url_prefers_non_empty_env_override() {`
  - Purpose: Verifies that `daemon_url_from_env` returns the environment-provided URL only if non-empty; otherwise, it delegates to a fallback function. [crates/ghook/src/planned_shutdown.rs:313-328]
- `skip_dispatch_requires_stop_marker_and_unreachable_daemon` (function) component `skip_dispatch_requires_stop_marker_and_unreachable_daemon [function]` (`6d2e8e43-9e71-511d-a45f-eb4a5ada2e25`) lines 331-341 [crates/ghook/src/planned_shutdown.rs:331-341]
  - Signature: `fn skip_dispatch_requires_stop_marker_and_unreachable_daemon() {`
  - Purpose: This test function verifies that dispatch skipping is triggered only when a "Stop" marker is present AND the daemon is unreachable (second closure returns false), and that reachable daemons or non-Stop messages prevent skipping. [crates/ghook/src/planned_shutdown.rs:331-341]
- `daemon_probe_treats_http_responses_as_reachable` (function) component `daemon_probe_treats_http_responses_as_reachable [function]` (`0ca341ce-ab00-5703-9dcd-1fc994600bc1`) lines 344-360 [crates/ghook/src/planned_shutdown.rs:344-360]
  - Signature: `fn daemon_probe_treats_http_responses_as_reachable() {`
  - Purpose: This function is a unit test that verifies `daemon_is_reachable()` treats HTTP responses—including non-2xx status codes like 503—as indicators of daemon reachability on the `/api/admin/health` endpoint. [crates/ghook/src/planned_shutdown.rs:344-360]
- `daemon_probe_treats_transport_failure_as_unreachable` (function) component `daemon_probe_treats_transport_failure_as_unreachable [function]` (`449a9c3e-0594-53f7-b3df-7be89b810128`) lines 363-365 [crates/ghook/src/planned_shutdown.rs:363-365]
  - Signature: `fn daemon_probe_treats_transport_failure_as_unreachable() {`
  - Purpose: This test verifies that the `daemon_is_reachable()` function returns false when attempting to probe an invalid file URI, confirming that transport failures result in an unreachable status. [crates/ghook/src/planned_shutdown.rs:363-365]
- `post_enqueue_suppression_deletes_stop_envelope_for_connect_or_timeout` (function) component `post_enqueue_suppression_deletes_stop_envelope_for_connect_or_timeout [function]` (`93017a05-b596-5dca-abed-8edb8698c68b`) lines 368-390 [crates/ghook/src/planned_shutdown.rs:368-390]
  - Signature: `fn post_enqueue_suppression_deletes_stop_envelope_for_connect_or_timeout() {`
  - Purpose: This test asserts that `suppress_after_failed_post_with_marker` successfully deletes Stop/STOP envelope marker files when invoked with `DeliveryFailureKind::Connect` or `DeliveryFailureKind::Timeout`. [crates/ghook/src/planned_shutdown.rs:368-390]
- `post_enqueue_suppression_accepts_already_deleted_envelope` (function) component `post_enqueue_suppression_accepts_already_deleted_envelope [function]` (`87758fbe-1dc1-5838-82ac-d56671b8d346`) lines 393-403 [crates/ghook/src/planned_shutdown.rs:393-403]
  - Signature: `fn post_enqueue_suppression_accepts_already_deleted_envelope() {`
  - Purpose: Tests that suppressing a Connect-failed envelope post-enqueue returns true even when the target envelope file is already deleted. [crates/ghook/src/planned_shutdown.rs:393-403]
- `post_enqueue_suppression_rejects_http_non_stop_and_stale_marker` (function) component `post_enqueue_suppression_rejects_http_non_stop_and_stale_marker [function]` (`8a8e0b91-aed5-5088-982f-988a7945bf7c`) lines 406-436 [crates/ghook/src/planned_shutdown.rs:406-436]
  - Signature: `fn post_enqueue_suppression_rejects_http_non_stop_and_stale_marker() {`
  - Purpose: Tests that `suppress_after_failed_post_with_marker` correctly rejects suppression (returns false) for HTTP failures with Stop markers, Connect failures with PreToolUse markers, and Connect failures with false callbacks, while verifying marker files persist. [crates/ghook/src/planned_shutdown.rs:406-436]
- `post_enqueue_suppression_rejects_delete_failure` (function) component `post_enqueue_suppression_rejects_delete_failure [function]` (`7583de8d-714b-5e8c-a51f-f8f88f8fde83`) lines 439-445 [crates/ghook/src/planned_shutdown.rs:439-445]
  - Signature: `fn post_enqueue_suppression_rejects_delete_failure() {`
  - Purpose: This test verifies that `delete_enqueued()` returns `false` when the target path is a directory instead of a file. [crates/ghook/src/planned_shutdown.rs:439-445]

