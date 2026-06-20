---
title: crates/gcode/src/commands/codewiki/render/common.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/render/common.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/render/common.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/render|crates/gcode/src/commands/codewiki/render]]

## Overview

`crates/gcode/src/commands/codewiki/render/common.rs` exposes 6 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/render/common.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `model_degraded_sources` | function | Returns a single-element vector containing '"model-unavailable"' when 'degraded' is 'true', otherwise returns an empty 'Vec<String>'. [crates/gcode/src/commands/codewiki/render/common.rs:1-7] |
| `cell_summary` | function | The 'cell_summary' function extracts the first paragraph of a Markdown summary by joining its trimmed, non-empty lines with spaces, halting at empty lines or Markdown table rows, falling back to a whitespace-flattened full summary if empty, and truncating the result to a maximum character limit at a word boundary with an appended ellipsis. [crates/gcode/src/commands/codewiki/render/common.rs:23-61] |

_Verified by 4 in-file unit tests._

