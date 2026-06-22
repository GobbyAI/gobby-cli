---
title: crates/gcode/src/commands/codewiki/text.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/text.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/text.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Overview

`crates/gcode/src/commands/codewiki/text.rs` exposes 20 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/text.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `span` | function | Constructs a 'SourceSpan' from a file path (converted via the 'Into<String>' trait) and a line range defined by start and end line numbers. [crates/gcode/src/commands/codewiki/text.rs:52-58] |
| `transport_failure` | function | Constructs and returns an 'AiError::TransportFailure' variant with null status and body fields and "connection reset" as the error source. [crates/gcode/src/commands/codewiki/text.rs:325-331] |

_Verified by 18 in-file unit tests._

