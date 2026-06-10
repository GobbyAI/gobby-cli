---
title: crates/gwiki/src/support/time.rs
type: code_file
provenance:
- file: crates/gwiki/src/support/time.rs
  ranges:
  - 3-6
  - 8-17
  - 24-39
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/support/time.rs

Module: [[code/modules/crates/gwiki/src/support|crates/gwiki/src/support]]

## Purpose

`crates/gwiki/src/support/time.rs` exposes 3 indexed API symbols.
[crates/gwiki/src/support/time.rs:3-6]
[crates/gwiki/src/support/time.rs:8-17]
[crates/gwiki/src/support/time.rs:24-39]

## API Symbols

- `collect_timestamp` (function) component `collect_timestamp [function]` (`3e2f928b-097a-5b21-9bce-c31e8a06b096`) lines 3-6 [crates/gwiki/src/support/time.rs:3-6]
  - Signature: `pub(crate) fn collect_timestamp() -> Result<String, WikiError> {`
  - Purpose: Returns the current Unix timestamp in milliseconds as a formatted string with the "unix-ms:" prefix, or propagates a `WikiError` on failure. [crates/gwiki/src/support/time.rs:3-6]
- `unix_timestamp_ms` (function) component `unix_timestamp_ms [function]` (`846416e3-5b33-5a34-aaa2-933004d7b604`) lines 8-17 [crates/gwiki/src/support/time.rs:8-17]
  - Signature: `pub(crate) fn unix_timestamp_ms() -> Result<u64, WikiError> {`
  - Purpose: Returns the current Unix timestamp in milliseconds as a `u64`, or a `WikiError` if the system clock is before the Unix epoch or the millisecond value overflows `u64`. [crates/gwiki/src/support/time.rs:8-17]
- `unix_timestamp_ms_returns_epoch_milliseconds` (function) component `unix_timestamp_ms_returns_epoch_milliseconds [function]` (`53594747-a121-50f2-a698-e8d276c76a69`) lines 24-39 [crates/gwiki/src/support/time.rs:24-39]
  - Signature: `fn unix_timestamp_ms_returns_epoch_milliseconds() {`
  - Purpose: This test validates that `unix_timestamp_ms()` returns a u64 Unix epoch timestamp in milliseconds, bounded between a predefined minimum (January 1, 2024) and the current system time. [crates/gwiki/src/support/time.rs:24-39]

