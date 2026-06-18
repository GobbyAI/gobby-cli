---
title: crates/ghook/src/planned_shutdown.rs
type: code_file
provenance:
- file: crates/ghook/src/planned_shutdown.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/ghook/src/planned_shutdown.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Overview

`crates/ghook/src/planned_shutdown.rs` exposes 31 indexed API symbols.

## How it fits

`crates/ghook/src/planned_shutdown.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `should_skip_dispatch` | function | Returns 'should_skip_dispatch_with' for the given 'hook_type', using a closure that detects a fresh shutdown marker in 'marker_home()' and another that checks whether the daemon at 'gobby_core::daemon_url::daemon_url()' is reachable. [crates/ghook/src/planned_shutdown.rs:21-27] |
| `suppress_after_failed_post` | function | Returns the result of 'suppress_after_failed_post_with_marker' for the given hook type, optional delivery failure kind, and enqueued path, using a marker check that reports whether 'marker_home()' exists and contains a fresh shutdown marker. [crates/ghook/src/planned_shutdown.rs:29-37] |
| `suppress_after_failed_post_with_marker` | function | Returns 'false' unless 'should_suppress_failed_post(hook_type, failure_kind, marker_active)' is true, in which case it deletes the enqueued file at 'enqueued_path' and returns whether that deletion succeeded. [crates/ghook/src/planned_shutdown.rs:39-50] |
| `is_stop_hook` | function | Returns 'true' when 'hook_type' equals '"stop"' case-insensitively, and 'false' otherwise. [crates/ghook/src/planned_shutdown.rs:52-54] |
| `should_skip_dispatch_with` | function | Returns 'true' only when 'hook_type' is a stop hook, the local marker is active, and the daemon is not reachable, indicating dispatch should be skipped in that case. [crates/ghook/src/planned_shutdown.rs:56-62] |
| `should_suppress_failed_post` | function | Returns 'true' only when 'hook_type' is a stop hook, 'failure_kind' is 'Connect' or 'Timeout', and 'marker_active()' evaluates to 'true'; otherwise it returns 'false'. [crates/ghook/src/planned_shutdown.rs:64-75] |
| `fresh_shutdown_marker` | function | Returns the result of 'fresh_shutdown_marker_at(home, now_secs(), allow_seconds())', checking whether the shutdown marker at 'home' is considered fresh using the current time and the permitted age threshold. [crates/ghook/src/planned_shutdown.rs:77-79] |
| `fresh_shutdown_marker_at` | function | Returns 'true' only if 'home/ACTIVE_MARKER' exists and its contents satisfy 'marker_is_allowed_and_fresh(&marker, now, allow_seconds)', otherwise 'false'. [crates/ghook/src/planned_shutdown.rs:81-84] |
| `marker_is_allowed_and_fresh` | function | Returns 'true' only for markers with a present timestamp not in the future and no older than 'allow_seconds', where the marker is either an explicit 'stop'/'restart' intent or has a 'source' whose lowercase text starts with one of 'ALLOWED_SOURCES'. [crates/ghook/src/planned_shutdown.rs:86-113] |
| `read_marker` | function | Reads the file at 'path', attempts to parse it as JSON into a 'serde_json::Value', and returns 'Some(value)' only if both operations succeed and the parsed value is a JSON object, otherwise 'None'. [crates/ghook/src/planned_shutdown.rs:115-119] |
| `daemon_is_reachable` | function | Returns 'true' if an HTTP GET health probe to the daemon’s 'HEALTH_ENDPOINT' succeeds or receives any HTTP status response, and 'false' only when the request fails with a transport error after logging the failure. [crates/ghook/src/planned_shutdown.rs:121-130] |
| `marker_home` | function | Returns the 'gobby_core::gobby_home()' path if it resolves successfully, otherwise 'None'. [crates/ghook/src/planned_shutdown.rs:132-134] |
| `allow_seconds` | function | Returns the shutdown-hook grace period in seconds by reading 'GOBBY_SHUTDOWN_HOOK_ALLOW_SECONDS' from the environment and passing its optional string value to 'allow_seconds_from_env'. [crates/ghook/src/planned_shutdown.rs:136-142] |
| `allow_seconds_from_env` | function | Returns the parsed 'f64' from the optional environment string only if it is finite and strictly positive, otherwise falling back to 'DEFAULT_ALLOW_SECONDS'. [crates/ghook/src/planned_shutdown.rs:144-152] |
| `optional_float` | function | Returns 'Some(f64)' when the input 'Value' is either a numeric variant convertible via 'as_f64()' or a string that parses as an 'f64', and returns 'None' for all other cases or parse failures. [crates/ghook/src/planned_shutdown.rs:154-160] |
| `value_as_text` | function | Returns a 'String' copy of a 'Value' when it is a 'String', 'Number', or 'Bool' by converting the inner value to text, and returns 'None' for all other variants. [crates/ghook/src/planned_shutdown.rs:162-169] |
| `now_secs` | function | Returns the current system time as a 'f64' number of seconds since the Unix epoch, or '0.0' if the clock is earlier than the epoch. [crates/ghook/src/planned_shutdown.rs:171-176] |
| `delete_enqueued` | function | Deletes the file at 'enqueued_path' and returns 'true' if the removal succeeds or the file is already absent, otherwise returns 'false'. [crates/ghook/src/planned_shutdown.rs:178-184] |
| `write_marker` | function | Creates the 'home' directory if needed, then serializes 'value' to JSON bytes and writes it to the file 'home/name', panicking on any I/O or serialization failure. [crates/ghook/src/planned_shutdown.rs:195-198] |
| `stop_hook_matching_is_case_insensitive` | function | Verifies that 'is_stop_hook' performs case-insensitive matching for the literal '"stop"' and does not match strings containing it as a substring such as '"SubagentStop"'. [crates/ghook/src/planned_shutdown.rs:201-206] |
| `marker_accepts_fresh_allowed_intents` | function | Verifies that an 'ACTIVE_MARKER' containing the allowed 'restart' intent and a timestamp within the freshness window is accepted as fresh by 'fresh_shutdown_marker_at'. [crates/ghook/src/planned_shutdown.rs:209-219] |
| `marker_accepts_allowed_source_prefixes` | function | Verifies that 'fresh_shutdown_marker_at' treats active markers whose 'source' is one of 'cli_stop', 'http_shutdown', 'service_restart', or 'mcp_stop' and whose timestamp is recent as valid shutdown markers. [crates/ghook/src/planned_shutdown.rs:222-237] |
| `marker_rejects_stale_missing_invalid_and_disallowed_markers` | function | Verifies that 'fresh_shutdown_marker_at' returns 'false' for shutdown markers that are stale, timestamped in the future, missing a timestamp, contain invalid JSON, or use a disallowed source/intent. [crates/ghook/src/planned_shutdown.rs:240-282] |
| `env_freshness_override_uses_positive_parseable_values` | function | Verifies that 'allow_seconds_from_env' returns the default when the environment value is absent, zero, negative, or unparsable, and only overrides it with a positive parseable value such as '2.5'. [crates/ghook/src/planned_shutdown.rs:285-291] |
| `skip_dispatch_requires_stop_marker_and_unreachable_daemon` | function | Verifies that 'should_skip_dispatch_with' returns 'true' only for 'Stop'/'stop' when the stop-marker condition is present and the daemon is unreachable, and returns 'false' for other markers, missing stop conditions, or a reachable daemon. [crates/ghook/src/planned_shutdown.rs:294-304] |
| `daemon_probe_treats_http_responses_as_reachable` | function | Verifies that 'daemon_is_reachable' returns 'true' for an HTTP endpoint by sending a 'GET /api/admin/health' request and treating an 'HTTP/1.1 503 Service Unavailable' response as reachable. [crates/ghook/src/planned_shutdown.rs:307-323] |
| `daemon_probe_treats_transport_failure_as_unreachable` | function | Verifies that 'daemon_is_reachable("file:///tmp/not-a-daemon")' returns 'false' when the probe encounters a transport failure. [crates/ghook/src/planned_shutdown.rs:326-328] |
| `post_enqueue_suppression_deletes_stop_envelope_for_connect_or_timeout` | function | Verifies that 'suppress_after_failed_post_with_marker' returns 'true' and deletes the suppression file when the post marker matches 'Stop'/'STOP' for 'Connect' or 'Timeout' delivery failures. [crates/ghook/src/planned_shutdown.rs:331-353] |
| `post_enqueue_suppression_accepts_already_deleted_envelope` | function | Verifies that 'suppress_after_failed_post_with_marker' returns 'true' for a failed post with 'DeliveryFailureKind::Connect' even when the marker/envelope file path points to a non-existent file. [crates/ghook/src/planned_shutdown.rs:356-366] |
| `post_enqueue_suppression_rejects_http_non_stop_and_stale_marker` | function | Verifies that 'suppress_after_failed_post_with_marker' returns 'false' and leaves the marker file intact for HTTP delivery failures, non-'Stop' post events, and stale markers. [crates/ghook/src/planned_shutdown.rs:369-399] |
| `post_enqueue_suppression_rejects_delete_failure` | function | Creates a temporary directory at a path named 'not-a-file' and asserts that 'delete_enqueued(&path)' returns 'false' when the target is a directory rather than a file. [crates/ghook/src/planned_shutdown.rs:402-408] |

