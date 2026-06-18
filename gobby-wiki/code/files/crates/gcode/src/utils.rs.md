---
title: crates/gcode/src/utils.rs
type: code_file
provenance:
- file: crates/gcode/src/utils.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/utils.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

`crates/gcode/src/utils.rs` exposes 8 indexed API symbols.

## How it fits

`crates/gcode/src/utils.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `api_key_fingerprint` | function | Computes the SHA-256 digest of the API key bytes and returns the first 8 bytes encoded as a 16-character lowercase hexadecimal fingerprint string. [crates/gcode/src/utils.rs:4-12] |
| `short_id` | function | Returns a 'String' containing the first eight Unicode scalar values from 'id', or the entire string if it is shorter than eight characters. [crates/gcode/src/utils.rs:14-16] |
| `i64_to_usize` | function | Converts an 'i64' to 'usize' via 'try_into', returning an 'anyhow::Result' with a column-specific context error if the value is negative or exceeds 'usize' range. [crates/gcode/src/utils.rs:18-22] |
| `short_id_truncates_long_ids` | function | Verifies that 'short_id' truncates an input identifier longer than eight characters by returning only the first eight characters, e.g. '"1234567890"' becomes '"12345678"'. [crates/gcode/src/utils.rs:29-31] |
| `short_id_returns_input_for_short_strings` | function | Verifies that 'short_id' returns the original input unchanged when given a short string, specifically '"abc"'. [crates/gcode/src/utils.rs:34-36] |
| `short_id_returns_input_for_exact_length` | function | Verifies that 'short_id' returns the original string unchanged when the input is exactly eight characters long. [crates/gcode/src/utils.rs:39-41] |
| `short_id_handles_unicode` | function | Verifies that 'short_id' correctly truncates a Unicode string of nine 'é' characters down to eight characters without corrupting multibyte text. [crates/gcode/src/utils.rs:44-48] |
| `api_key_fingerprint_uses_stable_short_sha256` | function | Verifies that 'api_key_fingerprint("secret-key")' deterministically returns the fixed 16-character short SHA-256 fingerprint '"85dbe15d75ef9308"'. [crates/gcode/src/utils.rs:51-53] |

