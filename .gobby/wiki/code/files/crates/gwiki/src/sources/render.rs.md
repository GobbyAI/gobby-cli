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

# crates/gwiki/src/sources/render.rs

Module: [[code/modules/crates/gwiki/src/sources|crates/gwiki/src/sources]]

## Purpose

This file renders and preserves the raw source index for the wiki. `render_entry` formats each `SourceRecord` as a markdown list item with escaped title and destination, inline metadata fields, and serialized JSON metadata embedded in an HTML comment. The URL helpers `canonicalize_location`, `split_sorted_query`, and `lower_url_scheme_and_authority` normalize locations by removing fragments, lowercasing scheme/authority, sorting query parameters, and trimming trailing slashes so source IDs and stored references stay stable. `source_id` builds a deterministic identifier from a hash prefix plus an optional slugified canonical location. The preserved-index helpers read an existing index file, extract the non-generated prefix/suffix around the source-manifest section, and normalize those boundaries so regenerated output can be merged without losing surrounding content. Supporting text utilities escape markdown, collapse inline text whitespace, and normalize newlines, and the tests verify the escaping, whitespace normalization, and empty-hash sentinel behavior.
[crates/gwiki/src/sources/render.rs:15-45]
[crates/gwiki/src/sources/render.rs:47-58]
[crates/gwiki/src/sources/render.rs:60-70]
[crates/gwiki/src/sources/render.rs:72-75]
[crates/gwiki/src/sources/render.rs:77-124]

## API Symbols

- `render_entry` (function) component `render_entry [function]` (`5e77abb0-7a68-59c2-b1ee-79caa6f3fcf4`) lines 15-45 [crates/gwiki/src/sources/render.rs:15-45]
  - Signature: `pub(crate) fn render_entry(entry: &SourceRecord, index: &mut String) -> Result<(), WikiError> {`
  - Purpose: Appends a markdown-formatted SourceRecord entry with escaped markdown text/destinations and serialized metadata to the provided index string. [crates/gwiki/src/sources/render.rs:15-45]
- `canonicalize_location` (function) component `canonicalize_location [function]` (`1c9e0102-691f-523d-997d-7ca20601c51b`) lines 47-58 [crates/gwiki/src/sources/render.rs:47-58]
  - Signature: `pub(crate) fn canonicalize_location(location: &str) -> String {`
  - Purpose: Canonicalizes a URL by removing the fragment identifier, lowercasing the scheme and authority, sorting query parameters, and stripping trailing slashes (except for the root path). [crates/gwiki/src/sources/render.rs:47-58]
- `split_sorted_query` (function) component `split_sorted_query [function]` (`98d0a19e-a5f8-5a31-9ce6-67dcdd71be6c`) lines 60-70 [crates/gwiki/src/sources/render.rs:60-70]
  - Signature: `fn split_sorted_query(location: &str) -> (String, Option<String>) {`
  - Purpose: Splits a URL at the query delimiter and returns the base path with lexicographically sorted query parameters. [crates/gwiki/src/sources/render.rs:60-70]
- `PreservedSourceIndex` (class) component `PreservedSourceIndex [class]` (`b08e7597-ef34-54ae-8163-e620ab79f2ef`) lines 72-75 [crates/gwiki/src/sources/render.rs:72-75]
  - Signature: `pub(crate) struct PreservedSourceIndex {`
  - Purpose: `PreservedSourceIndex` is a crate-private struct that encapsulates string-based prefix and suffix fields for storing preserved source code segments. [crates/gwiki/src/sources/render.rs:72-75]
- `existing_index_without_manifest` (function) component `existing_index_without_manifest [function]` (`c659fb5b-a01d-558f-88ef-15ccb78d1f98`) lines 77-124 [crates/gwiki/src/sources/render.rs:77-124]
  - Signature: `pub(crate) fn existing_index_without_manifest(`
  - Purpose: Reads an index file and extracts the prefix and suffix surrounding a generated source manifest section (identified by markers or `## Source manifest` header), returning the preserved non-manifest content as a `PreservedSourceIndex`. [crates/gwiki/src/sources/render.rs:77-124]
- `normalize_preserved_index_prefix` (function) component `normalize_preserved_index_prefix [function]` (`2e39bc5d-8f78-50d4-9695-bcbbeced6754`) lines 126-133 [crates/gwiki/src/sources/render.rs:126-133]
  - Signature: `fn normalize_preserved_index_prefix(prefix: &str) -> String {`
  - Purpose: Normalizes a prefix string by removing trailing newlines, substituting a default markdown header ("# Raw Sources") if the content is empty, and appending double newlines. [crates/gwiki/src/sources/render.rs:126-133]
- `normalize_preserved_index_suffix` (function) component `normalize_preserved_index_suffix [function]` (`ceba4072-2897-5aa3-af55-49687688a1af`) lines 135-137 [crates/gwiki/src/sources/render.rs:135-137]
  - Signature: `fn normalize_preserved_index_suffix(suffix: &str) -> String {`
  - Purpose: Removes all leading newline characters from the input string and returns the trimmed result as an owned `String`. [crates/gwiki/src/sources/render.rs:135-137]
- `suffix_after_unmarked_manifest` (function) component `suffix_after_unmarked_manifest [function]` (`d6eb26bd-2075-5aab-b236-c6c02ce9f87a`) lines 139-145 [crates/gwiki/src/sources/render.rs:139-145]
  - Signature: `fn suffix_after_unmarked_manifest(existing: &str, header_start: usize) -> String {`
  - Purpose: Extracts and normalizes the text content between the "## Source manifest" header and the next markdown section header, or returns an empty string if no subsequent header exists. [crates/gwiki/src/sources/render.rs:139-145]
- `lower_url_scheme_and_authority` (function) component `lower_url_scheme_and_authority [function]` (`5be09559-7ca3-54fd-844e-81b97f88c3b2`) lines 147-166 [crates/gwiki/src/sources/render.rs:147-166]
  - Signature: `fn lower_url_scheme_and_authority(location: &str) -> String {`
  - Purpose: Lowercases the scheme and authority components of a URL while preserving the path and normalizing backslashes to forward slashes. [crates/gwiki/src/sources/render.rs:147-166]
- `source_id` (function) component `source_id [function]` (`b80e810a-c3c7-508a-ad81-060a03868bf2`) lines 168-183 [crates/gwiki/src/sources/render.rs:168-183]
  - Signature: `pub(crate) fn source_id(canonical_location: &str, content_hash: &str) -> String {`
  - Purpose: Constructs a source identifier by concatenating a truncated content hash prefix with an optional slugified canonical location, formatted as `src-{hash_prefix}` or `src-{hash_prefix}-{slug}`. [crates/gwiki/src/sources/render.rs:168-183]
- `escape_markdown_text` (function) component `escape_markdown_text [function]` (`3b6e188a-4356-52ba-9c06-3bc22ca25dd6`) lines 185-190 [crates/gwiki/src/sources/render.rs:185-190]
  - Signature: `fn escape_markdown_text(text: &str) -> String {`
  - Purpose: This function escapes markdown special characters (backslashes and square brackets) and normalizes newlines in the input string. [crates/gwiki/src/sources/render.rs:185-190]
- `escape_markdown_destination` (function) component `escape_markdown_destination [function]` (`2fb3fded-79b8-5165-aeea-af2a124a3a39`) lines 192-197 [crates/gwiki/src/sources/render.rs:192-197]
  - Signature: `fn escape_markdown_destination(destination: &str) -> String {`
  - Purpose: Escapes backslashes and parentheses in markdown destination strings after normalizing newlines. [crates/gwiki/src/sources/render.rs:192-197]
- `inline_text` (function) component `inline_text [function]` (`2ea5e442-5c30-58a3-999b-7afe9f100107`) lines 199-204 [crates/gwiki/src/sources/render.rs:199-204]
  - Signature: `fn inline_text(text: &str) -> String {`
  - Purpose: Normalizes newlines and collapses all consecutive whitespace sequences into single spaces. [crates/gwiki/src/sources/render.rs:199-204]
- `normalize_newlines` (function) component `normalize_newlines [function]` (`c25e2aa2-7d8a-5895-8c19-d4b09c22fff6`) lines 206-208 [crates/gwiki/src/sources/render.rs:206-208]
  - Signature: `fn normalize_newlines(text: &str) -> String {`
  - Purpose: Normalizes all line endings in the input string to Unix-style line feeds (LF) by replacing Windows (CRLF) and Mac (CR) line ending sequences. [crates/gwiki/src/sources/render.rs:206-208]
- `markdown_link_escaping_escapes_backslashes_before_breakers` (function) component `markdown_link_escaping_escapes_backslashes_before_breakers [function]` (`adfc137e-4c0f-5355-a08c-b90d50ae35cd`) lines 215-221 [crates/gwiki/src/sources/render.rs:215-221]
  - Signature: `fn markdown_link_escaping_escapes_backslashes_before_breakers() {`
  - Purpose: This test verifies that `escape_markdown_text` and `escape_markdown_destination` correctly escape backslashes preceding markdown syntax breakers (brackets and parentheses) by tripling the backslash and escaping the breaker character. [crates/gwiki/src/sources/render.rs:215-221]
- `inline_text_normalizes_newlines_and_collapses_whitespace` (function) component `inline_text_normalizes_newlines_and_collapses_whitespace [function]` (`6677691f-1273-5176-be48-2654e734120e`) lines 224-229 [crates/gwiki/src/sources/render.rs:224-229]
  - Signature: `fn inline_text_normalizes_newlines_and_collapses_whitespace() {`
  - Purpose: This test verifies that the `inline_text` function normalizes all whitespace characters (CRLF, CR, tabs, spaces) and collapses consecutive whitespace into single spaces. [crates/gwiki/src/sources/render.rs:224-229]
- `source_id_uses_empty_hash_sentinel` (function) component `source_id_uses_empty_hash_sentinel [function]` (`1b88729e-637a-5d95-b494-5b4655f76e45`) lines 232-234 [crates/gwiki/src/sources/render.rs:232-234]
  - Signature: `fn source_id_uses_empty_hash_sentinel() {`
  - Purpose: This test verifies that the `source_id` function returns a zero-valued hash sentinel (`src-0000000000000000`) when invoked with empty string arguments. [crates/gwiki/src/sources/render.rs:232-234]

