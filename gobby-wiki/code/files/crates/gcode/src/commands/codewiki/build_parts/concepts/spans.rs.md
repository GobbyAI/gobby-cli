---
title: crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts|crates/gcode/src/commands/codewiki/build_parts]]

## Overview

`crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs` exposes 3 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `all_input_spans` | function | Returns a deduplicated, sorted 'Vec<SourceSpan>' containing the union of all 'source_spans' from the provided 'files' and 'modules' by inserting them into a 'BTreeSet' and collecting the result. [crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs:4-13] |
| `narrative_spans` | function | Collects and deduplicates all 'SourceSpan's referenced by the page’s own modules/files plus each referenced concept’s modules/files, resolving lookups through the provided module and file maps and returning the spans in sorted order. [crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs:15-42] |
| `item_spans` | function | 'item_spans' resolves the requested module and file names through the provided lookup maps, collects all associated 'source_spans' into a 'BTreeSet' to deduplicate and sort them, and returns the resulting spans as a 'Vec<SourceSpan>'. [crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs:44-62] |

