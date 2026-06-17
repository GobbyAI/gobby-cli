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

<details>
<summary>Relevant source files</summary>

- [crates/ghook/src/detach.rs:23-44](crates/ghook/src/detach.rs#L23-L44)

</details>

# crates/ghook/src/detach.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Purpose

Provides a cross-platform best-effort process detachment helper. On Unix, `detach()` calls `setsid()` to start a new session and leave the controlling terminal and parent process group; on Windows, it calls `FreeConsole()` to detach from the console. The file keeps the behavior intentionally minimal and non-fatal: failures are ignored so callers can request detachment without handling platform-specific daemonization details. [crates/ghook/src/detach.rs:23-44]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `detach` | function | `pub fn detach() {` | `detach [function]` | `ad9a59f4-3cd2-52d5-8dc9-1447563bcc66` | 23-44 [crates/ghook/src/detach.rs:23-44] | Indexed function `detach` in `crates/ghook/src/detach.rs`. [crates/ghook/src/detach.rs:23-44] |
