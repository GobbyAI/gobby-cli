---
title: crates/gcode/src/commands/codewiki/prompts.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/prompts.rs
  ranges:
  - 13-35
  - 37-59
  - 64-69
  - 71-87
  - 89-124
  - 126-142
  - 146-174
  - 177-190
  - 192-231
  - 233-248
  - 266-284
  - 288-302
  - 305-313
  - 316-319
  - 324-329
  - 335-344
  - 347-367
  - 370-377
  - 380-387
  - 389-396
  - 399-423
  - 426-429
  - 432-440
  - 443-463
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/prompts.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

This file defines the prompt-building layer for `codewiki` documentation generation. It provides system instructions and helper functions that assemble prompts for symbols, files, modules, repositories, and architecture overviews by combining names, kinds, line ranges, child summaries, and bounded source excerpts into consistent text templates. The small data structs (`SymbolSummary`, `ChildSummary`, `SourceExcerpt`) carry the metadata these builders format, while the tests verify that summaries and excerpts are truncated, flattened, and omitted with explicit placeholders when empty.
[crates/gcode/src/commands/codewiki/prompts.rs:13-35]
[crates/gcode/src/commands/codewiki/prompts.rs:37-59]
[crates/gcode/src/commands/codewiki/prompts.rs:64-69]
[crates/gcode/src/commands/codewiki/prompts.rs:71-87]
[crates/gcode/src/commands/codewiki/prompts.rs:89-124]

## API Symbols

- `symbol_prompt` (function) component `symbol_prompt [function]` (`aa346d01-c654-54ae-b635-6176f8fe0d30`) lines 13-35 [crates/gcode/src/commands/codewiki/prompts.rs:13-35]
  - Signature: `pub fn symbol_prompt(symbol: &Symbol) -> String {`
  - Purpose: Builds a multiline prompt string containing the symbol’s file path, qualified name, kind, and line range, then conditionally appends non-empty signature and docstring sections. [crates/gcode/src/commands/codewiki/prompts.rs:13-35]
- `file_prompt` (function) component `file_prompt [function]` (`786022e4-1bf5-545f-bed7-7458cbdcf216`) lines 37-59 [crates/gcode/src/commands/codewiki/prompts.rs:37-59]
  - Signature: `pub fn file_prompt(file: &str, symbols: &[SymbolSummary], sources: &[SourceExcerpt]) -> String {`
  - Purpose: Builds a prompt string instructing a single-file summary from AST symbols, listing each symbol’s metadata and appending source excerpts. [crates/gcode/src/commands/codewiki/prompts.rs:37-59]
- `content_file_prompt` (function) component `content_file_prompt [function]` (`d71303b4-ab3f-5785-8fcf-ff4b77b34645`) lines 64-69 [crates/gcode/src/commands/codewiki/prompts.rs:64-69]
  - Signature: `pub fn content_file_prompt(file: &str, source: &SourceExcerpt) -> String {`
  - Purpose: Builds a prompt string instructing a single summary of a repository file from its leading content, then appends a source excerpt section for the provided 'SourceExcerpt' and returns the combined prompt. [crates/gcode/src/commands/codewiki/prompts.rs:64-69]
- `module_prompt` (function) component `module_prompt [function]` (`a33b704c-1a1b-5ce3-a770-69648187e83a`) lines 71-87 [crates/gcode/src/commands/codewiki/prompts.rs:71-87]
  - Signature: `pub fn module_prompt(`
  - Purpose: 'module_prompt' builds and returns a module-focused documentation brief string by delegating the module name, file summaries, child module summaries, component names, and source excerpts to 'build_entity_prompt' with a fixed module-documentation instruction. [crates/gcode/src/commands/codewiki/prompts.rs:71-87]
- `repo_prompt` (function) component `repo_prompt [function]` (`c15c5a81-0157-5714-a08d-d2255cc4173b`) lines 89-124 [crates/gcode/src/commands/codewiki/prompts.rs:89-124]
  - Signature: `pub fn repo_prompt(`
  - Purpose: Builds and returns a formatted repository-overview prompt string by listing module summaries, root-file summaries, and appended source excerpts, using fallback “No modules/files” lines when the corresponding slices are empty. [crates/gcode/src/commands/codewiki/prompts.rs:89-124]
- `architecture_prompt` (function) component `architecture_prompt [function]` (`ad4692e5-86db-52db-916b-603d6cf979e8`) lines 126-142 [crates/gcode/src/commands/codewiki/prompts.rs:126-142]
  - Signature: `pub fn architecture_prompt(`
  - Purpose: Builds and returns a repository architecture overview prompt for a given subsystem by delegating the subsystem name, file/module summaries, components, and source excerpts to 'build_entity_prompt' with a subsystem-responsibility instruction. [crates/gcode/src/commands/codewiki/prompts.rs:126-142]
- `architecture_narrative_prompt` (function) component `architecture_narrative_prompt [function]` (`108e7b5d-1f85-5b17-b7d1-505674480d6a`) lines 146-174 [crates/gcode/src/commands/codewiki/prompts.rs:146-174]
  - Signature: `pub fn architecture_narrative_prompt(`
  - Purpose: Builds and returns a Markdown-style prompt string that enumerates subsystem summaries and dependency edges, inserting explicit “no data” placeholders when either input slice is empty. [crates/gcode/src/commands/codewiki/prompts.rs:146-174]
- `build_entity_prompt` (function) component `build_entity_prompt [function]` (`c6904a06-8b68-52c3-9883-39b29d6211f5`) lines 177-190 [crates/gcode/src/commands/codewiki/prompts.rs:177-190]
  - Signature: `fn build_entity_prompt(`
  - Purpose: Constructs a prompt string by formatting the header and entity label/value, then appending child-summary sections for files/modules/components and a source-excerpt section before returning the assembled 'String'. [crates/gcode/src/commands/codewiki/prompts.rs:177-190]
- `append_child_summary_sections` (function) component `append_child_summary_sections [function]` (`999fb395-4547-5af6-8182-5f53bd0f169a`) lines 192-231 [crates/gcode/src/commands/codewiki/prompts.rs:192-231]
  - Signature: `fn append_child_summary_sections(`
  - Purpose: It appends three labeled sections to 'prompt' listing direct files, child modules, and stable component IDs, emitting placeholder “none” lines when each collection is empty and otherwise formatting each entry with its name and summary excerpt. [crates/gcode/src/commands/codewiki/prompts.rs:192-231]
- `append_source_excerpt_section` (function) component `append_source_excerpt_section [function]` (`dcdf6c75-ce75-5c91-8d7f-a260287b98d3`) lines 233-248 [crates/gcode/src/commands/codewiki/prompts.rs:233-248]
  - Signature: `fn append_source_excerpt_section(prompt: &mut String, sources: &[SourceExcerpt]) {`
  - Purpose: Appends a 'Source excerpts:' section to 'prompt', emitting a no-excerpts marker when 'sources' is empty or otherwise formatting up to 'MAX_PROMPT_SOURCE_EXCERPTS' entries with each source’s path, line range, and bounded excerpt text. [crates/gcode/src/commands/codewiki/prompts.rs:233-248]
- `summary_excerpt` (function) component `summary_excerpt [function]` (`db7a8fcb-e142-53fc-a9fe-fca8b34ff76b`) lines 266-284 [crates/gcode/src/commands/codewiki/prompts.rs:266-284]
  - Signature: `fn summary_excerpt(summary: &str) -> String {`
  - Purpose: Returns a trimmed, whitespace-normalized excerpt of the first paragraph of 'summary', truncating it at 'CHILD_SUMMARY_EXCERPT_MAX_CHARS' Unicode scalar values and appending an ellipsis if truncation occurs. [crates/gcode/src/commands/codewiki/prompts.rs:266-284]
- `bounded_excerpt` (function) component `bounded_excerpt [function]` (`f0adace5-99f4-56e5-a3c9-af0f4b8bf4d3`) lines 288-302 [crates/gcode/src/commands/codewiki/prompts.rs:288-302]
  - Signature: `fn bounded_excerpt(excerpt: &str) -> String {`
  - Purpose: Trims trailing whitespace from 'excerpt', returns it unchanged if it is at most 'SOURCE_EXCERPT_MAX_CHARS' Unicode scalar values long, otherwise truncates at the corresponding character boundary and appends an ellipsis ('…'). [crates/gcode/src/commands/codewiki/prompts.rs:288-302]
- `SymbolSummary` (class) component `SymbolSummary [class]` (`5eaf4d1a-1881-5554-a303-5217845d3065`) lines 305-313 [crates/gcode/src/commands/codewiki/prompts.rs:305-313]
  - Signature: `pub struct SymbolSummary {`
  - Purpose: SymbolSummary is a Rust struct that stores a symbol’s name, kind, owning component ID and label, source line range, and free-text purpose description. [crates/gcode/src/commands/codewiki/prompts.rs:305-313]
- `ChildSummary` (class) component `ChildSummary [class]` (`af4e65d0-4a20-5d50-9a6a-2667f612315b`) lines 316-319 [crates/gcode/src/commands/codewiki/prompts.rs:316-319]
  - Signature: `pub struct ChildSummary {`
  - Purpose: 'ChildSummary' is a Rust struct containing two owned 'String' fields, 'name' and 'summary', used to represent a child item’s name and its associated summary text. [crates/gcode/src/commands/codewiki/prompts.rs:316-319]
- `SourceExcerpt` (class) component `SourceExcerpt [class]` (`25cbf9d8-d3b6-5695-8acb-2dc9c26e96dd`) lines 324-329 [crates/gcode/src/commands/codewiki/prompts.rs:324-329]
  - Signature: `pub struct SourceExcerpt {`
  - Purpose: 'SourceExcerpt' is a data-only Rust struct that represents a contiguous excerpt from a source file by storing its file path, inclusive line range, and extracted text. [crates/gcode/src/commands/codewiki/prompts.rs:324-329]
- `oversized_child` (function) component `oversized_child [function]` (`75a4637a-ecc5-57c6-8fa5-c0f024e10a86`) lines 335-344 [crates/gcode/src/commands/codewiki/prompts.rs:335-344]
  - Signature: `fn oversized_child(name: &str) -> ChildSummary {`
  - Purpose: Constructs a 'ChildSummary' by cloning 'name' into a 'String' and setting 'summary' to a string containing a fixed sentence followed by 2,000 newline-separated citation-like lines. [crates/gcode/src/commands/codewiki/prompts.rs:335-344]
- `aggregate_prompts_bound_each_child_summary` (function) component `aggregate_prompts_bound_each_child_summary [function]` (`af887455-a30d-5386-92ca-530471da959c`) lines 347-367 [crates/gcode/src/commands/codewiki/prompts.rs:347-367]
  - Signature: `fn aggregate_prompts_bound_each_child_summary() {`
  - Purpose: Verifies that child-summary lines emitted by 'module_prompt', 'architecture_prompt', and 'repo_prompt' for oversized 'src/' children are length-bounded and end with an ellipsis to indicate truncation. [crates/gcode/src/commands/codewiki/prompts.rs:347-367]
- `short_summaries_pass_through_untruncated` (function) component `short_summaries_pass_through_untruncated [function]` (`15e8a6d0-30dd-5fb6-a46f-b75cfc35f5e5`) lines 370-377 [crates/gcode/src/commands/codewiki/prompts.rs:370-377]
  - Signature: `fn short_summaries_pass_through_untruncated() {`
  - Purpose: Verifies that 'module_prompt' passes through a short child summary unchanged and includes it verbatim in the generated prompt. [crates/gcode/src/commands/codewiki/prompts.rs:370-377]
- `excerpt_flattens_multiline_summaries_to_one_line` (function) component `excerpt_flattens_multiline_summaries_to_one_line [function]` (`f14a8715-0b36-5471-951d-1822b02438dc`) lines 380-387 [crates/gcode/src/commands/codewiki/prompts.rs:380-387]
  - Signature: `fn excerpt_flattens_multiline_summaries_to_one_line() {`
  - Purpose: Verifies that 'module_prompt' renders a child summary’s multiline text as a single-line excerpt by replacing the newline with a space in the generated bullet list entry. [crates/gcode/src/commands/codewiki/prompts.rs:380-387]
- `excerpt` (function) component `excerpt [function]` (`1ae6bee1-316e-5845-99d4-d09c22b2bcaf`) lines 389-396 [crates/gcode/src/commands/codewiki/prompts.rs:389-396]
  - Signature: `fn excerpt(path: &str, content: &str) -> SourceExcerpt {`
  - Purpose: Constructs a 'SourceExcerpt' by copying the given 'path' and entire 'content' into owned strings and setting the excerpt's line range to fixed values '1..=40'. [crates/gcode/src/commands/codewiki/prompts.rs:389-396]
- `aggregate_prompts_embed_bounded_source_excerpts` (function) component `aggregate_prompts_embed_bounded_source_excerpts [function]` (`2db0c47a-ba90-5c4d-891b-cafc1cfce3a6`) lines 399-423 [crates/gcode/src/commands/codewiki/prompts.rs:399-423]
  - Signature: `fn aggregate_prompts_embed_bounded_source_excerpts() {`
  - Purpose: Verifies that 'module_prompt' caps embedded source excerpts at 'MAX_PROMPT_SOURCE_EXCERPTS' and keeps each excerpt block bounded in size even when given oversized source text. [crates/gcode/src/commands/codewiki/prompts.rs:399-423]
- `prompts_without_excerpts_state_their_absence` (function) component `prompts_without_excerpts_state_their_absence [function]` (`c1ef3246-2ce7-5af8-ba82-9d7eaf9889d4`) lines 426-429 [crates/gcode/src/commands/codewiki/prompts.rs:426-429]
  - Signature: `fn prompts_without_excerpts_state_their_absence() {`
  - Purpose: Asserts that 'repo_prompt' called with three empty slices includes the literal 'Source excerpts:\n- No source excerpts.\n' marker, verifying it explicitly states when no source excerpts are present. [crates/gcode/src/commands/codewiki/prompts.rs:426-429]
- `content_file_prompt_carries_leading_content` (function) component `content_file_prompt_carries_leading_content [function]` (`825a9d98-c7fb-59ac-970d-9f938ce31f7f`) lines 432-440 [crates/gcode/src/commands/codewiki/prompts.rs:432-440]
  - Signature: `fn content_file_prompt_carries_leading_content() {`
  - Purpose: Verifies that 'content_file_prompt' includes the filename header, line-range metadata, and the leading excerpt text when generating a prompt for 'README.md'. [crates/gcode/src/commands/codewiki/prompts.rs:432-440]
- `architecture_narrative_prompt_lists_subsystems_and_edges` (function) component `architecture_narrative_prompt_lists_subsystems_and_edges [function]` (`ade564ae-5574-560e-96f2-c30bc2162257`) lines 443-463 [crates/gcode/src/commands/codewiki/prompts.rs:443-463]
  - Signature: `fn architecture_narrative_prompt_lists_subsystems_and_edges() {`
  - Purpose: Verifies that 'architecture_narrative_prompt' renders each subsystem summary, includes formatted cross-subsystem dependency edges, and emits a specific no-edges message when the edge list is empty. [crates/gcode/src/commands/codewiki/prompts.rs:443-463]

