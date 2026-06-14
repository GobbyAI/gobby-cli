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

This file defines prompt templates and builders for an AI-driven code documentation system. It provides seven system prompts (SYMBOL_SYSTEM, FILE_SYSTEM, CONTENT_FILE_SYSTEM, MODULE_SYSTEM, REPO_SYSTEM, ARCHITECTURE_SYSTEM, ARCHITECTURE_NARRATIVE_SYSTEM) that instruct an LLM on how to generate different types of documentation. The core functions—symbol_prompt, file_prompt, content_file_prompt, module_prompt, repo_prompt, architecture_prompt, and architecture_narrative_prompt—construct complete prompts by combining these system instructions with code context like Symbol objects, file metadata, and excerpts. Supporting functions handle excerpt extraction (summary_excerpt, bounded_excerpt), child-summary aggregation (append_child_summary_sections), source-excerpt embedding (append_source_excerpt_section, aggregate_prompts_embed_bounded_source_excerpts), and formatting constraints (aggregate_prompts_bound_each_child_summary, oversized_child). Data structures SymbolSummary, ChildSummary, and SourceExcerpt organize the contextual information that gets composed into prompts. Test functions validate that summarization, truncation, and excerpt handling work correctly.
[crates/gcode/src/commands/codewiki/prompts.rs:13-35]
[crates/gcode/src/commands/codewiki/prompts.rs:37-59]
[crates/gcode/src/commands/codewiki/prompts.rs:64-69]
[crates/gcode/src/commands/codewiki/prompts.rs:71-87]
[crates/gcode/src/commands/codewiki/prompts.rs:89-124]

## API Symbols

- `symbol_prompt` (function) component `symbol_prompt [function]` (`aa346d01-c654-54ae-b635-6176f8fe0d30`) lines 13-35 [crates/gcode/src/commands/codewiki/prompts.rs:13-35]
  - Signature: `pub fn symbol_prompt(symbol: &Symbol) -> String {`
  - Purpose: Indexed function `symbol_prompt` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:13-35]
- `file_prompt` (function) component `file_prompt [function]` (`786022e4-1bf5-545f-bed7-7458cbdcf216`) lines 37-59 [crates/gcode/src/commands/codewiki/prompts.rs:37-59]
  - Signature: `pub fn file_prompt(file: &str, symbols: &[SymbolSummary], sources: &[SourceExcerpt]) -> String {`
  - Purpose: Indexed function `file_prompt` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:37-59]
- `content_file_prompt` (function) component `content_file_prompt [function]` (`d71303b4-ab3f-5785-8fcf-ff4b77b34645`) lines 64-69 [crates/gcode/src/commands/codewiki/prompts.rs:64-69]
  - Signature: `pub fn content_file_prompt(file: &str, source: &SourceExcerpt) -> String {`
  - Purpose: Indexed function `content_file_prompt` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:64-69]
- `module_prompt` (function) component `module_prompt [function]` (`a33b704c-1a1b-5ce3-a770-69648187e83a`) lines 71-87 [crates/gcode/src/commands/codewiki/prompts.rs:71-87]
  - Signature: `pub fn module_prompt(`
  - Purpose: Indexed function `module_prompt` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:71-87]
- `repo_prompt` (function) component `repo_prompt [function]` (`c15c5a81-0157-5714-a08d-d2255cc4173b`) lines 89-124 [crates/gcode/src/commands/codewiki/prompts.rs:89-124]
  - Signature: `pub fn repo_prompt(`
  - Purpose: Indexed function `repo_prompt` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:89-124]
- `architecture_prompt` (function) component `architecture_prompt [function]` (`ad4692e5-86db-52db-916b-603d6cf979e8`) lines 126-142 [crates/gcode/src/commands/codewiki/prompts.rs:126-142]
  - Signature: `pub fn architecture_prompt(`
  - Purpose: Indexed function `architecture_prompt` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:126-142]
- `architecture_narrative_prompt` (function) component `architecture_narrative_prompt [function]` (`108e7b5d-1f85-5b17-b7d1-505674480d6a`) lines 146-174 [crates/gcode/src/commands/codewiki/prompts.rs:146-174]
  - Signature: `pub fn architecture_narrative_prompt(`
  - Purpose: Indexed function `architecture_narrative_prompt` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:146-174]
- `build_entity_prompt` (function) component `build_entity_prompt [function]` (`c6904a06-8b68-52c3-9883-39b29d6211f5`) lines 177-190 [crates/gcode/src/commands/codewiki/prompts.rs:177-190]
  - Signature: `fn build_entity_prompt(`
  - Purpose: Indexed function `build_entity_prompt` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:177-190]
- `append_child_summary_sections` (function) component `append_child_summary_sections [function]` (`999fb395-4547-5af6-8182-5f53bd0f169a`) lines 192-231 [crates/gcode/src/commands/codewiki/prompts.rs:192-231]
  - Signature: `fn append_child_summary_sections(`
  - Purpose: Indexed function `append_child_summary_sections` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:192-231]
- `append_source_excerpt_section` (function) component `append_source_excerpt_section [function]` (`dcdf6c75-ce75-5c91-8d7f-a260287b98d3`) lines 233-248 [crates/gcode/src/commands/codewiki/prompts.rs:233-248]
  - Signature: `fn append_source_excerpt_section(prompt: &mut String, sources: &[SourceExcerpt]) {`
  - Purpose: Indexed function `append_source_excerpt_section` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:233-248]
- `summary_excerpt` (function) component `summary_excerpt [function]` (`db7a8fcb-e142-53fc-a9fe-fca8b34ff76b`) lines 266-284 [crates/gcode/src/commands/codewiki/prompts.rs:266-284]
  - Signature: `fn summary_excerpt(summary: &str) -> String {`
  - Purpose: Indexed function `summary_excerpt` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:266-284]
- `bounded_excerpt` (function) component `bounded_excerpt [function]` (`f0adace5-99f4-56e5-a3c9-af0f4b8bf4d3`) lines 288-302 [crates/gcode/src/commands/codewiki/prompts.rs:288-302]
  - Signature: `fn bounded_excerpt(excerpt: &str) -> String {`
  - Purpose: Indexed function `bounded_excerpt` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:288-302]
- `SymbolSummary` (class) component `SymbolSummary [class]` (`5eaf4d1a-1881-5554-a303-5217845d3065`) lines 305-313 [crates/gcode/src/commands/codewiki/prompts.rs:305-313]
  - Signature: `pub struct SymbolSummary {`
  - Purpose: Indexed class `SymbolSummary` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:305-313]
- `ChildSummary` (class) component `ChildSummary [class]` (`af4e65d0-4a20-5d50-9a6a-2667f612315b`) lines 316-319 [crates/gcode/src/commands/codewiki/prompts.rs:316-319]
  - Signature: `pub struct ChildSummary {`
  - Purpose: Indexed class `ChildSummary` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:316-319]
- `SourceExcerpt` (class) component `SourceExcerpt [class]` (`25cbf9d8-d3b6-5695-8acb-2dc9c26e96dd`) lines 324-329 [crates/gcode/src/commands/codewiki/prompts.rs:324-329]
  - Signature: `pub struct SourceExcerpt {`
  - Purpose: Indexed class `SourceExcerpt` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:324-329]
- `oversized_child` (function) component `oversized_child [function]` (`75a4637a-ecc5-57c6-8fa5-c0f024e10a86`) lines 335-344 [crates/gcode/src/commands/codewiki/prompts.rs:335-344]
  - Signature: `fn oversized_child(name: &str) -> ChildSummary {`
  - Purpose: Indexed function `oversized_child` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:335-344]
- `aggregate_prompts_bound_each_child_summary` (function) component `aggregate_prompts_bound_each_child_summary [function]` (`af887455-a30d-5386-92ca-530471da959c`) lines 347-367 [crates/gcode/src/commands/codewiki/prompts.rs:347-367]
  - Signature: `fn aggregate_prompts_bound_each_child_summary() {`
  - Purpose: Indexed function `aggregate_prompts_bound_each_child_summary` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:347-367]
- `short_summaries_pass_through_untruncated` (function) component `short_summaries_pass_through_untruncated [function]` (`15e8a6d0-30dd-5fb6-a46f-b75cfc35f5e5`) lines 370-377 [crates/gcode/src/commands/codewiki/prompts.rs:370-377]
  - Signature: `fn short_summaries_pass_through_untruncated() {`
  - Purpose: Indexed function `short_summaries_pass_through_untruncated` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:370-377]
- `excerpt_flattens_multiline_summaries_to_one_line` (function) component `excerpt_flattens_multiline_summaries_to_one_line [function]` (`f14a8715-0b36-5471-951d-1822b02438dc`) lines 380-387 [crates/gcode/src/commands/codewiki/prompts.rs:380-387]
  - Signature: `fn excerpt_flattens_multiline_summaries_to_one_line() {`
  - Purpose: Indexed function `excerpt_flattens_multiline_summaries_to_one_line` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:380-387]
- `excerpt` (function) component `excerpt [function]` (`1ae6bee1-316e-5845-99d4-d09c22b2bcaf`) lines 389-396 [crates/gcode/src/commands/codewiki/prompts.rs:389-396]
  - Signature: `fn excerpt(path: &str, content: &str) -> SourceExcerpt {`
  - Purpose: Indexed function `excerpt` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:389-396]
- `aggregate_prompts_embed_bounded_source_excerpts` (function) component `aggregate_prompts_embed_bounded_source_excerpts [function]` (`2db0c47a-ba90-5c4d-891b-cafc1cfce3a6`) lines 399-423 [crates/gcode/src/commands/codewiki/prompts.rs:399-423]
  - Signature: `fn aggregate_prompts_embed_bounded_source_excerpts() {`
  - Purpose: Indexed function `aggregate_prompts_embed_bounded_source_excerpts` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:399-423]
- `prompts_without_excerpts_state_their_absence` (function) component `prompts_without_excerpts_state_their_absence [function]` (`c1ef3246-2ce7-5af8-ba82-9d7eaf9889d4`) lines 426-429 [crates/gcode/src/commands/codewiki/prompts.rs:426-429]
  - Signature: `fn prompts_without_excerpts_state_their_absence() {`
  - Purpose: Indexed function `prompts_without_excerpts_state_their_absence` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:426-429]
- `content_file_prompt_carries_leading_content` (function) component `content_file_prompt_carries_leading_content [function]` (`825a9d98-c7fb-59ac-970d-9f938ce31f7f`) lines 432-440 [crates/gcode/src/commands/codewiki/prompts.rs:432-440]
  - Signature: `fn content_file_prompt_carries_leading_content() {`
  - Purpose: Indexed function `content_file_prompt_carries_leading_content` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:432-440]
- `architecture_narrative_prompt_lists_subsystems_and_edges` (function) component `architecture_narrative_prompt_lists_subsystems_and_edges [function]` (`ade564ae-5574-560e-96f2-c30bc2162257`) lines 443-463 [crates/gcode/src/commands/codewiki/prompts.rs:443-463]
  - Signature: `fn architecture_narrative_prompt_lists_subsystems_and_edges() {`
  - Purpose: Indexed function `architecture_narrative_prompt_lists_subsystems_and_edges` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:443-463]

