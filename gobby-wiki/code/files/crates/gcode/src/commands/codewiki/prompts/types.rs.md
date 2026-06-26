---
title: crates/gcode/src/commands/codewiki/prompts/types.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/prompts/types.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/prompts/types.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/prompts|crates/gcode/src/commands/codewiki/prompts]]

## Overview

`crates/gcode/src/commands/codewiki/prompts/types.rs` exposes 4 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/prompts/types.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `PageEvidenceRow` | class | 'PageEvidenceRow' is a public struct that encapsulates evidence data with four String fields: 'name', 'kind', 'citation', and 'summary'. [crates/gcode/src/commands/codewiki/prompts/types.rs:7-12] |
| `SymbolSummary` | class | 'SymbolSummary' is a struct that encapsulates metadata for a code symbol, including its name, kind, component association, source location span (line_start to line_end), and documented purpose. [crates/gcode/src/commands/codewiki/prompts/types.rs:15-23] |
| `ChildSummary` | class | 'ChildSummary' is a public Rust struct containing two owned 'String' fields: 'name' and 'summary'. [crates/gcode/src/commands/codewiki/prompts/types.rs:26-29] |
| `SourceExcerpt` | class | SourceExcerpt is a struct that encapsulates a contiguous source code excerpt with its file path and line number boundaries (start and end). [crates/gcode/src/commands/codewiki/prompts/types.rs:34-39] |

