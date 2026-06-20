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

`crates/gcode/src/commands/codewiki/text.rs` exposes 17 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/text.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `span` | function | The 'span' function constructs and returns a 'SourceSpan' struct by converting the provided 'file' parameter into a 'String' and associating it with the specified start and end line indices. [crates/gcode/src/commands/codewiki/text.rs:52-58] |
| `transport_failure` | function | Returns an 'AiError::TransportFailure' with 'status' and 'body' set to 'None' and 'source' set to '"connection reset"'. [crates/gcode/src/commands/codewiki/text.rs:285-291] |

_Verified by 15 in-file unit tests._

