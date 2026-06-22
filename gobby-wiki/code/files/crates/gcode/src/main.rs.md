---
title: crates/gcode/src/main.rs
type: code_file
provenance:
- file: crates/gcode/src/main.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/main.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

`crates/gcode/src/main.rs` exposes 3 indexed API symbols.

## How it fits

`crates/gcode/src/main.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `main` | function | Calls 'reset_sigpipe()' to restore SIGPIPE handling, then returns the 'std::process::ExitCode' produced by 'dispatch::run_with_exit_code()'. [crates/gcode/src/main.rs:4-7] |
| `reset_sigpipe` | function | Sets the process-wide 'SIGPIPE' disposition back to the default handler using 'libc::signal(SIGPIPE, SIG_DFL)' in an unsafe startup-only call. [crates/gcode/src/main.rs:16-22] |
| `reset_sigpipe` | function | Restores the process’s SIGPIPE disposition to the default handler. [crates/gcode/src/main.rs:25] |

