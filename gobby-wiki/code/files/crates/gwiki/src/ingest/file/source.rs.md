---
title: crates/gwiki/src/ingest/file/source.rs
type: code_file
provenance:
- file: crates/gwiki/src/ingest/file/source.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/ingest/file/source.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/ingest/file/source.rs` exposes 4 indexed API symbols.

## How it fits

`crates/gwiki/src/ingest/file/source.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `detect_source_kind` | function | The 'detect_source_kind' function determines a file's type by matching its lowercase extension against predefined categories to return the corresponding 'SourceKind' enum variant, defaulting to 'SourceKind::File'. [crates/gwiki/src/ingest/file/source.rs:9-25] |
| `source_location` | function | This function returns a forward-slash-standardized, relative string representation of a file path by stripping the specified vault root prefix from either the direct or canonicalized path, falling back to the full path if stripping fails. [crates/gwiki/src/ingest/file/source.rs:27-41] |
| `should_store_asset` | function | The 'should_store_asset' function returns 'true' if the source kind is text and its byte length exceeds 'TEXT_INLINE_LIMIT_BYTES', or if it matches any non-text asset type (specifically audio, image, video, PDF, office, HTML, or file). [crates/gwiki/src/ingest/file/source.rs:43-55] |
| `read_source_file` | function | The 'read_source_file' function reads the byte contents of a file at the specified path and returns them as a vector, mapping any standard I/O error into a custom 'WikiError::Io' error containing path and action metadata. [crates/gwiki/src/ingest/file/source.rs:57-63] |

