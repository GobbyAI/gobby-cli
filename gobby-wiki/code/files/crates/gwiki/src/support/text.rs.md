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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/support/text.rs:7-13](crates/gwiki/src/support/text.rs#L7-L13), [crates/gwiki/src/support/text.rs:15-22](crates/gwiki/src/support/text.rs#L15-L22), [crates/gwiki/src/support/text.rs:26-46](crates/gwiki/src/support/text.rs#L26-L46), [crates/gwiki/src/support/text.rs:48-59](crates/gwiki/src/support/text.rs#L48-L59), [crates/gwiki/src/support/text.rs:61-73](crates/gwiki/src/support/text.rs#L61-L73), [crates/gwiki/src/support/text.rs:75-83](crates/gwiki/src/support/text.rs#L75-L83), [crates/gwiki/src/support/text.rs:85-91](crates/gwiki/src/support/text.rs#L85-L91), [crates/gwiki/src/support/text.rs:93-95](crates/gwiki/src/support/text.rs#L93-L95), [crates/gwiki/src/support/text.rs:97-99](crates/gwiki/src/support/text.rs#L97-L99), [crates/gwiki/src/support/text.rs:101-126](crates/gwiki/src/support/text.rs#L101-L126), [crates/gwiki/src/support/text.rs:133-138](crates/gwiki/src/support/text.rs#L133-L138), [crates/gwiki/src/support/text.rs:141-153](crates/gwiki/src/support/text.rs#L141-L153), [crates/gwiki/src/support/text.rs:156-166](crates/gwiki/src/support/text.rs#L156-L166)

</details>

# crates/gwiki/src/support/text.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

Utilities for query handling, text normalization, and display labels used by `gwiki` support code. The file splits search queries into lowercase tokens, scores text against those tokens, sanitizes code paths into safe repo-relative strings, and extracts short snippets from larger text. It also maps degradation and document/object kinds into stable label strings, and provides slugification and path-display helpers, with tests covering path sanitization, snippet ellipsis handling, and slugify fallback/max-length behavior.
[crates/gwiki/src/support/text.rs:7-13]
[crates/gwiki/src/support/text.rs:15-22]
[crates/gwiki/src/support/text.rs:26-46]
[crates/gwiki/src/support/text.rs:48-59]
[crates/gwiki/src/support/text.rs:61-73]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `query_tokens` | function | `pub(crate) fn query_tokens(query: &str) -> Vec<String> {` | `query_tokens [function]` | `9d7a2ce6-8feb-5fb6-aa36-19986c3ef7b7` | 7-13 [crates/gwiki/src/support/text.rs:7-13] | Indexed function `query_tokens` in `crates/gwiki/src/support/text.rs`. [crates/gwiki/src/support/text.rs:7-13] |
| `keyword_score` | function | `pub(crate) fn keyword_score(text: &str, tokens: &[String]) -> usize {` | `keyword_score [function]` | `91790d1a-0fe3-5fc3-ab61-2655714dc637` | 15-22 [crates/gwiki/src/support/text.rs:15-22] | Indexed function `keyword_score` in `crates/gwiki/src/support/text.rs`. [crates/gwiki/src/support/text.rs:15-22] |
| `sanitize_code_path` | function | `pub(crate) fn sanitize_code_path(path: &str) -> Option<String> {` | `sanitize_code_path [function]` | `e6ee4298-a16f-59b0-8280-90cadaa5fcc3` | 26-46 [crates/gwiki/src/support/text.rs:26-46] | Indexed function `sanitize_code_path` in `crates/gwiki/src/support/text.rs`. [crates/gwiki/src/support/text.rs:26-46] |
| `snippet_from_text` | function | `pub(crate) fn snippet_from_text(text: &str) -> String {` | `snippet_from_text [function]` | `a19532b2-de2b-59bd-8b3b-75376c885954` | 48-59 [crates/gwiki/src/support/text.rs:48-59] | Indexed function `snippet_from_text` in `crates/gwiki/src/support/text.rs`. [crates/gwiki/src/support/text.rs:48-59] |
| `degradation_label` | function | `pub(crate) fn degradation_label(degradation: &DegradationKind) -> String {` | `degradation_label [function]` | `67129cf2-e917-5cd9-b30a-aed2a05b5be1` | 61-73 [crates/gwiki/src/support/text.rs:61-73] | Indexed function `degradation_label` in `crates/gwiki/src/support/text.rs`. [crates/gwiki/src/support/text.rs:61-73] |
| `document_kind_name` | function | `pub(crate) fn document_kind_name(kind: store::WikiDocumentKind) -> &'static str {` | `document_kind_name [function]` | `d42b4658-ebe0-52ae-a9e1-373a5a81d760` | 75-83 [crates/gwiki/src/support/text.rs:75-83] | Indexed function `document_kind_name` in `crates/gwiki/src/support/text.rs`. [crates/gwiki/src/support/text.rs:75-83] |
| `postgres_object_kind` | function | `pub(crate) fn postgres_object_kind(kind: setup::GwikiPostgresObjectKind) -> &'static str {` | `postgres_object_kind [function]` | `972dc6e5-2409-58d6-b9ed-89de9de3b427` | 85-91 [crates/gwiki/src/support/text.rs:85-91] | Indexed function `postgres_object_kind` in `crates/gwiki/src/support/text.rs`. [crates/gwiki/src/support/text.rs:85-91] |
| `display_path` | function | `pub(crate) fn display_path(path: &Path) -> String {` | `display_path [function]` | `a33408bc-a2eb-574c-b231-09c256188203` | 93-95 [crates/gwiki/src/support/text.rs:93-95] | Indexed function `display_path` in `crates/gwiki/src/support/text.rs`. [crates/gwiki/src/support/text.rs:93-95] |
| `slugify` | function | `pub(crate) fn slugify(value: &str) -> String {` | `slugify [function]` | `f9678e6e-5cab-5644-9005-69225719f089` | 97-99 [crates/gwiki/src/support/text.rs:97-99] | Indexed function `slugify` in `crates/gwiki/src/support/text.rs`. [crates/gwiki/src/support/text.rs:97-99] |
| `slugify_with_options` | function | `pub(crate) fn slugify_with_options(` | `slugify_with_options [function]` | `85deb1dd-437d-5e93-bed7-18ce0f2b4493` | 101-126 [crates/gwiki/src/support/text.rs:101-126] | Indexed function `slugify_with_options` in `crates/gwiki/src/support/text.rs`. [crates/gwiki/src/support/text.rs:101-126] |
| `snippets_reserve_space_for_ellipsis` | function | `fn snippets_reserve_space_for_ellipsis() {` | `snippets_reserve_space_for_ellipsis [function]` | `9e229e53-0e5c-5140-b948-55f4b02e870a` | 133-138 [crates/gwiki/src/support/text.rs:133-138] | Indexed function `snippets_reserve_space_for_ellipsis` in `crates/gwiki/src/support/text.rs`. [crates/gwiki/src/support/text.rs:133-138] |
| `sanitize_code_path_strips_current_dir_components` | function | `fn sanitize_code_path_strips_current_dir_components() {` | `sanitize_code_path_strips_current_dir_components [function]` | `8cf79b6a-4e06-5249-bb09-a271f3e99c7a` | 141-153 [crates/gwiki/src/support/text.rs:141-153] | Indexed function `sanitize_code_path_strips_current_dir_components` in `crates/gwiki/src/support/text.rs`. [crates/gwiki/src/support/text.rs:141-153] |
| `slugify_with_options_applies_fallback_and_max_length` | function | `fn slugify_with_options_applies_fallback_and_max_length() {` | `slugify_with_options_applies_fallback_and_max_length [function]` | `68bfe972-fb6b-5463-b9b8-292389fe08ce` | 156-166 [crates/gwiki/src/support/text.rs:156-166] | Indexed function `slugify_with_options_applies_fallback_and_max_length` in `crates/gwiki/src/support/text.rs`. [crates/gwiki/src/support/text.rs:156-166] |
