---
title: crates/gwiki/src/citations.rs
type: code_file
provenance:
- file: crates/gwiki/src/citations.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/citations.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/citations.rs` exposes 9 indexed API symbols.

## How it fits

`crates/gwiki/src/citations.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `render_source_citations` | function | Returns a 'Result' containing a 'Vec<String>' of rendered source citation strings by resolving source records for the given 'source_paths' under 'vault_root' and mapping each record through 'render_source_citation', propagating any 'WikiError' from record lookup. [crates/gwiki/src/citations.rs:6-14] |
| `source_records_for_paths` | function | Reads the source manifest from 'vault_root' and returns either all 'SourceRecord's when 'source_paths' is empty or only the entries whose path matches any requested path, preserving manifest order. [crates/gwiki/src/citations.rs:16-35] |
| `source_record_matches_path` | function | Returns 'true' when the normalized 'entry.location' matches either the normalized 'path' relative to 'vault_root' or the normalized absolute 'path', and 'false' otherwise. [crates/gwiki/src/citations.rs:37-46] |
| `render_source_citation` | function | Builds a citation string from a 'SourceRecord' by choosing 'citation', then 'title', then 'location' as the primary label, optionally adding a 'Source:' line when the primary is not the location, and always appending 'Kind', 'Fetched', optional 'License', and 'Hash' fields before joining the parts. [crates/gwiki/src/citations.rs:48-69] |
| `join_citation_parts` | function | Trims each citation part, skips empties, and concatenates the remaining parts into one string, inserting '. ' between parts unless the current text already ends with sentence punctuation, in which case it inserts a single space. [crates/gwiki/src/citations.rs:71-88] |
| `normalize_path_text` | function | Returns a new 'String' with leading and trailing whitespace removed from 'value' and all backslashes converted to forward slashes. [crates/gwiki/src/citations.rs:90-92] |

_Verified by 3 in-file unit tests._

