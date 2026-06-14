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

This file provides shared text utilities for gwiki: it tokenizes search queries, scores text against normalized keywords, safely normalizes code paths to repo-relative form, extracts short snippets from text, and maps degradation states and document/object kinds to stable labels or names. It also exposes slugification helpers plus a small path display helper, so the rest of the crate can reuse consistent text normalization, indexing, and user-facing formatting rules from one place.
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
  - Purpose: Indexed function `sanitize_code_path` in `crates/gwiki/src/support/text.rs`. [crates/gwiki/src/support/text.rs:26-46]
- `snippet_from_text` (function) component `snippet_from_text [function]` (`a19532b2-de2b-59bd-8b3b-75376c885954`) lines 48-59 [crates/gwiki/src/support/text.rs:48-59]
  - Signature: `pub(crate) fn snippet_from_text(text: &str) -> String {`
  - Purpose: Indexed function `snippet_from_text` in `crates/gwiki/src/support/text.rs`. [crates/gwiki/src/support/text.rs:48-59]
- `degradation_label` (function) component `degradation_label [function]` (`67129cf2-e917-5cd9-b30a-aed2a05b5be1`) lines 61-73 [crates/gwiki/src/support/text.rs:61-73]
  - Signature: `pub(crate) fn degradation_label(degradation: &DegradationKind) -> String {`
  - Purpose: Indexed function `degradation_label` in `crates/gwiki/src/support/text.rs`. [crates/gwiki/src/support/text.rs:61-73]
- `document_kind_name` (function) component `document_kind_name [function]` (`d42b4658-ebe0-52ae-a9e1-373a5a81d760`) lines 75-83 [crates/gwiki/src/support/text.rs:75-83]
  - Signature: `pub(crate) fn document_kind_name(kind: store::WikiDocumentKind) -> &'static str {`
  - Purpose: Indexed function `document_kind_name` in `crates/gwiki/src/support/text.rs`. [crates/gwiki/src/support/text.rs:75-83]
- `postgres_object_kind` (function) component `postgres_object_kind [function]` (`972dc6e5-2409-58d6-b9ed-89de9de3b427`) lines 85-91 [crates/gwiki/src/support/text.rs:85-91]
  - Signature: `pub(crate) fn postgres_object_kind(kind: setup::GwikiPostgresObjectKind) -> &'static str {`
  - Purpose: Indexed function `postgres_object_kind` in `crates/gwiki/src/support/text.rs`. [crates/gwiki/src/support/text.rs:85-91]
- `display_path` (function) component `display_path [function]` (`a33408bc-a2eb-574c-b231-09c256188203`) lines 93-95 [crates/gwiki/src/support/text.rs:93-95]
  - Signature: `pub(crate) fn display_path(path: &Path) -> String {`
  - Purpose: Indexed function `display_path` in `crates/gwiki/src/support/text.rs`. [crates/gwiki/src/support/text.rs:93-95]
- `slugify` (function) component `slugify [function]` (`f9678e6e-5cab-5644-9005-69225719f089`) lines 97-99 [crates/gwiki/src/support/text.rs:97-99]
  - Signature: `pub(crate) fn slugify(value: &str) -> String {`
  - Purpose: Indexed function `slugify` in `crates/gwiki/src/support/text.rs`. [crates/gwiki/src/support/text.rs:97-99]
- `slugify_with_options` (function) component `slugify_with_options [function]` (`85deb1dd-437d-5e93-bed7-18ce0f2b4493`) lines 101-126 [crates/gwiki/src/support/text.rs:101-126]
  - Signature: `pub(crate) fn slugify_with_options(`
  - Purpose: Indexed function `slugify_with_options` in `crates/gwiki/src/support/text.rs`. [crates/gwiki/src/support/text.rs:101-126]
- `snippets_reserve_space_for_ellipsis` (function) component `snippets_reserve_space_for_ellipsis [function]` (`9e229e53-0e5c-5140-b948-55f4b02e870a`) lines 133-138 [crates/gwiki/src/support/text.rs:133-138]
  - Signature: `fn snippets_reserve_space_for_ellipsis() {`
  - Purpose: Indexed function `snippets_reserve_space_for_ellipsis` in `crates/gwiki/src/support/text.rs`. [crates/gwiki/src/support/text.rs:133-138]
- `sanitize_code_path_strips_current_dir_components` (function) component `sanitize_code_path_strips_current_dir_components [function]` (`8cf79b6a-4e06-5249-bb09-a271f3e99c7a`) lines 141-153 [crates/gwiki/src/support/text.rs:141-153]
  - Signature: `fn sanitize_code_path_strips_current_dir_components() {`
  - Purpose: Indexed function `sanitize_code_path_strips_current_dir_components` in `crates/gwiki/src/support/text.rs`. [crates/gwiki/src/support/text.rs:141-153]
- `slugify_with_options_applies_fallback_and_max_length` (function) component `slugify_with_options_applies_fallback_and_max_length [function]` (`68bfe972-fb6b-5463-b9b8-292389fe08ce`) lines 156-166 [crates/gwiki/src/support/text.rs:156-166]
  - Signature: `fn slugify_with_options_applies_fallback_and_max_length() {`
  - Purpose: Indexed function `slugify_with_options_applies_fallback_and_max_length` in `crates/gwiki/src/support/text.rs`. [crates/gwiki/src/support/text.rs:156-166]

