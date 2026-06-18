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

`crates/gcode/src/models.rs` is documented from its indexed symbols; see the Key components below and the module page for how it connects to sibling files.

## Key components

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
| `ContentChunk` | class | 'ContentChunk' is a data struct representing a persisted file fragment within a project, identified by 'id' and 'project_id', with source location metadata ('file_path', 'chunk_index', 'line_start', 'line_end'), textual 'content', 'language', and a 'created_at' timestamp. [crates/gcode/src/models.rs:272-282] |
| `ContentChunk::make_id` | method | 'make_id' deterministically generates a UUID v5 string from the concatenated 'project_id', 'file_path', and 'chunk_index' using a fixed 'CODE_INDEX_UUID_NAMESPACE' as the namespace. [crates/gcode/src/models.rs:285-288] |
| `ImportRelation` | class | 'ImportRelation' is a Rust struct that models a relation between an imported module and its source file via two owned 'String' fields: 'file_path' and 'module_name'. [crates/gcode/src/models.rs:293-296] |
| `CallTargetKind` | type | Indexed type `CallTargetKind` in `crates/gcode/src/models.rs`. [crates/gcode/src/models.rs:300-310] |
| `CallTargetKind::as_str` | method | Returns the canonical ''static' string identifier for the enum variant, mapping 'Symbol' to '"symbol"', 'Unresolved' to '"unresolved"', 'External' to '"external"', and 'LocalImport' to '"local_import"'. [crates/gcode/src/models.rs:313-320] |
| `CallRelation` | class | 'CallRelation' models a call-site relationship by recording the caller symbol ID, an optional callee symbol ID, the callee name and target kind, an optional external module for the callee, and the source file path and line number where the call occurs. [crates/gcode/src/models.rs:325-333] |
| `CallRelation::new` | method | Constructs a 'Self' call-record with the given caller symbol ID, callee name, file path, and line number, initializing the callee as unresolved with no callee symbol ID or external module. [crates/gcode/src/models.rs:336-351] |
| `CallRelation::with_symbol_target` | method | Sets 'self.callee_symbol_id' to 'Some(callee_symbol_id)', marks 'self.callee_target_kind' as 'CallTargetKind::Symbol', and returns the updated 'Self'. [crates/gcode/src/models.rs:353-357] |
| `CallRelation::with_external_target` | method | Sets the callee name, marks the call target as 'External', stores the provided external module in 'callee_external_module', and returns the updated builder/state. [crates/gcode/src/models.rs:359-368] |
| `CallRelation::with_local_import_target` | method | Sets the callee metadata to a local-import call target by recording the provided 'callee_name', clearing any symbol ID, and storing the candidate file paths joined with 'LOCAL_IMPORT_CANDIDATE_SEP' in 'callee_external_module'. [crates/gcode/src/models.rs:382-392] |
| `CallRelation::with_local_default_import_target` | method | Sets the call target to a local import by recording the callee name, clearing any symbol ID, and encoding the default export marker plus candidate file list into 'callee_external_module' as a separator-joined string. [crates/gcode/src/models.rs:394-408] |
| `CallRelation::local_import_uses_default_export_fallback` | method | Returns 'true' only when the call target is a 'LocalImport' and the callee’s external module string begins with 'LOCAL_IMPORT_DEFAULT_EXPORT_MARKER' before the 'LOCAL_IMPORT_CANDIDATE_SEP' delimiter, indicating a default-export fallback import. [crates/gcode/src/models.rs:410-417] |
| `CallRelation::local_import_candidate_files` | method | Returns the candidate file names for a 'LocalImport' call target by splitting 'callee_external_module' on 'LOCAL_IMPORT_CANDIDATE_SEP', discarding empty segments and the 'LOCAL_IMPORT_DEFAULT_EXPORT_MARKER', and otherwise returning an empty 'Vec<String>'. [crates/gcode/src/models.rs:421-435] |
| `IndexedProject` | class | 'IndexedProject' is a serializable Rust struct that records an indexed project’s identity, root path, file and symbol counts, last indexing timestamp, indexing duration in milliseconds, and an optional count of eligible files. [crates/gcode/src/models.rs:446-455] |
| `SearchResult` | class | 'SearchResult' is a serializable Rust struct that represents a code-search hit with identifiers, symbol metadata, file location, relevance scores, and optional summary, signature, and source references. [crates/gcode/src/models.rs:459-477] |
| `GraphResult` | class | 'GraphResult' is a serializable Rust struct representing a graph projection result with node identity and source-location fields ('id', 'name', 'file_path', 'line') plus optional edge/context metadata ('confidence', 'relation', 'distance', 'metadata'). [crates/gcode/src/models.rs:481-495] |
| `GraphPathStep` | class | 'GraphPathStep' is a data structure that represents a single step in a graph path, carrying its ordinal position along with the node 'id', display 'name', source 'file_path', and source 'line' number. [crates/gcode/src/models.rs:498-504] |
| `ParseResult` | class | 'ParseResult' is a data container holding the parsed symbols, import relations, call relations, and the original file bytes used later for body-snippet extraction. [crates/gcode/src/models.rs:507-513] |
| `IndexResult` | class | 'IndexResult' is a struct that summarizes an indexing run with the project identifier, counts of indexed and skipped files, number of symbols found, a list of error messages, and the elapsed duration in milliseconds. [crates/gcode/src/models.rs:517-524] |
| `PagedResponse` | class | 'PagedResponse<T>' is a generic serializable pagination container that holds a project identifier, total result count, current offset and limit, a vector of page items, and an optional serialization-skipped hint string. [crates/gcode/src/models.rs:529-537] |
| `OutlineSymbol` | class | 'OutlineSymbol' is a serializable Rust struct that identifies an outlined code symbol by 'id', 'name', 'kind', and source line range ('line_start' to 'line_end'), with an optional 'signature' field omitted during serialization when 'None'. [crates/gcode/src/models.rs:541-549] |
| `ContentSearchHit` | class | 'ContentSearchHit' represents a serialized search result hit containing a file path, inclusive line-range bounds, a text snippet, and an optional language tag. [crates/gcode/src/models.rs:553-560] |
| `symbol_make_id_matches_python_uuid5_golden_vectors` | function | Verifies that 'CODE_INDEX_UUID_NAMESPACE' and 'Symbol::make_id(project_id, file_path, name, kind, byte_start)' exactly match Python UUID5 golden-vector outputs for several representative symbol inputs. [crates/gcode/src/models.rs:567-615] |
| `unresolved_and_external_ids_match_python_uuid5_golden_vectors` | function | Verifies that 'make_unresolved_callee_id' and 'make_external_symbol_id' produce UUID5 strings matching fixed Python golden vectors for a missing function and two external symbol cases, with and without a module name. [crates/gcode/src/models.rs:618-631] |
| `test_call_relation_promotes_symbol_targets` | function | Verifies that 'CallRelation::with_symbol_target' sets 'callee_symbol_id' to the provided symbol ID and changes 'callee_target_kind' to 'CallTargetKind::Symbol'. [crates/gcode/src/models.rs:633-644] |
| `graph_result_metadata_remains_optional_in_json_contract` | function | Verifies that 'GraphResult' JSON can be deserialized without a 'metadata' field, defaults 'confidence' to 'ProjectionProvenance::Extracted', and reserializes without emitting 'metadata' while preserving 'confidence' as '"EXTRACTED"'. [crates/gcode/src/models.rs:647-663] |
| `graph_result_without_metadata_omits_metadata_when_serialized` | function | Uses property-based testing to verify that serializing a 'GraphResult' with 'metadata: None' produces JSON containing the expected '"confidence": "EXTRACTED"' field and omits the 'metadata' field entirely. [crates/gcode/src/models.rs:666-702] |

