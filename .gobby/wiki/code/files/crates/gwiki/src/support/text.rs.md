---
title: crates/gwiki/src/support/text.rs
type: code_file
provenance:
- file: crates/gwiki/src/support/text.rs
  ranges:
  - 7-13
  - 15-22
  - 24-35
  - 37-49
  - 51-59
  - 61-67
  - 69-71
  - 73-75
  - 77-102
  - 109-114
  - 117-127
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/support/text.rs

Module: [[code/modules/crates/gwiki/src/support|crates/gwiki/src/support]]

## Purpose

`crates/gwiki/src/support/text.rs` exposes 11 indexed API symbols.
[crates/gwiki/src/support/text.rs:7-13]
[crates/gwiki/src/support/text.rs:15-22]
[crates/gwiki/src/support/text.rs:24-35]
[crates/gwiki/src/support/text.rs:37-49]
[crates/gwiki/src/support/text.rs:51-59]

## API Symbols

- `query_tokens` (function) component `query_tokens [function]` (`9d7a2ce6-8feb-5fb6-aa36-19986c3ef7b7`) lines 7-13 [crates/gwiki/src/support/text.rs:7-13]
  - Signature: `pub(crate) fn query_tokens(query: &str) -> Vec<String> {`
  - Purpose: This function tokenizes a query string by splitting on non-alphanumeric characters, filtering empty tokens, and converting the results to lowercase. [crates/gwiki/src/support/text.rs:7-13]
- `keyword_score` (function) component `keyword_score [function]` (`91790d1a-0fe3-5fc3-ab61-2655714dc637`) lines 15-22 [crates/gwiki/src/support/text.rs:15-22]
  - Signature: `pub(crate) fn keyword_score(text: &str, tokens: &[String]) -> usize {`
  - Purpose: Counts the total occurrences of all provided normalized tokens within a case-insensitive version of the input text. [crates/gwiki/src/support/text.rs:15-22]
- `snippet_from_text` (function) component `snippet_from_text [function]` (`565c6461-166f-5d18-91c6-23b28a664e08`) lines 24-35 [crates/gwiki/src/support/text.rs:24-35]
  - Signature: `pub(crate) fn snippet_from_text(text: &str) -> String {`
  - Purpose: Extracts the first non-empty line from the input text, trims it, and returns it truncated to 240 characters with '...' appended if it exceeds that length. [crates/gwiki/src/support/text.rs:24-35]
- `degradation_label` (function) component `degradation_label [function]` (`dd4c773e-02ab-5f4e-8e61-b20704393db1`) lines 37-49 [crates/gwiki/src/support/text.rs:37-49]
  - Signature: `pub(crate) fn degradation_label(degradation: &DegradationKind) -> String {`
  - Purpose: Maps a `DegradationKind` enum variant to its corresponding string label representation, with service unavailability cases further differentiated by their `ServiceState`. [crates/gwiki/src/support/text.rs:37-49]
- `document_kind_name` (function) component `document_kind_name [function]` (`cd9bfc9c-9322-5e23-91f2-e44d1ea31620`) lines 51-59 [crates/gwiki/src/support/text.rs:51-59]
  - Signature: `pub(crate) fn document_kind_name(kind: store::WikiDocumentKind) -> &'static str {`
  - Purpose: Maps a `WikiDocumentKind` enum variant to its corresponding static string identifier. [crates/gwiki/src/support/text.rs:51-59]
- `postgres_object_kind` (function) component `postgres_object_kind [function]` (`fb1bdf5a-98ea-5331-88a5-099bb1fb3caa`) lines 61-67 [crates/gwiki/src/support/text.rs:61-67]
  - Signature: `pub(crate) fn postgres_object_kind(kind: setup::GwikiPostgresObjectKind) -> &'static str {`
  - Purpose: Maps `GwikiPostgresObjectKind` enum variants to their corresponding static string representations via pattern matching. [crates/gwiki/src/support/text.rs:61-67]
- `display_path` (function) component `display_path [function]` (`865de779-6685-5a45-9b5b-52923941e2ee`) lines 69-71 [crates/gwiki/src/support/text.rs:69-71]
  - Signature: `pub(crate) fn display_path(path: &Path) -> String {`
  - Purpose: Converts a `Path` to a UTF-8 string representation with all backslashes normalized to forward slashes. [crates/gwiki/src/support/text.rs:69-71]
- `slugify` (function) component `slugify [function]` (`2e6f0d32-a201-59b5-81e4-20be67a8adcf`) lines 73-75 [crates/gwiki/src/support/text.rs:73-75]
  - Signature: `pub(crate) fn slugify(value: &str) -> String {`
  - Purpose: Wraps `slugify_with_options` to convert a string to a URL-friendly slug using default configuration parameters. [crates/gwiki/src/support/text.rs:73-75]
- `slugify_with_options` (function) component `slugify_with_options [function]` (`b80d26fc-3355-527f-aa2c-8df0bf8e79d6`) lines 77-102 [crates/gwiki/src/support/text.rs:77-102]
  - Signature: `pub(crate) fn slugify_with_options(`
  - Purpose: Converts a string into a lowercase, ASCII-alphanumeric slug with single-dash word delimiters, optionally truncated to a maximum length and falling back to a provided string if the result is empty. [crates/gwiki/src/support/text.rs:77-102]
- `snippets_reserve_space_for_ellipsis` (function) component `snippets_reserve_space_for_ellipsis [function]` (`3dc3cb65-c67f-558c-9095-1f919ab863c2`) lines 109-114 [crates/gwiki/src/support/text.rs:109-114]
  - Signature: `fn snippets_reserve_space_for_ellipsis() {`
  - Purpose: Tests that `snippet_from_text` truncates input strings to exactly 240 characters while appending a trailing ellipsis marker. [crates/gwiki/src/support/text.rs:109-114]
- `slugify_with_options_applies_fallback_and_max_length` (function) component `slugify_with_options_applies_fallback_and_max_length [function]` (`22092578-41f7-5706-83d1-92d63e86a0f5`) lines 117-127 [crates/gwiki/src/support/text.rs:117-127]
  - Signature: `fn slugify_with_options_applies_fallback_and_max_length() {`
  - Purpose: This unit test verifies that `slugify_with_options` correctly truncates slugs to a maximum length limit and returns a fallback value when the generated slug would be empty. [crates/gwiki/src/support/text.rs:117-127]

