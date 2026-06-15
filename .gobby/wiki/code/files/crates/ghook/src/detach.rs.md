---
title: crates/ghook/src/detach.rs
type: code_file
provenance:
- file: crates/ghook/src/detach.rs
  ranges:
  - 23-44
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/ghook/src/detach.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Purpose

Provides a small cross-platform helper for detaching the current process from its controlling terminal or console. On Unix, `detach()` calls `setsid()` to start a new session and leave the parent process group; on Windows, it calls `FreeConsole()` as a best-effort way to drop console attachment. The function is intentionally lightweight and non-fatal: failures are ignored so callers can request detachment without changing control flow. [crates/ghook/src/detach.rs:23-44]

## API Symbols

- `detach` (function) component `detach [function]` (`ad9a59f4-3cd2-52d5-8dc9-1447563bcc66`) lines 23-44 [crates/ghook/src/detach.rs:23-44]
  - Signature: `pub fn detach() {`
  - Purpose: Indexed function `detach` in `crates/ghook/src/detach.rs`. [crates/ghook/src/detach.rs:23-44]

