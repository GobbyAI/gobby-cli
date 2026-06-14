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

# crates/ghook/src/output.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Purpose

Provides two tiny output helpers for the crate: `stdout` writes formatted `Arguments` to a locked standard output stream, and `stderr` does the same for standard error. Both ignore any I/O error from `write_fmt`, so the file centralizes best-effort console logging without propagating failures.
[crates/ghook/src/output.rs:3-5]
[crates/ghook/src/output.rs:7-9]

## API Symbols

- `stdout` (function) component `stdout [function]` (`677ea6dd-6742-544e-9bff-64bd94b6a6b1`) lines 3-5 [crates/ghook/src/output.rs:3-5]
  - Signature: `pub(crate) fn stdout(args: Arguments<'_>) {`
  - Purpose: Writes the provided formatted 'Arguments' to the process’s locked standard output, ignoring any I/O error. [crates/ghook/src/output.rs:3-5]
- `stderr` (function) component `stderr [function]` (`0a198369-26e3-55ef-a139-d04ae0c5fa76`) lines 7-9 [crates/ghook/src/output.rs:7-9]
  - Signature: `pub(crate) fn stderr(args: Arguments<'_>) {`
  - Purpose: Writes the provided formatted arguments to the process’s standard error stream by locking 'stderr' and ignoring any I/O error returned by 'write_fmt'. [crates/ghook/src/output.rs:7-9]

