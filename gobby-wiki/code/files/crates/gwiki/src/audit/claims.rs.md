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

<details>
<summary>Relevant source files</summary>

- [crates/gwiki/src/audit/claims.rs:15-44](crates/gwiki/src/audit/claims.rs#L15-L44), [crates/gwiki/src/audit/claims.rs:46-55](crates/gwiki/src/audit/claims.rs#L46-L55), [crates/gwiki/src/audit/claims.rs:57-62](crates/gwiki/src/audit/claims.rs#L57-L62), [crates/gwiki/src/audit/claims.rs:64-73](crates/gwiki/src/audit/claims.rs#L64-L73), [crates/gwiki/src/audit/claims.rs:75-80](crates/gwiki/src/audit/claims.rs#L75-L80), [crates/gwiki/src/audit/claims.rs:82-98](crates/gwiki/src/audit/claims.rs#L82-L98), [crates/gwiki/src/audit/claims.rs:100-106](crates/gwiki/src/audit/claims.rs#L100-L106), [crates/gwiki/src/audit/claims.rs:108-145](crates/gwiki/src/audit/claims.rs#L108-L145), [crates/gwiki/src/audit/claims.rs:148-153](crates/gwiki/src/audit/claims.rs#L148-L153), [crates/gwiki/src/audit/claims.rs:156-159](crates/gwiki/src/audit/claims.rs#L156-L159), [crates/gwiki/src/audit/claims.rs:166-243](crates/gwiki/src/audit/claims.rs#L166-L243), [crates/gwiki/src/audit/claims.rs:245-251](crates/gwiki/src/audit/claims.rs#L245-L251), [crates/gwiki/src/audit/claims.rs:253-262](crates/gwiki/src/audit/claims.rs#L253-L262), [crates/gwiki/src/audit/claims.rs:264-268](crates/gwiki/src/audit/claims.rs#L264-L268), [crates/gwiki/src/audit/claims.rs:270-272](crates/gwiki/src/audit/claims.rs#L270-L272), [crates/gwiki/src/audit/claims.rs:274-281](crates/gwiki/src/audit/claims.rs#L274-L281), [crates/gwiki/src/audit/claims.rs:283-295](crates/gwiki/src/audit/claims.rs#L283-L295), [crates/gwiki/src/audit/claims.rs:297-305](crates/gwiki/src/audit/claims.rs#L297-L305), [crates/gwiki/src/audit/claims.rs:307-320](crates/gwiki/src/audit/claims.rs#L307-L320), [crates/gwiki/src/audit/claims.rs:322-327](crates/gwiki/src/audit/claims.rs#L322-L327), [crates/gwiki/src/audit/claims.rs:329-334](crates/gwiki/src/audit/claims.rs#L329-L334), [crates/gwiki/src/audit/claims.rs:336-347](crates/gwiki/src/audit/claims.rs#L336-L347), [crates/gwiki/src/audit/claims.rs:349-371](crates/gwiki/src/audit/claims.rs#L349-L371)

</details>

# crates/gwiki/src/audit/claims.rs

Module: [[code/modules/crates/gwiki/src|crates/gwiki/src]]

## Purpose

This file implements the audit logic for wiki-page claims, deciding which claim lines lack acceptable provenance and should be reported as `UnsupportedClaim`s. `unsupported_claims` ties the pieces together by collecting claim lines, checking whether each line is supported by page/frontmatter provenance or inline citations, and attaching source context, while the helper functions classify claim kinds, detect generated codewiki pages, inspect frontmatter/source spans, and filter out structural, ignored, or otherwise supported claims.
[crates/gwiki/src/audit/claims.rs:15-44]
[crates/gwiki/src/audit/claims.rs:46-55]
[crates/gwiki/src/audit/claims.rs:57-62]
[crates/gwiki/src/audit/claims.rs:64-73]
[crates/gwiki/src/audit/claims.rs:75-80]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `unsupported_claims` | function | `pub(super) fn unsupported_claims(` | `unsupported_claims [function]` | `bb771ef7-b1fb-5c78-99cc-5384c6645ed0` | 15-44 [crates/gwiki/src/audit/claims.rs:15-44] | Indexed function `unsupported_claims` in `crates/gwiki/src/audit/claims.rs`. [crates/gwiki/src/audit/claims.rs:15-44] |
| `claim_source_context` | function | `fn claim_source_context(` | `claim_source_context [function]` | `79c6c10b-f4bc-5b8f-ae41-9af7c7b1c1dc` | 46-55 [crates/gwiki/src/audit/claims.rs:46-55] | Indexed function `claim_source_context` in `crates/gwiki/src/audit/claims.rs`. [crates/gwiki/src/audit/claims.rs:46-55] |
| `is_generated_codewiki_page` | function | `fn is_generated_codewiki_page(page: &WikiPage) -> bool {` | `is_generated_codewiki_page [function]` | `89d06819-27e5-56e7-b43c-7d8745a63a61` | 57-62 [crates/gwiki/src/audit/claims.rs:57-62] | Indexed function `is_generated_codewiki_page` in `crates/gwiki/src/audit/claims.rs`. [crates/gwiki/src/audit/claims.rs:57-62] |
| `has_codewiki_frontmatter_source_spans` | function | `pub(super) fn has_codewiki_frontmatter_source_spans(page: &WikiPage) -> bool {` | `has_codewiki_frontmatter_source_spans [function]` | `3cc8426f-c5dd-581d-b5df-309aea49d190` | 64-73 [crates/gwiki/src/audit/claims.rs:64-73] | Indexed function `has_codewiki_frontmatter_source_spans` in `crates/gwiki/src/audit/claims.rs`. [crates/gwiki/src/audit/claims.rs:64-73] |
| `frontmatter_value_has_code_source_span` | function | `fn frontmatter_value_has_code_source_span(value: &Value) -> bool {` | `frontmatter_value_has_code_source_span [function]` | `3dc8cb1f-352c-50b5-9f5f-6ae0508f12cb` | 75-80 [crates/gwiki/src/audit/claims.rs:75-80] | Indexed function `frontmatter_value_has_code_source_span` in `crates/gwiki/src/audit/claims.rs`. [crates/gwiki/src/audit/claims.rs:75-80] |
| `frontmatter_source_has_code_span` | function | `fn frontmatter_source_has_code_span(value: &Value) -> bool {` | `frontmatter_source_has_code_span [function]` | `9d6d71ea-06ed-5a7c-a3e4-441e51459081` | 82-98 [crates/gwiki/src/audit/claims.rs:82-98] | Indexed function `frontmatter_source_has_code_span` in `crates/gwiki/src/audit/claims.rs`. [crates/gwiki/src/audit/claims.rs:82-98] |
| `frontmatter_range_is_valid` | function | `fn frontmatter_range_is_valid(value: &Value) -> bool {` | `frontmatter_range_is_valid [function]` | `646fd59a-8711-5d1d-82f6-38a417a482a6` | 100-106 [crates/gwiki/src/audit/claims.rs:100-106] | Indexed function `frontmatter_range_is_valid` in `crates/gwiki/src/audit/claims.rs`. [crates/gwiki/src/audit/claims.rs:100-106] |
| `supported_claim_lines` | function | `fn supported_claim_lines(` | `supported_claim_lines [function]` | `213ddb02-a92c-55a7-b7e8-ce12fd455afb` | 108-145 [crates/gwiki/src/audit/claims.rs:108-145] | Indexed function `supported_claim_lines` in `crates/gwiki/src/audit/claims.rs`. [crates/gwiki/src/audit/claims.rs:108-145] |
| `ClaimLine` | class | `pub(super) struct ClaimLine {` | `ClaimLine [class]` | `2a2866b8-0e85-5583-8267-60b8fd16edd4` | 148-153 [crates/gwiki/src/audit/claims.rs:148-153] | Indexed class `ClaimLine` in `crates/gwiki/src/audit/claims.rs`. [crates/gwiki/src/audit/claims.rs:148-153] |
| `ClaimKind` | type | `enum ClaimKind {` | `ClaimKind [type]` | `7e0e51e9-7522-59cd-a6ce-781274798d0b` | 156-159 [crates/gwiki/src/audit/claims.rs:156-159] | Indexed type `ClaimKind` in `crates/gwiki/src/audit/claims.rs`. [crates/gwiki/src/audit/claims.rs:156-159] |
| `claim_lines` | function | `pub(super) fn claim_lines(page: &WikiPage, options: &AuditOptions) -> Vec<ClaimLine> {` | `claim_lines [function]` | `2c337166-5272-5bc4-a295-8c06d43cd9f1` | 166-243 [crates/gwiki/src/audit/claims.rs:166-243] | Indexed function `claim_lines` in `crates/gwiki/src/audit/claims.rs`. [crates/gwiki/src/audit/claims.rs:166-243] |
| `claim_kind` | function | `fn claim_kind(text: &str) -> ClaimKind {` | `claim_kind [function]` | `ffd89550-d951-59b7-a8a8-ed43f4c1081c` | 245-251 [crates/gwiki/src/audit/claims.rs:245-251] | Indexed function `claim_kind` in `crates/gwiki/src/audit/claims.rs`. [crates/gwiki/src/audit/claims.rs:245-251] |
| `is_structural_codewiki_claim` | function | `fn is_structural_codewiki_claim(text: &str) -> bool {` | `is_structural_codewiki_claim [function]` | `39c1e0c0-6e67-5f9b-a9d3-a15c15de8cbd` | 253-262 [crates/gwiki/src/audit/claims.rs:253-262] | Indexed function `is_structural_codewiki_claim` in `crates/gwiki/src/audit/claims.rs`. [crates/gwiki/src/audit/claims.rs:253-262] |
| `heading_title` | function | `fn heading_title(line: &str) -> Option<String> {` | `heading_title [function]` | `ef51c03b-1755-5967-8954-55a0b6a7bf76` | 264-268 [crates/gwiki/src/audit/claims.rs:264-268] | Indexed function `heading_title` in `crates/gwiki/src/audit/claims.rs`. [crates/gwiki/src/audit/claims.rs:264-268] |
| `ignored_claim_section` | function | `fn ignored_claim_section(heading: Option<&str>, options: &AuditOptions) -> bool {` | `ignored_claim_section [function]` | `ceb9984d-3f54-5cb8-9eeb-f869f6a6dff6` | 270-272 [crates/gwiki/src/audit/claims.rs:270-272] | Indexed function `ignored_claim_section` in `crates/gwiki/src/audit/claims.rs`. [crates/gwiki/src/audit/claims.rs:270-272] |
| `ignored_claim_line` | function | `fn ignored_claim_line(line: &str) -> bool {` | `ignored_claim_line [function]` | `7f3ba8b5-835b-50f8-a279-9abab16398d6` | 274-281 [crates/gwiki/src/audit/claims.rs:274-281] | Indexed function `ignored_claim_line` in `crates/gwiki/src/audit/claims.rs`. [crates/gwiki/src/audit/claims.rs:274-281] |
| `is_thematic_break` | function | `fn is_thematic_break(line: &str) -> bool {` | `is_thematic_break [function]` | `5854c35e-e0b6-5738-af87-76f25cd61c18` | 283-295 [crates/gwiki/src/audit/claims.rs:283-295] | Indexed function `is_thematic_break` in `crates/gwiki/src/audit/claims.rs`. [crates/gwiki/src/audit/claims.rs:283-295] |
| `has_inline_source_support` | function | `pub(super) fn has_inline_source_support(line: &str) -> bool {` | `has_inline_source_support [function]` | `b2f1979f-585b-5a43-baf4-dc3896505436` | 297-305 [crates/gwiki/src/audit/claims.rs:297-305] | Indexed function `has_inline_source_support` in `crates/gwiki/src/audit/claims.rs`. [crates/gwiki/src/audit/claims.rs:297-305] |
| `has_code_source_span` | function | `fn has_code_source_span(line: &str) -> bool {` | `has_code_source_span [function]` | `ce09f2d1-c92c-53ec-85f5-4fcfd51528bc` | 307-320 [crates/gwiki/src/audit/claims.rs:307-320] | Indexed function `has_code_source_span` in `crates/gwiki/src/audit/claims.rs`. [crates/gwiki/src/audit/claims.rs:307-320] |
| `is_code_source_span` | function | `fn is_code_source_span(candidate: &str) -> bool {` | `is_code_source_span [function]` | `d4ce3bdb-6817-5c2e-8500-1bb69b8b1332` | 322-327 [crates/gwiki/src/audit/claims.rs:322-327] | Indexed function `is_code_source_span` in `crates/gwiki/src/audit/claims.rs`. [crates/gwiki/src/audit/claims.rs:322-327] |
| `is_code_source_path` | function | `fn is_code_source_path(path: &str) -> bool {` | `is_code_source_path [function]` | `fd2f5b36-16ed-534a-baa7-0355ea2b77ad` | 329-334 [crates/gwiki/src/audit/claims.rs:329-334] | Indexed function `is_code_source_path` in `crates/gwiki/src/audit/claims.rs`. [crates/gwiki/src/audit/claims.rs:329-334] |
| `is_line_span` | function | `fn is_line_span(span: &str) -> bool {` | `is_line_span [function]` | `44719776-0871-55f4-878c-ec897dd657df` | 336-347 [crates/gwiki/src/audit/claims.rs:336-347] | Indexed function `is_line_span` in `crates/gwiki/src/audit/claims.rs`. [crates/gwiki/src/audit/claims.rs:336-347] |
| `has_link_like_source_token` | function | `fn has_link_like_source_token(line: &str, token: &str) -> bool {` | `has_link_like_source_token [function]` | `871e5c2f-c3a6-5d37-b32d-2b5df199947c` | 349-371 [crates/gwiki/src/audit/claims.rs:349-371] | Indexed function `has_link_like_source_token` in `crates/gwiki/src/audit/claims.rs`. [crates/gwiki/src/audit/claims.rs:349-371] |
