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

# crates/gwiki/src/audit/tests.rs

Module: [[code/modules/crates/gwiki/src/audit|crates/gwiki/src/audit]]

## Purpose

Test module for the audit and claim-extraction logic in `gwiki`: it exercises `run`, `claim_lines`, `unsupported_claims`, and the source-span helpers to verify how unsupported claims are reported, how scope and paths are preserved, and how markdown/frontmatter/comment parsing affects claim detection. The suite also covers Codewiki provenance handling, inline source citation validation, ignored-section configuration, and includes a small `WikiPage` fixture helper used by those cases.
[crates/gwiki/src/audit/tests.rs:14-48]
[crates/gwiki/src/audit/tests.rs:51-117]
[crates/gwiki/src/audit/tests.rs:120-145]
[crates/gwiki/src/audit/tests.rs:148-174]
[crates/gwiki/src/audit/tests.rs:177-196]

## API Symbols

- `reports_unsupported_claims` (function) component `reports_unsupported_claims [function]` (`97faef9e-0cc6-50c4-8781-fb1c8f0b9b67`) lines 14-48 [crates/gwiki/src/audit/tests.rs:14-48]
  - Signature: `fn reports_unsupported_claims() {`
  - Purpose: Verifies that 'run' reports a single unsupported claim for 'knowledge/topics/claims.md', including its line number, heading, claim text, and associated source context/citation. [crates/gwiki/src/audit/tests.rs:14-48]
- `generated_codewiki_numeric_claims_do_not_inherit_raw_source_context` (function) component `generated_codewiki_numeric_claims_do_not_inherit_raw_source_context [function]` (`9a36e866-3e86-5670-b8ea-74252b113b37`) lines 51-117 [crates/gwiki/src/audit/tests.rs:51-117]
  - Signature: `fn generated_codewiki_numeric_claims_do_not_inherit_raw_source_context() {`
  - Purpose: Verifies that numeric claims extracted from the generated 'code/_changes.md' page are reported as unsupported with empty 'source_context', rather than inheriting context from the registered raw source. [crates/gwiki/src/audit/tests.rs:51-117]
- `reports_include_paths_and_scope` (function) component `reports_include_paths_and_scope [function]` (`ed005516-2a0c-5c35-90ff-979240d44e6b`) lines 120-145 [crates/gwiki/src/audit/tests.rs:120-145]
  - Signature: `fn reports_include_paths_and_scope() {`
  - Purpose: Verifies that an audit report preserves the project scope identity in both the typed 'report.scope' field and serialized JSON, and that an unsupported claim is reported with the correct relative source path. [crates/gwiki/src/audit/tests.rs:120-145]
- `topic_scope_audits_only_topic_pages` (function) component `topic_scope_audits_only_topic_pages [function]` (`dedece25-7042-5177-9d93-9267ff9cfbd1`) lines 148-174 [crates/gwiki/src/audit/tests.rs:148-174]
  - Signature: `fn topic_scope_audits_only_topic_pages() {`
  - Purpose: Creates a temporary knowledge tree with one 'topic' page and one 'concept' page, runs 'run(root, ScopeIdentity::topic("ops"))', and asserts that only the topic page is reported as an unsupported claim. [crates/gwiki/src/audit/tests.rs:148-174]
- `frontmatter_closes_only_on_matching_document_start_delimiter` (function) component `frontmatter_closes_only_on_matching_document_start_delimiter [function]` (`dd053e87-efa9-535d-ad6c-eb4326276c90`) lines 177-196 [crates/gwiki/src/audit/tests.rs:177-196]
  - Signature: `fn frontmatter_closes_only_on_matching_document_start_delimiter() {`
  - Purpose: Verifies that frontmatter parsing ends only at a closing delimiter that matches the opening document-start delimiter, so '---' inside TOML '+++' frontmatter does not terminate it and both claims in the body are extracted. [crates/gwiki/src/audit/tests.rs:177-196]
- `multiline_html_comments_do_not_emit_claims` (function) component `multiline_html_comments_do_not_emit_claims [function]` (`46447086-db83-5d79-b2b0-2346d7c5d45c`) lines 199-219 [crates/gwiki/src/audit/tests.rs:199-219]
  - Signature: `fn multiline_html_comments_do_not_emit_claims() {`
  - Purpose: Verifies that 'claim_lines' ignores text inside multiline HTML comments and returns only the visible claims from the markdown page. [crates/gwiki/src/audit/tests.rs:199-219]
- `inline_source_support_requires_link_like_target` (function) component `inline_source_support_requires_link_like_target [function]` (`dd5581a2-0c40-59ea-a147-548057babc23`) lines 222-230 [crates/gwiki/src/audit/tests.rs:222-230]
  - Signature: `fn inline_source_support_requires_link_like_target() {`
  - Purpose: Verifies that 'has_inline_source_support' returns 'false' for plain text and 'true' only when the input contains a link-like target such as a URL or a bracketed source reference. [crates/gwiki/src/audit/tests.rs:222-230]
- `inline_source_support_accepts_codewiki_source_spans` (function) component `inline_source_support_accepts_codewiki_source_spans [function]` (`2d5a14a8-60f5-595f-a226-c0652d3b7a76`) lines 233-246 [crates/gwiki/src/audit/tests.rs:233-246]
  - Signature: `fn inline_source_support_accepts_codewiki_source_spans() {`
  - Purpose: Verifies that 'has_inline_source_support' recognizes valid Codewiki-style source citations with file-and-line or file-and-range spans, while rejecting non-source citations and invalid ranges. [crates/gwiki/src/audit/tests.rs:233-246]
- `codewiki_frontmatter_source_spans_support_structural_claims` (function) component `codewiki_frontmatter_source_spans_support_structural_claims [function]` (`710a6796-6b9c-5899-9831-2968de980256`) lines 249-286 [crates/gwiki/src/audit/tests.rs:249-286]
  - Signature: `fn codewiki_frontmatter_source_spans_support_structural_claims() {`
  - Purpose: Verifies that a 'WikiPage' with codewiki frontmatter source spans is recognized by 'has_codewiki_frontmatter_source_spans' and produces no unsupported structural claims from 'unsupported_claims'. [crates/gwiki/src/audit/tests.rs:249-286]
- `codewiki_contract_golden_page_counts_as_code_source_spans` (function) component `codewiki_contract_golden_page_counts_as_code_source_spans [function]` (`2d6ef56c-f898-558c-8e94-89557a7fb1a6`) lines 289-296 [crates/gwiki/src/audit/tests.rs:289-296]
  - Signature: `fn codewiki_contract_golden_page_counts_as_code_source_spans() {`
  - Purpose: Constructs the 'code/files/src/lib.rs.md' codewiki page using 'GOLDEN_PAGE' and asserts that it contains codewiki frontmatter source spans. [crates/gwiki/src/audit/tests.rs:289-296]
- `codewiki_frontmatter_source_spans_do_not_support_prose_claims` (function) component `codewiki_frontmatter_source_spans_do_not_support_prose_claims [function]` (`76af33b0-e5a2-50af-81f8-c3acd6070829`) lines 299-328 [crates/gwiki/src/audit/tests.rs:299-328]
  - Signature: `fn codewiki_frontmatter_source_spans_do_not_support_prose_claims() {`
  - Purpose: Verifies that a Codewiki page with frontmatter source spans still flags an unsupported prose sentence in the body as a single unsupported claim. [crates/gwiki/src/audit/tests.rs:299-328]
- `frontmatter_migration_audits_legacy_and_shared_sources_equivalently` (function) component `frontmatter_migration_audits_legacy_and_shared_sources_equivalently [function]` (`a9b91493-11bb-58a2-aafc-8dcf0aa19727`) lines 331-384 [crates/gwiki/src/audit/tests.rs:331-384]
  - Signature: `fn frontmatter_migration_audits_legacy_and_shared_sources_equivalently() {`
  - Purpose: Verifies that legacy frontmatter without 'provenance' is treated as missing source spans and yields one unsupported claim, while canonical frontmatter with 'provenance' is recognized as having codewiki source spans and produces no unsupported claims. [crates/gwiki/src/audit/tests.rs:331-384]
- `test_codewiki_page` (function) component `test_codewiki_page [function]` (`68c45157-0a33-5153-a3e6-73da88a3097c`) lines 386-395 [crates/gwiki/src/audit/tests.rs:386-395]
  - Signature: `fn test_codewiki_page(path: &str, markdown: &str) -> WikiPage {`
  - Purpose: Constructs and returns a 'WikiPage' test fixture from the given path and markdown by setting both path fields, copying the markdown, parsing it with 'parse_markdown' using an empty iterator, and marking 'has_frontmatter' as 'true'. [crates/gwiki/src/audit/tests.rs:386-395]
- `configured_ignored_sections_extend_defaults` (function) component `configured_ignored_sections_extend_defaults [function]` (`1082329c-dee9-5555-9155-5104368d8d6b`) lines 398-417 [crates/gwiki/src/audit/tests.rs:398-417]
  - Signature: `fn configured_ignored_sections_extend_defaults() {`
  - Purpose: Verifies that 'AuditOptions::with_additional_ignored_sections(["Notes"])' extends the default ignored-section set so 'claim_lines' returns only the top-level claim and excludes text under both '## Notes' and the default-ignored '## Sources' sections. [crates/gwiki/src/audit/tests.rs:398-417]

