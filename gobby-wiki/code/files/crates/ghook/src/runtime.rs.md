---
title: crates/ghook/src/runtime.rs
type: code_file
provenance:
- file: crates/ghook/src/runtime.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/ghook/src/runtime.rs

Module: [[code/modules/crates/ghook/src|crates/ghook/src]]

## Overview

`crates/ghook/src/runtime.rs` exposes 1 indexed API symbol.

## How it fits

`crates/ghook/src/runtime.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `write_runtime_stamp` | function | The 'write_runtime_stamp' function creates a 'bin' directory within the Gobby home path, atomically writes a JSON file named '.ghook-runtime.json' containing current schema and ghook version metadata to it, and outputs the ghook version to standard output. [crates/ghook/src/runtime.rs:4-16] |

