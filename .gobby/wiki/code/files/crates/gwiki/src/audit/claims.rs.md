---
title: crates/gwiki/src/audit/claims.rs
type: code_file
provenance:
- file: crates/gwiki/src/audit/claims.rs
  ranges:
  - 15-44
  - 46-55
  - 57-62
  - 64-73
  - 75-80
  - 82-98
  - 100-106
  - 108-145
  - 148-153
  - 156-159
  - 166-243
  - 245-251
  - 253-262
  - 264-268
  - 270-272
  - 274-281
  - 283-295
  - 297-305
  - 307-320
  - 322-327
  - 329-334
  - 336-347
  - 349-371
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gwiki/src/audit/claims.rs

Module: [[code/modules/crates/gwiki/src/audit|crates/gwiki/src/audit]]

## Purpose

This file audits wiki page claims and emits `UnsupportedClaim` entries for lines that lack support from page-level provenance, section provenance, or inline citations. It does this by extracting claim lines from Markdown, classifying structural vs prose claims, checking whether headings and frontmatter provenance provide support, and suppressing unsupported reports for generated CodeWiki pages or claims that already carry valid source spans or citation-like tokens.
[crates/gwiki/src/audit/claims.rs:15-44]
[crates/gwiki/src/audit/claims.rs:46-55]
[crates/gwiki/src/audit/claims.rs:57-62]
[crates/gwiki/src/audit/claims.rs:64-73]
[crates/gwiki/src/audit/claims.rs:75-80]

## API Symbols

- `unsupported_claims` (function) component `unsupported_claims [function]` (`bb771ef7-b1fb-5c78-99cc-5384c6645ed0`) lines 15-44 [crates/gwiki/src/audit/claims.rs:15-44]
  - Signature: `pub(super) fn unsupported_claims(`
  - Purpose: Returns a 'Vec<UnsupportedClaim>' for the given wiki page by extracting claims and filtering out those covered by page-level source spans, provenance-backed lines, or inline citations, emitting the remaining claims with path, line, heading, text, and a fixed “no source provenance or inline citation” reason. [crates/gwiki/src/audit/claims.rs:15-44]
- `claim_source_context` (function) component `claim_source_context [function]` (`79c6c10b-f4bc-5b8f-ae41-9af7c7b1c1dc`) lines 46-55 [crates/gwiki/src/audit/claims.rs:46-55]
  - Signature: `fn claim_source_context(`
  - Purpose: Returns an empty 'Arc<Vec<AuditSourceContext>>' for generated CodeWiki pages, otherwise clones and returns the provided 'source_context'. [crates/gwiki/src/audit/claims.rs:46-55]
- `is_generated_codewiki_page` (function) component `is_generated_codewiki_page [function]` (`89d06819-27e5-56e7-b43c-7d8745a63a61`) lines 57-62 [crates/gwiki/src/audit/claims.rs:57-62]
  - Signature: `fn is_generated_codewiki_page(page: &WikiPage) -> bool {`
  - Purpose: Returns 'true' only when the page’s normalized relative path starts with 'code/' and its frontmatter 'trust' field is exactly 'gobby_core::codewiki_contract::TRUST_GENERATED'. [crates/gwiki/src/audit/claims.rs:57-62]
- `has_codewiki_frontmatter_source_spans` (function) component `has_codewiki_frontmatter_source_spans [function]` (`3cc8426f-c5dd-581d-b5df-309aea49d190`) lines 64-73 [crates/gwiki/src/audit/claims.rs:64-73]
  - Signature: `pub(super) fn has_codewiki_frontmatter_source_spans(page: &WikiPage) -> bool {`
  - Purpose: Returns 'true' when the page’s relative path is under 'code/' and its frontmatter provenance contains at least one value with a code source span, otherwise 'false'. [crates/gwiki/src/audit/claims.rs:64-73]
- `frontmatter_value_has_code_source_span` (function) component `frontmatter_value_has_code_source_span [function]` (`3dc8cb1f-352c-50b5-9f5f-6ae0508f12cb`) lines 75-80 [crates/gwiki/src/audit/claims.rs:75-80]
  - Signature: `fn frontmatter_value_has_code_source_span(value: &Value) -> bool {`
  - Purpose: Returns 'true' if 'value' is a 'Value::Array' containing at least one element for which 'frontmatter_source_has_code_span' returns 'true', and 'false' otherwise. [crates/gwiki/src/audit/claims.rs:75-80]
- `frontmatter_source_has_code_span` (function) component `frontmatter_source_has_code_span [function]` (`9d6d71ea-06ed-5a7c-a3e4-441e51459081`) lines 82-98 [crates/gwiki/src/audit/claims.rs:82-98]
  - Signature: `fn frontmatter_source_has_code_span(value: &Value) -> bool {`
  - Purpose: Returns 'true' only when 'value' is an object containing a provenance file string that satisfies 'is_code_source_path' and a provenance ranges array with at least one range for which 'frontmatter_range_is_valid' returns 'true'; otherwise returns 'false'. [crates/gwiki/src/audit/claims.rs:82-98]
- `frontmatter_range_is_valid` (function) component `frontmatter_range_is_valid [function]` (`646fd59a-8711-5d1d-82f6-38a417a482a6`) lines 100-106 [crates/gwiki/src/audit/claims.rs:100-106]
  - Signature: `fn frontmatter_range_is_valid(value: &Value) -> bool {`
  - Purpose: Returns 'true' if 'value' is either a string that parses as a valid line span via 'is_line_span', or an unsigned integer greater than zero; otherwise returns 'false'. [crates/gwiki/src/audit/claims.rs:100-106]
- `supported_claim_lines` (function) component `supported_claim_lines [function]` (`213ddb02-a92c-55a7-b7e8-ce12fd455afb`) lines 108-145 [crates/gwiki/src/audit/claims.rs:108-145]
  - Signature: `fn supported_claim_lines(`
  - Purpose: Returns the set of line numbers for 'claims' whose optional heading matches a section heading on the given 'page' that is present in the 'provenance' graph, but only if at least one such heading exists; otherwise it returns an empty 'BTreeSet'. [crates/gwiki/src/audit/claims.rs:108-145]
- `ClaimLine` (class) component `ClaimLine [class]` (`2a2866b8-0e85-5583-8267-60b8fd16edd4`) lines 148-153 [crates/gwiki/src/audit/claims.rs:148-153]
  - Signature: `pub(super) struct ClaimLine {`
  - Purpose: 'ClaimLine' is a package-visible struct representing a parsed claim line, storing its source line number, an optional heading, the line text, and an internal 'ClaimKind' discriminator. [crates/gwiki/src/audit/claims.rs:148-153]
- `ClaimKind` (type) component `ClaimKind [type]` (`7e0e51e9-7522-59cd-a6ce-781274798d0b`) lines 156-159 [crates/gwiki/src/audit/claims.rs:156-159]
  - Signature: `enum ClaimKind {`
  - Purpose: Indexed type `ClaimKind` in `crates/gwiki/src/audit/claims.rs`. [crates/gwiki/src/audit/claims.rs:156-159]
- `claim_lines` (function) component `claim_lines [function]` (`2c337166-5272-5bc4-a295-8c06d43cd9f1`) lines 166-243 [crates/gwiki/src/audit/claims.rs:166-243]
  - Signature: `pub(super) fn claim_lines(page: &WikiPage, options: &AuditOptions) -> Vec<ClaimLine> {`
  - Purpose: 'claim_lines' scans a wiki page’s Markdown line by line and returns 'ClaimLine' entries for non-empty, non-comment, non-frontmatter, non-fenced, non-heading, non-ignored content lines, tracking the current heading and byte offset as it goes. [crates/gwiki/src/audit/claims.rs:166-243]
- `claim_kind` (function) component `claim_kind [function]` (`ffd89550-d951-59b7-a8a8-ed43f4c1081c`) lines 245-251 [crates/gwiki/src/audit/claims.rs:245-251]
  - Signature: `fn claim_kind(text: &str) -> ClaimKind {`
  - Purpose: Returns 'ClaimKind::Structural' when 'text' satisfies 'is_structural_codewiki_claim', otherwise returns 'ClaimKind::Prose'. [crates/gwiki/src/audit/claims.rs:245-251]
- `is_structural_codewiki_claim` (function) component `is_structural_codewiki_claim [function]` (`39c1e0c0-6e67-5f9b-a9d3-a15c15de8cbd`) lines 253-262 [crates/gwiki/src/audit/claims.rs:253-262]
  - Signature: `fn is_structural_codewiki_claim(text: &str) -> bool {`
  - Purpose: Returns 'true' when the input, case-insensitively, begins with one of several CodeWiki structural prefixes ('module:', 'parent:', 'signature:', 'source path:', 'component:', 'components:', or '[[code/'), and 'false' otherwise. [crates/gwiki/src/audit/claims.rs:253-262]
- `heading_title` (function) component `heading_title [function]` (`ef51c03b-1755-5967-8954-55a0b6a7bf76`) lines 264-268 [crates/gwiki/src/audit/claims.rs:264-268]
  - Signature: `fn heading_title(line: &str) -> Option<String> {`
  - Purpose: Returns the non-empty ATX heading text parsed from 'line' as 'Some(String)', or 'None' if the line is not a heading or the heading content is empty. [crates/gwiki/src/audit/claims.rs:264-268]
- `ignored_claim_section` (function) component `ignored_claim_section [function]` (`ceb9984d-3f54-5cb8-9eeb-f869f6a6dff6`) lines 270-272 [crates/gwiki/src/audit/claims.rs:270-272]
  - Signature: `fn ignored_claim_section(heading: Option<&str>, options: &AuditOptions) -> bool {`
  - Purpose: Returns 'true' only when 'heading' is 'Some' and 'options.ignores_section(heading)' evaluates to 'true', otherwise 'false'. [crates/gwiki/src/audit/claims.rs:270-272]
- `ignored_claim_line` (function) component `ignored_claim_line [function]` (`7f3ba8b5-835b-50f8-a279-9abab16398d6`) lines 274-281 [crates/gwiki/src/audit/claims.rs:274-281]
  - Signature: `fn ignored_claim_line(line: &str) -> bool {`
  - Purpose: Returns 'true' when the input line, case-insensitively, begins with 'sources:', 'source path:', 'citation:', or 'citations:', or is exactly '- none recorded.' after ASCII lowercasing. [crates/gwiki/src/audit/claims.rs:274-281]
- `is_thematic_break` (function) component `is_thematic_break [function]` (`5854c35e-e0b6-5738-af87-76f25cd61c18`) lines 283-295 [crates/gwiki/src/audit/claims.rs:283-295]
  - Signature: `fn is_thematic_break(line: &str) -> bool {`
  - Purpose: Returns 'true' when the input line contains at least three non-whitespace characters and, after removing all whitespace, consists entirely of a single repeated marker character of '-', '*', or '_'. [crates/gwiki/src/audit/claims.rs:283-295]
- `has_inline_source_support` (function) component `has_inline_source_support [function]` (`b2f1979f-585b-5a43-baf4-dc3896505436`) lines 297-305 [crates/gwiki/src/audit/claims.rs:297-305]
  - Signature: `pub(super) fn has_inline_source_support(line: &str) -> bool {`
  - Purpose: Returns 'true' if the input line contains any inline source indicator, including '[[knowledge/sources/', '(knowledge/sources/', a code-source span, link-like 'citation:' or 'source:' tokens, or 'gwiki-source:' (case-insensitive where applicable). [crates/gwiki/src/audit/claims.rs:297-305]
- `has_code_source_span` (function) component `has_code_source_span [function]` (`ce09f2d1-c92c-53ec-85f5-4fcfd51528bc`) lines 307-320 [crates/gwiki/src/audit/claims.rs:307-320]
  - Signature: `fn has_code_source_span(line: &str) -> bool {`
  - Purpose: Returns 'true' if 'line' contains any bracketed substring whose contents satisfy 'is_code_source_span', scanning left to right and returning 'false' if no such span is found or if an opening '[' lacks a matching ']'. [crates/gwiki/src/audit/claims.rs:307-320]
- `is_code_source_span` (function) component `is_code_source_span [function]` (`d4ce3bdb-6817-5c2e-8500-1bb69b8b1332`) lines 322-327 [crates/gwiki/src/audit/claims.rs:322-327]
  - Signature: `fn is_code_source_span(candidate: &str) -> bool {`
  - Purpose: Returns 'true' only when 'candidate' contains a final ':' separator, the prefix satisfies 'is_code_source_path', and the suffix satisfies 'is_line_span'; otherwise returns 'false'. [crates/gwiki/src/audit/claims.rs:322-327]
- `is_code_source_path` (function) component `is_code_source_path [function]` (`fd2f5b36-16ed-534a-baa7-0355ea2b77ad`) lines 329-334 [crates/gwiki/src/audit/claims.rs:329-334]
  - Signature: `fn is_code_source_path(path: &str) -> bool {`
  - Purpose: Returns 'true' only for non-empty, whitespace-free strings that contain either '/' or '.', and do not contain the substring '://', which is used to heuristically classify a path as code-source-like. [crates/gwiki/src/audit/claims.rs:329-334]
- `is_line_span` (function) component `is_line_span [function]` (`44719776-0871-55f4-878c-ec897dd657df`) lines 336-347 [crates/gwiki/src/audit/claims.rs:336-347]
  - Signature: `fn is_line_span(span: &str) -> bool {`
  - Purpose: Returns 'true' if 'span' is either a positive 1-based line number or a valid 'start-end' line range where both endpoints parse as 'usize', 'start > 0', and 'end >= start'. [crates/gwiki/src/audit/claims.rs:336-347]
- `has_link_like_source_token` (function) component `has_link_like_source_token [function]` (`871e5c2f-c3a6-5d37-b32d-2b5df199947c`) lines 349-371 [crates/gwiki/src/audit/claims.rs:349-371]
  - Signature: `fn has_link_like_source_token(line: &str, token: &str) -> bool {`
  - Purpose: Returns 'true' if 'token' appears in 'line' as a whole token boundary and is immediately followed, after optional whitespace, by a link-like source prefix such as 'http://', 'https://', '[[knowledge/sources/', '[', '(knowledge/sources/', 'knowledge/sources/', or 'gwiki-source:'; otherwise returns 'false'. [crates/gwiki/src/audit/claims.rs:349-371]

