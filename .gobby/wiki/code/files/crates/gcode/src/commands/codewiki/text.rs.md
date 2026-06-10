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
  - 159-168
  - 170-190
  - 192-199
  - 201-210
  - 212-218
  - 220-230
  - 232-245
  - 247-273
  - 275-292
  - 294-307
  - 309-311
  - 315-366
  - 372-378
  - 381-401
  - 404-418
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/text.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

`crates/gcode/src/commands/codewiki/text.rs` exposes 27 indexed API symbols.
[crates/gcode/src/commands/codewiki/text.rs:8-20]
[crates/gcode/src/commands/codewiki/text.rs:23-26]
[crates/gcode/src/commands/codewiki/text.rs:28-59]
[crates/gcode/src/commands/codewiki/text.rs:61-77]
[crates/gcode/src/commands/codewiki/text.rs:79-87]
[crates/gcode/src/commands/codewiki/text.rs:89-92]
[crates/gcode/src/commands/codewiki/text.rs:94-109]
[crates/gcode/src/commands/codewiki/text.rs:111-120]
[crates/gcode/src/commands/codewiki/text.rs:122-134]
[crates/gcode/src/commands/codewiki/text.rs:136-142]
[crates/gcode/src/commands/codewiki/text.rs:144-146]
[crates/gcode/src/commands/codewiki/text.rs:148-157]
[crates/gcode/src/commands/codewiki/text.rs:159-168]
[crates/gcode/src/commands/codewiki/text.rs:170-190]
[crates/gcode/src/commands/codewiki/text.rs:192-199]
[crates/gcode/src/commands/codewiki/text.rs:201-210]
[crates/gcode/src/commands/codewiki/text.rs:212-218]
[crates/gcode/src/commands/codewiki/text.rs:220-230]
[crates/gcode/src/commands/codewiki/text.rs:232-245]
[crates/gcode/src/commands/codewiki/text.rs:247-273]
[crates/gcode/src/commands/codewiki/text.rs:275-292]
[crates/gcode/src/commands/codewiki/text.rs:294-307]
[crates/gcode/src/commands/codewiki/text.rs:309-311]
[crates/gcode/src/commands/codewiki/text.rs:315-366]
[crates/gcode/src/commands/codewiki/text.rs:372-378]
[crates/gcode/src/commands/codewiki/text.rs:381-401]
[crates/gcode/src/commands/codewiki/text.rs:404-418]

## API Symbols

- `Frontmatter` (class) component `Frontmatter [class]` (`5e888c37-961f-5e8b-9167-bc80542f182f`) lines 8-20 [crates/gcode/src/commands/codewiki/text.rs:8-20]
  - Signature: `struct Frontmatter<'a> {`
  - Purpose: `Frontmatter<'a>` is a lifetime-parameterized struct that aggregates document metadata—including title, type, provenance, generation source, and quality indicators (trust, freshness)—with optional degradation tracking for serde serialization using borrowed string references. [crates/gcode/src/commands/codewiki/text.rs:8-20]
- `FrontmatterSourceFile` (class) component `FrontmatterSourceFile [class]` (`ef0454e6-7d8e-5e37-8dc1-04c834c91ce0`) lines 23-26 [crates/gcode/src/commands/codewiki/text.rs:23-26]
  - Signature: `struct FrontmatterSourceFile<'a> {`
  - Purpose: A lifetime-parameterized struct that pairs a borrowed source file reference with a vector of string ranges representing frontmatter sections or locations. [crates/gcode/src/commands/codewiki/text.rs:23-26]
- `resolve_text_generator` (function) component `resolve_text_generator [function]` (`a26a6d71-2213-5e3c-9352-2911bba74bf8`) lines 28-59 [crates/gcode/src/commands/codewiki/text.rs:28-59]
  - Signature: `pub(crate) fn resolve_text_generator(`
  - Purpose: Returns a boxed text generator closure that routes text generation requests through either daemon or direct API endpoints based on resolved AI routing configuration, with graceful error handling. [crates/gcode/src/commands/codewiki/text.rs:28-59]
- `resolve_ai_context` (function) component `resolve_ai_context [function]` (`92d6fb72-6370-54f4-8f4a-c2d3436874d7`) lines 61-77 [crates/gcode/src/commands/codewiki/text.rs:61-77]
  - Signature: `pub(crate) fn resolve_ai_context(`
  - Purpose: Resolves an AiContext by compositing PostgreSQL-backed and optional standalone AI configurations with optional routing override support. [crates/gcode/src/commands/codewiki/text.rs:61-77]
- `maybe_generate` (function) component `maybe_generate [function]` (`1f0e0319-f634-56a5-875f-a552dfeb373f`) lines 79-87 [crates/gcode/src/commands/codewiki/text.rs:79-87]
  - Signature: `pub(crate) fn maybe_generate(`
  - Purpose: Conditionally applies an optional mutable `TextGenerator` reference with the provided prompt and system parameters, returning the generated text if present or `None` otherwise. [crates/gcode/src/commands/codewiki/text.rs:79-87]
- `clean_generated` (function) component `clean_generated [function]` (`54892051-a65e-5fdb-bb24-4e183b4d433a`) lines 89-92 [crates/gcode/src/commands/codewiki/text.rs:89-92]
  - Signature: `pub(crate) fn clean_generated(text: String) -> Option<String> {`
  - Purpose: Returns `Some(String)` containing the trimmed input if non-empty, or `None` if the trimmed input is empty. [crates/gcode/src/commands/codewiki/text.rs:89-92]
- `structural_symbol_purpose` (function) component `structural_symbol_purpose [function]` (`6077645c-2070-517f-97b9-e5d496a3ccd3`) lines 94-109 [crates/gcode/src/commands/codewiki/text.rs:94-109]
  - Signature: `pub(crate) fn structural_symbol_purpose(symbol: &Symbol) -> String {`
  - Purpose: Returns a symbol's description by cascading through its non-empty summary, docstring, or a formatted default string containing the symbol's kind, qualified name, and file path. [crates/gcode/src/commands/codewiki/text.rs:94-109]
- `structural_file_summary` (function) component `structural_file_summary [function]` (`4f717f81-c8af-5b31-ba9a-805a05ebe63f`) lines 111-120 [crates/gcode/src/commands/codewiki/text.rs:111-120]
  - Signature: `pub(crate) fn structural_file_summary(file: &str, symbols: &[SymbolDoc]) -> String {`
  - Purpose: Constructs a summary string indicating the number of indexed API symbols exposed by a given file, or reports none if the symbols slice is empty. [crates/gcode/src/commands/codewiki/text.rs:111-120]
- `structural_module_summary` (function) component `structural_module_summary [function]` (`06f3b739-b627-5423-aae1-a2aa86644840`) lines 122-134 [crates/gcode/src/commands/codewiki/text.rs:122-134]
  - Signature: `pub(crate) fn structural_module_summary(`
  - Purpose: Returns a formatted string summarizing a module's structure by enumerating its direct file and child module counts with grammatical pluralization. [crates/gcode/src/commands/codewiki/text.rs:122-134]
- `structural_repo_summary` (function) component `structural_repo_summary [function]` (`25d49938-2870-56c3-abba-9dd4cdaedd1e`) lines 136-142 [crates/gcode/src/commands/codewiki/text.rs:136-142]
  - Signature: `pub(crate) fn structural_repo_summary(file_count: usize, module_count: usize) -> String {`
  - Purpose: Generates a formatted `String` describing repository code documentation coverage across a specified number of files and modules with conditional pluralization. [crates/gcode/src/commands/codewiki/text.rs:136-142]
- `write_section` (function) component `write_section [function]` (`2eeda5ca-b9dc-5f46-9cf9-9407d5884bae`) lines 144-146 [crates/gcode/src/commands/codewiki/text.rs:144-146]
  - Signature: `pub(crate) fn write_section(doc: &mut String, heading: &str, body: &str) {`
  - Purpose: Appends a markdown level-2 section with the provided heading and trimmed body content to a mutable document string. [crates/gcode/src/commands/codewiki/text.rs:144-146]
- `collect_link_spans` (function) component `collect_link_spans [function]` (`16c9aea8-0c7e-5596-8766-59d6c81f28f0`) lines 148-157 [crates/gcode/src/commands/codewiki/text.rs:148-157]
  - Signature: `pub(crate) fn collect_link_spans(files: &[FileLink], modules: &[ModuleLink]) -> Vec<SourceSpan> {`
  - Purpose: Aggregates and deduplicates source spans from FileLink and ModuleLink inputs into a sorted vector. [crates/gcode/src/commands/codewiki/text.rs:148-157]
- `citation_list` (function) component `citation_list [function]` (`cf5fee06-d6e5-5058-acbd-ff8c12e472be`) lines 159-168 [crates/gcode/src/commands/codewiki/text.rs:159-168]
  - Signature: `pub(crate) fn citation_list(spans: &[SourceSpan]) -> String {`
  - Purpose: This function deduplicates and sorts a slice of `SourceSpan` references using a `BTreeSet`, maps each to its citation representation, and returns the results joined as a newline-delimited string. [crates/gcode/src/commands/codewiki/text.rs:159-168]
- `wrap_citation_items` (function) component `wrap_citation_items [function]` (`863f17b8-6b40-5012-a727-852af745ba08`) lines 170-190 [crates/gcode/src/commands/codewiki/text.rs:170-190]
  - Signature: `fn wrap_citation_items<I>(items: I, max_line_width: usize) -> String`
  - Purpose: Wraps space-delimited citation items across multiple lines, breaking to a new line whenever the cumulative width would exceed the specified maximum line width. [crates/gcode/src/commands/codewiki/text.rs:170-190]
- `citation_markers` (function) component `citation_markers [function]` (`0b0512fa-8e9b-5441-b0f1-58420bc96497`) lines 192-199 [crates/gcode/src/commands/codewiki/text.rs:192-199]
  - Signature: `pub(crate) fn citation_markers(spans: &[SourceSpan]) -> String {`
  - Purpose: Converts source spans to citation references, formats their indices as bracketed markers `[n]`, and wraps them to a fallback line width. [crates/gcode/src/commands/codewiki/text.rs:192-199]
- `citation_references` (function) component `citation_references [function]` (`c636d715-1dba-57c2-a3c9-da9b3c5fb19d`) lines 201-210 [crates/gcode/src/commands/codewiki/text.rs:201-210]
  - Signature: `fn citation_references(spans: &[SourceSpan]) -> Vec<(usize, String)> {`
  - Purpose: Deduplicates and sorts source spans, then enumerates them with 1-based indices paired to their citation strings. [crates/gcode/src/commands/codewiki/text.rs:201-210]
- `replace_citations_with_markers` (function) component `replace_citations_with_markers [function]` (`b1fbc0a6-5338-5b7b-bd6f-840e8f1e1646`) lines 212-218 [crates/gcode/src/commands/codewiki/text.rs:212-218]
  - Signature: `pub(crate) fn replace_citations_with_markers(text: &str, spans: &[SourceSpan]) -> String {`
  - Purpose: Replaces citation strings in text with numbered bracket markers [n] corresponding to their indices in the provided source spans. [crates/gcode/src/commands/codewiki/text.rs:212-218]
- `write_references` (function) component `write_references [function]` (`e88ae08f-29ad-57bb-bc42-f47eb2c46b16`) lines 220-230 [crates/gcode/src/commands/codewiki/text.rs:220-230]
  - Signature: `pub(crate) fn write_references(doc: &mut String, spans: &[SourceSpan]) {`
  - Purpose: Appends a markdown-formatted References section containing indexed citations derived from source spans to a documentation string. [crates/gcode/src/commands/codewiki/text.rs:220-230]
- `ground_text` (function) component `ground_text [function]` (`b73bb34e-62c5-51b0-bb9b-c1068b28a7be`) lines 232-245 [crates/gcode/src/commands/codewiki/text.rs:232-245]
  - Signature: `pub(crate) fn ground_text(`
  - Purpose: Removes invalid citations from text based on valid source spans and appends a fallback citation (space or newline-delimited) if the cleaned text contains no valid citations. [crates/gcode/src/commands/codewiki/text.rs:232-245]
- `strip_invalid_citations` (function) component `strip_invalid_citations [function]` (`374204bf-6283-59a5-9f4e-e06d9e6a46e5`) lines 247-273 [crates/gcode/src/commands/codewiki/text.rs:247-273]
  - Signature: `pub(crate) fn strip_invalid_citations(text: &str, valid_spans: &[SourceSpan]) -> String {`
  - Purpose: Removes bracket-enclosed citations whose referenced source spans are not contained within the provided valid spans list. [crates/gcode/src/commands/codewiki/text.rs:247-273]
- `contains_valid_citation` (function) component `contains_valid_citation [function]` (`15933aa0-c92e-503d-ba3d-8e4f091870e3`) lines 275-292 [crates/gcode/src/commands/codewiki/text.rs:275-292]
  - Signature: `pub(crate) fn contains_valid_citation(text: &str, valid_spans: &[SourceSpan]) -> bool {`
  - Purpose: # Summary

Returns true if text contains a bracketed citation `[...]` whose parsed components (file, start, end) fall within any of the provided valid source spans. [crates/gcode/src/commands/codewiki/text.rs:275-292]
- `citation_parts` (function) component `citation_parts [function]` (`e7609374-0fb8-517c-9bde-4e0ca5cf4907`) lines 294-307 [crates/gcode/src/commands/codewiki/text.rs:294-307]
  - Signature: `pub(crate) fn citation_parts(value: &str) -> Option<(&str, usize, usize)> {`
  - Purpose: Parses a citation string split at the last `:` into a non-empty, whitespace-free file path and either a single line or `start-end` line range, returning `Some((file, line_start, line_end))` only when the bounds are numeric and `1 <= line_start <= line_end`, otherwise `None`. [crates/gcode/src/commands/codewiki/text.rs:294-307]
- `frontmatter` (function) component `frontmatter [function]` (`9d052ca9-5007-5f5c-a403-4d73805f6406`) lines 309-311 [crates/gcode/src/commands/codewiki/text.rs:309-311]
  - Signature: `pub(crate) fn frontmatter(title: &str, kind: &str, source_spans: &[SourceSpan]) -> String {`
  - Purpose: This is a thin wrapper that returns the result of `frontmatter_with_degradation(title, kind, source_spans, &[])`, i.e. it generates frontmatter with no degradation entries. [crates/gcode/src/commands/codewiki/text.rs:309-311]
- `frontmatter_with_degradation` (function) component `frontmatter_with_degradation [function]` (`a58f74d7-471e-5dea-88de-fd35d1e48a43`) lines 315-366 [crates/gcode/src/commands/codewiki/text.rs:315-366]
  - Signature: `pub(crate) fn frontmatter_with_degradation(`
  - Purpose: It deduplicates and sorts `source_spans` into per-file line ranges, builds a `Frontmatter` value with provenance plus degradation metadata, serializes it to YAML, and վերադարձs the result wrapped in `---` frontmatter delimiters with a trailing newline guaranteed. [crates/gcode/src/commands/codewiki/text.rs:315-366]
- `span` (function) component `span [function]` (`a8cd5c7d-9ada-557e-abfc-d6f6335dc6df`) lines 372-378 [crates/gcode/src/commands/codewiki/text.rs:372-378]
  - Signature: `fn span(file: impl Into<String>, line_start: usize, line_end: usize) -> SourceSpan {`
  - Purpose: Constructs and returns a `SourceSpan` by converting `file` into a `String` and populating its `file`, `line_start`, and `line_end` fields with the provided values. [crates/gcode/src/commands/codewiki/text.rs:372-378]
- `citation_list_emits_one_fallback_range_per_line` (function) component `citation_list_emits_one_fallback_range_per_line [function]` (`e15c99c4-c626-5918-8b9c-3eb197e9d6a0`) lines 381-401 [crates/gcode/src/commands/codewiki/text.rs:381-401]
  - Signature: `fn citation_list_emits_one_fallback_range_per_line() {`
  - Purpose: This test asserts that `citation_list(&spans)` returns exactly one newline-delimited citation per input span, and that each emitted line is the corresponding span’s `citation()` string. [crates/gcode/src/commands/codewiki/text.rs:381-401]
- `citation_markers_use_shared_width_wrapper` (function) component `citation_markers_use_shared_width_wrapper [function]` (`f7bb2055-75d7-5f4e-8133-084fc5bb6040`) lines 404-418 [crates/gcode/src/commands/codewiki/text.rs:404-418]
  - Signature: `fn citation_markers_use_shared_width_wrapper() {`
  - Purpose: This test constructs 80 single-point citation spans, formats them with `citation_markers`, and verifies the result wraps across multiple lines with every line length bounded by `FALLBACK_CITATION_LINE_WIDTH`. [crates/gcode/src/commands/codewiki/text.rs:404-418]

