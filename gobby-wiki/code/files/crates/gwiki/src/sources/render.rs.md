---
title: crates/gwiki/src/sources/render.rs
type: code_file
provenance:
- file: crates/gwiki/src/sources/render.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/sources/render.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/sources/render.rs` exposes 17 indexed API symbols.

## How it fits

`crates/gwiki/src/sources/render.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `render_entry` | function | Serializes a 'SourceRecord' to JSON and appends a Markdown index entry for it to 'index', including escaped title/location, metadata fields, optional citation/license lines, and an embedded source marker, returning a 'WikiError::Json' if serialization fails. [crates/gwiki/src/sources/render.rs:15-45] |
| `canonicalize_location` | function | Returns a normalized location string by stripping any fragment, lowercasing the URL scheme and authority, sorting and separating the query, removing redundant trailing slashes from the path, and then recombining the base with the query if present. [crates/gwiki/src/sources/render.rs:47-58] |
| `split_sorted_query` | function | Splits 'location' at the first '?', returning the base path as a 'String' and, if present, a 'Some' containing the '&'-joined query parameters sorted lexicographically with empty parameters removed, otherwise 'None'. [crates/gwiki/src/sources/render.rs:60-70] |
| `PreservedSourceIndex` | class | 'PreservedSourceIndex' is an internal struct that stores two 'String' segments, 'prefix' and 'suffix', representing preserved source text around an index. [crates/gwiki/src/sources/render.rs:72-75] |
| `existing_index_without_manifest` | function | Returns a 'PreservedSourceIndex' by reading an existing raw source index file and splitting out any generated source-manifest section so the surrounding preserved prefix and suffix can be reused, or falls back to a default '# Raw Sources\n\n' prefix when the file is missing. [crates/gwiki/src/sources/render.rs:77-124] |
| `normalize_preserved_index_prefix` | function | Trims trailing newlines from 'prefix', replaces an empty-or-whitespace-only result with '"# Raw Sources"', then appends two newline characters and returns the normalized string. [crates/gwiki/src/sources/render.rs:126-133] |
| `normalize_preserved_index_suffix` | function | Returns a 'String' with any leading newline characters removed from 'suffix', leaving all other characters unchanged. [crates/gwiki/src/sources/render.rs:135-137] |
| `suffix_after_unmarked_manifest` | function | Returns the normalized substring of 'existing' that follows the first subsequent '\n## ' section marker after the '"## Source manifest"' header, or an empty string if no such marker exists. [crates/gwiki/src/sources/render.rs:139-145] |
| `lower_url_scheme_and_authority` | function | Returns a normalized URL string by lowercasing the scheme and authority when a '://' separator is present, otherwise replacing backslashes with forward slashes and leaving the rest unchanged. [crates/gwiki/src/sources/render.rs:147-166] |
| `source_id` | function | Builds a Markdown-friendly source ID by taking a hash prefix from 'content_hash' (or a sentinel when empty), slugifying 'canonical_location' to 48 characters, and formatting 'src-{prefix}' or 'src-{prefix}-{slug}' depending on whether the slug is empty. [crates/gwiki/src/sources/render.rs:168-183] |
| `escape_markdown_text` | function | Returns a new string with normalized newlines and backslashes, '[' and ']' escaped for Markdown by prefixing each with a backslash. [crates/gwiki/src/sources/render.rs:185-190] |
| `escape_markdown_destination` | function | Returns a 'String' with normalized newlines where backslashes are doubled and literal '(' and ')' characters are escaped with backslashes for safe Markdown destination formatting. [crates/gwiki/src/sources/render.rs:192-197] |
| `inline_text` | function | Returns a new 'String' with all newline variants normalized and all runs of whitespace collapsed to single spaces by splitting on whitespace and joining with '" "'. [crates/gwiki/src/sources/render.rs:199-204] |
| `normalize_newlines` | function | Returns a new 'String' in which all Windows CRLF sequences ('\r\n') and any remaining standalone carriage returns ('\r') are converted to Unix line feeds ('\n'). [crates/gwiki/src/sources/render.rs:206-208] |

_Verified by 3 in-file unit tests._

