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

`crates/ghook/src/planned_shutdown.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

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

_Verified by 12 in-file unit tests._

