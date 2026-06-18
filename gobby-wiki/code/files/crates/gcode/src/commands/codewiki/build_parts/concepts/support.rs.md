---
title: crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/build_parts/concepts|crates/gcode/src/commands/codewiki/build_parts/concepts]]

## Overview

`crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs` exposes 6 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `degraded_sources` | function | Returns a vector containing '"model-unavailable"' when 'degraded' is 'true', and an empty vector otherwise. [crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs:1-7] |
| `concept_title` | function | Returns a title-cased display string for the last path segment of 'module', splitting on '_' and '-', discarding empty parts, capitalizing each part’s first character, and joining the results with spaces. [crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs:9-25] |
| `concept_doc_path` | function | Returns the concept document path for a given slug by appending '.md' to the result of 'concept_doc_stem(slug)'. [crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs:27-29] |
| `concept_doc_stem` | function | Returns a 'String' containing the concept documentation path stem 'code/concepts/{slug}' by formatting the provided slug into that template. [crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs:31-33] |
| `narrative_doc_path` | function | Returns the repository-relative Markdown path 'code/narrative/{slug}.md' by formatting the provided slug into that template. [crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs:35-37] |
| `slugify` | function | Converts an input string to a lowercase ASCII slug by retaining only alphanumeric characters, collapsing each run of non-alphanumerics into a single '-' between existing characters, and trimming any leading or trailing dashes. [crates/gcode/src/commands/codewiki/build_parts/concepts/support.rs:39-53] |

