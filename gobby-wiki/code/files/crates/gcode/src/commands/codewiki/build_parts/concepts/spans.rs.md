---
title: crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
degraded: true
degraded_sources:
- model-unavailable
---

# crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts/concepts|crates/gcode/src/commands/codewiki/build_parts/concepts]]

## Overview

## How it fits

This file serves as a functional helper within the broader concepts-building phase of the documentation generation process. It links logical pages and conceptual models back to physical source locations by interacting with mapped document structures.

The `all_input_spans` function in crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs:4-13 aggregates source spans directly from pre-resolved slices of file and module documentation objects. This serves scenarios where the documents are already loaded.
[crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs:4-13]
[crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs:15-42]
[crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs:44-62]

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `all_input_spans` | function | Returns a deduplicated, sorted 'Vec<SourceSpan>' containing the union of all 'source_spans' from the provided 'files' and 'modules' by inserting them into a 'BTreeSet' and collecting the result. [crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs:4-13] |
| `narrative_spans` | function | Collects and deduplicates all 'SourceSpan's referenced by the page’s own modules/files plus each referenced concept’s modules/files, resolving lookups through the provided module and file maps and returning the spans in sorted order. [crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs:15-42] |
| `item_spans` | function | 'item_spans' resolves the requested module and file names through the provided lookup maps, collects all associated 'source_spans' into a 'BTreeSet' to deduplicate and sort them, and returns the resulting spans as a 'Vec<SourceSpan>'. [crates/gcode/src/commands/codewiki/build_parts/concepts/spans.rs:44-62] |

