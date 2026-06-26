---
title: crates/gwiki/src/commands/ask/narration.rs
type: code_file
provenance:
- file: crates/gwiki/src/commands/ask/narration.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/commands/ask/narration.rs

Module: [[code/modules/crates/gwiki/src/commands/ask|crates/gwiki/src/commands/ask]]

## Overview

`crates/gwiki/src/commands/ask/narration.rs` exposes 9 indexed API symbols.

## How it fits

`crates/gwiki/src/commands/ask/narration.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `strip_leading_model_narration` | function | Trims leading whitespace, scans up to 'NARRATION_SCAN_LIMIT' initial sentences from 'answer' to detect model-first-person narration, and removes the maximal leading narration prefix only when the text opens with narration, otherwise returns the trimmed input unchanged. [crates/gwiki/src/commands/ask/narration.rs:7-58] |
| `leading_sentence_end` | function | Returns the byte index immediately after the first occurrence of '.', '!', or '?' in the string, or 'None' if no such sentence-ending punctuation appears. [crates/gwiki/src/commands/ask/narration.rs:60-64] |
| `is_model_narration_sentence` | function | Returns 'true' only if the trimmed, case-normalized sentence both starts with a recognized narration opener after stripping discourse markers and contains at least one narration process marker, otherwise 'false'. [crates/gwiki/src/commands/ask/narration.rs:89-103] |
| `strip_narration_discourse_markers` | function | Returns the input string slice with any leading narration/discourse markers repeatedly removed, along with an optional following comma and space, until no marker prefix remains. [crates/gwiki/src/commands/ask/narration.rs:105-123] |

_Verified by 5 in-file unit tests._

