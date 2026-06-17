---
title: crates/gwiki/src/sources/render.rs
type: code_file
provenance:
- file: crates/gwiki/src/sources/render.rs
  ranges:
  - 15-45
  - 47-58
  - 60-70
  - 72-75
  - 77-124
  - 126-133
  - 135-137
  - 139-145
  - 147-166
  - 168-183
  - 185-190
  - 192-197
  - 199-204
  - 206-208
  - 215-221
  - 224-229
  - 232-234
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/sources/render.rs:15-45](crates/gwiki/src/sources/render.rs#L15-L45), [crates/gwiki/src/sources/render.rs:47-58](crates/gwiki/src/sources/render.rs#L47-L58), [crates/gwiki/src/sources/render.rs:60-70](crates/gwiki/src/sources/render.rs#L60-L70), [crates/gwiki/src/sources/render.rs:72-75](crates/gwiki/src/sources/render.rs#L72-L75), [crates/gwiki/src/sources/render.rs:77-124](crates/gwiki/src/sources/render.rs#L77-L124), [crates/gwiki/src/sources/render.rs:126-133](crates/gwiki/src/sources/render.rs#L126-L133), [crates/gwiki/src/sources/render.rs:135-137](crates/gwiki/src/sources/render.rs#L135-L137), [crates/gwiki/src/sources/render.rs:139-145](crates/gwiki/src/sources/render.rs#L139-L145), [crates/gwiki/src/sources/render.rs:147-166](crates/gwiki/src/sources/render.rs#L147-L166), [crates/gwiki/src/sources/render.rs:168-183](crates/gwiki/src/sources/render.rs#L168-L183), [crates/gwiki/src/sources/render.rs:185-190](crates/gwiki/src/sources/render.rs#L185-L190), [crates/gwiki/src/sources/render.rs:192-197](crates/gwiki/src/sources/render.rs#L192-L197), [crates/gwiki/src/sources/render.rs:199-204](crates/gwiki/src/sources/render.rs#L199-L204), [crates/gwiki/src/sources/render.rs:206-208](crates/gwiki/src/sources/render.rs#L206-L208), [crates/gwiki/src/sources/render.rs:215-221](crates/gwiki/src/sources/render.rs#L215-L221), [crates/gwiki/src/sources/render.rs:224-229](crates/gwiki/src/sources/render.rs#L224-L229), [crates/gwiki/src/sources/render.rs:232-234](crates/gwiki/src/sources/render.rs#L232-L234)

</details>

# crates/gwiki/src/sources/render.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Builds and maintains the rendered source index for wiki sources. `render_entry` formats a `SourceRecord` into a markdown list item with metadata, optional citation/license lines, and an embedded JSON marker; the helper functions normalize source locations by stripping fragments, lowercasing scheme/authority, sorting query parameters, and trimming redundant trailing slashes. The remaining helpers generate stable source IDs, preserve or recover existing index content around manifest markers, and escape/normalize text and link destinations so the generated markdown stays valid.
[crates/gwiki/src/sources/render.rs:15-45]
[crates/gwiki/src/sources/render.rs:47-58]
[crates/gwiki/src/sources/render.rs:60-70]
[crates/gwiki/src/sources/render.rs:72-75]
[crates/gwiki/src/sources/render.rs:77-124]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `render_entry` | function | `pub(crate) fn render_entry(entry: &SourceRecord, index: &mut String) -> Result<(), WikiError> {` | `render_entry [function]` | `5e77abb0-7a68-59c2-b1ee-79caa6f3fcf4` | 15-45 [crates/gwiki/src/sources/render.rs:15-45] | Indexed function `render_entry` in `crates/gwiki/src/sources/render.rs`. [crates/gwiki/src/sources/render.rs:15-45] |
| `canonicalize_location` | function | `pub(crate) fn canonicalize_location(location: &str) -> String {` | `canonicalize_location [function]` | `1c9e0102-691f-523d-997d-7ca20601c51b` | 47-58 [crates/gwiki/src/sources/render.rs:47-58] | Indexed function `canonicalize_location` in `crates/gwiki/src/sources/render.rs`. [crates/gwiki/src/sources/render.rs:47-58] |
| `split_sorted_query` | function | `fn split_sorted_query(location: &str) -> (String, Option<String>) {` | `split_sorted_query [function]` | `98d0a19e-a5f8-5a31-9ce6-67dcdd71be6c` | 60-70 [crates/gwiki/src/sources/render.rs:60-70] | Indexed function `split_sorted_query` in `crates/gwiki/src/sources/render.rs`. [crates/gwiki/src/sources/render.rs:60-70] |
| `PreservedSourceIndex` | class | `pub(crate) struct PreservedSourceIndex {` | `PreservedSourceIndex [class]` | `b08e7597-ef34-54ae-8163-e620ab79f2ef` | 72-75 [crates/gwiki/src/sources/render.rs:72-75] | Indexed class `PreservedSourceIndex` in `crates/gwiki/src/sources/render.rs`. [crates/gwiki/src/sources/render.rs:72-75] |
| `existing_index_without_manifest` | function | `pub(crate) fn existing_index_without_manifest(` | `existing_index_without_manifest [function]` | `c659fb5b-a01d-558f-88ef-15ccb78d1f98` | 77-124 [crates/gwiki/src/sources/render.rs:77-124] | Indexed function `existing_index_without_manifest` in `crates/gwiki/src/sources/render.rs`. [crates/gwiki/src/sources/render.rs:77-124] |
| `normalize_preserved_index_prefix` | function | `fn normalize_preserved_index_prefix(prefix: &str) -> String {` | `normalize_preserved_index_prefix [function]` | `2e39bc5d-8f78-50d4-9695-bcbbeced6754` | 126-133 [crates/gwiki/src/sources/render.rs:126-133] | Indexed function `normalize_preserved_index_prefix` in `crates/gwiki/src/sources/render.rs`. [crates/gwiki/src/sources/render.rs:126-133] |
| `normalize_preserved_index_suffix` | function | `fn normalize_preserved_index_suffix(suffix: &str) -> String {` | `normalize_preserved_index_suffix [function]` | `ceba4072-2897-5aa3-af55-49687688a1af` | 135-137 [crates/gwiki/src/sources/render.rs:135-137] | Indexed function `normalize_preserved_index_suffix` in `crates/gwiki/src/sources/render.rs`. [crates/gwiki/src/sources/render.rs:135-137] |
| `suffix_after_unmarked_manifest` | function | `fn suffix_after_unmarked_manifest(existing: &str, header_start: usize) -> String {` | `suffix_after_unmarked_manifest [function]` | `d6eb26bd-2075-5aab-b236-c6c02ce9f87a` | 139-145 [crates/gwiki/src/sources/render.rs:139-145] | Indexed function `suffix_after_unmarked_manifest` in `crates/gwiki/src/sources/render.rs`. [crates/gwiki/src/sources/render.rs:139-145] |
| `lower_url_scheme_and_authority` | function | `fn lower_url_scheme_and_authority(location: &str) -> String {` | `lower_url_scheme_and_authority [function]` | `5be09559-7ca3-54fd-844e-81b97f88c3b2` | 147-166 [crates/gwiki/src/sources/render.rs:147-166] | Indexed function `lower_url_scheme_and_authority` in `crates/gwiki/src/sources/render.rs`. [crates/gwiki/src/sources/render.rs:147-166] |
| `source_id` | function | `pub(crate) fn source_id(canonical_location: &str, content_hash: &str) -> String {` | `source_id [function]` | `b80e810a-c3c7-508a-ad81-060a03868bf2` | 168-183 [crates/gwiki/src/sources/render.rs:168-183] | Indexed function `source_id` in `crates/gwiki/src/sources/render.rs`. [crates/gwiki/src/sources/render.rs:168-183] |
| `escape_markdown_text` | function | `fn escape_markdown_text(text: &str) -> String {` | `escape_markdown_text [function]` | `3b6e188a-4356-52ba-9c06-3bc22ca25dd6` | 185-190 [crates/gwiki/src/sources/render.rs:185-190] | Indexed function `escape_markdown_text` in `crates/gwiki/src/sources/render.rs`. [crates/gwiki/src/sources/render.rs:185-190] |
| `escape_markdown_destination` | function | `fn escape_markdown_destination(destination: &str) -> String {` | `escape_markdown_destination [function]` | `2fb3fded-79b8-5165-aeea-af2a124a3a39` | 192-197 [crates/gwiki/src/sources/render.rs:192-197] | Indexed function `escape_markdown_destination` in `crates/gwiki/src/sources/render.rs`. [crates/gwiki/src/sources/render.rs:192-197] |
| `inline_text` | function | `fn inline_text(text: &str) -> String {` | `inline_text [function]` | `2ea5e442-5c30-58a3-999b-7afe9f100107` | 199-204 [crates/gwiki/src/sources/render.rs:199-204] | Indexed function `inline_text` in `crates/gwiki/src/sources/render.rs`. [crates/gwiki/src/sources/render.rs:199-204] |
| `normalize_newlines` | function | `fn normalize_newlines(text: &str) -> String {` | `normalize_newlines [function]` | `c25e2aa2-7d8a-5895-8c19-d4b09c22fff6` | 206-208 [crates/gwiki/src/sources/render.rs:206-208] | Indexed function `normalize_newlines` in `crates/gwiki/src/sources/render.rs`. [crates/gwiki/src/sources/render.rs:206-208] |
| `markdown_link_escaping_escapes_backslashes_before_breakers` | function | `fn markdown_link_escaping_escapes_backslashes_before_breakers() {` | `markdown_link_escaping_escapes_backslashes_before_breakers [function]` | `adfc137e-4c0f-5355-a08c-b90d50ae35cd` | 215-221 [crates/gwiki/src/sources/render.rs:215-221] | Indexed function `markdown_link_escaping_escapes_backslashes_before_breakers` in `crates/gwiki/src/sources/render.rs`. [crates/gwiki/src/sources/render.rs:215-221] |
| `inline_text_normalizes_newlines_and_collapses_whitespace` | function | `fn inline_text_normalizes_newlines_and_collapses_whitespace() {` | `inline_text_normalizes_newlines_and_collapses_whitespace [function]` | `6677691f-1273-5176-be48-2654e734120e` | 224-229 [crates/gwiki/src/sources/render.rs:224-229] | Indexed function `inline_text_normalizes_newlines_and_collapses_whitespace` in `crates/gwiki/src/sources/render.rs`. [crates/gwiki/src/sources/render.rs:224-229] |
| `source_id_uses_empty_hash_sentinel` | function | `fn source_id_uses_empty_hash_sentinel() {` | `source_id_uses_empty_hash_sentinel [function]` | `1b88729e-637a-5d95-b494-5b4655f76e45` | 232-234 [crates/gwiki/src/sources/render.rs:232-234] | Indexed function `source_id_uses_empty_hash_sentinel` in `crates/gwiki/src/sources/render.rs`. [crates/gwiki/src/sources/render.rs:232-234] |
