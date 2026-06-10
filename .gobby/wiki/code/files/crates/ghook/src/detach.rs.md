---
title: crates/ghook/src/detach.rs
type: code_file
provenance:
- file: crates/ghook/src/detach.rs
  ranges:
  - 23-43
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/ghook/src/detach.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Purpose

`crates/ghook/src/detach.rs` exposes 1 indexed API symbol. [crates/ghook/src/detach.rs:23-43]

## API Symbols

- `detach` (function) component `detach [function]` (`ad9a59f4-3cd2-52d5-8dc9-1447563bcc66`) lines 23-43 [crates/ghook/src/detach.rs:23-43]
  - Signature: `pub fn detach() {`
  - Purpose: The `detach()` function disconnects the current process from its controlling terminal or console by invoking platform-specific system calls: `setsid()` on Unix-based systems and `FreeConsole()` on Windows. [crates/ghook/src/detach.rs:23-43]

