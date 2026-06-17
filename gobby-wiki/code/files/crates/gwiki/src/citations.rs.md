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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/citations.rs:6-14](crates/gwiki/src/citations.rs#L6-L14), [crates/gwiki/src/citations.rs:16-35](crates/gwiki/src/citations.rs#L16-L35), [crates/gwiki/src/citations.rs:37-46](crates/gwiki/src/citations.rs#L37-L46), [crates/gwiki/src/citations.rs:48-69](crates/gwiki/src/citations.rs#L48-L69), [crates/gwiki/src/citations.rs:71-88](crates/gwiki/src/citations.rs#L71-L88), [crates/gwiki/src/citations.rs:90-92](crates/gwiki/src/citations.rs#L90-L92), [crates/gwiki/src/citations.rs:100-124](crates/gwiki/src/citations.rs#L100-L124), [crates/gwiki/src/citations.rs:127-148](crates/gwiki/src/citations.rs#L127-L148), [crates/gwiki/src/citations.rs:151-170](crates/gwiki/src/citations.rs#L151-L170)

</details>

# crates/gwiki/src/citations.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file filters source manifest entries by path and formats them into human-readable citation strings. `source_records_for_paths` reads the manifest from the vault root and returns either all entries or only those whose stored location matches any requested absolute or vault-relative path, using `source_record_matches_path` and path normalization to compare consistently. `render_source_citations` turns those matching records into rendered citation strings through `render_source_citation`, which chooses a primary citation/title/location, appends source metadata like kind, fetched time, optional license, and content hash, then joins the parts cleanly with `join_citation_parts`. The tests check that the renderer avoids adding redundant wrapper punctuation and does not duplicate the location when it is already the primary citation.
[crates/gwiki/src/citations.rs:6-14]
[crates/gwiki/src/citations.rs:16-35]
[crates/gwiki/src/citations.rs:37-46]
[crates/gwiki/src/citations.rs:48-69]
[crates/gwiki/src/citations.rs:71-88]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `render_source_citations` | function | `pub fn render_source_citations(` | `render_source_citations [function]` | `2edd175a-71b9-5017-9d87-5c7a12eaf506` | 6-14 [crates/gwiki/src/citations.rs:6-14] | Indexed function `render_source_citations` in `crates/gwiki/src/citations.rs`. [crates/gwiki/src/citations.rs:6-14] |
| `source_records_for_paths` | function | `pub fn source_records_for_paths(` | `source_records_for_paths [function]` | `7457504d-0726-5fa5-a33c-213900f5cab5` | 16-35 [crates/gwiki/src/citations.rs:16-35] | Indexed function `source_records_for_paths` in `crates/gwiki/src/citations.rs`. [crates/gwiki/src/citations.rs:16-35] |
| `source_record_matches_path` | function | `pub fn source_record_matches_path(entry: &SourceRecord, vault_root: &Path, path: &Path) -> bool {` | `source_record_matches_path [function]` | `109c0dbc-971f-5c00-904c-6a6522d13e66` | 37-46 [crates/gwiki/src/citations.rs:37-46] | Indexed function `source_record_matches_path` in `crates/gwiki/src/citations.rs`. [crates/gwiki/src/citations.rs:37-46] |
| `render_source_citation` | function | `fn render_source_citation(entry: &SourceRecord) -> String {` | `render_source_citation [function]` | `fd79833e-6cf8-527e-81a0-1473d41941cb` | 48-69 [crates/gwiki/src/citations.rs:48-69] | Indexed function `render_source_citation` in `crates/gwiki/src/citations.rs`. [crates/gwiki/src/citations.rs:48-69] |
| `join_citation_parts` | function | `fn join_citation_parts(parts: &[String]) -> String {` | `join_citation_parts [function]` | `22a38e2a-4fe7-54ac-80d3-3c1dc25ed9a0` | 71-88 [crates/gwiki/src/citations.rs:71-88] | Indexed function `join_citation_parts` in `crates/gwiki/src/citations.rs`. [crates/gwiki/src/citations.rs:71-88] |
| `normalize_path_text` | function | `fn normalize_path_text(value: &str) -> String {` | `normalize_path_text [function]` | `26d9a5e0-632e-527b-aff9-0249dc888d80` | 90-92 [crates/gwiki/src/citations.rs:90-92] | Indexed function `normalize_path_text` in `crates/gwiki/src/citations.rs`. [crates/gwiki/src/citations.rs:90-92] |
| `renders_source_citations` | function | `fn renders_source_citations() {` | `renders_source_citations [function]` | `9d97b896-830e-51cc-91c5-cbe77bac5ce0` | 100-124 [crates/gwiki/src/citations.rs:100-124] | Indexed function `renders_source_citations` in `crates/gwiki/src/citations.rs`. [crates/gwiki/src/citations.rs:100-124] |
| `citation_renderer_does_not_add_wrapper_punctuation` | function | `fn citation_renderer_does_not_add_wrapper_punctuation() {` | `citation_renderer_does_not_add_wrapper_punctuation [function]` | `9252d81e-14cb-5f0e-8137-2086a7842b3b` | 127-148 [crates/gwiki/src/citations.rs:127-148] | Indexed function `citation_renderer_does_not_add_wrapper_punctuation` in `crates/gwiki/src/citations.rs`. [crates/gwiki/src/citations.rs:127-148] |
| `citation_renderer_does_not_duplicate_location` | function | `fn citation_renderer_does_not_duplicate_location() {` | `citation_renderer_does_not_duplicate_location [function]` | `ab0bf7a8-ee08-5db6-be7a-404c47b22950` | 151-170 [crates/gwiki/src/citations.rs:151-170] | Indexed function `citation_renderer_does_not_duplicate_location` in `crates/gwiki/src/citations.rs`. [crates/gwiki/src/citations.rs:151-170] |
