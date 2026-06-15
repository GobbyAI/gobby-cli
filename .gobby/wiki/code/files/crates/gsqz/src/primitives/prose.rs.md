---
title: crates/gsqz/src/primitives/prose.rs
type: code_file
provenance:
- file: crates/gsqz/src/primitives/prose.rs
  ranges:
  - 5-9
  - 11-20
  - 23-34
  - 50-100
  - 102-109
  - 116-124
  - 187-211
  - 218-278
  - 280-303
  - 310-314
  - 317-321
  - 324-328
  - 331-335
  - 338-343
  - 346-350
  - 353-363
  - 366-370
  - 373-378
  - 381-386
  - 389-393
  - 396-399
  - 402-407
  - 410-418
  - 421-425
  - 428-432
  - 435-439
  - 442-446
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gsqz/src/primitives/prose.rs

Module: [[code/modules/crates/gsqz/src/primitives|crates/gsqz/src/primitives]]

## Purpose

Defines a prose-compression utility with three levels, `Lite`, `Standard`, and `Aggressive`, plus a string parser for selecting a level from `"lite"`, `"standard"`, or `"aggressive"`. The main `compress_prose` pipeline first extracts and protects YAML frontmatter, fenced code blocks, inline code, URLs, XML tags, and file paths, then applies the chosen compression strategy, and finally restores the protected spans. `Lite` does basic cleanup, `Standard` adds filler-phrase and filler-word reduction while preserving structure, and `Aggressive` truncates lists and multi-sentence paragraphs more heavily; the tests cover level parsing, preservation behavior, and each compression mode’s core transformations.
[crates/gsqz/src/primitives/prose.rs:5-9]
[crates/gsqz/src/primitives/prose.rs:11-20]
[crates/gsqz/src/primitives/prose.rs:12-19]
[crates/gsqz/src/primitives/prose.rs:23-34]
[crates/gsqz/src/primitives/prose.rs:50-100]

## API Symbols

- `Level` (type) component `Level [type]` (`3ca658d6-488a-5acf-b927-891537b26e87`) lines 5-9 [crates/gsqz/src/primitives/prose.rs:5-9]
  - Signature: `pub enum Level {`
  - Purpose: Indexed type `Level` in `crates/gsqz/src/primitives/prose.rs`. [crates/gsqz/src/primitives/prose.rs:5-9]
- `Level` (class) component `Level [class]` (`7c933687-ad7e-5051-8af0-8245e9894c42`) lines 11-20 [crates/gsqz/src/primitives/prose.rs:11-20]
  - Signature: `impl Level {`
  - Purpose: A fallible string parser that maps the literals "lite", "standard", and "aggressive" to their corresponding `Level` enum variants, returning `None` for unrecognized inputs. [crates/gsqz/src/primitives/prose.rs:11-20]
- `Level.from_str` (method) component `Level.from_str [method]` (`dfcaf855-3e24-50d8-a6d5-6624c6be66ed`) lines 12-19 [crates/gsqz/src/primitives/prose.rs:12-19]
  - Signature: `pub fn from_str(s: &str) -> Option<Self> {`
  - Purpose: # Summary

This method parses a string slice into an optional enum variant by pattern matching against three literal string patterns ("lite", "standard", "aggressive"), returning `None` for unrecognized input. [crates/gsqz/src/primitives/prose.rs:12-19]
- `compress_prose` (function) component `compress_prose [function]` (`a5c1a010-6aec-52d0-a208-1448cd9c8227`) lines 23-34 [crates/gsqz/src/primitives/prose.rs:23-34]
  - Signature: `pub fn compress_prose(input: &str, level: Level) -> String {`
  - Purpose: `compress_prose` applies level-based text compression (Lite, Standard, or Aggressive) to input prose while protecting and restoring fenced code blocks and YAML frontmatter. [crates/gsqz/src/primitives/prose.rs:23-34]
- `extract_protected` (function) component `extract_protected [function]` (`8851a2f6-632a-526d-8b9d-9a31607b0085`) lines 50-100 [crates/gsqz/src/primitives/prose.rs:50-100]
  - Signature: `fn extract_protected(input: &str) -> (String, Vec<String>) {`
  - Purpose: Extracts YAML frontmatter, code blocks, inline code, URLs, XML tags, and file paths from input text, replacing them with indexed placeholders while returning both the modified text and a vector of the extracted elements. [crates/gsqz/src/primitives/prose.rs:50-100]
- `restore_protected` (function) component `restore_protected [function]` (`e362714e-b998-55c2-8ea5-d97e45cfd471`) lines 102-109 [crates/gsqz/src/primitives/prose.rs:102-109]
  - Signature: `fn restore_protected(text: &str, protected: &[String]) -> String {`
  - Purpose: Restores protected strings by replacing indexed placeholders (`__GSQZ_P[n]__`) in the input text with their corresponding values from the protected array. [crates/gsqz/src/primitives/prose.rs:102-109]
- `compress_lite` (function) component `compress_lite [function]` (`3570fc24-aa31-543c-b1f8-f33c32b78779`) lines 116-124 [crates/gsqz/src/primitives/prose.rs:116-124]
  - Signature: `fn compress_lite(text: &str) -> String {`
  - Purpose: `compress_lite` removes HTML comments, normalizes multiple consecutive blank lines to double newlines, and trims trailing whitespace from each line. [crates/gsqz/src/primitives/prose.rs:116-124]
- `compress_standard` (function) component `compress_standard [function]` (`cc17b08f-4d98-5910-a8a2-ee3a882f6d48`) lines 187-211 [crates/gsqz/src/primitives/prose.rs:187-211]
  - Signature: `fn compress_standard(text: &str) -> String {`
  - Purpose: `compress_standard` compresses text through sequential lite compression, regex-based filler phrase replacement, and selective filler word removal on non-heading/non-code lines while collapsing whitespace. [crates/gsqz/src/primitives/prose.rs:187-211]
- `compress_aggressive` (function) component `compress_aggressive [function]` (`bc9da16f-e7d5-5851-b23a-c82209638496`) lines 218-278 [crates/gsqz/src/primitives/prose.rs:218-278]
  - Signature: `fn compress_aggressive(text: &str) -> String {`
  - Purpose: Applies aggressive compression by limiting list items to the first five, truncating multi-sentence paragraphs to their opening sentence, and preserving structural elements (headings, protected placeholders, blank lines). [crates/gsqz/src/primitives/prose.rs:218-278]
- `split_sentences` (function) component `split_sentences [function]` (`8c88eaf1-c45f-5c89-85ed-37bc231c53db`) lines 280-303 [crates/gsqz/src/primitives/prose.rs:280-303]
  - Signature: `fn split_sentences(text: &str) -> Vec<&str> {`
  - Purpose: Splits a string into trimmed sentence slices at boundaries marked by sentence-ending punctuation (`.!?`) followed by whitespace, using regex matching. [crates/gsqz/src/primitives/prose.rs:280-303]
- `test_lite_collapses_blank_lines` (function) component `test_lite_collapses_blank_lines [function]` (`d8c29844-440f-5abc-9c02-922103991024`) lines 310-314 [crates/gsqz/src/primitives/prose.rs:310-314]
  - Signature: `fn test_lite_collapses_blank_lines() {`
  - Purpose: Verifies that `compress_prose` with `Level::Lite` normalizes sequences of 3 or more consecutive newlines to exactly 2 newlines. [crates/gsqz/src/primitives/prose.rs:310-314]
- `test_lite_strips_html_comments` (function) component `test_lite_strips_html_comments [function]` (`7447b2b8-52eb-527f-8ccb-e165078936d0`) lines 317-321 [crates/gsqz/src/primitives/prose.rs:317-321]
  - Signature: `fn test_lite_strips_html_comments() {`
  - Purpose: Verifies that `compress_prose()` with `Level::Lite` removes HTML comments from input text while preserving surrounding content. [crates/gsqz/src/primitives/prose.rs:317-321]
- `test_lite_trims_trailing_whitespace` (function) component `test_lite_trims_trailing_whitespace [function]` (`87daea3a-eb20-56ed-b142-dd7bbe06f786`) lines 324-328 [crates/gsqz/src/primitives/prose.rs:324-328]
  - Signature: `fn test_lite_trims_trailing_whitespace() {`
  - Purpose: This test asserts that `compress_prose` with `Level::Lite` removes trailing whitespace from each line while preserving newline characters. [crates/gsqz/src/primitives/prose.rs:324-328]
- `test_standard_replaces_filler_phrases` (function) component `test_standard_replaces_filler_phrases [function]` (`61bc4ff8-3bf6-5d90-8a8b-b93e94b18a4c`) lines 331-335 [crates/gsqz/src/primitives/prose.rs:331-335]
  - Signature: `fn test_standard_replaces_filler_phrases() {`
  - Purpose: Tests that `compress_prose` with `Level::Standard` removes filler phrases by replacing "In order to" with "To" at the sentence start. [crates/gsqz/src/primitives/prose.rs:331-335]
- `test_standard_removes_filler_words` (function) component `test_standard_removes_filler_words [function]` (`71d84431-22f3-5f78-853e-f6086597054e`) lines 338-343 [crates/gsqz/src/primitives/prose.rs:338-343]
  - Signature: `fn test_standard_removes_filler_words() {`
  - Purpose: Tests that `compress_prose` with `Level::Standard` removes filler words ("basically" and "essentially") from input prose. [crates/gsqz/src/primitives/prose.rs:338-343]
- `test_standard_preserves_headings` (function) component `test_standard_preserves_headings [function]` (`94dfbc7f-5dc2-59c2-a040-a0f9d3452cfa`) lines 346-350 [crates/gsqz/src/primitives/prose.rs:346-350]
  - Signature: `fn test_standard_preserves_headings() {`
  - Purpose: Verifies that `compress_prose` with `Level::Standard` preserves markdown headings in the compressed output. [crates/gsqz/src/primitives/prose.rs:346-350]
- `test_aggressive_truncates_long_lists` (function) component `test_aggressive_truncates_long_lists [function]` (`8eb4aa5c-88fa-595b-b57a-a98e8fb76bbf`) lines 353-363 [crates/gsqz/src/primitives/prose.rs:353-363]
  - Signature: `fn test_aggressive_truncates_long_lists() {`
  - Purpose: Tests that `compress_prose` at `Level::Aggressive` truncates lists to retain only the first five items and replaces the remaining items with a count placeholder `[... 5 more items]`. [crates/gsqz/src/primitives/prose.rs:353-363]
- `test_aggressive_keeps_first_sentence` (function) component `test_aggressive_keeps_first_sentence [function]` (`5a190088-d6c2-5228-90e7-b705bc96eae4`) lines 366-370 [crates/gsqz/src/primitives/prose.rs:366-370]
  - Signature: `fn test_aggressive_keeps_first_sentence() {`
  - Purpose: This unit test asserts that `compress_prose` with `Level::Aggressive` truncates multi-sentence input to only the first sentence. [crates/gsqz/src/primitives/prose.rs:366-370]
- `test_preserves_code_blocks` (function) component `test_preserves_code_blocks [function]` (`ac07b82d-7d3a-5780-88d9-8cf9e7e8b088`) lines 373-378 [crates/gsqz/src/primitives/prose.rs:373-378]
  - Signature: `fn test_preserves_code_blocks() {`
  - Purpose: This test validates that `compress_prose` with `Level::Standard` preserves code block content while compressing adjacent prose by removing filler words. [crates/gsqz/src/primitives/prose.rs:373-378]
- `test_preserves_yaml_frontmatter` (function) component `test_preserves_yaml_frontmatter [function]` (`932462bb-6f94-59cb-b91f-aa35a2965a94`) lines 381-386 [crates/gsqz/src/primitives/prose.rs:381-386]
  - Signature: `fn test_preserves_yaml_frontmatter() {`
  - Purpose: Verifies that `compress_prose(Level::Standard)` preserves YAML frontmatter while compressing the document body text. [crates/gsqz/src/primitives/prose.rs:381-386]
- `test_empty_input` (function) component `test_empty_input [function]` (`c1d900e4-a469-587e-9518-489868679bf3`) lines 389-393 [crates/gsqz/src/primitives/prose.rs:389-393]
  - Signature: `fn test_empty_input() {`
  - Purpose: Verifies that the `compress_prose` function returns an empty string for empty input across all three compression levels (Lite, Standard, Aggressive). [crates/gsqz/src/primitives/prose.rs:389-393]
- `test_already_concise_passthrough` (function) component `test_already_concise_passthrough [function]` (`08ebd6f5-3cf3-5b20-91e6-5f7571d66a4e`) lines 396-399 [crates/gsqz/src/primitives/prose.rs:396-399]
  - Signature: `fn test_already_concise_passthrough() {`
  - Purpose: This test asserts that `compress_prose()` with `Level::Standard` returns the input string unchanged when the text is already concise, demonstrating passthrough behavior. [crates/gsqz/src/primitives/prose.rs:396-399]
- `test_level_from_str` (function) component `test_level_from_str [function]` (`9b162aa1-f0e9-54e9-9f8e-4194cea7f8d8`) lines 402-407 [crates/gsqz/src/primitives/prose.rs:402-407]
  - Signature: `fn test_level_from_str() {`
  - Purpose: Verifies that `Level::from_str()` correctly parses valid string literals ("lite", "standard", "aggressive") into their corresponding `Level` enum variants and returns `None` for invalid input. [crates/gsqz/src/primitives/prose.rs:402-407]
- `test_numbered_list_truncation` (function) component `test_numbered_list_truncation [function]` (`4aa2a455-8a2d-5bdc-a9a8-5f23a5e83d51`) lines 410-418 [crates/gsqz/src/primitives/prose.rs:410-418]
  - Signature: `fn test_numbered_list_truncation() {`
  - Purpose: This test verifies that `compress_prose` with `Level::Aggressive` compression truncates a numbered list by preserving the first item and replacing subsequent items with a truncation placeholder `[... 3 more items]`. [crates/gsqz/src/primitives/prose.rs:410-418]
- `test_preserves_inline_code` (function) component `test_preserves_inline_code [function]` (`7abaefda-2fa9-5783-9433-2813efc0cf2f`) lines 421-425 [crates/gsqz/src/primitives/prose.rs:421-425]
  - Signature: `fn test_preserves_inline_code() {`
  - Purpose: Verifies that the `compress_prose` function with `Level::Standard` preserves backtick-delimited inline code when compressing text. [crates/gsqz/src/primitives/prose.rs:421-425]
- `test_preserves_urls` (function) component `test_preserves_urls [function]` (`ac7b454d-77b4-5b07-964b-2a84ed01c357`) lines 428-432 [crates/gsqz/src/primitives/prose.rs:428-432]
  - Signature: `fn test_preserves_urls() {`
  - Purpose: Verifies that `compress_prose()` with `Level::Standard` preserves URLs unchanged in its output. [crates/gsqz/src/primitives/prose.rs:428-432]
- `test_preserves_xml_tags` (function) component `test_preserves_xml_tags [function]` (`4e61b741-cad2-564f-b126-fabefc70b41f`) lines 435-439 [crates/gsqz/src/primitives/prose.rs:435-439]
  - Signature: `fn test_preserves_xml_tags() {`
  - Purpose: This test verifies that the `compress_prose` function preserves XML tags with their attributes intact when performing Standard-level text compression. [crates/gsqz/src/primitives/prose.rs:435-439]
- `test_preserves_file_paths` (function) component `test_preserves_file_paths [function]` (`52084e5e-5d60-56ed-b1a6-12bbff60d3be`) lines 442-446 [crates/gsqz/src/primitives/prose.rs:442-446]
  - Signature: `fn test_preserves_file_paths() {`
  - Purpose: This test verifies that the `compress_prose` function with `Level::Standard` compression preserves relative file paths within the input text. [crates/gsqz/src/primitives/prose.rs:442-446]

