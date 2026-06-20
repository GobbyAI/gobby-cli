---
title: crates/gwiki/src/compile/collect.rs
type: code_file
provenance:
- file: crates/gwiki/src/compile/collect.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/compile/collect.rs

Module: [[code/modules/crates/gwiki/src/compile|crates/gwiki/src/compile]]

## Overview

`crates/gwiki/src/compile/collect.rs` exposes 12 indexed API symbols.

## How it fits

`crates/gwiki/src/compile/collect.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `collect_accepted_sources` | function | 'collect_accepted_sources' iterates over 'session.accepted_notes', verifies each note path exists and stays within the session scope, reads and parses the note sections, deduplicates and aggregates citations/conflicting claims/missing evidence, and returns a 'CollectedSources' built from the accepted note metadata and parsed chunks or a 'WikiError' on missing/IO failures. [crates/gwiki/src/compile/collect.rs:10-82] |
| `ParsedNoteSections` | class | 'ParsedNoteSections' is a struct that groups a note’s extracted citation strings, conflicting claims, missing evidence items, and parsed content chunks in separate 'Vec' fields. [crates/gwiki/src/compile/collect.rs:85-90] |
| `ParsedNoteChunk` | class | 'ParsedNoteChunk' is a struct representing a parsed note fragment with its textual content and the byte-range offsets ('byte_start' to 'byte_end') identifying that chunk within the source data. [crates/gwiki/src/compile/collect.rs:93-97] |
| `parse_note_sections` | function | 'parse_note_sections' scans the input text line by line, classifies non-empty trimmed lines into 'citations', 'conflicting_claims', or 'missing_evidence' based on known prefixes, and records all other lines as 'ParsedNoteChunk's with byte offsets for the trimmed content. [crates/gwiki/src/compile/collect.rs:99-127] |
| `body_line_spans` | function | Returns a vector of '(byte_offset, line_slice)' pairs for each line in the text body starting at 'body_start_offset(text)', preserving original offsets while stripping trailing '\n' and optional '\r' from each line. [crates/gwiki/src/compile/collect.rs:129-142] |
| `body_start_offset` | function | Returns the byte offset immediately after the closing '---' line of a leading YAML-style front matter block, or '0' if the text does not start with such a block, and 'text.len()' if no closing delimiter is found. [crates/gwiki/src/compile/collect.rs:144-171] |
| `prefixed_value` | function | Returns the trimmed, non-empty suffix of 'line' after the first case-insensitive matching prefix from 'prefixes', or 'None' if no prefix matches or the suffix is empty. [crates/gwiki/src/compile/collect.rs:173-185] |
| `extend_unique` | function | Appends each string from 'values' to 'target' only if it is not already present in 'target' or in earlier 'values', preserving first occurrence order. [crates/gwiki/src/compile/collect.rs:187-195] |
| `note_path` | function | 'note_path' returns 'path' unchanged if it is absolute, otherwise it resolves the relative 'path' against 'root' by joining them into a 'PathBuf'. [crates/gwiki/src/compile/collect.rs:197-203] |
| `require_path_in_scope` | function | Canonicalizes 'root' and 'path', returns 'Ok(())' only if the canonicalized 'path' is within the canonicalized 'root' prefix, and otherwise returns an I/O error for canonicalization failures or an 'InvalidInput' error indicating the accepted note is outside wiki scope. [crates/gwiki/src/compile/collect.rs:207-239] |

_Verified by 2 in-file unit tests._

