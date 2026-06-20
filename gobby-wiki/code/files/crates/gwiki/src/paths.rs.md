---
title: crates/gwiki/src/paths.rs
type: code_file
provenance:
- file: crates/gwiki/src/paths.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/paths.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/paths.rs` exposes 7 indexed API symbols.

## How it fits

`crates/gwiki/src/paths.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `validate_source_id` | function | The 'validate_source_id' function trims and validates a string slice identifier, returning the trimmed slice if it is non-empty and consists strictly of a single, normal path component containing no path separators or directory-traversal elements, or returning an 'InvalidInput' error if validation fails. [crates/gwiki/src/paths.rs:6-22] |
| `raw_source_path` | function | The 'raw_source_path' function validates a string slice identifier and returns a 'PathBuf' pointing to its corresponding markdown file within the 'raw' directory, or a 'WikiError' if validation fails. [crates/gwiki/src/paths.rs:24-27] |
| `derived_markdown_path` | function | This function validates the identifier of a given 'SourceRecord' and, if successful, returns a 'PathBuf' pointing to its corresponding markdown file path at 'knowledge/sources/{id}.md'. [crates/gwiki/src/paths.rs:29-34] |
| `source_record` | function | The 'source_record' function constructs and returns a 'SourceRecord' struct initialized with the provided string slice identifier and a predefined set of mock field values. [crates/gwiki/src/paths.rs:71-86] |

_Verified by 3 in-file unit tests._

