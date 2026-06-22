---
title: crates/gwiki/src/commands/ask/render.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/ask/render.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/ask/render.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/commands/ask/render.rs` exposes 3 indexed API symbols.

## How it fits

`crates/gwiki/src/commands/ask/render.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `render` | function | Serializes the 'AskOutput' to JSON, renders response text from its query and scope, and returns a scoped '"ask"' 'CommandOutcome', mapping serialization failures into 'WikiError::Json'. [crates/gwiki/src/commands/ask/render.rs:6-16] |
| `render_text` | function | 'render_text' formats either a synthesized answer or a fallback wiki-hits report for the given query and scope, including degradation notices, hit listings, code citations, and an unverified-claims warning when citation support is incomplete. [crates/gwiki/src/commands/ask/render.rs:18-68] |

_Verified by 1 in-file unit test._

