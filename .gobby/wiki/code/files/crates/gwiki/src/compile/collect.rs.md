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

# crates/gwiki/src/compile/collect.rs

Module: [[code/modules/crates/gwiki/src/compile|crates/gwiki/src/compile]]

## Purpose

`crates/gwiki/src/compile/collect.rs` exposes 12 indexed API symbols.
[crates/gwiki/src/compile/collect.rs:10-82]
[crates/gwiki/src/compile/collect.rs:85-90]
[crates/gwiki/src/compile/collect.rs:93-97]
[crates/gwiki/src/compile/collect.rs:99-127]
[crates/gwiki/src/compile/collect.rs:129-142]
[crates/gwiki/src/compile/collect.rs:144-171]
[crates/gwiki/src/compile/collect.rs:173-185]
[crates/gwiki/src/compile/collect.rs:187-195]
[crates/gwiki/src/compile/collect.rs:197-203]
[crates/gwiki/src/compile/collect.rs:207-239]
[crates/gwiki/src/compile/collect.rs:246-269]
[crates/gwiki/src/compile/collect.rs:272-300]

## API Symbols

- `collect_accepted_sources` (function) component `collect_accepted_sources [function]` (`23d732c6-84ed-5480-8de1-d8b5557464ac`) lines 10-82 [crates/gwiki/src/compile/collect.rs:10-82]
  - Signature: `pub(crate) fn collect_accepted_sources(`
  - Purpose: Indexed function `collect_accepted_sources` in `crates/gwiki/src/compile/collect.rs`. [crates/gwiki/src/compile/collect.rs:10-82]
- `ParsedNoteSections` (class) component `ParsedNoteSections [class]` (`c4464172-a545-5c35-b5ab-60a55ecef7e3`) lines 85-90 [crates/gwiki/src/compile/collect.rs:85-90]
  - Signature: `struct ParsedNoteSections {`
  - Purpose: Indexed class `ParsedNoteSections` in `crates/gwiki/src/compile/collect.rs`. [crates/gwiki/src/compile/collect.rs:85-90]
- `ParsedNoteChunk` (class) component `ParsedNoteChunk [class]` (`288abf22-a012-5bd1-9278-2767c732c5fe`) lines 93-97 [crates/gwiki/src/compile/collect.rs:93-97]
  - Signature: `struct ParsedNoteChunk {`
  - Purpose: Indexed class `ParsedNoteChunk` in `crates/gwiki/src/compile/collect.rs`. [crates/gwiki/src/compile/collect.rs:93-97]
- `parse_note_sections` (function) component `parse_note_sections [function]` (`baaff445-0c64-5c5d-a2f4-899d7dcee052`) lines 99-127 [crates/gwiki/src/compile/collect.rs:99-127]
  - Signature: `fn parse_note_sections(text: &str) -> ParsedNoteSections {`
  - Purpose: Indexed function `parse_note_sections` in `crates/gwiki/src/compile/collect.rs`. [crates/gwiki/src/compile/collect.rs:99-127]
- `body_line_spans` (function) component `body_line_spans [function]` (`8d85d0a8-e16c-5210-ad8c-bfa04bf7dd56`) lines 129-142 [crates/gwiki/src/compile/collect.rs:129-142]
  - Signature: `fn body_line_spans(text: &str) -> Vec<(usize, &str)> {`
  - Purpose: Indexed function `body_line_spans` in `crates/gwiki/src/compile/collect.rs`. [crates/gwiki/src/compile/collect.rs:129-142]
- `body_start_offset` (function) component `body_start_offset [function]` (`e7fe4178-31b0-5401-9dcf-ec4d4cc97c51`) lines 144-171 [crates/gwiki/src/compile/collect.rs:144-171]
  - Signature: `fn body_start_offset(text: &str) -> usize {`
  - Purpose: Indexed function `body_start_offset` in `crates/gwiki/src/compile/collect.rs`. [crates/gwiki/src/compile/collect.rs:144-171]
- `prefixed_value` (function) component `prefixed_value [function]` (`7487a80f-8096-529f-a1b1-68e8a6df153d`) lines 173-185 [crates/gwiki/src/compile/collect.rs:173-185]
  - Signature: `fn prefixed_value<'a>(line: &'a str, prefixes: &[&str]) -> Option<&'a str> {`
  - Purpose: Indexed function `prefixed_value` in `crates/gwiki/src/compile/collect.rs`. [crates/gwiki/src/compile/collect.rs:173-185]
- `extend_unique` (function) component `extend_unique [function]` (`9486b9f1-345e-50c5-bc7c-7c3cf70dcad4`) lines 187-195 [crates/gwiki/src/compile/collect.rs:187-195]
  - Signature: `pub(crate) fn extend_unique(target: &mut Vec<String>, values: Vec<String>) {`
  - Purpose: Indexed function `extend_unique` in `crates/gwiki/src/compile/collect.rs`. [crates/gwiki/src/compile/collect.rs:187-195]
- `note_path` (function) component `note_path [function]` (`86a66327-f657-5f40-9456-73fe29a71bec`) lines 197-203 [crates/gwiki/src/compile/collect.rs:197-203]
  - Signature: `fn note_path(root: &Path, path: &Path) -> PathBuf {`
  - Purpose: Indexed function `note_path` in `crates/gwiki/src/compile/collect.rs`. [crates/gwiki/src/compile/collect.rs:197-203]
- `require_path_in_scope` (function) component `require_path_in_scope [function]` (`61302e83-d007-53cd-9be3-baedf55045c7`) lines 207-239 [crates/gwiki/src/compile/collect.rs:207-239]
  - Signature: `fn require_path_in_scope(path: &Path, root: &Path) -> Result<(), WikiError> {`
  - Purpose: Indexed function `require_path_in_scope` in `crates/gwiki/src/compile/collect.rs`. [crates/gwiki/src/compile/collect.rs:207-239]
- `extend_unique_preserves_order_and_removes_existing_or_new_duplicates` (function) component `extend_unique_preserves_order_and_removes_existing_or_new_duplicates [function]` (`db28a7a8-6630-5489-93fa-ee61cb0d4751`) lines 246-269 [crates/gwiki/src/compile/collect.rs:246-269]
  - Signature: `fn extend_unique_preserves_order_and_removes_existing_or_new_duplicates() {`
  - Purpose: Indexed function `extend_unique_preserves_order_and_removes_existing_or_new_duplicates` in `crates/gwiki/src/compile/collect.rs`. [crates/gwiki/src/compile/collect.rs:246-269]
- `missing_accepted_note_returns_not_found` (function) component `missing_accepted_note_returns_not_found [function]` (`cf9ce15c-731a-59cd-80e6-6ce100eda6a7`) lines 272-300 [crates/gwiki/src/compile/collect.rs:272-300]
  - Signature: `fn missing_accepted_note_returns_not_found() {`
  - Purpose: Indexed function `missing_accepted_note_returns_not_found` in `crates/gwiki/src/compile/collect.rs`. [crates/gwiki/src/compile/collect.rs:272-300]

