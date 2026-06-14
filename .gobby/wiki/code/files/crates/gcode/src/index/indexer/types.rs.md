---
title: crates/gcode/src/index/indexer/types.rs
type: code_file
provenance:
- file: crates/gcode/src/index/indexer/types.rs
  ranges:
  - 8-17
  - 20-25
  - 29-42
  - 45-68
  - 71-76
  - 79-84
  - 86-109
  - 111-113
  - 116-124
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/index/indexer/types.rs

Module: [[code/modules/crates/gcode/src/index/indexer|crates/gcode/src/index/indexer]]

## Purpose

This file defines the core data structures for the code indexing subsystem. IndexRequest specifies indexing parameters including project root, path filters, and control flags for depth, C++ semantics, and projection sync. IndexOutcome is the primary result struct that aggregates comprehensive metrics from an indexing operation—file counts (scanned, indexed, skipped), indexed entity counts (symbols, imports, calls), processing timings via IndexDurations, unsupported file types, and optional degradation diagnostics and projection sync status. Supporting types include IndexDegradation (an enum for various indexing failures), FileIndexCounts (per-file statistics), UnsupportedFileType (tracking unsupported extensions), and OverlayIndexMetadata (project reference metadata). These types work together to configure indexing operations and serialize complete indexing results with detailed metrics and diagnostics.
[crates/gcode/src/index/indexer/types.rs:8-17]
[crates/gcode/src/index/indexer/types.rs:20-25]
[crates/gcode/src/index/indexer/types.rs:29-42]
[crates/gcode/src/index/indexer/types.rs:45-68]
[crates/gcode/src/index/indexer/types.rs:71-76]

## API Symbols

- `IndexRequest` (class) component `IndexRequest [class]` (`f008b690-f127-5149-ab35-de6fde0893a2`) lines 8-17 [crates/gcode/src/index/indexer/types.rs:8-17]
  - Signature: `pub struct IndexRequest {`
  - Purpose: IndexRequest is a configuration struct that specifies project indexing parameters including a root directory, optional path filter, explicit files, and boolean flags controlling full indexing depth, C++ semantics requirement, and projection synchronization. [crates/gcode/src/index/indexer/types.rs:8-17]
- `IndexDurations` (class) component `IndexDurations [class]` (`59e57725-f26f-5161-91e4-37a99b8855d3`) lines 20-25 [crates/gcode/src/index/indexer/types.rs:20-25]
  - Signature: `pub struct IndexDurations {`
  - Purpose: `IndexDurations` is a struct that aggregates timing measurements in milliseconds for the discovery, indexing, statistics, and total execution phases of an indexing operation. [crates/gcode/src/index/indexer/types.rs:20-25]
- `IndexDegradation` (type) component `IndexDegradation [type]` (`d196f3e6-dc4d-5be8-826c-fb269952d95d`) lines 29-42 [crates/gcode/src/index/indexer/types.rs:29-42]
  - Signature: `pub enum IndexDegradation {`
  - Purpose: Indexed type `IndexDegradation` in `crates/gcode/src/index/indexer/types.rs`. [crates/gcode/src/index/indexer/types.rs:29-42]
- `IndexOutcome` (class) component `IndexOutcome [class]` (`d4b4995c-dbf3-5265-9317-bd4c2c318e4a`) lines 45-68 [crates/gcode/src/index/indexer/types.rs:45-68]
  - Signature: `pub struct IndexOutcome {`
  - Purpose: `IndexOutcome` is a struct that encapsulates comprehensive metrics and diagnostics from a code indexing operation, including file statistics (scanned, indexed, skipped), indexed entity counts (symbols, imports, calls), processing durations, unsupported file types, and optional synchronization status. [crates/gcode/src/index/indexer/types.rs:45-68]
- `UnsupportedFileType` (class) component `UnsupportedFileType [class]` (`54396602-75ae-5b77-bc8b-0410746b2566`) lines 71-76 [crates/gcode/src/index/indexer/types.rs:71-76]
  - Signature: `pub struct UnsupportedFileType {`
  - Purpose: `UnsupportedFileType` is a serializable struct that records an unsupported file extension, the count of files with that extension, and an optional list of example filenames that is omitted from serialization if empty. [crates/gcode/src/index/indexer/types.rs:71-76]
- `OverlayIndexMetadata` (class) component `OverlayIndexMetadata [class]` (`bd704bf0-da3f-5561-b346-73369db80095`) lines 79-84 [crates/gcode/src/index/indexer/types.rs:79-84]
  - Signature: `pub struct OverlayIndexMetadata {`
  - Purpose: `OverlayIndexMetadata` is a metadata struct that maintains bidirectional project references by storing the identifiers and root paths for both an overlay project and its parent project. [crates/gcode/src/index/indexer/types.rs:79-84]
- `IndexOutcome` (class) component `IndexOutcome [class]` (`bff99496-be66-54ac-a7e1-7b51f6553e86`) lines 86-109 [crates/gcode/src/index/indexer/types.rs:86-109]
  - Signature: `impl IndexOutcome {`
  - Purpose: IndexOutcome accumulates code indexing metrics (file count, symbols, imports, calls, unresolved targets, chunks) and metadata (indexed file paths, unsupported file types) for a project. [crates/gcode/src/index/indexer/types.rs:86-109]
- `IndexOutcome.new` (method) component `IndexOutcome.new [method]` (`38f2c05b-417b-542c-aec1-bee3adf7654f`) lines 87-92 [crates/gcode/src/index/indexer/types.rs:87-92]
  - Signature: `pub(super) fn new(project_id: &str) -> Self {`
  - Purpose: Creates a new instance by converting the project ID string reference to an owned String and initializing all other fields to their default values. [crates/gcode/src/index/indexer/types.rs:87-92]
- `IndexOutcome.add_counts` (method) component `IndexOutcome.add_counts [method]` (`b32fcc3e-3403-585e-8072-a6c6f1261f86`) lines 94-104 [crates/gcode/src/index/indexer/types.rs:94-104]
  - Signature: `pub(super) fn add_counts(&mut self, counts: FileIndexCounts) {`
  - Purpose: Accumulates indexing metrics from a `FileIndexCounts` struct into the current instance and conditionally appends the indexed file path when files were processed. [crates/gcode/src/index/indexer/types.rs:94-104]
- `IndexOutcome.set_unsupported_file_types` (method) component `IndexOutcome.set_unsupported_file_types [method]` (`bd3b3e97-15cd-5557-a5b6-3769e6a2f397`) lines 106-108 [crates/gcode/src/index/indexer/types.rs:106-108]
  - Signature: `pub(super) fn set_unsupported_file_types(&mut self, unsupported: Vec<UnsupportedFileType>) {`
  - Purpose: Sets the `unsupported_file_types` field to the provided vector of `UnsupportedFileType` via a crate-private setter method. [crates/gcode/src/index/indexer/types.rs:106-108]
- `is_zero` (function) component `is_zero [function]` (`945b3776-c46f-51d5-bddc-b405641cd578`) lines 111-113 [crates/gcode/src/index/indexer/types.rs:111-113]
  - Signature: `fn is_zero(value: &usize) -> bool {`
  - Purpose: Returns `true` if the dereferenced `usize` reference equals zero, `false` otherwise. [crates/gcode/src/index/indexer/types.rs:111-113]
- `FileIndexCounts` (class) component `FileIndexCounts [class]` (`af868d53-8ad5-5409-aa39-c4b7f522ffc9`) lines 116-124 [crates/gcode/src/index/indexer/types.rs:116-124]
  - Signature: `pub(super) struct FileIndexCounts {`
  - Purpose: `FileIndexCounts` aggregates indexing statistics for a file path, tracking counts of indexed files, symbols, imports, calls, unresolved targets, and chunks. [crates/gcode/src/index/indexer/types.rs:116-124]

