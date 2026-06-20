---
title: crates/gcode/src/progress.rs
type: code_file
provenance:
- file: crates/gcode/src/progress.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/progress.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

`crates/gcode/src/progress.rs` exposes 4 indexed API symbols.

## How it fits

`crates/gcode/src/progress.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `ProgressBar` | class | 'ProgressBar' is a struct that tracks a bounded progress state with a total and current count, an enabled flag, and a configured bar width for rendering. [crates/gcode/src/progress.rs:9-14] |
| `ProgressBar::new` | method | Constructs a new instance with 'current' initialized to '0', 'bar_width' fixed at '20', and 'enabled' set to 'true' only when 'quiet' is 'false', 'total > 0', and 'stderr' is a terminal. [crates/gcode/src/progress.rs:18-26] |
| `ProgressBar::tick` | method | Increments the progress counter, and if progress reporting is enabled, renders an updated stderr progress bar with the current/total count and a left-truncated file path constrained to an 80-character terminal width, then flushes stderr. [crates/gcode/src/progress.rs:29-62] |
| `ProgressBar::finish` | method | If 'self.enabled' is true, this method clears the current stderr line with a carriage return and ANSI erase-line sequence, then flushes 'stderr', otherwise it does nothing. [crates/gcode/src/progress.rs:65-70] |

