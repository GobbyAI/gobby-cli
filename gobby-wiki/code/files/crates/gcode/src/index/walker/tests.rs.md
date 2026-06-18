---
title: crates/gcode/src/index/walker/tests.rs
type: code_file
provenance:
- file: crates/gcode/src/index/walker/tests.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/walker/tests.rs

Module: [[code/modules/crates/gcode/src/index/walker|crates/gcode/src/index/walker]]

## Overview

`crates/gcode/src/index/walker/tests.rs` exposes 2 indexed API symbols.

## How it fits

`crates/gcode/src/index/walker/tests.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `write_file` | function | Creates any missing parent directories under 'root' for the relative path 'rel', then writes 'contents' to the resulting file path, panicking on any filesystem error. [crates/gcode/src/index/walker/tests.rs:11-17] |
| `rels` | function | Returns the sorted list of UTF-8-lossy relative path strings obtained by stripping 'root' from each input path, panicking if any path is not under 'root'. [crates/gcode/src/index/walker/tests.rs:19-31] |

