---
title: crates/gcode/src/utils.rs
type: code_file
provenance:
- file: crates/gcode/src/utils.rs
  ranges:
  - 4-12
  - 14-16
  - 18-22
  - 29-31
  - 34-36
  - 39-41
  - 44-48
  - 51-53
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/utils.rs:4-12](crates/gcode/src/utils.rs#L4-L12), [crates/gcode/src/utils.rs:14-16](crates/gcode/src/utils.rs#L14-L16), [crates/gcode/src/utils.rs:18-22](crates/gcode/src/utils.rs#L18-L22), [crates/gcode/src/utils.rs:29-31](crates/gcode/src/utils.rs#L29-L31), [crates/gcode/src/utils.rs:34-36](crates/gcode/src/utils.rs#L34-L36), [crates/gcode/src/utils.rs:39-41](crates/gcode/src/utils.rs#L39-L41), [crates/gcode/src/utils.rs:44-48](crates/gcode/src/utils.rs#L44-L48), [crates/gcode/src/utils.rs:51-53](crates/gcode/src/utils.rs#L51-L53)

</details>

# crates/gcode/src/utils.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

Utility helpers for `gcode` that normalize identifiers and validate numeric conversions: `api_key_fingerprint` returns a stable 16-hex-character fingerprint from the first 8 bytes of a SHA-256 digest, `short_id` truncates an ID to the first 8 Unicode scalar values, and `i64_to_usize` converts signed counts to `usize` with a contextual error on negative or overflow values. The test module exercises the truncation and fingerprinting behavior across long, short, exact-length, and Unicode inputs to lock in those edge cases.
[crates/gcode/src/utils.rs:4-12]
[crates/gcode/src/utils.rs:14-16]
[crates/gcode/src/utils.rs:18-22]
[crates/gcode/src/utils.rs:29-31]
[crates/gcode/src/utils.rs:34-36]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `api_key_fingerprint` | function | `pub fn api_key_fingerprint(api_key: &str) -> String {` | `api_key_fingerprint [function]` | `ad5c0986-eae3-56e6-9e32-77b939e69cab` | 4-12 [crates/gcode/src/utils.rs:4-12] | Indexed function `api_key_fingerprint` in `crates/gcode/src/utils.rs`. [crates/gcode/src/utils.rs:4-12] |
| `short_id` | function | `pub fn short_id(id: &str) -> String {` | `short_id [function]` | `300bbf35-9e00-5213-82f8-225bad6fccda` | 14-16 [crates/gcode/src/utils.rs:14-16] | Indexed function `short_id` in `crates/gcode/src/utils.rs`. [crates/gcode/src/utils.rs:14-16] |
| `i64_to_usize` | function | `pub(crate) fn i64_to_usize(value: i64, column: &str) -> anyhow::Result<usize> {` | `i64_to_usize [function]` | `fae1da5d-8bd3-5d4b-88f0-3b7ff07b8a25` | 18-22 [crates/gcode/src/utils.rs:18-22] | Indexed function `i64_to_usize` in `crates/gcode/src/utils.rs`. [crates/gcode/src/utils.rs:18-22] |
| `short_id_truncates_long_ids` | function | `fn short_id_truncates_long_ids() {` | `short_id_truncates_long_ids [function]` | `ec5a2acc-c541-5277-b3ea-274def0123c0` | 29-31 [crates/gcode/src/utils.rs:29-31] | Indexed function `short_id_truncates_long_ids` in `crates/gcode/src/utils.rs`. [crates/gcode/src/utils.rs:29-31] |
| `short_id_returns_input_for_short_strings` | function | `fn short_id_returns_input_for_short_strings() {` | `short_id_returns_input_for_short_strings [function]` | `05de6dda-c389-5e30-9849-b4695870bc9b` | 34-36 [crates/gcode/src/utils.rs:34-36] | Indexed function `short_id_returns_input_for_short_strings` in `crates/gcode/src/utils.rs`. [crates/gcode/src/utils.rs:34-36] |
| `short_id_returns_input_for_exact_length` | function | `fn short_id_returns_input_for_exact_length() {` | `short_id_returns_input_for_exact_length [function]` | `605a2b69-f74a-5f7b-a144-491bbac0f65c` | 39-41 [crates/gcode/src/utils.rs:39-41] | Indexed function `short_id_returns_input_for_exact_length` in `crates/gcode/src/utils.rs`. [crates/gcode/src/utils.rs:39-41] |
| `short_id_handles_unicode` | function | `fn short_id_handles_unicode() {` | `short_id_handles_unicode [function]` | `066a21cd-b78f-53db-913b-108eb1adb7d6` | 44-48 [crates/gcode/src/utils.rs:44-48] | Indexed function `short_id_handles_unicode` in `crates/gcode/src/utils.rs`. [crates/gcode/src/utils.rs:44-48] |
| `api_key_fingerprint_uses_stable_short_sha256` | function | `fn api_key_fingerprint_uses_stable_short_sha256() {` | `api_key_fingerprint_uses_stable_short_sha256 [function]` | `8037f444-32f0-5ee8-b1f7-52f8f33b2c2c` | 51-53 [crates/gcode/src/utils.rs:51-53] | Indexed function `api_key_fingerprint_uses_stable_short_sha256` in `crates/gcode/src/utils.rs`. [crates/gcode/src/utils.rs:51-53] |
