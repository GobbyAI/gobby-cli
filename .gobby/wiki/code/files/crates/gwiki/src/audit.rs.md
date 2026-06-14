---
title: crates/gwiki/src/audit.rs
type: code_file
provenance:
- file: crates/gwiki/src/audit.rs
  ranges:
  - 33-35
  - 37-73
  - 75-84
  - 87-93
  - 96-103
  - 106-111
  - 114-116
  - 118-141
  - 143-172
  - 174-186
  - 188-195
  - 197-226
  - 228-237
  - 239-244
  - 246-255
  - 257-262
  - 264-280
  - 282-288
  - 290-327
  - 330-335
  - 338-341
  - 348-425
  - 427-433
  - 435-444
  - 446-450
  - 452-454
  - 456-463
  - 465-477
  - 479-487
  - 489-502
  - 504-509
  - 511-516
  - 518-529
  - 531-553
  - 561-595
  - 598-664
  - 667-692
  - 695-722
  - 725-744
  - 747-767
  - 770-778
  - 781-794
  - 797-834
  - 837-844
  - 847-876
  - 879-932
  - 934-943
  - 946-965
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/audit.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file implements the wiki audit logic for checking claim provenance and reporting unsupported content. `AuditOptions` builds the audit configuration, seeding a default set of ignored section headings and optionally extending it from the `GOBBY_WIKI_AUDIT_IGNORED_SECTIONS` environment variable or caller-provided sections; its helper methods normalize headings before matching. `AuditReport`, `UnsupportedClaim`, `AuditSourceContext`, and `ClaimLine` model the structured audit output, while `run` and `run_with_options` drive the audit over collected pages and provenance data. The remaining functions break the audit into focused checks: they render reports, derive source context, identify generated Codewiki pages and valid source spans, classify claim lines and kinds, filter out ignored or structural claims, and decide whether claims are supported by inline sources, frontmatter, or path/scope rules. The tests at the bottom encode the contract for those rules, especially around generated pages, frontmatter handling, ignored sections, and which claims should or should not be reported.
[crates/gwiki/src/audit.rs:33-35]
[crates/gwiki/src/audit.rs:37-73]
[crates/gwiki/src/audit.rs:38-44]
[crates/gwiki/src/audit.rs:47-54]
[crates/gwiki/src/audit.rs:56-59]

## API Symbols

- `AuditOptions` (class) component `AuditOptions [class]` (`962b6a4c-e33b-5686-aa38-1699c9cd8005`) lines 33-35 [crates/gwiki/src/audit.rs:33-35]
  - Signature: `pub struct AuditOptions {`
  - Purpose: Indexed class `AuditOptions` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:33-35]
- `AuditOptions` (class) component `AuditOptions [class]` (`5662f13d-2458-5b0d-9fd3-8aea928a23b4`) lines 37-73 [crates/gwiki/src/audit.rs:37-73]
  - Signature: `impl AuditOptions {`
  - Purpose: Indexed class `AuditOptions` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:37-73]
- `AuditOptions.from_env` (method) component `AuditOptions.from_env [method]` (`1c519df6-86e8-57cd-b97c-ee12e75c6ea3`) lines 38-44 [crates/gwiki/src/audit.rs:38-44]
  - Signature: `pub fn from_env() -> Self {`
  - Purpose: Indexed method `AuditOptions.from_env` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:38-44]
- `AuditOptions.with_additional_ignored_sections` (method) component `AuditOptions.with_additional_ignored_sections [method]` (`b859bdeb-9413-5ae4-8d9b-c15b7cfa4c98`) lines 47-54 [crates/gwiki/src/audit.rs:47-54]
  - Signature: `pub fn with_additional_ignored_sections<I, S>(mut self, sections: I) -> Self`
  - Purpose: Indexed method `AuditOptions.with_additional_ignored_sections` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:47-54]
- `AuditOptions.ignores_section` (method) component `AuditOptions.ignores_section [method]` (`dcde16b8-964d-5c4f-ab33-dddcf3a5883c`) lines 56-59 [crates/gwiki/src/audit.rs:56-59]
  - Signature: `fn ignores_section(&self, heading: &str) -> bool {`
  - Purpose: Indexed method `AuditOptions.ignores_section` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:56-59]
- `AuditOptions.extend_ignored_sections` (method) component `AuditOptions.extend_ignored_sections [method]` (`d4d64256-21a8-5aa4-975f-ab0106fcb60a`) lines 61-72 [crates/gwiki/src/audit.rs:61-72]
  - Signature: `fn extend_ignored_sections<I, S>(&mut self, sections: I)`
  - Purpose: Indexed method `AuditOptions.extend_ignored_sections` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:61-72]
- `AuditOptions` (class) component `AuditOptions [class]` (`5e1efccb-ad24-5d5c-9a3b-697587f1f195`) lines 75-84 [crates/gwiki/src/audit.rs:75-84]
  - Signature: `impl Default for AuditOptions {`
  - Purpose: Indexed class `AuditOptions` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:75-84]
- `AuditOptions.default` (method) component `AuditOptions.default [method]` (`908d6750-a06a-51a8-82cb-8ceea1479abc`) lines 76-83 [crates/gwiki/src/audit.rs:76-83]
  - Signature: `fn default() -> Self {`
  - Purpose: Indexed method `AuditOptions.default` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:76-83]
- `AuditReport` (class) component `AuditReport [class]` (`a785c503-904f-543d-b13b-b1a4def6ff79`) lines 87-93 [crates/gwiki/src/audit.rs:87-93]
  - Signature: `pub struct AuditReport {`
  - Purpose: Indexed class `AuditReport` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:87-93]
- `UnsupportedClaim` (class) component `UnsupportedClaim [class]` (`9e360145-a461-5c3c-baac-f93d8ea4e49b`) lines 96-103 [crates/gwiki/src/audit.rs:96-103]
  - Signature: `pub struct UnsupportedClaim {`
  - Purpose: Indexed class `UnsupportedClaim` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:96-103]
- `AuditSourceContext` (class) component `AuditSourceContext [class]` (`a22bfb9d-a06c-5984-ae6f-b460d19b96ee`) lines 106-111 [crates/gwiki/src/audit.rs:106-111]
  - Signature: `pub struct AuditSourceContext {`
  - Purpose: Indexed class `AuditSourceContext` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:106-111]
- `run` (function) component `run [function]` (`86557e81-e8f0-519d-8859-18555ca2ed1c`) lines 114-116 [crates/gwiki/src/audit.rs:114-116]
  - Signature: `pub fn run(vault_root: &Path, scope: ScopeIdentity) -> Result<AuditReport, WikiError> {`
  - Purpose: Indexed function `run` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:114-116]
- `run_with_options` (function) component `run_with_options [function]` (`8b19636c-46b2-5ba5-a426-e439b948746d`) lines 118-141 [crates/gwiki/src/audit.rs:118-141]
  - Signature: `pub fn run_with_options(`
  - Purpose: Indexed function `run_with_options` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:118-141]
- `render_text` (function) component `render_text [function]` (`dbe9e3fb-74b1-59a9-b799-1f7873dfb188`) lines 143-172 [crates/gwiki/src/audit.rs:143-172]
  - Signature: `pub fn render_text(report: &AuditReport) -> String {`
  - Purpose: Indexed function `render_text` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:143-172]
- `source_context` (function) component `source_context [function]` (`45f40063-8b04-5a0d-b04a-25fecd2361a0`) lines 174-186 [crates/gwiki/src/audit.rs:174-186]
  - Signature: `fn source_context(vault_root: &Path) -> Result<Vec<AuditSourceContext>, WikiError> {`
  - Purpose: Indexed function `source_context` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:174-186]
- `load_provenance` (function) component `load_provenance [function]` (`8a6eb2f8-14df-567b-8c72-9af5e092a8bd`) lines 188-195 [crates/gwiki/src/audit.rs:188-195]
  - Signature: `fn load_provenance(vault_root: &Path) -> Result<ProvenanceGraph, WikiError> {`
  - Purpose: Indexed function `load_provenance` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:188-195]
- `unsupported_claims` (function) component `unsupported_claims [function]` (`a38fa861-0f28-51d6-a56d-9050e3d69ec6`) lines 197-226 [crates/gwiki/src/audit.rs:197-226]
  - Signature: `fn unsupported_claims(`
  - Purpose: Indexed function `unsupported_claims` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:197-226]
- `claim_source_context` (function) component `claim_source_context [function]` (`da75cadc-0ebe-5f00-9243-457b7263aa37`) lines 228-237 [crates/gwiki/src/audit.rs:228-237]
  - Signature: `fn claim_source_context(`
  - Purpose: Indexed function `claim_source_context` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:228-237]
- `is_generated_codewiki_page` (function) component `is_generated_codewiki_page [function]` (`2bdecda5-796c-585b-8cb5-204d5ae29da1`) lines 239-244 [crates/gwiki/src/audit.rs:239-244]
  - Signature: `fn is_generated_codewiki_page(page: &WikiPage) -> bool {`
  - Purpose: Indexed function `is_generated_codewiki_page` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:239-244]
- `has_codewiki_frontmatter_source_spans` (function) component `has_codewiki_frontmatter_source_spans [function]` (`ebe69580-0827-5ea0-b0c4-453baa3f6aef`) lines 246-255 [crates/gwiki/src/audit.rs:246-255]
  - Signature: `fn has_codewiki_frontmatter_source_spans(page: &WikiPage) -> bool {`
  - Purpose: Indexed function `has_codewiki_frontmatter_source_spans` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:246-255]
- `frontmatter_value_has_code_source_span` (function) component `frontmatter_value_has_code_source_span [function]` (`d851249c-e81d-5af8-806d-c6cb9b1c979f`) lines 257-262 [crates/gwiki/src/audit.rs:257-262]
  - Signature: `fn frontmatter_value_has_code_source_span(value: &Value) -> bool {`
  - Purpose: Indexed function `frontmatter_value_has_code_source_span` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:257-262]
- `frontmatter_source_has_code_span` (function) component `frontmatter_source_has_code_span [function]` (`85cb60bb-8a32-59e4-b6ea-5215dedebb45`) lines 264-280 [crates/gwiki/src/audit.rs:264-280]
  - Signature: `fn frontmatter_source_has_code_span(value: &Value) -> bool {`
  - Purpose: Indexed function `frontmatter_source_has_code_span` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:264-280]
- `frontmatter_range_is_valid` (function) component `frontmatter_range_is_valid [function]` (`9ff4a594-eaf1-5d30-9521-72434c2018f0`) lines 282-288 [crates/gwiki/src/audit.rs:282-288]
  - Signature: `fn frontmatter_range_is_valid(value: &Value) -> bool {`
  - Purpose: Indexed function `frontmatter_range_is_valid` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:282-288]
- `supported_claim_lines` (function) component `supported_claim_lines [function]` (`d2389b0b-da4c-5107-9967-a4497ff2a73a`) lines 290-327 [crates/gwiki/src/audit.rs:290-327]
  - Signature: `fn supported_claim_lines(`
  - Purpose: Indexed function `supported_claim_lines` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:290-327]
- `ClaimLine` (class) component `ClaimLine [class]` (`219e963d-c1be-5399-abf2-7b72310e7153`) lines 330-335 [crates/gwiki/src/audit.rs:330-335]
  - Signature: `struct ClaimLine {`
  - Purpose: Indexed class `ClaimLine` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:330-335]
- `ClaimKind` (type) component `ClaimKind [type]` (`a6627f7e-abd5-5efa-947c-7e55e747912f`) lines 338-341 [crates/gwiki/src/audit.rs:338-341]
  - Signature: `enum ClaimKind {`
  - Purpose: Indexed type `ClaimKind` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:338-341]
- `claim_lines` (function) component `claim_lines [function]` (`f4cad0e4-6ad4-5a4a-b5a1-4fc5d2826fdd`) lines 348-425 [crates/gwiki/src/audit.rs:348-425]
  - Signature: `fn claim_lines(page: &WikiPage, options: &AuditOptions) -> Vec<ClaimLine> {`
  - Purpose: Indexed function `claim_lines` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:348-425]
- `claim_kind` (function) component `claim_kind [function]` (`34110589-f133-5afe-9270-50b447e28285`) lines 427-433 [crates/gwiki/src/audit.rs:427-433]
  - Signature: `fn claim_kind(text: &str) -> ClaimKind {`
  - Purpose: Indexed function `claim_kind` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:427-433]
- `is_structural_codewiki_claim` (function) component `is_structural_codewiki_claim [function]` (`85baf4b1-c821-5810-a2c5-ca2d0c3db419`) lines 435-444 [crates/gwiki/src/audit.rs:435-444]
  - Signature: `fn is_structural_codewiki_claim(text: &str) -> bool {`
  - Purpose: Indexed function `is_structural_codewiki_claim` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:435-444]
- `heading_title` (function) component `heading_title [function]` (`edbd4ed0-6091-52f5-9d01-40fd09c6dc5c`) lines 446-450 [crates/gwiki/src/audit.rs:446-450]
  - Signature: `fn heading_title(line: &str) -> Option<String> {`
  - Purpose: Indexed function `heading_title` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:446-450]
- `ignored_claim_section` (function) component `ignored_claim_section [function]` (`f3fe9ac9-162b-55a0-845a-ba5c4c8443f5`) lines 452-454 [crates/gwiki/src/audit.rs:452-454]
  - Signature: `fn ignored_claim_section(heading: Option<&str>, options: &AuditOptions) -> bool {`
  - Purpose: Indexed function `ignored_claim_section` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:452-454]
- `ignored_claim_line` (function) component `ignored_claim_line [function]` (`a74809f7-30d2-5169-aadb-561f93ee93f6`) lines 456-463 [crates/gwiki/src/audit.rs:456-463]
  - Signature: `fn ignored_claim_line(line: &str) -> bool {`
  - Purpose: Indexed function `ignored_claim_line` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:456-463]
- `is_thematic_break` (function) component `is_thematic_break [function]` (`0256b916-bc81-59b8-b45c-e48473ca15c3`) lines 465-477 [crates/gwiki/src/audit.rs:465-477]
  - Signature: `fn is_thematic_break(line: &str) -> bool {`
  - Purpose: Indexed function `is_thematic_break` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:465-477]
- `has_inline_source_support` (function) component `has_inline_source_support [function]` (`a6c70cfb-3b92-5374-8f48-8987c0e28ef8`) lines 479-487 [crates/gwiki/src/audit.rs:479-487]
  - Signature: `fn has_inline_source_support(line: &str) -> bool {`
  - Purpose: Indexed function `has_inline_source_support` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:479-487]
- `has_code_source_span` (function) component `has_code_source_span [function]` (`10fcb562-7e3c-5e37-9ede-ecc681613a02`) lines 489-502 [crates/gwiki/src/audit.rs:489-502]
  - Signature: `fn has_code_source_span(line: &str) -> bool {`
  - Purpose: Indexed function `has_code_source_span` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:489-502]
- `is_code_source_span` (function) component `is_code_source_span [function]` (`dd410d9d-b2b5-5272-9ef6-4f03bd40a0f8`) lines 504-509 [crates/gwiki/src/audit.rs:504-509]
  - Signature: `fn is_code_source_span(candidate: &str) -> bool {`
  - Purpose: Indexed function `is_code_source_span` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:504-509]
- `is_code_source_path` (function) component `is_code_source_path [function]` (`68063c70-e6d4-5af4-a6ef-bd3f990d5291`) lines 511-516 [crates/gwiki/src/audit.rs:511-516]
  - Signature: `fn is_code_source_path(path: &str) -> bool {`
  - Purpose: Indexed function `is_code_source_path` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:511-516]
- `is_line_span` (function) component `is_line_span [function]` (`58128a56-baba-5558-b95c-d833ee901a6a`) lines 518-529 [crates/gwiki/src/audit.rs:518-529]
  - Signature: `fn is_line_span(span: &str) -> bool {`
  - Purpose: Indexed function `is_line_span` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:518-529]
- `has_link_like_source_token` (function) component `has_link_like_source_token [function]` (`3c6a7276-5881-50e7-b607-1cb6d3ac5fef`) lines 531-553 [crates/gwiki/src/audit.rs:531-553]
  - Signature: `fn has_link_like_source_token(line: &str, token: &str) -> bool {`
  - Purpose: Indexed function `has_link_like_source_token` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:531-553]
- `reports_unsupported_claims` (function) component `reports_unsupported_claims [function]` (`4abd0b7a-92d4-515c-b166-0193712b50c0`) lines 561-595 [crates/gwiki/src/audit.rs:561-595]
  - Signature: `fn reports_unsupported_claims() {`
  - Purpose: Indexed function `reports_unsupported_claims` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:561-595]
- `generated_codewiki_numeric_claims_do_not_inherit_raw_source_context` (function) component `generated_codewiki_numeric_claims_do_not_inherit_raw_source_context [function]` (`517021ae-ebae-5855-9939-ae30a8055ddf`) lines 598-664 [crates/gwiki/src/audit.rs:598-664]
  - Signature: `fn generated_codewiki_numeric_claims_do_not_inherit_raw_source_context() {`
  - Purpose: Indexed function `generated_codewiki_numeric_claims_do_not_inherit_raw_source_context` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:598-664]
- `reports_include_paths_and_scope` (function) component `reports_include_paths_and_scope [function]` (`b6b1b6b9-e89f-5049-9080-d384d3670a00`) lines 667-692 [crates/gwiki/src/audit.rs:667-692]
  - Signature: `fn reports_include_paths_and_scope() {`
  - Purpose: Indexed function `reports_include_paths_and_scope` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:667-692]
- `topic_scope_audits_only_topic_pages` (function) component `topic_scope_audits_only_topic_pages [function]` (`74cdeb38-9e7e-53ab-9985-4d806c429cc3`) lines 695-722 [crates/gwiki/src/audit.rs:695-722]
  - Signature: `fn topic_scope_audits_only_topic_pages() {`
  - Purpose: Indexed function `topic_scope_audits_only_topic_pages` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:695-722]
- `frontmatter_closes_only_on_matching_document_start_delimiter` (function) component `frontmatter_closes_only_on_matching_document_start_delimiter [function]` (`17e6af57-789c-52d9-8e98-a6a727e47366`) lines 725-744 [crates/gwiki/src/audit.rs:725-744]
  - Signature: `fn frontmatter_closes_only_on_matching_document_start_delimiter() {`
  - Purpose: Indexed function `frontmatter_closes_only_on_matching_document_start_delimiter` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:725-744]
- `multiline_html_comments_do_not_emit_claims` (function) component `multiline_html_comments_do_not_emit_claims [function]` (`792872e7-5cf1-5ccc-9ca5-407dbf3adfb3`) lines 747-767 [crates/gwiki/src/audit.rs:747-767]
  - Signature: `fn multiline_html_comments_do_not_emit_claims() {`
  - Purpose: Indexed function `multiline_html_comments_do_not_emit_claims` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:747-767]
- `inline_source_support_requires_link_like_target` (function) component `inline_source_support_requires_link_like_target [function]` (`ceb6491a-cdc1-550f-85df-eb58f77a79fb`) lines 770-778 [crates/gwiki/src/audit.rs:770-778]
  - Signature: `fn inline_source_support_requires_link_like_target() {`
  - Purpose: Indexed function `inline_source_support_requires_link_like_target` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:770-778]
- `inline_source_support_accepts_codewiki_source_spans` (function) component `inline_source_support_accepts_codewiki_source_spans [function]` (`83236681-2ead-5824-8253-f1257516685f`) lines 781-794 [crates/gwiki/src/audit.rs:781-794]
  - Signature: `fn inline_source_support_accepts_codewiki_source_spans() {`
  - Purpose: Indexed function `inline_source_support_accepts_codewiki_source_spans` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:781-794]
- `codewiki_frontmatter_source_spans_support_structural_claims` (function) component `codewiki_frontmatter_source_spans_support_structural_claims [function]` (`fe95c6cb-d29b-57d4-ad2f-bdfc629ec021`) lines 797-834 [crates/gwiki/src/audit.rs:797-834]
  - Signature: `fn codewiki_frontmatter_source_spans_support_structural_claims() {`
  - Purpose: Indexed function `codewiki_frontmatter_source_spans_support_structural_claims` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:797-834]
- `codewiki_contract_golden_page_counts_as_code_source_spans` (function) component `codewiki_contract_golden_page_counts_as_code_source_spans [function]` (`56231cb8-6a5d-5147-950f-a37c096dbd95`) lines 837-844 [crates/gwiki/src/audit.rs:837-844]
  - Signature: `fn codewiki_contract_golden_page_counts_as_code_source_spans() {`
  - Purpose: Indexed function `codewiki_contract_golden_page_counts_as_code_source_spans` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:837-844]
- `codewiki_frontmatter_source_spans_do_not_support_prose_claims` (function) component `codewiki_frontmatter_source_spans_do_not_support_prose_claims [function]` (`836fab09-3c2b-5689-bc89-efffdb1a7458`) lines 847-876 [crates/gwiki/src/audit.rs:847-876]
  - Signature: `fn codewiki_frontmatter_source_spans_do_not_support_prose_claims() {`
  - Purpose: Indexed function `codewiki_frontmatter_source_spans_do_not_support_prose_claims` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:847-876]
- `frontmatter_migration_audits_legacy_and_shared_sources_equivalently` (function) component `frontmatter_migration_audits_legacy_and_shared_sources_equivalently [function]` (`f72e2881-c772-563c-ba16-1838ba334956`) lines 879-932 [crates/gwiki/src/audit.rs:879-932]
  - Signature: `fn frontmatter_migration_audits_legacy_and_shared_sources_equivalently() {`
  - Purpose: Indexed function `frontmatter_migration_audits_legacy_and_shared_sources_equivalently` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:879-932]
- `test_codewiki_page` (function) component `test_codewiki_page [function]` (`e43e591b-9b8e-5555-a1b3-19045f705e18`) lines 934-943 [crates/gwiki/src/audit.rs:934-943]
  - Signature: `fn test_codewiki_page(path: &str, markdown: &str) -> WikiPage {`
  - Purpose: Indexed function `test_codewiki_page` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:934-943]
- `configured_ignored_sections_extend_defaults` (function) component `configured_ignored_sections_extend_defaults [function]` (`2eaaf991-75bd-5db3-abe6-4a1d6da37cff`) lines 946-965 [crates/gwiki/src/audit.rs:946-965]
  - Signature: `fn configured_ignored_sections_extend_defaults() {`
  - Purpose: Indexed function `configured_ignored_sections_extend_defaults` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:946-965]

