---
title: crates/ghook/src/output.rs
type: code_file
provenance:
- file: crates/ghook/src/output.rs
  ranges:
  - 3-5
  - 7-9
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/ghook/src/output.rs:3-5](crates/ghook/src/output.rs#L3-L5), [crates/ghook/src/output.rs:7-9](crates/ghook/src/output.rs#L7-L9)

</details>

# crates/ghook/src/output.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Purpose

Provides two small output helpers that write formatted `Arguments` directly to the process streams. `stdout` and `stderr` each lock the corresponding standard handle, call `write_fmt`, and discard any I/O error, giving the rest of the crate a simple fire-and-forget way to emit text to either stream.
[crates/ghook/src/output.rs:3-5]
[crates/ghook/src/output.rs:7-9]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `stdout` | function | `pub(crate) fn stdout(args: Arguments<'_>) {` | `stdout [function]` | `677ea6dd-6742-544e-9bff-64bd94b6a6b1` | 3-5 [crates/ghook/src/output.rs:3-5] | Indexed function `stdout` in `crates/ghook/src/output.rs`. [crates/ghook/src/output.rs:3-5] |
| `stderr` | function | `pub(crate) fn stderr(args: Arguments<'_>) {` | `stderr [function]` | `0a198369-26e3-55ef-a139-d04ae0c5fa76` | 7-9 [crates/ghook/src/output.rs:7-9] | Indexed function `stderr` in `crates/ghook/src/output.rs`. [crates/ghook/src/output.rs:7-9] |
