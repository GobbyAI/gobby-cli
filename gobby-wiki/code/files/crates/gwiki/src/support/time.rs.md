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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/support/time.rs:3-6](crates/gwiki/src/support/time.rs#L3-L6), [crates/gwiki/src/support/time.rs:8-17](crates/gwiki/src/support/time.rs#L8-L17), [crates/gwiki/src/support/time.rs:24-39](crates/gwiki/src/support/time.rs#L24-L39)

</details>

# crates/gwiki/src/support/time.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file provides small time utilities for the wiki support code. `unix_timestamp_ms` reads the current `SystemTime`, converts it to Unix epoch milliseconds, and returns `WikiError::Config` if the clock is before the epoch or the value does not fit in `u64`; `collect_timestamp` builds on that by formatting the result as `unix-ms:{millis}`. The test checks that `unix_timestamp_ms` returns a plausible epoch-millisecond timestamp within a recent range.
[crates/gwiki/src/support/time.rs:3-6]
[crates/gwiki/src/support/time.rs:8-17]
[crates/gwiki/src/support/time.rs:24-39]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `collect_timestamp` | function | `pub(crate) fn collect_timestamp() -> Result<String, WikiError> {` | `collect_timestamp [function]` | `3e2f928b-097a-5b21-9bce-c31e8a06b096` | 3-6 [crates/gwiki/src/support/time.rs:3-6] | Indexed function `collect_timestamp` in `crates/gwiki/src/support/time.rs`. [crates/gwiki/src/support/time.rs:3-6] |
| `unix_timestamp_ms` | function | `pub(crate) fn unix_timestamp_ms() -> Result<u64, WikiError> {` | `unix_timestamp_ms [function]` | `846416e3-5b33-5a34-aaa2-933004d7b604` | 8-17 [crates/gwiki/src/support/time.rs:8-17] | Indexed function `unix_timestamp_ms` in `crates/gwiki/src/support/time.rs`. [crates/gwiki/src/support/time.rs:8-17] |
| `unix_timestamp_ms_returns_epoch_milliseconds` | function | `fn unix_timestamp_ms_returns_epoch_milliseconds() {` | `unix_timestamp_ms_returns_epoch_milliseconds [function]` | `53594747-a121-50f2-a698-e8d276c76a69` | 24-39 [crates/gwiki/src/support/time.rs:24-39] | Indexed function `unix_timestamp_ms_returns_epoch_milliseconds` in `crates/gwiki/src/support/time.rs`. [crates/gwiki/src/support/time.rs:24-39] |
