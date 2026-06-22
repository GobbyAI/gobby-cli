---
title: crates/gcode/src/models.rs
type: code_file
provenance:
- file: crates/gcode/src/models.rs
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/models.rs

Module: [[code/modules/crates/gcode/src|crates/gcode/src]]

## Overview

`crates/gcode/src/models.rs` exposes 51 indexed API symbols.

## How it fits

`crates/gcode/src/models.rs` is documented from its indexed symbols; see the Reference table below and the module page for how it connects to sibling files.

## Reference

| Symbol | Kind | Purpose |
| --- | --- | --- |
| `ProjectionProvenance` | type | Indexed type `ProjectionProvenance` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:19-24] |
| `ProjectionProvenance::as_str` | method | Returns a '&'static str' by matching the enum variant and mapping 'Extracted', 'Inferred', and 'Ambiguous' to the string literals '"EXTRACTED"', '"INFERRED"', and '"AMBIGUOUS"' respectively. [crates/gcode/src/models.rs:27-33] |
| `ProjectionProvenance::from_wire_value` | method | Parses a string wire value case-insensitively for '"EXTRACTED"', '"INFERRED"', or '"AMBIGUOUS"' and returns the corresponding 'Self' variant, otherwise 'None'. [crates/gcode/src/models.rs:35-42] |
| `ProjectionProvenance::fmt` | method | Implements 'Display' formatting by writing the string slice returned by 'self.as_str()' directly into the provided formatter. [crates/gcode/src/models.rs:46-48] |
| `ProjectionMetadata` | class | 'ProjectionMetadata' is a serializable Rust struct that records a projection’s provenance, optional confidence, originating system, and optional source location and matching details. [crates/gcode/src/models.rs:53-66] |
| `ProjectionMetadata::new` | method | Constructs a 'Self' value from the given 'ProjectionProvenance' and 'source_system', initializing 'confidence', 'source_file_path', 'source_line', 'source_symbol_id', and 'matching_method' to 'None'. [crates/gcode/src/models.rs:69-79] |
| `ProjectionMetadata::gcode_extracted` | method | Constructs a new instance tagged with 'ProjectionProvenance::Extracted' and 'SOURCE_SYSTEM_GCODE', then sets its confidence to 'Some(1.0)'. [crates/gcode/src/models.rs:81-83] |
| `ProjectionMetadata::inferred` | method | Constructs a new provenance value marked 'ProjectionProvenance::Inferred' for the given 'source_system', then attaches the optional 'confidence' via 'with_confidence'. [crates/gcode/src/models.rs:85-87] |
| `ProjectionMetadata::ambiguous` | method | Creates a new 'Self' with 'ProjectionProvenance::Ambiguous' and the given 'source_system', then applies the optional 'confidence' via 'with_confidence'. [crates/gcode/src/models.rs:89-91] |
| `ProjectionMetadata::with_confidence` | method | Sets the 'confidence' field on 'self' to the provided 'Option<f64>' value and returns the updated instance. [crates/gcode/src/models.rs:93-96] |
| `ProjectionMetadata::with_source_file_path` | method | Sets 'self.source_file_path' to 'Some(file_path.into())' and returns the updated builder instance. [crates/gcode/src/models.rs:98-101] |
| `ProjectionMetadata::with_source_line` | method | Returns 'self' after setting 'self.source_line' to 'Some(line)', enabling a builder-style update of the source line field. [crates/gcode/src/models.rs:103-106] |
| `ProjectionMetadata::with_source_symbol_id` | method | Sets 'self.source_symbol_id' to 'Some(symbol_id.into())' and returns the updated builder instance. [crates/gcode/src/models.rs:108-111] |
| `ProjectionMetadata::with_matching_method` | method | Sets 'self.matching_method' to 'Some(matching_method.into())' and returns the updated builder by value. [crates/gcode/src/models.rs:113-116] |
| `ProjectionMetadata::is_hypothesis` | method | Returns 'true' when 'self.provenance' is either 'ProjectionProvenance::Inferred' or 'ProjectionProvenance::Ambiguous', and 'false' otherwise. [crates/gcode/src/models.rs:118-123] |
| `Symbol` | class | 'Symbol' is a serialized metadata record for a code symbol, capturing its identity, project and file location, qualified naming, kind and language, byte/line ranges, optional signature/docstring/parent linkage/summary, and content hash with creation and update timestamps. [crates/gcode/src/models.rs:128-154] |
| `Symbol::make_id` | method | Constructs a deterministic UUID v5 string by hashing the concatenated 'project_id', 'file_path', 'name', 'kind', and 'byte_start' under 'CODE_INDEX_UUID_NAMESPACE'. [crates/gcode/src/models.rs:159-168] |
| `Symbol::from_row` | method | Constructs 'Self' from a database 'Row' by extracting each column with 'try_get', converting the position fields from 'i64' to 'usize', and defaulting missing 'content_hash', 'created_at', and 'updated_at' values to empty strings, returning any conversion or lookup error via 'anyhow::Result'. [crates/gcode/src/models.rs:174-201] |
| `Symbol::to_outline` | method | Returns a new 'OutlineSymbol' by cloning 'id', 'name', 'kind', and 'signature' from 'self' and copying the 'line_start' and 'line_end' fields. [crates/gcode/src/models.rs:204-213] |
| `Symbol::to_brief` | method | Creates and returns a 'SearchResult' by cloning the object's identifying, location, summary, and signature fields, copying line bounds, and resetting ranking/source metadata to 'score: 0.0', 'rrf_score: None', and 'sources: None'. [crates/gcode/src/models.rs:216-232] |
| `make_unresolved_callee_id` | function | Generates a deterministic UUIDv5 string in the 'CODE_INDEX_UUID_NAMESPACE' from the namespaced key 'unresolved:{project_id}:{callee_name}' to identify an unresolved callee. [crates/gcode/src/models.rs:235-238] |
| `make_external_symbol_id` | function | Generates a deterministic UUIDv5 string in the 'CODE_INDEX_UUID_NAMESPACE' from the concatenated key 'external:{project_id}:{module_or_empty}:{callee_name}', using an empty string when 'module' is 'None'. [crates/gcode/src/models.rs:240-248] |
| `IndexedFile` | class | 'IndexedFile' is a metadata record for an indexed source file, storing its identifiers, path, language, content hash, symbol count, byte size, and indexing timestamp. [crates/gcode/src/models.rs:252-261] |
| `IndexedFile::make_id` | method | Generates a deterministic UUID v5 string by hashing the 'project_id:file_path' key with 'CODE_INDEX_UUID_NAMESPACE'. [crates/gcode/src/models.rs:264-267] |

_22 more symbol(s) not shown — run `gcode outline crates/gcode/src/models.rs` for the full list._

_Verified by 5 in-file unit tests._

