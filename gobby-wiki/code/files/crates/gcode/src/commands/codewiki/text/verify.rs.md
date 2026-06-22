---
title: crates/gcode/src/commands/codewiki/text/verify.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/text/verify.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/text/verify.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki/text|crates/gcode/src/commands/codewiki/text]]

## Overview

`crates/gcode/src/commands/codewiki/text/verify.rs` exposes 18 indexed API symbols.

## How it fits

`crates/gcode/src/commands/codewiki/text/verify.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `VerifyOutcome` | type | Indexed type `VerifyOutcome` in `crates/gcode/src/commands/codewiki/text/verify.rs`. [crates/gcode/src/commands/codewiki/text/verify.rs:19-30] |
| `verify_with_notes` | function | Conditionally runs an external verifier on non-empty block-split text using a generated prompt from symbols, sources, and relationships, and returns 'Verified' with parsed notes when verification succeeds, otherwise 'Skipped' on missing verifier, empty input, transport failure, or malformed response. [crates/gcode/src/commands/codewiki/text/verify.rs:38-65] |
| `split_blocks` | function | Splits the input string on double-newline block separators, trims whitespace from each block, discards empty blocks, and returns the remaining blocks as owned 'String's. [crates/gcode/src/commands/codewiki/text/verify.rs:70-76] |
| `VerifyNoteResponse` | class | 'VerifyNoteResponse' is a struct containing a note identifier ('usize') and a textual 'reason' ('String') describing the verification result. [crates/gcode/src/commands/codewiki/text/verify.rs:79-82] |
| `parse_verify_notes` | function | Parses a trimmed JSON string into 'Vec<VerifyNoteResponse>', filters notes whose 'id' is within '1..=block_count', converts them to 'VerifyNote', sorts by 'id', removes duplicate 'id's, and returns 'Some(filtered_notes)' or 'None' if deserialization fails. [crates/gcode/src/commands/codewiki/text/verify.rs:87-97] |
| `sources` | function | Returns a 'Vec<SourceExcerpt>' containing one excerpt for 'src/lib.rs' spanning lines 1-4 with the text 'pub fn run() {}'. [crates/gcode/src/commands/codewiki/text/verify.rs:104-111] |
| `symbols` | function | Returns a one-element 'Vec<SymbolSummary>' describing the 'run\|cli' function symbol, including its function kind, component identifiers/label, source line range '7..=9', and the purpose “Handles command dispatch.” [crates/gcode/src/commands/codewiki/text/verify.rs:113-123] |

_Verified by 11 in-file unit tests._

