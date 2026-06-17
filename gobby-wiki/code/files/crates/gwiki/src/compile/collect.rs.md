---
title: crates/gwiki/src/compile/collect.rs
type: code_file
provenance:
- file: crates/gwiki/src/compile/collect.rs
  ranges:
  - 10-82
  - 85-90
  - 93-97
  - 99-127
  - 129-142
  - 144-171
  - 173-185
  - 187-195
  - 197-203
  - 207-239
  - 246-269
  - 272-300
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/compile/collect.rs:10-82](crates/gwiki/src/compile/collect.rs#L10-L82), [crates/gwiki/src/compile/collect.rs:85-90](crates/gwiki/src/compile/collect.rs#L85-L90), [crates/gwiki/src/compile/collect.rs:93-97](crates/gwiki/src/compile/collect.rs#L93-L97), [crates/gwiki/src/compile/collect.rs:99-127](crates/gwiki/src/compile/collect.rs#L99-L127), [crates/gwiki/src/compile/collect.rs:129-142](crates/gwiki/src/compile/collect.rs#L129-L142), [crates/gwiki/src/compile/collect.rs:144-171](crates/gwiki/src/compile/collect.rs#L144-L171), [crates/gwiki/src/compile/collect.rs:173-185](crates/gwiki/src/compile/collect.rs#L173-L185), [crates/gwiki/src/compile/collect.rs:187-195](crates/gwiki/src/compile/collect.rs#L187-L195), [crates/gwiki/src/compile/collect.rs:197-203](crates/gwiki/src/compile/collect.rs#L197-L203), [crates/gwiki/src/compile/collect.rs:207-239](crates/gwiki/src/compile/collect.rs#L207-L239), [crates/gwiki/src/compile/collect.rs:246-269](crates/gwiki/src/compile/collect.rs#L246-L269), [crates/gwiki/src/compile/collect.rs:272-300](crates/gwiki/src/compile/collect.rs#L272-L300)

</details>

# crates/gwiki/src/compile/collect.rs

Module: [[code/modules/crates/gwiki/src/compile|crates/gwiki/src/compile]]

## Purpose

Collects accepted research notes for compilation by validating each note path is in scope and exists, reading the file, parsing its structured sections, and assembling `CollectedSources` along with deduplicated citations, conflicting claims, and missing-evidence entries. The helper types and functions break that work into parsing note chunks and line spans, deriving body offsets and prefixed values, enforcing scoped paths, and extending lists without introducing duplicates, with tests covering order-preserving deduplication and not-found handling.
[crates/gwiki/src/compile/collect.rs:10-82]
[crates/gwiki/src/compile/collect.rs:85-90]
[crates/gwiki/src/compile/collect.rs:93-97]
[crates/gwiki/src/compile/collect.rs:99-127]
[crates/gwiki/src/compile/collect.rs:129-142]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `collect_accepted_sources` | function | `pub(crate) fn collect_accepted_sources(` | `collect_accepted_sources [function]` | `23d732c6-84ed-5480-8de1-d8b5557464ac` | 10-82 [crates/gwiki/src/compile/collect.rs:10-82] | Indexed function `collect_accepted_sources` in `crates/gwiki/src/compile/collect.rs`. [crates/gwiki/src/compile/collect.rs:10-82] |
| `ParsedNoteSections` | class | `struct ParsedNoteSections {` | `ParsedNoteSections [class]` | `c4464172-a545-5c35-b5ab-60a55ecef7e3` | 85-90 [crates/gwiki/src/compile/collect.rs:85-90] | Indexed class `ParsedNoteSections` in `crates/gwiki/src/compile/collect.rs`. [crates/gwiki/src/compile/collect.rs:85-90] |
| `ParsedNoteChunk` | class | `struct ParsedNoteChunk {` | `ParsedNoteChunk [class]` | `288abf22-a012-5bd1-9278-2767c732c5fe` | 93-97 [crates/gwiki/src/compile/collect.rs:93-97] | Indexed class `ParsedNoteChunk` in `crates/gwiki/src/compile/collect.rs`. [crates/gwiki/src/compile/collect.rs:93-97] |
| `parse_note_sections` | function | `fn parse_note_sections(text: &str) -> ParsedNoteSections {` | `parse_note_sections [function]` | `baaff445-0c64-5c5d-a2f4-899d7dcee052` | 99-127 [crates/gwiki/src/compile/collect.rs:99-127] | Indexed function `parse_note_sections` in `crates/gwiki/src/compile/collect.rs`. [crates/gwiki/src/compile/collect.rs:99-127] |
| `body_line_spans` | function | `fn body_line_spans(text: &str) -> Vec<(usize, &str)> {` | `body_line_spans [function]` | `8d85d0a8-e16c-5210-ad8c-bfa04bf7dd56` | 129-142 [crates/gwiki/src/compile/collect.rs:129-142] | Indexed function `body_line_spans` in `crates/gwiki/src/compile/collect.rs`. [crates/gwiki/src/compile/collect.rs:129-142] |
| `body_start_offset` | function | `fn body_start_offset(text: &str) -> usize {` | `body_start_offset [function]` | `e7fe4178-31b0-5401-9dcf-ec4d4cc97c51` | 144-171 [crates/gwiki/src/compile/collect.rs:144-171] | Indexed function `body_start_offset` in `crates/gwiki/src/compile/collect.rs`. [crates/gwiki/src/compile/collect.rs:144-171] |
| `prefixed_value` | function | `fn prefixed_value<'a>(line: &'a str, prefixes: &[&str]) -> Option<&'a str> {` | `prefixed_value [function]` | `7487a80f-8096-529f-a1b1-68e8a6df153d` | 173-185 [crates/gwiki/src/compile/collect.rs:173-185] | Indexed function `prefixed_value` in `crates/gwiki/src/compile/collect.rs`. [crates/gwiki/src/compile/collect.rs:173-185] |
| `extend_unique` | function | `pub(crate) fn extend_unique(target: &mut Vec<String>, values: Vec<String>) {` | `extend_unique [function]` | `9486b9f1-345e-50c5-bc7c-7c3cf70dcad4` | 187-195 [crates/gwiki/src/compile/collect.rs:187-195] | Indexed function `extend_unique` in `crates/gwiki/src/compile/collect.rs`. [crates/gwiki/src/compile/collect.rs:187-195] |
| `note_path` | function | `fn note_path(root: &Path, path: &Path) -> PathBuf {` | `note_path [function]` | `86a66327-f657-5f40-9456-73fe29a71bec` | 197-203 [crates/gwiki/src/compile/collect.rs:197-203] | Indexed function `note_path` in `crates/gwiki/src/compile/collect.rs`. [crates/gwiki/src/compile/collect.rs:197-203] |
| `require_path_in_scope` | function | `fn require_path_in_scope(path: &Path, root: &Path) -> Result<(), WikiError> {` | `require_path_in_scope [function]` | `61302e83-d007-53cd-9be3-baedf55045c7` | 207-239 [crates/gwiki/src/compile/collect.rs:207-239] | Indexed function `require_path_in_scope` in `crates/gwiki/src/compile/collect.rs`. [crates/gwiki/src/compile/collect.rs:207-239] |
| `extend_unique_preserves_order_and_removes_existing_or_new_duplicates` | function | `fn extend_unique_preserves_order_and_removes_existing_or_new_duplicates() {` | `extend_unique_preserves_order_and_removes_existing_or_new_duplicates [function]` | `db28a7a8-6630-5489-93fa-ee61cb0d4751` | 246-269 [crates/gwiki/src/compile/collect.rs:246-269] | Indexed function `extend_unique_preserves_order_and_removes_existing_or_new_duplicates` in `crates/gwiki/src/compile/collect.rs`. [crates/gwiki/src/compile/collect.rs:246-269] |
| `missing_accepted_note_returns_not_found` | function | `fn missing_accepted_note_returns_not_found() {` | `missing_accepted_note_returns_not_found [function]` | `cf9ce15c-731a-59cd-80e6-6ce100eda6a7` | 272-300 [crates/gwiki/src/compile/collect.rs:272-300] | Indexed function `missing_accepted_note_returns_not_found` in `crates/gwiki/src/compile/collect.rs`. [crates/gwiki/src/compile/collect.rs:272-300] |
