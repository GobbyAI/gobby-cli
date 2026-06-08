---
title: crates/gcode/src/commands/codewiki/text.rs
type: code_file
source_files:
- file: crates/gcode/src/commands/codewiki/text.rs
  ranges:
  - 6-11
  - 14-17
  - 19-50
  - 52-68
  - 70-78
  - 80-83
  - 85-100
  - 102-111
  - 113-125
  - 127-133
  - 135-137
  - 139-148
  - 150-159
  - 161-172
  - 174-200
  - 202-219
  - 221-234
  - 236-277
---

# crates/gcode/src/commands/codewiki/text.rs

Module: [[modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

`crates/gcode/src/commands/codewiki/text.rs` exposes 18 indexed API symbols. [crates/gcode/src/commands/codewiki/text.rs:6-11] [crates/gcode/src/commands/codewiki/text.rs:14-17] [crates/gcode/src/commands/codewiki/text.rs:19-50] [crates/gcode/src/commands/codewiki/text.rs:52-68] [crates/gcode/src/commands/codewiki/text.rs:70-78] [crates/gcode/src/commands/codewiki/text.rs:80-83] [crates/gcode/src/commands/codewiki/text.rs:85-100] [crates/gcode/src/commands/codewiki/text.rs:102-111] [crates/gcode/src/commands/codewiki/text.rs:113-125] [crates/gcode/src/commands/codewiki/text.rs:127-133] [crates/gcode/src/commands/codewiki/text.rs:135-137] [crates/gcode/src/commands/codewiki/text.rs:139-148] [crates/gcode/src/commands/codewiki/text.rs:150-159] [crates/gcode/src/commands/codewiki/text.rs:161-172] [crates/gcode/src/commands/codewiki/text.rs:174-200] [crates/gcode/src/commands/codewiki/text.rs:202-219] [crates/gcode/src/commands/codewiki/text.rs:221-234] [crates/gcode/src/commands/codewiki/text.rs:236-277]

## API Symbols

- `Frontmatter` (class) component `Frontmatter [class]` (`08461f06-3472-5506-9d7d-453cb4ac9c44`) lines 6-11 [crates/gcode/src/commands/codewiki/text.rs:6-11]
  - Signature: `struct Frontmatter<'a> {`
  - Purpose: A lifetime-bound struct that encapsulates frontmatter metadata containing borrowed references to a title string, a type identifier, and a vector of associated source files. [crates/gcode/src/commands/codewiki/text.rs:6-11]
- `FrontmatterSourceFile` (class) component `FrontmatterSourceFile [class]` (`fe68d8e4-3c87-5bc5-b1a0-5fd0e4784f53`) lines 14-17 [crates/gcode/src/commands/codewiki/text.rs:14-17]
  - Signature: `struct FrontmatterSourceFile<'a> {`
  - Purpose: A lifetime-parameterized struct that associates a borrowed source file string reference with a vector of string ranges. [crates/gcode/src/commands/codewiki/text.rs:14-17]
- `resolve_text_generator` (function) component `resolve_text_generator [function]` (`029d9061-fe5a-5a89-8af0-de6b1988e932`) lines 19-50 [crates/gcode/src/commands/codewiki/text.rs:19-50]
  - Signature: `pub(crate) fn resolve_text_generator(`
  - Purpose: Returns an optional boxed closure that routes text generation prompts through either daemon or direct AI channels based on resolved configuration, with error recovery and optional warning on failure. [crates/gcode/src/commands/codewiki/text.rs:19-50]
- `resolve_ai_context` (function) component `resolve_ai_context [function]` (`3aa3aa5a-54d2-58fe-a6f6-e345b471853d`) lines 52-68 [crates/gcode/src/commands/codewiki/text.rs:52-68]
  - Signature: `pub(crate) fn resolve_ai_context(`
  - Purpose: Resolves AI context from combined PostgreSQL and standalone configuration sources, with optional forced routing override. [crates/gcode/src/commands/codewiki/text.rs:52-68]
- `maybe_generate` (function) component `maybe_generate [function]` (`f45981ff-c357-5f9f-a24c-f5f9edbd4ce7`) lines 70-78 [crates/gcode/src/commands/codewiki/text.rs:70-78]
  - Signature: `pub(crate) fn maybe_generate(`
  - Purpose: Invokes an optional mutable text generator with the provided prompt and system parameters, returning an optional string result or None if no generator is available. [crates/gcode/src/commands/codewiki/text.rs:70-78]
- `clean_generated` (function) component `clean_generated [function]` (`7840f92b-f63c-5f5a-a257-6c45dff73833`) lines 80-83 [crates/gcode/src/commands/codewiki/text.rs:80-83]
  - Signature: `pub(crate) fn clean_generated(text: String) -> Option<String> {`
  - Purpose: Trims whitespace from the input string and returns `Some(String)` if non-empty, otherwise `None`. [crates/gcode/src/commands/codewiki/text.rs:80-83]
- `structural_symbol_purpose` (function) component `structural_symbol_purpose [function]` (`b2d34cb9-b5b1-5d76-a9cc-fa7a4400f134`) lines 85-100 [crates/gcode/src/commands/codewiki/text.rs:85-100]
  - Signature: `pub(crate) fn structural_symbol_purpose(symbol: &Symbol) -> String {`
  - Purpose: Returns a descriptive string for a symbol by extracting its summary or docstring with fallback to a generated string containing the symbol's kind, qualified name, and file path. [crates/gcode/src/commands/codewiki/text.rs:85-100]
- `structural_file_summary` (function) component `structural_file_summary [function]` (`60919aa9-689b-53bc-8c52-260626bc69c7`) lines 102-111 [crates/gcode/src/commands/codewiki/text.rs:102-111]
  - Signature: `pub(crate) fn structural_file_summary(file: &str, symbols: &[SymbolDoc]) -> String {`
  - Purpose: This function generates a summary string reporting the count of indexed API symbols in a file, returning a special message if no symbols are present. [crates/gcode/src/commands/codewiki/text.rs:102-111]
- `structural_module_summary` (function) component `structural_module_summary [function]` (`754ba63e-f314-5986-a285-f55dba08627a`) lines 113-125 [crates/gcode/src/commands/codewiki/text.rs:113-125]
  - Signature: `pub(crate) fn structural_module_summary(`
  - Purpose: Generates a formatted string that summarizes a module's structural composition by reporting the counts of its direct files and child modules with appropriate pluralization. [crates/gcode/src/commands/codewiki/text.rs:113-125]
- `structural_repo_summary` (function) component `structural_repo_summary [function]` (`58d81b90-4edd-547f-ba0e-0c714d514859`) lines 127-133 [crates/gcode/src/commands/codewiki/text.rs:127-133]
  - Signature: `pub(crate) fn structural_repo_summary(file_count: usize, module_count: usize) -> String {`
  - Purpose: Generates a formatted string summary reporting a repository's file and module counts with grammatically correct pluralization. [crates/gcode/src/commands/codewiki/text.rs:127-133]
- `write_section` (function) component `write_section [function]` (`5cb731df-20f9-5cc1-876e-2c8f85f80e3c`) lines 135-137 [crates/gcode/src/commands/codewiki/text.rs:135-137]
  - Signature: `pub(crate) fn write_section(doc: &mut String, heading: &str, body: &str) {`
  - Purpose: Appends a markdown level-2 section with the specified heading and trimmed body content to a mutable string. [crates/gcode/src/commands/codewiki/text.rs:135-137]
- `collect_link_spans` (function) component `collect_link_spans [function]` (`5a52ba01-1b09-5290-bee3-7c59b8c2aa0f`) lines 139-148 [crates/gcode/src/commands/codewiki/text.rs:139-148]
  - Signature: `pub(crate) fn collect_link_spans(files: &[FileLink], modules: &[ModuleLink]) -> Vec<SourceSpan> {`
  - Purpose: Collects and deduplicates source spans from FileLink and ModuleLink arrays into a sorted vector using a BTreeSet. [crates/gcode/src/commands/codewiki/text.rs:139-148]
- `citation_list` (function) component `citation_list [function]` (`c64a9604-e252-5b7a-9722-8ae409c17011`) lines 150-159 [crates/gcode/src/commands/codewiki/text.rs:150-159]
  - Signature: `pub(crate) fn citation_list(spans: &[SourceSpan]) -> String {`
  - Purpose: Converts a slice of `SourceSpan` references into a space-separated string of deduplicated and sorted citations by collecting through a `BTreeSet`. [crates/gcode/src/commands/codewiki/text.rs:150-159]
- `ground_text` (function) component `ground_text [function]` (`3d7e3e09-1df1-52e6-a466-8c767f728b03`) lines 161-172 [crates/gcode/src/commands/codewiki/text.rs:161-172]
  - Signature: `pub(crate) fn ground_text(`
  - Purpose: Removes invalid citations from text and appends a fallback citation if the cleaned result contains no valid citations. [crates/gcode/src/commands/codewiki/text.rs:161-172]
- `strip_invalid_citations` (function) component `strip_invalid_citations [function]` (`7f70bfb1-c083-5dbb-b3fb-c6e9563f8483`) lines 174-200 [crates/gcode/src/commands/codewiki/text.rs:174-200]
  - Signature: `pub(crate) fn strip_invalid_citations(text: &str, valid_spans: &[SourceSpan]) -> String {`
  - Purpose: **Removes bracket notation from citations that parse successfully but are not contained within any of the provided valid source spans.** [crates/gcode/src/commands/codewiki/text.rs:174-200]
- `contains_valid_citation` (function) component `contains_valid_citation [function]` (`61a2937f-0344-59b8-8487-e17f7d12bb29`) lines 202-219 [crates/gcode/src/commands/codewiki/text.rs:202-219]
  - Signature: `pub(crate) fn contains_valid_citation(text: &str, valid_spans: &[SourceSpan]) -> bool {`
  - Purpose: # Summary

Returns `true` if the text contains at least one bracketed citation whose parsed file and byte range components are contained within a valid `SourceSpan`. [crates/gcode/src/commands/codewiki/text.rs:202-219]
- `citation_parts` (function) component `citation_parts [function]` (`eb984333-29ec-5303-bc3a-7d6c2affa0f8`) lines 221-234 [crates/gcode/src/commands/codewiki/text.rs:221-234]
  - Signature: `pub(crate) fn citation_parts(value: &str) -> Option<(&str, usize, usize)> {`
  - Purpose: This function parses a colon-delimited citation string into a file path and validated line range tuple (single line or start-end inclusive), returning `None` if the file is empty, contains whitespace, or the line numbers are invalid. [crates/gcode/src/commands/codewiki/text.rs:221-234]
- `frontmatter` (function) component `frontmatter [function]` (`54af2126-3616-51fa-abff-3a069ab985ed`) lines 236-277 [crates/gcode/src/commands/codewiki/text.rs:236-277]
  - Signature: `pub(crate) fn frontmatter(title: &str, kind: &str, source_spans: &[SourceSpan]) -> String {`
  - Purpose: Generates a YAML-formatted frontmatter block containing metadata (title, kind) and aggregated source file line ranges parsed from a slice of SourceSpan objects. [crates/gcode/src/commands/codewiki/text.rs:236-277]

