---
title: crates/gcode/src/commands/codewiki/prompts.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/prompts.rs
  ranges:
  - 16-38
  - 40-73
  - 78-83
  - 85-101
  - 103-126
  - 128-136
  - 138-143
  - 145-149
  - 151-167
  - 171-199
  - 202-217
  - 219-242
  - 244-259
  - 278-298
  - 302-316
  - 319-327
  - 330-333
  - 338-343
  - 349-358
  - 361-381
  - 384-391
  - 394-405
  - 408-417
  - 420-435
  - 438-453
  - 455-462
  - 465-489
  - 492-495
  - 498-506
  - 509-529
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

<details>
<summary>Relevant source files</summary>

- [crates/gcode/src/commands/codewiki/prompts.rs:16-38](crates/gcode/src/commands/codewiki/prompts.rs#L16-L38), [crates/gcode/src/commands/codewiki/prompts.rs:40-73](crates/gcode/src/commands/codewiki/prompts.rs#L40-L73), [crates/gcode/src/commands/codewiki/prompts.rs:78-83](crates/gcode/src/commands/codewiki/prompts.rs#L78-L83), [crates/gcode/src/commands/codewiki/prompts.rs:85-101](crates/gcode/src/commands/codewiki/prompts.rs#L85-L101), [crates/gcode/src/commands/codewiki/prompts.rs:103-126](crates/gcode/src/commands/codewiki/prompts.rs#L103-L126), [crates/gcode/src/commands/codewiki/prompts.rs:128-136](crates/gcode/src/commands/codewiki/prompts.rs#L128-L136), [crates/gcode/src/commands/codewiki/prompts.rs:138-143](crates/gcode/src/commands/codewiki/prompts.rs#L138-L143), [crates/gcode/src/commands/codewiki/prompts.rs:145-149](crates/gcode/src/commands/codewiki/prompts.rs#L145-L149), [crates/gcode/src/commands/codewiki/prompts.rs:151-167](crates/gcode/src/commands/codewiki/prompts.rs#L151-L167), [crates/gcode/src/commands/codewiki/prompts.rs:171-199](crates/gcode/src/commands/codewiki/prompts.rs#L171-L199), [crates/gcode/src/commands/codewiki/prompts.rs:202-217](crates/gcode/src/commands/codewiki/prompts.rs#L202-L217), [crates/gcode/src/commands/codewiki/prompts.rs:219-242](crates/gcode/src/commands/codewiki/prompts.rs#L219-L242), [crates/gcode/src/commands/codewiki/prompts.rs:244-259](crates/gcode/src/commands/codewiki/prompts.rs#L244-L259), [crates/gcode/src/commands/codewiki/prompts.rs:278-298](crates/gcode/src/commands/codewiki/prompts.rs#L278-L298), [crates/gcode/src/commands/codewiki/prompts.rs:302-316](crates/gcode/src/commands/codewiki/prompts.rs#L302-L316), [crates/gcode/src/commands/codewiki/prompts.rs:319-327](crates/gcode/src/commands/codewiki/prompts.rs#L319-L327), [crates/gcode/src/commands/codewiki/prompts.rs:330-333](crates/gcode/src/commands/codewiki/prompts.rs#L330-L333), [crates/gcode/src/commands/codewiki/prompts.rs:338-343](crates/gcode/src/commands/codewiki/prompts.rs#L338-L343), [crates/gcode/src/commands/codewiki/prompts.rs:349-358](crates/gcode/src/commands/codewiki/prompts.rs#L349-L358), [crates/gcode/src/commands/codewiki/prompts.rs:361-381](crates/gcode/src/commands/codewiki/prompts.rs#L361-L381), [crates/gcode/src/commands/codewiki/prompts.rs:384-391](crates/gcode/src/commands/codewiki/prompts.rs#L384-L391), [crates/gcode/src/commands/codewiki/prompts.rs:394-405](crates/gcode/src/commands/codewiki/prompts.rs#L394-L405), [crates/gcode/src/commands/codewiki/prompts.rs:408-417](crates/gcode/src/commands/codewiki/prompts.rs#L408-L417), [crates/gcode/src/commands/codewiki/prompts.rs:420-435](crates/gcode/src/commands/codewiki/prompts.rs#L420-L435), [crates/gcode/src/commands/codewiki/prompts.rs:438-453](crates/gcode/src/commands/codewiki/prompts.rs#L438-L453), [crates/gcode/src/commands/codewiki/prompts.rs:455-462](crates/gcode/src/commands/codewiki/prompts.rs#L455-L462), [crates/gcode/src/commands/codewiki/prompts.rs:465-489](crates/gcode/src/commands/codewiki/prompts.rs#L465-L489), [crates/gcode/src/commands/codewiki/prompts.rs:492-495](crates/gcode/src/commands/codewiki/prompts.rs#L492-L495), [crates/gcode/src/commands/codewiki/prompts.rs:498-506](crates/gcode/src/commands/codewiki/prompts.rs#L498-L506), [crates/gcode/src/commands/codewiki/prompts.rs:509-529](crates/gcode/src/commands/codewiki/prompts.rs#L509-L529)

</details>

# crates/gcode/src/commands/codewiki/prompts.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

This file defines the prompt-building machinery for the `codewiki` documentation pipeline. It provides system prompt constants and a set of constructors for symbol, file, content-file, module, repository, architecture, and narrative-architecture prompts, all assembled from symbol summaries, child summaries, source excerpts, and markdown tables. The helper functions and small data types (`SymbolSummary`, `ChildSummary`, `SourceExcerpt`) support that assembly by formatting summaries, bounding excerpts, deciding when to truncate, and appending tables or guidance so each prompt carries the right evidence for the requested documentation level.
[crates/gcode/src/commands/codewiki/prompts.rs:16-38]
[crates/gcode/src/commands/codewiki/prompts.rs:40-73]
[crates/gcode/src/commands/codewiki/prompts.rs:78-83]
[crates/gcode/src/commands/codewiki/prompts.rs:85-101]
[crates/gcode/src/commands/codewiki/prompts.rs:103-126]

## API Symbols

| Symbol | Kind | Signature | Component | Component ID | Lines | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| `symbol_prompt` | function | `pub fn symbol_prompt(symbol: &Symbol) -> String {` | `symbol_prompt [function]` | `6048e940-59ad-5974-bdfd-91ece5bc6ec5` | 16-38 [crates/gcode/src/commands/codewiki/prompts.rs:16-38] | Indexed function `symbol_prompt` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:16-38] |
| `file_prompt` | function | `pub fn file_prompt(file: &str, symbols: &[SymbolSummary], sources: &[SourceExcerpt]) -> String {` | `file_prompt [function]` | `e64dc13f-e538-5327-9ea2-3d4e4dc47ef3` | 40-73 [crates/gcode/src/commands/codewiki/prompts.rs:40-73] | Indexed function `file_prompt` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:40-73] |
| `content_file_prompt` | function | `pub fn content_file_prompt(file: &str, source: &SourceExcerpt) -> String {` | `content_file_prompt [function]` | `b3b7827b-0f31-5a4d-b399-41b686526fa6` | 78-83 [crates/gcode/src/commands/codewiki/prompts.rs:78-83] | Indexed function `content_file_prompt` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:78-83] |
| `module_prompt` | function | `pub fn module_prompt(` | `module_prompt [function]` | `fb0c4554-b915-58a5-951c-bbbde2a8e9d8` | 85-101 [crates/gcode/src/commands/codewiki/prompts.rs:85-101] | Indexed function `module_prompt` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:85-101] |
| `repo_prompt` | function | `pub fn repo_prompt(` | `repo_prompt [function]` | `30eccb94-792f-5c82-9725-15c4f570615c` | 103-126 [crates/gcode/src/commands/codewiki/prompts.rs:103-126] | Indexed function `repo_prompt` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:103-126] |
| `append_child_summary_table` | function | `fn append_child_summary_table(prompt: &mut String, headers: &[&str], children: &[ChildSummary]) {` | `append_child_summary_table [function]` | `80c99d77-1b4a-52a2-9659-cf79005ee699` | 128-136 [crates/gcode/src/commands/codewiki/prompts.rs:128-136] | Indexed function `append_child_summary_table` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:128-136] |
| `append_component_table` | function | `fn append_component_table(prompt: &mut String, components: &[String]) {` | `append_component_table [function]` | `1f9d1a4a-ea17-59c5-94c5-9b71c7bf407f` | 138-143 [crates/gcode/src/commands/codewiki/prompts.rs:138-143] | Indexed function `append_component_table` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:138-143] |
| `append_table_guidance` | function | `fn append_table_guidance(prompt: &mut String) {` | `append_table_guidance [function]` | `be94f45c-95dd-5b63-95db-06980fa0c11d` | 145-149 [crates/gcode/src/commands/codewiki/prompts.rs:145-149] | Indexed function `append_table_guidance` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:145-149] |
| `architecture_prompt` | function | `pub fn architecture_prompt(` | `architecture_prompt [function]` | `047e492c-90ed-5492-a7ea-1e99091e36de` | 151-167 [crates/gcode/src/commands/codewiki/prompts.rs:151-167] | Indexed function `architecture_prompt` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:151-167] |
| `architecture_narrative_prompt` | function | `pub fn architecture_narrative_prompt(` | `architecture_narrative_prompt [function]` | `2eb7b14b-48e3-5c41-b153-3516a2f39d10` | 171-199 [crates/gcode/src/commands/codewiki/prompts.rs:171-199] | Indexed function `architecture_narrative_prompt` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:171-199] |
| `build_entity_prompt` | function | `fn build_entity_prompt(` | `build_entity_prompt [function]` | `1fcab931-17a3-502a-b105-265a65be2a28` | 202-217 [crates/gcode/src/commands/codewiki/prompts.rs:202-217] | Indexed function `build_entity_prompt` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:202-217] |
| `append_child_summary_sections` | function | `fn append_child_summary_sections(` | `append_child_summary_sections [function]` | `40a43cdc-b3ca-57db-8abc-d94537b7fa68` | 219-242 [crates/gcode/src/commands/codewiki/prompts.rs:219-242] | Indexed function `append_child_summary_sections` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:219-242] |
| `append_source_excerpt_section` | function | `fn append_source_excerpt_section(prompt: &mut String, sources: &[SourceExcerpt]) {` | `append_source_excerpt_section [function]` | `58d9ebf2-b2ef-5497-9c7f-36ee6136806d` | 244-259 [crates/gcode/src/commands/codewiki/prompts.rs:244-259] | Indexed function `append_source_excerpt_section` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:244-259] |
| `summary_excerpt` | function | `fn summary_excerpt(summary: &str) -> String {` | `summary_excerpt [function]` | `f2b3375f-e276-5c5b-b3d5-423f5baf6df7` | 278-298 [crates/gcode/src/commands/codewiki/prompts.rs:278-298] | Indexed function `summary_excerpt` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:278-298] |
| `bounded_excerpt` | function | `fn bounded_excerpt(excerpt: &str) -> String {` | `bounded_excerpt [function]` | `5079b3f1-ad69-5290-9b5b-7f0e24d34b93` | 302-316 [crates/gcode/src/commands/codewiki/prompts.rs:302-316] | Indexed function `bounded_excerpt` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:302-316] |
| `SymbolSummary` | class | `pub struct SymbolSummary {` | `SymbolSummary [class]` | `dd72a50e-0b23-5300-9469-a908a47a7c67` | 319-327 [crates/gcode/src/commands/codewiki/prompts.rs:319-327] | Indexed class `SymbolSummary` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:319-327] |
| `ChildSummary` | class | `pub struct ChildSummary {` | `ChildSummary [class]` | `6115a0aa-3b5f-5aed-8f02-d7274348664d` | 330-333 [crates/gcode/src/commands/codewiki/prompts.rs:330-333] | Indexed class `ChildSummary` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:330-333] |
| `SourceExcerpt` | class | `pub struct SourceExcerpt {` | `SourceExcerpt [class]` | `b2dd376c-9457-59f0-adf4-0a3cd4eb1d4c` | 338-343 [crates/gcode/src/commands/codewiki/prompts.rs:338-343] | Indexed class `SourceExcerpt` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:338-343] |
| `oversized_child` | function | `fn oversized_child(name: &str) -> ChildSummary {` | `oversized_child [function]` | `f0eb634e-c598-51c0-b9dc-e8e0e06b3b05` | 349-358 [crates/gcode/src/commands/codewiki/prompts.rs:349-358] | Indexed function `oversized_child` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:349-358] |
| `aggregate_prompts_bound_each_child_summary` | function | `fn aggregate_prompts_bound_each_child_summary() {` | `aggregate_prompts_bound_each_child_summary [function]` | `7b339d92-cfc2-5e07-98c5-5b32f39af3c5` | 361-381 [crates/gcode/src/commands/codewiki/prompts.rs:361-381] | Indexed function `aggregate_prompts_bound_each_child_summary` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:361-381] |
| `short_summaries_pass_through_untruncated` | function | `fn short_summaries_pass_through_untruncated() {` | `short_summaries_pass_through_untruncated [function]` | `06300c20-dad3-58e5-880c-603c3f0c703b` | 384-391 [crates/gcode/src/commands/codewiki/prompts.rs:384-391] | Indexed function `short_summaries_pass_through_untruncated` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:384-391] |
| `summary_excerpt_includes_ellipsis_inside_hard_cap` | function | `fn summary_excerpt_includes_ellipsis_inside_hard_cap() {` | `summary_excerpt_includes_ellipsis_inside_hard_cap [function]` | `bc702a28-abb8-5eaa-b173-33c6d41688fe` | 394-405 [crates/gcode/src/commands/codewiki/prompts.rs:394-405] | Indexed function `summary_excerpt_includes_ellipsis_inside_hard_cap` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:394-405] |
| `excerpt_flattens_multiline_summaries_to_one_line` | function | `fn excerpt_flattens_multiline_summaries_to_one_line() {` | `excerpt_flattens_multiline_summaries_to_one_line [function]` | `c41994dc-5a5d-5d9f-bd71-35870ad20ff7` | 408-417 [crates/gcode/src/commands/codewiki/prompts.rs:408-417] | Indexed function `excerpt_flattens_multiline_summaries_to_one_line` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:408-417] |
| `aggregate_prompts_request_tables_for_enumerable_facts` | function | `fn aggregate_prompts_request_tables_for_enumerable_facts() {` | `aggregate_prompts_request_tables_for_enumerable_facts [function]` | `31414d68-8b6b-5197-a4c2-e5b436f6c60b` | 420-435 [crates/gcode/src/commands/codewiki/prompts.rs:420-435] | Indexed function `aggregate_prompts_request_tables_for_enumerable_facts` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:420-435] |
| `file_prompt_lists_symbols_as_markdown_table` | function | `fn file_prompt_lists_symbols_as_markdown_table() {` | `file_prompt_lists_symbols_as_markdown_table [function]` | `66c3b8ee-7aa6-5fc3-892f-337e6004c351` | 438-453 [crates/gcode/src/commands/codewiki/prompts.rs:438-453] | Indexed function `file_prompt_lists_symbols_as_markdown_table` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:438-453] |
| `excerpt` | function | `fn excerpt(path: &str, content: &str) -> SourceExcerpt {` | `excerpt [function]` | `98d66e9f-9d23-5538-8bbb-922c4a8bbfa3` | 455-462 [crates/gcode/src/commands/codewiki/prompts.rs:455-462] | Indexed function `excerpt` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:455-462] |
| `aggregate_prompts_embed_bounded_source_excerpts` | function | `fn aggregate_prompts_embed_bounded_source_excerpts() {` | `aggregate_prompts_embed_bounded_source_excerpts [function]` | `72792fb0-4574-5215-8121-b61ce5fef5aa` | 465-489 [crates/gcode/src/commands/codewiki/prompts.rs:465-489] | Indexed function `aggregate_prompts_embed_bounded_source_excerpts` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:465-489] |
| `prompts_without_excerpts_state_their_absence` | function | `fn prompts_without_excerpts_state_their_absence() {` | `prompts_without_excerpts_state_their_absence [function]` | `660df2a0-1202-591e-896f-e8e9513729e9` | 492-495 [crates/gcode/src/commands/codewiki/prompts.rs:492-495] | Indexed function `prompts_without_excerpts_state_their_absence` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:492-495] |
| `content_file_prompt_carries_leading_content` | function | `fn content_file_prompt_carries_leading_content() {` | `content_file_prompt_carries_leading_content [function]` | `d0f8076b-b4fc-5ffc-b407-1c3a8939589b` | 498-506 [crates/gcode/src/commands/codewiki/prompts.rs:498-506] | Indexed function `content_file_prompt_carries_leading_content` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:498-506] |
| `architecture_narrative_prompt_lists_subsystems_and_edges` | function | `fn architecture_narrative_prompt_lists_subsystems_and_edges() {` | `architecture_narrative_prompt_lists_subsystems_and_edges [function]` | `13e12ca3-9cf4-5673-93c5-744b43b429de` | 509-529 [crates/gcode/src/commands/codewiki/prompts.rs:509-529] | Indexed function `architecture_narrative_prompt_lists_subsystems_and_edges` in `crates/gcode/src/commands/codewiki/prompts.rs`. [crates/gcode/src/commands/codewiki/prompts.rs:509-529] |
