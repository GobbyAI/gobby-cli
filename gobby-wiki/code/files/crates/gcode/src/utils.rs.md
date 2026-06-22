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

`crates/gcode/src/utils.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `api_key_fingerprint` | function | Computes the SHA-256 digest of the API key bytes and returns the first 8 bytes encoded as a 16-character lowercase hexadecimal fingerprint string. [crates/gcode/src/utils.rs:4-12] |
| `short_id` | function | Returns a 'String' containing the first eight Unicode scalar values from 'id', or the entire string if it is shorter than eight characters. [crates/gcode/src/utils.rs:14-16] |
| `i64_to_usize` | function | Converts an 'i64' to 'usize' via 'try_into', returning an 'anyhow::Result' with a column-specific context error if the value is negative or exceeds 'usize' range. [crates/gcode/src/utils.rs:18-22] |

_Verified by 5 in-file unit tests._

