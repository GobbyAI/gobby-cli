---
title: crates/gwiki/src/frontmatter.rs
type: code_file
provenance:
- file: crates/gwiki/src/frontmatter.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/frontmatter.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Overview

`crates/gwiki/src/frontmatter.rs` exposes 31 indexed API symbols.

## How it fits

`crates/gwiki/src/frontmatter.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `FrontmatterFormat` | type | Indexed type `FrontmatterFormat` in `crates/gwiki/src/frontmatter.rs`. [crates/gwiki/src/frontmatter.rs:10-13] |
| `WikiFrontmatter` | class | 'WikiFrontmatter' is a frontmatter metadata container for wiki entries, holding optional canonical fields such as title, source kind, provenance, trust and freshness timestamps, plus arbitrary unrecognized key-value pairs preserved in 'unknown' for round-trip serialization. [crates/gwiki/src/frontmatter.rs:16-30] |
| `WikiFrontmatter::empty` | method | Returns a 'Self' value with all optional fields set to 'None' and all collection fields initialized empty ('Vec::new()'/'BTreeMap::new()'). [crates/gwiki/src/frontmatter.rs:33-48] |
| `WikiFrontmatter::as_json` | method | Builds a JSON 'Value::Object' by cloning all entries from 'self.unknown' and conditionally inserting the struct’s populated fields ('title', non-empty 'aliases'/'tags', 'source_kind', 'captured_from', 'source', 'provenance', 'generated_by', 'trust', etc.) under their corresponding keys. [crates/gwiki/src/frontmatter.rs:51-115] |
| `ParsedFrontmatter` | class | A lifetime-parameterized struct that encapsulates parsed frontmatter data including optional format and byte range information, a borrowed string slice body, and extracted WikiFrontmatter metadata. [crates/gwiki/src/frontmatter.rs:119-125] |
| `FrontmatterError` | class | 'FrontmatterError' is a Rust struct that encapsulates frontmatter parsing or validation failure details in a single 'String' field named 'detail'. [crates/gwiki/src/frontmatter.rs:128-130] |
| `FrontmatterError::fmt` | method | Formats 'self' by delegating to 'write!' and emitting the string representation of 'self.detail' into the provided 'fmt::Formatter'. [crates/gwiki/src/frontmatter.rs:133-135] |
| `parse_frontmatter` | function | Parses frontmatter metadata from a markdown string bounded by delimiters, returning the parsed metadata and body content, or an error if the frontmatter block is unterminated. [crates/gwiki/src/frontmatter.rs:140-170] |
| `mark_stale_markdown` | function | Parses markdown frontmatter, injects 'stale: true' and 'stale_reason' metadata fields, re-serializes the frontmatter in its original format (YAML or TOML), and returns the reconstructed markdown. [crates/gwiki/src/frontmatter.rs:173-191] |
| `FrontmatterError::new` | method | Constructs a new instance by converting an 'Into<String>' parameter to a 'String' and assigning it to the 'detail' field. [crates/gwiki/src/frontmatter.rs:194-198] |
| `OpeningDelimiter` | class | 'OpeningDelimiter' is a struct that stores a frontmatter format, its static opening marker string, and the byte offset where the frontmatter content begins. [crates/gwiki/src/frontmatter.rs:201-205] |
| `opening_delimiter` | function | Parses a markdown string to detect either a YAML ("---") or TOML ("+++") opening frontmatter delimiter, returning an 'OpeningDelimiter' struct containing the format type, marker, and content start position, or 'None' if neither delimiter is found. [crates/gwiki/src/frontmatter.rs:207-221] |
| `delimiter_content_start` | function | This function returns the byte offset where content begins after a marker string if the markdown string starts with that marker followed by a line ending (CRLF or LF), or None otherwise. [crates/gwiki/src/frontmatter.rs:223-232] |
| `find_closing_delimiter` | function | Scans 'markdown' line by line from 'offset' to find a line whose trimmed contents exactly equal 'marker', returning the matched line’s start byte offset and the byte offset immediately after its line ending, or 'None' if no such closing delimiter is found. [crates/gwiki/src/frontmatter.rs:234-264] |
| `parse_metadata` | function | Parses YAML or TOML frontmatter from a raw string and converts it to a 'WikiFrontmatter' object, validating that the parsed value is an object/table. [crates/gwiki/src/frontmatter.rs:266-286] |
| `serialize_yaml_frontmatter` | function | Serializes 'WikiFrontmatter' to a YAML string via 'serde_yaml', removes an optional leading '---\n' and trailing '...\n', ensures the result ends with a newline, and wraps serialization failures in 'FrontmatterError'. [crates/gwiki/src/frontmatter.rs:289-303] |
| `serialize_toml_frontmatter` | function | Serializes 'metadata' to TOML via 'toml::to_string(metadata.as_json())', maps any serialization failure into a 'FrontmatterError', and ensures the returned string ends with a trailing newline. [crates/gwiki/src/frontmatter.rs:306-314] |
| `parse_yaml` | function | Parses a YAML frontmatter string into a 'serde_json::Value', returning an empty object for blank input and wrapping YAML parse or JSON conversion failures in 'FrontmatterError'. [crates/gwiki/src/frontmatter.rs:316-329] |
| `parse_toml` | function | Parses a TOML frontmatter string into a 'serde_json::Value', returning an empty object for blank input and wrapping TOML parse or JSON conversion failures in 'FrontmatterError'. [crates/gwiki/src/frontmatter.rs:331-344] |
| `frontmatter_from_object` | function | Builds a 'WikiFrontmatter' by extracting and type-converting known keys from a 'Map<String, Value>' ('title', 'aliases', 'tags', 'source_kind'/'kind', 'source', 'captured_from', provenance/generation/trust/freshness/indexed_at), defaulting missing list fields to empty and preserving all unrecognized entries in 'unknown'. [crates/gwiki/src/frontmatter.rs:346-394] |
| `string_value` | function | Extracts an optional String from a Value by applying 'as_str()' and then chaining the result to the 'string_value_str' function via monadic bind. [crates/gwiki/src/frontmatter.rs:396-398] |
| `string_list` | function | Converts a 'Value' reference into a 'Vec<String>' by extracting string elements via 'string_value_str' for String variants, filtering and mapping array elements through 'string_value' for Array variants, or returning an empty vector for other types. [crates/gwiki/src/frontmatter.rs:400-406] |
| `string_value_str` | function | This function returns an 'Option<String>' containing an owned copy of the whitespace-trimmed input string if non-empty, or 'None' if the trimmed value is empty. [crates/gwiki/src/frontmatter.rs:408-415] |
| `tag_list` | function | Parses a 'Value' into a normalized 'Vec<String>' of tags by splitting comma/whitespace-delimited strings or filtering array elements, with leading '#' characters and empty tags removed. [crates/gwiki/src/frontmatter.rs:419-434] |

_1 more symbol(s) not shown — run `gcode outline crates/gwiki/src/frontmatter.rs` for the full list._

_Verified by 6 in-file unit tests._

