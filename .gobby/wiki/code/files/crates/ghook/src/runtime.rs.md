---
title: crates/ghook/src/runtime.rs
type: code_file
provenance:
- file: crates/ghook/src/runtime.rs
  ranges:
  - 4-16
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/ghook/src/runtime.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Purpose

Provides `write_runtime_stamp`, which initializes `~/.gobby/bin`, builds a `.ghook-runtime.json` stamp containing the current envelope schema version and `ghook` version, writes it atomically, and prints `ghook <version>` to stdout. The function ties together `gobby_core` path resolution, `envelope` metadata, `diagnose` version info, `transport` atomic persistence, and `output` reporting, returning any I/O or serialization error. [crates/ghook/src/runtime.rs:4-16]

## API Symbols

- `write_runtime_stamp` (function) component `write_runtime_stamp [function]` (`56de4550-bc82-5099-9930-43415fd43d07`) lines 4-16 [crates/ghook/src/runtime.rs:4-16]
  - Signature: `pub(crate) fn write_runtime_stamp() -> Result<()> {`
  - Purpose: Creates '~/.gobby/bin/.ghook-runtime.json' with the current schema and 'ghook' version, writes it atomically, prints 'ghook <version>' to stdout, and returns success or any I/O/serialization error. [crates/ghook/src/runtime.rs:4-16]

