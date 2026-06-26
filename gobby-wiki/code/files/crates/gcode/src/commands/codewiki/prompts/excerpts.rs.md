---
title: crates/gcode/src/commands/codewiki/prompts/excerpts.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/prompts/excerpts.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/prompts/excerpts.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/prompts|crates/gcode/src/commands/codewiki/prompts]]

## Overview

`crates/gcode/src/commands/codewiki/prompts/excerpts.rs` exposes 4 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/prompts/excerpts.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `append_source_excerpt_section` | function | This function appends a capped number of source excerpts to a prompt string by delegating to 'append_source_excerpt_section_n' with 'MAX_PROMPT_SOURCE_EXCERPTS' as the limit. [crates/gcode/src/commands/codewiki/prompts/excerpts.rs:5-7] |
| `append_source_excerpt_section_n` | function | Appends up to 'take' source code excerpts with formatted file paths, line ranges, and bounded content to a mutable prompt string. [crates/gcode/src/commands/codewiki/prompts/excerpts.rs:12-31] |
| `summary_excerpt` | function | # Function Summary 'summary_excerpt' extracts the first paragraph from a summary string, normalizes whitespace, and returns it truncated to 'CHILD_SUMMARY_EXCERPT_MAX_CHARS' with a trailing ellipsis if necessary. [crates/gcode/src/commands/codewiki/prompts/excerpts.rs:60-80] |
| `bounded_excerpt` | function | Truncates a trimmed excerpt to 'SOURCE_EXCERPT_MAX_CHARS' characters and appends an ellipsis if truncation occurs. [crates/gcode/src/commands/codewiki/prompts/excerpts.rs:84-98] |

