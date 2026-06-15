---
title: crates/gwiki/src/support/text.rs
type: code_file
provenance:
- file: crates/gwiki/src/support/text.rs
  ranges:
  - 7-13
  - 15-22
  - 26-46
  - 48-59
  - 61-73
  - 75-83
  - 85-91
  - 93-95
  - 97-99
  - 101-126
  - 133-138
  - 141-153
  - 156-166
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/support/text.rs

Module: [[code/modules/crates/gwiki/src/support|crates/gwiki/src/support]]

## Purpose

Utilities for normalizing and classifying text in `gwiki`: it tokenizes search queries, scores text against normalized keywords, sanitizes user-supplied code paths into safe repo-relative strings, extracts short display snippets, maps degradation/document/database kinds to canonical labels, and builds display paths and slugs. The helper functions are paired with tests that confirm snippet truncation, path sanitization, and slug fallback/max-length behavior.
[crates/gwiki/src/support/text.rs:7-13]
[crates/gwiki/src/support/text.rs:15-22]
[crates/gwiki/src/support/text.rs:26-46]
[crates/gwiki/src/support/text.rs:48-59]
[crates/gwiki/src/support/text.rs:61-73]

## API Symbols

- `query_tokens` (function) component `query_tokens [function]` (`9d7a2ce6-8feb-5fb6-aa36-19986c3ef7b7`) lines 7-13 [crates/gwiki/src/support/text.rs:7-13]
  - Signature: `pub(crate) fn query_tokens(query: &str) -> Vec<String> {`
  - Purpose: This function tokenizes a query string by splitting on non-alphanumeric characters, filtering empty tokens, and converting the results to lowercase. [crates/gwiki/src/support/text.rs:7-13]
- `keyword_score` (function) component `keyword_score [function]` (`91790d1a-0fe3-5fc3-ab61-2655714dc637`) lines 15-22 [crates/gwiki/src/support/text.rs:15-22]
  - Signature: `pub(crate) fn keyword_score(text: &str, tokens: &[String]) -> usize {`
  - Purpose: Counts the total occurrences of all provided normalized tokens within a case-insensitive version of the input text. [crates/gwiki/src/support/text.rs:15-22]
- `sanitize_code_path` (function) component `sanitize_code_path [function]` (`e6ee4298-a16f-59b0-8280-90cadaa5fcc3`) lines 26-46 [crates/gwiki/src/support/text.rs:26-46]
  - Signature: `pub(crate) fn sanitize_code_path(path: &str) -> Option<String> {`
  - Purpose: Trims the input, rejects empty or absolute paths and any path containing '..', root, or platform prefix components, then returns the remaining normal components joined with '/' as a relative code path, or 'None' if nothing valid remains. [crates/gwiki/src/support/text.rs:26-46]
- `snippet_from_text` (function) component `snippet_from_text [function]` (`a19532b2-de2b-59bd-8b3b-75376c885954`) lines 48-59 [crates/gwiki/src/support/text.rs:48-59]
  - Signature: `pub(crate) fn snippet_from_text(text: &str) -> String {`
  - Purpose: Returns the first non-empty trimmed line from 'text', truncating it to 240 characters by keeping the first 237 characters and appending '...' when necessary. [crates/gwiki/src/support/text.rs:48-59]
- `degradation_label` (function) component `degradation_label [function]` (`67129cf2-e917-5cd9-b30a-aed2a05b5be1`) lines 61-73 [crates/gwiki/src/support/text.rs:61-73]
  - Signature: `pub(crate) fn degradation_label(degradation: &DegradationKind) -> String {`
  - Purpose: Returns a canonical string label for a 'DegradationKind', mapping service-unavailable states to '{service}_{available|not_configured|unreachable}' and all other variants to fixed snake_case identifiers. [crates/gwiki/src/support/text.rs:61-73]
- `document_kind_name` (function) component `document_kind_name [function]` (`d42b4658-ebe0-52ae-a9e1-373a5a81d760`) lines 75-83 [crates/gwiki/src/support/text.rs:75-83]
  - Signature: `pub(crate) fn document_kind_name(kind: store::WikiDocumentKind) -> &'static str {`
  - Purpose: Returns the canonical '&'static str' identifier for a 'store::WikiDocumentKind' variant by matching 'SourceCatalog', 'SourceNote', 'Concept', 'Topic', and 'CodeDoc' to '"source_catalog"', '"source_note"', '"concept"', '"topic"', and '"code_doc"' respectively. [crates/gwiki/src/support/text.rs:75-83]
- `postgres_object_kind` (function) component `postgres_object_kind [function]` (`972dc6e5-2409-58d6-b9ed-89de9de3b427`) lines 85-91 [crates/gwiki/src/support/text.rs:85-91]
  - Signature: `pub(crate) fn postgres_object_kind(kind: setup::GwikiPostgresObjectKind) -> &'static str {`
  - Purpose: Maps a 'setup::GwikiPostgresObjectKind' enum variant to its corresponding lowercase PostgreSQL object kind string literal: '"preflight"', '"table"', or '"index"'. [crates/gwiki/src/support/text.rs:85-91]
- `display_path` (function) component `display_path [function]` (`a33408bc-a2eb-574c-b231-09c256188203`) lines 93-95 [crates/gwiki/src/support/text.rs:93-95]
  - Signature: `pub(crate) fn display_path(path: &Path) -> String {`
  - Purpose: Converts a 'Path' to a lossy UTF-8 'String' and normalizes it by replacing all backslashes with forward slashes. [crates/gwiki/src/support/text.rs:93-95]
- `slugify` (function) component `slugify [function]` (`f9678e6e-5cab-5644-9005-69225719f089`) lines 97-99 [crates/gwiki/src/support/text.rs:97-99]
  - Signature: `pub(crate) fn slugify(value: &str) -> String {`
  - Purpose: 'slugify' returns a 'String' by delegating to 'slugify_with_options(value, None, None)', applying the default slugification behavior to the input string. [crates/gwiki/src/support/text.rs:97-99]
- `slugify_with_options` (function) component `slugify_with_options [function]` (`85deb1dd-437d-5e93-bed7-18ce0f2b4493`) lines 101-126 [crates/gwiki/src/support/text.rs:101-126]
  - Signature: `pub(crate) fn slugify_with_options(`
  - Purpose: Produces a lowercase ASCII slug from 'value' by keeping alphanumerics, collapsing non-alphanumeric runs into single dashes, trimming trailing dashes, enforcing an optional 'max_len' cutoff on the accumulated slug length, and returning 'fallback' or '""' if the result is empty. [crates/gwiki/src/support/text.rs:101-126]
- `snippets_reserve_space_for_ellipsis` (function) component `snippets_reserve_space_for_ellipsis [function]` (`9e229e53-0e5c-5140-b948-55f4b02e870a`) lines 133-138 [crates/gwiki/src/support/text.rs:133-138]
  - Signature: `fn snippets_reserve_space_for_ellipsis() {`
  - Purpose: Verifies that 'snippet_from_text' truncates a 300-character string to 240 characters while reserving room for and appending an ellipsis ('...'). [crates/gwiki/src/support/text.rs:133-138]
- `sanitize_code_path_strips_current_dir_components` (function) component `sanitize_code_path_strips_current_dir_components [function]` (`8cf79b6a-4e06-5249-bb09-a271f3e99c7a`) lines 141-153 [crates/gwiki/src/support/text.rs:141-153]
  - Signature: `fn sanitize_code_path_strips_current_dir_components() {`
  - Purpose: Tests that 'sanitize_code_path' removes '.' path components and redundant separators while rejecting empty, absolute, and parent-directory-escaping paths. [crates/gwiki/src/support/text.rs:141-153]
- `slugify_with_options_applies_fallback_and_max_length` (function) component `slugify_with_options_applies_fallback_and_max_length [function]` (`68bfe972-fb6b-5463-b9b8-292389fe08ce`) lines 156-166 [crates/gwiki/src/support/text.rs:156-166]
  - Signature: `fn slugify_with_options_applies_fallback_and_max_length() {`
  - Purpose: Verifies that 'slugify_with_options' truncates the generated slug to the requested maximum length and falls back to the provided default when normalization yields an empty slug, while plain 'slugify' returns an empty string for non-slugifiable input. [crates/gwiki/src/support/text.rs:156-166]

