---
title: crates/ghook/src/output.rs
type: code_file
provenance:
- file: crates/ghook/src/output.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/ghook/src/output.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Overview

`crates/ghook/src/output.rs` exposes 2 indexed API symbols.

## How it fits

`crates/ghook/src/output.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `stdout` | function | Writes the provided formatted 'Arguments' to the process standard output by locking 'stdout' and ignoring any 'write_fmt' error. [crates/ghook/src/output.rs:3-5] |
| `stderr` | function | Writes the provided formatted arguments to the process’s locked standard error stream and ignores any I/O error returned by 'write_fmt'. [crates/ghook/src/output.rs:7-9] |

