---
title: crates/gwiki/src/citations.rs
type: code_file
provenance:
- file: crates/gwiki/src/citations.rs
  ranges:
  - 6-14
  - 16-35
  - 37-46
  - 48-69
  - 71-88
  - 90-92
  - 100-124
  - 127-148
  - 151-170
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/citations.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

`crates/gwiki/src/citations.rs` exposes 9 indexed API symbols.
[crates/gwiki/src/citations.rs:6-14]
[crates/gwiki/src/citations.rs:16-35]
[crates/gwiki/src/citations.rs:37-46]
[crates/gwiki/src/citations.rs:48-69]
[crates/gwiki/src/citations.rs:71-88]

## API Symbols

- `render_source_citations` (function) component `render_source_citations [function]` (`2edd175a-71b9-5017-9d87-5c7a12eaf506`) lines 6-14 [crates/gwiki/src/citations.rs:6-14]
  - Signature: `pub fn render_source_citations(`
  - Purpose: Maps source records from the provided vault paths through `render_source_citation` to produce a vector of formatted citation strings. [crates/gwiki/src/citations.rs:6-14]
- `source_records_for_paths` (function) component `source_records_for_paths [function]` (`7457504d-0726-5fa5-a33c-213900f5cab5`) lines 16-35 [crates/gwiki/src/citations.rs:16-35]
  - Signature: `pub fn source_records_for_paths(`
  - Purpose: Reads a source manifest from a vault root and returns entries matching any of the provided paths, or all entries if no paths are specified. [crates/gwiki/src/citations.rs:16-35]
- `source_record_matches_path` (function) component `source_record_matches_path [function]` (`109c0dbc-971f-5c00-904c-6a6522d13e66`) lines 37-46 [crates/gwiki/src/citations.rs:37-46]
  - Signature: `pub fn source_record_matches_path(entry: &SourceRecord, vault_root: &Path, path: &Path) -> bool {`
  - Purpose: Compares a `SourceRecord`'s normalized location against a given path in both relative-to-vault-root and absolute forms, returning `true` if either representation matches. [crates/gwiki/src/citations.rs:37-46]
- `render_source_citation` (function) component `render_source_citation [function]` (`fd79833e-6cf8-527e-81a0-1473d41941cb`) lines 48-69 [crates/gwiki/src/citations.rs:48-69]
  - Signature: `fn render_source_citation(entry: &SourceRecord) -> String {`
  - Purpose: Renders a SourceRecord into a formatted citation string by combining its primary identifier (citation, title, or location), source location (if distinct), kind, fetch timestamp, optional license, and content hash. [crates/gwiki/src/citations.rs:48-69]
- `join_citation_parts` (function) component `join_citation_parts [function]` (`22a38e2a-4fe7-54ac-80d3-3c1dc25ed9a0`) lines 71-88 [crates/gwiki/src/citations.rs:71-88]
  - Signature: `fn join_citation_parts(parts: &[String]) -> String {`
  - Purpose: Joins non-empty trimmed string parts into a single string, inserting either a space (if the accumulated result ends with `.`, `!`, or `?`) or period-space (otherwise) between parts. [crates/gwiki/src/citations.rs:71-88]
- `normalize_path_text` (function) component `normalize_path_text [function]` (`26d9a5e0-632e-527b-aff9-0249dc888d80`) lines 90-92 [crates/gwiki/src/citations.rs:90-92]
  - Signature: `fn normalize_path_text(value: &str) -> String {`
  - Purpose: Normalizes a path string by trimming leading/trailing whitespace and converting all backslashes to forward slashes. [crates/gwiki/src/citations.rs:90-92]
- `renders_source_citations` (function) component `renders_source_citations [function]` (`9d97b896-830e-51cc-91c5-cbe77bac5ce0`) lines 100-124 [crates/gwiki/src/citations.rs:100-124]
  - Signature: `fn renders_source_citations() {`
  - Purpose: Unit test that verifies `render_source_citations()` correctly generates formatted citation strings containing source metadata (citation text, file path, license, and timestamp) for registered documents. [crates/gwiki/src/citations.rs:100-124]
- `citation_renderer_does_not_add_wrapper_punctuation` (function) component `citation_renderer_does_not_add_wrapper_punctuation [function]` (`9252d81e-14cb-5f0e-8137-2086a7842b3b`) lines 127-148 [crates/gwiki/src/citations.rs:127-148]
  - Signature: `fn citation_renderer_does_not_add_wrapper_punctuation() {`
  - Purpose: This test verifies that `render_source_citation` does not add or duplicate punctuation when rendering a `SourceRecord` with a citation that already ends with a period. [crates/gwiki/src/citations.rs:127-148]
- `citation_renderer_does_not_duplicate_location` (function) component `citation_renderer_does_not_duplicate_location [function]` (`ab0bf7a8-ee08-5db6-be7a-404c47b22950`) lines 151-170 [crates/gwiki/src/citations.rs:151-170]
  - Signature: `fn citation_renderer_does_not_duplicate_location() {`
  - Purpose: Tests that `render_source_citation` renders a SourceRecord with matching location and citation fields without duplicating the path string. [crates/gwiki/src/citations.rs:151-170]

