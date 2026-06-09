---
title: crates/gcode/src/commands/codewiki/text.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/text.rs
  ranges:
  - 8-20
  - 23-26
  - 28-59
  - 61-77
  - 79-87
  - 89-92
  - 94-109
  - 111-120
  - 122-134
  - 136-142
  - 144-146
  - 148-157
  - 159-169
  - 171-191
  - 193-200
  - 202-211
  - 213-219
  - 221-231
  - 233-246
  - 248-274
  - 276-293
  - 295-308
  - 310-312
  - 316-367
  - 373-379
  - 382-407
  - 410-424
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/text.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

`crates/gcode/src/commands/codewiki/text.rs` exposes 27 indexed API symbols.
[crates/gcode/src/commands/codewiki/text.rs:8-20] [crates/gcode/src/commands/codewiki/text.rs:23-26] [crates/gcode/src/commands/codewiki/text.rs:28-59] [crates/gcode/src/commands/codewiki/text.rs:61-77]
[crates/gcode/src/commands/codewiki/text.rs:79-87] [crates/gcode/src/commands/codewiki/text.rs:89-92] [crates/gcode/src/commands/codewiki/text.rs:94-109] [crates/gcode/src/commands/codewiki/text.rs:111-120]
[crates/gcode/src/commands/codewiki/text.rs:122-134] [crates/gcode/src/commands/codewiki/text.rs:136-142] [crates/gcode/src/commands/codewiki/text.rs:144-146] [crates/gcode/src/commands/codewiki/text.rs:148-157]
[crates/gcode/src/commands/codewiki/text.rs:159-169] [crates/gcode/src/commands/codewiki/text.rs:171-191] [crates/gcode/src/commands/codewiki/text.rs:193-200] [crates/gcode/src/commands/codewiki/text.rs:202-211]
[crates/gcode/src/commands/codewiki/text.rs:213-219] [crates/gcode/src/commands/codewiki/text.rs:221-231] [crates/gcode/src/commands/codewiki/text.rs:233-246] [crates/gcode/src/commands/codewiki/text.rs:248-274]
[crates/gcode/src/commands/codewiki/text.rs:276-293] [crates/gcode/src/commands/codewiki/text.rs:295-308] [crates/gcode/src/commands/codewiki/text.rs:310-312] [crates/gcode/src/commands/codewiki/text.rs:316-367]
[crates/gcode/src/commands/codewiki/text.rs:373-379] [crates/gcode/src/commands/codewiki/text.rs:382-407] [crates/gcode/src/commands/codewiki/text.rs:410-424]

## API Symbols

- `Frontmatter` (class) component `Frontmatter [class]` (`5e888c37-961f-5e8b-9167-bc80542f182f`) lines 8-20 [crates/gcode/src/commands/codewiki/text.rs:8-20]
  - Signature: `struct Frontmatter<'a> {`
  - Purpose: Indexed class `Frontmatter` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:8-20]
- `FrontmatterSourceFile` (class) component `FrontmatterSourceFile [class]` (`ef0454e6-7d8e-5e37-8dc1-04c834c91ce0`) lines 23-26 [crates/gcode/src/commands/codewiki/text.rs:23-26]
  - Signature: `struct FrontmatterSourceFile<'a> {`
  - Purpose: Indexed class `FrontmatterSourceFile` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:23-26]
- `resolve_text_generator` (function) component `resolve_text_generator [function]` (`a26a6d71-2213-5e3c-9352-2911bba74bf8`) lines 28-59 [crates/gcode/src/commands/codewiki/text.rs:28-59]
  - Signature: `pub(crate) fn resolve_text_generator(`
  - Purpose: Indexed function `resolve_text_generator` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:28-59]
- `resolve_ai_context` (function) component `resolve_ai_context [function]` (`92d6fb72-6370-54f4-8f4a-c2d3436874d7`) lines 61-77 [crates/gcode/src/commands/codewiki/text.rs:61-77]
  - Signature: `pub(crate) fn resolve_ai_context(`
  - Purpose: Indexed function `resolve_ai_context` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:61-77]
- `maybe_generate` (function) component `maybe_generate [function]` (`1f0e0319-f634-56a5-875f-a552dfeb373f`) lines 79-87 [crates/gcode/src/commands/codewiki/text.rs:79-87]
  - Signature: `pub(crate) fn maybe_generate(`
  - Purpose: Indexed function `maybe_generate` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:79-87]
- `clean_generated` (function) component `clean_generated [function]` (`54892051-a65e-5fdb-bb24-4e183b4d433a`) lines 89-92 [crates/gcode/src/commands/codewiki/text.rs:89-92]
  - Signature: `pub(crate) fn clean_generated(text: String) -> Option<String> {`
  - Purpose: Indexed function `clean_generated` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:89-92]
- `structural_symbol_purpose` (function) component `structural_symbol_purpose [function]` (`6077645c-2070-517f-97b9-e5d496a3ccd3`) lines 94-109 [crates/gcode/src/commands/codewiki/text.rs:94-109]
  - Signature: `pub(crate) fn structural_symbol_purpose(symbol: &Symbol) -> String {`
  - Purpose: Indexed function `structural_symbol_purpose` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:94-109]
- `structural_file_summary` (function) component `structural_file_summary [function]` (`4f717f81-c8af-5b31-ba9a-805a05ebe63f`) lines 111-120 [crates/gcode/src/commands/codewiki/text.rs:111-120]
  - Signature: `pub(crate) fn structural_file_summary(file: &str, symbols: &[SymbolDoc]) -> String {`
  - Purpose: Indexed function `structural_file_summary` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:111-120]
- `structural_module_summary` (function) component `structural_module_summary [function]` (`06f3b739-b627-5423-aae1-a2aa86644840`) lines 122-134 [crates/gcode/src/commands/codewiki/text.rs:122-134]
  - Signature: `pub(crate) fn structural_module_summary(`
  - Purpose: Indexed function `structural_module_summary` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:122-134]
- `structural_repo_summary` (function) component `structural_repo_summary [function]` (`25d49938-2870-56c3-abba-9dd4cdaedd1e`) lines 136-142 [crates/gcode/src/commands/codewiki/text.rs:136-142]
  - Signature: `pub(crate) fn structural_repo_summary(file_count: usize, module_count: usize) -> String {`
  - Purpose: Indexed function `structural_repo_summary` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:136-142]
- `write_section` (function) component `write_section [function]` (`2eeda5ca-b9dc-5f46-9cf9-9407d5884bae`) lines 144-146 [crates/gcode/src/commands/codewiki/text.rs:144-146]
  - Signature: `pub(crate) fn write_section(doc: &mut String, heading: &str, body: &str) {`
  - Purpose: Indexed function `write_section` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:144-146]
- `collect_link_spans` (function) component `collect_link_spans [function]` (`16c9aea8-0c7e-5596-8766-59d6c81f28f0`) lines 148-157 [crates/gcode/src/commands/codewiki/text.rs:148-157]
  - Signature: `pub(crate) fn collect_link_spans(files: &[FileLink], modules: &[ModuleLink]) -> Vec<SourceSpan> {`
  - Purpose: Indexed function `collect_link_spans` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:148-157]
- `citation_list` (function) component `citation_list [function]` (`cf5fee06-d6e5-5058-acbd-ff8c12e472be`) lines 159-169 [crates/gcode/src/commands/codewiki/text.rs:159-169]
  - Signature: `pub(crate) fn citation_list(spans: &[SourceSpan]) -> String {`
  - Purpose: Indexed function `citation_list` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:159-169]
- `wrap_citation_items` (function) component `wrap_citation_items [function]` (`69073f1a-b7ab-5d06-9a82-b48c53c30f9e`) lines 171-191 [crates/gcode/src/commands/codewiki/text.rs:171-191]
  - Signature: `fn wrap_citation_items<I>(items: I, max_line_width: usize) -> String`
  - Purpose: Indexed function `wrap_citation_items` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:171-191]
- `citation_markers` (function) component `citation_markers [function]` (`64c7fdea-18c1-5603-b790-bc67ed143852`) lines 193-200 [crates/gcode/src/commands/codewiki/text.rs:193-200]
  - Signature: `pub(crate) fn citation_markers(spans: &[SourceSpan]) -> String {`
  - Purpose: Indexed function `citation_markers` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:193-200]
- `citation_references` (function) component `citation_references [function]` (`003bdd5f-dd9e-5a24-836b-1681d7620adf`) lines 202-211 [crates/gcode/src/commands/codewiki/text.rs:202-211]
  - Signature: `fn citation_references(spans: &[SourceSpan]) -> Vec<(usize, String)> {`
  - Purpose: Indexed function `citation_references` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:202-211]
- `replace_citations_with_markers` (function) component `replace_citations_with_markers [function]` (`0aede9c4-6861-5675-9e05-603eb56c2244`) lines 213-219 [crates/gcode/src/commands/codewiki/text.rs:213-219]
  - Signature: `pub(crate) fn replace_citations_with_markers(text: &str, spans: &[SourceSpan]) -> String {`
  - Purpose: Indexed function `replace_citations_with_markers` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:213-219]
- `write_references` (function) component `write_references [function]` (`ec9b6758-e8a9-5c97-9240-3eafa1045211`) lines 221-231 [crates/gcode/src/commands/codewiki/text.rs:221-231]
  - Signature: `pub(crate) fn write_references(doc: &mut String, spans: &[SourceSpan]) {`
  - Purpose: Indexed function `write_references` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:221-231]
- `ground_text` (function) component `ground_text [function]` (`51edd45e-7197-5373-9af4-eb9f33c5c533`) lines 233-246 [crates/gcode/src/commands/codewiki/text.rs:233-246]
  - Signature: `pub(crate) fn ground_text(`
  - Purpose: Indexed function `ground_text` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:233-246]
- `strip_invalid_citations` (function) component `strip_invalid_citations [function]` (`a122fcae-b709-5bd9-87dd-3b2cc25eb2ac`) lines 248-274 [crates/gcode/src/commands/codewiki/text.rs:248-274]
  - Signature: `pub(crate) fn strip_invalid_citations(text: &str, valid_spans: &[SourceSpan]) -> String {`
  - Purpose: Indexed function `strip_invalid_citations` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:248-274]
- `contains_valid_citation` (function) component `contains_valid_citation [function]` (`c1f91387-b30f-5041-b060-bb01f1fd0a66`) lines 276-293 [crates/gcode/src/commands/codewiki/text.rs:276-293]
  - Signature: `pub(crate) fn contains_valid_citation(text: &str, valid_spans: &[SourceSpan]) -> bool {`
  - Purpose: Indexed function `contains_valid_citation` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:276-293]
- `citation_parts` (function) component `citation_parts [function]` (`faa0cf8c-7cca-523b-8094-5bd29a2a2255`) lines 295-308 [crates/gcode/src/commands/codewiki/text.rs:295-308]
  - Signature: `pub(crate) fn citation_parts(value: &str) -> Option<(&str, usize, usize)> {`
  - Purpose: Indexed function `citation_parts` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:295-308]
- `frontmatter` (function) component `frontmatter [function]` (`f86f161b-9c94-58df-9477-86c76734fdc1`) lines 310-312 [crates/gcode/src/commands/codewiki/text.rs:310-312]
  - Signature: `pub(crate) fn frontmatter(title: &str, kind: &str, source_spans: &[SourceSpan]) -> String {`
  - Purpose: Indexed function `frontmatter` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:310-312]
- `frontmatter_with_degradation` (function) component `frontmatter_with_degradation [function]` (`82350019-b173-5f9c-95be-6ea85088d14c`) lines 316-367 [crates/gcode/src/commands/codewiki/text.rs:316-367]
  - Signature: `pub(crate) fn frontmatter_with_degradation(`
  - Purpose: Indexed function `frontmatter_with_degradation` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:316-367]
- `span` (function) component `span [function]` (`69eef318-26f8-5260-a1c5-56364e35fb29`) lines 373-379 [crates/gcode/src/commands/codewiki/text.rs:373-379]
  - Signature: `fn span(file: impl Into<String>, line_start: usize, line_end: usize) -> SourceSpan {`
  - Purpose: Indexed function `span` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:373-379]
- `citation_list_wraps_fallback_citations_by_width` (function) component `citation_list_wraps_fallback_citations_by_width [function]` (`2e90d967-7ccf-5cf9-a6ef-1a60b3851aba`) lines 382-407 [crates/gcode/src/commands/codewiki/text.rs:382-407]
  - Signature: `fn citation_list_wraps_fallback_citations_by_width() {`
  - Purpose: Indexed function `citation_list_wraps_fallback_citations_by_width` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:382-407]
- `citation_markers_use_shared_width_wrapper` (function) component `citation_markers_use_shared_width_wrapper [function]` (`7dd12133-575d-5bde-9078-6ca57c01adcf`) lines 410-424 [crates/gcode/src/commands/codewiki/text.rs:410-424]
  - Signature: `fn citation_markers_use_shared_width_wrapper() {`
  - Purpose: Indexed function `citation_markers_use_shared_width_wrapper` in `crates/gcode/src/commands/codewiki/text.rs`. [crates/gcode/src/commands/codewiki/text.rs:410-424]

