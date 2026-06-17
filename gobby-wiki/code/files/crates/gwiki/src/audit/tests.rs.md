---
title: crates/gwiki/src/audit/tests.rs
type: code_file
provenance:
- file: crates/gwiki/src/audit/tests.rs
  ranges:
  - 14-48
  - 51-117
  - 120-145
  - 148-174
  - 177-196
  - 199-219
  - 222-230
  - 233-246
  - 249-286
  - 289-296
  - 299-328
  - 331-384
  - 386-395
  - 398-417
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/audit/tests.rs:14-48](crates/gwiki/src/audit/tests.rs#L14-L48), [crates/gwiki/src/audit/tests.rs:51-117](crates/gwiki/src/audit/tests.rs#L51-L117), [crates/gwiki/src/audit/tests.rs:120-145](crates/gwiki/src/audit/tests.rs#L120-L145), [crates/gwiki/src/audit/tests.rs:148-174](crates/gwiki/src/audit/tests.rs#L148-L174), [crates/gwiki/src/audit/tests.rs:177-196](crates/gwiki/src/audit/tests.rs#L177-L196), [crates/gwiki/src/audit/tests.rs:199-219](crates/gwiki/src/audit/tests.rs#L199-L219), [crates/gwiki/src/audit/tests.rs:222-230](crates/gwiki/src/audit/tests.rs#L222-L230), [crates/gwiki/src/audit/tests.rs:233-246](crates/gwiki/src/audit/tests.rs#L233-L246), [crates/gwiki/src/audit/tests.rs:249-286](crates/gwiki/src/audit/tests.rs#L249-L286), [crates/gwiki/src/audit/tests.rs:289-296](crates/gwiki/src/audit/tests.rs#L289-L296), [crates/gwiki/src/audit/tests.rs:299-328](crates/gwiki/src/audit/tests.rs#L299-L328), [crates/gwiki/src/audit/tests.rs:331-384](crates/gwiki/src/audit/tests.rs#L331-L384), [crates/gwiki/src/audit/tests.rs:386-395](crates/gwiki/src/audit/tests.rs#L386-L395), [crates/gwiki/src/audit/tests.rs:398-417](crates/gwiki/src/audit/tests.rs#L398-L417)

</details>

# crates/gwiki/src/audit/tests.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file is an audit test suite for wiki page claim extraction and source-context rules. It sets up temporary wiki roots, registers source manifests, and runs the audit pipeline to verify that unsupported claims are reported with the correct path, line, heading, and citation data; that generated codewiki numeric claims do not accidentally inherit raw source context; that reports preserve path and scope information; that topic audits only inspect topic pages; that frontmatter and HTML comment parsing behave correctly; and that inline or frontmatter source spans are accepted or rejected according to claim type, migration mode, and configured ignored sections.
[crates/gwiki/src/audit/tests.rs:14-48]
[crates/gwiki/src/audit/tests.rs:51-117]
[crates/gwiki/src/audit/tests.rs:120-145]
[crates/gwiki/src/audit/tests.rs:148-174]
[crates/gwiki/src/audit/tests.rs:177-196]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `reports_unsupported_claims` | function | `fn reports_unsupported_claims() {` | `reports_unsupported_claims [function]` | `97faef9e-0cc6-50c4-8781-fb1c8f0b9b67` | 14-48 [crates/gwiki/src/audit/tests.rs:14-48] | Indexed function `reports_unsupported_claims` in `crates/gwiki/src/audit/tests.rs`. [crates/gwiki/src/audit/tests.rs:14-48] |
| `generated_codewiki_numeric_claims_do_not_inherit_raw_source_context` | function | `fn generated_codewiki_numeric_claims_do_not_inherit_raw_source_context() {` | `generated_codewiki_numeric_claims_do_not_inherit_raw_source_context [function]` | `9a36e866-3e86-5670-b8ea-74252b113b37` | 51-117 [crates/gwiki/src/audit/tests.rs:51-117] | Indexed function `generated_codewiki_numeric_claims_do_not_inherit_raw_source_context` in `crates/gwiki/src/audit/tests.rs`. [crates/gwiki/src/audit/tests.rs:51-117] |
| `reports_include_paths_and_scope` | function | `fn reports_include_paths_and_scope() {` | `reports_include_paths_and_scope [function]` | `ed005516-2a0c-5c35-90ff-979240d44e6b` | 120-145 [crates/gwiki/src/audit/tests.rs:120-145] | Indexed function `reports_include_paths_and_scope` in `crates/gwiki/src/audit/tests.rs`. [crates/gwiki/src/audit/tests.rs:120-145] |
| `topic_scope_audits_only_topic_pages` | function | `fn topic_scope_audits_only_topic_pages() {` | `topic_scope_audits_only_topic_pages [function]` | `dedece25-7042-5177-9d93-9267ff9cfbd1` | 148-174 [crates/gwiki/src/audit/tests.rs:148-174] | Indexed function `topic_scope_audits_only_topic_pages` in `crates/gwiki/src/audit/tests.rs`. [crates/gwiki/src/audit/tests.rs:148-174] |
| `frontmatter_closes_only_on_matching_document_start_delimiter` | function | `fn frontmatter_closes_only_on_matching_document_start_delimiter() {` | `frontmatter_closes_only_on_matching_document_start_delimiter [function]` | `dd053e87-efa9-535d-ad6c-eb4326276c90` | 177-196 [crates/gwiki/src/audit/tests.rs:177-196] | Indexed function `frontmatter_closes_only_on_matching_document_start_delimiter` in `crates/gwiki/src/audit/tests.rs`. [crates/gwiki/src/audit/tests.rs:177-196] |
| `multiline_html_comments_do_not_emit_claims` | function | `fn multiline_html_comments_do_not_emit_claims() {` | `multiline_html_comments_do_not_emit_claims [function]` | `46447086-db83-5d79-b2b0-2346d7c5d45c` | 199-219 [crates/gwiki/src/audit/tests.rs:199-219] | Indexed function `multiline_html_comments_do_not_emit_claims` in `crates/gwiki/src/audit/tests.rs`. [crates/gwiki/src/audit/tests.rs:199-219] |
| `inline_source_support_requires_link_like_target` | function | `fn inline_source_support_requires_link_like_target() {` | `inline_source_support_requires_link_like_target [function]` | `dd5581a2-0c40-59ea-a147-548057babc23` | 222-230 [crates/gwiki/src/audit/tests.rs:222-230] | Indexed function `inline_source_support_requires_link_like_target` in `crates/gwiki/src/audit/tests.rs`. [crates/gwiki/src/audit/tests.rs:222-230] |
| `inline_source_support_accepts_codewiki_source_spans` | function | `fn inline_source_support_accepts_codewiki_source_spans() {` | `inline_source_support_accepts_codewiki_source_spans [function]` | `2d5a14a8-60f5-595f-a226-c0652d3b7a76` | 233-246 [crates/gwiki/src/audit/tests.rs:233-246] | Indexed function `inline_source_support_accepts_codewiki_source_spans` in `crates/gwiki/src/audit/tests.rs`. [crates/gwiki/src/audit/tests.rs:233-246] |
| `codewiki_frontmatter_source_spans_support_structural_claims` | function | `fn codewiki_frontmatter_source_spans_support_structural_claims() {` | `codewiki_frontmatter_source_spans_support_structural_claims [function]` | `710a6796-6b9c-5899-9831-2968de980256` | 249-286 [crates/gwiki/src/audit/tests.rs:249-286] | Indexed function `codewiki_frontmatter_source_spans_support_structural_claims` in `crates/gwiki/src/audit/tests.rs`. [crates/gwiki/src/audit/tests.rs:249-286] |
| `codewiki_contract_golden_page_counts_as_code_source_spans` | function | `fn codewiki_contract_golden_page_counts_as_code_source_spans() {` | `codewiki_contract_golden_page_counts_as_code_source_spans [function]` | `2d6ef56c-f898-558c-8e94-89557a7fb1a6` | 289-296 [crates/gwiki/src/audit/tests.rs:289-296] | Indexed function `codewiki_contract_golden_page_counts_as_code_source_spans` in `crates/gwiki/src/audit/tests.rs`. [crates/gwiki/src/audit/tests.rs:289-296] |
| `codewiki_frontmatter_source_spans_do_not_support_prose_claims` | function | `fn codewiki_frontmatter_source_spans_do_not_support_prose_claims() {` | `codewiki_frontmatter_source_spans_do_not_support_prose_claims [function]` | `76af33b0-e5a2-50af-81f8-c3acd6070829` | 299-328 [crates/gwiki/src/audit/tests.rs:299-328] | Indexed function `codewiki_frontmatter_source_spans_do_not_support_prose_claims` in `crates/gwiki/src/audit/tests.rs`. [crates/gwiki/src/audit/tests.rs:299-328] |
| `frontmatter_migration_audits_legacy_and_shared_sources_equivalently` | function | `fn frontmatter_migration_audits_legacy_and_shared_sources_equivalently() {` | `frontmatter_migration_audits_legacy_and_shared_sources_equivalently [function]` | `a9b91493-11bb-58a2-aafc-8dcf0aa19727` | 331-384 [crates/gwiki/src/audit/tests.rs:331-384] | Indexed function `frontmatter_migration_audits_legacy_and_shared_sources_equivalently` in `crates/gwiki/src/audit/tests.rs`. [crates/gwiki/src/audit/tests.rs:331-384] |
| `test_codewiki_page` | function | `fn test_codewiki_page(path: &str, markdown: &str) -> WikiPage {` | `test_codewiki_page [function]` | `68c45157-0a33-5153-a3e6-73da88a3097c` | 386-395 [crates/gwiki/src/audit/tests.rs:386-395] | Indexed function `test_codewiki_page` in `crates/gwiki/src/audit/tests.rs`. [crates/gwiki/src/audit/tests.rs:386-395] |
| `configured_ignored_sections_extend_defaults` | function | `fn configured_ignored_sections_extend_defaults() {` | `configured_ignored_sections_extend_defaults [function]` | `1082329c-dee9-5555-9155-5104368d8d6b` | 398-417 [crates/gwiki/src/audit/tests.rs:398-417] | Indexed function `configured_ignored_sections_extend_defaults` in `crates/gwiki/src/audit/tests.rs`. [crates/gwiki/src/audit/tests.rs:398-417] |
