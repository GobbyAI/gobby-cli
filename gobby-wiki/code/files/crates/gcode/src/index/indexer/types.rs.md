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
  - 87-92
  - 94-104
  - 106-108
  - 111-113
  - 116-124
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/index/indexer/types.rs:8-17](crates/gcode/src/index/indexer/types.rs#L8-L17), [crates/gcode/src/index/indexer/types.rs:20-25](crates/gcode/src/index/indexer/types.rs#L20-L25), [crates/gcode/src/index/indexer/types.rs:29-42](crates/gcode/src/index/indexer/types.rs#L29-L42), [crates/gcode/src/index/indexer/types.rs:45-68](crates/gcode/src/index/indexer/types.rs#L45-L68), [crates/gcode/src/index/indexer/types.rs:71-76](crates/gcode/src/index/indexer/types.rs#L71-L76), [crates/gcode/src/index/indexer/types.rs:79-84](crates/gcode/src/index/indexer/types.rs#L79-L84), [crates/gcode/src/index/indexer/types.rs:87-92](crates/gcode/src/index/indexer/types.rs#L87-L92), [crates/gcode/src/index/indexer/types.rs:94-104](crates/gcode/src/index/indexer/types.rs#L94-L104), [crates/gcode/src/index/indexer/types.rs:106-108](crates/gcode/src/index/indexer/types.rs#L106-L108), [crates/gcode/src/index/indexer/types.rs:111-113](crates/gcode/src/index/indexer/types.rs#L111-L113), [crates/gcode/src/index/indexer/types.rs:116-124](crates/gcode/src/index/indexer/types.rs#L116-L124)

</details>

# crates/gcode/src/index/indexer/types.rs

Module: [[code/modules/crates/gcode/src/index/indexer|crates/gcode/src/index/indexer]]

## Purpose

Defines the data types used to drive and report indexing in `gcode`: `IndexRequest` carries the project root, optional path filtering, explicit file selection, and indexing mode flags; `IndexDurations` records timing breakdowns; `IndexDegradation` captures non-fatal indexing problems such as file errors or projection sync/cleanup issues; and `IndexOutcome` aggregates the run’s counts, durations, degradation notes, optional projection sync state, and overlay metadata. `IndexOutcome::new`, `add_counts`, and `set_unsupported_file_types` build up that summary, with `is_zero` used to omit empty tombstone counts from serialization. `UnsupportedFileType` and `FileIndexCounts` model per-extension and per-file counting details that feed into the outcome.
[crates/gcode/src/index/indexer/types.rs:8-17]
[crates/gcode/src/index/indexer/types.rs:20-25]
[crates/gcode/src/index/indexer/types.rs:29-42]
[crates/gcode/src/index/indexer/types.rs:45-68]
[crates/gcode/src/index/indexer/types.rs:71-76]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `IndexRequest` | class | `pub struct IndexRequest {` | `IndexRequest [class]` | `f008b690-f127-5149-ab35-de6fde0893a2` | 8-17 [crates/gcode/src/index/indexer/types.rs:8-17] | Indexed class `IndexRequest` in `crates/gcode/src/index/indexer/types.rs`. [crates/gcode/src/index/indexer/types.rs:8-17] |
| `IndexDurations` | class | `pub struct IndexDurations {` | `IndexDurations [class]` | `59e57725-f26f-5161-91e4-37a99b8855d3` | 20-25 [crates/gcode/src/index/indexer/types.rs:20-25] | Indexed class `IndexDurations` in `crates/gcode/src/index/indexer/types.rs`. [crates/gcode/src/index/indexer/types.rs:20-25] |
| `IndexDegradation` | type | `pub enum IndexDegradation {` | `IndexDegradation [type]` | `d196f3e6-dc4d-5be8-826c-fb269952d95d` | 29-42 [crates/gcode/src/index/indexer/types.rs:29-42] | Indexed type `IndexDegradation` in `crates/gcode/src/index/indexer/types.rs`. [crates/gcode/src/index/indexer/types.rs:29-42] |
| `IndexOutcome` | class | `pub struct IndexOutcome {` | `IndexOutcome [class]` | `d4b4995c-dbf3-5265-9317-bd4c2c318e4a` | 45-68 [crates/gcode/src/index/indexer/types.rs:45-68] | Indexed class `IndexOutcome` in `crates/gcode/src/index/indexer/types.rs`. [crates/gcode/src/index/indexer/types.rs:45-68] |
| `UnsupportedFileType` | class | `pub struct UnsupportedFileType {` | `UnsupportedFileType [class]` | `54396602-75ae-5b77-bc8b-0410746b2566` | 71-76 [crates/gcode/src/index/indexer/types.rs:71-76] | Indexed class `UnsupportedFileType` in `crates/gcode/src/index/indexer/types.rs`. [crates/gcode/src/index/indexer/types.rs:71-76] |
| `OverlayIndexMetadata` | class | `pub struct OverlayIndexMetadata {` | `OverlayIndexMetadata [class]` | `bd704bf0-da3f-5561-b346-73369db80095` | 79-84 [crates/gcode/src/index/indexer/types.rs:79-84] | Indexed class `OverlayIndexMetadata` in `crates/gcode/src/index/indexer/types.rs`. [crates/gcode/src/index/indexer/types.rs:79-84] |
| `IndexOutcome::new` | method | `pub(super) fn new(project_id: &str) -> Self {` | `IndexOutcome::new [method]` | `38f2c05b-417b-542c-aec1-bee3adf7654f` | 87-92 [crates/gcode/src/index/indexer/types.rs:87-92] | Indexed method `IndexOutcome::new` in `crates/gcode/src/index/indexer/types.rs`. [crates/gcode/src/index/indexer/types.rs:87-92] |
| `IndexOutcome::add_counts` | method | `pub(super) fn add_counts(&mut self, counts: FileIndexCounts) {` | `IndexOutcome::add_counts [method]` | `b32fcc3e-3403-585e-8072-a6c6f1261f86` | 94-104 [crates/gcode/src/index/indexer/types.rs:94-104] | Indexed method `IndexOutcome::add_counts` in `crates/gcode/src/index/indexer/types.rs`. [crates/gcode/src/index/indexer/types.rs:94-104] |
| `IndexOutcome::set_unsupported_file_types` | method | `pub(super) fn set_unsupported_file_types(&mut self, unsupported: Vec<UnsupportedFileType>) {` | `IndexOutcome::set_unsupported_file_types [method]` | `bd3b3e97-15cd-5557-a5b6-3769e6a2f397` | 106-108 [crates/gcode/src/index/indexer/types.rs:106-108] | Indexed method `IndexOutcome::set_unsupported_file_types` in `crates/gcode/src/index/indexer/types.rs`. [crates/gcode/src/index/indexer/types.rs:106-108] |
| `is_zero` | function | `fn is_zero(value: &usize) -> bool {` | `is_zero [function]` | `945b3776-c46f-51d5-bddc-b405641cd578` | 111-113 [crates/gcode/src/index/indexer/types.rs:111-113] | Indexed function `is_zero` in `crates/gcode/src/index/indexer/types.rs`. [crates/gcode/src/index/indexer/types.rs:111-113] |
| `FileIndexCounts` | class | `pub(super) struct FileIndexCounts {` | `FileIndexCounts [class]` | `af868d53-8ad5-5409-aa39-c4b7f522ffc9` | 116-124 [crates/gcode/src/index/indexer/types.rs:116-124] | Indexed class `FileIndexCounts` in `crates/gcode/src/index/indexer/types.rs`. [crates/gcode/src/index/indexer/types.rs:116-124] |
