---
title: crates/gcode/src/commands/codewiki/prompts.rs
type: code_file
provenance:
- file: crates/gcode/src/commands/codewiki/prompts.rs
  ranges:
  - 11-33
  - 35-56
  - 58-72
  - 74-104
  - 106-120
  - 122-133
  - 135-174
  - 185-203
  - 206-214
  - 217-220
  - 226-235
  - 238-258
  - 261-268
  - 271-278
generated_by: gcode-codewiki
trust: generated
freshness: indexed
---

# crates/gcode/src/commands/codewiki/prompts.rs

Module: [[code/modules/crates/gcode/src/commands/codewiki|crates/gcode/src/commands/codewiki]]

## Purpose

`crates/gcode/src/commands/codewiki/prompts.rs` exposes 14 indexed API symbols.
[crates/gcode/src/commands/codewiki/prompts.rs:11-33]
[crates/gcode/src/commands/codewiki/prompts.rs:35-56]
[crates/gcode/src/commands/codewiki/prompts.rs:58-72]
[crates/gcode/src/commands/codewiki/prompts.rs:74-104]
[crates/gcode/src/commands/codewiki/prompts.rs:106-120]

## API Symbols

- `symbol_prompt` (function) component `symbol_prompt [function]` (`5a65fb56-e981-5cfb-8db9-cd7603f94ad6`) lines 11-33 [crates/gcode/src/commands/codewiki/prompts.rs:11-33]
  - Signature: `pub fn symbol_prompt(symbol: &Symbol) -> String {`
  - Purpose: Builds a formatted prompt string containing a Symbol's file path, qualified name, kind, line range, and optionally appends its signature and docstring if present. [crates/gcode/src/commands/codewiki/prompts.rs:11-33]
- `file_prompt` (function) component `file_prompt [function]` (`b981c250-dd67-5629-abce-4ec63966c980`) lines 35-56 [crates/gcode/src/commands/codewiki/prompts.rs:35-56]
  - Signature: `pub fn file_prompt(file: &str, symbols: &[SymbolSummary]) -> String {`
  - Purpose: Constructs a structured text prompt for file summarization by formatting AST symbol metadata (name, kind, component ID, line range, purpose) or a placeholder if no symbols are indexed. [crates/gcode/src/commands/codewiki/prompts.rs:35-56]
- `module_prompt` (function) component `module_prompt [function]` (`bf0e4e18-e0c4-5300-b1bd-ea69e9c727ee`) lines 58-72 [crates/gcode/src/commands/codewiki/prompts.rs:58-72]
  - Signature: `pub fn module_prompt(`
  - Purpose: Constructs a prompt string that directs the summarization of a module by aggregating lower-level file summaries, submodule summaries, and component data. [crates/gcode/src/commands/codewiki/prompts.rs:58-72]
- `repo_prompt` (function) component `repo_prompt [function]` (`8eda5041-f84d-5eca-a8a6-b5bdb51d0190`) lines 74-104 [crates/gcode/src/commands/codewiki/prompts.rs:74-104]
  - Signature: `pub fn repo_prompt(modules: &[ChildSummary], files: &[ChildSummary]) -> String {`
  - Purpose: Builds a formatted string prompt for repository summarization by concatenating module and root file names with truncated summary excerpts. [crates/gcode/src/commands/codewiki/prompts.rs:74-104]
- `architecture_prompt` (function) component `architecture_prompt [function]` (`441bdb33-45ca-527f-86e3-e6d5d11f74f0`) lines 106-120 [crates/gcode/src/commands/codewiki/prompts.rs:106-120]
  - Signature: `pub fn architecture_prompt(`
  - Purpose: Generates a prompt string for summarizing a subsystem's architectural responsibility by composing its constituent files, modules, and components into an entity prompt. [crates/gcode/src/commands/codewiki/prompts.rs:106-120]
- `build_entity_prompt` (function) component `build_entity_prompt [function]` (`1ab7ed3d-0df5-57e0-9520-59134c434eed`) lines 122-133 [crates/gcode/src/commands/codewiki/prompts.rs:122-133]
  - Signature: `fn build_entity_prompt(`
  - Purpose: Constructs a formatted prompt string by concatenating a header, labeled entity, and organized child summary sections for files, modules, and components. [crates/gcode/src/commands/codewiki/prompts.rs:122-133]
- `append_child_summary_sections` (function) component `append_child_summary_sections [function]` (`6aea097f-ce69-50e5-a917-bdbeeede369e`) lines 135-174 [crates/gcode/src/commands/codewiki/prompts.rs:135-174]
  - Signature: `fn append_child_summary_sections(`
  - Purpose: Appends formatted sections describing child files, child modules, and component IDs to a mutable prompt string, with fallback messages for empty collections. [crates/gcode/src/commands/codewiki/prompts.rs:135-174]
- `summary_excerpt` (function) component `summary_excerpt [function]` (`51a64357-9d9e-53ce-874a-c2ea4fae8cd7`) lines 185-203 [crates/gcode/src/commands/codewiki/prompts.rs:185-203]
  - Signature: `fn summary_excerpt(summary: &str) -> String {`
  - Purpose: Extracts the first paragraph from a summary string, normalizes internal whitespace, and truncates it to `CHILD_SUMMARY_EXCERPT_MAX_CHARS` characters with an ellipsis suffix. [crates/gcode/src/commands/codewiki/prompts.rs:185-203]
- `SymbolSummary` (class) component `SymbolSummary [class]` (`396a2812-2b79-5a16-9138-b288c87aad5e`) lines 206-214 [crates/gcode/src/commands/codewiki/prompts.rs:206-214]
  - Signature: `pub struct SymbolSummary {`
  - Purpose: SymbolSummary is a metadata struct that aggregates information about a code symbol, including its name, kind, associated component, source line range, and functional purpose. [crates/gcode/src/commands/codewiki/prompts.rs:206-214]
- `ChildSummary` (class) component `ChildSummary [class]` (`3ff9fd49-308b-54ef-8976-f7557d063d10`) lines 217-220 [crates/gcode/src/commands/codewiki/prompts.rs:217-220]
  - Signature: `pub struct ChildSummary {`
  - Purpose: `ChildSummary` is a public Rust struct containing two `String` fields (`name` and `summary`) that serves as a lightweight data container for representing a named summary of a child entity. [crates/gcode/src/commands/codewiki/prompts.rs:217-220]
- `oversized_child` (function) component `oversized_child [function]` (`2571a12a-6af1-5dd8-b02a-fd80cfd7d84f`) lines 226-235 [crates/gcode/src/commands/codewiki/prompts.rs:226-235]
  - Signature: `fn oversized_child(name: &str) -> ChildSummary {`
  - Purpose: Creates a `ChildSummary` struct with the provided name and a summary string consisting of a single sentence followed by 2,000 newline-separated citation references formatted as `[src/lib.rs:{line_number}]`. [crates/gcode/src/commands/codewiki/prompts.rs:226-235]
- `aggregate_prompts_bound_each_child_summary` (function) component `aggregate_prompts_bound_each_child_summary [function]` (`4c70f6e7-e138-54ff-842c-34fb8a146dbe`) lines 238-258 [crates/gcode/src/commands/codewiki/prompts.rs:238-258]
  - Signature: `fn aggregate_prompts_bound_each_child_summary() {`
  - Purpose: Tests that aggregated prompts containing oversized child module summaries enforce character-length bounds on summary excerpt lines and mark truncations with ellipses. [crates/gcode/src/commands/codewiki/prompts.rs:238-258]
- `short_summaries_pass_through_untruncated` (function) component `short_summaries_pass_through_untruncated [function]` (`37e6dcd9-0f7b-5fb7-b5cc-a41bd81f6b2d`) lines 261-268 [crates/gcode/src/commands/codewiki/prompts.rs:261-268]
  - Signature: `fn short_summaries_pass_through_untruncated() {`
  - Purpose: This test verifies that `module_prompt()` passes through short child summaries untruncated with proper list formatting. [crates/gcode/src/commands/codewiki/prompts.rs:261-268]
- `excerpt_flattens_multiline_summaries_to_one_line` (function) component `excerpt_flattens_multiline_summaries_to_one_line [function]` (`6aeb065d-23a7-5f06-98aa-7c3be58f5d36`) lines 271-278 [crates/gcode/src/commands/codewiki/prompts.rs:271-278]
  - Signature: `fn excerpt_flattens_multiline_summaries_to_one_line() {`
  - Purpose: Tests that `module_prompt` flattens multiline child summaries to single-line text by replacing embedded newlines with spaces. [crates/gcode/src/commands/codewiki/prompts.rs:271-278]

