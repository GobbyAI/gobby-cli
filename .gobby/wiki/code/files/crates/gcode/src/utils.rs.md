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

# crates/gcode/src/utils.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Purpose

Provides small utility helpers for `gcode`: `api_key_fingerprint` turns an API key into a stable 16-character SHA-256 fingerprint, `short_id` trims identifiers to the first eight Unicode characters, and `i64_to_usize` converts signed counts to `usize` with contextual error reporting. The tests lock in truncation behavior, Unicode handling, and deterministic fingerprint output.
[crates/gcode/src/utils.rs:4-12]
[crates/gcode/src/utils.rs:14-16]
[crates/gcode/src/utils.rs:18-22]
[crates/gcode/src/utils.rs:29-31]
[crates/gcode/src/utils.rs:34-36]

## API Symbols

- `api_key_fingerprint` (function) component `api_key_fingerprint [function]` (`ad5c0986-eae3-56e6-9e32-77b939e69cab`) lines 4-12 [crates/gcode/src/utils.rs:4-12]
  - Signature: `pub fn api_key_fingerprint(api_key: &str) -> String {`
  - Purpose: Computes a 16-character hexadecimal fingerprint of an API key by SHA256-hashing it and encoding the first 8 bytes as hex digits. [crates/gcode/src/utils.rs:4-12]
- `short_id` (function) component `short_id [function]` (`300bbf35-9e00-5213-82f8-225bad6fccda`) lines 14-16 [crates/gcode/src/utils.rs:14-16]
  - Signature: `pub fn short_id(id: &str) -> String {`
  - Purpose: This function truncates the input string to its first 8 characters and returns the result as a new String. [crates/gcode/src/utils.rs:14-16]
- `i64_to_usize` (function) component `i64_to_usize [function]` (`fae1da5d-8bd3-5d4b-88f0-3b7ff07b8a25`) lines 18-22 [crates/gcode/src/utils.rs:18-22]
  - Signature: `pub(crate) fn i64_to_usize(value: i64, column: &str) -> anyhow::Result<usize> {`
  - Purpose: Converts an i64 to usize, wrapping any conversion failure with error context that includes the source column name and the invalid value. [crates/gcode/src/utils.rs:18-22]
- `short_id_truncates_long_ids` (function) component `short_id_truncates_long_ids [function]` (`ec5a2acc-c541-5277-b3ea-274def0123c0`) lines 29-31 [crates/gcode/src/utils.rs:29-31]
  - Signature: `fn short_id_truncates_long_ids() {`
  - Purpose: This test verifies that the `short_id` function truncates a 10-character string input to its first 8 characters. [crates/gcode/src/utils.rs:29-31]
- `short_id_returns_input_for_short_strings` (function) component `short_id_returns_input_for_short_strings [function]` (`05de6dda-c389-5e30-9849-b4695870bc9b`) lines 34-36 [crates/gcode/src/utils.rs:34-36]
  - Signature: `fn short_id_returns_input_for_short_strings() {`
  - Purpose: This test verifies that the `short_id` function returns the input string unchanged when passed a short string argument. [crates/gcode/src/utils.rs:34-36]
- `short_id_returns_input_for_exact_length` (function) component `short_id_returns_input_for_exact_length [function]` (`605a2b69-f74a-5f7b-a144-491bbac0f65c`) lines 39-41 [crates/gcode/src/utils.rs:39-41]
  - Signature: `fn short_id_returns_input_for_exact_length() {`
  - Purpose: This test verifies that the `short_id()` function returns its input unmodified when passed an 8-character string. [crates/gcode/src/utils.rs:39-41]
- `short_id_handles_unicode` (function) component `short_id_handles_unicode [function]` (`066a21cd-b78f-53db-913b-108eb1adb7d6`) lines 44-48 [crates/gcode/src/utils.rs:44-48]
  - Signature: `fn short_id_handles_unicode() {`
  - Purpose: Tests that the `short_id` function truncates a 9-character Unicode string (U+00E9 repeated) to 8 characters. [crates/gcode/src/utils.rs:44-48]
- `api_key_fingerprint_uses_stable_short_sha256` (function) component `api_key_fingerprint_uses_stable_short_sha256 [function]` (`8037f444-32f0-5ee8-b1f7-52f8f33b2c2c`) lines 51-53 [crates/gcode/src/utils.rs:51-53]
  - Signature: `fn api_key_fingerprint_uses_stable_short_sha256() {`
  - Purpose: This test verifies that `api_key_fingerprint()` generates a stable, deterministic 16-character SHA256-based hash for a given API key input. [crates/gcode/src/utils.rs:51-53]

