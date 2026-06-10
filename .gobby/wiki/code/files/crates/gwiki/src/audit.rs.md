---
title: crates/gwiki/src/audit.rs
type: code_file
provenance:
- file: crates/gwiki/src/audit.rs
  ranges:
  - 33-35
  - 37-72
  - 38-44
  - 46-53
  - 55-58
  - 60-71
  - 74-83
  - 75-82
  - 86-92
  - 95-102
  - 105-110
  - 112-114
  - 116-139
  - 141-170
  - 172-184
  - 186-193
  - 195-223
  - 225-234
  - 236-241
  - 243-254
  - 256-262
  - 264-301
  - 304-309
  - 312-315
  - 322-399
  - 401-407
  - 409-418
  - 420-424
  - 426-428
  - 430-437
  - 439-451
  - 453-461
  - 463-476
  - 478-483
  - 485-490
  - 492-503
  - 505-527
  - 535-569
  - 572-597
  - 600-627
  - 630-649
  - 652-672
  - 675-683
  - 686-699
  - 702-739
  - 742-771
  - 774-827
  - 829-838
  - 841-860
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/audit.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

`crates/gwiki/src/audit.rs` exposes 49 indexed API symbols.
[crates/gwiki/src/audit.rs:33-35]
[crates/gwiki/src/audit.rs:37-72]
[crates/gwiki/src/audit.rs:38-44]
[crates/gwiki/src/audit.rs:46-53]
[crates/gwiki/src/audit.rs:55-58]
[crates/gwiki/src/audit.rs:60-71]
[crates/gwiki/src/audit.rs:74-83]
[crates/gwiki/src/audit.rs:75-82]
[crates/gwiki/src/audit.rs:86-92]
[crates/gwiki/src/audit.rs:95-102]
[crates/gwiki/src/audit.rs:105-110]
[crates/gwiki/src/audit.rs:112-114]
[crates/gwiki/src/audit.rs:116-139]
[crates/gwiki/src/audit.rs:141-170]
[crates/gwiki/src/audit.rs:172-184]
[crates/gwiki/src/audit.rs:186-193]
[crates/gwiki/src/audit.rs:195-223]
[crates/gwiki/src/audit.rs:225-234]
[crates/gwiki/src/audit.rs:236-241]
[crates/gwiki/src/audit.rs:243-254]
[crates/gwiki/src/audit.rs:256-262]
[crates/gwiki/src/audit.rs:264-301]
[crates/gwiki/src/audit.rs:304-309]
[crates/gwiki/src/audit.rs:312-315]
[crates/gwiki/src/audit.rs:322-399]
[crates/gwiki/src/audit.rs:401-407]
[crates/gwiki/src/audit.rs:409-418]
[crates/gwiki/src/audit.rs:420-424]
[crates/gwiki/src/audit.rs:426-428]
[crates/gwiki/src/audit.rs:430-437]
[crates/gwiki/src/audit.rs:439-451]
[crates/gwiki/src/audit.rs:453-461]
[crates/gwiki/src/audit.rs:463-476]
[crates/gwiki/src/audit.rs:478-483]
[crates/gwiki/src/audit.rs:485-490]
[crates/gwiki/src/audit.rs:492-503]
[crates/gwiki/src/audit.rs:505-527]
[crates/gwiki/src/audit.rs:535-569]
[crates/gwiki/src/audit.rs:572-597]
[crates/gwiki/src/audit.rs:600-627]
[crates/gwiki/src/audit.rs:630-649]
[crates/gwiki/src/audit.rs:652-672]
[crates/gwiki/src/audit.rs:675-683]
[crates/gwiki/src/audit.rs:686-699]
[crates/gwiki/src/audit.rs:702-739]
[crates/gwiki/src/audit.rs:742-771]
[crates/gwiki/src/audit.rs:774-827]
[crates/gwiki/src/audit.rs:829-838]
[crates/gwiki/src/audit.rs:841-860]

## API Symbols

- `AuditOptions` (class) component `AuditOptions [class]` (`962b6a4c-e33b-5686-aa38-1699c9cd8005`) lines 33-35 [crates/gwiki/src/audit.rs:33-35]
  - Signature: `pub struct AuditOptions {`
  - Purpose: Indexed class `AuditOptions` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:33-35]
- `AuditOptions` (class) component `AuditOptions [class]` (`5662f13d-2458-5b0d-9fd3-8aea928a23b4`) lines 37-72 [crates/gwiki/src/audit.rs:37-72]
  - Signature: `impl AuditOptions {`
  - Purpose: Indexed class `AuditOptions` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:37-72]
- `AuditOptions.from_env` (method) component `AuditOptions.from_env [method]` (`1c519df6-86e8-57cd-b97c-ee12e75c6ea3`) lines 38-44 [crates/gwiki/src/audit.rs:38-44]
  - Signature: `pub fn from_env() -> Self {`
  - Purpose: Indexed method `AuditOptions.from_env` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:38-44]
- `AuditOptions.with_additional_ignored_sections` (method) component `AuditOptions.with_additional_ignored_sections [method]` (`e1cffa2b-8c58-58f0-9d10-db05e143a17e`) lines 46-53 [crates/gwiki/src/audit.rs:46-53]
  - Signature: `pub fn with_additional_ignored_sections<I, S>(mut self, sections: I) -> Self`
  - Purpose: Indexed method `AuditOptions.with_additional_ignored_sections` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:46-53]
- `AuditOptions.ignores_section` (method) component `AuditOptions.ignores_section [method]` (`b8952d80-6dd3-553b-831c-da0514f88264`) lines 55-58 [crates/gwiki/src/audit.rs:55-58]
  - Signature: `fn ignores_section(&self, heading: &str) -> bool {`
  - Purpose: Indexed method `AuditOptions.ignores_section` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:55-58]
- `AuditOptions.extend_ignored_sections` (method) component `AuditOptions.extend_ignored_sections [method]` (`6650e4e5-4870-513a-84a3-0ba8c65670fc`) lines 60-71 [crates/gwiki/src/audit.rs:60-71]
  - Signature: `fn extend_ignored_sections<I, S>(&mut self, sections: I)`
  - Purpose: Indexed method `AuditOptions.extend_ignored_sections` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:60-71]
- `AuditOptions` (class) component `AuditOptions [class]` (`d26d0d1c-ad89-5a70-b7b4-69c79ff339ca`) lines 74-83 [crates/gwiki/src/audit.rs:74-83]
  - Signature: `impl Default for AuditOptions {`
  - Purpose: Indexed class `AuditOptions` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:74-83]
- `AuditOptions.default` (method) component `AuditOptions.default [method]` (`8bd57e32-abfb-546f-b073-7eb0fb937ccc`) lines 75-82 [crates/gwiki/src/audit.rs:75-82]
  - Signature: `fn default() -> Self {`
  - Purpose: Indexed method `AuditOptions.default` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:75-82]
- `AuditReport` (class) component `AuditReport [class]` (`925d5dfc-d982-52d7-910e-539153201cd1`) lines 86-92 [crates/gwiki/src/audit.rs:86-92]
  - Signature: `pub struct AuditReport {`
  - Purpose: Indexed class `AuditReport` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:86-92]
- `UnsupportedClaim` (class) component `UnsupportedClaim [class]` (`7d23ba81-ab98-5431-8dcc-c37cd7b9e3b3`) lines 95-102 [crates/gwiki/src/audit.rs:95-102]
  - Signature: `pub struct UnsupportedClaim {`
  - Purpose: Indexed class `UnsupportedClaim` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:95-102]
- `AuditSourceContext` (class) component `AuditSourceContext [class]` (`10498c04-06f2-5cd4-a3df-ab53772d3701`) lines 105-110 [crates/gwiki/src/audit.rs:105-110]
  - Signature: `pub struct AuditSourceContext {`
  - Purpose: Indexed class `AuditSourceContext` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:105-110]
- `run` (function) component `run [function]` (`60ec9f9f-1076-5b7d-a4e9-8a6c26bcf7b1`) lines 112-114 [crates/gwiki/src/audit.rs:112-114]
  - Signature: `pub fn run(vault_root: &Path, scope: ScopeIdentity) -> Result<AuditReport, WikiError> {`
  - Purpose: Indexed function `run` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:112-114]
- `run_with_options` (function) component `run_with_options [function]` (`dbf45863-3900-5cd2-865a-e67ffe56e82d`) lines 116-139 [crates/gwiki/src/audit.rs:116-139]
  - Signature: `pub fn run_with_options(`
  - Purpose: Indexed function `run_with_options` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:116-139]
- `render_text` (function) component `render_text [function]` (`8e9e8ff1-9e7a-5b75-ba5c-ec7406506692`) lines 141-170 [crates/gwiki/src/audit.rs:141-170]
  - Signature: `pub fn render_text(report: &AuditReport) -> String {`
  - Purpose: Indexed function `render_text` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:141-170]
- `source_context` (function) component `source_context [function]` (`018802ea-3358-52b7-99f8-5a089d4b2d1a`) lines 172-184 [crates/gwiki/src/audit.rs:172-184]
  - Signature: `fn source_context(vault_root: &Path) -> Result<Vec<AuditSourceContext>, WikiError> {`
  - Purpose: Indexed function `source_context` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:172-184]
- `load_provenance` (function) component `load_provenance [function]` (`b9fcd9d9-3dce-555b-8cf2-97e2371ab9db`) lines 186-193 [crates/gwiki/src/audit.rs:186-193]
  - Signature: `fn load_provenance(vault_root: &Path) -> Result<ProvenanceGraph, WikiError> {`
  - Purpose: Indexed function `load_provenance` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:186-193]
- `unsupported_claims` (function) component `unsupported_claims [function]` (`e02b2ed9-d0e2-53a6-b7b4-241d4adc4d47`) lines 195-223 [crates/gwiki/src/audit.rs:195-223]
  - Signature: `fn unsupported_claims(`
  - Purpose: Indexed function `unsupported_claims` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:195-223]
- `has_codewiki_frontmatter_source_spans` (function) component `has_codewiki_frontmatter_source_spans [function]` (`0241048f-a599-5296-bde6-3f154a80050a`) lines 225-234 [crates/gwiki/src/audit.rs:225-234]
  - Signature: `fn has_codewiki_frontmatter_source_spans(page: &WikiPage) -> bool {`
  - Purpose: Indexed function `has_codewiki_frontmatter_source_spans` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:225-234]
- `frontmatter_value_has_code_source_span` (function) component `frontmatter_value_has_code_source_span [function]` (`7c5c53bc-b56e-5cd3-a39d-d5c36d3e3d43`) lines 236-241 [crates/gwiki/src/audit.rs:236-241]
  - Signature: `fn frontmatter_value_has_code_source_span(value: &Value) -> bool {`
  - Purpose: Indexed function `frontmatter_value_has_code_source_span` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:236-241]
- `frontmatter_source_has_code_span` (function) component `frontmatter_source_has_code_span [function]` (`bddf2e6a-8d1a-5597-a1a3-31a66124e698`) lines 243-254 [crates/gwiki/src/audit.rs:243-254]
  - Signature: `fn frontmatter_source_has_code_span(value: &Value) -> bool {`
  - Purpose: Indexed function `frontmatter_source_has_code_span` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:243-254]
- `frontmatter_range_is_valid` (function) component `frontmatter_range_is_valid [function]` (`dd48483d-5338-569e-8fbe-1c1a6a509b8c`) lines 256-262 [crates/gwiki/src/audit.rs:256-262]
  - Signature: `fn frontmatter_range_is_valid(value: &Value) -> bool {`
  - Purpose: Indexed function `frontmatter_range_is_valid` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:256-262]
- `supported_claim_lines` (function) component `supported_claim_lines [function]` (`4ae806c8-3ca8-5440-bd24-11fec641c550`) lines 264-301 [crates/gwiki/src/audit.rs:264-301]
  - Signature: `fn supported_claim_lines(`
  - Purpose: Indexed function `supported_claim_lines` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:264-301]
- `ClaimLine` (class) component `ClaimLine [class]` (`7f4fb696-8ba0-5562-b8f3-55d14144525e`) lines 304-309 [crates/gwiki/src/audit.rs:304-309]
  - Signature: `struct ClaimLine {`
  - Purpose: Indexed class `ClaimLine` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:304-309]
- `ClaimKind` (type) component `ClaimKind [type]` (`f32d5813-fe83-5265-a209-aeff6d3e3687`) lines 312-315 [crates/gwiki/src/audit.rs:312-315]
  - Signature: `enum ClaimKind {`
  - Purpose: Indexed type `ClaimKind` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:312-315]
- `claim_lines` (function) component `claim_lines [function]` (`ee20be9e-7e80-5526-8c77-58e3e2ba8f0d`) lines 322-399 [crates/gwiki/src/audit.rs:322-399]
  - Signature: `fn claim_lines(page: &WikiPage, options: &AuditOptions) -> Vec<ClaimLine> {`
  - Purpose: Indexed function `claim_lines` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:322-399]
- `claim_kind` (function) component `claim_kind [function]` (`679acb60-8660-5a47-9c24-471e9cda45d2`) lines 401-407 [crates/gwiki/src/audit.rs:401-407]
  - Signature: `fn claim_kind(text: &str) -> ClaimKind {`
  - Purpose: Indexed function `claim_kind` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:401-407]
- `is_structural_codewiki_claim` (function) component `is_structural_codewiki_claim [function]` (`a21c99bb-58e7-52da-8dcf-5201066a2fcd`) lines 409-418 [crates/gwiki/src/audit.rs:409-418]
  - Signature: `fn is_structural_codewiki_claim(text: &str) -> bool {`
  - Purpose: Indexed function `is_structural_codewiki_claim` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:409-418]
- `heading_title` (function) component `heading_title [function]` (`1371276b-c2fb-50c6-b22a-da21d5acfad5`) lines 420-424 [crates/gwiki/src/audit.rs:420-424]
  - Signature: `fn heading_title(line: &str) -> Option<String> {`
  - Purpose: Indexed function `heading_title` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:420-424]
- `ignored_claim_section` (function) component `ignored_claim_section [function]` (`f594df67-e279-510f-98aa-5562039a3d63`) lines 426-428 [crates/gwiki/src/audit.rs:426-428]
  - Signature: `fn ignored_claim_section(heading: Option<&str>, options: &AuditOptions) -> bool {`
  - Purpose: Indexed function `ignored_claim_section` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:426-428]
- `ignored_claim_line` (function) component `ignored_claim_line [function]` (`e603c60e-c461-5e40-876f-8e172c1be719`) lines 430-437 [crates/gwiki/src/audit.rs:430-437]
  - Signature: `fn ignored_claim_line(line: &str) -> bool {`
  - Purpose: Indexed function `ignored_claim_line` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:430-437]
- `is_thematic_break` (function) component `is_thematic_break [function]` (`9a8e3af3-12f6-5f57-9946-0662ca1945e5`) lines 439-451 [crates/gwiki/src/audit.rs:439-451]
  - Signature: `fn is_thematic_break(line: &str) -> bool {`
  - Purpose: Indexed function `is_thematic_break` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:439-451]
- `has_inline_source_support` (function) component `has_inline_source_support [function]` (`4249011d-0623-5fdd-b7c2-c32e9b46711e`) lines 453-461 [crates/gwiki/src/audit.rs:453-461]
  - Signature: `fn has_inline_source_support(line: &str) -> bool {`
  - Purpose: Indexed function `has_inline_source_support` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:453-461]
- `has_code_source_span` (function) component `has_code_source_span [function]` (`c3527481-09bb-52e7-9665-bb346140380c`) lines 463-476 [crates/gwiki/src/audit.rs:463-476]
  - Signature: `fn has_code_source_span(line: &str) -> bool {`
  - Purpose: Indexed function `has_code_source_span` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:463-476]
- `is_code_source_span` (function) component `is_code_source_span [function]` (`99425789-a909-51ae-b03e-5a0d39b78e39`) lines 478-483 [crates/gwiki/src/audit.rs:478-483]
  - Signature: `fn is_code_source_span(candidate: &str) -> bool {`
  - Purpose: Indexed function `is_code_source_span` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:478-483]
- `is_code_source_path` (function) component `is_code_source_path [function]` (`b00a6ed6-c91a-5b2f-bd37-adc6b0d5b746`) lines 485-490 [crates/gwiki/src/audit.rs:485-490]
  - Signature: `fn is_code_source_path(path: &str) -> bool {`
  - Purpose: Indexed function `is_code_source_path` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:485-490]
- `is_line_span` (function) component `is_line_span [function]` (`36dad96b-e155-57ad-bc64-e89398787168`) lines 492-503 [crates/gwiki/src/audit.rs:492-503]
  - Signature: `fn is_line_span(span: &str) -> bool {`
  - Purpose: Indexed function `is_line_span` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:492-503]
- `has_link_like_source_token` (function) component `has_link_like_source_token [function]` (`1df6e677-77af-5e8c-9d3d-38433e8cf04c`) lines 505-527 [crates/gwiki/src/audit.rs:505-527]
  - Signature: `fn has_link_like_source_token(line: &str, token: &str) -> bool {`
  - Purpose: Indexed function `has_link_like_source_token` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:505-527]
- `reports_unsupported_claims` (function) component `reports_unsupported_claims [function]` (`126718f1-cc60-57b1-bd59-a74f6d5e3e77`) lines 535-569 [crates/gwiki/src/audit.rs:535-569]
  - Signature: `fn reports_unsupported_claims() {`
  - Purpose: Indexed function `reports_unsupported_claims` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:535-569]
- `reports_include_paths_and_scope` (function) component `reports_include_paths_and_scope [function]` (`da24623a-d32b-5590-bcbf-b2f773a46c21`) lines 572-597 [crates/gwiki/src/audit.rs:572-597]
  - Signature: `fn reports_include_paths_and_scope() {`
  - Purpose: Indexed function `reports_include_paths_and_scope` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:572-597]
- `topic_scope_audits_only_topic_pages` (function) component `topic_scope_audits_only_topic_pages [function]` (`3fa5a282-f7a0-5a27-ba61-02bdd09a45b3`) lines 600-627 [crates/gwiki/src/audit.rs:600-627]
  - Signature: `fn topic_scope_audits_only_topic_pages() {`
  - Purpose: Indexed function `topic_scope_audits_only_topic_pages` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:600-627]
- `frontmatter_closes_only_on_matching_document_start_delimiter` (function) component `frontmatter_closes_only_on_matching_document_start_delimiter [function]` (`d0e58b97-6ea7-5425-9c40-08fd2ee3ce19`) lines 630-649 [crates/gwiki/src/audit.rs:630-649]
  - Signature: `fn frontmatter_closes_only_on_matching_document_start_delimiter() {`
  - Purpose: Indexed function `frontmatter_closes_only_on_matching_document_start_delimiter` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:630-649]
- `multiline_html_comments_do_not_emit_claims` (function) component `multiline_html_comments_do_not_emit_claims [function]` (`40678c5f-3283-508d-af44-0c517262bb24`) lines 652-672 [crates/gwiki/src/audit.rs:652-672]
  - Signature: `fn multiline_html_comments_do_not_emit_claims() {`
  - Purpose: Indexed function `multiline_html_comments_do_not_emit_claims` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:652-672]
- `inline_source_support_requires_link_like_target` (function) component `inline_source_support_requires_link_like_target [function]` (`6f7d2899-5814-5b91-a4d1-0d78dd38f723`) lines 675-683 [crates/gwiki/src/audit.rs:675-683]
  - Signature: `fn inline_source_support_requires_link_like_target() {`
  - Purpose: Indexed function `inline_source_support_requires_link_like_target` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:675-683]
- `inline_source_support_accepts_codewiki_source_spans` (function) component `inline_source_support_accepts_codewiki_source_spans [function]` (`ba23d8b9-3839-52a6-bb5c-24b653606dec`) lines 686-699 [crates/gwiki/src/audit.rs:686-699]
  - Signature: `fn inline_source_support_accepts_codewiki_source_spans() {`
  - Purpose: Indexed function `inline_source_support_accepts_codewiki_source_spans` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:686-699]
- `codewiki_frontmatter_source_spans_support_structural_claims` (function) component `codewiki_frontmatter_source_spans_support_structural_claims [function]` (`0e778215-2823-5154-9ac4-ce9ce188bfb9`) lines 702-739 [crates/gwiki/src/audit.rs:702-739]
  - Signature: `fn codewiki_frontmatter_source_spans_support_structural_claims() {`
  - Purpose: Indexed function `codewiki_frontmatter_source_spans_support_structural_claims` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:702-739]
- `codewiki_frontmatter_source_spans_do_not_support_prose_claims` (function) component `codewiki_frontmatter_source_spans_do_not_support_prose_claims [function]` (`747733d4-b4e2-58ca-b9f4-392272768f61`) lines 742-771 [crates/gwiki/src/audit.rs:742-771]
  - Signature: `fn codewiki_frontmatter_source_spans_do_not_support_prose_claims() {`
  - Purpose: Indexed function `codewiki_frontmatter_source_spans_do_not_support_prose_claims` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:742-771]
- `frontmatter_migration_audits_legacy_and_shared_sources_equivalently` (function) component `frontmatter_migration_audits_legacy_and_shared_sources_equivalently [function]` (`29d915fc-31af-5686-aba1-d3df9bb0445c`) lines 774-827 [crates/gwiki/src/audit.rs:774-827]
  - Signature: `fn frontmatter_migration_audits_legacy_and_shared_sources_equivalently() {`
  - Purpose: Indexed function `frontmatter_migration_audits_legacy_and_shared_sources_equivalently` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:774-827]
- `test_codewiki_page` (function) component `test_codewiki_page [function]` (`f3513a32-4703-589b-8b8e-b85bc08b5407`) lines 829-838 [crates/gwiki/src/audit.rs:829-838]
  - Signature: `fn test_codewiki_page(path: &str, markdown: &str) -> WikiPage {`
  - Purpose: Indexed function `test_codewiki_page` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:829-838]
- `configured_ignored_sections_extend_defaults` (function) component `configured_ignored_sections_extend_defaults [function]` (`3627cfa1-a57d-53e8-9da3-3fcbce0f4e77`) lines 841-860 [crates/gwiki/src/audit.rs:841-860]
  - Signature: `fn configured_ignored_sections_extend_defaults() {`
  - Purpose: Indexed function `configured_ignored_sections_extend_defaults` in `crates/gwiki/src/audit.rs`. [crates/gwiki/src/audit.rs:841-860]

